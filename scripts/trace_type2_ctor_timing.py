#!/usr/bin/env python3
from pathlib import Path
import argparse,bisect
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_OP_REG,X86_OP_IMM

TARGET=0x001CDCC0
TIMING={0x98:'mt',0xAC:'straps',0xB0:'vmr',0xB8:'vmt2',0xBC:'vmt3'}
ALIASES={'r9'}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
    pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
    funcs=[]
    for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
        b=e.struct.BeginAddress;en=e.struct.EndAddress
        if b<en: funcs.append((b,en))
    funcs.sort(); starts=[b for b,_ in funcs]
    j=bisect.bisect_right(starts,TARGET)-1;fn=funcs[j]
    md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
    arr=list(md.disasm(pe.get_data(fn[0],fn[1]-fn[0]),base+fn[0]))
    aliases=set(ALIASES)
    events=[]
    calls=[]
    for idx,ins in enumerate(arr):
        # simple pointer alias propagation from R9 (config record)
        if ins.mnemonic in ('mov','lea') and len(ins.operands)==2:
            d,s=ins.operands
            if d.type==X86_OP_REG:
                dn=ins.reg_name(d.reg)
                if s.type==X86_OP_REG:
                    sn=ins.reg_name(s.reg)
                    if sn in aliases: aliases.add(dn)
                elif s.type==X86_OP_MEM and s.mem.base:
                    bn=ins.reg_name(s.mem.base)
                    if bn in aliases and s.mem.disp==0: aliases.add(dn)
        for op in ins.operands:
            if op.type==X86_OP_MEM and op.mem.base:
                bn=ins.reg_name(op.mem.base)
                if bn in aliases:
                    d=op.mem.disp
                    events.append((idx,ins,bn,d,TIMING.get(d,'')))
        if ins.mnemonic=='call':
            calls.append((idx,ins))
    lines=['# NVIDIA Type2 ctor timing-flow trace','',f'PDATA `0x{fn[0]:08X}..0x{fn[1]:08X}`','',
           'Entry `R9` is the original per-GPU config-record pointer.','',
           f'Observed aliases: `{", ".join(sorted(aliases))}`','',
           '| RVA | base | disp | label | instruction |','|---|---|---:|---|---|']
    for idx,ins,bn,d,lab in events:
        lines.append(f'| `0x{ins.address-base:08X}` | `{bn}` | `0x{d:X}` | {lab} | `{ins.mnemonic} {ins.op_str}` |')
    lines += ['','## Timing-field contexts','']
    for idx,ins,bn,d,lab in events:
        if not lab: continue
        lines += [f'### {lab} at `0x{ins.address-base:08X}`','','```asm']
        for w in arr[max(0,idx-25):min(len(arr),idx+45)]: lines.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
        lines += ['```','']
    lines += ['','## All calls','','| RVA | target/form | nearby config aliases in arg registers |','|---|---|---|']
    for idx,ins in calls:
        near=[]
        for w in arr[max(0,idx-8):idx]:
            if w.mnemonic in ('mov','lea') and len(w.operands)==2 and w.operands[0].type==X86_OP_REG:
                dn=w.reg_name(w.operands[0].reg)
                if dn in ('rcx','rdx','r8','r9'): near.append(f'{dn}<={w.op_str.split(",",1)[1].strip()}')
        lines.append(f'| `0x{ins.address-base:08X}` | `{ins.op_str}` | {"; ".join(near)} |')
    out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'nvidia_type2_ctor_timing.md';p.write_text('\n'.join(lines),encoding='utf-8')
    print('aliases',aliases,'timing_hits',sum(bool(e[4]) for e in events),'calls',len(calls))

if __name__=='__main__':main()
