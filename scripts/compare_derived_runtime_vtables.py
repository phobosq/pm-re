#!/usr/bin/env python3
"""Decode and compare the two derived runtime-class vtables and context usage.
Static only; PhoenixMiner is never executed.
"""
from __future__ import annotations
import argparse,bisect,struct
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_OP_IMM

VTABLES={0x0044B3D8:'derived_type1',0x004BD558:'derived_type2'}
MAX=48

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 text=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.text')
 lo=text.VirtualAddress;hi=lo+max(text.Misc_VirtualSize,text.SizeOfRawData)
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en: funcs.append((b,en))
 funcs.sort();starts=[b for b,_ in funcs]
 def fnof(r):
  j=bisect.bisect_right(starts,r)-1
  return funcs[j] if j>=0 and funcs[j][0]<=r<funcs[j][1] else None
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 methods={}
 lines=['# Derived runtime vtable comparison','',
        'Type1 ctor: `0x161030`, vtable `0x44B3D8`.',
        'Type2 ctor: `0x1CDCC0`, vtable `0x4BD558`.',
        'Both inherit base ctor `0x12F250` and store the same context interface at `this+0x90`.','']
 tables={}
 for vrva,name in VTABLES.items():
  raw=pe.get_data(vrva,MAX*8); ent=[]; non=0
  for n in range(len(raw)//8):
   q=struct.unpack_from('<Q',raw,n*8)[0]
   mr=q-base if base<=q<base+pe.OPTIONAL_HEADER.SizeOfImage else None
   if mr is not None and lo<=mr<hi:
    non=0; ent.append((n,mr,fnof(mr)))
   else:
    non+=1
    if n>=4 and non>=3: break
  tables[name]=ent
  for n,m,f in ent: methods.setdefault(m,[]).append((name,n,f))
  lines += [f'## {name} vtable `0x{vrva:08X}`','', '| slot | method | PDATA |','|---:|---|---|']
  for n,m,f in ent:
   p='none' if not f else f'0x{f[0]:08X}..0x{f[1]:08X}'
   lines.append(f'| `+0x{n*8:X}` | `0x{m:08X}` | `{p}` |')
  lines.append('')
 # side-by-side
 lines += ['## Slot comparison','', '| slot | type1 | type2 | same? |','|---:|---|---|---|']
 d1={n:m for n,m,_ in tables.get('derived_type1',[])};d2={n:m for n,m,_ in tables.get('derived_type2',[])}
 for n in sorted(set(d1)|set(d2)):
  a1=d1.get(n);a2=d2.get(n)
  lines.append(f'| `+0x{n*8:X}` | {"-" if a1 is None else f"`0x{a1:08X}`"} | {"-" if a2 is None else f"`0x{a2:08X}`"} | {a1==a2 and a1 is not None} |')
 lines += ['','## Method bodies and `this+0x90` context accesses','']
 seen=set()
 for m,owners in sorted(methods.items()):
  if m in seen: continue
  seen.add(m); f=fnof(m)
  if not f:
   # decode thunk until ret/jmp
   ins=list(md.disasm(pe.get_data(m,0x100),base+m));cut=[]
   for i in ins:
    cut.append(i)
    if i.mnemonic in ('ret','jmp'): break
   ins=cut;rg=(m,m+(ins[-1].address-base-m+ins[-1].size if ins else 0x20))
  else:
   rg=f;ins=list(md.disasm(pe.get_data(f[0],f[1]-f[0]),base+f[0]))
  ctxt=[]
  for i in ins:
   for op in i.operands:
    if op.type==X86_OP_MEM and op.mem.disp==0x90: ctxt.append(i)
  # Include all method bodies if unique between types; otherwise only compact metadata for shared stub.
  owner_names={o[0] for o in owners}; unique=len(owner_names)==1
  lines += [f'### method `0x{m:08X}` owners: '+', '.join(f'{o[0]} +0x{o[1]*8:X}' for o in owners),'']
  if ctxt:
   lines.append('Context +0x90 accesses:')
   for i in ctxt: lines.append(f'- `0x{i.address-base:08X}`: `{i.mnemonic} {i.op_str}`')
   lines.append('')
  calls=[]
  for i in ins:
   if i.mnemonic=='call':
    if i.operands and i.operands[0].type==X86_OP_IMM: calls.append((i.address-base,f'0x{i.operands[0].imm-base:08X}'))
    else: calls.append((i.address-base,i.op_str))
  if calls:
   lines.append('Calls:')
   for r,t in calls: lines.append(f'- `0x{r:08X}` -> `{t}`')
   lines.append('')
  if unique or ctxt:
   lines += ['```asm']
   for i in ins: lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
   lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'derived_runtime_vtables_compare.md';p.write_text('\n'.join(lines),encoding='utf-8');print(p)
if __name__=='__main__':main()
