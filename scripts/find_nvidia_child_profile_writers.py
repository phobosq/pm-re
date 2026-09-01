#!/usr/bin/env python3
from pathlib import Path
import argparse
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_OP_REG

PROFILE_OFFSETS={0x08:'reg_9A0290_field',0x2C:'reg_9A0298_field',0x38:'reg_9A029C_field',0x44:'reg_9A02A0_field'}
CHILD_OFFSETS={0x144:'profile_cache_base',0x260:'flag0',0x264:'flag1',0x268:'flag2',0x270:'state_idx',0x274:'max_idx',0x278:'retry',0x27C:'counter',0x398:'profile_valid_flags',0x3A0:'gpu_table_key'}

def is_write(ins,op_index):
    if op_index!=0:return False
    return ins.mnemonic.startswith(('mov','lea','xor','and','or','add','sub','inc','dec','xchg'))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
    pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
    md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
    funcs=[]
    for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
        b=e.struct.BeginAddress;en=e.struct.EndAddress
        if b<en:funcs.append((b,en))
    funcs=sorted(set(funcs));hits=[]
    for fn in funcs:
        arr=list(md.disasm(pe.get_data(fn[0],fn[1]-fn[0]),base+fn[0]))
        local=[]
        for k,ins in enumerate(arr):
            for oi,op in enumerate(ins.operands):
                if op.type!=X86_OP_MEM or not op.mem.base:continue
                bn=ins.reg_name(op.mem.base);d=op.mem.disp
                label=None
                # profile field writes through arbitrary struct pointer; keep small offsets.
                if d in PROFILE_OFFSETS and is_write(ins,oi): label=PROFILE_OFFSETS[d]
                # child object state/cache writes; exclude stack/rip.
                if bn not in ('rsp','rbp','rip') and d in CHILD_OFFSETS and is_write(ins,oi): label=CHILD_OFFSETS[d]
                if label: local.append((k,ins,bn,d,label))
        if local:hits.append((fn,arr,local))
    lines=['# NVIDIA child strap profile/cache writers','',
           'Static candidate census. High-value anchors are 0x5C profile fields that feed RegisterOp and unique child state/cache offsets.','',
           f'functions with candidate writes: `{len(hits)}`','']
    for fn,arr,local in hits:
        labels=sorted(set(x[4] for x in local))
        lines += [f'## `0x{fn[0]:08X}..0x{fn[1]:08X}` — {", ".join(labels)}','',
                  '| RVA | base | disp | label | instruction |','|---|---|---:|---|---|']
        for k,i,bn,d,label in local:
            lines.append(f'| `0x{i.address-base:08X}` | `{bn}` | `0x{d:X}` | {label} | `{i.mnemonic} {i.op_str}` |')
        lines += ['','### Contexts','']
        for k,i,bn,d,label in local[:12]:
            lines += [f'#### {label} @ `0x{i.address-base:08X}`','','```asm']
            for w in arr[max(0,k-12):min(len(arr),k+18)]:lines.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
            lines += ['```','']
    out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'nvidia_child_profile_writers.md';p.write_text('\n'.join(lines),encoding='utf-8');print('functions',len(hits))
if __name__=='__main__':main()
