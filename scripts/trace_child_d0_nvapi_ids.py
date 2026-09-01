#!/usr/bin/env python3
from pathlib import Path
import argparse
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM,X86_OP_REG,X86_OP_IMM,X86_REG_RIP

BEGIN=0x001D4A80; END=0x001F1000
TEXT_BEGIN=0x00001000; TEXT_END=0x00420000

def rip_target(i,op,base): return i.address+i.size+op.mem.disp-base

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('binary'); ap.add_argument('--out-dir',default='notes'); a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False); base=pe.OPTIONAL_HEADER.ImageBase
 md=Cs(CS_ARCH_X86,CS_MODE_64); md.detail=True; md.skipdata=True
 child=list(md.disasm(pe.get_data(BEGIN,END-BEGIN),base+BEGIN))
 text=list(md.disasm(pe.get_data(TEXT_BEGIN,TEXT_END-TEXT_BEGIN),base+TEXT_BEGIN))
 lines=['# NVIDIA child +0xD0 NvAPI function provenance','', 'Find calls whose RCX is loaded from child `+0xD0`, then resolve RIP-global function slots and their initialization sites.','']
 calls=[]
 for idx,i in enumerate(child):
  if i.mnemonic!='call' or not i.operands: continue
  # nearest RCX load [reg+0xd0]
  rcx_idx=None
  for j in range(idx-1,max(-1,idx-20),-1):
   z=child[j]
   if z.mnemonic=='mov' and len(z.operands)>=2 and z.operands[0].type==X86_OP_REG and z.reg_name(z.operands[0].reg)=='rcx':
    s=z.operands[1]
    if s.type==X86_OP_MEM and s.mem.disp==0xd0:
     rcx_idx=j
    break
  if rcx_idx is None: continue
  slot=None
  op=i.operands[0]
  if op.type==X86_OP_MEM and op.mem.base==X86_REG_RIP: slot=rip_target(i,op,base)
  elif op.type==X86_OP_REG:
   rn=i.reg_name(op.reg)
   for j in range(idx-1,max(-1,idx-12),-1):
    z=child[j]
    if z.mnemonic=='mov' and len(z.operands)>=2 and z.operands[0].type==X86_OP_REG and z.reg_name(z.operands[0].reg)==rn:
     s=z.operands[1]
     if s.type==X86_OP_MEM and s.mem.base==X86_REG_RIP: slot=rip_target(z,s,base)
     break
  calls.append((idx,i,slot,rcx_idx))
 lines.append(f'calls: `{len(calls)}`')
 for idx,i,slot,rcx_idx in calls:
  lines += ['',f'## call `0x{i.address-base:08X}` function slot `{("0x%08X"%slot) if slot is not None else "unknown"}`','', '```asm']
  for z in child[max(0,rcx_idx-4):min(len(child),idx+4)]: lines.append(f'0x{z.address-base:08X}: {z.mnemonic} {z.op_str}'.rstrip())
  lines += ['```']
  if slot is None: continue
  refs=[]
  for k,z in enumerate(text):
   for op2 in z.operands if z.id else []:
    if op2.type==X86_OP_MEM and op2.mem.base==X86_REG_RIP and rip_target(z,op2,base)==slot:
     refs.append(k); break
  lines += ['',f'### refs to global slot `0x{slot:08X}`: `{len(refs)}`']
  for k in refs:
   z=text[k]
   lines += ['',f'#### ref `0x{z.address-base:08X}`','', '```asm']
   for q in text[max(0,k-18):min(len(text),k+8)]: lines.append(f'0x{q.address-base:08X}: {q.mnemonic} {q.op_str}'.rstrip())
   lines += ['```']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'nvidia_child_d0_nvapi_ids.md').write_text('\n'.join(lines),encoding='utf-8')
 print('calls',len(calls),[(hex(i.address-base),hex(s) if s else None) for _,i,s,_ in calls])
if __name__=='__main__':main()
