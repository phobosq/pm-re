#!/usr/bin/env python3
from pathlib import Path
import argparse
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_OP_REG
BEGIN=0x001D7930;END=0x001D9455

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 arr=list(md.disasm(pe.get_data(BEGIN,END-BEGIN),base+BEGIN))
 lines=['# VMR profile +0x08 copyout confirmation','',
        '`0x1D7930`: R13 = caller output profile pointer. Local working profile is rooted at RSP+0x70; VMR interpolation writes RSP+0x78.','',
        '## References to R13 output pointer','','| RVA | access | instruction |','|---|---|---|']
 for idx,i in enumerate(arr):
  if i.id==0:continue
  for op in i.operands:
   if op.type==X86_OP_MEM and op.mem.base and i.reg_name(op.mem.base)=='r13':
    access='write' if getattr(op,'access',0)&2 else 'read'
    lines.append(f'| `0x{i.address-base:08X}` | {access} | `{i.mnemonic} {i.op_str}` |')
    lines += ['','```asm']
    for z in arr[max(0,idx-12):min(len(arr),idx+14)]:lines.append(f'0x{z.address-base:08X}: {z.mnemonic} {z.op_str}'.rstrip())
    lines += ['```','']
    break
 lines += ['','## References to local VMR slot RSP+0x78','','| RVA | access | instruction |','|---|---|---|']
 for idx,i in enumerate(arr):
  if i.id==0:continue
  for op in i.operands:
   if op.type==X86_OP_MEM and op.mem.base and i.reg_name(op.mem.base)=='rsp' and op.mem.disp==0x78:
    access='write' if getattr(op,'access',0)&2 else 'read'
    lines.append(f'| `0x{i.address-base:08X}` | {access} | `{i.mnemonic} {i.op_str}` |')
    lines += ['','```asm']
    for z in arr[max(0,idx-12):min(len(arr),idx+14)]:lines.append(f'0x{z.address-base:08X}: {z.mnemonic} {z.op_str}'.rstrip())
    lines += ['```','']
    break
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'vmr_profile_copyout.md').write_text('\n'.join(lines),encoding='utf-8');print('done')
if __name__=='__main__':main()
