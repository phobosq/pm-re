#!/usr/bin/env python3
"""Find functions that read timing fields from argument-derived pointers.
Tracks simple register aliases of RCX/RDX/R8/R9 and ranks functions by distinct
config offsets read. Static only; target binary is never executed.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64,CS_AC_READ
from capstone.x86 import X86_OP_MEM,X86_OP_REG
FIELDS={0x98:'mt',0xAC:'straps',0xB0:'vmr/rxboost',0xB8:'vmt2',0xBC:'vmt3'}
ARGREGS=('rcx','rdx','r8','r9')

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True;md.skipdata=True
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en:funcs.append((b,en))
 funcs=sorted(set(funcs))
 results=[]
 for b,en in funcs:
  arr=[i for i in md.disasm(pe.get_data(b,en-b),base+b) if i.id!=0]
  # provenance: reg -> (arg_name, additive_offset). We only need simple aliases.
  prov={r:(r,0) for r in ARGREGS};hits=[]
  for i in arr:
   # record reads before updating provenance
   for op in i.operands:
    if op.type!=X86_OP_MEM or not (op.access & CS_AC_READ):continue
    bn=i.reg_name(op.mem.base)
    if bn not in prov:continue
    arg,add=prov[bn];off=add+op.mem.disp
    if off in FIELDS:
      hits.append((i.address-base,arg,off,FIELDS[off],i.mnemonic+' '+i.op_str))
   # propagate simple mov dst,src and lea dst,[src+disp]
   if i.mnemonic=='mov' and len(i.operands)==2 and i.operands[0].type==X86_OP_REG:
    dst=i.reg_name(i.operands[0].reg);src=i.operands[1]
    if src.type==X86_OP_REG and i.reg_name(src.reg) in prov:prov[dst]=prov[i.reg_name(src.reg)]
    elif dst in prov:prov.pop(dst,None)
   elif i.mnemonic=='lea' and len(i.operands)==2 and i.operands[0].type==X86_OP_REG and i.operands[1].type==X86_OP_MEM:
    dst=i.reg_name(i.operands[0].reg);m=i.operands[1].mem;bn=i.reg_name(m.base)
    if bn in prov and m.index==0:
      arg,add=prov[bn];prov[dst]=(arg,add+m.disp)
    elif dst in prov:prov.pop(dst,None)
   else:
    # conservative kill for explicit destination-register writes, except compare/test/call/jumps
    if i.mnemonic not in ('cmp','test','call') and i.operands and i.operands[0].type==X86_OP_REG:
      dst=i.reg_name(i.operands[0].reg)
      if dst in prov and i.mnemonic not in ('push',):prov.pop(dst,None)
  if hits:
   distinct=sorted(set(h[2] for h in hits));byarg={}
   for h in hits:byarg.setdefault(h[1],set()).add(h[2])
   results.append((b,en,hits,distinct,byarg))
 results.sort(key=lambda x:(max((len(v) for v in x[4].values()),default=0),len(x[3]),len(x[2])),reverse=True)
 lines=['# Argument-derived timing-record consumers','',f'functions with timing-field reads: `{len(results)}`','',
        '| PDATA | best arg | distinct fields | total hits |','|---|---|---|---:|']
 for b,en,hits,distinct,byarg in results:
  best=max(byarg.items(),key=lambda kv:len(kv[1]));labels=', '.join(FIELDS[o] for o in sorted(best[1]))
  lines.append(f'| `0x{b:08X}..0x{en:08X}` | `{best[0]}` | {labels} | {len(hits)} |')
 lines += ['','## Details','']
 for b,en,hits,distinct,byarg in results:
  best=max(len(v) for v in byarg.values())
  if best<2 and 0xB0 not in distinct:continue
  lines += [f'### `0x{b:08X}..0x{en:08X}`','','| RVA | arg | field | instruction |','|---|---|---|---|']
  for r,arg,o,lab,ins in hits:lines.append(f'| `0x{r:08X}` | `{arg}` | {lab} `+0x{o:X}` | `{ins}` |')
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'timing_record_consumers.md').write_text('\n'.join(lines),encoding='utf-8')
 print('functions',len(results))
if __name__=='__main__':main()
