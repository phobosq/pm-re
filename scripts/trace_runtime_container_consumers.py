#!/usr/bin/env python3
"""Trace callers of runtime-object container accessor 0x13C5A0.
Focus on object extraction, direct config reads and virtual calls. Static only.
"""
from __future__ import annotations
import argparse,bisect
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_IMM,X86_OP_MEM
TARGET=0x0013C5A0
INTEREST={0x368:'snapshotA',0x418:'vmrA',0x440:'snapshotB',0x4F0:'vmrB',0x90:'context'}
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
 hits=[]
 for fn in funcs:
  arr=list(md.disasm(pe.get_data(fn[0],fn[1]-fn[0]),base+fn[0]))
  for k,i in enumerate(arr):
   if i.mnemonic=='call' and i.operands and i.operands[0].type==X86_OP_IMM and i.operands[0].imm-base==TARGET:
    hits.append((fn,arr,k))
 lines=['# Runtime container consumers via 0x13C5A0','',f'direct callers: {len(hits)}','']
 for fn,arr,k in hits:
  cs=arr[k].address-base
  lines += [f'## call `0x{cs:08X}` in `0x{fn[0]:08X}..0x{fn[1]:08X}`','','```asm']
  for i in arr[max(0,k-20):min(len(arr),k+130)]:lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
  lines += ['```','','### Interesting accesses/calls after accessor','', '| RVA | kind | instruction |','|---|---|---|']
  for i in arr[k+1:min(len(arr),k+160)]:
   tagged=[]
   for op in i.operands:
    if op.type==X86_OP_MEM and op.mem.disp in INTEREST:tagged.append(INTEREST[op.mem.disp])
   if tagged:lines.append(f'| `0x{i.address-base:08X}` | {"/".join(tagged)} | `{i.mnemonic} {i.op_str}` |')
   if i.mnemonic=='call':
    form=i.op_str
    if i.operands and i.operands[0].type==X86_OP_IMM:form=f'direct 0x{i.operands[0].imm-base:08X}'
    else:form='indirect '+form
    lines.append(f'| `0x{i.address-base:08X}` | call | `{form}` |')
  lines += ['']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'runtime_container_consumers.md';p.write_text('\n'.join(lines),encoding='utf-8');print('callers',len(hits))
if __name__=='__main__':main()
