#!/usr/bin/env python3
"""Recover compiler-obfuscated ASCII literals from PhoenixMiner main.

Observation: literal builder blocks emit one XOR immediate per output character.
The immediates themselves encode the intended ASCII sequence (e.g. 2D 76 73 -> '-vs').
This scanner groups dense XOR-immediate runs and reports printable sequences.
Static only; never executes the target binary.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import pefile
from capstone import Cs, CS_ARCH_X86, CS_MODE_64
from capstone.x86 import X86_OP_IMM

BEGIN=0x00129A50
END=0x0012DA40


def parse_args():
    p=argparse.ArgumentParser()
    p.add_argument('binary')
    p.add_argument('--out-dir',default='notes')
    return p.parse_args()


def printable(v): return 0x20 <= v <= 0x7e


def main():
    a=parse_args(); out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
    pe=pefile.PE(a.binary,fast_load=False); base=pe.OPTIONAL_HEADER.ImageBase
    md=Cs(CS_ARCH_X86,CS_MODE_64); md.detail=True
    ins=list(md.disasm(pe.get_data(BEGIN,END-BEGIN),base+BEGIN))

    # collect xor reg, imm8-ish occurrences; group when separated by <= 12 instructions,
    # which matches the repeated literal-builder template.
    xs=[]
    for idx,i in enumerate(ins):
        if i.mnemonic!='xor' or len(i.operands)!=2 or i.operands[1].type!=X86_OP_IMM:
            continue
        v=i.operands[1].imm & 0xff
        if printable(v): xs.append((idx,i.address-base,v,i.op_str))

    groups=[]; cur=[]
    for x in xs:
        if cur and x[0]-cur[-1][0] > 12:
            groups.append(cur); cur=[]
        cur.append(x)
    if cur: groups.append(cur)

    rows=[]
    for g in groups:
        s=''.join(chr(x[2]) for x in g)
        if len(s) < 2: continue
        # Require useful signal: option prefix, identifier-ish content, or >=3 printable chars.
        score=sum(c.isalnum() or c in '-_./:' for c in s)/len(s)
        if len(s)>=3 and score>=0.70:
            rows.append((g[0][1],g[-1][1],s,len(g)))

    mdout=['# Recovered obfuscated literals from PM62C_MAIN','',
           'Method: group printable low-byte immediates from repeated `xor reg, imm` literal-builder sequences.','',
           '| begin RVA | end RVA | chars | recovered literal |','|---|---|---:|---|']
    for b,e,s,n in rows:
        safe=s.replace('|','\\|').replace('`','\\`')
        mdout.append(f'| `0x{b:08X}` | `0x{e:08X}` | {n} | `{safe}` |')
    mdout += ['', '## High-value timing-related matches','']
    needles=('vmr','vmt','strap','rxboost','mt','nvmem','vmdag')
    hits=0
    for b,e,s,n in rows:
        if any(k in s.lower() for k in needles):
            mdout.append(f'- `0x{b:08X}`..`0x{e:08X}` → `{s}`')
            hits+=1
    if not hits: mdout.append('- none in this pass')

    (out/'main_recovered_literals.md').write_text('\n'.join(mdout),encoding='utf-8')
    print('groups',len(rows),'timing_hits',hits)
    print(out/'main_recovered_literals.md')

if __name__=='__main__': main()
