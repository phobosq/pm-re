# per-GPU snapshot propagation

Anchor accessor: `0x000E3F60`, record size/stride `0xD8`.

## callsite `0x0006FA51` in `0x0006F940..0x000700E0`

```asm
0x0006FA38: lea rdx, [rbp + 0x90]
0x0006FA3F: mov rcx, r15
0x0006FA42: call 0x140084a60
0x0006FA47: mov edx, r14d
0x0006FA4A: lea rcx, [rbp + 0x190]
0x0006FA51: call 0x1400e3f60
0x0006FA56: lea rcx, [rsp + 0x60]
0x0006FA5B: movups xmm0, xmmword ptr [rax]
0x0006FA5E: movups xmmword ptr [rcx], xmm0
0x0006FA61: movups xmm1, xmmword ptr [rax + 0x10]
0x0006FA65: movups xmmword ptr [rcx + 0x10], xmm1
0x0006FA69: movups xmm0, xmmword ptr [rax + 0x20]
0x0006FA6D: movups xmmword ptr [rcx + 0x20], xmm0
0x0006FA71: movups xmm1, xmmword ptr [rax + 0x30]
0x0006FA75: movups xmmword ptr [rcx + 0x30], xmm1
0x0006FA79: movups xmm0, xmmword ptr [rax + 0x40]
0x0006FA7D: movups xmmword ptr [rcx + 0x40], xmm0
0x0006FA81: movups xmm1, xmmword ptr [rax + 0x50]
0x0006FA85: movups xmmword ptr [rcx + 0x50], xmm1
0x0006FA89: movups xmm0, xmmword ptr [rax + 0x60]
0x0006FA8D: movups xmmword ptr [rcx + 0x60], xmm0
0x0006FA91: lea rcx, [rcx + 0x80]
0x0006FA98: movups xmm1, xmmword ptr [rax + 0x70]
0x0006FA9C: movups xmmword ptr [rcx - 0x10], xmm1
0x0006FAA0: sub rax, -0x80
0x0006FAA4: movups xmm0, xmmword ptr [rax]
0x0006FAA7: movups xmmword ptr [rcx], xmm0
0x0006FAAA: movups xmm1, xmmword ptr [rax + 0x10]
0x0006FAAE: movups xmmword ptr [rcx + 0x10], xmm1
0x0006FAB2: movups xmm0, xmmword ptr [rax + 0x20]
0x0006FAB6: movups xmmword ptr [rcx + 0x20], xmm0
0x0006FABA: movups xmm1, xmmword ptr [rax + 0x30]
0x0006FABE: movups xmmword ptr [rcx + 0x30], xmm1
0x0006FAC2: movups xmm0, xmmword ptr [rax + 0x40]
0x0006FAC6: movups xmmword ptr [rcx + 0x40], xmm0
0x0006FACA: mov rax, qword ptr [rax + 0x50]
0x0006FACE: mov qword ptr [rcx + 0x50], rax
0x0006FAD2: mov eax, dword ptr [rbp + 0x90]
0x0006FAD8: mov rdx, qword ptr [rsp + 0x60]
0x0006FADD: test edx, edx
0x0006FADF: cmovns eax, edx
0x0006FAE2: mov dword ptr [rbp + 0x90], eax
0x0006FAE8: mov rax, qword ptr [rsp + 0x78]
0x0006FAED: shr rax, 0x20
0x0006FAF1: mov dword ptr [rbp + 0xac], eax
0x0006FAF7: mov eax, dword ptr [rbp - 0x78]
0x0006FAFA: mov dword ptr [rbp + 0xb8], eax
0x0006FB00: mov eax, dword ptr [rbp + 0x98]
0x0006FB06: mov rcx, qword ptr [rsp + 0x68]
0x0006FB0B: test ecx, ecx
0x0006FB0D: cmovne eax, ecx
0x0006FB10: mov dword ptr [rbp + 0x98], eax
0x0006FB16: shr rcx, 0x20
0x0006FB1A: mov eax, dword ptr [rbp + 0x9c]
0x0006FB20: test ecx, ecx
0x0006FB22: cmovg eax, ecx
0x0006FB25: mov dword ptr [rbp + 0x9c], eax
0x0006FB2B: mov eax, dword ptr [rbp - 0x10]
0x0006FB2E: mov dword ptr [rbp + 0x120], eax
0x0006FB34: mov ecx, dword ptr [rbp + 0xd8]
0x0006FB3A: mov eax, dword ptr [rbp - 0x58]
0x0006FB3D: test eax, eax
0x0006FB3F: cmovns ecx, eax
0x0006FB42: mov dword ptr [rbp + 0xd8], ecx
0x0006FB48: mov ecx, dword ptr [rbp + 0xcc]
0x0006FB4E: mov eax, dword ptr [rbp - 0x64]
0x0006FB51: test eax, eax
0x0006FB53: cmovg ecx, eax
0x0006FB56: mov dword ptr [rbp + 0xcc], ecx
0x0006FB5C: mov ecx, dword ptr [rbp + 0xd0]
0x0006FB62: mov eax, dword ptr [rbp - 0x60]
0x0006FB65: test eax, eax
0x0006FB67: cmovg ecx, eax
0x0006FB6A: mov dword ptr [rbp + 0xd0], ecx
0x0006FB70: mov ecx, dword ptr [rbp + 0xd4]
0x0006FB76: mov eax, dword ptr [rbp - 0x5c]
0x0006FB79: test eax, eax
0x0006FB7B: cmovg ecx, eax
0x0006FB7E: mov dword ptr [rbp + 0xd4], ecx
0x0006FB84: mov ecx, dword ptr [rbp + 0xdc]
0x0006FB8A: mov eax, dword ptr [rbp - 0x54]
0x0006FB8D: test eax, eax
0x0006FB8F: cmovns ecx, eax
0x0006FB92: mov dword ptr [rbp + 0xdc], ecx
0x0006FB98: mov ecx, dword ptr [rbp + 0xe0]
0x0006FB9E: mov eax, dword ptr [rbp - 0x50]
0x0006FBA1: test eax, eax
0x0006FBA3: cmovns ecx, eax
0x0006FBA6: mov dword ptr [rbp + 0xe0], ecx
0x0006FBAC: mov eax, dword ptr [rbp - 0x38]
0x0006FBAF: mov dword ptr [rbp + 0xf8], eax
0x0006FBB5: mov ecx, dword ptr [rbp + 0x108]
0x0006FBBB: mov eax, dword ptr [rbp - 0x28]
0x0006FBBE: test eax, eax
0x0006FBC0: cmovg ecx, eax
0x0006FBC3: mov dword ptr [rbp + 0x108], ecx
0x0006FBC9: mov ecx, dword ptr [rbp + 0xe8]
0x0006FBCF: mov eax, dword ptr [rbp - 0x48]
0x0006FBD2: test eax, eax
0x0006FBD4: cmovg ecx, eax
0x0006FBD7: mov dword ptr [rbp + 0xe8], ecx
0x0006FBDD: mov ecx, dword ptr [rbp + 0xec]
0x0006FBE3: mov eax, dword ptr [rbp - 0x44]
0x0006FBE6: test eax, eax
0x0006FBE8: cmovne ecx, eax
```

### Calls after accessor

| RVA | target/form |
|---|---|
| `0x0006FCC2` | `RVA 0x001362D0` |
| `0x0006FCE0` | `RVA 0x0013F7E0` |
| `0x0006FD00` | `qword ptr [rax]` |
| `0x0006FD15` | `qword ptr [rax + 8]` |
| `0x0006FD31` | `RVA 0x00127270` |
| `0x0006FD44` | `RVA 0x000594C0` |
| `0x0006FF53` | `RVA 0x001A56A0` |
| `0x0006FF66` | `RVA 0x00062FF0` |

## callsite `0x0007FC7A` in `0x0007F0F0..0x000831BB`

```asm
0x0007FC68: shr rax, 0x3f
0x0007FC6C: add rdx, rax
0x0007FC6F: je 0x14007fd4a
0x0007FC75: mov edx, ebx
0x0007FC77: mov rcx, rsi
0x0007FC7A: call 0x1400e3f60
0x0007FC7F: cmp dword ptr [rax + 0x10], 0
0x0007FC83: je 0x14007fd22
0x0007FC89: lea rcx, [rsp + 0x870]
0x0007FC91: movups xmm0, xmmword ptr [rax]
0x0007FC94: movups xmmword ptr [rcx], xmm0
0x0007FC97: movups xmm1, xmmword ptr [rax + 0x10]
0x0007FC9B: movups xmmword ptr [rcx + 0x10], xmm1
0x0007FC9F: movups xmm0, xmmword ptr [rax + 0x20]
0x0007FCA3: movups xmmword ptr [rcx + 0x20], xmm0
0x0007FCA7: movups xmm1, xmmword ptr [rax + 0x30]
0x0007FCAB: movups xmmword ptr [rcx + 0x30], xmm1
0x0007FCAF: movups xmm0, xmmword ptr [rax + 0x40]
0x0007FCB3: movups xmmword ptr [rcx + 0x40], xmm0
0x0007FCB7: movups xmm1, xmmword ptr [rax + 0x50]
0x0007FCBB: movups xmmword ptr [rcx + 0x50], xmm1
0x0007FCBF: movups xmm0, xmmword ptr [rax + 0x60]
0x0007FCC3: movups xmmword ptr [rcx + 0x60], xmm0
0x0007FCC7: lea rcx, [rcx + 0x80]
0x0007FCCE: movups xmm1, xmmword ptr [rax + 0x70]
0x0007FCD2: movups xmmword ptr [rcx - 0x10], xmm1
0x0007FCD6: sub rax, -0x80
0x0007FCDA: movups xmm0, xmmword ptr [rax]
0x0007FCDD: movups xmmword ptr [rcx], xmm0
0x0007FCE0: movups xmm1, xmmword ptr [rax + 0x10]
0x0007FCE4: movups xmmword ptr [rcx + 0x10], xmm1
0x0007FCE8: movups xmm0, xmmword ptr [rax + 0x20]
0x0007FCEC: movups xmmword ptr [rcx + 0x20], xmm0
0x0007FCF0: movups xmm1, xmmword ptr [rax + 0x30]
0x0007FCF4: movups xmmword ptr [rcx + 0x30], xmm1
0x0007FCF8: movups xmm0, xmmword ptr [rax + 0x40]
0x0007FCFC: movups xmmword ptr [rcx + 0x40], xmm0
0x0007FD00: mov rax, qword ptr [rax + 0x50]
0x0007FD04: mov qword ptr [rcx + 0x50], rax
0x0007FD08: mov dword ptr [rsp + 0x880], r15d
0x0007FD10: lea r8, [rsp + 0x870]
0x0007FD18: mov edx, ebx
0x0007FD1A: mov rcx, rsi
0x0007FD1D: call 0x140123000
0x0007FD22: inc ebx
0x0007FD24: mov rcx, qword ptr [rdi + 8]
0x0007FD28: sub rcx, qword ptr [rdi]
0x0007FD2B: mov rax, r12
0x0007FD2E: imul rcx
0x0007FD31: sar rdx, 2
0x0007FD35: mov rax, rdx
0x0007FD38: shr rax, 0x3f
0x0007FD3C: add rdx, rax
0x0007FD3F: mov eax, ebx
0x0007FD41: cmp rax, rdx
0x0007FD44: jb 0x14007fc75
0x0007FD4A: cmp dword ptr [rsi + 0x1c4], 0
0x0007FD51: je 0x14007fda5
0x0007FD53: mov ecx, 0xc8
0x0007FD58: call 0x1403b2098
0x0007FD5D: mov qword ptr [rsp + 0x70], rax
0x0007FD62: test rax, rax
0x0007FD65: je 0x14007fd7a
0x0007FD67: xor r8d, r8d
0x0007FD6A: mov edx, dword ptr [rsi + 0x1c4]
0x0007FD70: mov rcx, rax
0x0007FD73: call 0x140032960
0x0007FD78: jmp 0x14007fd7d
0x0007FD7A: mov rax, r15
0x0007FD7D: mov rbx, qword ptr [rsi + 0x1668]
0x0007FD84: mov qword ptr [rsi + 0x1668], rax
0x0007FD8B: test rbx, rbx
0x0007FD8E: je 0x14007fda5
0x0007FD90: mov rcx, rbx
0x0007FD93: call 0x140033240
0x0007FD98: mov edx, 0xc8
0x0007FD9D: mov rcx, rbx
0x0007FDA0: call 0x1403b20dc
0x0007FDA5: mov dword ptr [rsp + 0x578], 0x61
0x0007FDB0: mov eax, dword ptr [rsp + 0x578]
0x0007FDB7: add al, 0x61
0x0007FDB9: movsx ecx, al
0x0007FDBC: xor ecx, 0x21
0x0007FDBF: mov dword ptr [rsp + 0x57c], ecx
0x0007FDC6: mov eax, dword ptr [rsp + 0x57c]
0x0007FDCD: mov ecx, dword ptr [rsp + 0x578]
0x0007FDD4: xor ecx, eax
0x0007FDD6: xor ecx, 0x53
0x0007FDD9: mov byte ptr [rsp + 0x580], cl
0x0007FDE0: movsx ecx, byte ptr [rsp + 0x580]
0x0007FDE8: mov eax, dword ptr [rsp + 0x578]
0x0007FDEF: inc al
0x0007FDF1: xor eax, ecx
0x0007FDF3: xor eax, 0x74
0x0007FDF6: mov byte ptr [rsp + 0x581], al
0x0007FDFD: movsx ecx, byte ptr [rsp + 0x581]
0x0007FE05: mov eax, dword ptr [rsp + 0x578]
0x0007FE0C: add al, 2
0x0007FE0E: xor eax, ecx
0x0007FE10: xor eax, 0x61
0x0007FE13: mov byte ptr [rsp + 0x582], al
0x0007FE1A: movsx ecx, byte ptr [rsp + 0x582]
0x0007FE22: mov eax, dword ptr [rsp + 0x578]
0x0007FE29: add al, 3
0x0007FE2B: xor eax, ecx
```

### Calls after accessor

| RVA | target/form |
|---|---|
| `0x0007FD1D` | `RVA 0x00123000` |
| `0x0007FD58` | `RVA 0x003B2098` |
| `0x0007FD73` | `RVA 0x00032960` |
| `0x0007FD93` | `RVA 0x00033240` |
| `0x0007FDA0` | `RVA 0x003B20DC` |
| `0x0008000B` | `RVA 0x00056320` |
| `0x0008001E` | `RVA 0x00063150` |
| `0x00080045` | `RVA 0x00046AB0` |

## callsite `0x000A9247` in `0x000A8650..0x000A9414`

```asm
0x000A9233: call 0x1400e3f60
0x000A9238: cmp dword ptr [rax + 0x2c], 0
0x000A923C: jge 0x1400a92df
0x000A9242: mov edx, edi
0x000A9244: mov rcx, rsi
0x000A9247: call 0x1400e3f60
0x000A924C: lea rcx, [rbp + 0x70]
0x000A9250: movups xmm0, xmmword ptr [rax]
0x000A9253: movups xmmword ptr [rcx], xmm0
0x000A9256: movups xmm1, xmmword ptr [rax + 0x10]
0x000A925A: movups xmmword ptr [rcx + 0x10], xmm1
0x000A925E: movups xmm0, xmmword ptr [rax + 0x20]
0x000A9262: movups xmmword ptr [rcx + 0x20], xmm0
0x000A9266: movups xmm1, xmmword ptr [rax + 0x30]
0x000A926A: movups xmmword ptr [rcx + 0x30], xmm1
0x000A926E: movups xmm0, xmmword ptr [rax + 0x40]
0x000A9272: movups xmmword ptr [rcx + 0x40], xmm0
0x000A9276: movups xmm1, xmmword ptr [rax + 0x50]
0x000A927A: movups xmmword ptr [rcx + 0x50], xmm1
0x000A927E: movups xmm0, xmmword ptr [rax + 0x60]
0x000A9282: movups xmmword ptr [rcx + 0x60], xmm0
0x000A9286: lea rcx, [rcx + 0x80]
0x000A928D: movups xmm1, xmmword ptr [rax + 0x70]
0x000A9291: movups xmmword ptr [rcx - 0x10], xmm1
0x000A9295: sub rax, -0x80
0x000A9299: movups xmm0, xmmword ptr [rax]
0x000A929C: movups xmmword ptr [rcx], xmm0
0x000A929F: movups xmm1, xmmword ptr [rax + 0x10]
0x000A92A3: movups xmmword ptr [rcx + 0x10], xmm1
0x000A92A7: movups xmm0, xmmword ptr [rax + 0x20]
0x000A92AB: movups xmmword ptr [rcx + 0x20], xmm0
0x000A92AF: movups xmm1, xmmword ptr [rax + 0x30]
0x000A92B3: movups xmmword ptr [rcx + 0x30], xmm1
0x000A92B7: movups xmm0, xmmword ptr [rax + 0x40]
0x000A92BB: movups xmmword ptr [rcx + 0x40], xmm0
0x000A92BF: mov rax, qword ptr [rax + 0x50]
0x000A92C3: mov qword ptr [rcx + 0x50], rax
0x000A92C7: mov dword ptr [rbp + 0x9c], 1
0x000A92D1: lea r8, [rbp + 0x70]
0x000A92D5: mov edx, edi
0x000A92D7: mov rcx, rsi
0x000A92DA: call 0x140123000
0x000A92DF: inc edi
0x000A92E1: add r15, 0xa8
0x000A92E8: mov rcx, qword ptr [rsp + 0x30]
0x000A92ED: mov r8, qword ptr [rsp + 0x28]
0x000A92F2: sub rcx, r8
0x000A92F5: movabs r14, 0xc30c30c30c30c30d
0x000A92FF: mov rax, r14
0x000A9302: imul rcx
0x000A9305: add rdx, rcx
0x000A9308: sar rdx, 7
0x000A930C: mov rax, rdx
0x000A930F: shr rax, 0x3f
0x000A9313: add rdx, rax
0x000A9316: cmp edi, edx
0x000A9318: lea rax, [rsi + 0x300]
0x000A931F: jl 0x1400a91f0
0x000A9325: test r13b, r13b
0x000A9328: je 0x1400a933d
0x000A932A: test r12b, r12b
0x000A932D: jne 0x1400a9350
0x000A932F: mov dword ptr [rsi + 0x31c], 1
0x000A9339: xor edi, edi
0x000A933B: jmp 0x1400a9358
0x000A933D: test r12b, r12b
0x000A9340: je 0x1400a9350
0x000A9342: mov dword ptr [rsi + 0x31c], 2
0x000A934C: xor edi, edi
0x000A934E: jmp 0x1400a9358
0x000A9350: xor edi, edi
0x000A9352: mov dword ptr [rsi + 0x31c], edi
0x000A9358: lea rcx, [rsi + 0x300]
0x000A935F: call 0x140134a40
0x000A9364: mov bl, 1
0x000A9366: mov rdx, qword ptr [rsp + 0x70]
0x000A936B: test rdx, rdx
0x000A936E: je 0x1400a9392
0x000A9370: mov r8, qword ptr [rbp - 0x80]
0x000A9374: sub r8, rdx
0x000A9377: sar r8, 2
0x000A937B: lea rcx, [rsp + 0x70]
0x000A9380: call 0x14006f4d0
0x000A9385: xorps xmm0, xmm0
0x000A9388: movdqu xmmword ptr [rsp + 0x70], xmm0
0x000A938E: mov qword ptr [rbp - 0x80], rdi
0x000A9392: mov rcx, qword ptr [rsp + 0x28]
0x000A9397: test rcx, rcx
0x000A939A: je 0x1400a93e1
0x000A939C: movzx r9d, byte ptr [rsp + 0x20]
0x000A93A2: lea r8, [rsp + 0x28]
0x000A93A7: mov rdx, qword ptr [rsp + 0x30]
0x000A93AC: call 0x140094bf0
0x000A93B1: mov rcx, qword ptr [rsp + 0x38]
0x000A93B6: sub rcx, qword ptr [rsp + 0x28]
0x000A93BB: mov rax, r14
0x000A93BE: imul rcx
0x000A93C1: add rdx, rcx
0x000A93C4: sar rdx, 7
0x000A93C8: mov r8, rdx
0x000A93CB: shr r8, 0x3f
0x000A93CF: add r8, rdx
0x000A93D2: mov rdx, qword ptr [rsp + 0x28]
0x000A93D7: lea rcx, [rsp + 0x28]
0x000A93DC: call 0x1400a2710
```

### Calls after accessor

| RVA | target/form |
|---|---|
| `0x000A92DA` | `RVA 0x00123000` |
| `0x000A935F` | `RVA 0x00134A40` |
| `0x000A9380` | `RVA 0x0006F4D0` |
| `0x000A93AC` | `RVA 0x00094BF0` |
| `0x000A93DC` | `RVA 0x000A2710` |
| `0x000A93EE` | `RVA 0x003B24C0` |

## callsite `0x000B2426` in `0x000B20D0..0x000B251B`

```asm
0x000B2414: shr rax, 0x3f
0x000B2418: add rdx, rax
0x000B241B: je 0x1400b24fa
0x000B2421: mov edx, edi
0x000B2423: mov rcx, rbx
0x000B2426: call 0x1400e3f60
0x000B242B: cmp dword ptr [rax + 0x10], 0
0x000B242F: je 0x1400b24cb
0x000B2435: lea rdx, [rbp + 0xd0]
0x000B243C: movups xmm0, xmmword ptr [rax]
0x000B243F: movups xmmword ptr [rdx], xmm0
0x000B2442: movups xmm1, xmmword ptr [rax + 0x10]
0x000B2446: movups xmmword ptr [rdx + 0x10], xmm1
0x000B244A: movups xmm0, xmmword ptr [rax + 0x20]
0x000B244E: movups xmmword ptr [rdx + 0x20], xmm0
0x000B2452: movups xmm1, xmmword ptr [rax + 0x30]
0x000B2456: movups xmmword ptr [rdx + 0x30], xmm1
0x000B245A: movups xmm0, xmmword ptr [rax + 0x40]
0x000B245E: movups xmmword ptr [rdx + 0x40], xmm0
0x000B2462: movups xmm1, xmmword ptr [rax + 0x50]
0x000B2466: movups xmmword ptr [rdx + 0x50], xmm1
0x000B246A: movups xmm0, xmmword ptr [rax + 0x60]
0x000B246E: movups xmmword ptr [rdx + 0x60], xmm0
0x000B2472: lea rdx, [rdx + 0x80]
0x000B2479: movups xmm1, xmmword ptr [rax + 0x70]
0x000B247D: movups xmmword ptr [rdx - 0x10], xmm1
0x000B2481: sub rax, -0x80
0x000B2485: movups xmm0, xmmword ptr [rax]
0x000B2488: movups xmmword ptr [rdx], xmm0
0x000B248B: movups xmm1, xmmword ptr [rax + 0x10]
0x000B248F: movups xmmword ptr [rdx + 0x10], xmm1
0x000B2493: movups xmm0, xmmword ptr [rax + 0x20]
0x000B2497: movups xmmword ptr [rdx + 0x20], xmm0
0x000B249B: movups xmm1, xmmword ptr [rax + 0x30]
0x000B249F: movups xmmword ptr [rdx + 0x30], xmm1
0x000B24A3: movups xmm0, xmmword ptr [rax + 0x40]
0x000B24A7: movups xmmword ptr [rdx + 0x40], xmm0
0x000B24AB: mov rcx, qword ptr [rax + 0x50]
0x000B24AF: mov qword ptr [rdx + 0x50], rcx
0x000B24B3: mov dword ptr [rbp + 0xe0], r12d
0x000B24BA: lea r8, [rbp + 0xd0]
0x000B24C1: mov edx, edi
0x000B24C3: mov rcx, rbx
0x000B24C6: call 0x140123000
0x000B24CB: inc edi
0x000B24CD: mov rcx, qword ptr [rbx + 0x2c8]
0x000B24D4: sub rcx, qword ptr [rbx + 0x2c0]
0x000B24DB: mov rax, rsi
0x000B24DE: imul rcx
0x000B24E1: sar rdx, 2
0x000B24E5: mov rax, rdx
0x000B24E8: shr rax, 0x3f
0x000B24EC: add rdx, rax
0x000B24EF: mov eax, edi
0x000B24F1: cmp rax, rdx
0x000B24F4: jb 0x1400b2421
0x000B24FA: mov rcx, qword ptr [rbp + 0x1b0]
0x000B2501: xor rcx, rsp
0x000B2504: call 0x1403b24c0
0x000B2509: add rsp, 0x2c0
0x000B2510: pop r15
0x000B2512: pop r14
0x000B2514: pop r12
0x000B2516: pop rdi
0x000B2517: pop rsi
0x000B2518: pop rbx
0x000B2519: pop rbp
0x000B251A: ret
```

### Calls after accessor

| RVA | target/form |
|---|---|
| `0x000B24C6` | `RVA 0x00123000` |
| `0x000B2504` | `RVA 0x003B24C0` |
