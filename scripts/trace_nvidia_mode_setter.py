#!/usr/bin/env python3
from pathlib import Path
import argparse,bisect,struct
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64

ANCHOR=0x001DBADC

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en:funcs.append((b,en))
 funcs=sorted(set(funcs));starts=[b for b,_ in funcs]
 j=bisect.bisect_right(starts,ANCHOR)-1;fn=funcs[j];target=fn[0]
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 body=list(md.disasm(pe.get_data(fn[0],fn[1]-fn[0]),base+fn[0]))
 # raw direct callers
 text=None
 for s in pe.sections:
  if s.Name.rstrip(b'\0')==b'.text':text=(s.VirtualAddress,bytes(s.get_data()));break
 va,data=text;callers=[]
 for off in range(len(data)-5):
  if data[off]!=0xE8:continue
  rel=struct.unpack_from('<i',data,off+1)[0];c=va+off;t=c+5+rel
  if t==target:callers.append(c)
 lines=['# NVIDIA child mode setter','','Anchor `0x001DBADC`; containing function is the setter for child `+0x258/+0x25C/+0x260/+0x268`.','',
        f'Function `0x{fn[0]:08X}..0x{fn[1]:08X}`; direct callers: `{len(callers)}`.','',
        '## Full setter','','```asm']
 for i in body:lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
 lines += ['```','']
 for c in callers:
  k=bisect.bisect_right(starts,c)-1;cf=funcs[k] if k>=0 and funcs[k][0]<=c<funcs[k][1] else (max(va,c-0x200),c+0x100)
  b=max(cf[0],c-0x180);en=min(cf[1],c+0x100)
  arr=list(md.disasm(pe.get_data(b,en-b),base+b))
  lines += [f'## caller `0x{c:08X}` in `0x{cf[0]:08X}..0x{cf[1]:08X}`','','```asm']
  for i in arr:lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
  lines += ['```','']
 # qword refs to target VA in data sections can identify vtable slot
 target_va=base+target;needle=struct.pack('<Q',target_va)
 lines += ['## Data qword refs to setter','']
 for s in pe.sections:
  dat=bytes(s.get_data());pos=0
  while True:
   p=dat.find(needle,pos)
   if p<0:break
   lines.append(f'- `{s.Name.rstrip(b"\\0").decode(errors="ignore")}` RVA `0x{s.VirtualAddress+p:08X}`')
   pos=p+1
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'nvidia_mode_setter.md').write_text('\n'.join(lines),encoding='utf-8');print(hex(target),len(callers))
if __name__=='__main__':main()
