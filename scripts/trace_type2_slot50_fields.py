#!/usr/bin/env python3
"""List all accesses to the 0xD8 snapshot local in Type2 slot +0x50.
Snapshot base is rsp+0xB0 immediately after get_snapshot(0x84A60).
Static only.
"""
from __future__ import annotations
import argparse,bisect
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_OP_IMM
TARGET=0x001CF8B0
SNAP=0xB0
SIZE=0xD8
LABELS={0x98:'mt',0xAC:'straps',0xB0:'vmr/rxboost',0xB8:'vmt2',0xBC:'vmt3'}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en:funcs.append((b,en))
 funcs.sort();starts=[b for b,_ in funcs];j=bisect.bisect_right(starts,TARGET)-1;b,en=funcs[j]
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 arr=list(md.disasm(pe.get_data(b,en-b),base+b));hits=[]
 for idx,i in enumerate(arr):
  for op in i.operands:
   if op.type!=X86_OP_MEM or i.reg_name(op.mem.base)!='rsp':continue
   if SNAP<=op.mem.disp<SNAP+SIZE:
    off=op.mem.disp-SNAP;hits.append((idx,i,off,LABELS.get(off,'')))
 lines=['# Type2 slot +0x50 snapshot field accesses','',f'snapshot local: `rsp+0x{SNAP:X}` size `0x{SIZE:X}`','',
        '| RVA | snapshot off | label | instruction |','|---|---:|---|---|']
 for idx,i,o,l in hits:lines.append(f'| `0x{i.address-base:08X}` | `+0x{o:X}` | {l} | `{i.mnemonic} {i.op_str}` |')
 lines += ['','## Contexts for timing-related or late-record fields','']
 for idx,i,o,l in hits:
  if not l and o<0x90:continue
  lines += [f'### `+0x{o:X}` {l} @ `0x{i.address-base:08X}`','','```asm']
  for w in arr[max(0,idx-18):min(len(arr),idx+28)]:lines.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'type2_slot50_fields.md').write_text('\n'.join(lines),encoding='utf-8')
 print('hits',len(hits),'timing',sum(bool(x[3]) for x in hits))
if __name__=='__main__':main()
