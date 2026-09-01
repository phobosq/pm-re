#!/usr/bin/env python3
from pathlib import Path
import argparse
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en:funcs.append((b,en))
 funcs=sorted(set(funcs));hits=[]
 for fn in funcs:
  arr=list(md.disasm(pe.get_data(fn[0],fn[1]-fn[0]),base+fn[0]))
  for k,i in enumerate(arr):
   if i.mnemonic!='call' or not i.operands:continue
   op=i.operands[0]
   if op.type==X86_OP_MEM and op.mem.disp==0x80:
    hits.append((fn,k,arr,i))
 lines=['# Indirect vtable slot +0x80 callsites','',f'total: `{len(hits)}`','']
 for n,(fn,k,arr,i) in enumerate(hits,1):
  lines += [f'## {n}. `0x{i.address-base:08X}` in `0x{fn[0]:08X}..0x{fn[1]:08X}`','','```asm']
  for w in arr[max(0,k-45):min(len(arr),k+35)]:lines.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'nvidia_child_slot80_calls.md').write_text('\n'.join(lines),encoding='utf-8');print('hits',len(hits))
if __name__=='__main__':main()
