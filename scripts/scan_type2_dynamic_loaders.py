#!/usr/bin/env python3
"""Enumerate dynamic loader callsites in confirmed NVIDIA Type2 code region. Static only."""
from __future__ import annotations
import argparse,bisect
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_REG_RIP
LO,HI=0x001C0000,0x001F3000
WANTED={'GetProcAddress','LoadLibraryA','LoadLibraryW','LoadLibraryExA','LoadLibraryExW','GetModuleHandleA','GetModuleHandleW','GetModuleHandleExA','GetModuleHandleExW','FreeLibrary'}
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
   name=im.name.decode(errors='replace') if im.name else f'ord_{im.ordinal}'
   if name in WANTED:imports[im.address-base]=f'{dll}!{name}'
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True;md.skipdata=True
 arr=[i for i in md.disasm(pe.get_data(LO,HI-LO),base+LO) if i.id!=0]
 hits=[]
 for k,i in enumerate(arr):
  if i.mnemonic!='call' or not i.operands:continue
  op=i.operands[0]
  if op.type==X86_OP_MEM and op.mem.base==X86_REG_RIP:
   rr=(i.address+i.size+op.mem.disp)-base
   if rr in imports:hits.append((k,i,rr,imports[rr],fnof(i.address-base)))
 lines=['# NVIDIA Type2 dynamic loader callsites','',f'region `0x{LO:08X}..0x{HI:08X}`; hits: {len(hits)}','', '| RVA | PDATA | API |','|---|---|---|']
 for k,i,rr,name,fn in hits:
  fs='none' if not fn else f'0x{fn[0]:08X}..0x{fn[1]:08X}'
  lines.append(f'| `0x{i.address-base:08X}` | `{fs}` | `{name}` |')
 lines += ['','## Contexts','']
 for k,i,rr,name,fn in hits:
  lines += [f'### `0x{i.address-base:08X}` — `{name}`','','```asm']
  for w in arr[max(0,k-35):min(len(arr),k+20)]:lines.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
  lines += ['```','','Direct calls in preceding 35 instructions:']
  for w in arr[max(0,k-35):k]:
   if w.mnemonic=='call' and w.op_str.startswith('0x'):
    try:lines.append(f'- `0x{w.address-base:08X}` -> `0x{int(w.op_str,16)-base:08X}`')
    except:pass
  lines += ['']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'type2_dynamic_loaders.md';p.write_text('\n'.join(lines),encoding='utf-8');print('hits',len(hits))
if __name__=='__main__':main()
