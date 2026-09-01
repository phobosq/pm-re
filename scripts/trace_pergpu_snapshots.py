#!/usr/bin/env python3
"""Trace full per-GPU record snapshots from 0xE3F60 callers to their next calls.
Static only. Target binary is never executed.
"""
from __future__ import annotations
import argparse,bisect
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_IMM

CALLSITES=[0x0006FA51,0x0007FC7A,0x000A9247,0x000B2426]

def main():
    ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
    pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
    funcs=[]
    for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
        b=e.struct.BeginAddress;en=e.struct.EndAddress
        if b<en: funcs.append((b,en))
    funcs.sort();starts=[b for b,_ in funcs]
    def fnof(r):
        j=bisect.bisect_right(starts,r)-1
        return funcs[j] if j>=0 and funcs[j][0]<=r<funcs[j][1] else None
    md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
    lines=['# per-GPU snapshot propagation','', 'Anchor accessor: `0x000E3F60`, record size/stride `0xD8`.','']
    for cs in CALLSITES:
        fn=fnof(cs)
        if not fn: continue
        b,en=fn; ins=list(md.disasm(pe.get_data(b,en-b),base+b))
        idx=next((k for k,i in enumerate(ins) if i.address-base==cs),None)
        if idx is None: continue
        lines += [f'## callsite `0x{cs:08X}` in `0x{b:08X}..0x{en:08X}`','','```asm']
        # enough tail to include full 0xD8 copy plus several next calls
        for i in ins[max(0,idx-5):min(len(ins),idx+100)]:
            lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
        lines += ['```','','### Calls after accessor','', '| RVA | target/form |','|---|---|']
        seen=0
        for i in ins[idx+1:]:
            if i.mnemonic!='call': continue
            target=i.op_str
            if i.operands and i.operands[0].type==X86_OP_IMM:
                target=f'RVA 0x{i.operands[0].imm-base:08X}'
            lines.append(f'| `0x{i.address-base:08X}` | `{target}` |')
            seen+=1
            if seen>=8: break
        lines += ['']
    out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'pergpu_snapshot_propagation.md').write_text('\n'.join(lines),encoding='utf-8')
    print(out/'pergpu_snapshot_propagation.md')
if __name__=='__main__':main()
