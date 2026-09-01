#!/usr/bin/env python3
"""Decode 0x1362D0, first confirmed handoff of a merged 0xD8 per-GPU snapshot.
Static only; target binary is never executed.
"""
from __future__ import annotations
import argparse,bisect
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_OP_IMM
TARGET=0x001362D0

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en: funcs.append((b,en))
 funcs.sort();starts=[b for b,_ in funcs]
 j=bisect.bisect_right(starts,TARGET)-1
 fn=funcs[j] if j>=0 and funcs[j][0]<=TARGET<funcs[j][1] else (TARGET,TARGET+0x800)
 b,en=fn
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 ins=list(md.disasm(pe.get_data(b,en-b),base+b))
 fields={0x98:'mt',0xac:'straps',0xb0:'vmr_rxboost',0xb8:'vmt2',0xbc:'vmt3'}
 lines=['# Handoff consumer 0x1362D0','',f'PDATA: `0x{b:08X}..0x{en:08X}`','',
        'Confirmed callsite `0x6FCC2`: `RCX=r15`, `RDX=&merged_per_gpu_snapshot`.','',
        '## Timing-related memory accesses','','| RVA | field | instruction |','|---|---|---|']
 hits=[]
 for idx,i in enumerate(ins):
  for op in i.operands:
   if op.type==X86_OP_MEM and op.mem.disp in fields:
    hits.append((idx,i,fields[op.mem.disp]));lines.append(f'| `0x{i.address-base:08X}` | {fields[op.mem.disp]} `+0x{op.mem.disp:X}` | `{i.mnemonic} {i.op_str}` |')
 lines += ['','## Full function','','```asm']
 for i in ins: lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
 lines += ['```','','## Calls','','| RVA | target/form |','|---|---|']
 for i in ins:
  if i.mnemonic!='call': continue
  t=i.op_str
  if i.operands and i.operands[0].type==X86_OP_IMM:t=f'RVA 0x{i.operands[0].imm-base:08X}'
  lines.append(f'| `0x{i.address-base:08X}` | `{t}` |')
 lines += ['','## Field contexts','']
 for idx,i,n in hits:
  lines += [f'### {n} @ `0x{i.address-base:08X}`','','```asm']
  for w in ins[max(0,idx-10):min(len(ins),idx+16)]:lines.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'handoff_1362d0.md').write_text('\n'.join(lines),encoding='utf-8')
 print(f'fn=0x{b:X}..0x{en:X} hits={len(hits)}')
if __name__=='__main__':main()
