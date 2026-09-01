#!/usr/bin/env python3
from pathlib import Path
import argparse,bisect
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_REG_RIP
TARGETS=[0x001E8A10,0x001E2FE0,0x001E5160]

def is_data(ins):
 return ins.mnemonic=='.byte'

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en:funcs.append((b,en))
 funcs.sort();starts=[b for b,_ in funcs]
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True;md.skipdata=True
 textsec=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.text')
 text=textsec.get_data();tbase=textsec.VirtualAddress
 allins=list(md.disasm(text,base+tbase))
 lines=['# NVIDIA big-slot dynamic-call profile','']
 dynslots={}
 for tgt in TARGETS:
  j=bisect.bisect_right(starts,tgt)-1;fn=funcs[j]
  arr=list(md.disasm(pe.get_data(fn[0],fn[1]-fn[0]),base+fn[0]))
  lines += [f'## function `0x{fn[0]:08X}..0x{fn[1]:08X}`','', '| callsite | slot RVA | instruction |','|---|---|---|']
  for ins in arr:
   if is_data(ins) or ins.mnemonic!='call': continue
   try: ops=ins.operands
   except Exception: continue
   if not ops: continue
   op=ops[0]
   if op.type==X86_OP_MEM and op.mem.base==X86_REG_RIP:
    slot=(ins.address+ins.size+op.mem.disp)-base
    dynslots.setdefault(slot,[]).append(ins.address-base)
    lines.append(f'| `0x{ins.address-base:08X}` | `0x{slot:08X}` | `{ins.mnemonic} {ins.op_str}` |')
  lines.append('')
 for slot,calls in sorted(dynslots.items()):
  lines += [f'## slot `0x{slot:08X}`','',f'used by: {", ".join(f"0x{x:08X}" for x in calls)}','', '### references / candidate writers','']
  for i,ins in enumerate(allins):
   if is_data(ins): continue
   try: ops=ins.operands
   except Exception: continue
   hit=False
   for op in ops:
    if op.type==X86_OP_MEM and op.mem.base==X86_REG_RIP:
     ref=(ins.address+ins.size+op.mem.disp)-base
     if ref==slot: hit=True
   if not hit: continue
   lines += ['```asm']
   for w in allins[max(0,i-10):min(len(allins),i+12)]: lines.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
   lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'nvidia_bigslots_dynamic.md';p.write_text('\n'.join(lines),encoding='utf-8');print('slots',len(dynslots))
if __name__=='__main__':main()
