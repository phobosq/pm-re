#!/usr/bin/env python3
"""Trace the holder whose first qword becomes runtime base ctor RDX/context.
Static only; PhoenixMiner is never executed.
"""
from __future__ import annotations
import argparse,bisect
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_IMM

TARGETS=[0x00058210,0x000582D0]

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
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True;md.skipdata=True
 text=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.text')
 allins=[i for i in md.disasm(text.get_data(),base+text.VirtualAddress) if i.id]
 callers={t:[] for t in TARGETS}
 for idx,i in enumerate(allins):
  if i.mnemonic=='call' and i.operands and i.operands[0].type==X86_OP_IMM:
   t=i.operands[0].imm-base
   if t in callers: callers[t].append((idx,i,fnof(i.address-base)))
 lines=['# Context holder provenance','',
        'Factory functions pass `RDX = [r15]` into derived ctor -> base `this+0x90`.','']
 for t in TARGETS:
  fn=fnof(t);b,en=fn if fn else (t,t+0x200)
  ins=list(md.disasm(pe.get_data(b,en-b),base+b))
  lines += [f'## factory `0x{t:08X}` PDATA `0x{b:08X}..0x{en:08X}`','','### Full body','```asm']
  for i in ins: lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
  lines += ['```','','### Direct callers','']
  for idx,i,cf in callers[t]:
   c='none' if not cf else f'0x{cf[0]:08X}..0x{cf[1]:08X}'
   lines += [f'#### call `0x{i.address-base:08X}` in `{c}`','', '```asm']
   for w in allins[max(0,idx-24):min(len(allins),idx+24)]: lines.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
   lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'context_holder_provenance.md';p.write_text('\n'.join(lines),encoding='utf-8');print(p)
if __name__=='__main__':main()
