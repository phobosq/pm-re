#!/usr/bin/env python3
"""Focused static decoder for the first argv-processing path in PhoenixMiner 6.2c.

Never executes the target binary. Uses PE mapping + Capstone only.
"""
from __future__ import annotations

import argparse
from pathlib import Path
from collections import Counter
import pefile
from capstone import Cs, CS_ARCH_X86, CS_MODE_64
from capstone.x86 import X86_OP_IMM, X86_OP_MEM, X86_OP_REG

MAIN_BEGIN = 0x00129A50
MAIN_END = 0x0012DA40
FIRST_BEGIN = 0x00129A50
FIRST_END = 0x0012A250
HELPERS = [
    (0x000355E0, 0x00035880, "argv_string_ctor_candidate"),
    (0x00220EB0, 0x00220F70, "token_transform_candidate"),
    (0x003D2F70, 0x003D30A0, "string_compare_candidate"),
    (0x00220F70, 0x00221040, "token_transform_candidate_2"),
    (0x00226FB0, 0x00227100, "repeated_parser_helper"),
]


def args():
    p=argparse.ArgumentParser()
    p.add_argument("binary")
    p.add_argument("--out-dir", default="notes")
    return p.parse_args()


def fmt(insn, base):
    return f"0x{insn.address-base:08X}: {insn.mnemonic} {insn.op_str}".rstrip()


def decode(pe, md, begin, end):
    base=pe.OPTIONAL_HEADER.ImageBase
    return list(md.disasm(pe.get_data(begin,end-begin),base+begin))


def op_reg(insn, op):
    return insn.reg_name(op.reg) if op.type==X86_OP_REG else None


def stack_byte_events(insns, base):
    out=[]
    for insn in insns:
        if insn.mnemonic != "mov" or len(insn.operands) != 2:
            continue
        dst,src=insn.operands
        if dst.type != X86_OP_MEM or src.type != X86_OP_REG:
            continue
        m=dst.mem
        if not m.base or insn.reg_name(m.base) != "rsp":
            continue
        # Byte stores are useful even if the value is computed dynamically.
        if dst.size == 1:
            out.append((insn.address-base,m.disp,insn.reg_name(src.reg),insn.op_str))
    return out


def main():
    a=args(); out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
    pe=pefile.PE(a.binary,fast_load=False); base=pe.OPTIONAL_HEADER.ImageBase
    md=Cs(CS_ARCH_X86,CS_MODE_64); md.detail=True

    first=decode(pe,md,FIRST_BEGIN,FIRST_END)
    report=[
        "# PM62C_MAIN first argv parser pass",
        "",
        "Static-only focused decode.",
        "",
        "## Entry facts",
        "",
        "```asm",
    ]
    for i in first[:35]: report.append(fmt(i,base))
    report += ["```","","## Full first parser window","","```asm"]
    for i in first: report.append(fmt(i,base))
    report += ["```","","## Stack byte stores in first window","", "| RVA | RSP disp | source | instruction |", "|---|---:|---|---|"]
    for rva,disp,src,text in stack_byte_events(first,base):
        report.append(f"| `0x{rva:08X}` | `0x{disp:X}` | `{src}` | `{text}` |")

    report += ["","## argv-like indexed reads","", "These are memory operands with scale 8 in the first parser window.",""]
    for insn in first:
        hits=[]
        for op in insn.operands:
            if op.type==X86_OP_MEM and op.mem.index and op.mem.scale==8:
                hits.append(op)
        if hits: report.append(f"- `{fmt(insn,base)}`")

    report += ["","## Calls in first parser window","", "| callsite | operand |", "|---|---|"]
    for insn in first:
        if insn.mnemonic=="call": report.append(f"| `0x{insn.address-base:08X}` | `{insn.op_str}` |")

    for begin,end,label in HELPERS:
        ins=decode(pe,md,begin,end)
        report += ["",f"## Helper `{label}` 0x{begin:08X}..0x{end:08X}","","```asm"]
        for i in ins: report.append(fmt(i,base))
        report += ["```"]

    # Find every direct call from MAIN to selected helpers, with 12 instructions of context.
    whole=decode(pe,md,MAIN_BEGIN,MAIN_END)
    targets={base+b:label for b,_,label in HELPERS}
    report += ["","## Selected-helper callsites throughout PM62C_MAIN",""]
    for idx,insn in enumerate(whole):
        if insn.mnemonic!='call' or not insn.operands or insn.operands[0].type!=X86_OP_IMM:
            continue
        tgt=insn.operands[0].imm
        if tgt not in targets: continue
        report += [f"### {targets[tgt]} at `0x{insn.address-base:08X}`","","```asm"]
        for x in whole[max(0,idx-8):min(len(whole),idx+7)]: report.append(fmt(x,base))
        report += ["```",""]

    (out/'main_parser_firstpass.md').write_text('\n'.join(report),encoding='utf-8')
    print(out/'main_parser_firstpass.md')

if __name__=='__main__': main()
