#!/usr/bin/env python3
"""Trace callers and object provenance of straps backend entry 0x1C44F0.
Also summarize timing/transport-adjacent helpers around 0x1C.
Static only; PhoenixMiner is never executed.
"""
from __future__ import annotations
import argparse,bisect,struct
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_IMM,X86_OP_MEM,X86_REG_RIP
TARGET=0x001C44F0
HELPERS=[0x001C4010,0x001C44F0,0x001C5120,0x001C1F70,0x001C2100,0x001C3A00,0x001C6CA0]

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
 # direct caller map for helpers
 cm={h:[] for h in HELPERS}
 for off in range(len(raw)-5):
  if raw[off]!=0xE8:continue
  rel=struct.unpack_from('<i',raw,off+1)[0];c=trva+off;dst=c+5+rel
  if dst in cm:cm[dst].append((c,fnof(c)))
 lines=['# Straps / IOMap backend entry provenance','',
        'Confirmed transport family: `CreateFileA("\\\\.\\IOMap")` near `0x1C40F0`, `DeviceIoControl` at `0x1C44A1`, straps entry `0x1C44F0`.','']
 for h in HELPERS:
  fn=fnof(h)
  lines += [f'## helper `0x{h:08X}`'+(f' PDATA `0x{fn[0]:08X}..0x{fn[1]:08X}`' if fn else ''),'',f'direct callers: `{len(cm[h])}`','']
  for c,f in cm[h]:lines.append(f'- `0x{c:08X}` from `{("0x%08X..0x%08X"%f) if f else "no PDATA"}`')
  if h==TARGET or h in (0x001C5120,0x001C6CA0):
   b,en=fn or (h,h+0x1000);arr=[i for i in md.disasm(pe.get_data(b,en-b),base+b) if i.id!=0]
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
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'straps_backend_entry.md').write_text('\n'.join(lines),encoding='utf-8')
if __name__=='__main__':main()
