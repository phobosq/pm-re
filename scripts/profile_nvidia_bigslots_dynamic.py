#!/usr/bin/env python3
from pathlib import Path
import argparse,bisect
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_REG_RIP

TARGETS=[0x001E8A10,0x001E2FE0,0x001E5160]

def ops(ins):
    if ins.mnemonic=='.byte': return []
    try: return ins.operands
    except Exception: return []

def disasm_fn(pe,md,base,fn):
    return list(md.disasm(pe.get_data(fn[0],fn[1]-fn[0]),base+fn[0]))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
    pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
    funcs=[]
    for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
        b=e.struct.BeginAddress;en=e.struct.EndAddress
        if b<en: funcs.append((b,en))
    funcs=sorted(set(funcs));starts=[b for b,_ in funcs]
    md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True

    lines=['# NVIDIA big-slot dynamic-call profile','','Scope: NVIDIA child vtable large methods only.','']
    dynslots={}
    for tgt in TARGETS:
        j=bisect.bisect_right(starts,tgt)-1;fn=funcs[j];arr=disasm_fn(pe,md,base,fn)
        lines += [f'## function `0x{fn[0]:08X}..0x{fn[1]:08X}`','', '| callsite | slot RVA | instruction |','|---|---|---|']
        for ins in arr:
            if ins.mnemonic!='call': continue
            o=ops(ins)
            if not o: continue
            op=o[0]
            if op.type==X86_OP_MEM and op.mem.base==X86_REG_RIP:
                slot=(ins.address+ins.size+op.mem.disp)-base
                dynslots.setdefault(slot,[]).append(ins.address-base)
                lines.append(f'| `0x{ins.address-base:08X}` | `0x{slot:08X}` | `{ins.mnemonic} {ins.op_str}` |')
        lines.append('')

    refs={slot:[] for slot in dynslots}
    # PDATA single pass: each function decoded once. Capture context locally.
    for fn in funcs:
        arr=disasm_fn(pe,md,base,fn)
        for i,ins in enumerate(arr):
            for op in ops(ins):
                if op.type!=X86_OP_MEM or op.mem.base!=X86_REG_RIP: continue
                ref=(ins.address+ins.size+op.mem.disp)-base
                if ref not in refs: continue
                ctx=[]
                for w in arr[max(0,i-12):min(len(arr),i+14)]:
                    ctx.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
                refs[ref].append((ins.address-base,fn,ctx))

    for slot,calls in sorted(dynslots.items()):
        lines += [f'## slot `0x{slot:08X}`','',f'used by: {", ".join(f"0x{x:08X}" for x in calls)}','',f'references: `{len(refs[slot])}`','']
        for rva,fn,ctx in refs[slot]:
            lines += [f'### ref `0x{rva:08X}` in `0x{fn[0]:08X}..0x{fn[1]:08X}`','','```asm',*ctx,'```','']

    out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True)
    p=out/'nvidia_bigslots_dynamic.md';p.write_text('\n'.join(lines),encoding='utf-8')
    print('slots',len(dynslots),'refs',sum(len(v) for v in refs.values()))

if __name__=='__main__': main()
