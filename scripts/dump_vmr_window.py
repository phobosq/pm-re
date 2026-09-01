#!/usr/bin/env python3
from pathlib import Path
import argparse, pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64

BEGIN=0x000E8EA0
END=0x000E91A0

def main():
 p=argparse.ArgumentParser();p.add_argument('binary');p.add_argument('--out-dir',default='notes');a=p.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 ins=list(md.disasm(pe.get_data(BEGIN,END-BEGIN),base+BEGIN))
 lines=['# Narrow -vmr parser window','',f'`0x{BEGIN:08X}..0x{END:08X}`','','```asm']
 for i in ins: lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
 lines+=['```']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'vmr_window.md').write_text('\n'.join(lines),encoding='utf-8')
 print(out/'vmr_window.md')
if __name__=='__main__':main()
