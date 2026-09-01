#!/usr/bin/env python3
from pathlib import Path
import argparse,bisect
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_REG_RIP,X86_OP_IMM,X86_OP_REG

SLOT=0x007E7B08

def main():
    ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
    pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
    funcs=[]
    for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
        b=e.struct.BeginAddress;en=e.struct.EndAddress
        if b<en: funcs.append((b,en))
    funcs=sorted(set(funcs));starts=[b for b,_ in funcs]
    md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
    hits=[]
    decoded={}
    for fn in funcs:
        arr=list(md.disasm(pe.get_data(fn[0],fn[1]-fn[0]),base+fn[0]));decoded[fn]=arr
        for i,ins in enumerate(arr):
            try: ops=ins.operands
            except Exception: continue
            for op in ops:
                if op.type==X86_OP_MEM and op.mem.base==X86_REG_RIP:
                    ref=(ins.address+ins.size+op.mem.disp)-base
                    if ref==SLOT:
                        hits.append((fn,i,ins))
    # direct callers for hit-containing functions
    target_fns={fn[0] for fn,_,_ in hits}
    callers={t:[] for t in target_fns}
    for fn,arr in decoded.items():
        for ins in arr:
            if ins.mnemonic!='call' or not ins.operands: continue
            op=ins.operands[0]
            if op.type==X86_OP_IMM:
                tgt=op.imm-base
                if tgt in callers: callers[tgt].append((ins.address-base,fn))
    lines=['# NvAPI_GPU_RegisterOp (0x2EB3C140) usage in PhoenixMiner 6.2c','',
           f'Global function slot: `0x{SLOT:08X}`.','',f'References found: `{len(hits)}`.','']
    for n,(fn,i,ins) in enumerate(hits,1):
        arr=decoded[fn];rva=ins.address-base
        lines += [f'## hit {n}: `0x{rva:08X}` in `0x{fn[0]:08X}..0x{fn[1]:08X}`','',
                  f'Instruction: `{ins.mnemonic} {ins.op_str}`','',
                  '### Direct callers of containing function','']
        cs=callers.get(fn[0],[])
        if cs:
            for cr,cf in cs: lines.append(f'- `0x{cr:08X}` from `0x{cf[0]:08X}..0x{cf[1]:08X}`')
        else: lines.append('- none')
        lines += ['','### Context','','```asm']
        for w in arr[max(0,i-60):min(len(arr),i+80)]:
            lines.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
        lines += ['```','','### Last argument-register writes before call/reference','']
        for reg in ('rcx','rdx','r8','r9'):
            found=[]
            for w in arr[max(0,i-30):i]:
                if w.mnemonic in ('mov','lea','xor') and w.operands and w.operands[0].type==X86_OP_REG and w.reg_name(w.operands[0].reg)==reg:
                    found.append(w)
            if found:
                w=found[-1];lines.append(f'- `{reg}`: `0x{w.address-base:08X}: {w.mnemonic} {w.op_str}`')
            else: lines.append(f'- `{reg}`: no local write in last 30 instructions')
        lines.append('')
    out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'nvapi_registerop_usage.md';p.write_text('\n'.join(lines),encoding='utf-8')
    print('registerop_refs',len(hits),'containing_functions',len(target_fns))

if __name__=='__main__': main()
