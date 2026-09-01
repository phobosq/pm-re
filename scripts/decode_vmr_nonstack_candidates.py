#!/usr/bin/env python3
"""Decode high-value non-stack candidates reading runtime-shaped +0x418/+0x4F0.
Static only. The binary is never executed.
"""
from __future__ import annotations
import argparse,bisect
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
TARGETS=[0x000A2870,0x000A45A0,0x000AA6E0]
ANCHORS={0x000A338D,0x000A33D7,0x000A55BA,0x000A5601,0x000AA762}
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
  return funcs[j] if j>=0 and funcs[j][0]<=r<funcs[j][1] else None
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 lines=['# Focused non-stack VMR-shaped candidates','']
 for t in TARGETS:
  fn=fnof(t) or next((x for x in funcs if x[0]==t),None)
  lines += [f'## PDATA `{("0x%08X..0x%08X"%fn) if fn else "none"}`','']
  if not fn:continue
  arr=list(md.disasm(pe.get_data(fn[0],fn[1]-fn[0]),base+fn[0]))
  for k,i in enumerate(arr):
   r=i.address-base
   if r in ANCHORS:
    lines += [f'### anchor `0x{r:08X}` — `{i.mnemonic} {i.op_str}`','','```asm']
    for w in arr[max(0,k-90):min(len(arr),k+80)]:lines.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
    lines += ['```','','Backward assignments mentioning likely base register:']
    regs=[]
    s=i.op_str.lower()
    for reg in ('r14','r15','r13','r12','rdi','rsi','rbx'):
     if reg in s: regs.append(reg)
    for reg in regs:
     n=0
     for w in reversed(arr[max(0,k-220):k]):
      if reg in (w.mnemonic+' '+w.op_str).lower():
       lines.append(f'- `{reg}`: `0x{w.address-base:08X}: {w.mnemonic} {w.op_str}`');n+=1
       if n>=18:break
    lines += ['']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'vmr_nonstack_candidates.md';p.write_text('\n'.join(lines),encoding='utf-8');print(p)
if __name__=='__main__':main()
