#!/usr/bin/env python3
from pathlib import Path
import argparse,bisect
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_REG,X86_OP_IMM,X86_OP_MEM

TARGET=0x001D4A80

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en:funcs.append((b,en))
 funcs=sorted(set(funcs));starts=[b for b,_ in funcs]
 j=bisect.bisect_right(starts,TARGET)-1;b,en=funcs[j]
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 arr=list(md.disasm(pe.get_data(b,en-b),base+b))
 aliases={'rcx'}; events=[]
 for idx,i in enumerate(arr):
  # track child-this aliases conservatively
  if i.mnemonic in ('mov','lea') and len(i.operands)==2 and i.operands[0].type==X86_OP_REG:
   dst=i.reg_name(i.operands[0].reg);src=i.operands[1]
   if src.type==X86_OP_REG and i.reg_name(src.reg) in aliases: aliases.add(dst)
   elif dst in aliases and dst!='rcx': aliases.discard(dst)
  if i.mnemonic=='call':
   # snapshot last ~10 instructions and flag if an alias is placed in RCX/RDX/R8/R9 or memory
   recent=arr[max(0,idx-12):idx]
   evidence=[]
   for z in recent:
    for op in z.operands:
     if op.type==X86_OP_REG and z.reg_name(op.reg) in aliases: evidence.append(f'0x{z.address-base:08X}: {z.mnemonic} {z.op_str}')
   op=i.operands[0] if i.operands else None
   target=f'0x{op.imm-base:08X}' if op and op.type==X86_OP_IMM else i.op_str
   if evidence: events.append((idx,target,evidence[-6:]))
 lines=['# NVIDIA child ctor registration / this escapes','',f'Ctor PDATA `0x{b:08X}..0x{en:08X}`. Tracks child `this` aliases reaching calls.','',f'events: `{len(events)}`','']
 for idx,target,evid in events:
  i=arr[idx];lines += [f'## call `0x{i.address-base:08X}` -> `{target}`','','Recent child-this evidence:','']
  for x in evid:lines.append(f'- `{x}`')
  lines += ['','```asm']
  for z in arr[max(0,idx-12):min(len(arr),idx+10)]:lines.append(f'0x{z.address-base:08X}: {z.mnemonic} {z.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'nvidia_child_registration.md').write_text('\n'.join(lines),encoding='utf-8');print('events',len(events))
if __name__=='__main__':main()
