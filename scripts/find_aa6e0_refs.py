#!/usr/bin/env python3
"""Find address-taken/data/code references to 0xAA6E0.
Static only.
"""
from __future__ import annotations
import argparse,struct,bisect
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_REG_RIP
TARGET=0x000AA6E0
def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase;size=pe.OPTIONAL_HEADER.SizeOfImage
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en:funcs.append((b,en))
 funcs.sort();starts=[b for b,_ in funcs]
 def fnof(r):
  j=bisect.bisect_right(starts,r)-1
  return funcs[j] if j>=0 and funcs[j][0]<=r<funcs[j][1] else None
 datarefs=[]
 for s in pe.sections:
  b=s.get_data();sr=s.VirtualAddress
  for off in range(0,max(0,len(b)-7)):
   if off%4==0 and struct.unpack_from('<I',b,off)[0]==TARGET:datarefs.append((sr+off,s.Name.rstrip(b'\0').decode(errors='replace'),'rva32'))
   if off%8==0 and struct.unpack_from('<Q',b,off)[0]==base+TARGET:datarefs.append((sr+off,s.Name.rstrip(b'\0').decode(errors='replace'),'va64'))
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True;md.skipdata=True
 text=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.text')
 arr=[i for i in md.disasm(text.get_data(),base+text.VirtualAddress) if i.id!=0]
 coderefs=[]
 for k,i in enumerate(arr):
  for op in i.operands:
   if op.type==X86_OP_MEM and op.mem.base==X86_REG_RIP:
    rr=(i.address+i.size+op.mem.disp)-base
    if rr==TARGET:coderefs.append((k,i,'rip-target'))
  if i.mnemonic=='lea' and i.operands and TARGET in [((i.address+i.size+op.mem.disp)-base) for op in i.operands if op.type==X86_OP_MEM and op.mem.base==X86_REG_RIP]:pass
 lines=['# References to 0xAA6E0','',f'data refs: {len(datarefs)} code refs: {len(coderefs)}','', '## Data refs','', '| RVA | section | form |','|---|---|---|']
 for r,s,f in datarefs:lines.append(f'| `0x{r:08X}` | `{s}` | {f} |')
 lines += ['','## Code refs','']
 for k,i,kind in coderefs:
  fn=fnof(i.address-base);fs='none' if not fn else f'0x{fn[0]:08X}..0x{fn[1]:08X}'
  lines += [f'### `0x{i.address-base:08X}` {kind} PDATA `{fs}`','','```asm']
  for w in arr[max(0,k-35):min(len(arr),k+35)]:lines.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
  lines += ['```','']
 # neighborhoods around data refs
 lines += ['## Data neighborhoods','']
 for r,s,f in datarefs[:20]:
  sec=next((x for x in pe.sections if x.VirtualAddress<=r<x.VirtualAddress+x.Misc_VirtualSize),None)
  if not sec:continue
  start=max(sec.VirtualAddress,r-0x40);b=pe.get_data(start,0x80)
  lines += [f'### around `0x{r:08X}` in `{s}`','','| RVA | u32/RVA | u64/VA |','|---|---|---|']
  for off in range(0,len(b)-7,4):
   rr=start+off;u=struct.unpack_from('<I',b,off)[0];q=struct.unpack_from('<Q',b,off)[0]
   ui=f'0x{u:08X}' if 0x1000<=u<size else ''
   qi=f'0x{q-base:08X}' if base<=q<base+size else ''
   lines.append(f'| `0x{rr:08X}` | `{ui}` | `{qi}` |')
  lines += ['']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'aa6e0_refs.md';p.write_text('\n'.join(lines),encoding='utf-8');print('data',len(datarefs),'code',len(coderefs))
if __name__=='__main__':main()
