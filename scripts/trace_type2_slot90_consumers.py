#!/usr/bin/env python3
from pathlib import Path
import argparse
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_OP_REG

TEXT_BEGIN=0x1000;TEXT_END=0x420000
SLOT=0x90
TIMING_DISPS={0x98,0xAC,0xB0,0xB8,0xBC,0x368,0x418,0x440,0x4F0}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True;md.skipdata=True
 arr=list(md.disasm(pe.get_data(TEXT_BEGIN,TEXT_END-TEXT_BEGIN),base+TEXT_BEGIN))
 ranges=[]
 try:
  for e in pe.DIRECTORY_ENTRY_EXCEPTION:
   b=e.struct.BeginAddress;en=e.struct.EndAddress
   if b and en and b<en:ranges.append((b,en))
 except Exception:pass
 def fr(rva):
  for b,e in ranges:
   if b<=rva<e:return b,e
  return max(TEXT_BEGIN,rva-0x100),min(TEXT_END,rva+0x300)
 hits=[]
 for idx,i in enumerate(arr):
  if i.mnemonic!='call' or not i.operands:continue
  op=i.operands[0]
  if op.type==X86_OP_MEM and op.mem.disp==SLOT and op.mem.base:hits.append((idx,i))
 lines=['# Type2 slot +0x90 child accessor consumers','', 'Type2 vtable +0x90 is `0x1CF880` -> returns `[this+0x840]` NVIDIA child.','',f'raw slot+0x90 callsites: `{len(hits)}`','']
 for idx,i in hits:
  rva=i.address-base;b,e=fr(rva);loc=[z for z in arr if base+b<=z.address<base+e]
  # score by timing/config displacements and immediate use of returned RAX
  timing=[]
  for z in loc:
   for op in z.operands if z.id else []:
    if op.type==X86_OP_MEM and op.mem.disp in TIMING_DISPS:
     timing.append((z.address-base,op.mem.disp,z.mnemonic,z.op_str));break
  # post-call RAX flow first 20 insns
  post=arr[idx+1:idx+26]; flow=[]
  for z in post:
   text=f'{z.mnemonic} {z.op_str}'
   if any(k in text for k in ('rax','rcx','rdx','r8','r9')):flow.append(z)
  score=(1 if timing else 0)
  # recognize likely child virtual call after RAX return
  childcall=False
  for z in post:
   if z.mnemonic in ('call','jmp') and z.operands:
    op=z.operands[0]
    if op.type==X86_OP_MEM and op.mem.disp in (0x68,0x80):childcall=True;score+=2
  if score==0:continue
  lines += [f'## `0x{rva:08X}` function `0x{b:08X}..0x{e:08X}` score `{score}`','']
  if timing:
   lines += ['Timing/config displacement hits:']
   for rr,d,m,o in timing[:30]:lines.append(f'- `0x{rr:08X}` disp `+0x{d:X}`: `{m} {o}`')
  lines += ['','```asm']
  for z in arr[max(0,idx-24):min(len(arr),idx+32)]:lines.append(f'0x{z.address-base:08X}: {z.mnemonic} {z.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'type2_slot90_consumers.md').write_text('\n'.join(lines),encoding='utf-8')
 print('raw',len(hits),'reported sections',sum(1 for x in lines if x.startswith('## `')))
if __name__=='__main__':main()
