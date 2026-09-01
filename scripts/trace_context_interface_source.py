#!/usr/bin/env python3
"""Trace the original R8 argument passed into dispatcher 0x584A0.
That value is forwarded through derived factories into base this+0x90.
Static only.
"""
from __future__ import annotations
import argparse,bisect
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_IMM
TARGET=0x000584A0

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en:funcs.append((b,en))
 funcs.sort(); starts=[b for b,_ in funcs]
 def fnof(r):
  j=bisect.bisect_right(starts,r)-1
  return funcs[j] if j>=0 and funcs[j][0]<=r<funcs[j][1] else None
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 hits=[]
 for fn in funcs:
  arr=list(md.disasm(pe.get_data(fn[0],fn[1]-fn[0]),base+fn[0]))
  for k,i in enumerate(arr):
   if i.mnemonic=='call' and i.operands and i.operands[0].type==X86_OP_IMM and i.operands[0].imm-base==TARGET:
    hits.append((fn,arr,k))
 lines=['# Context interface source for dispatcher 0x584A0','',f'direct callers: {len(hits)}','']
 for fn,arr,k in hits:
  lines += [f'## call `0x{arr[k].address-base:08X}` in `0x{fn[0]:08X}..0x{fn[1]:08X}`','','```asm']
  for i in arr[max(0,k-28):min(len(arr),k+12)]:lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
  lines += ['```','','### Backward assignments mentioning r8','']
  found=0
  for i in reversed(arr[max(0,k-80):k]):
   s=(i.mnemonic+' '+i.op_str).lower()
   if 'r8' in s:
    lines.append(f'- `0x{i.address-base:08X}: {i.mnemonic} {i.op_str}`');found+=1
    if found>=12:break
  lines += ['']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'context_interface_source.md';p.write_text('\n'.join(lines),encoding='utf-8');print('callers',len(hits))
if __name__=='__main__':main()
