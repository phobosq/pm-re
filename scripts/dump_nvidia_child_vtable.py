#!/usr/bin/env python3
"""Dump NVIDIA child object's vtable at RVA 0x4BDE70 and profile methods.
Static only; target binary is never executed.
"""
from __future__ import annotations
import argparse,bisect,struct
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_OP_IMM
VT=0x004BDE70
MAX=40

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en:funcs.append((b,en))
 funcs.sort();starts=[b for b,_ in funcs]
 def fnof(r):
  j=bisect.bisect_right(starts,r)-1
  return funcs[j] if j>=0 and funcs[j][0]<=r<funcs[j][1] else None
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 raw=pe.get_data(VT,MAX*8)
 entries=[]
 for n in range(MAX):
  va=struct.unpack_from('<Q',raw,n*8)[0];rva=va-base if base<=va<base+pe.OPTIONAL_HEADER.SizeOfImage else None
  if rva is None or not any(s.VirtualAddress<=rva<s.VirtualAddress+max(s.Misc_VirtualSize,s.SizeOfRawData) and s.Name.rstrip(b'\0')==b'.text' for s in pe.sections):
   if n>=4:break
   entries.append((n,va,rva,None));continue
  entries.append((n,va,rva,fnof(rva)))
 lines=['# NVIDIA child vtable 0x004BDE70','', '| slot | target RVA | PDATA |','|---:|---|---|']
 for n,va,r,fn in entries:
  lines.append(f'| `+0x{n*8:X}` | {"-" if r is None else f"`0x{r:08X}`"} | {"none" if not fn else f"`0x{fn[0]:08X}..0x{fn[1]:08X}`"} |')
 for n,va,r,fn in entries:
  if r is None:continue
  b,en=fn or (r,r+0x300);arr=list(md.disasm(pe.get_data(b,en-b),base+b))
  lines += ['',f'## slot `+0x{n*8:X}` -> `0x{r:08X}`','','### Calls','','| RVA | target/form |','|---|---|']
  for i in arr:
   if i.mnemonic not in ('call','jmp'):continue
   f=i.op_str
   if i.operands and i.operands[0].type==X86_OP_IMM:f=f'RVA 0x{i.operands[0].imm-base:08X}'
   lines.append(f'| `0x{i.address-base:08X}` | `{i.mnemonic} {f}` |')
  lines += ['','### this-like field accesses','','| RVA | instruction |','|---|---|']
  aliases={'rcx'}
  # simple aliases from entry rcx to common callee-saved regs
  for i in arr[:20]:
   if i.mnemonic=='mov' and len(i.operands)==2 and i.reg_name(i.operands[1].reg) in aliases if i.operands[1].type==1 else False:
    aliases.add(i.reg_name(i.operands[0].reg))
  for i in arr:
   for op in i.operands:
    if op.type==X86_OP_MEM and i.reg_name(op.mem.base) in aliases and op.mem.disp:
      lines.append(f'| `0x{i.address-base:08X}` | `{i.mnemonic} {i.op_str}` |');break
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'nvidia_child_vtable.md').write_text('\n'.join(lines),encoding='utf-8')
 print('entries',len(entries))
if __name__=='__main__':main()
