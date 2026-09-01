#!/usr/bin/env python3
"""Derive setter field offsets for straps/vmr/rxboost descriptor vtables and find functions reading multiple such fields."""
from pathlib import Path
import argparse,struct,pefile
from capstone import Cs,CsError,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_OP_REG

VTABLES={'straps':0x0043F0B0,'vmr':0x0043F0E8,'rxboost':0x0043F120}
STACK={'rsp','rbp','esp','ebp'}

def rva_off(pe,rva):
 for s in pe.sections:
  if s.VirtualAddress<=rva<s.VirtualAddress+max(s.Misc_VirtualSize,s.SizeOfRawData):return s.PointerToRawData+rva-s.VirtualAddress
 raise ValueError(hex(rva))

def safe_ops(i):
 try:return i.operands
 except CsError:return ()

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 p=Path(a.binary);data=p.read_bytes();pe=pefile.PE(str(p),fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
 fields={}; methods={}
 for name,vt in VTABLES.items():
  q=struct.unpack_from('<Q',data,rva_off(pe,vt+0x10))[0];rva=q-base;methods[name]=rva
  ins=list(md.disasm(pe.get_data(rva,0x80),q))
  candidates=[]
  for i in ins:
   for oi,op in enumerate(i.operands):
    if op.type==X86_OP_MEM and oi==0 and i.mnemonic=='mov' and op.size==4 and op.mem.disp>=0:
     candidates.append((op.mem.disp,i.address-base,i.op_str))
   if i.mnemonic=='ret':break
  # target field is final dword memory store displacement
  fields[name]=candidates[-1][0] if candidates else None

 pdata=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.pdata').get_data(); funcs=[]
 for o in range(0,len(pdata)-11,12):
  b=int.from_bytes(pdata[o:o+4],'little');e=int.from_bytes(pdata[o+4:o+8],'little')
  if b and e>b:funcs.append((b,e))
 relevant=set(v for v in fields.values() if v is not None)
 rows=[]
 for b,e in funcs:
  ins=list(md.disasm(pe.get_data(b,e-b),base+b)); found={x:[] for x in relevant}
  for i in ins:
   oo=safe_ops(i)
   for oi,op in enumerate(oo):
    if op.type!=X86_OP_MEM or op.mem.disp not in relevant or op.size!=4:continue
    bn=i.reg_name(op.mem.base) if op.mem.base else ''
    if not bn or bn in STACK:continue
    # classify read-ish; writes retained separately only if needed
    is_write=(oi==0 and i.mnemonic=='mov')
    if not is_write:found[op.mem.disp].append(i)
  n=sum(bool(v) for v in found.values())
  if n>=2:rows.append((n,b,e,found,ins))
 rows.sort(key=lambda x:(-x[0],x[1]))
 lines=['# Timing-field structural fingerprint','', '## Descriptor setter fields','', '| option | vtable | setter | field offset |','|---|---|---|---|']
 for name in VTABLES:lines.append(f'| {name} | `0x{VTABLES[name]:08X}` | `0x{methods[name]:08X}` | `{fields[name]:+#x}` |')
 lines += ['','## Functions reading >=2 timing fields','',f'count: {len(rows)}','']
 for n,b,e,found,ins in rows:
  names=[name for name,offv in fields.items() if found.get(offv)]
  lines += [f'### `0x{b:08X}..0x{e:08X}` — {", ".join(names)}','','Key reads:']
  for name,offv in fields.items():
   for i in found.get(offv,[]):lines.append(f'- {name}: `0x{i.address-base:08X}: {i.mnemonic} {i.op_str}`')
  lines += ['','```asm']
  for i in ins:lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'timing_field_fingerprint.md').write_text('\n'.join(lines),encoding='utf-8')
 print(fields,'multi',len(rows))
if __name__=='__main__':main()
