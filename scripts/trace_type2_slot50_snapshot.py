#!/usr/bin/env python3
"""Trace the full snapshot flow inside NVIDIA Type2 vtable slot +0x50 (0x1CF8B0).
Static only; target binary is never executed.
"""
from __future__ import annotations
import argparse,bisect
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_IMM,X86_OP_MEM
TARGET=0x001CF8B0
GETTER=0x00084A60

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en:funcs.append((b,en))
 funcs.sort();starts=[b for b,_ in funcs]
 j=bisect.bisect_right(starts,TARGET)-1;b,en=funcs[j]
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 arr=list(md.disasm(pe.get_data(b,en-b),base+b))
 lines=['# Type2 slot +0x50 snapshot flow','',f'PDATA `0x{b:08X}..0x{en:08X}`','',
        'Known snapshot getter: `0x00084A60`.','',
        '## Calls','','| RVA | target/form |','|---|---|']
 for i in arr:
  if i.mnemonic!='call':continue
  form=i.op_str
  if i.operands and i.operands[0].type==X86_OP_IMM:form=f'RVA 0x{i.operands[0].imm-base:08X}'
  lines.append(f'| `0x{i.address-base:08X}` | `{form}` |')
 lines += ['','## Stack/local memory accesses around snapshot-sized regions','','| RVA | instruction |','|---|---|']
 for i in arr:
  hit=False
  for op in i.operands:
   if op.type!=X86_OP_MEM:continue
   bn=i.reg_name(op.mem.base);d=op.mem.disp
   if bn in ('rsp','rbp') and -0x400<=d<=0x800:
    hit=True
  if hit:lines.append(f'| `0x{i.address-base:08X}` | `{i.mnemonic} {i.op_str}` |')
 lines += ['','## Full body','','```asm']
 for i in arr:lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
 lines += ['```']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'type2_slot50_snapshot.md').write_text('\n'.join(lines),encoding='utf-8')
if __name__=='__main__':main()
