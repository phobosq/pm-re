#!/usr/bin/env python3
"""Trace owner+0x2C0 lifecycle in the 0xE0000..0xF0000 parser/config family.
Static only; target binary is never executed.
"""
from __future__ import annotations
import argparse,bisect
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM

BEGIN=0x000E0000
END=0x000F0000

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('binary'); ap.add_argument('--out-dir',default='notes'); a=ap.parse_args()
    pe=pefile.PE(a.binary,fast_load=False); base=pe.OPTIONAL_HEADER.ImageBase
    funcs=[]
    for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
        b=e.struct.BeginAddress; en=e.struct.EndAddress
        if b<en: funcs.append((b,en))
    funcs.sort(); starts=[x[0] for x in funcs]
    def fnof(rva):
        j=bisect.bisect_right(starts,rva)-1
        if j>=0 and funcs[j][0]<=rva<funcs[j][1]: return funcs[j]
        return None
    md=Cs(CS_ARCH_X86,CS_MODE_64); md.detail=True
    ins=list(md.disasm(pe.get_data(BEGIN,END-BEGIN),base+BEGIN))
    hits=[]
    for idx,i in enumerate(ins):
        if any(op.type==X86_OP_MEM and op.mem.disp==0x2c0 for op in i.operands):
            hits.append((idx,i,fnof(i.address-base)))
    lines=['# owner +0x2C0 lifecycle in 0xE-family','',f'hits: {len(hits)}','',
           '| RVA | PDATA | instruction |','|---|---|---|']
    for idx,i,fn in hits:
        f='none' if not fn else f'0x{fn[0]:08X}..0x{fn[1]:08X}'
        lines.append(f'| `0x{i.address-base:08X}` | `{f}` | `{i.mnemonic} {i.op_str}` |')
    lines += ['','## Contexts','']
    for idx,i,fn in hits:
        lines += [f'### `0x{i.address-base:08X}`','','```asm']
        for w in ins[max(0,idx-14):min(len(ins),idx+15)]:
            lines.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
        lines += ['```','']
    out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'owner_2c0_lifecycle.md').write_text('\n'.join(lines),encoding='utf-8')
    print('hits',len(hits))
if __name__=='__main__': main()
