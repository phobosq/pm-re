#!/usr/bin/env python3
from pathlib import Path
import argparse,bisect
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_OP_REG,X86_OP_IMM

TARGET=0x001CDCC0
WATCH={0x98:'mt',0xAC:'straps',0xB0:'vmr',0xB4:'vmt1?',0xB8:'vmt2',0xBC:'vmt3',0xC0:'cfg_c0'}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
    pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
    funcs=[]
    for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
        b=e.struct.BeginAddress;en=e.struct.EndAddress
        if b<en:funcs.append((b,en))
    funcs=sorted(set(funcs));starts=[b for b,_ in funcs]
    j=bisect.bisect_right(starts,TARGET)-1;b,en=funcs[j]
    md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
    arr=list(md.disasm(pe.get_data(b,en-b),base+b))
    aliases={'r9'};hits=[];calls=[]
    for idx,i in enumerate(arr):
        if i.mnemonic=='mov' and len(i.operands)==2 and i.operands[0].type==X86_OP_REG:
            dst=i.reg_name(i.operands[0].reg);src=i.operands[1]
            if src.type==X86_OP_REG and i.reg_name(src.reg) in aliases: aliases.add(dst)
            elif dst in aliases and dst!='r9': aliases.discard(dst)
        for op in i.operands:
            if op.type==X86_OP_MEM and op.mem.base and i.reg_name(op.mem.base) in aliases:
                hits.append((idx,i,op.mem.disp,WATCH.get(op.mem.disp,'')))
        if i.mnemonic=='call':
            op=i.operands[0];t=f'0x{op.imm-base:08X}' if op.type==X86_OP_IMM else i.op_str
            calls.append((i.address-base,t))
    lines=['# Type2 ctor config-record provenance','',f'PDATA `0x{b:08X}..0x{en:08X}`. Entry R9 is original 0xD8 config record.','',f'Aliases observed: `{", ".join(sorted(aliases))}`','',
           '## Config-pointer memory accesses','','| RVA | disp | label | instruction |','|---|---:|---|---|']
    for idx,i,d,l in hits: lines.append(f'| `0x{i.address-base:08X}` | `0x{d:X}` | `{l}` | `{i.mnemonic} {i.op_str}` |')
    lines += ['','## Calls','','| RVA | target |','|---|---|']
    for c,t in calls:lines.append(f'| `0x{c:08X}` | `{t}` |')
    lines += ['','## Full body','','```asm']
    for i in arr:lines.append(f'0x{i.address-base:08X}: {i.mnemonic} {i.op_str}'.rstrip())
    lines += ['```']
    out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'type2_ctor_config.md').write_text('\n'.join(lines),encoding='utf-8');print('hits',len(hits))
if __name__=='__main__':main()
