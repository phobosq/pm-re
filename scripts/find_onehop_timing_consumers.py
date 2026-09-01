#!/usr/bin/env python3
"""Scan one direct-call layer below confirmed vendor-specific runtime virtual methods.

Goal: find helpers that access timing fields after receiving a runtime object/snapshot.
This is lineage-constrained: only direct callees of methods in confirmed type1/type2 vtables.
Static only; PhoenixMiner is never executed.
"""
from __future__ import annotations
import argparse,bisect,struct
from collections import defaultdict
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_OP_IMM,X86_REG_RSP,X86_REG_RBP,X86_REG_ESP,X86_REG_EBP

VTABLES={0x0044B3D8:'type1',0x004BD558:'type2'}
STACK={X86_REG_RSP,X86_REG_RBP,X86_REG_ESP,X86_REG_EBP}
FIELDS={
 0x400:'A.mt',0x414:'A.straps',0x418:'A.vmr_rxboost',0x420:'A.vmt2',0x424:'A.vmt3',
 0x4D8:'B.mt',0x4EC:'B.straps',0x4F0:'B.vmr_rxboost',0x4F8:'B.vmt2',0x4FC:'B.vmt3',
 0x98:'record.mt?',0xAC:'record.straps?',0xB0:'record.vmr?',0xB8:'record.vmt2?',0xBC:'record.vmt3?',
}
SHARED_METHODS={0x00067840,0x00138970,0x00132720,0x0036EFD0}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 text=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.text');tlo=text.VirtualAddress;thi=tlo+max(text.Misc_VirtualSize,text.SizeOfRawData)
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en: funcs.append((b,en))
 funcs.sort();starts=[b for b,_ in funcs]
 def fnof(r):
  j=bisect.bisect_right(starts,r)-1
  return funcs[j] if j>=0 and funcs[j][0]<=r<funcs[j][1] else None
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 methods=[]
 for vrva,name in VTABLES.items():
  raw=pe.get_data(vrva,0xC0);non=0
  for n in range(len(raw)//8):
   q=struct.unpack_from('<Q',raw,n*8)[0];m=q-base if base<=q<base+pe.OPTIONAL_HEADER.SizeOfImage else None
   if m is not None and tlo<=m<thi:
    non=0
    if m not in SHARED_METHODS: methods.append((name,n,m))
   else:
    non+=1
    if n>=4 and non>=3: break
 # Gather direct calls from vendor-specific methods.
 edges=defaultdict(list) # callee -> [(type,slot,method,callrva,precontext)]
 for name,slot,m in methods:
  fn=fnof(m)
  if fn: b,en=fn;ins=list(md.disasm(pe.get_data(b,en-b),base+b))
  else:
   ins=list(md.disasm(pe.get_data(m,0x200),base+m));cut=[]
   for i in ins:
    cut.append(i)
    if i.mnemonic in ('ret','jmp'): break
   ins=cut
  for idx,i in enumerate(ins):
   if i.mnemonic=='call' and i.operands and i.operands[0].type==X86_OP_IMM:
    tgt=i.operands[0].imm-base
    if tlo<=tgt<thi:
     pre=ins[max(0,idx-8):idx+1]
     edges[tgt].append((name,slot,m,i.address-base,pre))
 # Scan each unique callee for timing-like displacements.
 hits=[]
 for tgt,origins in edges.items():
  fn=fnof(tgt)
  if fn: b,en=fn;ins=list(md.disasm(pe.get_data(b,en-b),base+b))
  else:
   ins=list(md.disasm(pe.get_data(tgt,0x300),base+tgt));cut=[]
   for i in ins:
    cut.append(i)
    if i.mnemonic=='ret': break
   ins=cut;b=tgt;en=tgt+(ins[-1].address-base-tgt+ins[-1].size if ins else 0x20)
  acc=[]
  for idx,i in enumerate(ins):
   for op in i.operands:
    if op.type==X86_OP_MEM and op.mem.disp in FIELDS and op.mem.base not in STACK:
     acc.append((idx,i,op.mem.disp))
  if acc: hits.append((tgt,b,en,origins,ins,acc))
 lines=['# One-hop timing consumers','',
        'Scope: direct callees of vendor-specific methods in confirmed type1/type2 runtime vtables.',
        'A hit is only a candidate until the callsite proves the relevant object/snapshot is passed.','',
        f'unique callees: {len(edges)}',f'callees with timing-like accesses: {len(hits)}','']
 for k,(tgt,b,en,origins,ins,acc) in enumerate(hits,1):
  distinct=sorted({d for _,_,d in acc})
  lines += [f'## candidate {k}: `0x{tgt:08X}` range `0x{b:08X}..0x{en:08X}`','',
            'Fields: '+', '.join(f'{FIELDS[d]}(+0x{d:X})' for d in distinct),'',
            '### Origins / callsites','']
  for name,slot,m,cs,pre in origins:
   lines += [f'- {name} slot `+0x{slot*8:X}` method `0x{m:08X}`, call `0x{cs:08X}`','```asm']
   for w in pre: lines.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
   lines += ['```']
  lines += ['','### Timing-like accesses','']
  for idx,i,d in acc: lines.append(f'- `0x{i.address-base:08X}` {FIELDS[d]} `+0x{d:X}`: `{i.mnemonic} {i.op_str}`')
  lines += ['','### Access contexts','']
  shown=set()
  for idx,i,d in acc:
   key=max(0,idx-10)
   if key in shown: continue
   shown.add(key);lines += ['```asm']
   for w in ins[max(0,idx-10):min(len(ins),idx+18)]: lines.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
   lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'onehop_timing_consumers.md';p.write_text('\n'.join(lines),encoding='utf-8');print(p)
if __name__=='__main__':main()
