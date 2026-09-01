#!/usr/bin/env python3
"""Find static consumers of the confirmed VMR config field.

Confirmed store shape:
    base = *([descriptor+8] + 0x2c0)
    slot = base + index*0xd8
    vmr  = dword [slot + 0xb0]

This scanner ranks x86-64 instructions with memory displacement 0xB0 and gives
extra score when the local window also contains IMUL by 0xD8 and/or +0x2C0.
Static only; target binary is never executed.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_OP_IMM


def main():
    ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
    pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
    text=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.text')
    md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True;md.skipdata=True
    ins=list(md.disasm(text.get_data(),base+text.VirtualAddress))
    hits=[]
    for idx,i in enumerate(ins):
        mems=[op.mem for op in i.operands if op.type==X86_OP_MEM and op.mem.disp==0xb0]
        if not mems: continue
        lo=max(0,idx-12);hi=min(len(ins),idx+13);window=ins[lo:hi]
        has_stride=False;has_baseoff=False
        for w in window:
            if w.mnemonic=='imul' and any(op.type==X86_OP_IMM and (op.imm & 0xffffffffffffffff)==0xd8 for op in w.operands): has_stride=True
            for op in w.operands:
                if op.type==X86_OP_MEM and op.mem.disp==0x2c0: has_baseoff=True
        score=1+3*has_stride+3*has_baseoff
        hits.append((score,idx,has_stride,has_baseoff))
    hits.sort(key=lambda x:(-x[0],ins[x[1]].address))
    lines=['# VMR field consumer candidates','',f'confirmed field: stride `0xD8`, offset `+0xB0`; total +0xB0 hits: {len(hits)}','',
           '| score | RVA | instruction | stride 0xD8 nearby | owner +0x2C0 nearby |','|---:|---|---|---|---|']
    for score,idx,hs,hb in hits:
        i=ins[idx];lines.append(f'| {score} | `0x{i.address-base:08X}` | `{i.mnemonic} {i.op_str}` | {hs} | {hb} |')
    lines += ['','## High-score contexts','']
    for score,idx,hs,hb in hits[:30]:
        if score<4: break
        i=ins[idx];lines += [f'### score {score} @ `0x{i.address-base:08X}`','','```asm']
        for w in ins[max(0,idx-12):min(len(ins),idx+13)]: lines.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
        lines += ['```','']
    out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'vmr_field_consumers.md').write_text('\n'.join(lines),encoding='utf-8')
    print('hits',len(hits),'high',sum(1 for h in hits if h[0]>=4))

if __name__=='__main__':main()
