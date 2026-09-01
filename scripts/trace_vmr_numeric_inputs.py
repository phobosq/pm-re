#!/usr/bin/env python3
from pathlib import Path
import argparse
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64,CS_AC_WRITE
from capstone.x86 import X86_OP_MEM,X86_OP_REG,X86_REG_RBP,X86_REG_RSP

BEGIN=0x001D7930; END=0x001D9450
ANCHOR=0x001D8B1F
WATCH={(X86_REG_RBP,0x28):'vmr_base_rbp28',(X86_REG_RBP,0xA8):'vmr_target_rbpA8',(X86_REG_RSP,0x40):'vmr_alt_rsp40'}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True;md.skipdata=True
 arr=list(md.disasm(pe.get_data(BEGIN,END-BEGIN),base+BEGIN))
 hits=[]
 for idx,i in enumerate(arr):
  for op in i.operands if i.id else []:
   if op.type==X86_OP_MEM and (op.mem.base,op.mem.disp) in WATCH:
    kind='write' if (getattr(op,'access',0)&CS_AC_WRITE) else 'read'
    hits.append((idx,i,WATCH[(op.mem.base,op.mem.disp)],kind));break
 lines=['# VMR numeric input provenance','','Interpolation anchor: `0x1D8B1F`; formula consumes ESI, ECX, child+0x25C and XMM6.','', '## Watched local accesses','']
 for idx,i,n,k in hits: lines.append(f'- `0x{i.address-base:08X}` {k} `{n}`: `{i.mnemonic} {i.op_str}`')
 for idx,i,n,k in hits:
  if k!='write':continue
  lines += ['',f'## writer `{n}` at `0x{i.address-base:08X}`','', '```asm']
  for z in arr[max(0,idx-24):min(len(arr),idx+18)]:lines.append(f'0x{z.address-base:08X}: {z.mnemonic} {z.op_str}'.rstrip())
  lines += ['```']
 # XMM6 last defs before anchor
 ai=next((k for k,z in enumerate(arr) if z.address-base==ANCHOR),None)
 lines += ['','## XMM6 definitions before interpolation','']
 if ai is not None:
  defs=[]
  for idx in range(ai-1,-1,-1):
   z=arr[idx]
   if not z.operands:continue
   op=z.operands[0]
   if op.type==X86_OP_REG and z.reg_name(op.reg) in ('xmm6','ymm6'):
    defs.append(idx)
    if len(defs)>=8:break
  for idx in defs:
   z=arr[idx];lines += ['',f'### `0x{z.address-base:08X}: {z.mnemonic} {z.op_str}`','', '```asm']
   for q in arr[max(0,idx-10):min(len(arr),idx+8)]:lines.append(f'0x{q.address-base:08X}: {q.mnemonic} {q.op_str}'.rstrip())
   lines += ['```']
 # full aligned lead-in from 0x1D89C0 to 0x1D8B60 using already aligned stream
 lines += ['','## Aligned lead-in 0x1D89C0..0x1D8B60','','```asm']
 for z in arr:
  r=z.address-base
  if 0x001D89C0<=r<0x001D8B60:lines.append(f'0x{r:08X}: {z.mnemonic} {z.op_str}'.rstrip())
 lines += ['```']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'vmr_numeric_inputs.md').write_text('\n'.join(lines),encoding='utf-8')
 print('hits',[(hex(i.address-base),n,k) for _,i,n,k in hits])
if __name__=='__main__':main()
