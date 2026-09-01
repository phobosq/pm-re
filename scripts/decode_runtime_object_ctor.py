#!/usr/bin/env python3
"""Decode the strongest runtime-object constructor/destructor family.
Static only; PhoenixMiner is never executed.
"""
from __future__ import annotations
import argparse,bisect
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_IMM,X86_OP_MEM

TARGETS=[0x0012F250,0x0012FFB0,0x0012FF50]

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
 # Build direct caller map in one pass over .text
 text=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.text')
 callers={t:[] for t in TARGETS}
 for i in md.disasm(text.get_data(),base+text.VirtualAddress):
  if i.mnemonic!='call' or not i.operands or i.operands[0].type!=X86_OP_IMM: continue
  t=i.operands[0].imm-base
  if t in callers:
   callers[t].append((i.address-base,fnof(i.address-base)))
 lines=['# Runtime object constructor family','',
        'Strong type seed: `0x12F250` touches +0x318, +0x368, +0x440 and +0x538.','']
 for target in TARGETS:
  fn=fnof(target)
  if not fn: continue
  b,en=fn; ins=list(md.disasm(pe.get_data(b,en-b),base+b))
  lines += [f'## target `0x{target:08X}` PDATA `0x{b:08X}..0x{en:08X}`','','```asm']
  for i in ins: lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
  lines += ['```','','### Object-relative memory operands','']
  for i in ins:
   for op in i.operands:
    if op.type==X86_OP_MEM and 0 <= op.mem.disp <= 0x800:
     lines.append(f'- `0x{i.address-base:08X}` disp `+0x{op.mem.disp:X}`: `{i.mnemonic} {i.op_str}`')
  lines += ['','### Direct calls','']
  for i in ins:
   if i.mnemonic!='call': continue
   if i.operands and i.operands[0].type==X86_OP_IMM:
    lines.append(f'- `0x{i.address-base:08X}` -> `0x{i.operands[0].imm-base:08X}`')
   else: lines.append(f'- `0x{i.address-base:08X}` -> `{i.op_str}`')
  lines += ['','### Direct callers','']
  for cs,cf in callers[target]:
   ctxt='none' if not cf else f'0x{cf[0]:08X}..0x{cf[1]:08X}'
   lines.append(f'- `0x{cs:08X}` in `{ctxt}`')
  lines.append('')
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'runtime_object_ctor.md';p.write_text('\n'.join(lines),encoding='utf-8');print(p)
if __name__=='__main__':main()
