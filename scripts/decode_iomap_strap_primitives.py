#!/usr/bin/env python3
"""Decode straps backend callers and low-level primitives around 0x1C1E40/0x1C1ED0.
Static only; PhoenixMiner is never executed.
"""
from __future__ import annotations
import argparse,bisect,struct
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_IMM,X86_OP_MEM,X86_REG_RIP
TARGETS=[0x00192100,0x001C55F0,0x001C1E40,0x001C1ED0]

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
 imports={}
 for d in getattr(pe,'DIRECTORY_ENTRY_IMPORT',[]):
  dll=d.dll.decode(errors='replace')
  for imp in d.imports:
   if imp.address:
    nm=imp.name.decode(errors='replace') if imp.name else f'ord{imp.ordinal}'
    imports[imp.address-base]=f'{dll}!{nm}'
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True;md.skipdata=True
 text=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.text');raw=text.get_data();trva=text.VirtualAddress
 def callers(target):
  out=[]
  for off in range(len(raw)-5):
   if raw[off]!=0xE8:continue
   rel=struct.unpack_from('<i',raw,off+1)[0];c=trva+off
   if c+5+rel==target:out.append((c,fnof(c)))
  return out
 lines=['# IOMap straps primitives and entry callers','']
 for t in TARGETS:
  fn=fnof(t) or (t,t+0x400);b,en=fn;arr=[i for i in md.disasm(pe.get_data(b,en-b),base+b) if i.id!=0]
  cs=callers(t)
  lines += [f'## target `0x{t:08X}` PDATA `0x{b:08X}..0x{en:08X}`','',f'direct callers `{len(cs)}`','']
  for c,f in cs:lines.append(f'- `0x{c:08X}` from `{("0x%08X..0x%08X"%f) if f else "no PDATA"}`')
  lines += ['','### Calls','','| RVA | target |','|---|---|']
  for i in arr:
   if i.mnemonic!='call':continue
   form=i.op_str
   if i.operands:
    op=i.operands[0]
    if op.type==X86_OP_IMM:form=f'RVA 0x{op.imm-base:08X}'
    elif op.type==X86_OP_MEM and op.mem.base==X86_REG_RIP:
     rva=i.address+i.size+op.mem.disp-base;form=imports.get(rva,f'IAT/RIP 0x{rva:08X}')
   lines.append(f'| `0x{i.address-base:08X}` | `{form}` |')
  lines += ['','### Full body','','```asm']
  for i in arr:lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'iomap_strap_primitives.md').write_text('\n'.join(lines),encoding='utf-8')
if __name__=='__main__':main()
