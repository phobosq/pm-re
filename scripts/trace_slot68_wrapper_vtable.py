#!/usr/bin/env python3
from pathlib import Path
import argparse, struct
import pefile
from capstone import Cs, CS_ARCH_X86, CS_MODE_64
from capstone.x86 import X86_OP_MEM, X86_OP_REG, X86_OP_IMM

WRAP_RVA=0x0016E0B0
TEXT_BEGIN=0x00001000
TEXT_END=0x00420000

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('binary'); ap.add_argument('--out-dir',default='notes'); a=ap.parse_args()
    pe=pefile.PE(a.binary,fast_load=False); base=pe.OPTIONAL_HEADER.ImageBase
    target=base+WRAP_RVA
    refs=[]
    for sec in pe.sections:
        name=sec.Name.rstrip(b'\0').decode('ascii','replace')
        raw=sec.get_data(); va=sec.VirtualAddress
        # Bytewise absolute-pointer scan: do not assume vtable alignment.
        needle=struct.pack('<Q',target); pos=0
        while True:
            off=raw.find(needle,pos)
            if off<0: break
            refs.append((name,va+off,off%8)); pos=off+1
    md=Cs(CS_ARCH_X86,CS_MODE_64); md.detail=True; md.skipdata=True
    text=list(md.disasm(pe.get_data(TEXT_BEGIN,TEXT_END-TEXT_BEGIN),base+TEXT_BEGIN))
    direct=[]
    for idx,i in enumerate(text):
        if i.mnemonic not in ('call','jmp') or not i.operands: continue
        op=i.operands[0]
        if op.type==X86_OP_IMM and op.imm==target: direct.append(idx)
    lines=['# NVIDIA mode-setter wrapper reference trace','',f'Wrapper `0x{WRAP_RVA:08X}` tail-calls child slot +0x68.','', '## Absolute qword references (bytewise scan)','']
    if not refs: lines.append('- none')
    for name,rva,align in refs: lines.append(f'- `{name}` RVA `0x{rva:08X}` (offset mod8={align})')
    lines += ['','## Direct CALL/JMP rel32 references','',f'count: `{len(direct)}`']
    for idx in direct:
        i=text[idx]; lines += ['',f'### `{i.mnemonic}` `0x{i.address-base:08X}`','', '```asm']
        for z in text[max(0,idx-18):min(len(text),idx+6)]: lines.append(f'0x{z.address-base:08X}: {z.mnemonic} {z.op_str}'.rstrip())
        lines += ['```']
    text_lo=base+TEXT_BEGIN; text_hi=base+TEXT_END
    for name,rva,align in refs:
        if align: continue
        sec=next(s for s in pe.sections if s.VirtualAddress <= rva < s.VirtualAddress+s.Misc_VirtualSize)
        raw=sec.get_data(); local=rva-sec.VirtualAddress
        start=local
        for back in range(8,0x108,8):
            p=local-back
            if p<0: break
            q=struct.unpack_from('<Q',raw,p)[0]
            if not (text_lo <= q < text_hi): start=p+8; break
            start=p
        slot=local-start; vt_rva=sec.VirtualAddress+start
        lines += ['',f'## Candidate vtable at `0x{vt_rva:08X}`; wrapper slot `+0x{slot:X}`','']
        for p in range(start,min(len(raw)-7,start+0xB0),8):
            q=struct.unpack_from('<Q',raw,p)[0]
            if text_lo <= q < text_hi: lines.append(f'- `+0x{p-start:02X}` -> `0x{q-base:08X}`')
            else: break
        hits=[]
        for idx,i in enumerate(text):
            if i.mnemonic not in ('call','jmp') or not i.operands: continue
            op=i.operands[0]
            if op.type==X86_OP_MEM and op.mem.disp==slot and op.mem.base: hits.append(idx)
        lines += ['','### Text callsites with same slot displacement','',f'count: `{len(hits)}`']
        for idx in hits:
            i=text[idx]; lines += ['',f'#### `{i.mnemonic}` `0x{i.address-base:08X}`','', '```asm']
            for z in text[max(0,idx-14):min(len(text),idx+5)]: lines.append(f'0x{z.address-base:08X}: {z.mnemonic} {z.op_str}'.rstrip())
            lines += ['```']
    out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
    (out/'nvidia_slot68_wrapper_vtable.md').write_text('\n'.join(lines),encoding='utf-8')
    print('abs refs',refs,'direct',[(hex(text[x].address-base),text[x].mnemonic) for x in direct])

if __name__=='__main__': main()
