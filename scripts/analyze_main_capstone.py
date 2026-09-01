#!/usr/bin/env python3
"""Capstone census for PhoenixMiner application main (RVA 0x00129A50).

Static only. Never executes the target binary.

Outputs:
  notes/main_call_census.csv
  notes/main_indirect_calls.md
  notes/main_argv_candidates.md

Requires: pip install pefile capstone
"""

from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path

import pefile
from capstone import Cs, CS_ARCH_X86, CS_MODE_64
from capstone.x86 import X86_OP_IMM, X86_OP_MEM, X86_OP_REG

IMAGE_BASE_DEFAULT = 0x140000000
MAIN_BEGIN = 0x00129A50
MAIN_END = 0x0012DA40


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("binary", nargs="?", default=r"C:\temp\pm\samples\work\unpacked\PhoenixMiner_6.2c_Windows\PhoenixMiner.exe.bin")
    p.add_argument("--out-dir", default=r"C:\temp\pm\notes")
    p.add_argument("--begin", type=lambda x: int(x, 0), default=MAIN_BEGIN)
    p.add_argument("--end", type=lambda x: int(x, 0), default=MAIN_END)
    return p.parse_args()


def operand_desc(insn, op):
    if op.type == X86_OP_REG:
        return insn.reg_name(op.reg)
    if op.type == X86_OP_IMM:
        return f"0x{op.imm & 0xFFFFFFFFFFFFFFFF:X}"
    if op.type == X86_OP_MEM:
        m = op.mem
        parts = []
        if m.base:
            parts.append(insn.reg_name(m.base))
        if m.index:
            idx = insn.reg_name(m.index)
            parts.append(f"{idx}*{m.scale}" if m.scale != 1 else idx)
        expr = "+".join(parts)
        if m.disp:
            sign = "+" if m.disp >= 0 else "-"
            expr += (sign if expr else ("" if m.disp >= 0 else "-")) + f"0x{abs(m.disp):X}"
        return f"[{expr}]"
    return "?"


def classify_call(insn):
    if not insn.operands:
        return "unknown", ""
    op = insn.operands[0]
    if op.type == X86_OP_IMM:
        return "direct", f"0x{op.imm - IMAGE_BASE_DEFAULT:08X}"
    if op.type == X86_OP_REG:
        return "register_indirect", insn.reg_name(op.reg)
    if op.type == X86_OP_MEM:
        m = op.mem
        if m.base and insn.reg_name(m.base) == "rip":
            target_va = insn.address + insn.size + m.disp
            return "rip_indirect", f"0x{target_va - IMAGE_BASE_DEFAULT:08X}"
        return "memory_indirect", operand_desc(insn, op)
    return "unknown", operand_desc(insn, op)


def fmt(insn):
    return f"0x{insn.address - IMAGE_BASE_DEFAULT:08X}: {insn.mnemonic} {insn.op_str}".rstrip()


def main():
    args = parse_args()
    binary = Path(args.binary)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    pe = pefile.PE(str(binary), fast_load=False)
    image_base = pe.OPTIONAL_HEADER.ImageBase
    global IMAGE_BASE_DEFAULT
    IMAGE_BASE_DEFAULT = image_base

    begin, end = args.begin, args.end
    size = end - begin
    raw = pe.get_data(begin, size)

    md = Cs(CS_ARCH_X86, CS_MODE_64)
    md.detail = True
    insns = list(md.disasm(raw, image_base + begin))

    rows = []
    indirect_md = [
        "# PM62C_MAIN indirect call census",
        "",
        f"range: `0x{begin:08X}..0x{end:08X}`",
        "",
        "Static-only Capstone decode. Context = previous 5 + next 3 decoded instructions.",
        "",
    ]

    call_indices = []
    for i, insn in enumerate(insns):
        if insn.mnemonic != "call":
            continue
        kind, target = classify_call(insn)
        call_indices.append(i)
        rows.append({
            "callsite_rva": f"0x{insn.address - image_base:08X}",
            "kind": kind,
            "target": target,
            "op_str": insn.op_str,
        })
        if kind != "direct":
            indirect_md += [f"## {fmt(insn)}", f"kind: `{kind}` target/source: `{target}`", "", "```asm"]
            for c in insns[max(0, i - 5): min(len(insns), i + 4)]:
                indirect_md.append(fmt(c))
            indirect_md += ["```", ""]

    with (out_dir / "main_call_census.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["callsite_rva", "kind", "target", "op_str"])
        w.writeheader()
        w.writerows(rows)

    (out_dir / "main_indirect_calls.md").write_text("\n".join(indirect_md), encoding="utf-8")

    # Heuristic argv-flow report. We intentionally avoid claiming semantics; this only
    # highlights early moves from RCX/RDX/R8/R9 and loop-like memory accesses using
    # registers that receive them.
    argv_md = [
        "# PM62C_MAIN argument-flow candidates",
        "",
        "Windows x64 entry candidates: RCX/RDX/R8/R9. These are not assigned semantics until verified.",
        "",
        "## First 160 instructions",
        "",
        "```asm",
    ]
    for insn in insns[:160]:
        argv_md.append(fmt(insn))
    argv_md += ["```", "", "## Calls by kind", ""]
    counts = Counter(r["kind"] for r in rows)
    for k, v in sorted(counts.items()):
        argv_md.append(f"- {k}: {v}")
    argv_md += [
        "",
        "## Manual review targets",
        "",
        "1. Identify where RCX/RDX/R8 are copied into nonvolatile registers or stack locals.",
        "2. Find loops with scale-8 array reads from the register derived from argv.",
        "3. Inspect the first calls fed with an argv[i] pointer.",
        "4. Classify conversion helpers (strtol/atoi/custom numeric parse) and token discriminators.",
        "5. Do not promote a handler to VMR relevance without an option-dependent value flow.",
    ]
    (out_dir / "main_argv_candidates.md").write_text("\n".join(argv_md), encoding="utf-8")

    print(f"decoded instructions: {len(insns)}")
    print(f"calls: {len(rows)}")
    print("call kinds:", dict(counts))
    print(out_dir / "main_call_census.csv")
    print(out_dir / "main_indirect_calls.md")
    print(out_dir / "main_argv_candidates.md")


if __name__ == "__main__":
    main()
