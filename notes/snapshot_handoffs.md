# Snapshot handoff call contexts

## merge6_first near `0x0006FCC2` in `0x0006F940..0x000700E0`

```asm
0x0006FC61: movsd qword ptr [rbp + 0x144], xmm0
0x0006FC69: mov eax, dword ptr [rbp + 0x1c]
0x0006FC6C: mov dword ptr [rbp + 0x14c], eax
0x0006FC72: shr rdx, 0x20
0x0006FC76: mov dword ptr [rbp + 0x94], edx
0x0006FC7C: mov edx, dword ptr [rbp + 0x10c]
0x0006FC82: mov eax, dword ptr [rbp - 0x24]
0x0006FC85: test eax, eax
0x0006FC87: cmovg edx, eax
0x0006FC8A: mov dword ptr [rbp + 0x10c], edx
0x0006FC90: mov edx, dword ptr [rbp + 0x110]
0x0006FC96: mov eax, dword ptr [rbp - 0x20]
0x0006FC99: test eax, eax
0x0006FC9B: cmovg edx, eax
0x0006FC9E: mov dword ptr [rbp + 0x110], edx
0x0006FCA4: mov edx, dword ptr [rbp + 0x114]
0x0006FCAA: mov eax, dword ptr [rbp - 0x1c]
0x0006FCAD: test eax, eax
0x0006FCAF: cmovg edx, eax
0x0006FCB2: mov dword ptr [rbp + 0x114], edx
0x0006FCB8: lea rdx, [rbp + 0x90]
0x0006FCBF: mov rcx, r15
0x0006FCC2: call 0x1401362d0
0x0006FCC7: cmp qword ptr [r13 + 0x12a8], 0
0x0006FCCF: je 0x14006fce5
0x0006FCD1: mov r8d, dword ptr [rsp + 0x70]
0x0006FCD6: mov edx, r14d
0x0006FCD9: lea rcx, [r13 + 0x300]
0x0006FCE0: call 0x14013f7e0
0x0006FCE5: inc r14d
0x0006FCE8: test rsi, rsi
0x0006FCEB: je 0x14006fd18
0x0006FCED: or eax, 0xffffffff
0x0006FCF0: lock xadd dword ptr [rsi + 8], eax
0x0006FCF5: cmp eax, 1
0x0006FCF8: jne 0x14006fd18
0x0006FCFA: mov rax, qword ptr [rsi]
0x0006FCFD: mov rcx, rsi
0x0006FD00: call qword ptr [rax]
0x0006FD02: or eax, 0xffffffff
0x0006FD05: lock xadd dword ptr [rsi + 0xc], eax
0x0006FD0A: cmp eax, 1
0x0006FD0D: jne 0x14006fd18
0x0006FD0F: mov rax, qword ptr [rsi]
0x0006FD12: mov rcx, rsi
0x0006FD15: call qword ptr [rax + 8]
0x0006FD18: add rbx, 0x10
0x0006FD1C: cmp rbx, rdi
0x0006FD1F: jne 0x14006fa20
0x0006FD25: xor esi, esi
0x0006FD27: lea rdx, [rbp + 0x190]
0x0006FD2E: mov rcx, r13
```

## merge6_second near `0x0006FCE0` in `0x0006F940..0x000700E0`

```asm
0x0006FC82: mov eax, dword ptr [rbp - 0x24]
0x0006FC85: test eax, eax
0x0006FC87: cmovg edx, eax
0x0006FC8A: mov dword ptr [rbp + 0x10c], edx
0x0006FC90: mov edx, dword ptr [rbp + 0x110]
0x0006FC96: mov eax, dword ptr [rbp - 0x20]
0x0006FC99: test eax, eax
0x0006FC9B: cmovg edx, eax
0x0006FC9E: mov dword ptr [rbp + 0x110], edx
0x0006FCA4: mov edx, dword ptr [rbp + 0x114]
0x0006FCAA: mov eax, dword ptr [rbp - 0x1c]
0x0006FCAD: test eax, eax
0x0006FCAF: cmovg edx, eax
0x0006FCB2: mov dword ptr [rbp + 0x114], edx
0x0006FCB8: lea rdx, [rbp + 0x90]
0x0006FCBF: mov rcx, r15
0x0006FCC2: call 0x1401362d0
0x0006FCC7: cmp qword ptr [r13 + 0x12a8], 0
0x0006FCCF: je 0x14006fce5
0x0006FCD1: mov r8d, dword ptr [rsp + 0x70]
0x0006FCD6: mov edx, r14d
0x0006FCD9: lea rcx, [r13 + 0x300]
0x0006FCE0: call 0x14013f7e0
0x0006FCE5: inc r14d
0x0006FCE8: test rsi, rsi
0x0006FCEB: je 0x14006fd18
0x0006FCED: or eax, 0xffffffff
0x0006FCF0: lock xadd dword ptr [rsi + 8], eax
0x0006FCF5: cmp eax, 1
0x0006FCF8: jne 0x14006fd18
0x0006FCFA: mov rax, qword ptr [rsi]
0x0006FCFD: mov rcx, rsi
0x0006FD00: call qword ptr [rax]
0x0006FD02: or eax, 0xffffffff
0x0006FD05: lock xadd dword ptr [rsi + 0xc], eax
0x0006FD0A: cmp eax, 1
0x0006FD0D: jne 0x14006fd18
0x0006FD0F: mov rax, qword ptr [rsi]
0x0006FD12: mov rcx, rsi
0x0006FD15: call qword ptr [rax + 8]
0x0006FD18: add rbx, 0x10
0x0006FD1C: cmp rbx, rdi
0x0006FD1F: jne 0x14006fa20
0x0006FD25: xor esi, esi
0x0006FD27: lea rdx, [rbp + 0x190]
0x0006FD2E: mov rcx, r13
0x0006FD31: call 0x140127270
0x0006FD36: mov rcx, qword ptr [r13 + 0x15a0]
0x0006FD3D: test rcx, rcx
0x0006FD40: je 0x14006fd49
0x0006FD42: xor edx, edx
0x0006FD44: call 0x1400594c0
```

## copyback7 near `0x0007FD1D` in `0x0007F0F0..0x000831BB`

```asm
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
```

## after_mergeA near `0x000A92DF` in `0x000A8650..0x000A9414`

```asm
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
```

## after_mergeB near `0x000B24CB` in `0x000B20D0..0x000B251B`

```asm
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
