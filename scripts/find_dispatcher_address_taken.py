#!/usr/bin/env python3
"""Find all static address-taken references to dispatcher 0x584A0 and its containing PDATA start.
Scans unaligned absolute VA, 32-bit RVA, rel32-like data and RIP-relative code references. Static only.
"""
from __future__ import annotations
import argparse,struct,bisect
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_OP_IMM,X86_REG_RIP
TARGET=0x000584A0
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
 fn=fnof(TARGET); targets={TARGET}
 if fn:targets.add(fn[0])
 datarefs=[]
 for s in pe.sections:
  if s.Name.rstrip(b'\0')==b'.text':continue
  data=s.get_data();sr=s.VirtualAddress
  for off in range(0,max(0,len(data)-7)):
   q=struct.unpack_from('<Q',data,off)[0]
   for t in targets:
    if q==base+t:datarefs.append((sr+off,s.Name.rstrip(b'\0').decode(errors='replace'),'abs64',t,q))
  for off in range(0,max(0,len(data)-3)):
   u=struct.unpack_from('<I',data,off)[0]
   for t in targets:
    if u==t:datarefs.append((sr+off,s.Name.rstrip(b'\0').decode(errors='replace'),'rva32',t,u))
    # signed displacement from end of 4-byte entry to target VA/RVA
    sv=struct.unpack_from('<i',data,off)[0]
    dest=(sr+off+4+sv)&0xffffffff
    if dest in targets:datarefs.append((sr+off,s.Name.rstrip(b'\0').decode(errors='replace'),'rel32-data',dest,u))
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True;md.skipdata=True
 text=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.text')
 ins=[i for i in md.disasm(text.get_data(),base+text.VirtualAddress) if i.id!=0]
 coderefs=[]
 for i in ins:
  for op in i.operands:
   if op.type==X86_OP_MEM and op.mem.base==X86_REG_RIP:
    rr=(i.address+i.size+op.mem.disp)-base
    if rr in targets:coderefs.append((i.address-base,'rip-mem',rr,i.mnemonic,i.op_str))
   elif op.type==X86_OP_IMM:
    v=op.imm-base
    if v in targets:coderefs.append((i.address-base,'imm',v,i.mnemonic,i.op_str))
  if i.mnemonic=='lea' and i.operands and len(i.operands)>=2 and i.operands[1].type==X86_OP_MEM and i.operands[1].mem.base==X86_REG_RIP:
   rr=(i.address+i.size+i.operands[1].mem.disp)-base
   if rr in targets:coderefs.append((i.address-base,'rip-lea',rr,i.mnemonic,i.op_str))
 lines=['# Dispatcher 0x584A0 address-taken scan','',f'containing PDATA: `{("0x%08X..0x%08X"%fn) if fn else "none"}`','',f'data refs: {len(datarefs)}; code refs: {len(coderefs)}','', '## Data refs','', '| RVA | section | kind | target |','|---|---|---|---|']
 for r,s,k,t,v in datarefs:lines.append(f'| `0x{r:08X}` | `{s}` | {k} | `0x{t:08X}` |')
 lines += ['','## Code refs','', '| RVA | kind | target | instruction |','|---|---|---|---|']
 for r,k,t,m,o in coderefs:lines.append(f'| `0x{r:08X}` | {k} | `0x{t:08X}` | `{m} {o}` |')
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'dispatcher_address_taken.md';p.write_text('\n'.join(lines),encoding='utf-8');print('data',len(datarefs),'code',len(coderefs))
if __name__=='__main__':main()
