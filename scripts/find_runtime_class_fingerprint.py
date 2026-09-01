#!/usr/bin/env python3
"""Find functions structurally tied to the runtime GPU object class.

Anchors confirmed from type-safe getter/setter pair:
  +0x318 lock/state
  +0x368 snapshot A
  +0x440 snapshot B
  +0x538 generation/ref counter

Static only. Target binary is never executed.
"""
from __future__ import annotations
import argparse,bisect
from pathlib import Path
from collections import defaultdict
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_OP_IMM

OFFS={0x318:'lock',0x368:'snapshotA',0x440:'snapshotB',0x538:'counter'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('binary'); ap.add_argument('--out-dir',default='notes'); a=ap.parse_args()
    pe=pefile.PE(a.binary,fast_load=False); base=pe.OPTIONAL_HEADER.ImageBase
    text=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.text')
    funcs=[]
    for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
        b=e.struct.BeginAddress; en=e.struct.EndAddress
        if b<en: funcs.append((b,en))
    funcs.sort(); starts=[b for b,_ in funcs]
    def fnof(r):
        j=bisect.bisect_right(starts,r)-1
        return funcs[j] if j>=0 and funcs[j][0]<=r<funcs[j][1] else None
    md=Cs(CS_ARCH_X86,CS_MODE_64); md.detail=True; md.skipdata=True
    ins=[i for i in md.disasm(text.get_data(),base+text.VirtualAddress) if i.id!=0]
    byfn=defaultdict(list)
    for i in ins:
        fn=fnof(i.address-base)
        if fn: byfn[fn].append(i)
    ranked=[]
    for fn,arr in byfn.items():
        seen=set(); touches=[]; calls=[]; ripstores=[]
        for i in arr:
            for op in i.operands:
                if op.type==X86_OP_MEM and op.mem.disp in OFFS:
                    seen.add(op.mem.disp); touches.append((i,op.mem.disp))
            if i.mnemonic=='call':
                target=i.op_str
                if i.operands and i.operands[0].type==X86_OP_IMM:
                    target=f'RVA 0x{i.operands[0].imm-base:08X}'
                calls.append((i.address-base,target))
            # constructor/vtable-ish: lea reg,[rip+disp] followed shortly by mov [reg/base],reg is handled in context output
            if i.mnemonic=='lea' and 'rip +' in i.op_str:
                ripstores.append(i)
        if len(seen)>=2:
            ranked.append((len(seen),len(calls),fn,seen,touches,calls,ripstores))
    ranked.sort(key=lambda x:(-x[0],-x[1],x[2][0]))
    lines=['# Runtime class structural fingerprint','',
           'Anchors: `+0x318`, `+0x368`, `+0x440`, `+0x538`.','',
           '| PDATA | anchors | calls | anchor names |','|---|---:|---:|---|']
    for n,c,fn,seen,touches,calls,ripstores in ranked:
        names=', '.join(OFFS[o] for o in sorted(seen))
        lines.append(f'| `0x{fn[0]:08X}..0x{fn[1]:08X}` | {n} | {c} | {names} |')
    lines += ['','## Contexts','']
    for n,c,fn,seen,touches,calls,ripstores in ranked[:30]:
        arr=byfn[fn]
        idxs=[k for k,i in enumerate(arr) if any(op.type==X86_OP_MEM and op.mem.disp in seen for op in i.operands)]
        if not idxs: continue
        lo=max(0,min(idxs)-20); hi=min(len(arr),max(idxs)+35)
        lines += [f'### `0x{fn[0]:08X}..0x{fn[1]:08X}` — {", ".join(OFFS[o] for o in sorted(seen))}','','```asm']
        for i in arr[lo:hi]: lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
        lines += ['```','','Calls:']
        for r,t in calls[:24]: lines.append(f'- `0x{r:08X}` -> `{t}`')
        if ripstores:
            lines += ['','RIP-relative LEAs:']
            for i in ripstores[:16]: lines.append(f'- `0x{i.address-base:08X}: {i.mnemonic} {i.op_str}`')
        lines += ['']
    out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
    p=out/'runtime_class_fingerprint.md'; p.write_text('\n'.join(lines),encoding='utf-8')
    print('runtime_class_candidates',len(ranked))
if __name__=='__main__': main()
