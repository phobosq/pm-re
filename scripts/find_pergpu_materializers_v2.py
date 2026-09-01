#!/usr/bin/env python3
"""Optimized per-GPU materializer scan. Static only."""
from __future__ import annotations
import argparse,bisect
from pathlib import Path
from collections import defaultdict
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_OP_IMM

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('binary'); ap.add_argument('--out-dir',default='notes'); a=ap.parse_args()
    pe=pefile.PE(a.binary,fast_load=False); base=pe.OPTIONAL_HEADER.ImageBase
    text=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.text')
    funcs=[]
    for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
        b=e.struct.BeginAddress; en=e.struct.EndAddress
        if b<en: funcs.append((b,en))
    funcs.sort(); starts=[b for b,_ in funcs]
    def fnof(rva):
        j=bisect.bisect_right(starts,rva)-1
        if j>=0 and funcs[j][0]<=rva<funcs[j][1]: return funcs[j]
        return None
    md=Cs(CS_ARCH_X86,CS_MODE_64); md.detail=True; md.skipdata=True
    grouped=defaultdict(list)
    for i in md.disasm(text.get_data(),base+text.VirtualAddress):
        if i.id==0: continue
        fn=fnof(i.address-base)
        if fn: grouped[fn].append(i)
    rows=[]
    for (b,en),fi in grouped.items():
        owner_sites=[]; stride=[]; calls=[]; interesting_offsets=set()
        for i in fi:
            for op in i.operands:
                if op.type==X86_OP_MEM:
                    if op.mem.disp==0x2c0: owner_sites.append(i)
                    if op.mem.disp in (0x98,0xac,0xb0,0xb8,0xbc): interesting_offsets.add(op.mem.disp)
            if i.mnemonic=='imul' and any(op.type==X86_OP_IMM and (op.imm & 0xffffffffffffffff)==0xd8 for op in i.operands): stride.append(i)
            if i.mnemonic=='call': calls.append(i)
        if owner_sites:
            rows.append((bool(stride),len(interesting_offsets),b,en,owner_sites,stride,calls,fi,interesting_offsets))
    rows.sort(key=lambda x:(-x[0],-x[1],x[2]))
    lines=['# per-GPU materializers v2','', 'Fingerprint: owner `+0x2C0`, stride `0xD8`, timing offsets `{0x98,0xAC,0xB0,0xB8,0xBC}`.','',
           '| exact stride | timing offsets in same fn | PDATA | +0x2C0 | calls |','|---|---:|---|---:|---:|']
    for exact,n,b,en,owners,strides,calls,fi,offs in rows:
        lines.append(f'| {exact} | {n} | `0x{b:08X}..0x{en:08X}` | {len(owners)} | {len(calls)} |')
    lines += ['','## Exact-stride details','']
    for exact,n,b,en,owners,strides,calls,fi,offs in rows:
        if not exact: continue
        lines += [f'### `0x{b:08X}..0x{en:08X}` — offsets {", ".join(hex(x) for x in sorted(offs)) or "none"}','','```asm']
        for i in fi:
            mark=i.mnemonic=='call'
            for op in i.operands:
                if op.type==X86_OP_MEM and op.mem.disp in (0x2c0,0x98,0xac,0xb0,0xb8,0xbc): mark=True
            if i.mnemonic=='imul' and any(op.type==X86_OP_IMM and (op.imm & 0xffffffffffffffff)==0xd8 for op in i.operands): mark=True
            if mark: lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
        lines += ['```','']
    out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True); (out/'pergpu_materializers_v2.md').write_text('\n'.join(lines),encoding='utf-8')
    print('owner_functions',len(rows),'exact_stride',sum(1 for r in rows if r[0]))
if __name__=='__main__': main()
