#!/usr/bin/env python3
from pathlib import Path
import argparse
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_OP_REG

# Search for local dataflow pattern:
#   call [parent_vptr+0x90] -> RAX child
#   save/move RAX
#   load child vptr from [child]
#   call [child_vptr+0x80]
# within a modest instruction window.

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True;md.skipdata=True
 text=None
 for s in pe.sections:
  if s.Name.rstrip(b'\0')==b'.text': text=(s.VirtualAddress,bytes(s.get_data()));break
 va,data=text; arr=list(md.disasm(data,base+va))
 hits=[]
 for idx,i in enumerate(arr):
  if i.id==0 or i.mnemonic!='call' or not i.operands: continue
  op=i.operands[0]
  if op.type!=X86_OP_MEM or op.mem.disp!=0x90: continue
  aliases={'rax'}; vptr=set(); found=[]
  for j in range(idx+1,min(len(arr),idx+60)):
   z=arr[j]
   if z.id==0: continue
   if z.mnemonic=='mov' and len(z.operands)==2 and z.operands[0].type==X86_OP_REG:
    dst=z.reg_name(z.operands[0].reg);src=z.operands[1]
    if src.type==X86_OP_REG and z.reg_name(src.reg) in aliases: aliases.add(dst)
    elif src.type==X86_OP_MEM and src.mem.base and z.reg_name(src.mem.base) in aliases and src.mem.disp==0: vptr.add(dst)
    elif src.type==X86_OP_REG and z.reg_name(src.reg) in vptr: vptr.add(dst)
   if z.mnemonic=='call' and z.operands:
    q=z.operands[0]
    if q.type==X86_OP_MEM and q.mem.base and z.reg_name(q.mem.base) in vptr and q.mem.disp==0x80:
     found.append(j);break
   if z.mnemonic=='ret': break
  if found:hits.append((idx,found[0]))
 lines=['# Parent slot +0x90 -> child slot +0x80 bridges','',f'hits: `{len(hits)}`','']
 for aidx,bidx in hits:
  ains=arr[aidx];bins=arr[bidx]
  lines += [f'## parent call `0x{ains.address-base:08X}` -> child +0x80 `0x{bins.address-base:08X}`','','```asm']
  for z in arr[max(0,aidx-16):min(len(arr),bidx+18)]: lines.append(f'0x{z.address-base:08X}: {z.mnemonic} {z.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'parent90_child80_bridge.md').write_text('\n'.join(lines),encoding='utf-8');print('hits',len(hits))
if __name__=='__main__':main()
