#!/usr/bin/env python3
from pathlib import Path
import argparse,struct,pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
COMMON=0x00090AB0
VT=0x0043F0E8

def rva_to_off(pe,rva):
 for s in pe.sections:
  va=s.VirtualAddress; sz=max(s.Misc_VirtualSize,s.SizeOfRawData)
  if va<=rva<va+sz:return s.PointerToRawData+(rva-va)
 raise ValueError(hex(rva))

def main():
 p=argparse.ArgumentParser();p.add_argument('binary');p.add_argument('--out-dir',default='notes');a=p.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase;data=Path(a.binary).read_bytes()
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 lines=['# VMR common setter and descriptor vtable','']
 # pdata range containing common
 pdata=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.pdata');pd=pdata.get_data();b=e=None
 for o in range(0,len(pd)-12,12):
  x=int.from_bytes(pd[o:o+4],'little');y=int.from_bytes(pd[o+4:o+8],'little')
  if x<=COMMON<y:b,e=x,y;break
 if b is None:b,e=COMMON-0x80,COMMON+0x500
 lines += [f'## Common parser containing function `0x{b:08X}..0x{e:08X}`','','```asm']
 for i in md.disasm(pe.get_data(b,e-b),base+b):lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
 lines += ['```','','## VMR descriptor vtable neighborhood','',f'VMR descriptor vtable base inferred from `0xDD570`: `0x{VT:08X}`','','| slot | address | qword VA | RVA |','|---:|---|---|---|']
 for rel in range(-0x30,0x81,8):
  rva=VT+rel;off=rva_to_off(pe,rva);q=struct.unpack_from('<Q',data,off)[0]
  qrva=q-base if base<=q<base+pe.OPTIONAL_HEADER.SizeOfImage else None
  lines.append(f'| `{rel:+#x}` | `0x{rva:08X}` | `0x{q:016X}` | '+(f'`0x{qrva:08X}`' if qrva is not None else '')+' |')
 # disassemble code targets from first 0x40 bytes of vtable
 seen=set(); lines += ['','## Candidate vtable code targets','']
 for rel in range(0,0x40,8):
  off=rva_to_off(pe,VT+rel);q=struct.unpack_from('<Q',data,off)[0]
  if not(base<=q<base+pe.OPTIONAL_HEADER.SizeOfImage):continue
  r=q-base
  if r in seen:continue
  seen.add(r)
  lines += [f'### slot +0x{rel:X} -> `0x{r:08X}`','','```asm']
  for i in md.disasm(pe.get_data(r,0x100),q):lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'vmr_common_vtable.md').write_text('\n'.join(lines),encoding='utf-8')
if __name__=='__main__':main()
