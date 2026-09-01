#!/usr/bin/env python3
"""Decode vendor-specific constructor helpers for derived runtime types.
Static only.
"""
from __future__ import annotations
import argparse,bisect,string
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_IMM,X86_OP_MEM,X86_REG_RIP
TARGETS=[0x00179840,0x00179430,0x001D4A80]
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
  for im in d.imports:
   imports[im.address-base]=dll+'!'+(im.name.decode(errors='replace') if im.name else f'ord_{im.ordinal}')
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 def ascii_at(rva,limit=120):
  try:b=pe.get_data(rva,limit)
  except:return None
  n=0
  while n<len(b) and b[n] and 0x20<=b[n]<0x7f:n+=1
  return b[:n].decode(errors='replace') if n>=4 else None
 def utf16_at(rva,limit=240):
  try:b=pe.get_data(rva,limit)
  except:return None
  chars=[]
  for k in range(0,len(b)-1,2):
   c=b[k]|(b[k+1]<<8)
   if c==0:break
   if c<0x20 or c>0x7e:return None
   chars.append(chr(c))
  return ''.join(chars) if len(chars)>=4 else None
 lines=['# Vendor constructor helpers','']
 for t in TARGETS:
  fn=fnof(t);lines += [f'## target `0x{t:08X}` PDATA `{("0x%08X..0x%08X"%fn) if fn else "none"}`','']
  if not fn:continue
  arr=list(md.disasm(pe.get_data(fn[0],fn[1]-fn[0]),base+fn[0]))
  lines += ['### Calls','', '| RVA | target/form | import? |','|---|---|---|']
  refs=[]
  for i in arr:
   if i.mnemonic=='call':
    target=i.op_str; imp=''
    if i.operands and i.operands[0].type==X86_OP_IMM:
     rr=i.operands[0].imm-base; target=f'RVA 0x{rr:08X}'
    elif i.operands and i.operands[0].type==X86_OP_MEM and i.operands[0].mem.base==X86_REG_RIP:
     rr=(i.address+i.size+i.operands[0].mem.disp)-base
     imp=imports.get(rr,'')
    lines.append(f'| `0x{i.address-base:08X}` | `{target}` | `{imp}` |')
   for op in i.operands:
    if op.type==X86_OP_MEM and op.mem.base==X86_REG_RIP:
     rr=(i.address+i.size+op.mem.disp)-base
     s=ascii_at(rr) or utf16_at(rr)
     if s:refs.append((i.address-base,rr,s))
  lines += ['','### RIP-relative literal candidates','', '| RVA | target | text |','|---|---|---|']
  for r,rr,s in refs:lines.append(f'| `0x{r:08X}` | `0x{rr:08X}` | `{s.replace("|","\\|")}` |')
  lines += ['','### Disassembly','', '```asm']
  for i in arr:lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'vendor_ctor_helpers.md';p.write_text('\n'.join(lines),encoding='utf-8');print(p)
if __name__=='__main__':main()
