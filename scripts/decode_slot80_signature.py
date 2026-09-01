#!/usr/bin/env python3
from pathlib import Path
import argparse
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_REG,X86_OP_MEM
TARGET=0x001DE8B0

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 arr=list(md.disasm(pe.get_data(TARGET,0x380),base+TARGET))
 # Stop only after reasonable body; slot is large, keep first 0x380 focused on argument capture/setup.
 lines=['# NVIDIA child slot +0x80 entry/signature','', 'Target `0x001DE8B0`; first 0x380 bytes.','', '## Entry disassembly','','```asm']
 for i in arr: lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
 lines += ['```','','## Entry-argument references','','| RVA | arg register | instruction |','|---|---|---|']
 for i in arr:
  txt=i.op_str.lower()
  for reg in ('rcx','rdx','r8','r9'):
   if reg in txt:
    lines.append(f'| `0x{i.address-base:08X}` | `{reg}` | `{i.mnemonic} {i.op_str}` |')
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'nvidia_slot80_signature.md').write_text('\n'.join(lines),encoding='utf-8');print('insns',len(arr))
if __name__=='__main__':main()
