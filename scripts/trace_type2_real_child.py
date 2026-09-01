#!/usr/bin/env python3
from pathlib import Path
import argparse,bisect,struct
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_OP_REG,X86_OP_IMM
TYPE2_VT=0x004BD558
MAX_SLOTS=32

def readq(pe,rva):
    try:return struct.unpack('<Q',pe.get_data(rva,8))[0]
    except:return 0

def main():
    ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
    pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
    funcs=[]
    for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
        b=e.struct.BeginAddress;en=e.struct.EndAddress
        if b<en: funcs.append((b,en))
    funcs=sorted(set(funcs)); starts=[b for b,_ in funcs]
    md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
    methods=[]
    for n in range(MAX_SLOTS):
        va=readq(pe,TYPE2_VT+n*8)
        if not (base<=va<base+0x1000000):break
        methods.append((n*8,va-base))
    lines=['# Type2 real NVIDIA child (+0x840) trace','',
           'Constructor 0x1CDCC0 stores the object returned by 0x1D4A80 at `this+0x840`.','']
    total=0
    for voff,r in methods:
        j=bisect.bisect_right(starts,r)-1
        if j<0:continue
        b,en=funcs[j]
        if not(b<=r<en):continue
        arr=list(md.disasm(pe.get_data(b,en-b),base+b))
        this_alias={'rcx'}; child=set(); vptr=set(); events=[]
        for idx,i in enumerate(arr):
            # propagate this aliases
            if i.mnemonic=='mov' and len(i.operands)==2 and i.operands[0].type==X86_OP_REG:
                dst=i.reg_name(i.operands[0].reg); src=i.operands[1]
                if src.type==X86_OP_REG and i.reg_name(src.reg) in this_alias:this_alias.add(dst)
                # load real child
                if src.type==X86_OP_MEM and src.mem.base and i.reg_name(src.mem.base) in this_alias and src.mem.disp==0x840:
                    child.add(dst);events.append((idx,'load_child',i))
                elif src.type==X86_OP_REG and i.reg_name(src.reg) in child:
                    child.add(dst)
                # vptr = [child]
                if src.type==X86_OP_MEM and src.mem.base and i.reg_name(src.mem.base) in child and src.mem.disp==0:
                    vptr.add(dst);events.append((idx,'load_vptr',i))
                elif src.type==X86_OP_REG and i.reg_name(src.reg) in vptr:
                    vptr.add(dst)
            # direct memory refs this+840
            for op in i.operands:
                if op.type==X86_OP_MEM and op.mem.base and i.reg_name(op.mem.base) in this_alias and op.mem.disp==0x840:
                    if not any(ev[0]==idx for ev in events):events.append((idx,'ref_child_field',i))
            # virtual call through vptr
            if i.mnemonic=='call' and i.operands:
                op=i.operands[0]
                if op.type==X86_OP_MEM and op.mem.base and i.reg_name(op.mem.base) in vptr:
                    events.append((idx,f'virtual_call_slot_0x{op.mem.disp:X}',i))
                elif op.type==X86_OP_IMM:
                    # record direct calls when RCX currently child in preceding few insns heuristically
                    events.append((idx,f'direct_call_0x{op.imm-base:08X}',i))
        interesting=[e for e in events if e[1].startswith(('load_child','ref_child_field','virtual_call'))]
        if not interesting: continue
        total+=1
        lines += [f'## parent slot `+0x{voff:X}` -> `0x{r:08X}` PDATA `0x{b:08X}..0x{en:08X}`','']
        for idx,kind,i in interesting:
            lines += [f'### {kind} at `0x{i.address-base:08X}`','','```asm']
            for z in arr[max(0,idx-10):min(len(arr),idx+13)]:lines.append(f'0x{z.address-base:08X}: {z.mnemonic} {z.op_str}'.rstrip())
            lines += ['```','']
    lines.insert(4,f'Methods touching real child: `{total}`')
    out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'type2_real_child_trace.md').write_text('\n'.join(lines),encoding='utf-8');print('methods',total)
if __name__=='__main__':main()
