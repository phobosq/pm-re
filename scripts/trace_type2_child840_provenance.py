#!/usr/bin/env python3
from pathlib import Path
import argparse
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_OP_REG

TEXT_BEGIN=0x1000; TEXT_END=0x420000
WATCH=0x840

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('binary'); ap.add_argument('--out-dir',default='notes'); a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False); base=pe.OPTIONAL_HEADER.ImageBase
 md=Cs(CS_ARCH_X86,CS_MODE_64); md.detail=True; md.skipdata=True
 arr=list(md.disasm(pe.get_data(TEXT_BEGIN,TEXT_END-TEXT_BEGIN),base+TEXT_BEGIN))
 # PDATA function ranges
 ranges=[]
 try:
  for e in pe.DIRECTORY_ENTRY_EXCEPTION:
   b=e.struct.BeginAddress; eaddr=e.struct.EndAddress
   if b and eaddr and b<eaddr: ranges.append((b,eaddr))
 except Exception: pass
 def fr(rva):
  for b,e in ranges:
   if b<=rva<e:return b,e
  return max(TEXT_BEGIN,rva-0x80),min(TEXT_END,rva+0x180)
 hits=[]
 for idx,i in enumerate(arr):
  for op in i.operands if i.id else []:
   if op.type==X86_OP_MEM and op.mem.disp==WATCH and op.mem.base:
    hits.append((idx,i,i.reg_name(op.mem.base))); break
 lines=['# Type2 +0x840 NVIDIA child provenance','', 'Tracks every `.text` memory reference with displacement `+0x840`; Type2 ctor stores the real NVIDIA child here.','',f'hits: `{len(hits)}`','']
 seen=set()
 for idx,i,bn in hits:
  rva=i.address-base; b,e=fr(rva); key=(b,e)
  lines += [f'## `0x{rva:08X}` base `{bn}` in `0x{b:08X}..0x{e:08X}`','',f'`{i.mnemonic} {i.op_str}`','', '```asm']
  # function-local slice from global arr
  loc=[z for z in arr if base+b<=z.address<base+e]
  # locate index in loc
  li=next((k for k,z in enumerate(loc) if z.address==i.address),0)
  for z in loc[max(0,li-18):min(len(loc),li+36)]:lines.append(f'0x{z.address-base:08X}: {z.mnemonic} {z.op_str}'.rstrip())
  lines += ['```']
  if key in seen: continue
  seen.add(key)
  # lightweight taint: any register loaded from [X+0x840], follow reg moves to RCX and look for call [vptr+0x68]
  tainted=set(); interesting=[]
  for z in loc:
   if z.mnemonic=='mov' and len(z.operands)>=2 and z.operands[0].type==X86_OP_REG:
    dst=z.reg_name(z.operands[0].reg); src=z.operands[1]
    if src.type==X86_OP_MEM and src.mem.disp==WATCH: tainted.add(dst)
    elif src.type==X86_OP_REG and z.reg_name(src.reg) in tainted: tainted.add(dst)
    elif dst in tainted: tainted.discard(dst)
   if z.mnemonic in ('call','jmp') and z.operands:
    op=z.operands[0]
    if op.type==X86_OP_MEM and op.mem.disp==0x68:
     interesting.append(z)
  if interesting:
   lines += ['','### slot +0x68 calls in same function','']
   for z in interesting: lines.append(f'- `0x{z.address-base:08X}: {z.mnemonic} {z.op_str}`')
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'type2_child840_provenance.md').write_text('\n'.join(lines),encoding='utf-8')
 print('hits',len(hits),[hex(i.address-base) for _,i,_ in hits])
if __name__=='__main__':main()
