#!/usr/bin/env python3
"""Find vendor-specific derived virtual methods that consume this+0x90 context.
Static only; PhoenixMiner is never executed.
"""
from __future__ import annotations
import argparse,bisect,struct
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_OP_IMM,X86_REG_RSP,X86_REG_RBP,X86_REG_ESP,X86_REG_EBP

VTABLES={0x0044B3D8:'type1',0x004BD558:'type2'}
STACK={X86_REG_RSP,X86_REG_RBP,X86_REG_ESP,X86_REG_EBP}
SHARED={0x00138970,0x00132720,0x00067840,0x0036EFD0}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 text=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.text');tlo=text.VirtualAddress;thi=tlo+max(text.Misc_VirtualSize,text.SizeOfRawData)
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en: funcs.append((b,en))
 funcs.sort();starts=[b for b,_ in funcs]
 def fnof(r):
  j=bisect.bisect_right(starts,r)-1
  return funcs[j] if j>=0 and funcs[j][0]<=r<funcs[j][1] else None
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 methods=[]
 for vrva,name in VTABLES.items():
  raw=pe.get_data(vrva,0xC0);non=0
  for n in range(len(raw)//8):
   q=struct.unpack_from('<Q',raw,n*8)[0];m=q-base if base<=q<base+pe.OPTIONAL_HEADER.SizeOfImage else None
   if m is not None and tlo<=m<thi:
    non=0;methods.append((name,n,m))
   else:
    non+=1
    if n>=4 and non>=3: break
 lines=['# Derived context consumers','',
        'Scans vendor-specific virtual methods for non-stack memory accesses at displacement `+0x90`.',
        'Shared base methods are excluded except where noted.','']
 hits=[]
 for name,slot,m in methods:
  if m in SHARED: continue
  fn=fnof(m)
  if fn: b,en=fn;ins=list(md.disasm(pe.get_data(b,en-b),base+b))
  else:
   ins=list(md.disasm(pe.get_data(m,0x180),base+m));cut=[]
   for i in ins:
    cut.append(i)
    if i.mnemonic in ('ret','jmp'): break
   ins=cut;b=m;en=m+(ins[-1].address-base-m+ins[-1].size if ins else 0x20)
  for idx,i in enumerate(ins):
   matched=False
   for op in i.operands:
    if op.type==X86_OP_MEM and op.mem.disp==0x90 and op.mem.base not in STACK:
     matched=True;break
   if matched: hits.append((name,slot,m,b,en,idx,ins))
 lines += [f'consumer hits: {len(hits)}','']
 for k,(name,slot,m,b,en,idx,ins) in enumerate(hits,1):
  i=ins[idx]
  lines += [f'## hit {k}: {name} slot `+0x{slot*8:X}` method `0x{m:08X}`','',
            f'context access: `0x{i.address-base:08X}: {i.mnemonic} {i.op_str}`','',
            '### Nearby calls/indirect branches','']
  for w in ins[idx:min(len(ins),idx+35)]:
   if w.mnemonic=='call':
    if w.operands and w.operands[0].type==X86_OP_IMM: tgt=f'RVA 0x{w.operands[0].imm-base:08X}'
    else: tgt=w.op_str
    lines.append(f'- `0x{w.address-base:08X}` call `{tgt}`')
   elif w.mnemonic=='jmp' and ('ptr' in w.op_str or '[' in w.op_str):
    lines.append(f'- `0x{w.address-base:08X}` jmp `{w.op_str}`')
  lines += ['','### Context','```asm']
  for w in ins[max(0,idx-14):min(len(ins),idx+35)]: lines.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'derived_context_consumers.md';p.write_text('\n'.join(lines),encoding='utf-8');print(p)
if __name__=='__main__':main()
