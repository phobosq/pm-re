#!/usr/bin/env python3
from __future__ import annotations
import argparse,struct
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_REG_RIP,X86_OP_IMM
TARGETS={0x000584A0:'dispatcher_584A0',0x00058210:'factory_type1',0x000582D0:'factory_type2'}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 refs=[]
 for s in pe.sections:
  data=s.get_data(); srva=s.VirtualAddress
  for off in range(0,max(0,len(data)-7),8):
   v=struct.unpack_from('<Q',data,off)[0]
   for rva,name in TARGETS.items():
    if v==base+rva: refs.append((srva+off,s.Name.rstrip(b'\0').decode(errors='replace'),rva,name))
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True;md.skipdata=True
 text=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.text')
 ins=[i for i in md.disasm(text.get_data(),base+text.VirtualAddress) if i.id!=0]
 ref_rvas={x[0] for x in refs}; code=[]
 for i in ins:
  for op in i.operands:
   if op.type==X86_OP_MEM and op.mem.base==X86_REG_RIP:
    rr=(i.address+i.size+op.mem.disp)-base
    if rr in ref_rvas: code.append((i.address-base,rr,i.mnemonic,i.op_str))
  if i.operands and i.operands[0].type==X86_OP_IMM:
   imm=i.operands[0].imm-base
   if imm in TARGETS: code.append((i.address-base,imm,i.mnemonic,i.op_str))
 lines=['# Context interface / factory dispatch provenance','',f'data refs: {len(refs)}  code refs: {len(code)}','', '## Data qwords','', '| RVA | section | target | label |','|---|---|---|---|']
 for rr,sec,t,n in refs: lines.append(f'| `0x{rr:08X}` | `{sec}` | `0x{t:08X}` | {n} |')
 lines += ['','## Code refs','', '| RVA | ref/target | instruction |','|---|---|---|']
 for r,rr,m,o in code: lines.append(f'| `0x{r:08X}` | `0x{rr:08X}` | `{m} {o}` |')
 addr_to_idx={i.address-base:k for k,i in enumerate(ins)}
 lines += ['','## Contexts','']
 for r,rr,m,o in code:
  k=addr_to_idx.get(r)
  if k is None:continue
  lines += [f'### `0x{r:08X}` -> `0x{rr:08X}`','','```asm']
  for w in ins[max(0,k-16):min(len(ins),k+20)]: lines.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'context_interface_source.md';p.write_text('\n'.join(lines),encoding='utf-8');print('refs',len(refs),'code',len(code))
if __name__=='__main__':main()
