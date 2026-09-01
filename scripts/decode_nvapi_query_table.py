#!/usr/bin/env python3
from pathlib import Path
import argparse,bisect
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_IMM,X86_OP_MEM,X86_OP_REG,X86_REG_RIP

TARGET=0x001FE160

def main():
    ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
    pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
    funcs=[]
    for e in getattr(pe,'DIRECTORY_ENTRY_EXCEPTION',[]):
        b=e.struct.BeginAddress;en=e.struct.EndAddress
        if b<en: funcs.append((b,en))
    funcs.sort();starts=[b for b,_ in funcs]
    j=bisect.bisect_right(starts,TARGET)-1;fn=funcs[j]
    md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True
    arr=list(md.disasm(pe.get_data(fn[0],fn[1]-fn[0]),base+fn[0]))

    current_id=None
    awaiting=None   # (query_call_rva, interface_id)
    resolved=[]
    for ins in arr:
        # Store of the previous query result may occur after ECX is already loaded
        # with the next interface id, so consume awaiting before changing its ID.
        if ins.mnemonic=='mov' and len(ins.operands)==2:
            d,s=ins.operands
            if d.type==X86_OP_MEM and d.mem.base==X86_REG_RIP and s.type==X86_OP_REG and ins.reg_name(s.reg)=='rax' and awaiting:
                call_rva,call_id=awaiting
                slot=(ins.address+ins.size+d.mem.disp)-base
                resolved.append((call_rva,call_id,slot,ins.address-base))
                awaiting=None
            if d.type==X86_OP_REG and ins.reg_name(d.reg)=='ecx' and s.type==X86_OP_IMM:
                current_id=s.imm & 0xffffffff

        if ins.mnemonic=='call' and current_id is not None:
            # In this loader the resolver is an indirect RIP call and each result
            # is stored to a global slot before the following query returns.
            o=ins.operands[0] if ins.operands else None
            if o is not None and o.type==X86_OP_MEM and o.mem.base==X86_REG_RIP:
                awaiting=(ins.address-base,current_id)
                current_id=None

    lines=['# PhoenixMiner 6.2c NVAPI QueryInterface table','',f'Loader PDATA `0x{fn[0]:08X}..0x{fn[1]:08X}`','',
           '| query call | interface ID | slot RVA | store RVA |','|---|---|---|---|']
    for call,idv,slot,store in resolved:
        lines.append(f'| `0x{call:08X}` | `0x{idv:08X}` | `0x{slot:08X}` | `0x{store:08X}` |')
    ids={x[1] for x in resolved}
    lines += ['','## High-value known private IDs presence','',
              f'- `NvAPI_GPU_GetRamConfigStrap 0x51CCDB2A`: {"PRESENT" if 0x51CCDB2A in ids else "absent"}',
              f'- `NvAPI_GPU_GetAllClocks 0x1BD69F49`: {"PRESENT" if 0x1BD69F49 in ids else "absent"}',
              f'- `NvAPI_GPU_SetClocks 0x6F151055`: {"PRESENT" if 0x6F151055 in ids else "absent"}',
              f'- `NvAPI_GPU_GetPStates20 0x6FF81213`: {"PRESENT" if 0x6FF81213 in ids else "absent"}',
              f'- `NvAPI_GPU_SetPStates20 0x0F4DAE6B`: {"PRESENT" if 0x0F4DAE6B in ids else "absent"}',
              '']
    out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'nvapi_query_table.md';p.write_text('\n'.join(lines),encoding='utf-8')
    print('entries',len(resolved))

if __name__=='__main__':main()
