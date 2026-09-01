#!/usr/bin/env python3
"""Find timing-field reads after type-safe runtime snapshot getter 0x084A60.

For each direct call to 0x084A60, recover the local snapshot pointer from the
nearest preceding LEA RDX,[RBP/RSP+disp], then look for accesses to
snapshot+{0x98,0xAC,0xB0,0xB8,0xBC} in the same function.
Static only; target binary is never executed.
"""
from __future__ import annotations
import argparse,bisect
from pathlib import Path
from collections import defaultdict
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_IMM,X86_OP_MEM,X86_OP_REG

GETTER=0x00084A60
FIELDS={0x98:'mt',0xac:'straps',0xb0:'vmr_rxboost',0xb8:'vmt2',0xbc:'vmt3'}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 text=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.text')
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en:funcs.append((b,en))
 funcs.sort();starts=[b for b,_ in funcs]
 def fnof(r):
  j=bisect.bisect_right(starts,r)-1
  return funcs[j] if j>=0 and funcs[j][0]<=r<funcs[j][1] else None
 mdall=Cs(CS_ARCH_X86,CS_MODE_64);mdall.detail=True;mdall.skipdata=True
 allins=[i for i in mdall.disasm(text.get_data(),base+text.VirtualAddress) if i.id!=0]
 callers=[]
 for i in allins:
  if i.mnemonic=='call' and i.operands and i.operands[0].type==X86_OP_IMM and i.operands[0].imm==base+GETTER:
   callers.append((i.address-base,fnof(i.address-base)))
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 lines=['# Type-safe timing snapshot reads','',f'getter callers: {len(callers)}','',
        '| getter call | PDATA | snapshot base | timing hits | calls after |','|---|---|---|---:|---:|']
 details=[]
 for callrva,fn in callers:
  if not fn:continue
  b,en=fn;ins=list(md.disasm(pe.get_data(b,en-b),base+b))
  idx=next((k for k,x in enumerate(ins) if x.address-base==callrva),None)
  if idx is None:continue
  snap=None
  # Win64 arg2 in RDX; identify local LEA shortly before getter.
  for k in range(idx-1,max(-1,idx-15),-1):
   x=ins[k]
   if x.mnemonic=='lea' and len(x.operands)>=2 and x.operands[0].type==X86_OP_REG and x.reg_name(x.operands[0].reg)=='rdx' and x.operands[1].type==X86_OP_MEM:
    m=x.operands[1].mem
    basereg=x.reg_name(m.base) if m.base else None
    if basereg in ('rbp','rsp') and not m.index:
     snap=(basereg,m.disp);break
  hits=[]
  if snap:
   sreg,sdisp=snap
   wanted={sdisp+off:(off,name) for off,name in FIELDS.items()}
   # Entire remainder of fn: snapshot may be consumed much later.
   for j in range(idx+1,len(ins)):
    x=ins[j]
    for op in x.operands:
     if op.type!=X86_OP_MEM:continue
     m=op.mem
     if not m.base or x.reg_name(m.base)!=sreg or m.index:continue
     if m.disp in wanted:
      off,name=wanted[m.disp]; hits.append((j,x,off,name))
  calls_after=[x for x in ins[idx+1:] if x.mnemonic=='call']
  sb='unresolved' if not snap else f'{snap[0]}{snap[1]:+d}'
  lines.append(f'| `0x{callrva:08X}` | `0x{b:08X}..0x{en:08X}` | `{sb}` | {len(hits)} | {len(calls_after)} |')
  details.append((callrva,b,en,ins,idx,snap,hits))
 lines += ['','## Functions with timing hits','']
 for callrva,b,en,ins,idx,snap,hits in details:
  if not hits:continue
  lines += [f'### getter `0x{callrva:08X}` in `0x{b:08X}..0x{en:08X}` — snapshot `{snap[0]}{snap[1]:+d}`','','Timing hits:']
  for j,x,off,name in hits:lines.append(f'- {name} `+0x{off:X}`: `0x{x.address-base:08X}: {x.mnemonic} {x.op_str}`')
  # Context around each distinct hit plus nearby downstream calls.
  shown=set()
  for j,x,off,name in hits:
   if x.address in shown:continue
   shown.add(x.address)
   lines += ['',f'#### {name} @ `0x{x.address-base:08X}`','','```asm']
   for w in ins[max(idx,j-14):min(len(ins),j+30)]:lines.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
   lines += ['```']
  lines += ['']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'typesafe_timing_snapshot_reads.md').write_text('\n'.join(lines),encoding='utf-8')
 print('getters',len(callers),'functions_with_hits',sum(1 for d in details if d[-1]))
if __name__=='__main__':main()
