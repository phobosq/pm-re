#!/usr/bin/env python3
"""Find direct callers of per-GPU record accessor 0xE3F60 and dump context.
Static only; target binary is never executed.
"""
from __future__ import annotations
import argparse,bisect
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_IMM

TARGET=0x000E3F60

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('binary'); ap.add_argument('--out-dir',default='notes'); a=ap.parse_args()
    pe=pefile.PE(a.binary,fast_load=False); base=pe.OPTIONAL_HEADER.ImageBase
    text=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.text')
    funcs=[]
    for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
        b=e.struct.BeginAddress; en=e.struct.EndAddress
        if b<en: funcs.append((b,en))
    funcs.sort(); starts=[x[0] for x in funcs]
    def fnof(rva):
        j=bisect.bisect_right(starts,rva)-1
        if j>=0 and funcs[j][0]<=rva<funcs[j][1]: return funcs[j]
        return None
    md=Cs(CS_ARCH_X86,CS_MODE_64); md.detail=True; md.skipdata=True
    ins=[i for i in md.disasm(text.get_data(),base+text.VirtualAddress) if i.id!=0]
    hits=[]
    for idx,i in enumerate(ins):
        if i.mnemonic=='call' and i.operands and i.operands[0].type==X86_OP_IMM and i.operands[0].imm==base+TARGET:
            hits.append((idx,i,fnof(i.address-base)))
    lines=['# Callers of per-GPU accessor 0xE3F60','',f'direct callers: {len(hits)}','',
           '| callsite | PDATA |','|---|---|']
    for idx,i,fn in hits:
        f='none' if not fn else f'0x{fn[0]:08X}..0x{fn[1]:08X}'
        lines.append(f'| `0x{i.address-base:08X}` | `{f}` |')
    lines += ['','## Contexts','']
    for idx,i,fn in hits:
        lines += [f'### `0x{i.address-base:08X}`','','```asm']
        for w in ins[max(0,idx-20):min(len(ins),idx+31)]:
            lines.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
        lines += ['```','']
    out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'pergpu_accessor_callers.md').write_text('\n'.join(lines),encoding='utf-8')
    print('callers',len(hits))
if __name__=='__main__': main()
