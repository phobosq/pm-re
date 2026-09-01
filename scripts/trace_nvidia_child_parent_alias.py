#!/usr/bin/env python3
from pathlib import Path
import argparse,bisect
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_REG,X86_OP_MEM

CTOR=0x001D4A80

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en: funcs.append((b,en))
 funcs=sorted(set(funcs));starts=[b for b,_ in funcs]
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 j=bisect.bisect_right(starts,CTOR)-1;b,en=funcs[j];arr=list(md.disasm(pe.get_data(b,en-b),base+b))
 aliases={'r8'}; stores=[]
 for idx,i in enumerate(arr):
  if i.mnemonic=='mov' and len(i.operands)==2:
   dst,src=i.operands
   if dst.type==X86_OP_REG:
    dn=i.reg_name(dst.reg)
    if src.type==X86_OP_REG and i.reg_name(src.reg) in aliases: aliases.add(dn)
    elif dn in aliases and dn!='r8': aliases.discard(dn)
   if dst.type==X86_OP_MEM and src.type==X86_OP_REG and i.reg_name(src.reg) in aliases:
    stores.append((idx,i,dst.mem.disp,i.reg_name(dst.mem.base) if dst.mem.base else ''))
 lines=['# NVIDIA child retention of Type2+8 (ctor R8)','',
        'Type2 ctor passes `R8 = parent + 8` into child ctor 0x1D4A80.','',
        f'Explicit stores of an R8-derived alias: `{len(stores)}`','']
 for idx,i,d,bb in stores:
  lines += [f'## store at `0x{i.address-base:08X}` base `{bb}` disp `0x{d:X}`','','```asm']
  for z in arr[max(0,idx-12):min(len(arr),idx+12)]:lines.append(f'0x{z.address-base:08X}: {z.mnemonic} {z.op_str}'.rstrip())
  lines += ['```','']
 # If stored into child this field, find all reads of that displacement in NVIDIA child region.
 child_fields=sorted({d for _,_,d,bb in stores if bb in ('rbx','rdi','rcx') and 0<=d<0x1000})
 lines += ['## Candidate retained-parent fields','',', '.join(f'`+0x{x:X}`' for x in child_fields) or '_none_','']
 if child_fields:
  begin=0x001D4A80;end=0x001F1000
  scan=list(md.disasm(pe.get_data(begin,end-begin),base+begin))
  for f in child_fields:
   lines += [f'### References to child field `+0x{f:X}`','']
   for idx,i in enumerate(scan):
    for op in i.operands:
     if op.type==X86_OP_MEM and op.mem.disp==f and op.mem.base:
      bn=i.reg_name(op.mem.base)
      if bn in ('rsp','rbp','rip'):continue
      lines.append(f'- `0x{i.address-base:08X}: {i.mnemonic} {i.op_str}`')
      break
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'nvidia_child_parent_alias.md').write_text('\n'.join(lines),encoding='utf-8');print('stores',len(stores),child_fields)
if __name__=='__main__':main()
