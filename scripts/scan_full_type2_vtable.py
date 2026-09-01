#!/usr/bin/env python3
from pathlib import Path
import argparse,bisect,struct
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_OP_REG,X86_OP_IMM

TYPE2_VT=0x004BD558
TYPE1_VT=0x0044B3D8
MAX_SLOTS=40
WATCH={0x368:'snapA_base',0x418:'vmrA',0x440:'snapB_base',0x4F0:'vmrB',0x838:'child'}

def readq(pe,rva):
    try:return struct.unpack('<Q',pe.get_data(rva,8))[0]
    except:return 0

def main():
    ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
    pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
    funcs=[]
    for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
        b=e.struct.BeginAddress;en=e.struct.EndAddress
        if b<en:funcs.append((b,en))
    funcs=sorted(set(funcs)); starts=[b for b,_ in funcs]
    md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
    slots=[]
    for n in range(MAX_SLOTS):
        va=readq(pe,TYPE2_VT+n*8); rva=va-base if base<=va<base+0x1000000 else None
        va1=readq(pe,TYPE1_VT+n*8); rva1=va1-base if base<=va1<base+0x1000000 else None
        if rva is None: break
        slots.append((n*8,rva,rva1,rva==rva1))
    lines=['# Full Type2 runtime vtable timing bridge scan','',f'Type2 vtable `0x{TYPE2_VT:08X}`; Type1 compare `0x{TYPE1_VT:08X}`.','',
           '| slot | Type2 RVA | Type1 RVA | class |','|---:|---:|---:|---|']
    for off,r,r1,same in slots: lines.append(f'| `+0x{off:X}` | `0x{r:08X}` | `{("0x%08X"%r1) if r1 is not None else "-"}` | {"shared" if same else "NVIDIA override"} |')
    for off,r,r1,same in slots:
        j=bisect.bisect_right(starts,r)-1
        if j<0: continue
        b,en=funcs[j]
        if not (b<=r<en): continue
        arr=list(md.disasm(pe.get_data(b,en-b),base+b))
        # Simple this aliases, initialized RCX. Propagate mov reg,alias only, drop on obvious overwrite.
        aliases={'rcx'}; hits=[]; calls=[]
        for idx,i in enumerate(arr):
            if i.mnemonic=='mov' and len(i.operands)==2 and i.operands[0].type==X86_OP_REG:
                dst=i.reg_name(i.operands[0].reg); src=i.operands[1]
                if src.type==X86_OP_REG and i.reg_name(src.reg) in aliases: aliases.add(dst)
                elif dst in aliases and not (src.type==X86_OP_REG and i.reg_name(src.reg) in aliases):
                    if dst!='rcx': aliases.discard(dst)
            for op in i.operands:
                if op.type==X86_OP_MEM and op.mem.base:
                    bn=i.reg_name(op.mem.base)
                    if bn in aliases and op.mem.disp in WATCH:
                        hits.append((idx,i,WATCH[op.mem.disp]))
            if i.mnemonic=='call':
                op=i.operands[0]
                target=f'0x{op.imm-base:08X}' if op.type==X86_OP_IMM else i.op_str
                calls.append((i.address-base,target))
        if not hits: continue
        lines += ['',f'## slot `+0x{off:X}` -> `0x{r:08X}` ({"shared" if same else "NVIDIA override"})','',f'PDATA `0x{b:08X}..0x{en:08X}`','', '### Hits','']
        for idx,i,label in hits:
            lines += [f'#### {label} at `0x{i.address-base:08X}`','','```asm']
            for z in arr[max(0,idx-10):min(len(arr),idx+13)]: lines.append(f'0x{z.address-base:08X}: {z.mnemonic} {z.op_str}'.rstrip())
            lines += ['```','']
        lines += ['### Calls','','| RVA | target |','|---|---|']
        for c,t in calls: lines.append(f'| `0x{c:08X}` | `{t}` |')
    out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True)
    (out/'full_type2_vtable_timing_scan.md').write_text('\n'.join(lines),encoding='utf-8');print('slots',len(slots))
if __name__=='__main__':main()
