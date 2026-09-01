#!/usr/bin/env python3
from pathlib import Path
import argparse, struct
import pefile
from capstone import Cs, CS_ARCH_X86, CS_MODE_64
from capstone.x86 import X86_OP_IMM

TARGET=0x001D78B0
WINDOW_BEFORE=0x100
WINDOW_AFTER=0x120

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('binary'); ap.add_argument('--out-dir',default='notes'); a=ap.parse_args()
    pe=pefile.PE(a.binary,fast_load=False); base=pe.OPTIONAL_HEADER.ImageBase
    md=Cs(CS_ARCH_X86,CS_MODE_64); md.detail=True
    # exact window around helper; enough to reveal prolog/ret and source-pointer setup
    b=TARGET-WINDOW_BEFORE; e=TARGET+WINDOW_AFTER
    arr=list(md.disasm(pe.get_data(b,e-b),base+b))
    lines=['# NVIDIA profile source helper around 0x1D78B0','', '## Disassembly','','```asm']
    for i in arr:
        lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
    lines += ['```','','## Direct callers of code RVAs in 0x1D78B0..0x1D7930','']
    # raw E8 rel32 scan is robust against skipdata
    text=None
    for s in pe.sections:
        name=s.Name.rstrip(b'\0')
        if name==b'.text':
            text=(s.VirtualAddress, bytes(s.get_data())); break
    if text:
        va,data=text
        hits=[]
        for off in range(0,len(data)-5):
            if data[off]!=0xE8: continue
            rel=struct.unpack_from('<i',data,off+1)[0]
            call_rva=va+off
            tgt=call_rva+5+rel
            if 0x001D78B0 <= tgt < 0x001D7930:
                hits.append((call_rva,tgt))
        for c,t in hits:
            lines.append(f'- call `0x{c:08X}` -> `0x{t:08X}`')
            cb=max(va,c-0x80); ce=min(va+len(data),c+0x40)
            ctx=list(md.disasm(pe.get_data(cb,ce-cb),base+cb))
            lines += ['','```asm']
            for i in ctx: lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
            lines += ['```','']
    out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
    (out/'nvidia_profile_source.md').write_text('\n'.join(lines),encoding='utf-8')
    print('done')
if __name__=='__main__': main()
