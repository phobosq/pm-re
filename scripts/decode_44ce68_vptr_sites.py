#!/usr/bin/env python3
"""Decode code sites that reference candidate vtable 0x44CE68 and identify constructors/owners.
Static only; PhoenixMiner is never executed.
"""
from __future__ import annotations
import argparse,bisect
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_IMM,X86_OP_MEM,X86_REG_RIP
SITES=[0x0017BFEE,0x0017CA8D]
VT=0x0044CE68

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en:funcs.append((b,en))
 funcs.sort();starts=[b for b,_ in funcs]
 def fnof(r):
  j=bisect.bisect_right(starts,r)-1
  return funcs[j] if j>=0 and funcs[j][0]<=r<funcs[j][1] else (r-0x100,r+0x300)
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True;md.skipdata=True
 lines=['# Candidate vtable 0x0044CE68 ownership','']
 done=set()
 for site in SITES:
  b,en=fnof(site)
  if (b,en) in done:continue
  done.add((b,en));arr=[i for i in md.disasm(pe.get_data(b,en-b),base+b) if i.id!=0]
  lines += [f'## PDATA `0x{b:08X}..0x{en:08X}` contains vptr ref site `0x{site:08X}`','',
            '### Calls','','| RVA | target/form |','|---|---|']
  for i in arr:
   if i.mnemonic not in ('call','jmp'):continue
   f=i.op_str
   if i.operands and i.operands[0].type==X86_OP_IMM:f=f'RVA 0x{i.operands[0].imm-base:08X}'
   lines.append(f'| `0x{i.address-base:08X}` | `{i.mnemonic} {f}` |')
  lines += ['','### Full body','','```asm']
  for i in arr:
   tag=''
   for op in i.operands:
    if op.type==X86_OP_MEM and op.mem.base==X86_REG_RIP:
     rva=i.address+i.size+op.mem.disp-base
     if rva==VT:tag=' ; VTABLE_44CE68'
   lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}{tag}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'owner_44ce68_sites.md').write_text('\n'.join(lines),encoding='utf-8')
if __name__=='__main__':main()
