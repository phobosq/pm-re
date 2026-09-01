#!/usr/bin/env python3
from pathlib import Path
import argparse,bisect
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_OP_IMM
TARGETS=[0x001D97E0,0x001D7930]

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en:funcs.append((b,en))
 funcs=sorted(set(funcs));starts=[b for b,_ in funcs]
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 lines=['# NVIDIA strap preprocessors 0x1D97E0 / 0x1D7930','',
        'Called by child vtable slot +0x80 immediately before RegisterOp-backed apply.','']
 for target in TARGETS:
  j=bisect.bisect_right(starts,target)-1;fn=funcs[j];arr=list(md.disasm(pe.get_data(fn[0],fn[1]-fn[0]),base+fn[0]))
  lines += [f'## target `0x{target:08X}` PDATA `0x{fn[0]:08X}..0x{fn[1]:08X}`','', '### Calls','','| RVA | target/form |','|---|---|']
  for i in arr:
   if i.mnemonic=='call':
    op=i.operands[0];dst=f'RVA 0x{op.imm-base:08X}' if op.type==X86_OP_IMM else i.op_str
    lines.append(f'| `0x{i.address-base:08X}` | `{dst}` |')
  lines += ['','### Object/struct accesses','','| RVA | base | disp | instruction |','|---|---|---:|---|']
  for i in arr:
   for op in i.operands:
    if op.type==X86_OP_MEM and op.mem.base:
     bn=i.reg_name(op.mem.base);d=op.mem.disp
     if bn not in ('rsp','rbp','rip') and 0 <= d <= 0x900:
      lines.append(f'| `0x{i.address-base:08X}` | `{bn}` | `0x{d:X}` | `{i.mnemonic} {i.op_str}` |')
  lines += ['','### Full body','','```asm']
  for i in arr: lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'nvidia_strap_preprocessors.md').write_text('\n'.join(lines),encoding='utf-8');print('done')
if __name__=='__main__':main()
