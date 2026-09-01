#!/usr/bin/env python3
"""Trace direct callers of 0xAA6E0 and RCX provenance before each call.
Static only.
"""
from __future__ import annotations
import argparse,bisect
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_IMM
TARGET=0x000AA6E0
def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en:funcs.append((b,en))
 funcs.sort();starts=[b for b,_ in funcs]
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 hits=[]
 for fn in funcs:
  arr=list(md.disasm(pe.get_data(fn[0],fn[1]-fn[0]),base+fn[0]))
  for k,i in enumerate(arr):
   if i.mnemonic=='call' and i.operands and i.operands[0].type==X86_OP_IMM and i.operands[0].imm-base==TARGET:hits.append((fn,arr,k))
 lines=['# Callers of 0xAA6E0','',f'direct callers: {len(hits)}','']
 for fn,arr,k in hits:
  i=arr[k];lines += [f'## call `0x{i.address-base:08X}` in `0x{fn[0]:08X}..0x{fn[1]:08X}`','','```asm']
  for w in arr[max(0,k-70):min(len(arr),k+25)]:lines.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
  lines += ['```','','### Backward RCX-related assignments','']
  n=0
  for w in reversed(arr[max(0,k-180):k]):
   s=(w.mnemonic+' '+w.op_str).lower()
   if 'rcx' in s:
    lines.append(f'- `0x{w.address-base:08X}: {w.mnemonic} {w.op_str}`');n+=1
    if n>=24:break
  lines += ['']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'aa6e0_callers.md';p.write_text('\n'.join(lines),encoding='utf-8');print('callers',len(hits))
if __name__=='__main__':main()
