#!/usr/bin/env python3
from pathlib import Path
import argparse,bisect
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_OP_REG,X86_OP_IMM
TARGETS=[0x001CF7C0,0x001CF8B0,0x001D0730,0x001CDFD0,0x001D0AD0,0x001CE0B0]
WATCH={0x368:'snapshotA_base',0x418:'vmr_A',0x440:'snapshotB_base',0x4F0:'vmr_B',0x838:'child'}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en:funcs.append((b,en))
 funcs=sorted(set(funcs));starts=[b for b,_ in funcs]
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 lines=['# Type2 NVIDIA vtable methods: type-safe VMR/snapshot scan','',
        'RCX is treated as `this`; simple register aliases are propagated.','']
 for tgt in TARGETS:
  j=bisect.bisect_right(starts,tgt)-1; fn=funcs[j]
  if not(fn[0]<=tgt<fn[1]):
   arr=list(md.disasm(pe.get_data(tgt,0x800),base+tgt)); fn=(tgt,tgt+0x800)
  else: arr=list(md.disasm(pe.get_data(fn[0],fn[1]-fn[0]),base+fn[0]))
  aliases={'rcx'};hits=[]
  for k,i in enumerate(arr):
   if i.mnemonic=='mov' and len(i.operands)==2 and i.operands[0].type==X86_OP_REG and i.operands[1].type==X86_OP_REG:
    d=i.reg_name(i.operands[0].reg);s=i.reg_name(i.operands[1].reg)
    if s in aliases: aliases.add(d)
   for op in i.operands:
    if op.type==X86_OP_MEM and op.mem.base:
     bn=i.reg_name(op.mem.base);d=op.mem.disp
     if bn in aliases and d in WATCH: hits.append((k,i,bn,d,WATCH[d]))
  lines += [f'## `0x{tgt:08X}` / PDATA `0x{fn[0]:08X}..0x{fn[1]:08X}`','',f'aliases: `{", ".join(sorted(aliases))}`',f'hits: `{len(hits)}`','']
  for k,i,bn,d,label in hits:
   lines += [f'### {label} at `0x{i.address-base:08X}`: `{i.mnemonic} {i.op_str}`','','```asm']
   for w in arr[max(0,k-25):min(len(arr),k+35)]: lines.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
   lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'type2_vtable_vmr_reads.md').write_text('\n'.join(lines),encoding='utf-8');print('done')
if __name__=='__main__':main()
