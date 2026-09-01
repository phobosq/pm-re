#!/usr/bin/env python3
from pathlib import Path
import argparse, struct
import pefile

TABLE_RVA=0x004BD6D0
# scan until first long run of invalid/unexpected records; known entries are 0x18 bytes
MAX_RECORDS=64
DIVISOR_RVA=0x004386B8

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False)
 def get(rva,n): return pe.get_data(rva,n)
 divisor=struct.unpack('<d',get(DIVISOR_RVA,8))[0]
 lines=['# VMR profile table / divisor extraction','',f'- divisor RVA `0x{DIVISOR_RVA:08X}` as double: `{divisor!r}`',f'- table start RVA `0x{TABLE_RVA:08X}`', '', '| idx | RVA | family/key | type | +0x08 | +0x0C | +0x10 | +0x14 |','|---:|---:|---:|---:|---:|---:|---:|---:|']
 recs=[]
 for idx in range(MAX_RECORDS):
  rva=TABLE_RVA+idx*0x18; raw=get(rva,0x18)
  if len(raw)<0x18:break
  vals=struct.unpack('<6I',raw)
  key,typ,a8,ac,a10,a14=vals
  recs.append((idx,rva,*vals))
  lines.append(f'| {idx} | `0x{rva:08X}` | {key} | {typ} | {a8} | {ac} | {a10} | {a14} |')
  # stop if clearly zero padding after at least a few records
  if idx>8 and vals==(0,0,0,0,0,0):
   # include first zero and stop
   break
 lines += ['','## Type 8/9 pairs by family/key','']
 by={}
 for idx,rva,key,typ,a8,ac,a10,a14 in recs:
  if typ in (8,9):by.setdefault(key,{})[typ]=(idx,rva,a8,ac,a10,a14)
 for key,d in sorted(by.items()):
  lines.append(f'### key `{key}`')
  for typ in (8,9):
   if typ in d:
    idx,rva,a8,ac,a10,a14=d[typ]
    lines.append(f'- type {typ}: `+08={a8}, +0C={ac}, +10={a10}, +14={a14}` at `0x{rva:08X}`')
  if 8 in d and 9 in d:
   base=d[8][-1];target=d[9][-1]
   lines.append(f'- VMR field endpoints (+0x14): base `{base}`, target `{target}`, delta `{base-target}`')
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'vmr_profile_table.md').write_text('\n'.join(lines),encoding='utf-8')
 print('divisor',divisor,'records',len(recs),'keys',sorted(by))
if __name__=='__main__':main()
