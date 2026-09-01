#!/usr/bin/env python3
"""Decode hot methods behind the confirmed runtime-object vtable.
Static only; PhoenixMiner is never executed.
"""
from __future__ import annotations
import argparse,bisect
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_IMM

TARGETS=[
 0x00132720, # derived vtable slot +0x28, no PDATA
 0x00138970, # derived vtable slot +0x18
 0x001354F0, # called by slot +0x18
 0x0006F460,
 0x0006A240,
 0x001312E0,
 0x00134690,
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
 # caller map
 text=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.text')
 callers={t:[] for t in TARGETS}
 for i in md.disasm(text.get_data(),base+text.VirtualAddress):
  if i.mnemonic=='call' and i.operands and i.operands[0].type==X86_OP_IMM:
   t=i.operands[0].imm-base
   if t in callers: callers[t].append((i.address-base,fnof(i.address-base)))
 lines=['# Runtime virtual hotpaths','',
        'Seeds come from confirmed derived vtable `0x440560` and direct callees of slot +0x18.','']
 for t in TARGETS:
  fn=fnof(t)
  if fn:
   b,en=fn; size=en-b
  else:
   b=t; size=0x180; en=b+size
  ins=list(md.disasm(pe.get_data(b,size),base+b))
  # For no-PDATA thunk, stop shortly after first RET/INT3 sequence.
  if not fn:
   cut=[]
   for i in ins:
    cut.append(i)
    if i.mnemonic=='ret': break
   ins=cut
  lines += [f'## target `0x{t:08X}` range `0x{b:08X}..0x{en:08X}` PDATA={bool(fn)}','','### Direct callers','']
  for cs,cf in callers[t]:
   c='none' if not cf else f'0x{cf[0]:08X}..0x{cf[1]:08X}'
   lines.append(f'- `0x{cs:08X}` in `{c}`')
  lines += ['','### Calls','']
  for i in ins:
   if i.mnemonic!='call': continue
   if i.operands and i.operands[0].type==X86_OP_IMM: lines.append(f'- `0x{i.address-base:08X}` -> `0x{i.operands[0].imm-base:08X}`')
   else: lines.append(f'- `0x{i.address-base:08X}` -> `{i.op_str}`')
  lines += ['','### Body','```asm']
  for i in ins: lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'runtime_virtual_hotpaths.md';p.write_text('\n'.join(lines),encoding='utf-8');print(p)
if __name__=='__main__':main()
