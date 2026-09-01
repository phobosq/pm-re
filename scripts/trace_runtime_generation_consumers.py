#!/usr/bin/env python3
"""Trace accesses to confirmed runtime generation/change field this+0x538.
Static only. Prioritize non-stack bases and nearby calls.
"""
from __future__ import annotations
import argparse,bisect
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64,CS_AC_READ,CS_AC_WRITE
from capstone.x86 import X86_OP_MEM,X86_REG_RSP,X86_REG_RBP,X86_OP_IMM
OFF=0x538
TYPE2={0x001CDF70,0x00067840,0x00138970,0x00132720,0x0036EFD0,0x001CF7C0,0x001CF8B0,0x001D0730,0x001CF890,0x001CDFB0,0x001CDFD0,0x001D0AD0,0x001CE0B0,0x001CFED0,0x001CF880}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en:funcs.append((b,en))
 funcs.sort();starts=[b for b,_ in funcs]
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 hits=[]
 for fn in funcs:
  arr=list(md.disasm(pe.get_data(fn[0],fn[1]-fn[0]),base+fn[0]))
  for k,i in enumerate(arr):
   for op in i.operands:
    if op.type==X86_OP_MEM and op.mem.disp==OFF:
     acc=[]
     if op.access & CS_AC_READ:acc.append('R')
     if op.access & CS_AC_WRITE:acc.append('W')
     br=i.reg_name(op.mem.base) if op.mem.base else ''
     hits.append((fn,arr,k,i,''.join(acc) or '?',br,op.mem.base in (X86_REG_RSP,X86_REG_RBP)))
 lines=['# Runtime generation +0x538 consumers','',f'hits: {len(hits)}','', '| RVA | PDATA | access | base | stack? | type2 method? | instruction |','|---|---|---|---|---:|---:|---|']
 for fn,arr,k,i,acc,br,stack in hits:
  lines.append(f'| `0x{i.address-base:08X}` | `0x{fn[0]:08X}..0x{fn[1]:08X}` | {acc} | `{br}` | {stack} | {fn[0] in TYPE2} | `{i.mnemonic} {i.op_str}` |')
 lines += ['','## Non-stack read contexts','']
 for fn,arr,k,i,acc,br,stack in hits:
  if stack or 'R' not in acc:continue
  lines += [f'### `0x{i.address-base:08X}` in `0x{fn[0]:08X}..0x{fn[1]:08X}` base `{br}` type2={fn[0] in TYPE2}','','```asm']
  for w in arr[max(0,k-45):min(len(arr),k+65)]:lines.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
  lines += ['```','','Nearby calls:']
  for w in arr[max(0,k-45):min(len(arr),k+65)]:
   if w.mnemonic=='call':
    if w.operands and w.operands[0].type==X86_OP_IMM:t=f'0x{w.operands[0].imm-base:08X}'
    else:t=w.op_str
    lines.append(f'- `0x{w.address-base:08X}` -> `{t}`')
  lines += ['']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'runtime_generation_consumers.md';p.write_text('\n'.join(lines),encoding='utf-8');print('hits',len(hits))
if __name__=='__main__':main()
