#!/usr/bin/env python3
from pathlib import Path
import argparse
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64
from capstone.x86 import X86_OP_MEM
BEGIN=0x001D4A80;END=0x001F1000
PROFILE={0x08:'reg_9A0290_field',0x2C:'reg_9A0298_field',0x38:'reg_9A029C_field',0x44:'reg_9A02A0_field'}
CHILD={0x144:'profile_cache_base',0x260:'flag0',0x264:'flag1',0x268:'flag2',0x270:'state_idx',0x274:'max_idx',0x278:'retry',0x27C:'counter',0x398:'profile_valid_flags',0x3A0:'gpu_table_key'}
WRITES=('mov','movups','movaps','movsd','movdqa','xor','and','or','add','sub','inc','dec','xchg')
def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);base=pe.OPTIONAL_HEADER.ImageBase
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=True;md.skipdata=True
 arr=list(md.disasm(pe.get_data(BEGIN,END-BEGIN),base+BEGIN));hits=[]
 for k,i in enumerate(arr):
  if not i.mnemonic.startswith(WRITES):continue
  try:ops=i.operands
  except:continue
  if not ops or ops[0].type!=X86_OP_MEM:continue
  op=ops[0];bn=i.reg_name(op.mem.base) if op.mem.base else '';d=op.mem.disp
  lab=None
  if d in PROFILE:lab=PROFILE[d]
  if bn not in ('rsp','rbp','rip') and d in CHILD:lab=CHILD[d]
  if lab:hits.append((k,i,bn,d,lab))
 lines=['# Focused NVIDIA child profile/cache writers','',f'Range `0x{BEGIN:08X}..0x{END:08X}`',f'hits: `{len(hits)}`','', '| RVA | base | disp | label | instruction |','|---|---|---:|---|---|']
 for k,i,bn,d,lab in hits:lines.append(f'| `0x{i.address-base:08X}` | `{bn}` | `0x{d:X}` | {lab} | `{i.mnemonic} {i.op_str}` |')
 lines += ['','## Contexts','']
 for k,i,bn,d,lab in hits:
  lines += [f'### {lab} @ `0x{i.address-base:08X}`','','```asm']
  for w in arr[max(0,k-10):min(len(arr),k+14)]:lines.append(f'0x{w.address-base:08X}: {w.mnemonic} {w.op_str}'.rstrip())
  lines += ['```','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'nvidia_child_profile_writers_fast.md').write_text('\n'.join(lines),encoding='utf-8');print('hits',len(hits))
if __name__=='__main__':main()
