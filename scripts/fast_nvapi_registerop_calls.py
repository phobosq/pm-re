#!/usr/bin/env python3
from pathlib import Path
import argparse,struct
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64

SLOT=0x007E7B08

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 sec=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.text');data=sec.get_data();srva=sec.VirtualAddress
 hits=[]
 for off in range(len(data)-6):
  if data[off]!=0xFF or data[off+1]!=0x15: continue
  disp=struct.unpack_from('<i',data,off+2)[0]
  rva=srva+off
  target=rva+6+disp
  if target==SLOT: hits.append(rva)
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 lines=['# Fast direct call scan for NvAPI_GPU_RegisterOp','',f'slot: `0x{SLOT:08X}`',f'direct `FF 15` calls: `{len(hits)}`','']
 for rva in hits:
  begin=max(srva,rva-0x80);end=min(srva+len(data),rva+0x100)
  lines += [f'## call `0x{rva:08X}`','','```asm']
  for i in md.disasm(pe.get_data(begin,end-begin),base+begin): lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'nvapi_registerop_fast.md';p.write_text('\n'.join(lines),encoding='utf-8');print('hits',hits)
if __name__=='__main__':main()
