#!/usr/bin/env python3
from pathlib import Path
import argparse, struct
import pefile

MAP_RVA=0x004BD620
TABLE_RVA=0x004BD6D0
PROFILE_RECORDS=16
DIVISOR_RVA=0x004386B8

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False)
 def get(rva,n): return pe.get_data(rva,n)
 divisor=struct.unpack('<d',get(DIVISOR_RVA,8))[0]
 lines=['# VMR profile table / divisor extraction','',f'- divisor RVA `0x{DIVISOR_RVA:08X}` as double: `{divisor!r}`',f'- family map RVA `0x{MAP_RVA:08X}..0x{TABLE_RVA:08X}`',f'- profile table RVA `0x{TABLE_RVA:08X}`; records: `{PROFILE_RECORDS}`','','## Family map used by child+0x39C -> child+0x3A0','','| idx | RVA | input key | family |','|---:|---:|---:|---:|']
 map_recs=[]
 for idx,rva in enumerate(range(MAP_RVA,TABLE_RVA,8)):
  key,fam=struct.unpack('<II',get(rva,8));map_recs.append((key,fam));lines.append(f'| {idx} | `0x{rva:08X}` | `{key}` (`0x{key:X}`) | `{fam}` |')
 lines += ['','## Profile records','', '| idx | RVA | family | type | +0x08 | +0x0C | +0x10 | +0x14 |','|---:|---:|---:|---:|---:|---:|---:|---:|']
 recs=[]
 for idx in range(PROFILE_RECORDS):
  rva=TABLE_RVA+idx*0x18; key,typ,a8,ac,a10,a14=struct.unpack('<6I',get(rva,0x18));recs.append((idx,rva,key,typ,a8,ac,a10,a14));lines.append(f'| {idx} | `0x{rva:08X}` | {key} | {typ} | {a8} | {ac} | {a10} | {a14} |')
 lines += ['','## Type 8/9 VMR endpoints','']
 by={}
 for idx,rva,key,typ,a8,ac,a10,a14 in recs:
  if typ in (8,9):by.setdefault(key,{})[typ]=(idx,rva,a8,ac,a10,a14)
 for key,d in sorted(by.items()):
  lines.append(f'### family `{key}`')
  for typ in (8,9):
   idx,rva,a8,ac,a10,a14=d[typ]; lines.append(f'- type {typ}: `+08={a8}, +0C={ac}, +10={a10}, +14={a14}` at `0x{rva:08X}`')
  base=d[8][-1];target=d[9][-1]
  lines.append(f'- VMR field endpoints (+0x14): base `{base}`, target `{target}`, delta `{base-target}`')
  lines.append(f'- no-cache formula: `trunc({base} - ({base}-{target}) * vmr / {divisor:g})`')
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);(out/'vmr_profile_table.md').write_text('\n'.join(lines),encoding='utf-8')
 print('divisor',divisor,'map',map_recs,'endpoints',{k:(v[8][-1],v[9][-1]) for k,v in by.items()})
if __name__=='__main__':main()
