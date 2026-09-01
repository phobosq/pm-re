#!/usr/bin/env python3
"""Find reads of VMR after config snapshot is copied into runtime object.

Confirmed by 0x1362D0:
  object+0x368 = per-GPU snapshot A -> VMR at object+0x418
  object+0x440 = per-GPU snapshot B -> VMR at object+0x4F0
Static only; target binary is never executed.
"""
from __future__ import annotations
import argparse,bisect
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64,CS_AC_READ
from capstone.x86 import X86_OP_MEM

OFFS={0x418:'vmr_runtime_A',0x4f0:'vmr_runtime_B'}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 text=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.text')
 funcs=[]
 for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
  b=e.struct.BeginAddress;en=e.struct.EndAddress
  if b<en: funcs.append((b,en))
 funcs.sort();starts=[b for b,_ in funcs]
 def fnof(r):
  j=bisect.bisect_right(starts,r)-1
  return funcs[j] if j>=0 and funcs[j][0]<=r<funcs[j][1] else None
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True;md.skipdata=True
 ins=[i for i in md.disasm(text.get_data(),base+text.VirtualAddress) if i.id!=0]
 hits=[]
 for idx,i in enumerate(ins):
  for op in i.operands:
   if op.type!=X86_OP_MEM or op.mem.disp not in OFFS: continue
   is_read=bool(op.access & CS_AC_READ) if op.access else not (i.operands and i.operands[0] is op and i.mnemonic.startswith('mov'))
   if is_read: hits.append((idx,i,op.mem.disp,fnof(i.address-base)))
 lines=['# Runtime-object VMR read candidates','',
        'Confirmed VMR copies: `object+0x418` and `object+0x4F0`.','',f'read candidates: {len(hits)}','',
        '| RVA | runtime field | PDATA | instruction |','|---|---|---|---|']
 for idx,i,o,fn in hits:
  f='none' if not fn else f'0x{fn[0]:08X}..0x{fn[1]:08X}'
  lines.append(f'| `0x{i.address-base:08X}` | {OFFS[o]} `+0x{o:X}` | `{f}` | `{i.mnemonic} {i.op_str}` |')
 lines += ['','## Contexts','']
 seen=set()
 for idx,i,o,fn in hits:
  key=fn or (i.address-base,i.address-base+i.size)
  if key in seen: continue
  seen.add(key)
  lines += [f'### `{("0x%08X..0x%08X"%key) if fn else ("0x%08X"%(i.address-base))}`','','```asm']
  for w in ins[max(0,idx-16):min(len(ins),idx+25)]: lines.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'runtime_vmr_reads.md').write_text('\n'.join(lines),encoding='utf-8')
 print('runtime_vmr_reads',len(hits))
if __name__=='__main__':main()
