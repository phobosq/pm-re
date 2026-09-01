#!/usr/bin/env python3
from pathlib import Path
import argparse,struct,bisect
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64

TARGET=0x0016E0B0

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en:funcs.append((b,en))
 funcs=sorted(set(funcs)); starts=[b for b,_ in funcs]
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 text=None
 for s in pe.sections:
  if s.Name.rstrip(b'\0')==b'.text':text=(s.VirtualAddress,bytes(s.get_data()));break
 va,data=text; callers=[]
 for off in range(len(data)-5):
  if data[off]!=0xE8:continue
  rel=struct.unpack_from('<i',data,off+1)[0]; c=va+off; t=c+5+rel
  if t==TARGET:callers.append(c)
 target_va=base+TARGET;needle=struct.pack('<Q',target_va);refs=[]
 for s in pe.sections:
  dat=bytes(s.get_data());pos=0
  while True:
   p=dat.find(needle,pos)
   if p<0:break
   refs.append((s.Name.rstrip(b'\0').decode(errors='ignore'),s.VirtualAddress+p));pos=p+1
 lines=['# NVIDIA child mode-setter tail wrapper 0x16E0B0','',
        '`0x16E0B0` replaces RCX with `[wrapper+0x80]` and tail-jumps to child vtable slot +0x68, preserving RDX/R8/R9.','',
        f'direct callers: `{len(callers)}`','', '## Data refs','']
 for n,r in refs:lines.append(f'- `{n}` RVA `0x{r:08X}`')
 for c in callers:
  j=bisect.bisect_right(starts,c)-1;fn=funcs[j] if j>=0 and funcs[j][0]<=c<funcs[j][1] else (max(va,c-0x300),c+0x100)
  b=max(fn[0],c-0x240);en=min(fn[1],c+0x120)
  arr=list(md.disasm(pe.get_data(b,en-b),base+b))
  lines += ['',f'## caller `0x{c:08X}` in `0x{fn[0]:08X}..0x{fn[1]:08X}`','','```asm']
  for i in arr:lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
  lines += ['```']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'nvidia_slot68_tail_wrapper.md').write_text('\n'.join(lines),encoding='utf-8');print('callers',len(callers),'refs',refs)
if __name__=='__main__':main()
