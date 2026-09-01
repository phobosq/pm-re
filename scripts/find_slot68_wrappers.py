#!/usr/bin/env python3
from pathlib import Path
import argparse,bisect
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM

SLOT=0x68

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en: funcs.append((b,en))
 funcs=sorted(set(funcs));starts=[b for b,_ in funcs]
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True;md.skipdata=True
 text=None
 for s in pe.sections:
  if s.Name.rstrip(b'\0')==b'.text':text=(s.VirtualAddress,bytes(s.get_data()));break
 va,data=text;arr=list(md.disasm(data,base+va));hits=[]
 for idx,i in enumerate(arr):
  if i.id==0 or i.mnemonic not in ('call','jmp') or not i.operands:continue
  op=i.operands[0]
  if op.type==X86_OP_MEM and op.mem.disp==SLOT:
   r=i.address-base;j=bisect.bisect_right(starts,r)-1;fn=funcs[j] if j>=0 and funcs[j][0]<=r<funcs[j][1] else (0,0)
   hits.append((idx,i,fn))
 lines=['# Slot +0x68 wrappers/tailcalls','','Includes indirect CALL and JMP through vtable slot +0x68.','',f'hits: `{len(hits)}`','']
 for idx,i,fn in hits:
  lines += [f'## `{i.mnemonic}` `0x{i.address-base:08X}` in `0x{fn[0]:08X}..0x{fn[1]:08X}`','','```asm']
  for z in arr[max(0,idx-28):min(len(arr),idx+12)]:lines.append(f'0x{z.address-base:08X}: {z.mnemonic} {z.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'slot68_wrappers.md').write_text('\n'.join(lines),encoding='utf-8');print('hits',len(hits))
if __name__=='__main__':main()
