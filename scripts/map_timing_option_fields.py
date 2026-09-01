#!/usr/bin/env python3
"""Map known timing option literal anchors -> descriptor ctor -> vtable -> setter -> per-GPU field.
Static only; target is never executed.
"""
from pathlib import Path
import argparse,struct,pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_IMM,X86_OP_MEM

ANCHORS={
 'mt':0x000E8D60,
 'straps':0x000E8E2C,
 'vmr':0x000E8F6E,
 'rxboost':0x000E9026,
 'vmt2':0x000E9245,
 'vmt3':0x000E931D,
 'vmdag':0x000E94BD,
 'leavemt':0x000EEE36,
}

def rva_off(pe,rva):
 for s in pe.sections:
  if s.VirtualAddress<=rva<s.VirtualAddress+max(s.Misc_VirtualSize,s.SizeOfRawData):return s.PointerToRawData+rva-s.VirtualAddress
 raise ValueError(hex(rva))

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 p=Path(a.binary);data=p.read_bytes();pe=pefile.PE(str(p),fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 rows=[]
 details=[]
 for name,anchor in ANCHORS.items():
  win=list(md.disasm(pe.get_data(anchor,0x180),base+anchor))
  calls=[]
  for i in win:
   if i.mnemonic=='call' and i.operands and i.operands[0].type==X86_OP_IMM:
    r=i.operands[0].imm-base
    if 0x000DD000<=r<0x000DE000:calls.append((i.address-base,r))
  # descriptor constructors in this parser family are tiny 0xDDxxx calls; select first candidate
  ctor=calls[0][1] if calls else None
  vt=None;setter=None;field=None
  if ctor is not None:
   ci=list(md.disasm(pe.get_data(ctor,0x30),base+ctor))
   for i in ci:
    if i.mnemonic=='lea' and len(i.operands)==2 and i.operands[1].type==X86_OP_MEM:
     m=i.operands[1].mem
     if m.base and i.reg_name(m.base)=='rip':
      vt=(i.address+i.size+m.disp)-base;break
   if vt is not None:
    q=struct.unpack_from('<Q',data,rva_off(pe,vt+0x10))[0]
    if base<=q<base+pe.OPTIONAL_HEADER.SizeOfImage:
     setter=q-base
     si=list(md.disasm(pe.get_data(setter,0x90),q))
     stores=[]
     for i in si:
      if i.mnemonic=='mov' and len(i.operands)>=2 and i.operands[0].type==X86_OP_MEM and i.operands[0].size==4:
       m=i.operands[0].mem
       bn=i.reg_name(m.base) if m.base else ''
       if bn not in ('rsp','rbp','esp','ebp') and m.disp>=0:stores.append((m.disp,i.address-base,i.op_str))
      if i.mnemonic=='ret':break
     if stores:field=stores[-1][0]
  rows.append((name,anchor,ctor,vt,setter,field,calls))
  details.append((name,win[:120]))
 lines=['# Timing option -> descriptor -> per-GPU field map','',
 '| option | literal anchor | ctor | vtable | setter +0x10 | field |','|---|---|---|---|---|---|']
 for name,anchor,ctor,vt,setter,field,calls in rows:
  h=lambda x: f'`0x{x:08X}`' if x is not None else '—'
  fs=f'`+0x{field:X}`' if field is not None else '—'
  lines.append(f'| {name} | {h(anchor)} | {h(ctor)} | {h(vt)} | {h(setter)} | {fs} |')
 lines+=['','## Candidate 0xDDxxx calls after each literal anchor','']
 for name,anchor,ctor,vt,setter,field,calls in rows:
  lines.append(f'- **{name}**: '+(', '.join(f'`0x{cs:08X}->0x{t:08X}`' for cs,t in calls) if calls else 'none'))
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'timing_option_field_map.md').write_text('\n'.join(lines),encoding='utf-8')
 print([(r[0],hex(r[5]) if r[5] is not None else None) for r in rows])
if __name__=='__main__':main()
