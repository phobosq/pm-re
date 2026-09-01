#!/usr/bin/env python3
from pathlib import Path
import argparse,bisect
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_OP_REG,X86_OP_IMM
TARGET=0x001DE8B0

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en: funcs.append((b,en))
 funcs=sorted(set(funcs));starts=[x[0] for x in funcs]
 j=bisect.bisect_right(starts,TARGET)-1;fn=funcs[j]
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 arr=list(md.disasm(pe.get_data(fn[0],fn[1]-fn[0]),base+fn[0]))
 lines=['# NVIDIA child slot +0x80 RegisterOp input provenance','',f'PDATA `0x{fn[0]:08X}..0x{fn[1]:08X}`','',
        'Known downstream: calls `0x001ECB90(this, current*, desired*, gpu_index)` at 0x1DF246 and 0x1DF43E.','']
 lines += ['## Calls','','| RVA | target/form |','|---|---|']
 for i in arr:
  if i.mnemonic=='call':
   op=i.operands[0]
   tgt=f'RVA 0x{op.imm-base:08X}' if op.type==X86_OP_IMM else i.op_str
   lines.append(f'| `0x{i.address-base:08X}` | `{tgt}` |')
 lines += ['','## Local candidate-struct accesses','','Tracks RBP-relative offsets near current/desired structures (`0..0x180`).','',
           '| RVA | disp | instruction |','|---|---:|---|']
 for i in arr:
  for op in i.operands:
   if op.type==X86_OP_MEM and op.mem.base and i.reg_name(op.mem.base)=='rbp' and 0 <= op.mem.disp <= 0x180:
    lines.append(f'| `0x{i.address-base:08X}` | `0x{op.mem.disp:X}` | `{i.mnemonic} {i.op_str}` |')
 lines += ['','## this-like accesses','','Candidate `this` registers are inferred from prolog and callsite use; list non-stack mem displacements >=0x200.','',
           '| RVA | base | disp | instruction |','|---|---|---:|---|']
 for i in arr:
  for op in i.operands:
   if op.type==X86_OP_MEM and op.mem.base:
    bn=i.reg_name(op.mem.base)
    if bn not in ('rsp','rbp','rip') and 0x200 <= op.mem.disp <= 0x900:
     lines.append(f'| `0x{i.address-base:08X}` | `{bn}` | `0x{op.mem.disp:X}` | `{i.mnemonic} {i.op_str}` |')
 for callrva in (0x001DF246,0x001DF43E):
  idx=next(k for k,x in enumerate(arr) if x.address-base==callrva)
  lines += ['',f'## RegisterOp helper call context `0x{callrva:08X}`','','```asm']
  for x in arr[max(0,idx-120):min(len(arr),idx+40)]:lines.append(f'0x{x.address-base:08X}: {x.mnemonic} {x.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'registerop_slot80_inputs.md').write_text('\n'.join(lines),encoding='utf-8');print('insns',len(arr))
if __name__=='__main__':main()
