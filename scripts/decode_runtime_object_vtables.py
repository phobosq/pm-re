#!/usr/bin/env python3
"""Decode confirmed runtime-object base/derived vtables and method bodies.
Static only; PhoenixMiner is never executed.
"""
from __future__ import annotations
import argparse,bisect,struct
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_IMM,X86_OP_MEM

VTABLES={0x00440528:'ctor_base_vtable',0x00440560:'derived_vtable'}
MAX_ENTRIES=40

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 text=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.text')
 text_lo=text.VirtualAddress;text_hi=text.VirtualAddress+max(text.Misc_VirtualSize,text.SizeOfRawData)
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en: funcs.append((b,en))
 funcs.sort();starts=[b for b,_ in funcs]
 def fnof(r):
  j=bisect.bisect_right(starts,r)-1
  return funcs[j] if j>=0 and funcs[j][0]<=r<funcs[j][1] else None
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 # all text instructions only for xrefs to vtable addresses
 all_ins=list(md.disasm(text.get_data(),base+text.VirtualAddress))
 lines=['# Runtime object vtables','',
        'Confirmed ctor writes: `[this]=0x440528` then `[this]=0x440560`.','']
 all_methods=[]
 for vrva,name in VTABLES.items():
  lines += [f'## {name} `RVA 0x{vrva:08X}`','', '| slot | qword | method RVA | PDATA |','|---:|---|---|---|']
  nontext=0
  entries=[]
  raw=pe.get_data(vrva,MAX_ENTRIES*8)
  for idx in range(min(MAX_ENTRIES,len(raw)//8)):
   val=struct.unpack_from('<Q',raw,idx*8)[0]
   mrva=val-base if base <= val < base+pe.OPTIONAL_HEADER.SizeOfImage else None
   if mrva is not None and text_lo <= mrva < text_hi:
    nontext=0;fn=fnof(mrva);p='none' if not fn else f'0x{fn[0]:08X}..0x{fn[1]:08X}'
    lines.append(f'| {idx} (`+0x{idx*8:X}`) | `0x{val:016X}` | `0x{mrva:08X}` | `{p}` |')
    entries.append((idx,mrva,fn));all_methods.append((name,idx,mrva,fn))
   else:
    nontext+=1
    shown='-' if mrva is None else f'0x{mrva:08X}'
    lines.append(f'| {idx} (`+0x{idx*8:X}`) | `0x{val:016X}` | `{shown}` | non-text |')
    if idx>=2 and nontext>=3: break
  lines += ['','### Code xrefs to vtable address','']
  target=base+vrva
  xrefs=[]
  for i in all_ins:
   # RIP-relative LEA/MOV whose effective address is the vtable VA.
   for op in i.operands:
    if op.type==X86_OP_MEM and op.mem.base:
     # x86 RIP reg id differs by capstone build; use textual '[rip +' plus computed next+disp.
     if 'rip' in i.op_str.lower():
      eff=i.address+i.size+op.mem.disp
      if eff==target: xrefs.append(i)
  for i in xrefs: lines.append(f'- `0x{i.address-base:08X}`: `{i.mnemonic} {i.op_str}` in `{fnof(i.address-base)}`')
  lines.append('')

 # Unique method details
 seen=set(); lines += ['## Virtual method details','']
 for name,slot,mrva,fn in all_methods:
  if mrva in seen: continue
  seen.add(mrva)
  if not fn: continue
  b,en=fn;ins=list(md.disasm(pe.get_data(b,en-b),base+b))
  lines += [f'### method `0x{mrva:08X}` PDATA `0x{b:08X}..0x{en:08X}`','','Vtable slots:']
  for n,s,m,f in all_methods:
   if m==mrva: lines.append(f'- {n} slot {s} (`+0x{s*8:X}`)')
  lines += ['','Calls:']
  for i in ins:
   if i.mnemonic!='call': continue
   if i.operands and i.operands[0].type==X86_OP_IMM: lines.append(f'- `0x{i.address-base:08X}` -> `0x{i.operands[0].imm-base:08X}`')
   else: lines.append(f'- `0x{i.address-base:08X}` -> `{i.op_str}`')
  lines += ['','Body:','```asm']
  for i in ins: lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'runtime_object_vtables.md';p.write_text('\n'.join(lines),encoding='utf-8');print(p)
if __name__=='__main__':main()
