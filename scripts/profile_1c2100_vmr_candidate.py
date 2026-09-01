#!/usr/bin/env python3
"""Profile RVA 0x1C2100 as NVIDIA-adjacent VMR-record candidate.
Static only; PhoenixMiner is never executed.
"""
from __future__ import annotations
import argparse,bisect,struct
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_IMM,X86_OP_MEM,X86_REG_RIP
TARGET=0x001C2100

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
 fn=fnof(TARGET) or (TARGET,TARGET+0x2000);b,en=fn
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True;md.skipdata=True
 arr=[i for i in md.disasm(pe.get_data(b,en-b),base+b) if i.id!=0]
 imports={}
 for d in getattr(pe,'DIRECTORY_ENTRY_IMPORT',[]):
  dll=d.dll.decode(errors='replace')
  for imp in d.imports:
   if imp.address:
    nm=imp.name.decode(errors='replace') if imp.name else f'ord{imp.ordinal}'
    imports[imp.address-base]=f'{dll}!{nm}'
 text=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.text');raw=text.get_data();trva=text.VirtualAddress
 callers=[]
 for off in range(len(raw)-5):
  if raw[off]!=0xE8:continue
  rel=struct.unpack_from('<i',raw,off+1)[0];c=trva+off
  if c+5+rel==TARGET:callers.append((c,fnof(c)))
 lines=['# VMR candidate 0x001C2100','',f'PDATA `0x{b:08X}..0x{en:08X}`','',f'direct callers: `{len(callers)}`','']
 for c,f in callers:lines.append(f'- `0x{c:08X}` from `{("0x%08X..0x%08X"%f) if f else "no PDATA"}`')
 lines += ['','## Calls','','| RVA | target |','|---|---|']
 for i in arr:
  if i.mnemonic!='call':continue
  form=i.op_str
  if i.operands:
   op=i.operands[0]
   if op.type==X86_OP_IMM:form=f'RVA 0x{op.imm-base:08X}'
   elif op.type==X86_OP_MEM and op.mem.base==X86_REG_RIP:
    rva=i.address+i.size+op.mem.disp-base;form=imports.get(rva,f'IAT/RIP 0x{rva:08X}')
  lines.append(f'| `0x{i.address-base:08X}` | `{form}` |')
 lines += ['','## RDX-derived / +0xB0-shaped accesses','','| RVA | instruction |','|---|---|']
 # simple rdx alias propagation for report readability
 aliases={'rdx':0}
 for i in arr:
  for op in i.operands:
   if op.type==X86_OP_MEM and i.reg_name(op.mem.base) in aliases:
    off=aliases[i.reg_name(op.mem.base)]+op.mem.disp
    if 0x90<=off<=0xC8:lines.append(f'| `0x{i.address-base:08X}` | `{i.mnemonic} {i.op_str}` |')
  if i.mnemonic=='mov' and len(i.operands)==2 and i.operands[0].type==1 and i.operands[1].type==1:
   d=i.reg_name(i.operands[0].reg);s=i.reg_name(i.operands[1].reg)
   if s in aliases:aliases[d]=aliases[s]
  elif i.mnemonic=='lea' and len(i.operands)==2 and i.operands[0].type==1 and i.operands[1].type==3:
   d=i.reg_name(i.operands[0].reg);m=i.operands[1].mem;s=i.reg_name(m.base)
   if s in aliases and m.index==0:aliases[d]=aliases[s]+m.disp
 lines += ['','## Full body','','```asm']
 for i in arr:lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
 lines += ['```']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'vmr_candidate_1c2100.md').write_text('\n'.join(lines),encoding='utf-8')
if __name__=='__main__':main()
