#!/usr/bin/env python3
"""Decode two high-value runtime-container consumer hotspots.
Static only. Focus: object provenance, vtable calls, timing-related offsets.
"""
from __future__ import annotations
import argparse,bisect
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_OP_IMM
TARGETS=[0x00074AB0,0x00086C60]
INTEREST={0x90:'context',0x98:'mt',0xAC:'straps',0xB0:'vmr/rxboost',0xB8:'vmt2',0xBC:'vmt3',0x368:'snapshotA',0x418:'vmrA',0x440:'snapshotB',0x4F0:'vmrB',0x538:'counter'}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en:funcs.append((b,en))
 funcs.sort(); starts=[b for b,_ in funcs]
 def fnof(r):
  j=bisect.bisect_right(starts,r)-1
  return funcs[j] if j>=0 and funcs[j][0]<=r<funcs[j][1] else None
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 lines=['# Runtime container hotspot decode','']
 for t in TARGETS:
  fn=fnof(t) or next((x for x in funcs if x[0]==t),None)
  lines += [f'## PDATA `{("0x%08X..0x%08X"%fn) if fn else "none"}`','']
  if not fn:continue
  arr=list(md.disasm(pe.get_data(fn[0],fn[1]-fn[0]),base+fn[0]))
  lines += ['### Calls and timing-shaped accesses','', '| RVA | kind | instruction |','|---|---|---|']
  for i in arr:
   tags=[]
   for op in i.operands:
    if op.type==X86_OP_MEM and op.mem.disp in INTEREST: tags.append(INTEREST[op.mem.disp])
   if tags:lines.append(f'| `0x{i.address-base:08X}` | {"/".join(tags)} | `{i.mnemonic} {i.op_str}` |')
   if i.mnemonic=='call':
    if i.operands and i.operands[0].type==X86_OP_IMM: form=f'direct 0x{i.operands[0].imm-base:08X}'
    else: form='indirect '+i.op_str
    lines.append(f'| `0x{i.address-base:08X}` | call | `{form}` |')
  # full windows around indirect calls
  for k,i in enumerate(arr):
   if i.mnemonic=='call' and not (i.operands and i.operands[0].type==X86_OP_IMM):
    lines += ['',f'### indirect call `0x{i.address-base:08X}` — `{i.op_str}`','','```asm']
    for w in arr[max(0,k-45):min(len(arr),k+30)]: lines.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
    lines += ['```']
  lines += ['']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'runtime_container_hotspots.md';p.write_text('\n'.join(lines),encoding='utf-8');print(p)
if __name__=='__main__':main()
