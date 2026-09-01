#!/usr/bin/env python3
from pathlib import Path
import argparse
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64

BEGIN=0x001305F0;END=0x001309D9

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True;md.skipdata=True
 arr=list(md.disasm(pe.get_data(BEGIN,END-BEGIN),base+BEGIN))
 lines=['# Type2 config -> NVIDIA child bridge 0x1305F0','','Full Capstone decode. Entry obtains child through parent slot +0x90 and builds a local config snapshot via 0x06A320.','','```asm']
 for i in arr: lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
 lines += ['```']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'type2_config_bridge_1305f0.md').write_text('\n'.join(lines),encoding='utf-8')
 print('instructions',len(arr))
if __name__=='__main__':main()
