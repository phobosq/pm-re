#!/usr/bin/env python3
"""Find data/code references to 0x192100 and reconstruct candidate vtable ownership.
Static only; PhoenixMiner is never executed.
"""
from __future__ import annotations
import argparse,struct
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_REG_RIP
TARGET=0x00192100

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase;size=pe.OPTIONAL_HEADER.SizeOfImage
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True;md.skipdata=True
 lines=['# References / vtable ownership for 0x00192100','']
 refs=[]
 for s in pe.sections:
  data=s.get_data();srva=s.VirtualAddress
  # qword VA refs
  needle=struct.pack('<Q',base+TARGET)
  off=0
  while True:
   p=data.find(needle,off)
   if p<0:break
   refs.append((srva+p,s.Name.rstrip(b'\0').decode(errors='replace'),'va64'));off=p+1
  # rva32 refs
  needle4=struct.pack('<I',TARGET)
  off=0
  while True:
   p=data.find(needle4,off)
   if p<0:break
   refs.append((srva+p,s.Name.rstrip(b'\0').decode(errors='replace'),'rva32'));off=p+1
 lines += ['## Data refs','','| RVA | section | form |','|---|---|---|']
 for r,s,f in sorted(set(refs)):lines.append(f'| `0x{r:08X}` | `{s}` | {f} |')
 # dump ±0x80 around non-pdata refs as qword VA candidates
 for r,s,f in sorted(set(refs)):
  if s=='.pdata':continue
  sec=next(x for x in pe.sections if x.VirtualAddress<=r<x.VirtualAddress+max(x.Misc_VirtualSize,x.SizeOfRawData))
  start=max(sec.VirtualAddress,r-0x80);end=min(sec.VirtualAddress+len(sec.get_data()),r+0x88)
  raw=pe.get_data(start,end-start)
  lines += ['',f'## Neighborhood around `0x{r:08X}` ({s})','','| RVA | qword target RVA |','|---|---|']
  for o in range(0,len(raw)-7,8):
   q=struct.unpack_from('<Q',raw,o)[0];tr=q-base if base<=q<base+size else None
   lines.append(f'| `0x{start+o:08X}` | {"" if tr is None else f"`0x{tr:08X}`"} |')
 # code RIP refs to data-ref locations
 targets={r for r,s,f in refs if s not in ('.pdata','.xdata')}
 text=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.text')
 lines += ['','## Code RIP refs to candidate table locations','','| RVA | data RVA | instruction |','|---|---|---|']
 for i in md.disasm(text.get_data(),base+text.VirtualAddress):
  if i.id==0:continue
  for op in i.operands:
   if op.type==X86_OP_MEM and op.mem.base==X86_REG_RIP:
    dr=i.address+i.size+op.mem.disp-base
    if any(abs(dr-t)<=0x80 for t in targets):
     lines.append(f'| `0x{i.address-base:08X}` | `0x{dr:08X}` | `{i.mnemonic} {i.op_str}` |')
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'owner_192100.md').write_text('\n'.join(lines),encoding='utf-8')
if __name__=='__main__':main()
