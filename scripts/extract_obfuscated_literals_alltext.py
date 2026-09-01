#!/usr/bin/env python3
"""Scan all executable .text for compiler-obfuscated ASCII literal builders.
Static only; never executes the target binary.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import pefile
from capstone import Cs, CS_ARCH_X86, CS_MODE_64
from capstone.x86 import X86_OP_IMM

NEEDLES=('vmr','vmt1','vmt2','vmt3','vmt','straps','rxboost','nvmem','vmdag','leavemt','-mt')

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('binary'); ap.add_argument('--out-dir',default='notes'); a=ap.parse_args()
    out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
    pe=pefile.PE(a.binary,fast_load=False); base=pe.OPTIONAL_HEADER.ImageBase
    text=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.text')
    begin=text.VirtualAddress; raw=text.get_data()
    md=Cs(CS_ARCH_X86,CS_MODE_64); md.detail=True; md.skipdata=True
    ins=list(md.disasm(raw,base+begin))
    xs=[]
    for idx,i in enumerate(ins):
        if i.mnemonic=='xor' and len(i.operands)==2 and i.operands[1].type==X86_OP_IMM:
            v=i.operands[1].imm & 0xff
            if 0x20<=v<=0x7e: xs.append((idx,i.address-base,v))
    groups=[]; cur=[]
    for x in xs:
        if cur and x[0]-cur[-1][0] > 12:
            groups.append(cur); cur=[]
        cur.append(x)
    if cur: groups.append(cur)
    rows=[]
    for g in groups:
        s=''.join(chr(x[2]) for x in g)
        candidates=[s, s[1:] if len(s)>1 else s]
        for cand in dict.fromkeys(candidates):
            low=cand.lower()
            if any(n in low for n in NEEDLES):
                rows.append((g[0][1],g[-1][1],cand,'timing'))
        for cand in dict.fromkeys(candidates):
            if cand.startswith('-') and 2<=len(cand)<=40 and all(0x20<=ord(c)<=0x7e for c in cand):
                rows.append((g[0][1],g[-1][1],cand,'cli'))
    seen=set(); uniq=[]
    for r in rows:
        k=(r[0],r[2],r[3])
        if k not in seen: seen.add(k); uniq.append(r)
    lines=['# All-.text recovered option literals','',f'.text RVA: `0x{begin:08X}`; decoded instructions: {len(ins)}; skipdata: enabled','',
           '| begin RVA | end RVA | class | literal |','|---|---|---|---|']
    for b,e,s,k in uniq:
        lines.append(f'| `0x{b:08X}` | `0x{e:08X}` | {k} | `{s.replace("|","\\|")}` |')
    lines += ['','## Timing hits','']
    hits=[r for r in uniq if r[3]=='timing']
    if hits:
        for b,e,s,k in hits: lines.append(f'- `0x{b:08X}`..`0x{e:08X}` → `{s}`')
    else: lines.append('- none')
    (out/'alltext_recovered_options.md').write_text('\n'.join(lines),encoding='utf-8')
    print('groups',len(groups),'retained',len(uniq),'timing',len(hits))

if __name__=='__main__': main()
