# Runtime object constructor family

Strong type seed: `0x12F250` touches +0x318, +0x368, +0x440 and +0x538.

## target `0x0012F250` PDATA `0x0012F250..0x0012F86D`

```asm
0x0012F250: push rbp
0x0012F252: push rsi
0x0012F253: push rdi
0x0012F254: push r14
0x0012F256: push r15
0x0012F258: lea rbp, [rsp - 0x37]
0x0012F25D: sub rsp, 0x90
0x0012F264: mov qword ptr [rbp - 0x31], 0xfffffffffffffffe
0x0012F26C: mov qword ptr [rsp + 0xc8], rbx
0x0012F274: mov rax, qword ptr [rip + 0x6a7675]
0x0012F27B: xor rax, rsp
0x0012F27E: mov qword ptr [rbp + 0x2f], rax
0x0012F282: mov rsi, r9
0x0012F285: mov ebx, r8d
0x0012F288: mov r14, rdx
0x0012F28B: mov rdi, rcx
0x0012F28E: mov qword ptr [rbp - 0x29], rcx
0x0012F292: mov ecx, dword ptr [rip + 0x660768]
0x0012F298: add ecx, r8d
0x0012F29B: mov dword ptr [rbp - 0x39], ecx
0x0012F29E: mov dword ptr [rbp - 0x21], 0x5b
0x0012F2A5: mov dword ptr [rbp - 0x1d], 0x69
0x0012F2AC: mov eax, dword ptr [rbp - 0x1d]
0x0012F2AF: xor eax, 0x1c
0x0012F2B2: mov byte ptr [rbp - 0x19], al
0x0012F2B5: movsx ecx, byte ptr [rbp - 0x19]
0x0012F2B9: xor ecx, 0xb
0x0012F2BC: mov byte ptr [rbp - 0x18], cl
0x0012F2BF: movsx ecx, byte ptr [rbp - 0x18]
0x0012F2C3: xor ecx, 0xe
0x0012F2C6: mov byte ptr [rbp - 0x17], cl
0x0012F2C9: movsx ecx, byte ptr [rbp - 0x17]
0x0012F2CD: xor ecx, 0x20
0x0012F2D0: mov byte ptr [rbp - 0x16], cl
0x0012F2D3: movsx ecx, byte ptr [rbp - 0x16]
0x0012F2D7: xor ecx, 0x26
0x0012F2DA: mov byte ptr [rbp - 0x15], cl
0x0012F2DD: xor eax, eax
0x0012F2DF: mov byte ptr [rbp - 0x14], al
0x0012F2E2: movzx eax, byte ptr [rbp - 0x19]
0x0012F2E6: lea rdx, [rbp + 0xf]
0x0012F2EA: lea rcx, [rbp - 0x21]
0x0012F2EE: call 0x14005ca20
0x0012F2F3: nop
0x0012F2F4: cmp qword ptr [rax + 0x18], 0x10
0x0012F2F9: jb 0x14012f2fe
0x0012F2FB: mov rax, qword ptr [rax]
0x0012F2FE: lea r8, [rbp - 0x39]
0x0012F302: mov rdx, rax
0x0012F305: lea rcx, [rbp - 0x11]
0x0012F309: call 0x14003f680
0x0012F30E: nop
0x0012F30F: lea rcx, [rip + 0x311212]
0x0012F316: mov qword ptr [rdi], rcx
0x0012F319: lea rcx, [rdi + 8]
0x0012F31D: mov qword ptr [rcx + 0x18], 0xf
0x0012F325: xor r15d, r15d
0x0012F328: mov qword ptr [rcx + 0x10], r15
0x0012F32C: cmp qword ptr [rcx + 0x18], 0x10
0x0012F331: jb 0x14012f338
0x0012F333: mov rdx, qword ptr [rcx]
0x0012F336: jmp 0x14012f33b
0x0012F338: mov rdx, rcx
0x0012F33B: mov byte ptr [rdx], r15b
0x0012F33E: or r9, 0xffffffffffffffff
0x0012F342: xor r8d, r8d
0x0012F345: mov rdx, rax
0x0012F348: call 0x1400354b0
0x0012F34D: mov dword ptr [rdi + 0x28], 0x1e
0x0012F354: lea rcx, [rdi + 0x30]
0x0012F358: mov edx, 2
0x0012F35D: call 0x140391a94
0x0012F362: mov qword ptr [rdi + 0x80], r15
0x0012F369: mov dword ptr [rdi + 0x88], r15d
0x0012F370: mov rax, qword ptr [rbp + 7]
0x0012F374: cmp rax, 0x10
0x0012F378: jb 0x14012f3c6
0x0012F37A: inc rax
0x0012F37D: mov rcx, qword ptr [rbp - 0x11]
0x0012F381: cmp rax, 0x1000
0x0012F387: jb 0x14012f3c1
0x0012F389: test cl, 0x1f
0x0012F38C: je 0x14012f394
0x0012F38E: call 0x1403db020
0x0012F393: int3
0x0012F394: mov rax, qword ptr [rcx - 8]
0x0012F398: cmp rax, rcx
0x0012F39B: jb 0x14012f3a3
0x0012F39D: call 0x1403db020
0x0012F3A2: int3
0x0012F3A3: sub rcx, rax
0x0012F3A6: cmp rcx, 8
0x0012F3AA: jae 0x14012f3b2
0x0012F3AC: call 0x1403db020
0x0012F3B1: int3
0x0012F3B2: cmp rcx, 0x27
0x0012F3B6: jbe 0x14012f3be
0x0012F3B8: call 0x1403db020
0x0012F3BD: int3
0x0012F3BE: mov rcx, rax
0x0012F3C1: call 0x1403b20d4
0x0012F3C6: mov qword ptr [rbp + 7], 0xf
0x0012F3CE: mov qword ptr [rbp - 1], r15
0x0012F3D2: mov byte ptr [rbp - 0x11], 0
0x0012F3D6: mov rax, qword ptr [rbp + 0x27]
0x0012F3DA: cmp rax, 0x10
0x0012F3DE: jb 0x14012f42c
0x0012F3E0: inc rax
0x0012F3E3: mov rcx, qword ptr [rbp + 0xf]
0x0012F3E7: cmp rax, 0x1000
0x0012F3ED: jb 0x14012f427
0x0012F3EF: test cl, 0x1f
0x0012F3F2: je 0x14012f3fa
0x0012F3F4: call 0x1403db020
0x0012F3F9: int3
0x0012F3FA: mov rax, qword ptr [rcx - 8]
0x0012F3FE: cmp rax, rcx
0x0012F401: jb 0x14012f409
0x0012F403: call 0x1403db020
0x0012F408: int3
0x0012F409: sub rcx, rax
0x0012F40C: cmp rcx, 8
0x0012F410: jae 0x14012f418
0x0012F412: call 0x1403db020
0x0012F417: int3
0x0012F418: cmp rcx, 0x27
0x0012F41C: jbe 0x14012f424
0x0012F41E: call 0x1403db020
0x0012F423: int3
0x0012F424: mov rcx, rax
0x0012F427: call 0x1403b20d4
0x0012F42C: lea rax, [rip + 0x31112d]
0x0012F433: mov qword ptr [rdi], rax
0x0012F436: mov qword ptr [rdi + 0x90], r14
0x0012F43D: mov dword ptr [rdi + 0x98], ebx
0x0012F443: mov word ptr [rdi + 0x9c], 0x100
0x0012F44C: mov dword ptr [rdi + 0xa0], r15d
0x0012F453: lea rcx, [rdi + 0xa8]
0x0012F45A: mov edx, 2
0x0012F45F: call 0x140391a94
0x0012F464: nop
0x0012F465: xor eax, eax
0x0012F467: mov qword ptr [rdi + 0xf8], rax
0x0012F46E: mov qword ptr [rdi + 0x100], rax
0x0012F475: mov qword ptr [rdi + 0x108], rax
0x0012F47C: mov qword ptr [rdi + 0x110], rax
0x0012F483: mov qword ptr [rdi + 0x118], rax
0x0012F48A: mov qword ptr [rdi + 0x120], rax
0x0012F491: mov qword ptr [rdi + 0x128], rax
0x0012F498: mov qword ptr [rdi + 0x130], rax
0x0012F49F: mov qword ptr [rdi + 0x138], rax
0x0012F4A6: mov qword ptr [rdi + 0x140], rax
0x0012F4AD: mov qword ptr [rdi + 0x148], rax
0x0012F4B4: mov qword ptr [rdi + 0x150], rax
0x0012F4BB: mov qword ptr [rdi + 0x158], r15
0x0012F4C2: mov dword ptr [rdi + 0x160], 0xffffffff
0x0012F4CC: mov qword ptr [rdi + 0x168], r15
0x0012F4D3: mov dword ptr [rdi + 0x170], r15d
0x0012F4DA: mov qword ptr [rdi + 0x180], r15
0x0012F4E1: mov qword ptr [rdi + 0x188], r15
0x0012F4E8: mov qword ptr [rdi + 0x190], r15
0x0012F4EF: mov qword ptr [rdi + 0x1a0], r15
0x0012F4F6: mov qword ptr [rdi + 0x1a8], r15
0x0012F4FD: mov qword ptr [rdi + 0x1b0], r15
0x0012F504: mov qword ptr [rdi + 0x1b8], rax
0x0012F50B: mov dword ptr [rdi + 0x1c0], eax
0x0012F511: mov dword ptr [rdi + 0x178], r15d
0x0012F518: mov dword ptr [rdi + 0x198], r15d
0x0012F51F: lea rcx, [rdi + 0x1d8]
0x0012F526: lea edx, [rax + 2]
0x0012F529: call 0x140391a94
0x0012F52E: nop
0x0012F52F: xor eax, eax
0x0012F531: mov qword ptr [rdi + 0x228], rax
0x0012F538: mov qword ptr [rdi + 0x230], rax
0x0012F53F: mov qword ptr [rdi + 0x238], rax
0x0012F546: mov qword ptr [rdi + 0x240], rax
0x0012F54D: mov qword ptr [rdi + 0x248], rax
0x0012F554: mov qword ptr [rdi + 0x250], rax
0x0012F55B: mov qword ptr [rdi + 0x258], rax
0x0012F562: mov qword ptr [rdi + 0x260], rax
0x0012F569: mov qword ptr [rdi + 0x268], rax
0x0012F570: mov qword ptr [rdi + 0x270], rax
0x0012F577: mov qword ptr [rdi + 0x278], rax
0x0012F57E: mov qword ptr [rdi + 0x280], rax
0x0012F585: mov qword ptr [rdi + 0x288], r15
0x0012F58C: mov dword ptr [rdi + 0x290], 0xffffffff
0x0012F596: mov qword ptr [rdi + 0x298], r15
0x0012F59D: mov dword ptr [rdi + 0x2a0], r15d
0x0012F5A4: mov qword ptr [rdi + 0x2b0], r15
0x0012F5AB: mov qword ptr [rdi + 0x2b8], r15
0x0012F5B2: mov qword ptr [rdi + 0x2c0], r15
0x0012F5B9: mov qword ptr [rdi + 0x2d0], r15
0x0012F5C0: mov qword ptr [rdi + 0x2d8], r15
0x0012F5C7: mov qword ptr [rdi + 0x2e0], r15
0x0012F5CE: mov qword ptr [rdi + 0x2e8], rax
0x0012F5D5: mov dword ptr [rdi + 0x2f0], eax
0x0012F5DB: mov dword ptr [rdi + 0x2a8], r15d
0x0012F5E2: mov dword ptr [rdi + 0x2c8], r15d
0x0012F5E9: mov byte ptr [rdi + 0x310], al
0x0012F5EF: lea rcx, [rdi + 0x318]
0x0012F5F6: lea edx, [rax + 2]
0x0012F5F9: call 0x140391a94
0x0012F5FE: nop
0x0012F5FF: lea rcx, [rdi + 0x368]
0x0012F606: movups xmm0, xmmword ptr [rsi]
0x0012F609: movups xmmword ptr [rcx], xmm0
0x0012F60C: movups xmm1, xmmword ptr [rsi + 0x10]
0x0012F610: movups xmmword ptr [rcx + 0x10], xmm1
0x0012F614: movups xmm0, xmmword ptr [rsi + 0x20]
0x0012F618: movups xmmword ptr [rcx + 0x20], xmm0
0x0012F61C: movups xmm1, xmmword ptr [rsi + 0x30]
0x0012F620: movups xmmword ptr [rcx + 0x30], xmm1
0x0012F624: movups xmm0, xmmword ptr [rsi + 0x40]
0x0012F628: movups xmmword ptr [rcx + 0x40], xmm0
0x0012F62C: movups xmm1, xmmword ptr [rsi + 0x50]
0x0012F630: movups xmmword ptr [rcx + 0x50], xmm1
0x0012F634: movups xmm0, xmmword ptr [rsi + 0x60]
0x0012F638: movups xmmword ptr [rcx + 0x60], xmm0
0x0012F63C: lea rcx, [rcx + 0x80]
0x0012F643: movups xmm0, xmmword ptr [rsi + 0x70]
0x0012F647: movups xmmword ptr [rcx - 0x10], xmm0
0x0012F64B: lea rax, [rsi + 0x80]
0x0012F652: movups xmm1, xmmword ptr [rax]
0x0012F655: movups xmmword ptr [rcx], xmm1
0x0012F658: movups xmm0, xmmword ptr [rax + 0x10]
0x0012F65C: movups xmmword ptr [rcx + 0x10], xmm0
0x0012F660: movups xmm1, xmmword ptr [rax + 0x20]
0x0012F664: movups xmmword ptr [rcx + 0x20], xmm1
0x0012F668: movups xmm0, xmmword ptr [rax + 0x30]
0x0012F66C: movups xmmword ptr [rcx + 0x30], xmm0
0x0012F670: movups xmm1, xmmword ptr [rax + 0x40]
0x0012F674: movups xmmword ptr [rcx + 0x40], xmm1
0x0012F678: mov rax, qword ptr [rax + 0x50]
0x0012F67C: mov qword ptr [rcx + 0x50], rax
0x0012F680: lea rcx, [rdi + 0x440]
0x0012F687: movups xmm0, xmmword ptr [rsi]
0x0012F68A: movups xmmword ptr [rcx], xmm0
0x0012F68D: movups xmm1, xmmword ptr [rsi + 0x10]
0x0012F691: movups xmmword ptr [rcx + 0x10], xmm1
0x0012F695: movups xmm0, xmmword ptr [rsi + 0x20]
0x0012F699: movups xmmword ptr [rcx + 0x20], xmm0
0x0012F69D: movups xmm1, xmmword ptr [rsi + 0x30]
0x0012F6A1: movups xmmword ptr [rcx + 0x30], xmm1
0x0012F6A5: movups xmm0, xmmword ptr [rsi + 0x40]
0x0012F6A9: movups xmmword ptr [rcx + 0x40], xmm0
0x0012F6AD: movups xmm1, xmmword ptr [rsi + 0x50]
0x0012F6B1: movups xmmword ptr [rcx + 0x50], xmm1
0x0012F6B5: movups xmm0, xmmword ptr [rsi + 0x60]
0x0012F6B9: movups xmmword ptr [rcx + 0x60], xmm0
0x0012F6BD: lea rcx, [rcx + 0x80]
0x0012F6C4: movups xmm1, xmmword ptr [rsi + 0x70]
0x0012F6C8: movups xmmword ptr [rcx - 0x10], xmm1
0x0012F6CC: sub rsi, -0x80
0x0012F6D0: movups xmm0, xmmword ptr [rsi]
0x0012F6D3: movups xmmword ptr [rcx], xmm0
0x0012F6D6: movups xmm1, xmmword ptr [rsi + 0x10]
0x0012F6DA: movups xmmword ptr [rcx + 0x10], xmm1
0x0012F6DE: movups xmm0, xmmword ptr [rsi + 0x20]
0x0012F6E2: movups xmmword ptr [rcx + 0x20], xmm0
0x0012F6E6: movups xmm1, xmmword ptr [rsi + 0x30]
0x0012F6EA: movups xmmword ptr [rcx + 0x30], xmm1
0x0012F6EE: movups xmm0, xmmword ptr [rsi + 0x40]
0x0012F6F2: movups xmmword ptr [rcx + 0x40], xmm0
0x0012F6F6: mov rax, qword ptr [rsi + 0x50]
0x0012F6FA: mov qword ptr [rcx + 0x50], rax
0x0012F6FE: lea rbx, [rdi + 0x518]
0x0012F705: mov qword ptr [rbp - 0x39], rbx
0x0012F709: mov qword ptr [rbx], r15
0x0012F70C: mov qword ptr [rbx + 8], r15
0x0012F710: mov rcx, rbx
0x0012F713: call 0x14012ffb0
0x0012F718: mov qword ptr [rbx], rax
0x0012F71B: lea rbx, [rdi + 0x528]
0x0012F722: mov qword ptr [rbp - 0x39], rbx
0x0012F726: mov qword ptr [rbx], r15
0x0012F729: mov qword ptr [rbx + 8], r15
0x0012F72D: mov rcx, rbx
0x0012F730: call 0x14012ffb0
0x0012F735: mov qword ptr [rbx], rax
0x0012F738: mov qword ptr [rdi + 0x538], r15
0x0012F73F: mov dword ptr [rdi + 0x540], 0
0x0012F749: mov word ptr [rdi + 0x544], 0
0x0012F752: mov byte ptr [rdi + 0x546], 0
0x0012F759: mov qword ptr [rdi + 0x548], r15
0x0012F760: mov word ptr [rdi + 0x550], 0
0x0012F769: lea rcx, [rdi + 0x558]
0x0012F770: mov edx, 2
0x0012F775: call 0x140391a94
0x0012F77A: nop
0x0012F77B: mov byte ptr [rdi + 0x5a8], 0
0x0012F782: mov edx, 2
0x0012F787: lea rcx, [rdi + 0x5b0]
0x0012F78E: call 0x140391a94
0x0012F793: lea rcx, [rdi + 0x600]
0x0012F79A: call 0x140391e84
0x0012F79F: mov byte ptr [rdi + 0x648], 1
0x0012F7A6: mov qword ptr [rdi + 0x650], r15
0x0012F7AD: mov dword ptr [rdi + 0x658], r15d
0x0012F7B4: lea rcx, [rdi + 0x660]
0x0012F7BB: mov edx, 2
0x0012F7C0: call 0x140391a94
0x0012F7C5: nop
0x0012F7C6: lea rcx, [rdi + 0x6b0]
0x0012F7CD: call 0x140391e84
0x0012F7D2: nop
0x0012F7D3: mov word ptr [rdi + 0x718], 0x100
0x0012F7DC: lea rax, [rdi + 0x720]
0x0012F7E3: mov qword ptr [rax + 0x18], 0xf
0x0012F7EB: mov qword ptr [rax + 0x10], r15
0x0012F7EF: cmp qword ptr [rax + 0x18], 0x10
0x0012F7F4: jb 0x14012f7f9
0x0012F7F6: mov rax, qword ptr [rax]
0x0012F7F9: mov byte ptr [rax], 0
0x0012F7FC: mov qword ptr [rdi + 0x740], r15
0x0012F803: mov qword ptr [rdi + 0x748], r15
0x0012F80A: lea rcx, [rdi + 0x750]
0x0012F811: mov edx, 2
0x0012F816: call 0x140391a94
0x0012F81B: nop
0x0012F81C: mov dword ptr [rdi + 0x7a0], r15d
0x0012F823: lea rbx, [rdi + 0x7a8]
0x0012F82A: mov qword ptr [rbp - 0x39], rbx
0x0012F82E: mov qword ptr [rbx], r15
0x0012F831: mov qword ptr [rbx + 8], r15
0x0012F835: mov rcx, rbx
0x0012F838: call 0x14012ff50
0x0012F83D: mov qword ptr [rbx], rax
0x0012F840: mov qword ptr [rdi + 0x7b8], r15
0x0012F847: mov rax, rdi
0x0012F84A: mov rcx, qword ptr [rbp + 0x2f]
0x0012F84E: xor rcx, rsp
0x0012F851: call 0x1403b24c0
0x0012F856: mov rbx, qword ptr [rsp + 0xc8]
0x0012F85E: add rsp, 0x90
0x0012F865: pop r15
0x0012F867: pop r14
0x0012F869: pop rdi
0x0012F86A: pop rsi
0x0012F86B: pop rbp
0x0012F86C: ret
```

### Object-relative memory operands

- `0x0012F26C` disp `+0xC8`: `mov qword ptr [rsp + 0xc8], rbx`
- `0x0012F27E` disp `+0x2F`: `mov qword ptr [rbp + 0x2f], rax`
- `0x0012F2E6` disp `+0xF`: `lea rdx, [rbp + 0xf]`
- `0x0012F2F4` disp `+0x18`: `cmp qword ptr [rax + 0x18], 0x10`
- `0x0012F2FB` disp `+0x0`: `mov rax, qword ptr [rax]`
- `0x0012F316` disp `+0x0`: `mov qword ptr [rdi], rcx`
- `0x0012F319` disp `+0x8`: `lea rcx, [rdi + 8]`
- `0x0012F31D` disp `+0x18`: `mov qword ptr [rcx + 0x18], 0xf`
- `0x0012F328` disp `+0x10`: `mov qword ptr [rcx + 0x10], r15`
- `0x0012F32C` disp `+0x18`: `cmp qword ptr [rcx + 0x18], 0x10`
- `0x0012F333` disp `+0x0`: `mov rdx, qword ptr [rcx]`
- `0x0012F33B` disp `+0x0`: `mov byte ptr [rdx], r15b`
- `0x0012F34D` disp `+0x28`: `mov dword ptr [rdi + 0x28], 0x1e`
- `0x0012F354` disp `+0x30`: `lea rcx, [rdi + 0x30]`
- `0x0012F362` disp `+0x80`: `mov qword ptr [rdi + 0x80], r15`
- `0x0012F369` disp `+0x88`: `mov dword ptr [rdi + 0x88], r15d`
- `0x0012F370` disp `+0x7`: `mov rax, qword ptr [rbp + 7]`
- `0x0012F3C6` disp `+0x7`: `mov qword ptr [rbp + 7], 0xf`
- `0x0012F3D6` disp `+0x27`: `mov rax, qword ptr [rbp + 0x27]`
- `0x0012F3E3` disp `+0xF`: `mov rcx, qword ptr [rbp + 0xf]`
- `0x0012F433` disp `+0x0`: `mov qword ptr [rdi], rax`
- `0x0012F436` disp `+0x90`: `mov qword ptr [rdi + 0x90], r14`
- `0x0012F43D` disp `+0x98`: `mov dword ptr [rdi + 0x98], ebx`
- `0x0012F443` disp `+0x9C`: `mov word ptr [rdi + 0x9c], 0x100`
- `0x0012F44C` disp `+0xA0`: `mov dword ptr [rdi + 0xa0], r15d`
- `0x0012F453` disp `+0xA8`: `lea rcx, [rdi + 0xa8]`
- `0x0012F467` disp `+0xF8`: `mov qword ptr [rdi + 0xf8], rax`
- `0x0012F46E` disp `+0x100`: `mov qword ptr [rdi + 0x100], rax`
- `0x0012F475` disp `+0x108`: `mov qword ptr [rdi + 0x108], rax`
- `0x0012F47C` disp `+0x110`: `mov qword ptr [rdi + 0x110], rax`
- `0x0012F483` disp `+0x118`: `mov qword ptr [rdi + 0x118], rax`
- `0x0012F48A` disp `+0x120`: `mov qword ptr [rdi + 0x120], rax`
- `0x0012F491` disp `+0x128`: `mov qword ptr [rdi + 0x128], rax`
- `0x0012F498` disp `+0x130`: `mov qword ptr [rdi + 0x130], rax`
- `0x0012F49F` disp `+0x138`: `mov qword ptr [rdi + 0x138], rax`
- `0x0012F4A6` disp `+0x140`: `mov qword ptr [rdi + 0x140], rax`
- `0x0012F4AD` disp `+0x148`: `mov qword ptr [rdi + 0x148], rax`
- `0x0012F4B4` disp `+0x150`: `mov qword ptr [rdi + 0x150], rax`
- `0x0012F4BB` disp `+0x158`: `mov qword ptr [rdi + 0x158], r15`
- `0x0012F4C2` disp `+0x160`: `mov dword ptr [rdi + 0x160], 0xffffffff`
- `0x0012F4CC` disp `+0x168`: `mov qword ptr [rdi + 0x168], r15`
- `0x0012F4D3` disp `+0x170`: `mov dword ptr [rdi + 0x170], r15d`
- `0x0012F4DA` disp `+0x180`: `mov qword ptr [rdi + 0x180], r15`
- `0x0012F4E1` disp `+0x188`: `mov qword ptr [rdi + 0x188], r15`
- `0x0012F4E8` disp `+0x190`: `mov qword ptr [rdi + 0x190], r15`
- `0x0012F4EF` disp `+0x1A0`: `mov qword ptr [rdi + 0x1a0], r15`
- `0x0012F4F6` disp `+0x1A8`: `mov qword ptr [rdi + 0x1a8], r15`
- `0x0012F4FD` disp `+0x1B0`: `mov qword ptr [rdi + 0x1b0], r15`
- `0x0012F504` disp `+0x1B8`: `mov qword ptr [rdi + 0x1b8], rax`
- `0x0012F50B` disp `+0x1C0`: `mov dword ptr [rdi + 0x1c0], eax`
- `0x0012F511` disp `+0x178`: `mov dword ptr [rdi + 0x178], r15d`
- `0x0012F518` disp `+0x198`: `mov dword ptr [rdi + 0x198], r15d`
- `0x0012F51F` disp `+0x1D8`: `lea rcx, [rdi + 0x1d8]`
- `0x0012F526` disp `+0x2`: `lea edx, [rax + 2]`
- `0x0012F531` disp `+0x228`: `mov qword ptr [rdi + 0x228], rax`
- `0x0012F538` disp `+0x230`: `mov qword ptr [rdi + 0x230], rax`
- `0x0012F53F` disp `+0x238`: `mov qword ptr [rdi + 0x238], rax`
- `0x0012F546` disp `+0x240`: `mov qword ptr [rdi + 0x240], rax`
- `0x0012F54D` disp `+0x248`: `mov qword ptr [rdi + 0x248], rax`
- `0x0012F554` disp `+0x250`: `mov qword ptr [rdi + 0x250], rax`
- `0x0012F55B` disp `+0x258`: `mov qword ptr [rdi + 0x258], rax`
- `0x0012F562` disp `+0x260`: `mov qword ptr [rdi + 0x260], rax`
- `0x0012F569` disp `+0x268`: `mov qword ptr [rdi + 0x268], rax`
- `0x0012F570` disp `+0x270`: `mov qword ptr [rdi + 0x270], rax`
- `0x0012F577` disp `+0x278`: `mov qword ptr [rdi + 0x278], rax`
- `0x0012F57E` disp `+0x280`: `mov qword ptr [rdi + 0x280], rax`
- `0x0012F585` disp `+0x288`: `mov qword ptr [rdi + 0x288], r15`
- `0x0012F58C` disp `+0x290`: `mov dword ptr [rdi + 0x290], 0xffffffff`
- `0x0012F596` disp `+0x298`: `mov qword ptr [rdi + 0x298], r15`
- `0x0012F59D` disp `+0x2A0`: `mov dword ptr [rdi + 0x2a0], r15d`
- `0x0012F5A4` disp `+0x2B0`: `mov qword ptr [rdi + 0x2b0], r15`
- `0x0012F5AB` disp `+0x2B8`: `mov qword ptr [rdi + 0x2b8], r15`
- `0x0012F5B2` disp `+0x2C0`: `mov qword ptr [rdi + 0x2c0], r15`
- `0x0012F5B9` disp `+0x2D0`: `mov qword ptr [rdi + 0x2d0], r15`
- `0x0012F5C0` disp `+0x2D8`: `mov qword ptr [rdi + 0x2d8], r15`
- `0x0012F5C7` disp `+0x2E0`: `mov qword ptr [rdi + 0x2e0], r15`
- `0x0012F5CE` disp `+0x2E8`: `mov qword ptr [rdi + 0x2e8], rax`
- `0x0012F5D5` disp `+0x2F0`: `mov dword ptr [rdi + 0x2f0], eax`
- `0x0012F5DB` disp `+0x2A8`: `mov dword ptr [rdi + 0x2a8], r15d`
- `0x0012F5E2` disp `+0x2C8`: `mov dword ptr [rdi + 0x2c8], r15d`
- `0x0012F5E9` disp `+0x310`: `mov byte ptr [rdi + 0x310], al`
- `0x0012F5EF` disp `+0x318`: `lea rcx, [rdi + 0x318]`
- `0x0012F5F6` disp `+0x2`: `lea edx, [rax + 2]`
- `0x0012F5FF` disp `+0x368`: `lea rcx, [rdi + 0x368]`
- `0x0012F606` disp `+0x0`: `movups xmm0, xmmword ptr [rsi]`
- `0x0012F609` disp `+0x0`: `movups xmmword ptr [rcx], xmm0`
- `0x0012F60C` disp `+0x10`: `movups xmm1, xmmword ptr [rsi + 0x10]`
- `0x0012F610` disp `+0x10`: `movups xmmword ptr [rcx + 0x10], xmm1`
- `0x0012F614` disp `+0x20`: `movups xmm0, xmmword ptr [rsi + 0x20]`
- `0x0012F618` disp `+0x20`: `movups xmmword ptr [rcx + 0x20], xmm0`
- `0x0012F61C` disp `+0x30`: `movups xmm1, xmmword ptr [rsi + 0x30]`
- `0x0012F620` disp `+0x30`: `movups xmmword ptr [rcx + 0x30], xmm1`
- `0x0012F624` disp `+0x40`: `movups xmm0, xmmword ptr [rsi + 0x40]`
- `0x0012F628` disp `+0x40`: `movups xmmword ptr [rcx + 0x40], xmm0`
- `0x0012F62C` disp `+0x50`: `movups xmm1, xmmword ptr [rsi + 0x50]`
- `0x0012F630` disp `+0x50`: `movups xmmword ptr [rcx + 0x50], xmm1`
- `0x0012F634` disp `+0x60`: `movups xmm0, xmmword ptr [rsi + 0x60]`
- `0x0012F638` disp `+0x60`: `movups xmmword ptr [rcx + 0x60], xmm0`
- `0x0012F63C` disp `+0x80`: `lea rcx, [rcx + 0x80]`
- `0x0012F643` disp `+0x70`: `movups xmm0, xmmword ptr [rsi + 0x70]`
- `0x0012F64B` disp `+0x80`: `lea rax, [rsi + 0x80]`
- `0x0012F652` disp `+0x0`: `movups xmm1, xmmword ptr [rax]`
- `0x0012F655` disp `+0x0`: `movups xmmword ptr [rcx], xmm1`
- `0x0012F658` disp `+0x10`: `movups xmm0, xmmword ptr [rax + 0x10]`
- `0x0012F65C` disp `+0x10`: `movups xmmword ptr [rcx + 0x10], xmm0`
- `0x0012F660` disp `+0x20`: `movups xmm1, xmmword ptr [rax + 0x20]`
- `0x0012F664` disp `+0x20`: `movups xmmword ptr [rcx + 0x20], xmm1`
- `0x0012F668` disp `+0x30`: `movups xmm0, xmmword ptr [rax + 0x30]`
- `0x0012F66C` disp `+0x30`: `movups xmmword ptr [rcx + 0x30], xmm0`
- `0x0012F670` disp `+0x40`: `movups xmm1, xmmword ptr [rax + 0x40]`
- `0x0012F674` disp `+0x40`: `movups xmmword ptr [rcx + 0x40], xmm1`
- `0x0012F678` disp `+0x50`: `mov rax, qword ptr [rax + 0x50]`
- `0x0012F67C` disp `+0x50`: `mov qword ptr [rcx + 0x50], rax`
- `0x0012F680` disp `+0x440`: `lea rcx, [rdi + 0x440]`
- `0x0012F687` disp `+0x0`: `movups xmm0, xmmword ptr [rsi]`
- `0x0012F68A` disp `+0x0`: `movups xmmword ptr [rcx], xmm0`
- `0x0012F68D` disp `+0x10`: `movups xmm1, xmmword ptr [rsi + 0x10]`
- `0x0012F691` disp `+0x10`: `movups xmmword ptr [rcx + 0x10], xmm1`
- `0x0012F695` disp `+0x20`: `movups xmm0, xmmword ptr [rsi + 0x20]`
- `0x0012F699` disp `+0x20`: `movups xmmword ptr [rcx + 0x20], xmm0`
- `0x0012F69D` disp `+0x30`: `movups xmm1, xmmword ptr [rsi + 0x30]`
- `0x0012F6A1` disp `+0x30`: `movups xmmword ptr [rcx + 0x30], xmm1`
- `0x0012F6A5` disp `+0x40`: `movups xmm0, xmmword ptr [rsi + 0x40]`
- `0x0012F6A9` disp `+0x40`: `movups xmmword ptr [rcx + 0x40], xmm0`
- `0x0012F6AD` disp `+0x50`: `movups xmm1, xmmword ptr [rsi + 0x50]`
- `0x0012F6B1` disp `+0x50`: `movups xmmword ptr [rcx + 0x50], xmm1`
- `0x0012F6B5` disp `+0x60`: `movups xmm0, xmmword ptr [rsi + 0x60]`
- `0x0012F6B9` disp `+0x60`: `movups xmmword ptr [rcx + 0x60], xmm0`
- `0x0012F6BD` disp `+0x80`: `lea rcx, [rcx + 0x80]`
- `0x0012F6C4` disp `+0x70`: `movups xmm1, xmmword ptr [rsi + 0x70]`
- `0x0012F6D0` disp `+0x0`: `movups xmm0, xmmword ptr [rsi]`
- `0x0012F6D3` disp `+0x0`: `movups xmmword ptr [rcx], xmm0`
- `0x0012F6D6` disp `+0x10`: `movups xmm1, xmmword ptr [rsi + 0x10]`
- `0x0012F6DA` disp `+0x10`: `movups xmmword ptr [rcx + 0x10], xmm1`
- `0x0012F6DE` disp `+0x20`: `movups xmm0, xmmword ptr [rsi + 0x20]`
- `0x0012F6E2` disp `+0x20`: `movups xmmword ptr [rcx + 0x20], xmm0`
- `0x0012F6E6` disp `+0x30`: `movups xmm1, xmmword ptr [rsi + 0x30]`
- `0x0012F6EA` disp `+0x30`: `movups xmmword ptr [rcx + 0x30], xmm1`
- `0x0012F6EE` disp `+0x40`: `movups xmm0, xmmword ptr [rsi + 0x40]`
- `0x0012F6F2` disp `+0x40`: `movups xmmword ptr [rcx + 0x40], xmm0`
- `0x0012F6F6` disp `+0x50`: `mov rax, qword ptr [rsi + 0x50]`
- `0x0012F6FA` disp `+0x50`: `mov qword ptr [rcx + 0x50], rax`
- `0x0012F6FE` disp `+0x518`: `lea rbx, [rdi + 0x518]`
- `0x0012F709` disp `+0x0`: `mov qword ptr [rbx], r15`
- `0x0012F70C` disp `+0x8`: `mov qword ptr [rbx + 8], r15`
- `0x0012F718` disp `+0x0`: `mov qword ptr [rbx], rax`
- `0x0012F71B` disp `+0x528`: `lea rbx, [rdi + 0x528]`
- `0x0012F726` disp `+0x0`: `mov qword ptr [rbx], r15`
- `0x0012F729` disp `+0x8`: `mov qword ptr [rbx + 8], r15`
- `0x0012F735` disp `+0x0`: `mov qword ptr [rbx], rax`
- `0x0012F738` disp `+0x538`: `mov qword ptr [rdi + 0x538], r15`
- `0x0012F73F` disp `+0x540`: `mov dword ptr [rdi + 0x540], 0`
- `0x0012F749` disp `+0x544`: `mov word ptr [rdi + 0x544], 0`
- `0x0012F752` disp `+0x546`: `mov byte ptr [rdi + 0x546], 0`
- `0x0012F759` disp `+0x548`: `mov qword ptr [rdi + 0x548], r15`
- `0x0012F760` disp `+0x550`: `mov word ptr [rdi + 0x550], 0`
- `0x0012F769` disp `+0x558`: `lea rcx, [rdi + 0x558]`
- `0x0012F77B` disp `+0x5A8`: `mov byte ptr [rdi + 0x5a8], 0`
- `0x0012F787` disp `+0x5B0`: `lea rcx, [rdi + 0x5b0]`
- `0x0012F793` disp `+0x600`: `lea rcx, [rdi + 0x600]`
- `0x0012F79F` disp `+0x648`: `mov byte ptr [rdi + 0x648], 1`
- `0x0012F7A6` disp `+0x650`: `mov qword ptr [rdi + 0x650], r15`
- `0x0012F7AD` disp `+0x658`: `mov dword ptr [rdi + 0x658], r15d`
- `0x0012F7B4` disp `+0x660`: `lea rcx, [rdi + 0x660]`
- `0x0012F7C6` disp `+0x6B0`: `lea rcx, [rdi + 0x6b0]`
- `0x0012F7D3` disp `+0x718`: `mov word ptr [rdi + 0x718], 0x100`
- `0x0012F7DC` disp `+0x720`: `lea rax, [rdi + 0x720]`
- `0x0012F7E3` disp `+0x18`: `mov qword ptr [rax + 0x18], 0xf`
- `0x0012F7EB` disp `+0x10`: `mov qword ptr [rax + 0x10], r15`
- `0x0012F7EF` disp `+0x18`: `cmp qword ptr [rax + 0x18], 0x10`
- `0x0012F7F6` disp `+0x0`: `mov rax, qword ptr [rax]`
- `0x0012F7F9` disp `+0x0`: `mov byte ptr [rax], 0`
- `0x0012F7FC` disp `+0x740`: `mov qword ptr [rdi + 0x740], r15`
- `0x0012F803` disp `+0x748`: `mov qword ptr [rdi + 0x748], r15`
- `0x0012F80A` disp `+0x750`: `lea rcx, [rdi + 0x750]`
- `0x0012F81C` disp `+0x7A0`: `mov dword ptr [rdi + 0x7a0], r15d`
- `0x0012F823` disp `+0x7A8`: `lea rbx, [rdi + 0x7a8]`
- `0x0012F82E` disp `+0x0`: `mov qword ptr [rbx], r15`
- `0x0012F831` disp `+0x8`: `mov qword ptr [rbx + 8], r15`
- `0x0012F83D` disp `+0x0`: `mov qword ptr [rbx], rax`
- `0x0012F840` disp `+0x7B8`: `mov qword ptr [rdi + 0x7b8], r15`
- `0x0012F84A` disp `+0x2F`: `mov rcx, qword ptr [rbp + 0x2f]`
- `0x0012F856` disp `+0xC8`: `mov rbx, qword ptr [rsp + 0xc8]`

### Direct calls

- `0x0012F2EE` -> `0x0005CA20`
- `0x0012F309` -> `0x0003F680`
- `0x0012F348` -> `0x000354B0`
- `0x0012F35D` -> `0x00391A94`
- `0x0012F38E` -> `0x003DB020`
- `0x0012F39D` -> `0x003DB020`
- `0x0012F3AC` -> `0x003DB020`
- `0x0012F3B8` -> `0x003DB020`
- `0x0012F3C1` -> `0x003B20D4`
- `0x0012F3F4` -> `0x003DB020`
- `0x0012F403` -> `0x003DB020`
- `0x0012F412` -> `0x003DB020`
- `0x0012F41E` -> `0x003DB020`
- `0x0012F427` -> `0x003B20D4`
- `0x0012F45F` -> `0x00391A94`
- `0x0012F529` -> `0x00391A94`
- `0x0012F5F9` -> `0x00391A94`
- `0x0012F713` -> `0x0012FFB0`
- `0x0012F730` -> `0x0012FFB0`
- `0x0012F775` -> `0x00391A94`
- `0x0012F78E` -> `0x00391A94`
- `0x0012F79A` -> `0x00391E84`
- `0x0012F7C0` -> `0x00391A94`
- `0x0012F7CD` -> `0x00391E84`
- `0x0012F816` -> `0x00391A94`
- `0x0012F838` -> `0x0012FF50`
- `0x0012F851` -> `0x003B24C0`

### Direct callers


## target `0x0012FFB0` PDATA `0x0012FFB0..0x00130002`

```asm
0x0012FFB0: mov qword ptr [rsp + 8], rcx
0x0012FFB5: sub rsp, 0x38
0x0012FFB9: mov qword ptr [rsp + 0x20], 0xfffffffffffffffe
0x0012FFC2: mov ecx, 0x30
0x0012FFC7: call 0x1403b2098
0x0012FFCC: mov qword ptr [rsp + 0x40], rax
0x0012FFD1: test rax, rax
0x0012FFD4: jne 0x14012ffdc
0x0012FFD6: call 0x1403db020
0x0012FFDB: nop
0x0012FFDC: mov qword ptr [rax], rax
0x0012FFDF: lea rcx, [rax + 8]
0x0012FFE3: test rcx, rcx
0x0012FFE6: je 0x14012ffeb
0x0012FFE8: mov qword ptr [rcx], rax
0x0012FFEB: lea rcx, [rax + 0x10]
0x0012FFEF: test rcx, rcx
0x0012FFF2: je 0x14012fff7
0x0012FFF4: mov qword ptr [rcx], rax
0x0012FFF7: mov word ptr [rax + 0x18], 0x101
0x0012FFFD: add rsp, 0x38
0x00130001: ret
```

### Object-relative memory operands

- `0x0012FFB0` disp `+0x8`: `mov qword ptr [rsp + 8], rcx`
- `0x0012FFB9` disp `+0x20`: `mov qword ptr [rsp + 0x20], 0xfffffffffffffffe`
- `0x0012FFCC` disp `+0x40`: `mov qword ptr [rsp + 0x40], rax`
- `0x0012FFDC` disp `+0x0`: `mov qword ptr [rax], rax`
- `0x0012FFDF` disp `+0x8`: `lea rcx, [rax + 8]`
- `0x0012FFE8` disp `+0x0`: `mov qword ptr [rcx], rax`
- `0x0012FFEB` disp `+0x10`: `lea rcx, [rax + 0x10]`
- `0x0012FFF4` disp `+0x0`: `mov qword ptr [rcx], rax`
- `0x0012FFF7` disp `+0x18`: `mov word ptr [rax + 0x18], 0x101`

### Direct calls

- `0x0012FFC7` -> `0x003B2098`
- `0x0012FFD6` -> `0x003DB020`

### Direct callers


## target `0x0012FF50` PDATA `0x0012FF50..0x0012FFA2`

```asm
0x0012FF50: mov qword ptr [rsp + 8], rcx
0x0012FF55: sub rsp, 0x38
0x0012FF59: mov qword ptr [rsp + 0x20], 0xfffffffffffffffe
0x0012FF62: mov ecx, 0x38
0x0012FF67: call 0x1403b2098
0x0012FF6C: mov qword ptr [rsp + 0x40], rax
0x0012FF71: test rax, rax
0x0012FF74: jne 0x14012ff7c
0x0012FF76: call 0x1403db020
0x0012FF7B: nop
0x0012FF7C: mov qword ptr [rax], rax
0x0012FF7F: lea rcx, [rax + 8]
0x0012FF83: test rcx, rcx
0x0012FF86: je 0x14012ff8b
0x0012FF88: mov qword ptr [rcx], rax
0x0012FF8B: lea rcx, [rax + 0x10]
0x0012FF8F: test rcx, rcx
0x0012FF92: je 0x14012ff97
0x0012FF94: mov qword ptr [rcx], rax
0x0012FF97: mov word ptr [rax + 0x18], 0x101
0x0012FF9D: add rsp, 0x38
0x0012FFA1: ret
```

### Object-relative memory operands

- `0x0012FF50` disp `+0x8`: `mov qword ptr [rsp + 8], rcx`
- `0x0012FF59` disp `+0x20`: `mov qword ptr [rsp + 0x20], 0xfffffffffffffffe`
- `0x0012FF6C` disp `+0x40`: `mov qword ptr [rsp + 0x40], rax`
- `0x0012FF7C` disp `+0x0`: `mov qword ptr [rax], rax`
- `0x0012FF7F` disp `+0x8`: `lea rcx, [rax + 8]`
- `0x0012FF88` disp `+0x0`: `mov qword ptr [rcx], rax`
- `0x0012FF8B` disp `+0x10`: `lea rcx, [rax + 0x10]`
- `0x0012FF94` disp `+0x0`: `mov qword ptr [rcx], rax`
- `0x0012FF97` disp `+0x18`: `mov word ptr [rax + 0x18], 0x101`

### Direct calls

- `0x0012FF67` -> `0x003B2098`
- `0x0012FF76` -> `0x003DB020`

### Direct callers

