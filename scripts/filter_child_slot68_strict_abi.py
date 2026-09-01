#!/usr/bin/env python3
from pathlib import Path
import argparse,bisect
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_OP_REG

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en:funcs.append((b,en))
 funcs=sorted(set(funcs)); starts=[b for b,_ in funcs]
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True;md.skipdata=True
 text=None
 for s in pe.sections:
  if s.Name.rstrip(b'\0')==b'.text':text=(s.VirtualAddress,bytes(s.get_data()));break
 va,data=text;arr=list(md.disasm(data,base+va));hits=[]
 for idx,i in enumerate(arr):
  if i.id==0 or i.mnemonic!='call' or not i.operands:continue
  op=i.operands[0]
  if op.type!=X86_OP_MEM or op.mem.disp!=0x68:continue
  # Walk backward, record nearest definition of each ABI argument register family.
  nearest={}
  for z in reversed(arr[max(0,idx-30):idx]):
   if z.id==0 or not z.operands or z.operands[0].type!=X86_OP_REG:continue
   rn=z.reg_name(z.operands[0].reg)
   fam=None
   if rn in ('edx','rdx','dx','dl'):fam='rdx'
   elif rn in ('r8d','r8','r8w','r8b'):fam='r8'
   elif rn in ('r9d','r9','r9w','r9b'):fam='r9'
   elif rn=='rcx':fam='rcx'
   if fam and fam not in nearest:nearest[fam]=(rn,z)
   if all(k in nearest for k in ('rdx','r8','r9')):break
  if not all(k in nearest for k in ('rdx','r8','r9')):continue
  # Exact setter ABI: 32-bit EDX, 32-bit R8D, 64-bit R9.
  exact=(nearest['rdx'][0]=='edx' and nearest['r8'][0]=='r8d' and nearest['r9'][0]=='r9')
  if exact:hits.append((idx,i,nearest))
 lines=['# Strict NVIDIA child slot +0x68 setter ABI candidates','',
        'Requires nearest defs `EDX` (preset), `R8D` (VMR), `R9` (aux pointer).','',f'hits: `{len(hits)}`','']
 for idx,i,n in hits:
  r=i.address-base;j=bisect.bisect_right(starts,r)-1;fn=funcs[j] if j>=0 and funcs[j][0]<=r<funcs[j][1] else (0,0)
  lines += [f'## `0x{r:08X}` in `0x{fn[0]:08X}..0x{fn[1]:08X}`','']
  for k in ('rdx','r8','r9','rcx'):
   if k in n:
    rn,z=n[k];lines.append(f'- {k}: `{rn}` <- `0x{z.address-base:08X}: {z.mnemonic} {z.op_str}`')
  lines += ['','```asm']
  for z in arr[max(0,idx-40):min(len(arr),idx+18)]:lines.append(f'0x{z.address-base:08X}: {z.mnemonic} {z.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'nvidia_child_slot68_strict_abi.md').write_text('\n'.join(lines),encoding='utf-8');print('hits',len(hits))
if __name__=='__main__':main()
