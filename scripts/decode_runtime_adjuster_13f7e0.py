#!/usr/bin/env python3
"""Decode type-safe runtime snapshot adjuster 0x13F7E0.

This function is a direct caller of both runtime-object getter 0x084A60 and
setter 0x1362D0, and is reached from 0x6FCE0 immediately after config merge.
Static only; target binary is never executed.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_IMM,X86_OP_MEM
B=0x0013F7E0; E=0x0013FCC0
FIELDS={0x98:'mt',0xac:'straps',0xb0:'vmr_rxboost',0xb8:'vmt2',0xbc:'vmt3'}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 ins=list(md.disasm(pe.get_data(B,E-B),base+B))
 lines=['# Runtime adjuster 0x13F7E0','', 'Type-safe: calls getter `0x084A60` and setter `0x1362D0` on the same runtime object.','',
        '## Timing-field accesses','','| RVA | field | instruction |','|---|---|---|']
 hits=[]
 for idx,i in enumerate(ins):
  for op in i.operands:
   if op.type==X86_OP_MEM and op.mem.disp in FIELDS:
    hits.append((idx,i,FIELDS[op.mem.disp],op.mem.disp)); lines.append(f'| `0x{i.address-base:08X}` | {FIELDS[op.mem.disp]} `+0x{op.mem.disp:X}` | `{i.mnemonic} {i.op_str}` |')
 lines += ['','## Full function','','```asm']
 for i in ins:lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
 lines += ['```','','## Calls','','| RVA | target/form |','|---|---|']
 for i in ins:
  if i.mnemonic!='call':continue
  t=i.op_str
  if i.operands and i.operands[0].type==X86_OP_IMM:t=f'RVA 0x{i.operands[0].imm-base:08X}'
  lines.append(f'| `0x{i.address-base:08X}` | `{t}` |')
 lines += ['','## Timing access contexts','']
 for idx,i,n,o in hits:
  lines += [f'### {n} @ `0x{i.address-base:08X}`','','```asm']
  for w in ins[max(0,idx-14):min(len(ins),idx+22)]:lines.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'runtime_adjuster_13f7e0.md').write_text('\n'.join(lines),encoding='utf-8')
 print('timing_hits',len(hits))
if __name__=='__main__':main()
