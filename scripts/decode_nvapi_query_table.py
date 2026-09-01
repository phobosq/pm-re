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
    # Resolver pattern: mov ecx, ID; call query; later mov [rip+slot], rax.
    # Track last immediate loaded into ECX before an indirect call, then map following RAX store.
    pending_id=None; pending_call=None; resolved=[]
    for ins in arr:
        if ins.mnemonic=='mov' and len(ins.operands)==2:
            d,s=ins.operands
            if d.type==X86_OP_REG and ins.reg_name(d.reg)=='ecx' and s.type==X86_OP_IMM:
                pending_id=s.imm & 0xffffffff
            elif d.type==X86_OP_MEM and d.mem.base==X86_REG_RIP and s.type==X86_OP_REG and ins.reg_name(s.reg)=='rax':
                if pending_call is not None:
                    slot=(ins.address+ins.size+d.mem.disp)-base
                    resolved.append((pending_call,pending_id,slot,ins.address-base))
                    pending_call=None
        if ins.mnemonic=='call' and pending_id is not None:
            pending_call=ins.address-base
            # Keep ID until corresponding store; next mov ecx may arrive before store in this binary,
            # so save it separately on call.
            call_id=pending_id
            pending_call=(pending_call,call_id)
        if pending_call is not None and isinstance(pending_call,tuple) and ins.mnemonic=='mov' and len(ins.operands)==2:
            d,s=ins.operands
            if d.type==X86_OP_MEM and d.mem.base==X86_REG_RIP and s.type==X86_OP_REG and ins.reg_name(s.reg)=='rax':
                call_rva,call_id=pending_call
                slot=(ins.address+ins.size+d.mem.disp)-base
                resolved.append((call_rva,call_id,slot,ins.address-base))
                pending_call=None
    # Dedup in case generic branch above ever matched.
    uniq=[];seen=set()
    for row in resolved:
        key=(row[0],row[1],row[2])
        if key not in seen: seen.add(key);uniq.append(row)
    lines=['# PhoenixMiner 6.2c NVAPI QueryInterface table','',f'Loader PDATA `0x{fn[0]:08X}..0x{fn[1]:08X}`','',
           '| query call | interface ID | slot RVA | store RVA |','|---|---|---|---|']
    for call,idv,slot,store in uniq:
        lines.append(f'| `0x{call:08X}` | `0x{idv:08X}` | `0x{slot:08X}` | `0x{store:08X}` |')
    ids={x[1] for x in uniq}
    lines += ['','## High-value known private IDs presence','',
              f'- `NvAPI_GPU_GetRamConfigStrap 0x51CCDB2A`: {"PRESENT" if 0x51CCDB2A in ids else "absent"}',
              f'- `NvAPI_GPU_GetAllClocks 0x1BD69F49`: {"PRESENT" if 0x1BD69F49 in ids else "absent"}',
              f'- `NvAPI_GPU_SetClocks 0x6F151055`: {"PRESENT" if 0x6F151055 in ids else "absent"}',
              f'- `NvAPI_GPU_GetPStates20 0x6FF81213`: {"PRESENT" if 0x6FF81213 in ids else "absent"}',
              f'- `NvAPI_GPU_SetPStates20 0x0F4DAE6B`: {"PRESENT" if 0x0F4DAE6B in ids else "absent"}',
              '']
    out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'nvapi_query_table.md';p.write_text('\n'.join(lines),encoding='utf-8')
    print('entries',len(uniq))

if __name__=='__main__':main()
