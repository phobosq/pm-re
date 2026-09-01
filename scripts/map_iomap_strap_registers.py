#!/usr/bin/env python3
"""Recover argument constants and struct destinations/sources for IOMap strap read/write loops.
Targets:
  0x1C5120 -> repeated read primitive 0x1C1E40(ECX,DX) -> EAX
  0x1C6CA0 -> repeated write primitive 0x1C1ED0(ECX,EDX,R8W)
Static only; PhoenixMiner is never executed.
"""
from __future__ import annotations
import argparse,bisect
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_IMM,X86_OP_REG,X86_OP_MEM
READ_FN=0x001C5120;READ_PRIM=0x001C1E40
WRITE_FN=0x001C6CA0;WRITE_PRIM=0x001C1ED0

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
  return funcs[j] if j>=0 and funcs[j][0]<=r<funcs[j][1] else (r,r+0x800)
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True;md.skipdata=True
 def insns(t):
  b,en=fnof(t);return b,en,[i for i in md.disasm(pe.get_data(b,en-b),base+b) if i.id!=0]
 lines=['# IOMap strap register map','',
        'Primitives: `0x1C1E40(ECX,DX)->EAX` read; `0x1C1ED0(ECX,EDX,R8W)->bool` write.','']
 for t,prim,title in [(READ_FN,READ_PRIM,'Read/current-state builder'),(WRITE_FN,WRITE_PRIM,'Write/apply path')]:
  b,en,arr=insns(t)
  lines += [f'## {title} `0x{b:08X}..0x{en:08X}`','',
            '| call | arg setup window | post-call/store |','|---|---|---|']
  for idx,i in enumerate(arr):
   if i.mnemonic!='call' or not i.operands or i.operands[0].type!=X86_OP_IMM or i.operands[0].imm-base!=prim:continue
   pre=arr[max(0,idx-8):idx];post=arr[idx+1:min(len(arr),idx+5)]
   p='; '.join(f'{x.mnemonic} {x.op_str}' for x in pre)
   q='; '.join(f'{x.mnemonic} {x.op_str}' for x in post)
   lines.append(f'| `0x{i.address-base:08X}` | `{p}` | `{q}` |')
  lines += ['','### Full body','','```asm']
  for i in arr:lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'iomap_strap_register_map.md').write_text('\n'.join(lines),encoding='utf-8')
if __name__=='__main__':main()
