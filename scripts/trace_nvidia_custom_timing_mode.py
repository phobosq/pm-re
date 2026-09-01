#!/usr/bin/env python3
from pathlib import Path
import argparse
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64,CS_AC_WRITE
from capstone.x86 import X86_OP_MEM
BEGIN=0x001D4A80;END=0x001F1000
WIN_B=0x001D8AE0;WIN_E=0x001D8F40
WATCH={0x258:'mode_258',0x25C:'mode_25c'}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True;md.skipdata=True
 arr=list(md.disasm(pe.get_data(BEGIN,END-BEGIN),base+BEGIN));hits=[]
 for idx,i in enumerate(arr):
  if i.id==0:continue
  for op in i.operands:
   if op.type==X86_OP_MEM and op.mem.disp in WATCH and op.mem.base:
    kind='write' if (getattr(op,'access',0)&CS_AC_WRITE) else 'read'
    hits.append((idx,i,op.mem.disp,kind,i.reg_name(op.mem.base)));break
 lines=['# NVIDIA custom timing mode trace','','Candidate child fields `+0x258/+0x25C` gate strap/custom-profile application.','',
        '| RVA | kind | field | base | instruction |','|---|---|---|---|---|']
 for idx,i,d,k,bn in hits:lines.append(f'| `0x{i.address-base:08X}` | {k} | `{WATCH[d]}` | `{bn}` | `{i.mnemonic} {i.op_str}` |')
 lines += ['','## Access contexts','']
 for idx,i,d,k,bn in hits:
  lines += [f'### {k} {WATCH[d]} at `0x{i.address-base:08X}`','','```asm']
  for z in arr[max(0,idx-12):min(len(arr),idx+14)]:lines.append(f'0x{z.address-base:08X}: {z.mnemonic} {z.op_str}'.rstrip())
  lines += ['```','']
 lines += ['','## Profile-builder custom branch 0x1D8AE0..0x1D8F40','','```asm']
 win=list(md.disasm(pe.get_data(WIN_B,WIN_E-WIN_B),base+WIN_B))
 for i in win:lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
 lines += ['```']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'nvidia_custom_timing_mode.md').write_text('\n'.join(lines),encoding='utf-8');print('hits',len(hits))
if __name__=='__main__':main()
