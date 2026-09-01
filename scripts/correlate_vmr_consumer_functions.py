#!/usr/bin/env python3
"""Correlate VMR structure features at PDATA-function granularity.
Features: owner+0x2C0 access, IMUL 0xD8, non-stack dword +0xB0 read.
Static only.
"""
from pathlib import Path
import argparse,pefile
from capstone import Cs,CsError,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_OP_IMM
STACK={'rsp','rbp','esp','ebp'}
def ops(i):
 try:return i.operands
 except CsError:return ()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 pdata=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.pdata').get_data()
 funcs=[]
 for o in range(0,len(pdata)-11,12):
  b=int.from_bytes(pdata[o:o+4],'little');e=int.from_bytes(pdata[o+4:o+8],'little')
  if b and e>b:funcs.append((b,e))
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 rows=[]
 for b,e in funcs:
  ins=list(md.disasm(pe.get_data(b,e-b),base+b))
  f2c0=[];fd8=[];fb0=[]
  for i in ins:
   oo=ops(i)
   for oi,op in enumerate(oo):
    if op.type==X86_OP_MEM:
     bn=i.reg_name(op.mem.base) if op.mem.base else ''
     if op.mem.disp==0x2c0:f2c0.append(i)
     if op.mem.disp==0xb0 and op.size==4 and bn not in STACK and bn:
      # accept obvious reads/comparisons/arithmetic; reject plain MOV destination
      if not(oi==0 and i.mnemonic=='mov'):fb0.append(i)
      elif oi>0:fb0.append(i)
    if op.type==X86_OP_IMM and i.mnemonic=='imul' and (op.imm & 0xffffffffffffffff)==0xd8:fd8.append(i)
  score=(4 if f2c0 else 0)+(4 if fd8 else 0)+(5 if fb0 else 0)
  if score>=8 or (f2c0 and fb0):rows.append((score,b,e,f2c0,fd8,fb0,ins))
 rows.sort(key=lambda r:(-r[0],r[1]))
 lines=['# VMR consumer function correlation','',f'candidate functions: {len(rows)}','',
 '| score | PDATA | +0x2C0 | imul 0xD8 | +0xB0 reads |','|---:|---|---:|---:|---:|']
 for sc,b,e,a2,ad,ab,ins in rows:lines.append(f'| {sc} | `0x{b:08X}..0x{e:08X}` | {len(a2)} | {len(ad)} | {len(ab)} |')
 lines+=['','## Exact/high candidates','']
 for sc,b,e,a2,ad,ab,ins in rows[:25]:
  lines += [f'### score {sc} `0x{b:08X}..0x{e:08X}`','','Key instructions:','']
  for i in a2:lines.append(f'- owner: `0x{i.address-base:08X}: {i.mnemonic} {i.op_str}`')
  for i in ad:lines.append(f'- stride: `0x{i.address-base:08X}: {i.mnemonic} {i.op_str}`')
  for i in ab:lines.append(f'- vmr-read: `0x{i.address-base:08X}: {i.mnemonic} {i.op_str}`')
  if sc>=13:
   lines += ['','```asm']
   for i in ins:lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
   lines += ['```']
  lines.append('')
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'vmr_consumer_function_correlation.md').write_text('\n'.join(lines),encoding='utf-8')
 print('candidates',len(rows),'exact',sum(1 for r in rows if r[0]>=13))
if __name__=='__main__':main()
