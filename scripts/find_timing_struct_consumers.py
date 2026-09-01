#!/usr/bin/env python3
"""Find PDATA functions reading >=3 confirmed timing fields from non-stack objects.
Confirmed per-GPU offsets: mt 0x98, straps 0xAC, vmr/rxboost 0xB0, vmt2 0xB8, vmt3 0xBC.
"""
from pathlib import Path
import argparse,pefile
from capstone import Cs,CsError,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM
FIELDS={0x98:'mt',0xac:'straps',0xb0:'vmr_rxboost',0xb8:'vmt2',0xbc:'vmt3'}
STACK={'rsp','rbp','esp','ebp'}
def safe(i):
 try:return i.operands
 except CsError:return ()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase;md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 pd=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.pdata').get_data();funcs=[]
 for o in range(0,len(pd)-11,12):
  b=int.from_bytes(pd[o:o+4],'little');e=int.from_bytes(pd[o+4:o+8],'little')
  if b and e>b:funcs.append((b,e))
 rows=[]
 for b,e in funcs:
  ins=list(md.disasm(pe.get_data(b,e-b),base+b));found={k:[] for k in FIELDS}
  for i in ins:
   oo=safe(i)
   for oi,op in enumerate(oo):
    if op.type!=X86_OP_MEM or op.mem.disp not in FIELDS or op.size!=4:continue
    bn=i.reg_name(op.mem.base) if op.mem.base else ''
    if not bn or bn in STACK:continue
    # reject plain memory destination MOV; everything else may read or RMW
    if oi==0 and i.mnemonic=='mov':continue
    found[op.mem.disp].append(i)
  n=sum(bool(x) for x in found.values())
  if n>=3:rows.append((n,b,e,found,ins))
 rows.sort(key=lambda r:(-r[0],r[1]))
 lines=['# Multi-field timing structure consumers','',f'functions reading >=3 confirmed fields: {len(rows)}','',
 '| fields | PDATA | matched |','|---:|---|---|']
 for n,b,e,f,ins in rows:
  names=', '.join(FIELDS[k] for k,v in f.items() if v);lines.append(f'| {n} | `0x{b:08X}..0x{e:08X}` | {names} |')
 lines+=['','## Candidate details','']
 for n,b,e,f,ins in rows:
  lines += [f'### {n} fields `0x{b:08X}..0x{e:08X}`','','Key accesses:']
  for k,v in f.items():
   for i in v:lines.append(f'- {FIELDS[k]} +0x{k:X}: `0x{i.address-base:08X}: {i.mnemonic} {i.op_str}`')
  lines += ['','```asm']
  for i in ins:lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'timing_struct_consumers.md').write_text('\n'.join(lines),encoding='utf-8')
 print('candidates',len(rows))
if __name__=='__main__':main()
