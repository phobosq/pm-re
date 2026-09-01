#!/usr/bin/env python3
from pathlib import Path
import argparse
import pefile
from capstone import Cs, CS_ARCH_X86, CS_MODE_64, CS_AC_WRITE
from capstone.x86 import X86_OP_MEM

BEGIN=0x001D4A80
END=0x001F1000
OFFSETS={0x14C:'ovr_14c',0x170:'ovr_170',0x17C:'ovr_17c',0x188:'ovr_188'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('binary'); ap.add_argument('--out-dir',default='notes'); a=ap.parse_args()
    pe=pefile.PE(a.binary,fast_load=False); base=pe.OPTIONAL_HEADER.ImageBase
    md=Cs(CS_ARCH_X86,CS_MODE_64); md.detail=True; md.skipdata=True
    arr=list(md.disasm(pe.get_data(BEGIN,END-BEGIN),base+BEGIN))
    hits=[]
    for idx,i in enumerate(arr):
        if i.id==0: continue
        for op in i.operands:
            if op.type!=X86_OP_MEM or op.mem.disp not in OFFSETS: continue
            # Capstone per-op access is available on normal decoded instructions.
            access='write' if (getattr(op,'access',0)&CS_AC_WRITE) else 'read'
            hits.append((idx,i,op,access))
    lines=['# NVIDIA profile override fields','','Offsets: `+0x14C/+0x170/+0x17C/+0x188` in NVIDIA child region.','',
           '| RVA | kind | base/index | field | instruction |','|---|---|---|---|---|']
    for idx,i,op,access in hits:
        m=op.mem; b=i.reg_name(m.base) if m.base else ''; x=i.reg_name(m.index) if m.index else ''
        lines.append(f'| `0x{i.address-base:08X}` | {access} | `{b}+{x}*{m.scale}` | `{OFFSETS[m.disp]}` | `{i.mnemonic} {i.op_str}` |')
    lines += ['','## Contexts','']
    for idx,i,op,access in hits:
        lines += [f'### `{access}` {OFFSETS[op.mem.disp]} at `0x{i.address-base:08X}`','','```asm']
        for z in arr[max(0,idx-12):min(len(arr),idx+14)]:
            lines.append(f'0x{z.address-base:08X}: {z.mnemonic} {z.op_str}'.rstrip())
        lines += ['```','']
    out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
    (out/'nvidia_profile_overrides.md').write_text('\n'.join(lines),encoding='utf-8')
    print('hits',len(hits))
if __name__=='__main__': main()
