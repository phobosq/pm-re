#!/usr/bin/env python3
"""Trace provenance of the object passed as RCX to 0x1362D0 at callsite 0x6FCC2.
Static only; target binary is never executed.
"""
from __future__ import annotations
import argparse,bisect
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_IMM
FUNC_RVA=0x0006F940
CALL_RVA=0x0006FCC2
TARGET=0x001362D0

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en:funcs.append((b,en))
 funcs.sort();starts=[b for b,_ in funcs]
 j=bisect.bisect_right(starts,FUNC_RVA)-1
 fn=funcs[j] if j>=0 and funcs[j][0]<=FUNC_RVA<funcs[j][1] else (FUNC_RVA,FUNC_RVA+0x800)
 b,en=fn
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 ins=list(md.disasm(pe.get_data(b,en-b),base+b))
 lines=['# Runtime object provenance at 0x6FCC2','',f'function `0x{b:08X}..0x{en:08X}`','',
        'Goal: identify provenance/type of the value in `r15` immediately before `call 0x1362D0`.','', '## Full function','','```asm']
 for i in ins:lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
 lines += ['```','','## r15-affecting instructions before 0x6FCC2','']
 for i in ins:
  r=i.address-base
  if r>CALL_RVA:break
  if 'r15' in i.op_str.lower():lines.append(f'- `0x{r:08X}: {i.mnemonic} {i.op_str}`')
 lines += ['','## Direct calls before handoff','','| RVA | target/form |','|---|---|']
 for i in ins:
  r=i.address-base
  if r>CALL_RVA:break
  if i.mnemonic!='call':continue
  t=i.op_str
  if i.operands and i.operands[0].type==X86_OP_IMM:t=f'RVA 0x{i.operands[0].imm-base:08X}'
  lines.append(f'| `0x{r:08X}` | `{t}` |')
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'runtime_object_provenance.md').write_text('\n'.join(lines),encoding='utf-8')
 print(out/'runtime_object_provenance.md')
if __name__=='__main__':main()
