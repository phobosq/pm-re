#!/usr/bin/env python3
"""Trace RIP-relative indirect-call slots used by Type2 ctor helper 0x1D4A80.
Find every code xref/writer to those slots and nearby imports/literals.
Static only.
"""
from __future__ import annotations
import argparse,bisect
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_REG_RIP,X86_OP_IMM
ROOT=0x001D4A80

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
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True;md.skipdata=True
 text=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.text')
 allins=[i for i in md.disasm(text.get_data(),base+text.VirtualAddress) if i.id!=0]
 rootfn=fnof(ROOT); rootins=[] if not rootfn else [i for i in allins if rootfn[0]<=i.address-base<rootfn[1]]
 slots=[]
 for i in rootins:
  if i.mnemonic!='call' or not i.operands:continue
  op=i.operands[0]
  if op.type==X86_OP_MEM and op.mem.base==X86_REG_RIP:
   rr=(i.address+i.size+op.mem.disp)-base
   slots.append((i.address-base,rr))
 slotset={s for _,s in slots}
 refs=[]
 for i in allins:
  for oi,op in enumerate(i.operands):
   if op.type==X86_OP_MEM and op.mem.base==X86_REG_RIP:
    rr=(i.address+i.size+op.mem.disp)-base
    if rr in slotset:
     access='unknown'
     if oi==0 and i.mnemonic.startswith(('mov','lea','xchg','cmpxchg')): access='dst/write-ish'
     elif i.mnemonic=='call':access='indirect-call'
     else:access='read-ish'
     refs.append((i,rr,access,fnof(i.address-base)))
 def lit(rva,limit=100):
  b=pe.get_data(rva,limit)
  n=0
  while n<len(b) and b[n] and 0x20<=b[n]<0x7f:n+=1
  if n>=4:return b[:n].decode(errors='replace')
  chars=[]
  for k in range(0,len(b)-1,2):
   c=b[k]|(b[k+1]<<8)
   if c==0:break
   if c<0x20 or c>0x7e:chars=[];break
   chars.append(chr(c))
  return ''.join(chars) if len(chars)>=4 else None
 lines=['# Type2 dynamic API slots','', 'Indirect RIP-call slots discovered in `0x001D4A80`.','', '| callsite | slot RVA |','|---|---|']
 for cs,s in slots:lines.append(f'| `0x{cs:08X}` | `0x{s:08X}` |')
 lines += ['','## All code refs to slots','', '| slot | RVA | PDATA | access | instruction |','|---|---|---|---|---|']
 for i,s,a2,fn in refs:
  fs='none' if not fn else f'0x{fn[0]:08X}..0x{fn[1]:08X}'
  lines.append(f'| `0x{s:08X}` | `0x{i.address-base:08X}` | `{fs}` | {a2} | `{i.mnemonic} {i.op_str}` |')
 lines += ['','## Ref contexts','']
 pos={i.address-base:k for k,i in enumerate(allins)}
 seen=set()
 for i,s,a2,fn in refs:
  key=(s,fn)
  if key in seen:continue
  seen.add(key);k=pos[i.address-base]
  lines += [f'### slot `0x{s:08X}` in `{("0x%08X..0x%08X"%fn) if fn else "no-pdata"}`','','```asm']
  for w in allins[max(0,k-22):min(len(allins),k+30)]:lines.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
  lines += ['```','','Nearby imports / literal refs:','']
  for w in allins[max(0,k-40):min(len(allins),k+45)]:
   for op in w.operands:
    if op.type==X86_OP_MEM and op.mem.base==X86_REG_RIP:
     rr=(w.address+w.size+op.mem.disp)-base
     if rr in imports:lines.append(f'- `0x{w.address-base:08X}` -> `{imports[rr]}`')
     else:
      s2=lit(rr)
      if s2:lines.append(f'- `0x{w.address-base:08X}` -> `0x{rr:08X}` text `{s2.replace("|","\\|")}`')
  lines += ['']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'type2_dynamic_api_slots.md';p.write_text('\n'.join(lines),encoding='utf-8');print('slots',len(slots),'refs',len(refs))
if __name__=='__main__':main()
