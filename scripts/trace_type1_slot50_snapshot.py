#!/usr/bin/env python3
"""Trace transitive 0xD8 snapshot copies inside AMD Type1 vtable slot +0x50 (0x1688D0).
Goal: follow config timing fields after get_snapshot() through local full-struct copies and into callees.
Static only; PhoenixMiner is never executed.
"""
from __future__ import annotations
import argparse,bisect
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_IMM,X86_OP_MEM,X86_OP_REG
TARGET=0x001688D0
GETTER=0x00084A60
SIZE=0xD8
LABELS={0x98:'mt',0xAC:'straps',0xB0:'vmr/rxboost',0xB8:'vmt2',0xBC:'vmt3'}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en:funcs.append((b,en))
 funcs.sort();starts=[b for b,_ in funcs]
 j=bisect.bisect_right(starts,TARGET)-1;b,en=funcs[j]
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True;md.skipdata=True
 arr=[i for i in md.disasm(pe.get_data(b,en-b),base+b) if i.id!=0]
 lines=['# AMD Type1 slot +0x50 transitive snapshot trace','',f'PDATA `0x{b:08X}..0x{en:08X}`','']
 # collect getter call sites and recover direct RDX output locals via last LEA
 getter_calls=[]
 for idx,i in enumerate(arr):
  if i.mnemonic!='call' or not i.operands or i.operands[0].type!=X86_OP_IMM or i.operands[0].imm-base!=GETTER:continue
  out=None
  for p in reversed(arr[max(0,idx-20):idx]):
   if p.mnemonic=='lea' and len(p.operands)==2 and p.operands[0].type==X86_OP_REG and p.reg_name(p.operands[0].reg)=='rdx' and p.operands[1].type==X86_OP_MEM:
    m=p.operands[1].mem;bn=p.reg_name(m.base)
    if bn in ('rsp','rbp'):out=(bn,m.disp,p.address-base);break
  getter_calls.append((idx,i,out))
 lines += ['## Getter calls','','| call | output local |','|---|---|']
 for idx,i,out in getter_calls:
  s='unknown' if not out else f'{out[0]}{out[1]:+#x}'
  lines.append(f'| `0x{i.address-base:08X}` | `{s}` |')
 # Known from prior body: full-copy destination around rsp+0x1A0. Detect SIMD/mov copy runs by same src/dst delta.
 lines += ['','## Timing-shaped accesses to plausible snapshot locals','','| RVA | base | record offset | label | instruction |','|---|---|---:|---|---|']
 # seed direct getter outputs plus detect likely copied bases from repeated same-size-offset moves
 bases=[]
 for _,_,out in getter_calls:
  if out:bases.append((out[0],out[1],'getter'))
 # Add known copy candidate bases inferred from LEA destinations near MOVUPS copy runs, but report them as candidates.
 # Enumerate stack/rbp displacements and score bases where multiple field offsets exist.
 memrefs=[]
 for idx,i in enumerate(arr):
  for op in i.operands:
   if op.type==X86_OP_MEM:
    bn=i.reg_name(op.mem.base)
    if bn in ('rsp','rbp'):memrefs.append((idx,i,bn,op.mem.disp))
 candidates={}
 for bn in ('rsp','rbp'):
  ds=[d for _,_,b0,d in memrefs if b0==bn]
  for d in ds:
   for off in LABELS:
    base0=d-off
    if -0x800<=base0<=0x1000:
     candidates[(bn,base0)]=candidates.get((bn,base0),0)+1
 for (bn,bs),score in sorted(candidates.items(),key=lambda kv:kv[1],reverse=True):
  if score<2:continue
  # only retain bases with actual accesses to >=2 distinct known field offsets
  offs=set()
  for _,_,b0,d in memrefs:
   if b0==bn and d-bs in LABELS:offs.add(d-bs)
  if len(offs)>=2:bases.append((bn,bs,'inferred'))
 seen=set()
 for bn,bs,kind in bases:
  if (bn,bs) in seen:continue
  seen.add((bn,bs))
  for idx,i,b0,d in memrefs:
   if b0!=bn:continue
   off=d-bs
   if off in LABELS:
    lines.append(f'| `0x{i.address-base:08X}` | `{bn}{bs:+#x}` ({kind}) | `+0x{off:X}` | {LABELS[off]} | `{i.mnemonic} {i.op_str}` |')
 # Calls with arguments that point into candidate snapshot locals or load known fields shortly before call.
 lines += ['','## Calls near snapshot/timing materialization','','| call | target | preceding window |','|---|---|---|']
 for idx,i in enumerate(arr):
  if i.mnemonic!='call':continue
  pre=arr[max(0,idx-14):idx]
  interesting=False
  for p in pre:
   for op in p.operands:
    if op.type==X86_OP_MEM:
     bn=p.reg_name(op.mem.base)
     for b0,bs,_ in bases:
      if bn==b0 and 0<=op.mem.disp-bs<SIZE:
       if op.mem.disp-bs in LABELS or p.mnemonic=='lea':interesting=True
  if not interesting:continue
  target=i.op_str
  if i.operands and i.operands[0].type==X86_OP_IMM:target=f'RVA 0x{i.operands[0].imm-base:08X}'
  win='; '.join(f'{p.mnemonic} {p.op_str}' for p in pre)
  lines.append(f'| `0x{i.address-base:08X}` | `{target}` | `{win}` |')
 lines += ['','## Full body','','```asm']
 for i in arr:lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
 lines += ['```']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'type1_slot50_transitive_snapshot.md').write_text('\n'.join(lines),encoding='utf-8')
 print('getter_calls',len(getter_calls),'candidate_bases',len(seen))
if __name__=='__main__':main()
