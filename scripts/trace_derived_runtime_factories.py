#!/usr/bin/env python3
"""Trace callers and derived vtables for runtime classes inheriting 0x12F250.
Static only; PhoenixMiner is never executed.
"""
from __future__ import annotations
import argparse,bisect,struct
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_IMM,X86_OP_MEM

CTORS=[0x00161030,0x001CDCC0]
# Derived vtables recovered from ctor RIP-relative LEA instructions.
# Script also computes them from the ctor bodies for verification.

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
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True;md.skipdata=True
 text=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.text')
 allins=[i for i in md.disasm(text.get_data(),base+text.VirtualAddress) if i.id]
 callers={t:[] for t in CTORS}
 for idx,i in enumerate(allins):
  if i.mnemonic=='call' and i.operands and i.operands[0].type==X86_OP_IMM:
   t=i.operands[0].imm-base
   if t in callers: callers[t].append((idx,i,fnof(i.address-base)))
 lines=['# Derived runtime factories','',
        'Both constructors inherit from `0x12F250`; their RDX is forwarded unchanged to base ctor -> base `this+0x90`.','']
 for ctor in CTORS:
  fn=fnof(ctor); b,en=fn if fn else (ctor,ctor+0x600)
  ins=list(md.disasm(pe.get_data(b,en-b),base+b))
  # Find first RIP-relative LEA after base ctor call followed by store to [this].
  vrefs=[]
  for i in ins:
   if 'rip' not in i.op_str.lower(): continue
   for op in i.operands:
    if op.type==X86_OP_MEM:
     va=i.address+i.size+op.mem.disp
     if base<=va<base+pe.OPTIONAL_HEADER.SizeOfImage:
      vrefs.append((i.address-base,va-base,i.mnemonic,i.op_str))
  lines += [f'## ctor `0x{ctor:08X}` PDATA `0x{b:08X}..0x{en:08X}`','','### RIP-relative refs','']
  for r,t,m,o in vrefs: lines.append(f'- `0x{r:08X}` -> RVA `0x{t:08X}`: `{m} {o}`')
  lines += ['','### Direct callers','']
  for idx,i,cf in callers[ctor]:
   c='none' if not cf else f'0x{cf[0]:08X}..0x{cf[1]:08X}'
   lines.append(f'- `0x{i.address-base:08X}` in `{c}`')
   lines += ['```asm']
   for w in allins[max(0,idx-18):min(len(allins),idx+20)]: lines.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
   lines += ['```']
  lines += ['','### Constructor body','```asm']
  for i in ins: lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
  lines += ['```','']
 # Decode likely vtable addresses directly known from ctor LEAs by collecting refs in image around 0x440000-0x480000
 lines += ['## Candidate derived vtables','']
 seen=set()
 for ctor in CTORS:
  fn=fnof(ctor); b,en=fn if fn else (ctor,ctor+0x600)
  ins=list(md.disasm(pe.get_data(b,en-b),base+b))
  for i in ins:
   if 'rip' not in i.op_str.lower(): continue
   for op in i.operands:
    if op.type!=X86_OP_MEM: continue
    r=(i.address+i.size+op.mem.disp)-base
    if not (0x400000<=r<=0x500000) or r in seen: continue
    seen.add(r)
    raw=pe.get_data(r,20*8)
    entries=[]
    for n in range(len(raw)//8):
     q=struct.unpack_from('<Q',raw,n*8)[0]
     mr=q-base if base<=q<base+pe.OPTIONAL_HEADER.SizeOfImage else None
     if mr is None or not (text.VirtualAddress<=mr<text.VirtualAddress+text.Misc_VirtualSize):
      if n>=2: break
     entries.append((n,q,mr))
    if len(entries)>=2:
     lines += [f'### RVA `0x{r:08X}` from ctor `0x{ctor:08X}`','']
     for n,q,mr in entries: lines.append(f'- slot +0x{n*8:X}: `0x{q:016X}` -> {"-" if mr is None else f"RVA 0x{mr:08X}"}')
     lines.append('')
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'derived_runtime_factories.md';p.write_text('\n'.join(lines),encoding='utf-8');print(p)
if __name__=='__main__':main()
