#!/usr/bin/env python3
"""Trace callers of confirmed runtime snapshot getter 0x84A60 and identify reads of snapshot+0xB0.
Static only. The target binary is never executed.
"""
from __future__ import annotations
import argparse,bisect,re
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_IMM,X86_OP_MEM,X86_REG_RSP,X86_REG_RBP
GETTER=0x00084A60

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en: funcs.append((b,en))
 funcs.sort(); starts=[b for b,_ in funcs]
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 hits=[]
 for fn in funcs:
  arr=list(md.disasm(pe.get_data(fn[0],fn[1]-fn[0]),base+fn[0]))
  for k,i in enumerate(arr):
   if not (i.mnemonic=='call' and i.operands and i.operands[0].type==X86_OP_IMM and i.operands[0].imm-base==GETTER): continue
   # infer most recent LEA RDX,[rsp/rbp+disp]
   out_base=None;out_reg=None;out_ins=None
   for w in reversed(arr[max(0,k-24):k]):
    if w.mnemonic=='lea' and len(w.operands)>=2 and w.reg_name(w.operands[0].reg)=='rdx' and w.operands[1].type==X86_OP_MEM:
     m=w.operands[1].mem
     if m.base in (X86_REG_RSP,X86_REG_RBP):
      out_base=m.disp;out_reg=m.base;out_ins=w;break
   consumers=[]
   if out_base is not None:
    target_disp=out_base+0xB0
    for j in range(k+1,min(len(arr),k+220)):
     w=arr[j]
     for op in w.operands:
      if op.type==X86_OP_MEM and op.mem.base==out_reg and op.mem.disp==target_disp:
       consumers.append((j,w,'snapshot+0xB0'))
   hits.append((fn,arr,k,i,out_base,out_reg,out_ins,consumers))
 lines=['# Snapshot getter VMR consumers','',f'getter: `0x{GETTER:08X}`; calls: {len(hits)}','',
        '| call | PDATA | output local | +0xB0 consumers |','|---|---|---|---:|']
 for fn,arr,k,i,ob,oreg,oi,cons in hits:
  local='unknown' if ob is None else f'{arr[k].reg_name(oreg)}{ob:+#x}'
  lines.append(f'| `0x{i.address-base:08X}` | `0x{fn[0]:08X}..0x{fn[1]:08X}` | `{local}` | {len(cons)} |')
 lines += ['','## Calls with snapshot+0xB0 consumers','']
 for fn,arr,k,i,ob,oreg,oi,cons in hits:
  if not cons: continue
  lines += [f'### getter call `0x{i.address-base:08X}` in `0x{fn[0]:08X}..0x{fn[1]:08X}`','']
  if oi: lines.append(f'output setup: `0x{oi.address-base:08X}: {oi.mnemonic} {oi.op_str}`')
  lines += ['','Consumers:']
  for j,w,label in cons: lines.append(f'- `0x{w.address-base:08X}`: `{w.mnemonic} {w.op_str}`')
  lo=max(0,k-18); hi=min(len(arr),max([x[0] for x in cons])+45)
  lines += ['','```asm']
  for w in arr[lo:hi]:lines.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'snapshot_vmr_consumers.md';p.write_text('\n'.join(lines),encoding='utf-8');print('calls',len(hits),'with_consumers',sum(bool(h[-1]) for h in hits))
if __name__=='__main__':main()
