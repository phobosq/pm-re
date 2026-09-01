#!/usr/bin/env python3
"""Profile NVIDIA child object ctor 0x1D4A80 and wrapper-target methods.
Static analysis only; PhoenixMiner is never executed.
"""
from __future__ import annotations
import argparse,bisect,struct
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_OP_IMM,X86_REG_RIP

TARGETS=[0x001D4A80,0x001EED90,0x001F0120,0x001F0960]

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en:funcs.append((b,en))
 funcs.sort();starts=[b for b,_ in funcs]
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 def fnof(r):
  j=bisect.bisect_right(starts,r)-1
  return funcs[j] if j>=0 and funcs[j][0]<=r<funcs[j][1] else (r,r+0x400)
 lines=['# NVIDIA child object profile','']
 vtable_candidates=[]
 for t in TARGETS:
  b,en=fnof(t);arr=list(md.disasm(pe.get_data(b,en-b),base+b))
  lines += [f'## target `0x{t:08X}` PDATA `0x{b:08X}..0x{en:08X}`','','### Calls','','| RVA | target/form |','|---|---|']
  for i in arr:
   if i.mnemonic=='call' or i.mnemonic=='jmp':
    form=i.op_str
    if i.operands and i.operands[0].type==X86_OP_IMM:form=f'RVA 0x{i.operands[0].imm-base:08X}'
    lines.append(f'| `0x{i.address-base:08X}` | `{i.mnemonic} {form}` |')
  lines += ['','### Object / RIP-relative accesses','','| RVA | instruction | note |','|---|---|---|']
  for i in arr:
   note=''
   for op in i.operands:
    if op.type!=X86_OP_MEM:continue
    bn=i.reg_name(op.mem.base)
    if bn in ('rcx','rdi','rsi','rbx','r14','r15') and op.mem.disp:
      note=f'{bn}{op.mem.disp:+#x}'
    if op.mem.base==X86_REG_RIP:
      va=i.address+i.size+op.mem.disp;rva=va-base
      note=(note+'; ' if note else '')+f'RIP->0x{rva:08X}'
   if note: lines.append(f'| `0x{i.address-base:08X}` | `{i.mnemonic} {i.op_str}` | {note} |')
   # ctor pattern lea reg,[rip+...] followed soon by mov [obj],reg
  lines += ['','### Full body','','```asm']
  for i in arr:lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'nvidia_child_object_profile.md').write_text('\n'.join(lines),encoding='utf-8')
if __name__=='__main__':main()
