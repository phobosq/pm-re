#!/usr/bin/env python3
"""Trace direct callers of runtime factory 0x584A0 and provenance of its R8 context argument.
Static only; PhoenixMiner is never executed.
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
  if b<en: funcs.append((b,en))
 funcs.sort();starts=[b for b,_ in funcs]
 def fnof(r):
  j=bisect.bisect_right(starts,r)-1
  return funcs[j] if j>=0 and funcs[j][0]<=r<funcs[j][1] else None
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True;md.skipdata=True
 text=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.text')
 allins=[i for i in md.disasm(text.get_data(),base+text.VirtualAddress) if i.id]
 hits=[]
 for idx,i in enumerate(allins):
  if i.mnemonic=='call' and i.operands and i.operands[0].type==X86_OP_IMM and i.operands[0].imm-base==TARGET:
   hits.append((idx,i,fnof(i.address-base)))
 lines=['# Runtime factory 0x584A0 callers','',
        'Factory contract established statically: RDX=&type, R8=context pointer, selected derived ctor receives context unchanged into base this+0x90.','',
        f'direct callers: {len(hits)}','']
 for n,(idx,i,fn) in enumerate(hits,1):
  f='none' if not fn else f'0x{fn[0]:08X}..0x{fn[1]:08X}'
  lines += [f'## caller {n}: call `0x{i.address-base:08X}` in `{f}`','', '### Call context','```asm']
  for w in allins[max(0,idx-40):min(len(allins),idx+28)]: lines.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
  lines += ['```','']
  if fn:
   b,en=fn;ins=list(md.disasm(pe.get_data(b,en-b),base+b))
   lines += ['### Full caller function','```asm']
   for w in ins: lines.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
   lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'runtime_factory_callers.md';p.write_text('\n'.join(lines),encoding='utf-8');print(p)
if __name__=='__main__':main()
