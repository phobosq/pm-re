#!/usr/bin/env python3
"""Decode first confirmed runtime VMR consumer 0x1302C0 and callsite neighborhoods.
Static only; target binary is never executed.
"""
from __future__ import annotations
import argparse,bisect
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_IMM
TARGET=0x001302C0
SITES=[0x000A33D7,0x000A5601,0x000AA762]

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en:funcs.append((b,en))
 funcs.sort();starts=[b for b,_ in funcs]
 def fnof(r):
  j=bisect.bisect_right(starts,r)-1
  return funcs[j] if j>=0 and funcs[j][0]<=r<funcs[j][1] else None
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 lines=['# Runtime VMR consumer 0x1302C0','', 'Confirmed runtime VMR reads feed EDX at callsites around A33D7/A5601/AA762.','']
 fn=fnof(TARGET) or (TARGET,TARGET+0x600);b,en=fn;ins=list(md.disasm(pe.get_data(b,en-b),base+b))
 lines += [f'## target PDATA `0x{b:08X}..0x{en:08X}`','','```asm']
 for i in ins:lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
 lines += ['```','','### Calls from target','','| RVA | target/form |','|---|---|']
 for i in ins:
  if i.mnemonic!='call':continue
  t=i.op_str
  if i.operands and i.operands[0].type==X86_OP_IMM:t=f'RVA 0x{i.operands[0].imm-base:08X}'
  lines.append(f'| `0x{i.address-base:08X}` | `{t}` |')
 for s in SITES:
  fn=fnof(s)
  if not fn:continue
  b,en=fn;ii=list(md.disasm(pe.get_data(b,en-b),base+b));idx=min(range(len(ii)),key=lambda k:abs((ii[k].address-base)-s))
  lines += ['',f'## callsite neighborhood `0x{s:08X}`','','```asm']
  for i in ii[max(0,idx-12):min(len(ii),idx+28)]:lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
  lines += ['```']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'runtime_vmr_consumer_1302c0.md').write_text('\n'.join(lines),encoding='utf-8')
 print(f'target=0x{b:X}..0x{en:X}')
if __name__=='__main__':main()
