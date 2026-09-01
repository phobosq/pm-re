#!/usr/bin/env python3
"""Trace the tail of the unique five-field timing consumer.

Static-only. Never executes the target binary.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import pefile
from capstone import Cs, CS_ARCH_X86, CS_MODE_64
from capstone.x86 import X86_OP_IMM, X86_OP_MEM

FUNC_BEGIN=0x003053C0
FUNC_END=0x00305BB6
TAIL_BEGIN=0x00305920
TAIL_END=0x00305BB6


def decode(pe, md, b, e):
    base=pe.OPTIONAL_HEADER.ImageBase
    return list(md.disasm(pe.get_data(b,e-b),base+b))


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('binary'); ap.add_argument('--out-dir',default='notes'); a=ap.parse_args()
    pe=pefile.PE(a.binary,fast_load=False); base=pe.OPTIONAL_HEADER.ImageBase
    md=Cs(CS_ARCH_X86,CS_MODE_64); md.detail=True
    ins=decode(pe,md,TAIL_BEGIN,TAIL_END)

    # import IAT map
    imports={}
    if hasattr(pe,'DIRECTORY_ENTRY_IMPORT'):
        for dll in pe.DIRECTORY_ENTRY_IMPORT:
            d=dll.dll.decode(errors='replace')
            for imp in dll.imports:
                if imp.address:
                    n=imp.name.decode(errors='replace') if imp.name else f'ord_{imp.ordinal}'
                    imports[imp.address]=(d,n)

    lines=['# Five-field timing consumer tail','',f'function: `0x{FUNC_BEGIN:08X}..0x{FUNC_END:08X}`',f'tail: `0x{TAIL_BEGIN:08X}..0x{TAIL_END:08X}`','',
           'Confirmed config fields: mt `+0x98`, straps `+0xAC`, vmr/rxboost `+0xB0`, vmt2 `+0xB8`, vmt3 `+0xBC`.','', '## Tail disassembly','','```asm']
    for i in ins:
        lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
    lines += ['```','','## Calls in tail','','| callsite | target/form |','|---|---|']
    for i in ins:
        if i.mnemonic!='call': continue
        desc=i.op_str
        if i.operands and i.operands[0].type==X86_OP_IMM:
            t=i.operands[0].imm; desc=f'RVA 0x{t-base:08X}'
        elif i.operands and i.operands[0].type==X86_OP_MEM:
            m=i.operands[0].mem
            if m.base and i.reg_name(m.base)=='rip':
                slot=i.address+i.size+m.disp
                desc+=f' ; IAT/ptr VA 0x{slot:X}'
                if slot in imports: desc+=f' = {imports[slot][0]}!{imports[slot][1]}'
        lines.append(f'| `0x{i.address-base:08X}` | `{desc}` |')

    # all direct rel32 callers to the function start in .text
    text=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.text')
    md2=Cs(CS_ARCH_X86,CS_MODE_64); md2.detail=True; md2.skipdata=True
    callers=[]
    target=base+FUNC_BEGIN
    for i in md2.disasm(text.get_data(),base+text.VirtualAddress):
        if i.id==0: continue
        if i.mnemonic=='call' and i.operands and i.operands[0].type==X86_OP_IMM and i.operands[0].imm==target:
            callers.append(i.address-base)
    lines += ['','## Direct callers to 0x3053C0','']
    if callers:
        lines += [f'- `0x{x:08X}`' for x in callers]
    else:
        lines += ['none (likely indirect/table dispatch or no direct rel32 xref)']

    out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
    (out/'timing_consumer_tail.md').write_text('\n'.join(lines),encoding='utf-8')
    print(out/'timing_consumer_tail.md')

if __name__=='__main__': main()
