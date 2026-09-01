#!/usr/bin/env python3
from pathlib import Path
import argparse, struct
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_OP_IMM

TARGET_RVA=0x001688B0
TEXT_BEGIN=0x1000; TEXT_END=0x420000

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('binary'); ap.add_argument('--out-dir',default='notes'); a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False); base=pe.OPTIONAL_HEADER.ImageBase; target=base+TARGET_RVA
 md=Cs(CS_ARCH_X86,CS_MODE_64); md.detail=True; md.skipdata=True
 text=list(md.disasm(pe.get_data(TEXT_BEGIN,TEXT_END-TEXT_BEGIN),base+TEXT_BEGIN))
 absrefs=[]
 needle=struct.pack('<Q',target)
 for sec in pe.sections:
  raw=sec.get_data(); name=sec.Name.rstrip(b'\0').decode('ascii','replace'); pos=0
  while True:
   off=raw.find(needle,pos)
   if off<0: break
   absrefs.append((name,sec.VirtualAddress+off,off%8)); pos=off+1
 direct=[]
 for idx,i in enumerate(text):
  if i.mnemonic not in ('call','jmp') or not i.operands: continue
  op=i.operands[0]
  if op.type==X86_OP_IMM and op.imm==target: direct.append(idx)
 lines=['# Parent mode wrapper 0x1688B0 reference trace','', 'This function loads `[this+0x888]` and tail-jumps to `0x16E0B0`, preserving RDX/R8/R9.','', '## Absolute qword refs','']
 if not absrefs: lines.append('- none')
 for n,r,a8 in absrefs: lines.append(f'- `{n}` RVA `0x{r:08X}` mod8={a8}')
 lines += ['','## Direct CALL/JMP refs','',f'count: `{len(direct)}`']
 for idx in direct:
  i=text[idx]; lines += ['',f'### `{i.mnemonic}` `0x{i.address-base:08X}`','', '```asm']
  for z in text[max(0,idx-24):min(len(text),idx+8)]: lines.append(f'0x{z.address-base:08X}: {z.mnemonic} {z.op_str}'.rstrip())
  lines += ['```']
 # For aligned absolute refs infer contiguous vtable and enumerate same-slot callsites.
 lo=base+TEXT_BEGIN; hi=base+TEXT_END
 for n,r,a8 in absrefs:
  if a8: continue
  sec=next(s for s in pe.sections if s.VirtualAddress<=r<s.VirtualAddress+s.Misc_VirtualSize)
  raw=sec.get_data(); local=r-sec.VirtualAddress; start=local
  for back in range(8,0x108,8):
   p=local-back
   if p<0: break
   q=struct.unpack_from('<Q',raw,p)[0]
   if not(lo<=q<hi): start=p+8; break
   start=p
  slot=local-start; vt=sec.VirtualAddress+start
  lines += ['',f'## Candidate vtable `0x{vt:08X}`, target slot `+0x{slot:X}`','']
  for p in range(start,min(len(raw)-7,start+0xB0),8):
   q=struct.unpack_from('<Q',raw,p)[0]
   if lo<=q<hi: lines.append(f'- `+0x{p-start:02X}` -> `0x{q-base:08X}`')
   else: break
  hits=[]
  for idx,i in enumerate(text):
   if i.mnemonic not in ('call','jmp') or not i.operands: continue
   op=i.operands[0]
   if op.type==X86_OP_MEM and op.mem.disp==slot and op.mem.base: hits.append(idx)
  lines += ['','### Same-slot indirect callsites','',f'count: `{len(hits)}`']
  for idx in hits:
   i=text[idx]; lines += ['',f'#### `{i.mnemonic}` `0x{i.address-base:08X}`','', '```asm']
   for z in text[max(0,idx-20):min(len(text),idx+6)]: lines.append(f'0x{z.address-base:08X}: {z.mnemonic} {z.op_str}'.rstrip())
   lines += ['```']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'nvidia_parent_mode_wrapper.md').write_text('\n'.join(lines),encoding='utf-8')
 print('abs',absrefs,'direct',[(hex(text[x].address-base),text[x].mnemonic) for x in direct])
if __name__=='__main__':main()
