#!/usr/bin/env python3
"""Trace original per-GPU config record accesses in NVIDIA child ctor 0x1D4A80.
Entry R9 is the config-record pointer; ctor copies it to RSI. Static only.
"""
from __future__ import annotations
import argparse,bisect
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_OP_IMM
TARGET=0x001D4A80
TIMING={0x98:'mt',0xAC:'straps',0xB0:'vmr/rxboost',0xB8:'vmt2',0xBC:'vmt3'}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en:funcs.append((b,en))
 funcs.sort();starts=[b for b,_ in funcs]
 j=bisect.bisect_right(starts,TARGET)-1;fn=funcs[j]
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 arr=list(md.disasm(pe.get_data(fn[0],fn[1]-fn[0]),base+fn[0]))
 # entry R9 is saved to RSI at 0x1D4AB6; treat rsi as config pointer.
 hits=[]
 for k,i in enumerate(arr):
  for op in i.operands:
   if op.type==X86_OP_MEM and i.reg_name(op.mem.base)=='rsi':hits.append((k,i,op.mem.disp,TIMING.get(op.mem.disp,'')))
 lines=['# NVIDIA child ctor config-record accesses','',f'PDATA `0x{fn[0]:08X}..0x{fn[1]:08X}`','',
        'Entry `R9` is copied to `RSI`; `RSI` therefore aliases the original per-GPU `0xD8` config record.','',
        '| RVA | disp | timing label | instruction |','|---|---:|---|---|']
 for k,i,d,lab in hits:lines.append(f'| `0x{i.address-base:08X}` | `0x{d:X}` | {lab} | `{i.mnemonic} {i.op_str}` |')
 lines += ['','## Timing-field contexts','']
 for k,i,d,lab in hits:
  if not lab:continue
  lines += [f'### {lab} +0x{d:X} at `0x{i.address-base:08X}`','','```asm']
  for w in arr[max(0,k-35):min(len(arr),k+60)]:lines.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'nvidia_child_config_reads.md';p.write_text('\n'.join(lines),encoding='utf-8');print('config_hits',len(hits),'timing_hits',sum(bool(x[3]) for x in hits))
if __name__=='__main__':main()
