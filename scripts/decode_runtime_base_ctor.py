#!/usr/bin/env python3
"""Decode runtime base ctor 0x12F250 and locate config-record copy/use.
Static only.
"""
from __future__ import annotations
import argparse,bisect
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_OP_IMM
TARGET=0x0012F250
INTEREST={0x90:'context',0x318:'lock',0x368:'snapshotA',0x418:'vmrA',0x440:'snapshotB',0x4F0:'vmrB',0x538:'counter',0x98:'mt',0xAC:'straps',0xB0:'vmr/rxboost',0xB8:'vmt2',0xBC:'vmt3'}
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
 fn=fnof(TARGET);lines=[f'# Runtime base ctor 0x{TARGET:08X}',f'',f'PDATA: `{("0x%08X..0x%08X"%fn) if fn else "none"}`','']
 if fn:
  arr=list(md.disasm(pe.get_data(fn[0],fn[1]-fn[0]),base+fn[0]))
  lines += ['## Calls / interesting accesses','', '| RVA | kind | instruction |','|---|---|---|']
  for i in arr:
   for op in i.operands:
    if op.type==X86_OP_MEM and op.mem.disp in INTEREST:
     lines.append(f'| `0x{i.address-base:08X}` | {INTEREST[op.mem.disp]} | `{i.mnemonic} {i.op_str}` |')
   if i.mnemonic=='call':
    if i.operands and i.operands[0].type==X86_OP_IMM:form=f'direct 0x{i.operands[0].imm-base:08X}'
    else:form='indirect '+i.op_str
    lines.append(f'| `0x{i.address-base:08X}` | call | `{form}` |')
  lines += ['','## Full disassembly','```asm']
  for i in arr:lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
  lines += ['```']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'runtime_base_ctor.md';p.write_text('\n'.join(lines),encoding='utf-8');print(p)
if __name__=='__main__':main()
