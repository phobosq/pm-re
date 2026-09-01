#!/usr/bin/env python3
from pathlib import Path
import argparse
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM
BEGIN=0x001D4A80;END=0x001F1000

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True;md.skipdata=True
 arr=list(md.disasm(pe.get_data(BEGIN,END-BEGIN),base+BEGIN));hits=[]
 for idx,i in enumerate(arr):
  if i.id==0:continue
  for op in i.operands:
   if op.type==X86_OP_MEM and op.mem.disp==0xD0 and op.mem.base:
    bn=i.reg_name(op.mem.base)
    if bn in ('rsp','rbp','rip'):continue
    hits.append((idx,i,bn));break
 lines=['# NVIDIA child +0xD0 RegisterOp-handle provenance','',
        'RegisterOp callsites use `[child+0xD0]` as RCX. This report lists all non-stack +0xD0 refs in the NVIDIA child region.','',f'hits: `{len(hits)}`','']
 for idx,i,bn in hits:
  lines += [f'## `0x{i.address-base:08X}` base `{bn}`: `{i.mnemonic} {i.op_str}`','','```asm']
  for z in arr[max(0,idx-18):min(len(arr),idx+20)]:lines.append(f'0x{z.address-base:08X}: {z.mnemonic} {z.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'registerop_handle_provenance.md').write_text('\n'.join(lines),encoding='utf-8');print('hits',len(hits))
if __name__=='__main__':main()
