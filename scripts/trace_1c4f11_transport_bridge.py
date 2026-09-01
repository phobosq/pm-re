#!/usr/bin/env python3
"""Trace the sole call to 0x1C2100 at 0x1C4F11 and its relation to nearby DeviceIoControl path.
Static only; PhoenixMiner is never executed.
"""
from __future__ import annotations
import argparse,bisect
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_IMM,X86_OP_MEM,X86_REG_RIP
TARGET_FN=0x001C44F0
NEAR_START=0x001C3F80
NEAR_END=0x001C5150

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
 imports={}
 for d in getattr(pe,'DIRECTORY_ENTRY_IMPORT',[]):
  dll=d.dll.decode(errors='replace')
  for imp in d.imports:
   if imp.address:
    nm=imp.name.decode(errors='replace') if imp.name else f'ord{imp.ordinal}'
    imports[imp.address-base]=f'{dll}!{nm}'
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True;md.skipdata=True
 fn=fnof(TARGET_FN) or (TARGET_FN,0x001C5118);b,en=fn
 arr=[i for i in md.disasm(pe.get_data(b,en-b),base+b) if i.id!=0]
 lines=['# 0x1C4F11 -> 0x1C2100 transport bridge','',f'caller PDATA `0x{b:08X}..0x{en:08X}`','',
        '## Calls in caller','','| RVA | target |','|---|---|']
 for i in arr:
  if i.mnemonic!='call':continue
  form=i.op_str
  if i.operands:
   op=i.operands[0]
   if op.type==X86_OP_IMM:form=f'RVA 0x{op.imm-base:08X}'
   elif op.type==X86_OP_MEM and op.mem.base==X86_REG_RIP:
    rva=i.address+i.size+op.mem.disp-base;form=imports.get(rva,f'IAT/RIP 0x{rva:08X}')
  lines.append(f'| `0x{i.address-base:08X}` | `{form}` |')
 lines += ['','## Full caller','','```asm']
 for i in arr:lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
 lines += ['```','','## Nearby transport window 0x1C3F80..0x1C5150','','```asm']
 near=[i for i in md.disasm(pe.get_data(NEAR_START,NEAR_END-NEAR_START),base+NEAR_START) if i.id!=0]
 for i in near:
  suffix=''
  if i.mnemonic=='call' and i.operands:
   op=i.operands[0]
   if op.type==X86_OP_IMM:suffix=f' ; -> RVA 0x{op.imm-base:08X}'
   elif op.type==X86_OP_MEM and op.mem.base==X86_REG_RIP:
    rva=i.address+i.size+op.mem.disp-base;suffix=f' ; -> {imports.get(rva,f"IAT/RIP 0x{rva:08X}")}'
  lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}{suffix}'.rstrip())
 lines += ['```']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'transport_bridge_1c4f11.md').write_text('\n'.join(lines),encoding='utf-8')
if __name__=='__main__':main()
