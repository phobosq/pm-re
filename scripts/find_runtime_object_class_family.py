#!/usr/bin/env python3
"""Find functions belonging to the runtime object that owns timing snapshots.

Confirmed type fingerprint:
  +0x318 lock/synchronization object
  +0x368 snapshot A (0xD8 bytes)
  +0x440 snapshot B (0xD8 bytes)
  +0x538 generation/ref counter
  +0x418 VMR inside snapshot A
  +0x4F0 VMR inside snapshot B

The scan rejects RSP/RBP based accesses to avoid stack-frame offset collisions.
Static only; target binary is never executed.
"""
from __future__ import annotations
import argparse, bisect
from collections import defaultdict
from pathlib import Path
import pefile
from capstone import Cs, CS_ARCH_X86, CS_MODE_64
from capstone.x86 import X86_OP_MEM, X86_OP_IMM, X86_REG_RSP, X86_REG_RBP, X86_REG_ESP, X86_REG_EBP

FINGERPRINT = {
    0x318: 'sync',
    0x368: 'snapshot_A',
    0x418: 'vmr_A',
    0x440: 'snapshot_B',
    0x4F0: 'vmr_B',
    0x538: 'counter',
}
STACK_BASES = {X86_REG_RSP, X86_REG_RBP, X86_REG_ESP, X86_REG_EBP}
SEEDS = {0x00084A60: 'snapshot_getter', 0x001362D0: 'snapshot_setter'}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('binary')
    ap.add_argument('--out-dir', default='notes')
    a = ap.parse_args()

    pe = pefile.PE(a.binary, fast_load=False)
    base = pe.OPTIONAL_HEADER.ImageBase
    text = next(s for s in pe.sections if s.Name.rstrip(b'\0') == b'.text')

    funcs = []
    for e in getattr(pe, 'DIRECTORY_ENTRY_EXCEPTION', []):
        b, en = e.struct.BeginAddress, e.struct.EndAddress
        if b < en:
            funcs.append((b, en))
    funcs.sort()
    starts = [b for b, _ in funcs]

    def fnof(rva):
        j = bisect.bisect_right(starts, rva) - 1
        if j >= 0 and funcs[j][0] <= rva < funcs[j][1]:
            return funcs[j]
        return None

    md = Cs(CS_ARCH_X86, CS_MODE_64)
    md.detail = True
    md.skipdata = True
    all_ins = [i for i in md.disasm(text.get_data(), base + text.VirtualAddress) if i.id]

    hits = defaultdict(list)
    calls = defaultdict(list)
    direct_callers = defaultdict(list)

    for ins in all_ins:
        rva = ins.address - base
        fn = fnof(rva)
        if not fn:
            continue
        for op in ins.operands:
            if op.type == X86_OP_MEM and op.mem.disp in FINGERPRINT and op.mem.base not in STACK_BASES:
                hits[fn].append((rva, op.mem.disp, ins.mnemonic, ins.op_str, op.mem.base, op.mem.index))
        if ins.mnemonic == 'call':
            target = None
            if ins.operands and ins.operands[0].type == X86_OP_IMM:
                target = ins.operands[0].imm - base
                direct_callers[target].append((fn, rva))
                calls[fn].append((rva, f'0x{target:08X}'))
            else:
                calls[fn].append((rva, ins.op_str))

    # Rank by number of distinct fingerprint fields. Seed functions are always included.
    ranked = []
    for fn, hs in hits.items():
        fields = {d for _, d, *_ in hs}
        score = len(fields)
        if score >= 2 or fn[0] in SEEDS:
            ranked.append((score, fn, hs))
    for seed in SEEDS:
        fn = fnof(seed)
        if fn and all(x[1] != fn for x in ranked):
            ranked.append((0, fn, hits.get(fn, [])))
    ranked.sort(key=lambda x: (-x[0], x[1][0]))

    lines = [
        '# Runtime object class-family scan', '',
        'Type fingerprint is derived from confirmed snapshot getter/setter methods.',
        'RSP/RBP-based accesses are excluded to suppress stack-offset collisions.', '',
        f'candidate functions: {len(ranked)}', '',
        '| score | PDATA | fields | direct calls | seed |',
        '|---:|---|---|---:|---|',
    ]

    for score, fn, hs in ranked:
        fields = sorted({d for _, d, *_ in hs})
        ftxt = ', '.join(f'{FINGERPRINT[d]}(+0x{d:X})' for d in fields) or '-'
        seed = SEEDS.get(fn[0], '')
        lines.append(f'| {score} | `0x{fn[0]:08X}..0x{fn[1]:08X}` | {ftxt} | {len(calls.get(fn, []))} | {seed} |')

    lines += ['', '## Candidate details', '']
    for score, fn, hs in ranked:
        lines += [f'### `0x{fn[0]:08X}..0x{fn[1]:08X}` score={score}', '']
        if fn[0] in SEEDS:
            lines.append(f'seed: **{SEEDS[fn[0]]}**')
            lines.append('')
        lines += ['Fingerprint accesses:', '']
        for rva, disp, mnem, ops, breg, ireg in hs:
            lines.append(f'- `0x{rva:08X}` {FINGERPRINT[disp]} `+0x{disp:X}`: `{mnem} {ops}`')
        lines += ['', 'Calls:', '']
        for rva, target in calls.get(fn, []):
            lines.append(f'- `0x{rva:08X}` -> `{target}`')
        lines.append('')

    lines += ['## Seed direct callers', '']
    for seed, name in SEEDS.items():
        lines += [f'### {name} `0x{seed:08X}`', '']
        for fn, rva in direct_callers.get(seed, []):
            lines.append(f'- `0x{rva:08X}` in `0x{fn[0]:08X}..0x{fn[1]:08X}`')
        lines.append('')

    out = Path(a.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    p = out / 'runtime_object_class_family.md'
    p.write_text('\n'.join(lines), encoding='utf-8')
    print(p)


if __name__ == '__main__':
    main()
