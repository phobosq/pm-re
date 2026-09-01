#!/usr/bin/env python3
"""Structure-aware scan of every call to snapshot getter 0x84A60.
For each call, recover the output local passed in RDX and find accesses to timing fields
within the returned 0xD8 snapshot. Static only.
"""
from __future__ import annotations
import argparse,bisect,struct
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_OP_REG
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
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True;md.skipdata=True
 text=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.text')
 tdata=text.get_data();trva=text.VirtualAddress
 # Robust direct-call scan: E8 rel32, target = next_instruction + rel32.
 calls=[]
 for off in range(0,len(tdata)-5):
  if tdata[off]!=0xE8:continue
  rel=struct.unpack_from('<i',tdata,off+1)[0]
  call_rva=trva+off
  target=call_rva+5+rel
  if target==GETTER:calls.append(call_rva)
 lines=['# All snapshot timing-field consumers','',f'getter `0x{GETTER:08X}`, calls `{len(calls)}`','',
        '| getter call | PDATA | output local | timing hits |','|---|---|---|---:|']
 details=[]
 for c in calls:
  fn=fnof(c)
  if not fn:continue
  b,en=fn;arr=[i for i in md.disasm(pe.get_data(b,en-b),base+b) if i.id!=0]
  ci=next((n for n,i in enumerate(arr) if i.address-base==c),None)
  if ci is None:continue
  # Walk backward and recover RDX as an alias of rsp/rbp local.
  aliases={}
  for i in arr[max(0,ci-32):ci]:
   if i.mnemonic=='lea' and len(i.operands)==2 and i.operands[0].type==X86_OP_REG and i.operands[1].type==X86_OP_MEM:
    dst=i.reg_name(i.operands[0].reg);mem=i.operands[1].mem;bn=i.reg_name(mem.base)
    if bn in ('rsp','rbp'):aliases[dst]=(bn,mem.disp,i.address-base)
   elif i.mnemonic=='mov' and len(i.operands)==2 and i.operands[0].type==X86_OP_REG and i.operands[1].type==X86_OP_REG:
    dst=i.reg_name(i.operands[0].reg);src=i.reg_name(i.operands[1].reg)
    if src in aliases:aliases[dst]=aliases[src]
    elif dst in aliases:aliases.pop(dst,None)
  outreg=outdisp=setup=None
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
