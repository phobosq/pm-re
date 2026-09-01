#!/usr/bin/env python3
"""Find data-table references to indirect runtime factory 0x584A0.
Static only; PhoenixMiner is never executed.
"""
from __future__ import annotations
import argparse,bisect,struct
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM

TARGETS={0x000584A0:'runtime_factory',0x00058210:'factory_type1',0x000582D0:'factory_type2'}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en: funcs.append((b,en))
 funcs.sort();starts=[b for b,_ in funcs]
 def fnof(r):
  j=bisect.bisect_right(starts,r)-1
  return funcs[j] if j>=0 and funcs[j][0]<=r<funcs[j][1] else None
 # qword matches in non-code sections
 matches=[]
 for s in pe.sections:
  name=s.Name.rstrip(b'\0').decode('ascii','replace')
  if name=='.text': continue
  data=s.get_data(); srva=s.VirtualAddress
  for off in range(0,max(0,len(data)-7),8):
   q=struct.unpack_from('<Q',data,off)[0]
   for trva,label in TARGETS.items():
    if q==base+trva: matches.append((srva+off,name,trva,label))
 lines=['# Runtime factory table references','',f'qword matches: {len(matches)}','']
 table_rvas=set()
 for rva,sec,trva,label in matches:
  table_rvas.add(rva)
  lines += [f'## {label} `0x{trva:08X}` stored at `{sec}` RVA `0x{rva:08X}`','', '### Neighbor qwords','', '| delta | qword | image RVA / ascii |','|---:|---|---|']
  start=max(0,rva-0x60);raw=pe.get_data(start,0xC8)
  for j in range(0,len(raw)-7,8):
   rr=start+j;q=struct.unpack_from('<Q',raw,j)[0]
   extra=''
   if base<=q<base+pe.OPTIONAL_HEADER.SizeOfImage: extra=f'RVA 0x{q-base:08X}'
   else:
    bs=struct.pack('<Q',q); txt=''.join(chr(x) if 32<=x<127 else '.' for x in bs)
    extra=txt
   lines.append(f'| `{rr-rva:+#x}` | `0x{q:016X}` | {extra} |')
  lines.append('')
 # Find code RIP-relative refs to each exact slot and nearby aligned table starts +/-0x80.
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True;md.skipdata=True
 text=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.text')
 ins=[i for i in md.disasm(text.get_data(),base+text.VirtualAddress) if i.id]
 candidates=set()
 for r,_,_,_ in matches:
  for d in range(-0x80,0x81,8): candidates.add(r+d)
 xrefs=[]
 for idx,i in enumerate(ins):
  if 'rip' not in i.op_str.lower(): continue
  for op in i.operands:
   if op.type!=X86_OP_MEM: continue
   rr=(i.address+i.size+op.mem.disp)-base
   if rr in candidates: xrefs.append((idx,i,rr,fnof(i.address-base)))
 lines += ['## Code refs to matching table neighborhoods','',f'xrefs: {len(xrefs)}','']
 for idx,i,rr,fn in xrefs:
  f='none' if not fn else f'0x{fn[0]:08X}..0x{fn[1]:08X}'
  lines += [f'### `0x{i.address-base:08X}` -> data RVA `0x{rr:08X}` in `{f}`','', '```asm']
  for w in ins[max(0,idx-12):min(len(ins),idx+16)]: lines.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'factory_table_refs.md';p.write_text('\n'.join(lines),encoding='utf-8');print(p)
if __name__=='__main__':main()
