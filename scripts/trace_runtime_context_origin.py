#!/usr/bin/env python3
"""Trace address-taken references to the runtime object constructor and vtable.
Goal: recover the factory/caller that supplies ctor RDX -> this+0x90 context object.
Static only.
"""
from __future__ import annotations
import argparse,bisect
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_OP_IMM,X86_REG_RIP

TARGETS={
 0x0012F250:'runtime_ctor',
 0x00440528:'base_vtable',
 0x00440560:'derived_vtable',
}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 text=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.text')
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en: funcs.append((b,en))
 funcs.sort();starts=[b for b,_ in funcs]
 def fnof(r):
  j=bisect.bisect_right(starts,r)-1
  return funcs[j] if j>=0 and funcs[j][0]<=r<funcs[j][1] else None
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 ins=list(md.disasm(text.get_data(),base+text.VirtualAddress))
 hits=[]
 for idx,i in enumerate(ins):
  # direct call/immediate refs
  for op in i.operands:
   target_rva=None
   if op.type==X86_OP_IMM:
    v=op.imm
    if base<=v<base+pe.OPTIONAL_HEADER.SizeOfImage: target_rva=v-base
   elif op.type==X86_OP_MEM and op.mem.base==X86_REG_RIP:
    v=i.address+i.size+op.mem.disp
    if base<=v<base+pe.OPTIONAL_HEADER.SizeOfImage: target_rva=v-base
   if target_rva in TARGETS:
    hits.append((idx,i,target_rva,fnof(i.address-base)))
 lines=['# Runtime context origin','',
        'Targets: ctor `0x12F250`, base vtable `0x440528`, derived vtable `0x440560`.','',
        f'hits: {len(hits)}','']
 for n,(idx,i,t,fn) in enumerate(hits,1):
  f='none' if not fn else f'0x{fn[0]:08X}..0x{fn[1]:08X}'
  lines += [f'## hit {n}: {TARGETS[t]} `0x{t:08X}` from `0x{i.address-base:08X}` in `{f}`','', '```asm']
  lo=max(0,idx-18);hi=min(len(ins),idx+24)
  for w in ins[lo:hi]: lines.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'runtime_context_origin.md';p.write_text('\n'.join(lines),encoding='utf-8');print(p)
if __name__=='__main__':main()
