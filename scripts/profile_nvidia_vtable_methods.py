#!/usr/bin/env python3
"""Profile high-value NVIDIA Type2 vtable methods.
Static only. Captures calls and memory offsets using the entry-this alias.
"""
from __future__ import annotations
import argparse,bisect,collections
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_OP_IMM,X86_REG_RCX
TARGETS={
 0x48:0x001CF7C0,
 0x58:0x001D0730,
 0x70:0x001CDFD0,
 0x78:0x001D0AD0,
 0x80:0x001CE0B0,
 0x88:0x001CFED0,
 0x90:0x001CF880,
}
KNOWN={0x418:'vmrA',0x4F0:'vmrB',0x538:'generation',0x90:'context',0x98:'gpu_index',0x7C0:'vendor_lock',0x810:'vendor_state',0x838:'vendor_obj',0x840:'nvml_obj?'}
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
 lines=['# Focused NVIDIA Type2 vtable profile','']
 for slot,t in TARGETS.items():
  fn=fnof(t)
  lines += [f'## slot `+0x{slot:X}` method `0x{t:08X}` PDATA `{("0x%08X..0x%08X"%fn) if fn else "none"}`','']
  if not fn:
   lines += ['No PDATA body.',''];continue
  arr=list(md.disasm(pe.get_data(fn[0],fn[1]-fn[0]),base+fn[0]))
  # track simple aliases of entry RCX: mov reg,rcx only; stop alias if overwritten is too much, but useful.
  aliases={'rcx'}
  accesses=[];calls=[]
  for i in arr:
   # add simple mov reg,rcx aliases
   if i.mnemonic=='mov' and len(i.operands)>=2 and i.operands[0].type==1 and i.operands[1].type==1:
    dst=i.reg_name(i.operands[0].reg);src=i.reg_name(i.operands[1].reg)
    if src in aliases:aliases.add(dst)
   for op in i.operands:
    if op.type==X86_OP_MEM:
     br=i.reg_name(op.mem.base) if op.mem.base else ''
     if br in aliases:
      accesses.append((i.address-base,br,op.mem.disp,i.mnemonic,i.op_str))
   if i.mnemonic=='call':
    if i.operands and i.operands[0].type==X86_OP_IMM: form=f'0x{i.operands[0].imm-base:08X}'
    else: form=i.op_str
    calls.append((i.address-base,form))
  lines += ['### this-derived accesses','', '| RVA | base | disp | label | instruction |','|---|---|---:|---|---|']
  for r,br,d,m,o in accesses:
   lab=KNOWN.get(d,'')
   lines.append(f'| `0x{r:08X}` | `{br}` | `0x{d:X}` | {lab} | `{m} {o}` |')
  lines += ['','### calls','', '| RVA | target/form |','|---|---|']
  for r,f in calls:lines.append(f'| `0x{r:08X}` | `{f}` |')
  lines += ['','### Full body','```asm']
  for i in arr:lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'nvidia_vtable_profile.md';p.write_text('\n'.join(lines),encoding='utf-8');print(p)
if __name__=='__main__':main()
