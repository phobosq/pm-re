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
 funcs=sorted(set(funcs));starts=[b for b,_ in funcs]
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True;md.skipdata=True
 text=None
 for s in pe.sections:
  if s.Name.rstrip(b'\0')==b'.text':text=(s.VirtualAddress,bytes(s.get_data()));break
 va,data=text;arr=list(md.disasm(data,base+va));hits=[]
 want={'edx':False,'rdx':False,'r8d':False,'r8':False,'r9':False,'r9d':False}
 for idx,i in enumerate(arr):
  if i.id==0 or i.mnemonic!='call' or not i.operands:continue
  op=i.operands[0]
  if op.type!=X86_OP_MEM or op.mem.disp!=0x68:continue
  seen=set(); defs=[]
  for z in arr[max(0,idx-24):idx]:
   if z.id==0:continue
   # collect explicit destination register writes via first operand
   if len(z.operands)>=1 and z.operands[0].type==X86_OP_REG:
    rn=z.reg_name(z.operands[0].reg)
    if rn in want:
     seen.add(rn);defs.append((rn,z))
   # LEA/MOV to rcx object context useful, but not score
  score=int(bool({'edx','rdx'}&seen))+int(bool({'r8d','r8'}&seen))+int(bool({'r9','r9d'}&seen))
  if score>=2:hits.append((idx,i,score,defs))
 lines=['# Child slot +0x68 callsites filtered by mode-setter ABI','',
        'Confirmed setter ABI: `RCX=child`, `EDX=preset`, `R8D=VMR`, `R9=&aux`.','',f'candidates score>=2: `{len(hits)}`','']
 for idx,i,score,defs in sorted(hits,key=lambda x:-x[2]):
  r=i.address-base;j=bisect.bisect_right(starts,r)-1;fn=funcs[j] if j>=0 and funcs[j][0]<=r<funcs[j][1] else (0,0)
  lines += [f'## `0x{r:08X}` score `{score}/3` in `0x{fn[0]:08X}..0x{fn[1]:08X}`','', 'Recent ABI defs:','']
  for rn,z in defs:lines.append(f'- `{rn}` <- `0x{z.address-base:08X}: {z.mnemonic} {z.op_str}`')
  lines += ['','```asm']
  for z in arr[max(0,idx-28):min(len(arr),idx+14)]:lines.append(f'0x{z.address-base:08X}: {z.mnemonic} {z.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'nvidia_child_slot68_abi_candidates.md').write_text('\n'.join(lines),encoding='utf-8');print('candidates',len(hits))
if __name__=='__main__':main()
