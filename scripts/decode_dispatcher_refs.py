#!/usr/bin/env python3
"""Decode static refs around dispatcher 0x584A0 and .rdata table entry 0x734A70.
Static only; target binary is never executed.
"""
from __future__ import annotations
import argparse,bisect,struct
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
TARGET=0x000584A0
REFS=[0x00080066,0x000A2F31,0x000A4DCC]
TABLE=0x00734A70

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
 lines=['# Dispatcher 0x584A0 reference contexts','']
 for r in REFS:
  fn=fnof(r);lines += [f'## ref `0x{r:08X}` PDATA `{("0x%08X..0x%08X"%fn) if fn else "none"}`','','```asm']
  if fn:
   arr=list(md.disasm(pe.get_data(fn[0],fn[1]-fn[0]),base+fn[0]))
   k=min(range(len(arr)),key=lambda x:abs((arr[x].address-base)-r))
   for i in arr[max(0,k-45):min(len(arr),k+55)]:lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
  lines += ['```','']
 lines += [f'## .rdata neighborhood `0x{TABLE:08X}`','', '| RVA | u32 | interpreted RVA | u64 | interpreted VA |','|---|---|---|---|---|']
 start=TABLE-0x80;data=pe.get_data(start,0x100)
 for off in range(0,len(data)-7,4):
  r=start+off;u=struct.unpack_from('<I',data,off)[0];q=struct.unpack_from('<Q',data,off)[0]
  ir=f'0x{u:08X}' if 0x1000<=u<pe.OPTIONAL_HEADER.SizeOfImage else ''
  iv=f'0x{q-base:08X}' if base<=q<base+pe.OPTIONAL_HEADER.SizeOfImage else ''
  mark=' **TARGET**' if r==TABLE else ''
  lines.append(f'| `0x{r:08X}`{mark} | `0x{u:08X}` | `{ir}` | `0x{q:016X}` | `{iv}` |')
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'dispatcher_ref_contexts.md';p.write_text('\n'.join(lines),encoding='utf-8');print(p)
if __name__=='__main__':main()
