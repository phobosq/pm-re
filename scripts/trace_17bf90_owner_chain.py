#!/usr/bin/env python3
"""Trace direct callers of ctor 0x17BF90 (vtable 0x44CE68) and decode caller contexts.
Static only; PhoenixMiner is never executed.
"""
from __future__ import annotations
import argparse,bisect,struct
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_IMM
TARGET=0x0017BF90

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
 text=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.text');raw=text.get_data();trva=text.VirtualAddress
 callers=[]
 for off in range(len(raw)-5):
  if raw[off]!=0xE8:continue
  rel=struct.unpack_from('<i',raw,off+1)[0];c=trva+off
  if c+5+rel==TARGET:callers.append((c,fnof(c)))
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True;md.skipdata=True
 lines=['# Owner chain for ctor 0x0017BF90 / vtable 0x0044CE68','',f'direct callers: `{len(callers)}`','']
 done=set()
 for c,fn in callers:
  lines.append(f'- `0x{c:08X}` from `{("0x%08X..0x%08X"%fn) if fn else "no PDATA"}`')
  if not fn or fn in done:continue
  done.add(fn);b,en=fn;arr=[i for i in md.disasm(pe.get_data(b,en-b),base+b) if i.id!=0]
  lines += ['',f'## caller PDATA `0x{b:08X}..0x{en:08X}`','','### Calls','','| RVA | target |','|---|---|']
  for i in arr:
   if i.mnemonic!='call':continue
   f=i.op_str
   if i.operands and i.operands[0].type==X86_OP_IMM:f=f'RVA 0x{i.operands[0].imm-base:08X}'
   lines.append(f'| `0x{i.address-base:08X}` | `{f}` |')
  lines += ['','### Full body','','```asm']
  for i in arr:lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
  lines += ['```']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'owner_chain_17bf90.md').write_text('\n'.join(lines),encoding='utf-8')
if __name__=='__main__':main()
