#!/usr/bin/env python3
"""Profile top argument-derived timing-record consumer candidates.
Reports direct callers, direct callees, imported IAT calls, and full bodies.
Static only.
"""
from __future__ import annotations
import argparse,bisect,struct
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_IMM,X86_OP_MEM,X86_REG_RIP
TARGETS=[0x003053C0,0x003C397C,0x0041D627,0x0015BB20,0x002284F0]

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
 imports={}
 if hasattr(pe,'DIRECTORY_ENTRY_IMPORT'):
  for d in pe.DIRECTORY_ENTRY_IMPORT:
   dll=d.dll.decode(errors='replace')
   for imp in d.imports:
    if not imp.address:continue
    name=imp.name.decode(errors='replace') if imp.name else f'ord{imp.ordinal}'
    imports[imp.address-base]=f'{dll}!{name}'
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True;md.skipdata=True
 text=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.text');tdata=text.get_data();trva=text.VirtualAddress
 # Robust E8 direct-call map.
 caller_map={t:[] for t in TARGETS}
 for off in range(len(tdata)-5):
  if tdata[off]!=0xE8:continue
  rel=struct.unpack_from('<i',tdata,off+1)[0];crva=trva+off;dst=crva+5+rel
  if dst in caller_map:caller_map[dst].append(crva)
 lines=['# Timing consumer candidate profiles','']
 for t in TARGETS:
  fn=fnof(t) or (t,t+0x800);b,en=fn;arr=[i for i in md.disasm(pe.get_data(b,en-b),base+b) if i.id!=0]
  lines += [f'## `0x{t:08X}` PDATA `0x{b:08X}..0x{en:08X}`','',f'direct callers: `{len(caller_map[t])}`','']
  for c in caller_map[t]:
   cfn=fnof(c);lines.append(f'- `0x{c:08X}` from `{("0x%08X..0x%08X"%cfn) if cfn else "no PDATA"}`')
  lines += ['','### Calls','','| RVA | target |','|---|---|']
  for i in arr:
   if i.mnemonic!='call':continue
   target=i.op_str
   if i.operands:
    op=i.operands[0]
    if op.type==X86_OP_IMM:target=f'RVA 0x{op.imm-base:08X}'
    elif op.type==X86_OP_MEM and op.mem.base==X86_REG_RIP:
     rva=i.address+i.size+op.mem.disp-base
     target=imports.get(rva,f'IAT/RIP 0x{rva:08X}')
   lines.append(f'| `0x{i.address-base:08X}` | `{target}` |')
  lines += ['','### Full body','','```asm']
  for i in arr:lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'timing_consumer_candidate_profiles.md').write_text('\n'.join(lines),encoding='utf-8')
if __name__=='__main__':main()
