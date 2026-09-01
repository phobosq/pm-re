# Runtime container hotspot decode

## PDATA `0x00074AB0..0x00079CAC`

### Calls and timing-shaped accesses

| RVA | kind | instruction |
|---|---|---|
| `0x00074AC9` | call | `direct 0x003B2500` |
| `0x00074B0D` | mt | `mov qword ptr [rsp + 0x98], rax` |
| `0x00074B36` | call | `direct 0x00062D20` |
| `0x00074B43` | call | `indirect qword ptr [rip + 0x3bb747]` |
| `0x00074B54` | call | `direct 0x002216B0` |
| `0x0007506C` | call | `direct 0x000862B0` |
| `0x000751DE` | call | `direct 0x00036AD0` |
| `0x00075222` | call | `direct 0x0006F540` |
| `0x00075263` | call | `direct 0x000328E0` |
| `0x00075270` | call | `direct 0x00039680` |
| `0x0007527E` | call | `direct 0x00032DC0` |
| `0x000752B8` | call | `direct 0x003DB020` |
| `0x000752C7` | call | `direct 0x003DB020` |
| `0x000752D6` | call | `direct 0x003DB020` |
| `0x000752E2` | call | `direct 0x003DB020` |
| `0x000752EB` | call | `direct 0x003B20D4` |
| `0x00075332` | call | `direct 0x003DB020` |
| `0x00075341` | call | `direct 0x003DB020` |
| `0x00075350` | call | `direct 0x003DB020` |
| `0x0007535C` | call | `direct 0x003DB020` |
| `0x00075365` | call | `direct 0x003B20D4` |
| `0x00075389` | call | `direct 0x0006F1F0` |
| `0x000753A0` | call | `direct 0x00072DE0` |
| `0x000753AD` | call | `direct 0x0023D0D0` |
| `0x000753BD` | call | `direct 0x002216B0` |
| `0x000753D0` | call | `direct 0x00072DE0` |
| `0x000753E3` | call | `direct 0x0023E320` |
| `0x000753F3` | call | `direct 0x00072F40` |
| `0x00075605` | call | `direct 0x0021D330` |
| `0x0007562A` | call | `direct 0x00063E00` |
| `0x00075656` | call | `direct 0x003DB020` |
| `0x00075665` | call | `direct 0x003DB020` |
| `0x00075674` | call | `direct 0x003DB020` |
| `0x00075680` | call | `direct 0x003DB020` |
| `0x00075689` | call | `direct 0x003B20D4` |
| `0x000756D0` | call | `direct 0x003DB020` |
| `0x000756DF` | call | `direct 0x003DB020` |
| `0x000756EE` | call | `direct 0x003DB020` |
| `0x000756FA` | call | `direct 0x003DB020` |
| `0x00075703` | call | `direct 0x003B20D4` |
| `0x0007572C` | call | `direct 0x00032EF0` |
| `0x0007573A` | call | `direct 0x00032EF0` |
| `0x00075748` | call | `direct 0x00032EF0` |
| `0x0007575C` | call | `direct 0x00241A60` |
| `0x00075776` | context | `mov qword ptr [rsp + 0x90], rax` |
| `0x000757D9` | call | `direct 0x00146260` |
| `0x00075817` | call | `direct 0x00159840` |
| `0x00075829` | call | `direct 0x00159BA0` |
| `0x0007585C` | call | `direct 0x00072F40` |
| `0x00075ADA` | call | `direct 0x000858D0` |
| `0x00075B15` | call | `direct 0x00062850` |
| `0x00075B23` | call | `direct 0x00032EF0` |
| `0x00075B31` | call | `direct 0x00032EF0` |
| `0x00075B40` | call | `direct 0x00159C30` |
| `0x00075B45` | context | `mov rcx, qword ptr [rsp + 0x90]` |
| `0x00075DAB` | call | `direct 0x0026BED0` |
| `0x00075DC3` | context | `lea r8, [rsp + 0x90]` |
| `0x00075DD6` | call | `direct 0x0003FB80` |
| `0x00075DEE` | call | `direct 0x00035230` |
| `0x00075DFC` | call | `direct 0x00032EF0` |
| `0x00075E0A` | call | `direct 0x00032EF0` |
| `0x00075E63` | call | `direct 0x00085A50` |
| `0x00075E80` | call | `direct 0x00063890` |
| `0x00075E8E` | call | `direct 0x00032EF0` |
| `0x00075E9C` | call | `direct 0x00032EF0` |
| `0x00075F49` | call | `direct 0x0026C060` |
| `0x00075F61` | call | `direct 0x00063890` |
| `0x00075F6F` | call | `direct 0x00032EF0` |
| `0x00076029` | call | `direct 0x0026C060` |
| `0x00076041` | call | `direct 0x00063890` |
| `0x0007604F` | call | `direct 0x00032EF0` |
| `0x00076273` | counter | `mov byte ptr [rsp + 0x538], al` |
| `0x0007627A` | counter | `movsx ecx, byte ptr [rsp + 0x538]` |
| `0x00076570` | call | `direct 0x00084F90` |
| `0x00076583` | call | `direct 0x00062FF0` |
| `0x00076591` | call | `direct 0x00032EF0` |
| `0x00076596` | call | `direct 0x00391550` |
| `0x0007659E` | call | `direct 0x00391534` |
| `0x000765DC` | call | `direct 0x00071070` |
| `0x000765F5` | call | `direct 0x00071E80` |
| `0x00076A91` | call | `direct 0x00086460` |
| `0x00076AA4` | call | `direct 0x00040050` |
| `0x00076AB2` | call | `direct 0x00032EF0` |
| `0x00076ABE` | call | `direct 0x00241DE0` |
| `0x00076AD8` | call | `direct 0x00071E80` |
| `0x00076AF4` | call | `direct 0x0006A590` |
| `0x00076F46` | call | `direct 0x001269F0` |
| `0x00076F5C` | call | `direct 0x00040530` |
| `0x00076F6A` | call | `direct 0x00032EF0` |
| `0x00076F78` | call | `direct 0x00032EF0` |
| `0x00076F84` | call | `direct 0x00241DE0` |
| `0x00076F8C` | call | `direct 0x000831C0` |
| `0x00076F9B` | call | `direct 0x00225800` |
| `0x00076FB6` | call | `direct 0x00087690` |
| `0x000774C7` | call | `direct 0x000DCCF0` |
| `0x000774E1` | call | `direct 0x00063420` |
| `0x000774EF` | call | `direct 0x00032EF0` |
| `0x00077536` | call | `direct 0x0013C5A0` |
| `0x0007756F` | call | `direct 0x00058410` |
| `0x0007757D` | call | `direct 0x001348B0` |
| `0x0007775B` | call | `direct 0x0026EE50` |
| `0x00077775` | call | `direct 0x0005CD90` |
| `0x00077785` | call | `direct 0x00043F90` |
| `0x00077792` | call | `direct 0x00032EF0` |
| `0x000777F7` | call | `direct 0x00085770` |
| `0x00077811` | call | `direct 0x0005CD90` |
| `0x00077829` | call | `direct 0x00035230` |
| `0x00077837` | call | `direct 0x00032EF0` |
| `0x0007784D` | call | `direct 0x00137960` |
| `0x00077B81` | call | `direct 0x0021C680` |
| `0x00077B91` | call | `direct 0x00043F90` |
| `0x00077C1C` | call | `direct 0x0026C060` |
| `0x00077C34` | call | `direct 0x00035230` |
| `0x00077C42` | call | `direct 0x00032EF0` |
| `0x00077D11` | call | `direct 0x001249B0` |
| `0x00077D42` | call | `direct 0x000627D0` |
| `0x00077D5A` | call | `direct 0x00035230` |
| `0x00077D68` | call | `direct 0x00032EF0` |
| `0x00077D76` | call | `direct 0x00032EF0` |
| `0x00077D9E` | call | `indirect qword ptr [rax]` |
| `0x00077DB5` | call | `indirect qword ptr [rax + 8]` |
| `0x00077DEA` | call | `direct 0x00040050` |
| `0x00077E14` | call | `direct 0x00040050` |
| `0x00077E22` | call | `direct 0x00032EF0` |
| `0x00077E30` | call | `direct 0x00032EF0` |
| `0x00077E4A` | call | `direct 0x00134A40` |
| `0x00077E52` | call | `direct 0x00079CB0` |
| `0x00077ED2` | call | `direct 0x0013C5A0` |
| `0x00077F1F` | call | `direct 0x00058410` |
| `0x00077F2D` | call | `direct 0x00134910` |
| `0x00078084` | call | `direct 0x000DBC00` |
| `0x0007809E` | call | `direct 0x0005CD90` |
| `0x000780AE` | call | `direct 0x00043F90` |
| `0x000780BB` | call | `direct 0x00032EF0` |
| `0x00078128` | call | `direct 0x001BFED0` |
| `0x00078142` | call | `direct 0x0005CD90` |
| `0x0007815A` | call | `direct 0x00035230` |
| `0x00078168` | call | `direct 0x00032EF0` |
| `0x00078176` | call | `direct 0x00032EF0` |
| `0x00078186` | call | `direct 0x0006A320` |
| `0x0007819A` | call | `indirect qword ptr [rax + 0x38]` |
| `0x000781E0` | call | `direct 0x00068370` |
| `0x0007820A` | call | `direct 0x00086AD0` |
| `0x0007823A` | call | `direct 0x00034800` |
| `0x0007824A` | call | `direct 0x00044EF0` |
| `0x00078265` | call | `direct 0x00032EF0` |
| `0x00078280` | call | `direct 0x00032EF0` |
| `0x000783A2` | call | `direct 0x000861E0` |
| `0x000783BB` | call | `direct 0x0005CD90` |
| `0x000783CB` | call | `direct 0x00043F90` |
| `0x000783D8` | call | `direct 0x00032EF0` |
| `0x00078447` | call | `direct 0x00084ED0` |
| `0x00078460` | call | `direct 0x0005CD90` |
| `0x00078478` | call | `direct 0x00035230` |
| `0x00078486` | call | `direct 0x00032EF0` |
| `0x00078494` | call | `direct 0x00032EF0` |
| `0x000784A2` | call | `direct 0x00032EF0` |
| `0x000784BB` | call | `indirect qword ptr [rax + 0x38]` |
| `0x0007850A` | call | `direct 0x000B9080` |
| `0x00078534` | call | `direct 0x00086AD0` |
| `0x00078564` | call | `direct 0x00034800` |
| `0x00078574` | call | `direct 0x00044EF0` |
| `0x0007858F` | call | `direct 0x00032EF0` |
| `0x000785AA` | call | `direct 0x00032EF0` |
| `0x000786DE` | call | `direct 0x00057250` |
| `0x000786F7` | call | `direct 0x0005CD90` |
| `0x00078707` | call | `direct 0x00043F90` |
| `0x00078714` | call | `direct 0x00032EF0` |
| `0x00078783` | call | `direct 0x00084ED0` |
| `0x0007879C` | call | `direct 0x0005CD90` |
| `0x000787B4` | call | `direct 0x00035230` |
| `0x000787C2` | call | `direct 0x00032EF0` |
| `0x000787D0` | call | `direct 0x00032EF0` |
| `0x000787DE` | call | `direct 0x00032EF0` |
| `0x000787F2` | call | `direct 0x00057980` |
| `0x00078927` | call | `direct 0x00057250` |
| `0x00078940` | call | `direct 0x0005CD90` |
| `0x00078950` | call | `direct 0x00043F90` |
| `0x0007895D` | call | `direct 0x00032EF0` |
| `0x000789CC` | call | `direct 0x00084ED0` |
| `0x000789E5` | call | `direct 0x0005CD90` |
| `0x000789FD` | call | `direct 0x00035230` |
| `0x00078A0B` | call | `direct 0x00032EF0` |
| `0x00078A19` | call | `direct 0x00032EF0` |
| `0x00078A26` | call | `direct 0x00134570` |
| `0x00078A3E` | call | `direct 0x00134570` |
| `0x00078A63` | call | `direct 0x00032EF0` |
| `0x00078A73` | call | `direct 0x00068B30` |
| `0x00078AB9` | call | `direct 0x00062FF0` |
| `0x00078AE2` | call | `direct 0x00063150` |
| `0x00078B06` | call | `direct 0x00063150` |
| `0x00078B2A` | call | `direct 0x00063150` |
| `0x00078B38` | call | `direct 0x00032EF0` |
| `0x00078B46` | call | `direct 0x00032EF0` |
| `0x00078B54` | call | `direct 0x00032EF0` |
| `0x00078B62` | call | `direct 0x00032EF0` |
| `0x00078B72` | call | `direct 0x0013C100` |
| `0x00078B83` | vmr/rxboost | `mov qword ptr [rsp + 0xb0], 0` |
| `0x00078B8F` | vmt2 | `mov dword ptr [rsp + 0xb8], r14d` |
| `0x00078BCC` | call | `direct 0x0013BFB0` |
| `0x00078BE0` | vmt2 | `movups xmmword ptr [rsp + 0xb8], xmm1` |
| `0x00078C0A` | call | `direct 0x00072F40` |
| `0x00078C1E` | call | `direct 0x00073C90` |
| `0x00078C2C` | call | `direct 0x00032EF0` |
| `0x00078C4A` | call | `direct 0x0006A590` |
| `0x00078C5E` | call | `direct 0x00073C90` |
| `0x00078C6C` | call | `direct 0x00032EF0` |
| `0x00078C89` | call | `direct 0x00268890` |
| `0x00078C99` | call | `direct 0x00072F40` |
| `0x00078FB9` | call | `direct 0x00086390` |
| `0x00078FD4` | call | `direct 0x00063D10` |
| `0x00078FE2` | call | `direct 0x00032EF0` |
| `0x00078FF0` | call | `direct 0x00032EF0` |
| `0x00078FFE` | call | `direct 0x00032EF0` |
| `0x00079006` | call | `direct 0x0006A410` |
| `0x00079016` | mt | `mov r14, qword ptr [rsp + 0x98]` |
| `0x00079021` | call | `direct 0x0014AC70` |
| `0x00079031` | call | `direct 0x00072F40` |
| `0x00079279` | call | `direct 0x0003A9B0` |
| `0x00079294` | call | `direct 0x00063D10` |
| `0x000792A2` | call | `direct 0x00032EF0` |
| `0x000792B0` | call | `direct 0x00032EF0` |
| `0x000792BE` | call | `direct 0x00032EF0` |
| `0x000792D1` | call | `direct 0x00072F40` |
| `0x000792EC` | call | `direct 0x000735B0` |
| `0x000792FA` | call | `direct 0x00032EF0` |
| `0x00079322` | call | `direct 0x00037F40` |
| `0x0007937F` | call | `direct 0x00072F40` |
| `0x000796BA` | call | `direct 0x00085EB0` |
| `0x000796DA` | call | `direct 0x00063C20` |
| `0x000796E8` | call | `direct 0x00032EF0` |
| `0x000796F6` | call | `direct 0x00032EF0` |
| `0x00079704` | call | `direct 0x0003A120` |
| `0x00079727` | call | `direct 0x0014AC70` |
| `0x0007973E` | call | `direct 0x0006A590` |
| `0x00079986` | call | `direct 0x0003A9B0` |
| `0x000799A1` | call | `direct 0x00063D10` |
| `0x000799AF` | call | `direct 0x00032EF0` |
| `0x000799BD` | call | `direct 0x00032EF0` |
| `0x000799CB` | call | `direct 0x00032EF0` |
| `0x000799EF` | call | `direct 0x0006A590` |
| `0x00079A0A` | call | `direct 0x000735B0` |
| `0x00079A18` | call | `direct 0x00032EF0` |
| `0x00079A20` | call | `direct 0x00072D50` |
| `0x00079A3A` | call | `direct 0x002216B0` |
| `0x00079C28` | call | `direct 0x0026EB10` |
| `0x00079C3E` | call | `direct 0x00063A60` |
| `0x00079C4C` | call | `direct 0x00032EF0` |
| `0x00079C5A` | call | `direct 0x00032EF0` |
| `0x00079C68` | call | `direct 0x00062D20` |
| `0x00079C76` | call | `direct 0x0012F910` |
| `0x00079C84` | call | `direct 0x00032EF0` |
| `0x00079C94` | call | `direct 0x003B24C0` |

### indirect call `0x00074B43` — `qword ptr [rip + 0x3bb747]`

```asm
0x00074AB0: mov byte ptr [rsp + 0x18], r8b
0x00074AB5: mov dword ptr [rsp + 0x10], edx
0x00074AB9: push rbx
0x00074ABA: push rsi
0x00074ABB: push rdi
0x00074ABC: push r12
0x00074ABE: push r13
0x00074AC0: push r14
0x00074AC2: push r15
0x00074AC4: mov eax, 0x1610
0x00074AC9: call 0x1403b2500
0x00074ACE: sub rsp, rax
0x00074AD1: mov qword ptr [rsp + 0x160], 0xfffffffffffffffe
0x00074ADD: mov rax, qword ptr [rip + 0x761e0c]
0x00074AE4: xor rax, rsp
0x00074AE7: mov qword ptr [rsp + 0x1600], rax
0x00074AEF: mov rbx, r9
0x00074AF2: mov r15, rcx
0x00074AF5: mov qword ptr [rsp + 0x88], rcx
0x00074AFD: mov qword ptr [rsp + 0xe0], rcx
0x00074B05: mov rax, qword ptr [rsp + 0x1680]
0x00074B0D: mov qword ptr [rsp + 0x98], rax
0x00074B15: mov rax, qword ptr [rsp + 0x1688]
0x00074B1D: mov qword ptr [rsp + 0xa0], rax
0x00074B25: xor r14d, r14d
0x00074B28: mov dword ptr [rsp + 0x34], r14d
0x00074B2D: lea rdx, [rip + 0x3c387c]
0x00074B34: mov cl, 1
0x00074B36: call 0x140062d20
0x00074B3B: lea rcx, [rsp + 0x998]
0x00074B43: call qword ptr [rip + 0x3bb747]
0x00074B49: mov rdx, rbx
0x00074B4C: lea rcx, [rsp + 0xa28]
0x00074B54: call 0x1402216b0
0x00074B59: mov rbx, rax
0x00074B5C: mov dword ptr [rsp + 0x5f0], 0x38
0x00074B67: mov dword ptr [rsp + 0x5f4], 0x35
0x00074B72: mov ecx, dword ptr [rsp + 0x5f4]
0x00074B79: xor ecx, 0x12
0x00074B7C: mov byte ptr [rsp + 0x5f8], cl
0x00074B83: movsx edx, byte ptr [rsp + 0x5f8]
0x00074B8B: xor edx, 0x12
0x00074B8E: mov byte ptr [rsp + 0x5f9], dl
0x00074B95: movsx ecx, byte ptr [rsp + 0x5f9]
0x00074B9D: xor ecx, 0x12
0x00074BA0: mov byte ptr [rsp + 0x5fa], cl
0x00074BA7: movsx ecx, byte ptr [rsp + 0x5fa]
0x00074BAF: xor ecx, 0x18
0x00074BB2: mov byte ptr [rsp + 0x5fb], cl
0x00074BB9: movsx ecx, byte ptr [rsp + 0x5fb]
0x00074BC1: xor ecx, 0x43
0x00074BC4: mov byte ptr [rsp + 0x5fc], cl
0x00074BCB: movsx ecx, byte ptr [rsp + 0x5fc]
0x00074BD3: xor ecx, 0x45
0x00074BD6: mov byte ptr [rsp + 0x5fd], cl
0x00074BDD: movsx ecx, byte ptr [rsp + 0x5fd]
0x00074BE5: xor ecx, 0x18
0x00074BE8: mov byte ptr [rsp + 0x5fe], cl
0x00074BEF: movsx ecx, byte ptr [rsp + 0x5fe]
0x00074BF7: xor ecx, 0x12
```

### indirect call `0x00077D9E` — `qword ptr [rax]`

```asm
0x00077CD4: inc ecx
0x00077CD6: mov byte ptr [rsp + 0x882], cl
0x00077CDD: movsx ecx, byte ptr [rsp + 0x882]
0x00077CE5: xor ecx, 0x29
0x00077CE8: inc ecx
0x00077CEA: mov byte ptr [rsp + 0x883], cl
0x00077CF1: mov byte ptr [rsp + 0x884], 0
0x00077CF9: movzx eax, byte ptr [rsp + 0x87c]
0x00077D01: lea rdx, [rsp + 0xb68]
0x00077D09: lea rcx, [rsp + 0x878]
0x00077D11: call 0x1401249b0
0x00077D16: nop
0x00077D17: cmp qword ptr [rax + 0x18], 0x10
0x00077D1C: jb 0x140077d21
0x00077D1E: mov rax, qword ptr [rax]
0x00077D21: mov qword ptr [rsp + 0x178], rax
0x00077D29: mov r8, qword ptr [rsp + 0x58]
0x00077D2E: add r8, 8
0x00077D32: lea r9, [rsp + 0x68]
0x00077D37: mov rdx, rax
0x00077D3A: lea rcx, [rsp + 0xb48]
0x00077D42: call 0x1400627d0
0x00077D47: nop
0x00077D48: or r9, 0xffffffffffffffff
0x00077D4C: xor r8d, r8d
0x00077D4F: mov rdx, rax
0x00077D52: lea rcx, [rsp + 0x938]
0x00077D5A: call 0x140035230
0x00077D5F: nop
0x00077D60: lea rcx, [rsp + 0xb48]
0x00077D68: call 0x140032ef0
0x00077D6D: nop
0x00077D6E: lea rcx, [rsp + 0xb68]
0x00077D76: call 0x140032ef0
0x00077D7B: nop
0x00077D7C: mov rcx, qword ptr [rsp + 0x60]
0x00077D81: test rcx, rcx
0x00077D84: je 0x140077db8
0x00077D86: or eax, 0xffffffff
0x00077D89: lock xadd dword ptr [rcx + 8], eax
0x00077D8E: cmp eax, 1
0x00077D91: jne 0x140077db8
0x00077D93: mov rsi, qword ptr [rsp + 0x60]
0x00077D98: mov rax, qword ptr [rsi]
0x00077D9B: mov rcx, rsi
0x00077D9E: call qword ptr [rax]
0x00077DA0: or eax, 0xffffffff
0x00077DA3: lock xadd dword ptr [rsi + 0xc], eax
0x00077DA8: cmp eax, 1
0x00077DAB: jne 0x140077db8
0x00077DAD: mov rcx, qword ptr [rsp + 0x60]
0x00077DB2: mov rax, qword ptr [rcx]
0x00077DB5: call qword ptr [rax + 8]
0x00077DB8: add rbx, 0x10
0x00077DBC: cmp rbx, rdi
0x00077DBF: jne 0x140077550
0x00077DC5: cmp qword ptr [rsp + 0x968], 0
0x00077DCE: je 0x140077def
0x00077DD0: lea rcx, [rsp + 0x958]
0x00077DD8: cmp qword ptr [rsp + 0x970], 0x10
0x00077DE1: cmovae rcx, qword ptr [rsp + 0x958]
0x00077DEA: call 0x140040050
0x00077DEF: cmp qword ptr [rsp + 0x948], 0
0x00077DF8: je 0x140077e1a
0x00077DFA: lea rcx, [rsp + 0x938]
0x00077E02: cmp qword ptr [rsp + 0x950], 0x10
0x00077E0B: cmovae rcx, qword ptr [rsp + 0x938]
0x00077E14: call 0x140040050
0x00077E19: nop
0x00077E1A: lea rcx, [rsp + 0x938]
0x00077E22: call 0x140032ef0
0x00077E27: nop
0x00077E28: lea rcx, [rsp + 0x958]
0x00077E30: call 0x140032ef0
0x00077E35: cmp dword ptr [rsp + 0x1658], 2
```

### indirect call `0x00077DB5` — `qword ptr [rax + 8]`

```asm
0x00077CF9: movzx eax, byte ptr [rsp + 0x87c]
0x00077D01: lea rdx, [rsp + 0xb68]
0x00077D09: lea rcx, [rsp + 0x878]
0x00077D11: call 0x1401249b0
0x00077D16: nop
0x00077D17: cmp qword ptr [rax + 0x18], 0x10
0x00077D1C: jb 0x140077d21
0x00077D1E: mov rax, qword ptr [rax]
0x00077D21: mov qword ptr [rsp + 0x178], rax
0x00077D29: mov r8, qword ptr [rsp + 0x58]
0x00077D2E: add r8, 8
0x00077D32: lea r9, [rsp + 0x68]
0x00077D37: mov rdx, rax
0x00077D3A: lea rcx, [rsp + 0xb48]
0x00077D42: call 0x1400627d0
0x00077D47: nop
0x00077D48: or r9, 0xffffffffffffffff
0x00077D4C: xor r8d, r8d
0x00077D4F: mov rdx, rax
0x00077D52: lea rcx, [rsp + 0x938]
0x00077D5A: call 0x140035230
0x00077D5F: nop
0x00077D60: lea rcx, [rsp + 0xb48]
0x00077D68: call 0x140032ef0
0x00077D6D: nop
0x00077D6E: lea rcx, [rsp + 0xb68]
0x00077D76: call 0x140032ef0
0x00077D7B: nop
0x00077D7C: mov rcx, qword ptr [rsp + 0x60]
0x00077D81: test rcx, rcx
0x00077D84: je 0x140077db8
0x00077D86: or eax, 0xffffffff
0x00077D89: lock xadd dword ptr [rcx + 8], eax
0x00077D8E: cmp eax, 1
0x00077D91: jne 0x140077db8
0x00077D93: mov rsi, qword ptr [rsp + 0x60]
0x00077D98: mov rax, qword ptr [rsi]
0x00077D9B: mov rcx, rsi
0x00077D9E: call qword ptr [rax]
0x00077DA0: or eax, 0xffffffff
0x00077DA3: lock xadd dword ptr [rsi + 0xc], eax
0x00077DA8: cmp eax, 1
0x00077DAB: jne 0x140077db8
0x00077DAD: mov rcx, qword ptr [rsp + 0x60]
0x00077DB2: mov rax, qword ptr [rcx]
0x00077DB5: call qword ptr [rax + 8]
0x00077DB8: add rbx, 0x10
0x00077DBC: cmp rbx, rdi
0x00077DBF: jne 0x140077550
0x00077DC5: cmp qword ptr [rsp + 0x968], 0
0x00077DCE: je 0x140077def
0x00077DD0: lea rcx, [rsp + 0x958]
0x00077DD8: cmp qword ptr [rsp + 0x970], 0x10
0x00077DE1: cmovae rcx, qword ptr [rsp + 0x958]
0x00077DEA: call 0x140040050
0x00077DEF: cmp qword ptr [rsp + 0x948], 0
0x00077DF8: je 0x140077e1a
0x00077DFA: lea rcx, [rsp + 0x938]
0x00077E02: cmp qword ptr [rsp + 0x950], 0x10
0x00077E0B: cmovae rcx, qword ptr [rsp + 0x938]
0x00077E14: call 0x140040050
0x00077E19: nop
0x00077E1A: lea rcx, [rsp + 0x938]
0x00077E22: call 0x140032ef0
0x00077E27: nop
0x00077E28: lea rcx, [rsp + 0x958]
0x00077E30: call 0x140032ef0
0x00077E35: cmp dword ptr [rsp + 0x1658], 2
0x00077E3D: jne 0x140078b67
0x00077E43: lea rcx, [rip + 0x76e5be]
0x00077E4A: call 0x140134a40
0x00077E4F: mov rcx, r15
0x00077E52: call 0x140079cb0
0x00077E57: mov qword ptr [rsp + 0x990], 0xf
0x00077E63: mov qword ptr [rsp + 0x988], r14
```

### indirect call `0x0007819A` — `qword ptr [rax + 0x38]`

```asm
0x000780AE: call 0x140043f90
0x000780B3: lea rcx, [rsp + 0xb88]
0x000780BB: call 0x140032ef0
0x000780C0: nop
0x000780C1: lea rcx, [rsp + 0xba8]
0x000780C9: jmp 0x140078176
0x000780CE: mov dword ptr [rsp + 0x8e8], 0x11
0x000780D9: mov dword ptr [rsp + 0x8ec], 0x26
0x000780E4: mov eax, dword ptr [rsp + 0x8ec]
0x000780EB: xor eax, 0x3d
0x000780EE: mov byte ptr [rsp + 0x8f0], al
0x000780F5: movsx ecx, byte ptr [rsp + 0x8f0]
0x000780FD: xor ecx, 0x31
0x00078100: mov byte ptr [rsp + 0x8f1], cl
0x00078107: xor eax, eax
0x00078109: mov byte ptr [rsp + 0x8f2], al
0x00078110: movzx eax, byte ptr [rsp + 0x8f0]
0x00078118: lea rdx, [rsp + 0xbe8]
0x00078120: lea rcx, [rsp + 0x8e8]
0x00078128: call 0x1401bfed0
0x0007812D: nop
0x0007812E: mov rsi, qword ptr [rsp + 0x70]
0x00078133: lea r8, [rsi + 8]
0x00078137: mov rdx, rax
0x0007813A: lea rcx, [rsp + 0xbc8]
0x00078142: call 0x14005cd90
0x00078147: nop
0x00078148: or r9, 0xffffffffffffffff
0x0007814C: xor r8d, r8d
0x0007814F: mov rdx, rax
0x00078152: lea rcx, [rsp + 0x978]
0x0007815A: call 0x140035230
0x0007815F: nop
0x00078160: lea rcx, [rsp + 0xbc8]
0x00078168: call 0x140032ef0
0x0007816D: nop
0x0007816E: lea rcx, [rsp + 0xbe8]
0x00078176: call 0x140032ef0
0x0007817B: lea rdx, [rsp + 0x1e0]
0x00078183: mov rcx, rsi
0x00078186: call 0x14006a320
0x0007818B: test r15b, r15b
0x0007818E: je 0x1400784ac
0x00078194: mov rax, qword ptr [rsi]
0x00078197: mov rcx, rsi
0x0007819A: call qword ptr [rax + 0x38]
0x0007819D: test al, al
0x0007819F: je 0x1400781f1
0x000781A1: mov dword ptr [rsp + 0x8e0], 0x2a
0x000781AC: mov eax, dword ptr [rsp + 0x8e0]
0x000781B3: xor eax, 0x30
0x000781B6: add eax, 0xa
0x000781B9: mov byte ptr [rsp + 0x8e4], al
0x000781C0: mov byte ptr [rsp + 0x8e5], 0
0x000781C8: movzx eax, byte ptr [rsp + 0x8e4]
0x000781D0: lea rdx, [rsp + 0xc28]
0x000781D8: lea rcx, [rsp + 0x8e0]
0x000781E0: call 0x140068370
0x000781E5: mov r12, rax
0x000781E8: mov esi, dword ptr [rsp + 0x34]
0x000781EC: or esi, 1
0x000781EF: jmp 0x140078219
0x000781F1: mov edx, 0xf
0x000781F6: mov eax, dword ptr [rsp + 0x1e8]
0x000781FD: test eax, eax
0x000781FF: cmovne edx, eax
0x00078202: lea rcx, [rsp + 0xc08]
0x0007820A: call 0x140086ad0
0x0007820F: mov r12, rax
0x00078212: mov esi, dword ptr [rsp + 0x34]
0x00078216: or esi, 2
0x00078219: mov dword ptr [rsp + 0x34], esi
0x0007821D: mov qword ptr [rsp + 0xab8], r14
0x00078225: mov qword ptr [rsp + 0xac0], r14
0x0007822D: xor r8d, r8d
```

### indirect call `0x000784BB` — `qword ptr [rax + 0x38]`

```asm
0x000783DD: nop
0x000783DE: lea rcx, [rsp + 0xc68]
0x000783E6: jmp 0x140078494
0x000783EB: mov dword ptr [rsp + 0x8f8], 0x2b
0x000783F6: mov eax, dword ptr [rsp + 0x8f8]
0x000783FD: add al, 0x2b
0x000783FF: movsx ecx, al
0x00078402: xor ecx, 0x2d
0x00078405: mov dword ptr [rsp + 0x8fc], ecx
0x0007840C: mov eax, dword ptr [rsp + 0x8fc]
0x00078413: mov ecx, dword ptr [rsp + 0x8f8]
0x0007841A: xor ecx, eax
0x0007841C: xor ecx, 0x2c
0x0007841F: mov byte ptr [rsp + 0x900], cl
0x00078426: xor eax, eax
0x00078428: mov byte ptr [rsp + 0x901], al
0x0007842F: movzx eax, byte ptr [rsp + 0x900]
0x00078437: lea rdx, [rsp + 0xca8]
0x0007843F: lea rcx, [rsp + 0x8f8]
0x00078447: call 0x140084ed0
0x0007844C: nop
0x0007844D: lea r8, [rsp + 0xaa8]
0x00078455: mov rdx, rax
0x00078458: lea rcx, [rsp + 0xc88]
0x00078460: call 0x14005cd90
0x00078465: nop
0x00078466: or r9, 0xffffffffffffffff
0x0007846A: xor r8d, r8d
0x0007846D: mov rdx, rax
0x00078470: lea rcx, [rsp + 0x9e8]
0x00078478: call 0x140035230
0x0007847D: nop
0x0007847E: lea rcx, [rsp + 0xc88]
0x00078486: call 0x140032ef0
0x0007848B: nop
0x0007848C: lea rcx, [rsp + 0xca8]
0x00078494: call 0x140032ef0
0x00078499: nop
0x0007849A: lea rcx, [rsp + 0xaa8]
0x000784A2: call 0x140032ef0
0x000784A7: mov rsi, qword ptr [rsp + 0x70]
0x000784AC: test r13b, r13b
0x000784AF: je 0x1400787e3
0x000784B5: mov rax, qword ptr [rsi]
0x000784B8: mov rcx, rsi
0x000784BB: call qword ptr [rax + 0x38]
0x000784BE: test al, al
0x000784C0: je 0x14007851b
0x000784C2: mov dword ptr [rsp + 0x928], 0x50
0x000784CD: mov dword ptr [rsp + 0x92c], 0x7f
0x000784D8: mov eax, dword ptr [rsp + 0x92c]
0x000784DF: xor eax, 0x60
0x000784E2: mov byte ptr [rsp + 0x930], al
0x000784E9: xor eax, eax
0x000784EB: mov byte ptr [rsp + 0x931], al
0x000784F2: movzx eax, byte ptr [rsp + 0x930]
0x000784FA: lea rdx, [rsp + 0xce8]
0x00078502: lea rcx, [rsp + 0x928]
0x0007850A: call 0x1400b9080
0x0007850F: mov r12, rax
0x00078512: mov esi, dword ptr [rsp + 0x34]
0x00078516: or esi, 4
0x00078519: jmp 0x140078543
0x0007851B: mov edx, 0x1e
0x00078520: mov eax, dword ptr [rsp + 0x1ec]
0x00078527: test eax, eax
0x00078529: cmovg edx, eax
0x0007852C: lea rcx, [rsp + 0xcc8]
0x00078534: call 0x140086ad0
0x00078539: mov r12, rax
0x0007853C: mov esi, dword ptr [rsp + 0x34]
0x00078540: or esi, 8
0x00078543: mov dword ptr [rsp + 0x34], esi
0x00078547: mov qword ptr [rsp + 0xa98], r14
0x0007854F: mov qword ptr [rsp + 0xaa0], r14
```

## PDATA `0x00086C60..0x0008759D`

### Calls and timing-shaped accesses

| RVA | kind | instruction |
|---|---|---|
| `0x00086CA9` | call | `direct 0x0013C5A0` |
| `0x00086CF2` | call | `direct 0x00134570` |
| `0x00086D15` | call | `direct 0x003D3750` |
| `0x00086D29` | call | `direct 0x00164410` |
| `0x00086D50` | call | `indirect qword ptr [rax]` |
| `0x00086D65` | call | `indirect qword ptr [rax + 8]` |
| `0x00086D8E` | call | `indirect qword ptr [rax]` |
| `0x00086DA2` | call | `indirect qword ptr [rax + 8]` |
| `0x000871BE` | call | `direct 0x00085440` |
| `0x000871D1` | call | `direct 0x00040050` |
| `0x000871FD` | call | `direct 0x003DB020` |
| `0x0008720C` | call | `direct 0x003DB020` |
| `0x0008721B` | call | `direct 0x003DB020` |
| `0x0008722B` | call | `direct 0x003DB020` |
| `0x00087501` | call | `direct 0x000862B0` |
| `0x00087514` | call | `direct 0x00040050` |
| `0x00087538` | call | `direct 0x003DB020` |
| `0x00087547` | call | `direct 0x003DB020` |
| `0x00087556` | call | `direct 0x003DB020` |
| `0x00087562` | call | `direct 0x003DB020` |
| `0x0008756B` | call | `direct 0x003B20D4` |
| `0x00087577` | call | `direct 0x003B24C0` |

### indirect call `0x00086D50` — `qword ptr [rax]`

```asm
0x00086CA2: add rcx, 0x300
0x00086CA9: call 0x14013c5a0
0x00086CAE: mov rbx, qword ptr [rax]
0x00086CB1: mov rdi, qword ptr [rax + 8]
0x00086CB5: cmp rbx, rdi
0x00086CB8: je 0x140086da5
0x00086CBE: xor r13d, r13d
0x00086CC1: or r15d, 0xffffffff
0x00086CC5: nop word ptr [rax + rax]
0x00086CD0: mov rsi, qword ptr [rbx + 8]
0x00086CD4: mov r14, qword ptr [rbx]
0x00086CD7: test rsi, rsi
0x00086CDA: je 0x140086ce0
0x00086CDC: lock inc dword ptr [rsi + 8]
0x00086CE0: mov qword ptr [rsp + 0x48], rsi
0x00086CE5: mov qword ptr [rsp + 0x40], r14
0x00086CEA: test r14, r14
0x00086CED: je 0x140086d38
0x00086CEF: mov rcx, r14
0x00086CF2: call 0x140134570
0x00086CF7: cmp dword ptr [rax + 0xc], 1
0x00086CFB: jne 0x140086d38
0x00086CFD: mov dword ptr [rsp + 0x20], r13d
0x00086D02: lea r9, [rip + 0x753307]
0x00086D09: lea r8, [rip + 0x7532d8]
0x00086D10: xor edx, edx
0x00086D12: mov rcx, r14
0x00086D15: call 0x1403d3750
0x00086D1A: test rax, rax
0x00086D1D: je 0x140086d38
0x00086D1F: lea r8, [rsp + 0x30]
0x00086D24: mov dl, 1
0x00086D26: mov rcx, rax
0x00086D29: call 0x140164410
0x00086D2E: or r12b, al
0x00086D31: cmp byte ptr [rsp + 0x30], 0
0x00086D36: jne 0x140086d76
0x00086D38: test rsi, rsi
0x00086D3B: je 0x140086d68
0x00086D3D: mov eax, r15d
0x00086D40: lock xadd dword ptr [rsi + 8], eax
0x00086D45: cmp eax, 1
0x00086D48: jne 0x140086d68
0x00086D4A: mov rax, qword ptr [rsi]
0x00086D4D: mov rcx, rsi
0x00086D50: call qword ptr [rax]
0x00086D52: mov eax, r15d
0x00086D55: lock xadd dword ptr [rsi + 0xc], eax
0x00086D5A: cmp eax, 1
0x00086D5D: jne 0x140086d68
0x00086D5F: mov rax, qword ptr [rsi]
0x00086D62: mov rcx, rsi
0x00086D65: call qword ptr [rax + 8]
0x00086D68: add rbx, 0x10
0x00086D6C: cmp rbx, rdi
0x00086D6F: je 0x140086da5
0x00086D71: jmp 0x140086cd0
0x00086D76: test rsi, rsi
0x00086D79: je 0x140086da5
0x00086D7B: mov eax, r15d
0x00086D7E: lock xadd dword ptr [rsi + 8], eax
0x00086D83: cmp eax, 1
0x00086D86: jne 0x140086da5
0x00086D88: mov rax, qword ptr [rsi]
0x00086D8B: mov rcx, rsi
0x00086D8E: call qword ptr [rax]
0x00086D90: lock xadd dword ptr [rsi + 0xc], r15d
0x00086D96: cmp r15d, 1
0x00086D9A: jne 0x140086da5
0x00086D9C: mov rax, qword ptr [rsi]
0x00086D9F: mov rcx, rsi
0x00086DA2: call qword ptr [rax + 8]
0x00086DA5: cmp byte ptr [rsp + 0x30], 0
0x00086DAA: je 0x140087231
0x00086DB0: mov dword ptr [rsp + 0x50], 0x6b
```

### indirect call `0x00086D65` — `qword ptr [rax + 8]`

```asm
0x00086CC1: or r15d, 0xffffffff
0x00086CC5: nop word ptr [rax + rax]
0x00086CD0: mov rsi, qword ptr [rbx + 8]
0x00086CD4: mov r14, qword ptr [rbx]
0x00086CD7: test rsi, rsi
0x00086CDA: je 0x140086ce0
0x00086CDC: lock inc dword ptr [rsi + 8]
0x00086CE0: mov qword ptr [rsp + 0x48], rsi
0x00086CE5: mov qword ptr [rsp + 0x40], r14
0x00086CEA: test r14, r14
0x00086CED: je 0x140086d38
0x00086CEF: mov rcx, r14
0x00086CF2: call 0x140134570
0x00086CF7: cmp dword ptr [rax + 0xc], 1
0x00086CFB: jne 0x140086d38
0x00086CFD: mov dword ptr [rsp + 0x20], r13d
0x00086D02: lea r9, [rip + 0x753307]
0x00086D09: lea r8, [rip + 0x7532d8]
0x00086D10: xor edx, edx
0x00086D12: mov rcx, r14
0x00086D15: call 0x1403d3750
0x00086D1A: test rax, rax
0x00086D1D: je 0x140086d38
0x00086D1F: lea r8, [rsp + 0x30]
0x00086D24: mov dl, 1
0x00086D26: mov rcx, rax
0x00086D29: call 0x140164410
0x00086D2E: or r12b, al
0x00086D31: cmp byte ptr [rsp + 0x30], 0
0x00086D36: jne 0x140086d76
0x00086D38: test rsi, rsi
0x00086D3B: je 0x140086d68
0x00086D3D: mov eax, r15d
0x00086D40: lock xadd dword ptr [rsi + 8], eax
0x00086D45: cmp eax, 1
0x00086D48: jne 0x140086d68
0x00086D4A: mov rax, qword ptr [rsi]
0x00086D4D: mov rcx, rsi
0x00086D50: call qword ptr [rax]
0x00086D52: mov eax, r15d
0x00086D55: lock xadd dword ptr [rsi + 0xc], eax
0x00086D5A: cmp eax, 1
0x00086D5D: jne 0x140086d68
0x00086D5F: mov rax, qword ptr [rsi]
0x00086D62: mov rcx, rsi
0x00086D65: call qword ptr [rax + 8]
0x00086D68: add rbx, 0x10
0x00086D6C: cmp rbx, rdi
0x00086D6F: je 0x140086da5
0x00086D71: jmp 0x140086cd0
0x00086D76: test rsi, rsi
0x00086D79: je 0x140086da5
0x00086D7B: mov eax, r15d
0x00086D7E: lock xadd dword ptr [rsi + 8], eax
0x00086D83: cmp eax, 1
0x00086D86: jne 0x140086da5
0x00086D88: mov rax, qword ptr [rsi]
0x00086D8B: mov rcx, rsi
0x00086D8E: call qword ptr [rax]
0x00086D90: lock xadd dword ptr [rsi + 0xc], r15d
0x00086D96: cmp r15d, 1
0x00086D9A: jne 0x140086da5
0x00086D9C: mov rax, qword ptr [rsi]
0x00086D9F: mov rcx, rsi
0x00086DA2: call qword ptr [rax + 8]
0x00086DA5: cmp byte ptr [rsp + 0x30], 0
0x00086DAA: je 0x140087231
0x00086DB0: mov dword ptr [rsp + 0x50], 0x6b
0x00086DB8: mov eax, dword ptr [rsp + 0x50]
0x00086DBC: xor eax, 0x55
0x00086DBF: inc eax
0x00086DC1: mov byte ptr [rsp + 0x54], al
0x00086DC5: movsx ecx, byte ptr [rsp + 0x54]
0x00086DCA: xor ecx, 0x6e
0x00086DCD: inc ecx
```

### indirect call `0x00086D8E` — `qword ptr [rax]`

```asm
0x00086CF7: cmp dword ptr [rax + 0xc], 1
0x00086CFB: jne 0x140086d38
0x00086CFD: mov dword ptr [rsp + 0x20], r13d
0x00086D02: lea r9, [rip + 0x753307]
0x00086D09: lea r8, [rip + 0x7532d8]
0x00086D10: xor edx, edx
0x00086D12: mov rcx, r14
0x00086D15: call 0x1403d3750
0x00086D1A: test rax, rax
0x00086D1D: je 0x140086d38
0x00086D1F: lea r8, [rsp + 0x30]
0x00086D24: mov dl, 1
0x00086D26: mov rcx, rax
0x00086D29: call 0x140164410
0x00086D2E: or r12b, al
0x00086D31: cmp byte ptr [rsp + 0x30], 0
0x00086D36: jne 0x140086d76
0x00086D38: test rsi, rsi
0x00086D3B: je 0x140086d68
0x00086D3D: mov eax, r15d
0x00086D40: lock xadd dword ptr [rsi + 8], eax
0x00086D45: cmp eax, 1
0x00086D48: jne 0x140086d68
0x00086D4A: mov rax, qword ptr [rsi]
0x00086D4D: mov rcx, rsi
0x00086D50: call qword ptr [rax]
0x00086D52: mov eax, r15d
0x00086D55: lock xadd dword ptr [rsi + 0xc], eax
0x00086D5A: cmp eax, 1
0x00086D5D: jne 0x140086d68
0x00086D5F: mov rax, qword ptr [rsi]
0x00086D62: mov rcx, rsi
0x00086D65: call qword ptr [rax + 8]
0x00086D68: add rbx, 0x10
0x00086D6C: cmp rbx, rdi
0x00086D6F: je 0x140086da5
0x00086D71: jmp 0x140086cd0
0x00086D76: test rsi, rsi
0x00086D79: je 0x140086da5
0x00086D7B: mov eax, r15d
0x00086D7E: lock xadd dword ptr [rsi + 8], eax
0x00086D83: cmp eax, 1
0x00086D86: jne 0x140086da5
0x00086D88: mov rax, qword ptr [rsi]
0x00086D8B: mov rcx, rsi
0x00086D8E: call qword ptr [rax]
0x00086D90: lock xadd dword ptr [rsi + 0xc], r15d
0x00086D96: cmp r15d, 1
0x00086D9A: jne 0x140086da5
0x00086D9C: mov rax, qword ptr [rsi]
0x00086D9F: mov rcx, rsi
0x00086DA2: call qword ptr [rax + 8]
0x00086DA5: cmp byte ptr [rsp + 0x30], 0
0x00086DAA: je 0x140087231
0x00086DB0: mov dword ptr [rsp + 0x50], 0x6b
0x00086DB8: mov eax, dword ptr [rsp + 0x50]
0x00086DBC: xor eax, 0x55
0x00086DBF: inc eax
0x00086DC1: mov byte ptr [rsp + 0x54], al
0x00086DC5: movsx ecx, byte ptr [rsp + 0x54]
0x00086DCA: xor ecx, 0x6e
0x00086DCD: inc ecx
0x00086DCF: mov byte ptr [rsp + 0x55], cl
0x00086DD3: movsx ecx, byte ptr [rsp + 0x55]
0x00086DD8: xor ecx, 0x61
0x00086DDB: inc ecx
0x00086DDD: mov byte ptr [rsp + 0x56], cl
0x00086DE1: movsx ecx, byte ptr [rsp + 0x56]
0x00086DE6: xor ecx, 0x62
0x00086DE9: inc ecx
0x00086DEB: mov byte ptr [rsp + 0x57], cl
0x00086DEF: movsx ecx, byte ptr [rsp + 0x57]
0x00086DF4: xor ecx, 0x6c
0x00086DF7: inc ecx
0x00086DF9: mov byte ptr [rsp + 0x58], cl
```

### indirect call `0x00086DA2` — `qword ptr [rax + 8]`

```asm
0x00086D12: mov rcx, r14
0x00086D15: call 0x1403d3750
0x00086D1A: test rax, rax
0x00086D1D: je 0x140086d38
0x00086D1F: lea r8, [rsp + 0x30]
0x00086D24: mov dl, 1
0x00086D26: mov rcx, rax
0x00086D29: call 0x140164410
0x00086D2E: or r12b, al
0x00086D31: cmp byte ptr [rsp + 0x30], 0
0x00086D36: jne 0x140086d76
0x00086D38: test rsi, rsi
0x00086D3B: je 0x140086d68
0x00086D3D: mov eax, r15d
0x00086D40: lock xadd dword ptr [rsi + 8], eax
0x00086D45: cmp eax, 1
0x00086D48: jne 0x140086d68
0x00086D4A: mov rax, qword ptr [rsi]
0x00086D4D: mov rcx, rsi
0x00086D50: call qword ptr [rax]
0x00086D52: mov eax, r15d
0x00086D55: lock xadd dword ptr [rsi + 0xc], eax
0x00086D5A: cmp eax, 1
0x00086D5D: jne 0x140086d68
0x00086D5F: mov rax, qword ptr [rsi]
0x00086D62: mov rcx, rsi
0x00086D65: call qword ptr [rax + 8]
0x00086D68: add rbx, 0x10
0x00086D6C: cmp rbx, rdi
0x00086D6F: je 0x140086da5
0x00086D71: jmp 0x140086cd0
0x00086D76: test rsi, rsi
0x00086D79: je 0x140086da5
0x00086D7B: mov eax, r15d
0x00086D7E: lock xadd dword ptr [rsi + 8], eax
0x00086D83: cmp eax, 1
0x00086D86: jne 0x140086da5
0x00086D88: mov rax, qword ptr [rsi]
0x00086D8B: mov rcx, rsi
0x00086D8E: call qword ptr [rax]
0x00086D90: lock xadd dword ptr [rsi + 0xc], r15d
0x00086D96: cmp r15d, 1
0x00086D9A: jne 0x140086da5
0x00086D9C: mov rax, qword ptr [rsi]
0x00086D9F: mov rcx, rsi
0x00086DA2: call qword ptr [rax + 8]
0x00086DA5: cmp byte ptr [rsp + 0x30], 0
0x00086DAA: je 0x140087231
0x00086DB0: mov dword ptr [rsp + 0x50], 0x6b
0x00086DB8: mov eax, dword ptr [rsp + 0x50]
0x00086DBC: xor eax, 0x55
0x00086DBF: inc eax
0x00086DC1: mov byte ptr [rsp + 0x54], al
0x00086DC5: movsx ecx, byte ptr [rsp + 0x54]
0x00086DCA: xor ecx, 0x6e
0x00086DCD: inc ecx
0x00086DCF: mov byte ptr [rsp + 0x55], cl
0x00086DD3: movsx ecx, byte ptr [rsp + 0x55]
0x00086DD8: xor ecx, 0x61
0x00086DDB: inc ecx
0x00086DDD: mov byte ptr [rsp + 0x56], cl
0x00086DE1: movsx ecx, byte ptr [rsp + 0x56]
0x00086DE6: xor ecx, 0x62
0x00086DE9: inc ecx
0x00086DEB: mov byte ptr [rsp + 0x57], cl
0x00086DEF: movsx ecx, byte ptr [rsp + 0x57]
0x00086DF4: xor ecx, 0x6c
0x00086DF7: inc ecx
0x00086DF9: mov byte ptr [rsp + 0x58], cl
0x00086DFD: movsx ecx, byte ptr [rsp + 0x58]
0x00086E02: xor ecx, 0x65
0x00086E05: inc ecx
0x00086E07: mov byte ptr [rsp + 0x59], cl
0x00086E0B: movsx ecx, byte ptr [rsp + 0x59]
0x00086E10: xor ecx, 0x20
```
