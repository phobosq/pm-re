#!/usr/bin/env python3
"""Trace local 0xD8 timing snapshots inside type1/type2 virtual slot +0x50 methods.

Confirmed getter callsites:
  type1 0x1689B0 -> snapshot rsp+0x1A0
  type1 0x1690C2 -> snapshot rsp+0x280
  type2 0x1CF954 -> snapshot rsp+0xB0
Static only; PhoenixMiner is never executed.
"""
from __future__ import annotations
import argparse,bisect
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_IMM,X86_OP_MEM,X86_REG_RSP

CASES=[
 ('type1_a',0x001689B0,0x1A0),
 ('type1_b',0x001690C2,0x280),
 ('type2',0x001CF954,0xB0),
]

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en: funcs.append((b,en))
 funcs.sort();starts=[b for b,_ in funcs]
 def fnof(r):
  j=bisect.bisect_right(starts,r)-1
  return funcs[j] if j>=0 and funcs[j][0]<=r<funcs[j][1] else None
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 lines=['# Backend snapshot handoffs','',
        'Type-safe seed: derived vtable slot `+0x50` methods call confirmed snapshot getter `0x084A60`.','']
 for name,cs,sbase in CASES:
  fn=fnof(cs)
  if not fn: continue
  b,en=fn;ins=list(md.disasm(pe.get_data(b,en-b),base+b))
  idx=next((k for k,i in enumerate(ins) if i.address-base==cs),None)
  if idx is None: continue
  lines += [f'## {name}: getter call `0x{cs:08X}` in `0x{b:08X}..0x{en:08X}` snapshot `rsp+0x{sbase:X}`','',
            '### Snapshot-related instructions after getter','']
  # Find direct stack references within snapshot range and LEAs of any address into that range.
  refs=[]
  for j,i in enumerate(ins[idx+1:],idx+1):
   for op in i.operands:
    if op.type==X86_OP_MEM and op.mem.base==X86_REG_RSP and sbase<=op.mem.disp<sbase+0xD8:
     refs.append((j,i,op.mem.disp-sbase))
     break
  for j,i,off in refs:
   lines.append(f'- `0x{i.address-base:08X}` snapshot+`0x{off:X}`: `{i.mnemonic} {i.op_str}`')
  lines += ['','### Calls after getter with pre-call context','']
  call_count=0
  for j in range(idx+1,len(ins)):
   i=ins[j]
   if i.mnemonic!='call': continue
   call_count+=1
   if i.operands and i.operands[0].type==X86_OP_IMM: tgt=f'RVA 0x{i.operands[0].imm-base:08X}'
   else: tgt=i.op_str
   lines += [f'#### call {call_count}: `0x{i.address-base:08X}` -> `{tgt}`','```asm']
   for w in ins[max(idx,j-10):j+2]: lines.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
   lines += ['```','']
   if call_count>=18: break
  lines += ['### Getter region full context','```asm']
  for i in ins[max(0,idx-20):min(len(ins),idx+180)]: lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'backend_snapshot_handoffs.md';p.write_text('\n'.join(lines),encoding='utf-8');print(p)
if __name__=='__main__':main()
