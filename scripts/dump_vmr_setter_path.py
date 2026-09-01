#!/usr/bin/env python3
from pathlib import Path
import argparse,pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
RANGES=[
 (0x000DD4D0,0x000DD630,'timing accessors dd510/dd570/dd5f0'),
 (0x000E9D40,0x000E9DE0,'common option tail'),
]
def main():
 p=argparse.ArgumentParser();p.add_argument('binary');p.add_argument('--out-dir',default='notes');a=p.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase;md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 lines=['# VMR setter path — accessors and common parser tail','']
 for b,e,label in RANGES:
  lines += [f'## {label} `0x{b:08X}..0x{e:08X}`','','```asm']
  for i in md.disasm(pe.get_data(b,e-b),base+b):lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
  lines+=['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'vmr_setter_path.md').write_text('\n'.join(lines),encoding='utf-8')
if __name__=='__main__':main()
