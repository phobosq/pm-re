#!/usr/bin/env python3
from pathlib import Path
import argparse
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64,CS_AC_WRITE
from capstone.x86 import X86_OP_MEM

BEGIN=0x001D4A80;END=0x001F1000
WATCH=0x39C

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True;md.skipdata=True
 arr=list(md.disasm(pe.get_data(BEGIN,END-BEGIN),base+BEGIN));hits=[]
 for idx,i in enumerate(arr):
  for op in i.operands if i.id else []:
   if op.type==X86_OP_MEM and op.mem.disp==WATCH and op.mem.base:
    k='write' if getattr(op,'access',0)&CS_AC_WRITE else 'read';hits.append((idx,i,k,i.reg_name(op.mem.base)));break
 lines=['# NVIDIA child +0x39C family-key provenance','',f'hits: `{len(hits)}`','']
 for idx,i,k,b in hits:
  lines += [f'## {k} `0x{i.address-base:08X}` base `{b}`: `{i.mnemonic} {i.op_str}`','', '```asm']
  for z in arr[max(0,idx-20):min(len(arr),idx+22)]:lines.append(f'0x{z.address-base:08X}: {z.mnemonic} {z.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'nvidia_child_39c_family_key.md').write_text('\n'.join(lines),encoding='utf-8')
 print('hits',[(hex(i.address-base),k,b) for _,i,k,b in hits])
if __name__=='__main__':main()
