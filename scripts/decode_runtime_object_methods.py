#!/usr/bin/env python3
"""Decode runtime object methods 0x084A60 and 0x1362D0 and find direct callers.
Static only; target binary is never executed.
"""
from __future__ import annotations
import argparse,bisect
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_IMM
TARGETS=[0x00084A60,0x001362D0]

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
 text=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.text')
 mdall=Cs(CS_ARCH_X86,CS_MODE_64);mdall.detail=True;mdall.skipdata=True
 allins=[i for i in mdall.disasm(text.get_data(),base+text.VirtualAddress) if i.id!=0]
 lines=['# Runtime object snapshot methods','']
 for target in TARGETS:
  fn=fnof(target) or (target,target+0x500);b,en=fn
  ins=list(md.disasm(pe.get_data(b,en-b),base+b))
  lines += [f'## target `0x{target:08X}` PDATA `0x{b:08X}..0x{en:08X}`','','```asm']
  for i in ins:lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
  lines += ['```','','### Direct callers','']
  callers=[]
  for i in allins:
   if i.mnemonic=='call' and i.operands and i.operands[0].type==X86_OP_IMM and i.operands[0].imm==base+target:
    callers.append((i.address-base,fnof(i.address-base)))
  for c,f in callers:
   fs='none' if not f else f'0x{f[0]:08X}..0x{f[1]:08X}'
   lines.append(f'- `0x{c:08X}` in `{fs}`')
  if not callers:lines.append('- none')
  lines += ['']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'runtime_object_methods.md').write_text('\n'.join(lines),encoding='utf-8')
 print(out/'runtime_object_methods.md')
if __name__=='__main__':main()
