#!/usr/bin/env python3
"""Recover stack-built GetProcAddress names in Type2 loader by static expression evaluation.
This does NOT execute target machine code; it evaluates a tiny whitelist of straight-line integer/string-building instructions.
"""
from __future__ import annotations
import argparse,re
from pathlib import Path
import pefile
from capstone import Cs,CS_ARCH_X86,CS_MODE_64

FN=(0x001D123E,0x001D353C)
SPECS=[
 (0x001D1E19,0x18,'slot_7E7840_name'),
 (0x001D2085,0x110,'slot_7E7848_name'),
 (0x001D24D3,0x168,'slot_7E7858_name'),
]

def canon_reg(r):
 r=r.lower()
 mp={'eax':('rax',32),'ax':('rax',16),'al':('rax',8),'ecx':('rcx',32),'cx':('rcx',16),'cl':('rcx',8),'edx':('rdx',32),'dx':('rdx',16),'dl':('rdx',8)}
 return mp.get(r,(r,64))
def getreg(regs,r):
 c,w=canon_reg(r);v=regs.get(c)
 if v is None:return None
 return v & ((1<<w)-1)
def setreg(regs,r,v):
 c,w=canon_reg(r)
 if v is None: regs[c]=None; return
 mask=(1<<w)-1;v &= mask
 old=regs.get(c,0) or 0
 if w==32:regs[c]=v
 elif w==64:regs[c]=v
 else:regs[c]=(old & ~mask)|v

def parse_mem(s):
 # only rbp +/- hex/decimal stack refs
 m=re.search(r'\[rbp(?:\s*([+-])\s*(0x[0-9a-f]+|\d+))?\]',s.lower())
 if not m:return None
 if not m.group(1):return 0
 n=int(m.group(2),0);return n if m.group(1)=='+' else -n
def mem_width(s):
 s=s.lower()
 if s.startswith('byte ptr'):return 1
 if s.startswith('word ptr'):return 2
 if s.startswith('dword ptr'):return 4
 if s.startswith('qword ptr'):return 8
 return None
def readmem(mem,off,w):
 vals=[mem.get(off+i) for i in range(w)]
 if any(v is None for v in vals):return None
 return sum(vals[i]<<(8*i) for i in range(w))
def writemem(mem,off,w,v):
 if v is None:
  for i in range(w):mem[off+i]=None
 else:
  for i in range(w):mem[off+i]=(v>>(8*i))&0xff

def eval_window(ins,target,base):
 # find nearest prior immediate dword write to base, use as start
 ti=next(i for i,x in enumerate(ins) if x.address==target)
 st=max(0,ti-260)
 pat=re.compile(rf'dword ptr \[rbp \+ 0x{base:x}\]',re.I)
 for j in range(ti-1,st-1,-1):
  if ins[j].mnemonic=='mov' and pat.search(ins[j].op_str) and ',' in ins[j].op_str:
   rhs=ins[j].op_str.split(',',1)[1].strip()
   try:int(rhs,0);st=j;break
   except:pass
 regs={};mem={};trace=[]
 for x in ins[st:ti+1]:
  m=x.mnemonic.lower(); ops=[z.strip() for z in x.op_str.split(',')]
  try:
   if m=='mov' and len(ops)==2:
    dst,src=ops; do=parse_mem(dst); so=parse_mem(src)
    if do is not None:
     w=mem_width(dst) or 8
     if so is not None:v=readmem(mem,so,mem_width(src) or w)
     elif re.fullmatch(r'-?0x[0-9a-f]+|-?\d+',src,re.I):v=int(src,0)
     else:v=getreg(regs,src)
     writemem(mem,do,w,v)
    else:
     if so is not None:v=readmem(mem,so,mem_width(src) or 4)
     elif re.fullmatch(r'-?0x[0-9a-f]+|-?\d+',src,re.I):v=int(src,0)
     else:v=getreg(regs,src)
     setreg(regs,dst,v)
   elif m in ('movsx','movzx') and len(ops)==2:
    dst,src=ops;so=parse_mem(src);v=None
    if so is not None:
     w=mem_width(src) or 1;v=readmem(mem,so,w)
     if v is not None and m=='movsx' and (v>>(w*8-1))&1:v-=1<<(w*8)
    else:v=getreg(regs,src)
    setreg(regs,dst,v)
   elif m in ('xor','add','sub') and len(ops)==2 and parse_mem(ops[0]) is None:
    dst,src=ops;v=getreg(regs,dst)
    try:s=int(src,0)
    except:s=getreg(regs,src)
    if v is not None and s is not None:
     if m=='xor':v^=s
     elif m=='add':v+=s
     else:v-=s
    else:v=None
    setreg(regs,dst,v)
   elif m in ('inc','dec') and len(ops)==1 and parse_mem(ops[0]) is None:
    v=getreg(regs,ops[0]);setreg(regs,ops[0],None if v is None else v+(1 if m=='inc' else -1))
  except Exception:pass
  trace.append(f'0x{x.address:016X}: {x.mnemonic} {x.op_str}')
 # collect bytes from base; first 4 often metadata/seed, show both raw and printable candidates at each offset
 raw=[]
 for o in range(base,base+96):
  v=mem.get(o)
  if v is None:break
  raw.append(v)
 def p(bs):return ''.join(chr(b) if 32<=b<127 else f'\\x{b:02x}' for b in bs)
 return st,raw,p(raw),p(raw[4:])

def main():
 ap=argparse.ArgumentParser();ap.add_argument('binary');ap.add_argument('--out-dir',default='notes');a=ap.parse_args()
 pe=pefile.PE(a.binary,fast_load=False);ib=pe.OPTIONAL_HEADER.ImageBase
 md=Cs(CS_ARCH_X86,CS_MODE_64);md.detail=False
 ins=list(md.disasm(pe.get_data(FN[0],FN[1]-FN[0]),ib+FN[0]))
 lines=['# Recovered Type2 GetProcAddress stack strings','', 'Static whitelist evaluation only; target code is not executed.','']
 for call_rva,base,label in SPECS:
  target=ib+call_rva;st,raw,full,skip4=eval_window(ins,target,base)
  lines += [f'## {label} before `0x{call_rva:08X}`','',f'stack base: `rbp+0x{base:X}`','',f'raw bytes: `{raw}`','',f'printable from base: `{full}`','',f'printable from base+4: `{skip4}`','']
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);p=out/'type2_getproc_strings.md';p.write_text('\n'.join(lines),encoding='utf-8');print(p)
if __name__=='__main__':main()
