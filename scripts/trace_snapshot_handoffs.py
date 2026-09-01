#!/usr/bin/env python3
"""Inspect call-argument setup after per-GPU snapshot merge sites.
Static only; target binary is never executed.
"""
from __future__ import annotations
import argparse,bisect
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64

SITES=[
 (0x0006FCC2,'merge6_first'),(0x0006FCE0,'merge6_second'),
 (0x0007FD1D,'copyback7'),
 (0x000A92DF,'after_mergeA'),
 (0x000B24CB,'after_mergeB'),
]

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en: funcs.append((b,en))
 funcs.sort();starts=[b for b,_ in funcs]
 def fnof(r):
  j=bisect.bisect_right(starts,r)-1
  return funcs[j] if j>=0 and funcs[j][0]<=r<funcs[j][1] else None
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 lines=['# Snapshot handoff call contexts','']
 for rva,label in SITES:
  fn=fnof(rva)
  if not fn: continue
  b,en=fn;ins=list(md.disasm(pe.get_data(b,en-b),base+b))
  idx=min(range(len(ins)), key=lambda k:abs((ins[k].address-base)-rva))
  lines += [f'## {label} near `0x{rva:08X}` in `0x{b:08X}..0x{en:08X}`','','```asm']
  for i in ins[max(0,idx-22):min(len(ins),idx+30)]: lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'snapshot_handoffs.md').write_text('\n'.join(lines),encoding='utf-8')
 print(out/'snapshot_handoffs.md')
if __name__=='__main__':main()
