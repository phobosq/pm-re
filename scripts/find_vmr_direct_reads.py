#!/usr/bin/env python3
"""Find read-side accesses to dword [object + 0xB0], excluding stack locals.
Static only. Ranks candidates and maps them to PDATA functions.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import pefile
from capstone import Cs,CsError,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_OP_REG

STACK={'rsp','rbp','esp','ebp'}

def safe_ops(i):
 try:return i.operands
 except CsError:return ()

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 text=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.text')
 pdata=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.pdata').get_data()
 funcs=[]
 for o in range(0,len(pdata)-11,12):
  b=int.from_bytes(pdata[o:o+4],'little');e=int.from_bytes(pdata[o+4:o+8],'little')
  if b and e>b:funcs.append((b,e))
 def fn(rva):
  lo,hi=0,len(funcs)-1
  while lo<=hi:
   m=(lo+hi)//2;b,e=funcs[m]
   if rva<b:hi=m-1
   elif rva>=e:lo=m+1
   else:return b,e
  return None
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True;md.skipdata=True
 ins=list(md.disasm(text.get_data(),base+text.VirtualAddress))
 hits=[]
 for idx,i in enumerate(ins):
  ops=safe_ops(i)
  if not ops:continue
  for oi,op in enumerate(ops):
   if op.type!=X86_OP_MEM or op.mem.disp!=0xb0 or op.size!=4:continue
   bn=i.reg_name(op.mem.base) if op.mem.base else ''
   if bn in STACK or not bn:continue
   # read if memory operand is not a pure destination for common write mnemonics
   pure_write=(oi==0 and i.mnemonic in {'mov','movzx','movsx','lea','inc','dec','add','sub','and','or','xor'})
   if pure_write and i.mnemonic=='mov':continue
   score=2
   if i.mnemonic in {'cmp','test'}:score+=2
   if oi>0:score+=2
   f=fn(i.address-base)
   hits.append((score,idx,bn,f))
 hits.sort(key=lambda x:(-x[0],ins[x[1]].address))
 lines=['# Direct VMR +0xB0 read candidates','',f'non-stack dword read candidates: {len(hits)}','',
 '| score | RVA | PDATA | instruction |','|---:|---|---|---|']
 for score,idx,bn,f in hits:
  i=ins[idx];fs=f'0x{f[0]:08X}..0x{f[1]:08X}' if f else 'none'
  lines.append(f'| {score} | `0x{i.address-base:08X}` | `{fs}` | `{i.mnemonic} {i.op_str}` |')
 lines+=['','## Top candidate contexts','']
 for score,idx,bn,f in hits[:40]:
  i=ins[idx];lines += [f'### `0x{i.address-base:08X}` score {score} base `{bn}`','','```asm']
  for w in ins[max(0,idx-10):min(len(ins),idx+14)]:lines.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
  lines+=['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'vmr_direct_reads.md').write_text('\n'.join(lines),encoding='utf-8')
 print('hits',len(hits))
if __name__=='__main__':main()
