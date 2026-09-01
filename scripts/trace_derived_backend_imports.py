#!/usr/bin/env python3
"""Trace direct-call/import reachability from confirmed derived runtime methods.
Static only; target binary is never executed.
"""
from __future__ import annotations
import argparse,bisect
from pathlib import Path
from collections import deque,defaultdict
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_IMM,X86_OP_MEM,X86_REG_RIP

ROOTS={
 'type1_slot50':0x001688D0,
 'type2_slot50':0x001CF8B0,
 'type1_slot58':0x00169660,
 'type2_slot58':0x001D0730,
}

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('binary'); ap.add_argument('--out-dir',default='notes'); ap.add_argument('--depth',type=int,default=3); a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False); base=pe.OPTIONAL_HEADER.ImageBase
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress; en=e.struct.EndAddress
  if b<en: funcs.append((b,en))
 funcs.sort(); starts=[b for b,_ in funcs]
 def fnof(r):
  j=bisect.bisect_right(starts,r)-1
  return funcs[j] if j>=0 and funcs[j][0]<=r<funcs[j][1] else None
 imports={}
 for d in getattr(pe,'DIRECTORY_ENTRY_IMPORT',[]):
  dll=d.dll.decode(errors='replace')
  for im in d.imports:
   rva=im.address-base
   name=im.name.decode(errors='replace') if im.name else f'ord_{im.ordinal}'
   imports[rva]=f'{dll}!{name}'
 md=Cs(CS_ARCH_X86,CS_MODE_64); md.detail=True
 cache={}
 def decode(fn):
  if fn in cache:return cache[fn]
  b,en=fn; arr=list(md.disasm(pe.get_data(b,en-b),base+b)); cache[fn]=arr; return arr
 def edges(fn):
  out=[]; imps=[]; indirect=[]
  for i in decode(fn):
   if i.mnemonic!='call': continue
   op=i.operands[0] if i.operands else None
   if op and op.type==X86_OP_IMM:
    r=op.imm-base; callee=fnof(r)
    if callee: out.append((i.address-base,r,callee))
    else: indirect.append((i.address-base,i.op_str))
   elif op and op.type==X86_OP_MEM and op.mem.base==X86_REG_RIP:
    mem=(i.address+i.size+op.mem.disp)-base
    if mem in imports: imps.append((i.address-base,imports[mem]))
    else: indirect.append((i.address-base,i.op_str))
   else: indirect.append((i.address-base,i.op_str))
  return out,imps,indirect
 lines=['# Derived backend import reachability','',f'Max direct-call depth: {a.depth}.','']
 for label,root in ROOTS.items():
  rf=fnof(root)
  lines += [f'## {label} root `0x{root:08X}`','']
  if not rf:
   lines += ['No PDATA function.','']; continue
  q=deque([(rf,0)]); seen={rf}; allimps=[]; nodes=[]; indirects=[]
  while q:
   fn,d=q.popleft(); nodes.append((d,fn))
   es,ims,inds=edges(fn)
   for cs,name in ims: allimps.append((d,fn,cs,name))
   for cs,form in inds: indirects.append((d,fn,cs,form))
   if d<a.depth:
    for cs,r,cf in es:
     if cf not in seen:
      seen.add(cf); q.append((cf,d+1))
  lines += [f'reachable functions: {len(nodes)}  imports: {len(allimps)}  indirect calls: {len(indirects)}','',
            '### Imports','', '| depth | function | callsite | import |','|---:|---|---|---|']
  for d,fn,cs,name in sorted(allimps,key=lambda x:(x[0],x[3],x[2])):
   lines.append(f'| {d} | `0x{fn[0]:08X}` | `0x{cs:08X}` | `{name}` |')
  lines += ['','### Reachable functions','', '| depth | PDATA |','|---:|---|']
  for d,fn in sorted(nodes): lines.append(f'| {d} | `0x{fn[0]:08X}..0x{fn[1]:08X}` |')
  lines += ['','### Indirect calls (first 80)','', '| depth | function | callsite | form |','|---:|---|---|---|']
  for d,fn,cs,form in indirects[:80]: lines.append(f'| {d} | `0x{fn[0]:08X}` | `0x{cs:08X}` | `{form}` |')
  lines += ['']
 out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True); p=out/'derived_backend_import_reachability.md'; p.write_text('\n'.join(lines),encoding='utf-8'); print(p)
if __name__=='__main__':main()
