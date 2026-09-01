#!/usr/bin/env python3
from pathlib import Path
import argparse,bisect
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_IMM,X86_OP_MEM,X86_OP_REG
TARGET=0x001ECCB6

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en:funcs.append((b,en))
 funcs=sorted(set(funcs));starts=[b for b,_ in funcs]
 j=bisect.bisect_right(starts,TARGET)-1;fn=funcs[j]
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 arr=list(md.disasm(pe.get_data(fn[0],fn[1]-fn[0]),base+fn[0]))
 callers=[]
 for cf in funcs:
  ca=list(md.disasm(pe.get_data(cf[0],cf[1]-cf[0]),base+cf[0]))
  for ins in ca:
   if ins.mnemonic=='call' and ins.operands and ins.operands[0].type==X86_OP_IMM and ins.operands[0].imm-base==fn[0]: callers.append((ins.address-base,cf))
 lines=['# RegisterOp-containing function provenance','',f'PDATA `0x{fn[0]:08X}..0x{fn[1]:08X}`','',f'direct callers: `{len(callers)}`','']
 for r,cf in callers:lines.append(f'- `0x{r:08X}` from `0x{cf[0]:08X}..0x{cf[1]:08X}`')
 lines += ['','## Full body','','```asm']
 for i in arr: lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
 lines += ['```','']
 for r,cf in callers:
  ca=list(md.disasm(pe.get_data(cf[0],cf[1]-cf[0]),base+cf[0]));idx=next(k for k,x in enumerate(ca) if x.address-base==r)
  lines += [f'## caller context `0x{r:08X}`','','```asm']
  for x in ca[max(0,idx-50):min(len(ca),idx+40)]:lines.append(f'0x{x.address-base:08X}: {x.mnemonic} {x.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'registerop_function_provenance.md').write_text('\n'.join(lines),encoding='utf-8');print(fn,callers)
if __name__=='__main__':main()
