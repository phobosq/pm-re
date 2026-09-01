#!/usr/bin/env python3
"""Enumerate functions that materialize the confirmed per-GPU config array.

Fingerprint: memory displacement +0x2C0 (owner->per_gpu base) plus arithmetic
compatible with stride 0xD8. Static only; target binary is never executed.
"""
from __future__ import annotations
import argparse
from pathlib import Path
from collections import defaultdict
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_OP_IMM


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('binary'); ap.add_argument('--out-dir',default='notes'); a=ap.parse_args()
    pe=pefile.PE(a.binary,fast_load=False); base=pe.OPTIONAL_HEADER.ImageBase
    text=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.text')
    md=Cs(CS_ARCH_X86,CS_MODE_64); md.detail=True; md.skipdata=True
    ins=[i for i in md.disasm(text.get_data(),base+text.VirtualAddress) if i.id!=0]

    funcs=[]
    if hasattr(pe,'DIRECTORY_ENTRY_EXCEPTION'):
        for e in pe.DIRECTORY_ENTRY_EXCEPTION:
            b=e.struct.BeginAddress; en=e.struct.EndAddress
            if b<en: funcs.append((b,en))
    funcs.sort()

    def owner(rva):
        lo=0; hi=len(funcs)
        while lo<hi:
            m=(lo+hi)//2
            if funcs[m][0]<=rva: lo=m+1
            else: hi=m
        if lo:
            b,en=funcs[lo-1]
            if b<=rva<en: return b,en
        return None

    grouped=defaultdict(list)
    for idx,i in enumerate(ins):
        has_2c0=any(op.type==X86_OP_MEM and op.mem.disp==0x2c0 for op in i.operands)
        if not has_2c0: continue
        fn=owner(i.address-base)
        if fn: grouped[fn].append(idx)

    rows=[]
    for fn,idxs in grouped.items():
        b,en=fn
        fi=[i for i in ins if b<=i.address-base<en]
        stride=[]
        for i in fi:
            if i.mnemonic=='imul' and any(op.type==X86_OP_IMM and (op.imm & 0xffffffffffffffff)==0xd8 for op in i.operands): stride.append(i.address-base)
            # lea x,[x+x*8] / shifts can participate, but keep direct 0xd8 as strongest marker
        calls=[]
        for i in fi:
            if i.mnemonic=='call': calls.append((i.address-base,i.op_str))
        rows.append((1 if stride else 0,b,en,idxs,stride,calls,fi))
    rows.sort(key=lambda x:(-x[0],x[1]))

    lines=['# per-GPU config materializers','', 'Confirmed owner field: `+0x2C0`; confirmed record stride: `0xD8`.','',
           '| exact stride | PDATA | +0x2C0 sites | calls |','|---|---|---:|---:|']
    for exact,b,en,idxs,stride,calls,fi in rows:
        lines.append(f'| {bool(exact)} | `0x{b:08X}..0x{en:08X}` | {len(idxs)} | {len(calls)} |')
    lines += ['','## Exact-stride functions','']
    for exact,b,en,idxs,stride,calls,fi in rows:
        if not exact: continue
        lines += [f'### `0x{b:08X}..0x{en:08X}`','','Key +0x2C0 / stride / calls:']
        for i in fi:
            mark=False
            if any(op.type==X86_OP_MEM and op.mem.disp==0x2c0 for op in i.operands): mark=True
            if i.mnemonic=='imul' and any(op.type==X86_OP_IMM and (op.imm & 0xffffffffffffffff)==0xd8 for op in i.operands): mark=True
            if i.mnemonic=='call': mark=True
            if mark: lines.append(f'- `0x{i.address-base:08X}: {i.mnemonic} {i.op_str}`')
        lines += ['','```asm']
        for i in fi: lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
        lines += ['```','']

    out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
    (out/'pergpu_materializers.md').write_text('\n'.join(lines),encoding='utf-8')
    print('functions',len(rows),'exact_stride',sum(r[0] for r in rows))

if __name__=='__main__': main()
