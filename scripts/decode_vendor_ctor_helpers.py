#!/usr/bin/env python3
"""Decode vendor-specific constructor and GetProcAddress string helpers. Static only."""
from __future__ import annotations
import argparse,bisect
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_IMM,X86_OP_MEM,X86_REG_RIP
TARGETS=[0x001D35C0,0x001A5430,0x00178F80,0x001D4A80]
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
  for im in d.imports: imports[im.address-base]=dll+'!'+(im.name.decode(errors='replace') if im.name else f'ord_{im.ordinal}')
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 lines=['# Vendor constructor / string helpers','']
 for t in TARGETS:
  fn=fnof(t);lines += [f'## target `0x{t:08X}` PDATA `{("0x%08X..0x%08X"%fn) if fn else "none"}`','']
  # If target lacks its own PDATA, decode a bounded 0x300-byte window from exact RVA.
  b,en=(fn if fn else (t,t+0x300)); arr=list(md.disasm(pe.get_data(b,en-b),base+b))
  # trim exact-window decoding after first RET beyond target
  if not fn:
   tmp=[]
   for i in arr:
    tmp.append(i)
    if i.address-base>=t and i.mnemonic=='ret':break
   arr=tmp
  lines += ['### Calls','', '| RVA | target/form | import? |','|---|---|---|']
  for i in arr:
   if i.mnemonic!='call':continue
   target=i.op_str;imp=''
   if i.operands and i.operands[0].type==X86_OP_IMM:target=f'RVA 0x{i.operands[0].imm-base:08X}'
   elif i.operands and i.operands[0].type==X86_OP_MEM and i.operands[0].mem.base==X86_REG_RIP:
    rr=(i.address+i.size+i.operands[0].mem.disp)-base;imp=imports.get(rr,'')
   lines.append(f'| `0x{i.address-base:08X}` | `{target}` | `{imp}` |')
  lines += ['','### Disassembly','', '```asm']
  for i in arr:lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'vendor_ctor_helpers.md';p.write_text('\n'.join(lines),encoding='utf-8');print(p)
if __name__=='__main__':main()
