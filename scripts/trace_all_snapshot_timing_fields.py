#!/usr/bin/env python3
"""Structure-aware scan of every call to snapshot getter 0x84A60.
For each call, recover the output local passed in RDX and find accesses to timing fields
within the returned 0xD8 snapshot. Static only.
"""
from __future__ import annotations
import argparse,bisect
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_IMM,X86_OP_MEM,X86_OP_REG
GETTER=0x00084A60
SIZE=0xD8
LABELS={0x98:'mt',0xAC:'straps',0xB0:'vmr/rxboost',0xB8:'vmt2',0xBC:'vmt3'}

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
 text=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.text')
 allins=list(md.disasm(text.get_data(),base+text.VirtualAddress));byaddr={i.address-base:k for k,i in enumerate(allins)}
 calls=[]
 for i in allins:
  if i.mnemonic=='call' and i.operands and i.operands[0].type==X86_OP_IMM and i.operands[0].imm-base==GETTER:calls.append(i.address-base)
 lines=['# All snapshot timing-field consumers','',f'getter `0x{GETTER:08X}`, calls `{len(calls)}`','',
        '| getter call | PDATA | output local | timing hits |','|---|---|---|---:|']
 details=[]
 for c in calls:
  fn=fnof(c)
  if not fn:continue
  b,en=fn;arr=allins[byaddr[b]:] if b in byaddr else list(md.disasm(pe.get_data(b,en-b),base+b))
  arr=[i for i in arr if i.address-base<en]
  ci=next((n for n,i in enumerate(arr) if i.address-base==c),None)
  if ci is None:continue
  outreg=None;outdisp=None;setup=None
  # walk back for last LEA RDX,[rsp/rbp+disp] or MOV RDX,reg derived from such LEA (simple case)
  aliases={}
  for i in arr[max(0,ci-24):ci]:
   if i.mnemonic=='lea' and len(i.operands)==2 and i.operands[0].type==X86_OP_REG and i.operands[1].type==X86_OP_MEM:
    dst=i.reg_name(i.operands[0].reg);mem=i.operands[1].mem;bn=i.reg_name(mem.base)
    if bn in ('rsp','rbp'):aliases[dst]=(bn,mem.disp,i.address-base)
   elif i.mnemonic=='mov' and len(i.operands)==2 and i.operands[0].type==X86_OP_REG and i.operands[1].type==X86_OP_REG:
    dst=i.reg_name(i.operands[0].reg);src=i.reg_name(i.operands[1].reg)
    if src in aliases:aliases[dst]=aliases[src]
  if 'rdx' in aliases:outreg,outdisp,setup=aliases['rdx']
  hits=[]
  if outreg is not None:
   for idx,i in enumerate(arr[ci+1:],start=ci+1):
    for op in i.operands:
     if op.type!=X86_OP_MEM or i.reg_name(op.mem.base)!=outreg:continue
     rel=op.mem.disp-outdisp
     if 0<=rel<SIZE:
      hits.append((idx,i,rel,LABELS.get(rel,'')))
  th=sum(bool(x[3]) for x in hits)
  ol='unknown' if outreg is None else f'{outreg}{outdisp:+#x}'
  lines.append(f'| `0x{c:08X}` | `0x{b:08X}..0x{en:08X}` | `{ol}` | {th} |')
  if hits:details.append((c,b,en,outreg,outdisp,hits,arr))
 lines += ['','## Detailed field accesses','']
 for c,b,en,oreg,od,hits,arr in details:
  lines += [f'### getter `0x{c:08X}` in `0x{b:08X}..0x{en:08X}` output `{oreg}{od:+#x}`','',
            '| RVA | snapshot off | label | instruction |','|---|---:|---|---|']
  for idx,i,o,l in hits:lines.append(f'| `0x{i.address-base:08X}` | `+0x{o:X}` | {l} | `{i.mnemonic} {i.op_str}` |')
  for idx,i,o,l in hits:
   if not l:continue
   lines += ['',f'#### {l} at `0x{i.address-base:08X}`','','```asm']
   for w in arr[max(0,idx-15):min(len(arr),idx+25)]:lines.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
   lines += ['```']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'all_snapshot_timing_fields.md').write_text('\n'.join(lines),encoding='utf-8')
 print('calls',len(calls),'functions_with_accesses',len(details))
if __name__=='__main__':main()
