#!/usr/bin/env python3
"""Find direct timing-field accesses inside confirmed derived runtime virtual methods.
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
FIELDS={
 0x400:'A.mt',0x414:'A.straps',0x418:'A.vmr_rxboost',0x420:'A.vmt2',0x424:'A.vmt3',
 0x4D8:'B.mt',0x4EC:'B.straps',0x4F0:'B.vmr_rxboost',0x4F8:'B.vmt2',0x4FC:'B.vmt3',
}

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
 uniq=[];seen=set()
 for x in methods:
  if (x[0],x[1],x[2]) not in seen: seen.add(x);uniq.append(x)
 hits=[]
 for name,slot,m in uniq:
  fn=fnof(m)
  if fn: b,en=fn;ins=list(md.disasm(pe.get_data(b,en-b),base+b))
  else:
   ins=list(md.disasm(pe.get_data(m,0x200),base+m));cut=[]
   for i in ins:
    cut.append(i)
    if i.mnemonic in ('ret','jmp'): break
   ins=cut;b=m;en=m+(ins[-1].address-base-m+ins[-1].size if ins else 0x20)
  for idx,i in enumerate(ins):
   for op in i.operands:
    if op.type==X86_OP_MEM and op.mem.disp in FIELDS and op.mem.base not in STACK:
     hits.append((name,slot,m,b,en,idx,ins,op.mem.disp))
 lines=['# Type-safe derived timing consumers','',
        'Confirmed object layout:',
        '- snapshot A base `this+0x368`',
        '- snapshot B base `this+0x440`',
        '- VMR/RXBoost therefore at `this+0x418` and `this+0x4F0`.',
        '',f'hits: {len(hits)}','']
 for k,(name,slot,m,b,en,idx,ins,disp) in enumerate(hits,1):
  i=ins[idx]
  lines += [f'## hit {k}: {name} slot `+0x{slot*8:X}` method `0x{m:08X}` field {FIELDS[disp]} `+0x{disp:X}`','',
            f'`0x{i.address-base:08X}: {i.mnemonic} {i.op_str}`','',
            '### Calls after field access','']
  for w in ins[idx:min(len(ins),idx+45)]:
   if w.mnemonic=='call':
    if w.operands and w.operands[0].type==X86_OP_IMM: tgt=f'RVA 0x{w.operands[0].imm-base:08X}'
    else: tgt=w.op_str
    lines.append(f'- `0x{w.address-base:08X}` -> `{tgt}`')
   if w.mnemonic=='jmp' and ('[' in w.op_str or 'ptr' in w.op_str): lines.append(f'- `0x{w.address-base:08X}` jmp `{w.op_str}`')
  lines += ['','### Context','```asm']
  for w in ins[max(0,idx-18):min(len(ins),idx+45)]: lines.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'derived_timing_consumers.md';p.write_text('\n'.join(lines),encoding='utf-8');print(p)
if __name__=='__main__':main()
