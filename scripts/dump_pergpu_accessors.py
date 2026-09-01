#!/usr/bin/env python3
from pathlib import Path
import argparse,pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_IMM
TARGETS=[(0x000E07F0,0x000E0876),(0x000E15A0,0x000E1605)]
def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 text=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.text')
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 allins=list(md.disasm(text.get_data(),base+text.VirtualAddress))
 lines=['# Per-GPU stride accessors and callers','']
 for b,e in TARGETS:
  lines += [f'## helper `0x{b:08X}..0x{e:08X}`','','```asm']
  for i in md.disasm(pe.get_data(b,e-b),base+b):lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
  lines += ['```','','### direct callers','']
  callers=[]
  tgt=base+b
  for idx,i in enumerate(allins):
   if i.mnemonic=='call' and i.operands and i.operands[0].type==X86_OP_IMM and i.operands[0].imm==tgt:callers.append(idx)
  lines.append(f'count: {len(callers)}')
  for idx in callers:
   i=allins[idx];lines += [f'#### `0x{i.address-base:08X}`','','```asm']
   for x in allins[max(0,idx-8):min(len(allins),idx+10)]:lines.append(f'0x{x.address-base:08X}: {x.mnemonic} {x.op_str}'.rstrip())
   lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'pergpu_accessors.md').write_text('\n'.join(lines),encoding='utf-8')
if __name__=='__main__':main()
