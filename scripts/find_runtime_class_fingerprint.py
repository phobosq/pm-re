#!/usr/bin/env python3
"""Trace materialization of confirmed snapshot bases (+0x368/+0x440) in derived runtime vtable methods.
For each hit, inspect the next direct callees for timing-record offsets such as +0xB0.
Static only.
"""
from __future__ import annotations
import argparse,bisect
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_OP_IMM
TYPE1=[0x1618B0,0x138970,0x132720,0x169AA0,0x1688B0,0x161DB0,0x168780,0x1688D0,0x169660,0x1620D0,0x1620F0,0x169F20,0x164350,0x169650,0x1688A0,0x161860,0x16AB50]
TYPE2=[0x1CDF70,0x138970,0x132720,0x1CF7C0,0x1CF8B0,0x1D0730,0x1CF890,0x1CDFB0,0x1CDFD0,0x1D0AD0,0x1CE0B0,0x1CFED0,0x1CF880]
SNAP={0x368:'snapshotA',0x440:'snapshotB'}
TIMING={0x98:'mt',0xAC:'straps',0xB0:'vmr_rxboost',0xB8:'vmt2',0xBC:'vmt3'}
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
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 cache={}
 def dec(fn):
  if fn not in cache:cache[fn]=list(md.disasm(pe.get_data(fn[0],fn[1]-fn[0]),base+fn[0]))
  return cache[fn]
 lines=['# Derived snapshot-base handoffs','', 'Seeds: confirmed derived vtable methods; snapshot bases `this+0x368` and `this+0x440`.','']
 hits=0
 for label,roots in [('type1',TYPE1),('type2',TYPE2)]:
  lines += [f'## {label}','']
  for root in roots:
   fn=fnof(root)
   if not fn: continue
   arr=dec(fn)
   for k,i in enumerate(arr):
    found=[]
    for op in i.operands:
     if op.type==X86_OP_MEM and op.mem.disp in SNAP:found.append(op.mem.disp)
    if not found:continue
    hits+=1
    lines += [f'### method `0x{root:08X}` hit `0x{i.address-base:08X}` {", ".join(SNAP[o] for o in found)}','','```asm']
    for w in arr[max(0,k-12):min(len(arr),k+20)]:lines.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
    lines += ['```','','Next direct callees:','']
    n=0
    for c in arr[k+1:]:
     if c.mnemonic!='call' or not c.operands or c.operands[0].type!=X86_OP_IMM:continue
     tr=c.operands[0].imm-base; cf=fnof(tr)
     lines.append(f'- call `0x{c.address-base:08X}` -> `0x{tr:08X}`')
     if cf:
      th=[]
      for x in dec(cf):
       for op in x.operands:
        if op.type==X86_OP_MEM and op.mem.disp in TIMING:
         th.append((x,op.mem.disp))
      if th:
       lines.append('  - timing-offset accesses in callee:')
       for x,o in th[:20]:lines.append(f'    - `{TIMING[o]}` `+0x{o:X}` at `0x{x.address-base:08X}: {x.mnemonic} {x.op_str}`')
     n+=1
     if n>=4:break
    lines += ['']
 lines.insert(3,f'snapshot-base hits: {hits}')
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'runtime_class_fingerprint.md';p.write_text('\n'.join(lines),encoding='utf-8');print('hits',hits)
if __name__=='__main__':main()
