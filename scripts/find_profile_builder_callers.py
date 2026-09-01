#!/usr/bin/env python3
from pathlib import Path
import argparse,struct,bisect
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
TARGET=0x001D7930

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en:funcs.append((b,en))
 funcs=sorted(set(funcs));starts=[b for b,_ in funcs]
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 text=None
 for s in pe.sections:
  if s.Name.rstrip(b'\0')==b'.text': text=(s.VirtualAddress,bytes(s.get_data()));break
 va,data=text; hits=[]
 for off in range(len(data)-5):
  if data[off]!=0xE8:continue
  rel=struct.unpack_from('<i',data,off+1)[0];c=va+off;t=c+5+rel
  if t==TARGET:hits.append(c)
 lines=['# Direct callers of NVIDIA profile builder 0x1D7930','',f'callers: `{len(hits)}`','']
 for c in hits:
  j=bisect.bisect_right(starts,c)-1;fn=funcs[j] if j>=0 and funcs[j][0]<=c<funcs[j][1] else (max(va,c-0x200),c+0x100)
  b=max(fn[0],c-0x180);en=min(fn[1],c+0x100)
  arr=list(md.disasm(pe.get_data(b,en-b),base+b))
  lines += [f'## call `0x{c:08X}` in `0x{fn[0]:08X}..0x{fn[1]:08X}`','','```asm']
  for i in arr:lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'nvidia_profile_builder_callers.md').write_text('\n'.join(lines),encoding='utf-8');print('callers',len(hits))
if __name__=='__main__':main()
