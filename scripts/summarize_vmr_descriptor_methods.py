#!/usr/bin/env python3
"""Compact summary of VMR descriptor vtable methods and field accesses."""
from pathlib import Path
import argparse,struct,pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM
VT=0x0043F0E8

def off(pe,rva):
 for s in pe.sections:
  if s.VirtualAddress<=rva<s.VirtualAddress+max(s.Misc_VirtualSize,s.SizeOfRawData):
   return s.PointerToRawData+rva-s.VirtualAddress
 raise ValueError(hex(rva))

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 p=Path(a.binary);data=p.read_bytes();pe=pefile.PE(str(p),fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 lines=['# VMR descriptor method summary','',f'vtable: `0x{VT:08X}`','']
 for slot in range(0,0x40,8):
  q=struct.unpack_from('<Q',data,off(pe,VT+slot))[0]
  if not(base<=q<base+pe.OPTIONAL_HEADER.SizeOfImage):continue
  rva=q-base; ins=list(md.disasm(pe.get_data(rva,0x180),q))
  lines += [f'## slot `+0x{slot:X}` -> `0x{rva:08X}`','','```asm']
  # stop at first ret, cap 80 instructions
  selected=[]
  for i in ins[:80]:
   selected.append(i)
   if i.mnemonic=='ret':break
  for i in selected:lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
  lines += ['```','','Field-like memory displacements:']
  seen=[]
  for i in selected:
   for op in i.operands:
    if op.type==X86_OP_MEM and op.mem.disp and op.mem.disp not in seen:seen.append(op.mem.disp)
  lines.append(', '.join(f'`{x:+#x}`' for x in seen) if seen else 'none')
  lines.append('')
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'vmr_descriptor_methods.md').write_text('\n'.join(lines),encoding='utf-8')
if __name__=='__main__':main()
