#!/usr/bin/env python3
from pathlib import Path
import argparse,bisect
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_OP_IMM

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en:funcs.append((b,en))
 funcs=sorted(set(funcs));starts=[b for b,_ in funcs]
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True;md.skipdata=True
 # scan text once
 text=None
 for s in pe.sections:
  if s.Name.rstrip(b'\0')==b'.text': text=(s.VirtualAddress,bytes(s.get_data()));break
 va,data=text; arr=list(md.disasm(data,base+va)); hits=[]
 for idx,i in enumerate(arr):
  if i.id==0:continue
  for op in i.operands:
   if op.type==X86_OP_MEM and op.mem.disp==0x840:
    hits.append((idx,i));break
 lines=['# Global users of displacement +0x840','','Candidate Type2 real NVIDIA child pointer field.','',f'hits: `{len(hits)}`','']
 seen=set()
 for idx,i in hits:
  r=i.address-base;j=bisect.bisect_right(starts,r)-1
  fn=funcs[j] if j>=0 and funcs[j][0]<=r<funcs[j][1] else (0,0)
  key=(fn,r)
  if key in seen:continue
  seen.add(key)
  lines += [f'## `0x{r:08X}` in PDATA `0x{fn[0]:08X}..0x{fn[1]:08X}`','','```asm']
  for z in arr[max(0,idx-16):min(len(arr),idx+24)]:lines.append(f'0x{z.address-base:08X}: {z.mnemonic} {z.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'type2_child_global_users.md').write_text('\n'.join(lines),encoding='utf-8');print('hits',len(hits))
if __name__=='__main__':main()
