#!/usr/bin/env python3
"""Focused static analysis around confirmed -vmr literal builder at RVA 0x000E8F6E.
Never executes PhoenixMiner.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import pefile
from capstone import Cs, CS_ARCH_X86, CS_MODE_64
from capstone.x86 import X86_OP_IMM, X86_OP_MEM

ANCHOR=0x000E8F6E


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('binary'); ap.add_argument('--out-dir',default='notes'); a=ap.parse_args()
    out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
    pe=pefile.PE(a.binary,fast_load=False); base=pe.OPTIONAL_HEADER.ImageBase
    # find pdata function containing anchor
    pdata=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.pdata')
    d=pdata.get_data(); begin=end=None
    for o in range(0,len(d)-12,12):
        b=int.from_bytes(d[o:o+4],'little'); e=int.from_bytes(d[o+4:o+8],'little')
        if b<=ANCHOR<e: begin,end=b,e; break
    if begin is None:
        begin=ANCHOR-0x300; end=ANCHOR+0x500
    md=Cs(CS_ARCH_X86,CS_MODE_64); md.detail=True
    ins=list(md.disasm(pe.get_data(begin,end-begin),base+begin))
    lines=['# Confirmed `-vmr` parser anchor','',f'anchor literal-builder RVA: `0x{ANCHOR:08X}`',f'containing pdata range: `0x{begin:08X}..0x{end:08X}`','', '## Full containing function','', '```asm']
    for i in ins: lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
    lines += ['```','','## Calls around vmr anchor','']
    anchor_idx=min(range(len(ins)),key=lambda k:abs((ins[k].address-base)-ANCHOR))
    lo=max(0,anchor_idx-60); hi=min(len(ins),anchor_idx+160)
    for idx in range(lo,hi):
        i=ins[idx]
        if i.mnemonic!='call': continue
        lines += [f'### call @ `0x{i.address-base:08X}` → `{i.op_str}`','', '```asm']
        for x in ins[max(lo,idx-8):min(hi,idx+9)]: lines.append(f'0x{x.address-base:08X}: {x.mnemonic} {x.op_str}'.rstrip())
        lines += ['```','']
    lines += ['## Writes after vmr anchor (next ~200 instructions)','']
    for i in ins[anchor_idx:min(len(ins),anchor_idx+220)]:
        if not i.operands: continue
        op=i.operands[0]
        if op.type==X86_OP_MEM and i.mnemonic in ('mov','movzx','movsx','inc','dec','add','sub','and','or','xor'):
            lines.append(f'- `0x{i.address-base:08X}: {i.mnemonic} {i.op_str}`')
    (out/'vmr_anchor_trace.md').write_text('\n'.join(lines),encoding='utf-8')
    print(hex(begin),hex(end),len(ins),out/'vmr_anchor_trace.md')

if __name__=='__main__': main()
