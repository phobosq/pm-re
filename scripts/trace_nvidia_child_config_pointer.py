#!/usr/bin/env python3
from pathlib import Path
import argparse,bisect
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_REG,X86_OP_MEM
TARGET=0x001D4A80

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en:funcs.append((b,en))
 funcs.sort();starts=[b for b,_ in funcs];j=bisect.bisect_right(starts,TARGET)-1;fn=funcs[j]
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 arr=list(md.disasm(pe.get_data(fn[0],fn[1]-fn[0]),base+fn[0]))
 lines=['# NVIDIA child ctor: config pointer retention','',f'PDATA `0x{fn[0]:08X}..0x{fn[1]:08X}`','',
        'Entry R9 is copied to RSI. This report lists every instruction that explicitly uses RSI as an operand and every store of RSI into memory.','',
        '| RVA | kind | instruction |','|---|---|---|']
 for i in arr:
  uses=False;kind=[]
  for n,op in enumerate(i.operands):
   if op.type==X86_OP_REG and i.reg_name(op.reg)=='rsi':
    uses=True;kind.append('RSI-reg')
    if n==1 and i.mnemonic in ('mov','lea'):kind.append('possible-source')
   if op.type==X86_OP_MEM and op.mem.base and i.reg_name(op.mem.base)=='rsi':
    uses=True;kind.append('dereference')
  if i.mnemonic=='mov' and len(i.operands)==2 and i.operands[0].type==X86_OP_MEM and i.operands[1].type==X86_OP_REG and i.reg_name(i.operands[1].reg)=='rsi':
   kind.append('STORE_CONFIG_PTR')
  if uses:lines.append(f'| `0x{i.address-base:08X}` | {" / ".join(kind)} | `{i.mnemonic} {i.op_str}` |')
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'nvidia_child_config_pointer.md').write_text('\n'.join(lines),encoding='utf-8');print('done')
if __name__=='__main__':main()
