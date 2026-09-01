# Indirect vtable slot +0x80 callsites

total: `53`

## 1. `0x001355A0` in `0x00135560..0x001355AF`

```asm
0x00135560: push rbx
0x00135562: sub rsp, 0x100
0x00135569: mov rbx, rcx
0x0013556C: mov eax, dword ptr [rcx + 0x88]
0x00135572: cmp eax, 1
0x00135575: jne 0x140135587
0x00135577: movzx edx, al
0x0013557A: call 0x140130170
0x0013557F: mov rcx, rbx
0x00135582: call 0x140228140
0x00135587: lea rdx, [rsp + 0x20]
0x0013558C: mov rcx, rbx
0x0013558F: call 0x14006a320
0x00135594: cmp dword ptr [rax + 0x2c], 0
0x00135598: jle 0x1401355a6
0x0013559A: mov rax, qword ptr [rbx]
0x0013559D: mov rcx, rbx
0x001355A0: call qword ptr [rax + 0x80]
0x001355A6: add rsp, 0x100
0x001355AD: pop rbx
0x001355AE: ret
```

## 2. `0x0013716A` in `0x00136D30..0x0013722D`

```asm
0x001370A9: test bl, bl
0x001370AB: jne 0x14013712b
0x001370AD: cmp byte ptr [rdi + 0x53d], bl
0x001370B3: jne 0x14013712b
0x001370B5: xor eax, eax
0x001370B7: mov qword ptr [rbp + 0x190], rax
0x001370BE: mov qword ptr [rbp + 0x198], rax
0x001370C5: mov qword ptr [rbp + 0x1a0], rax
0x001370CC: mov qword ptr [rbp + 0x1a8], rax
0x001370D3: lea rcx, [rsi + 0x20]
0x001370D7: lea r8, [rcx + 0x20]
0x001370DB: sub r8, rcx
0x001370DE: lea rdx, [rbp + 0x190]
0x001370E5: call 0x1403d2f70
0x001370EA: test eax, eax
0x001370EC: jne 0x140137178
0x001370F2: xor eax, eax
0x001370F4: mov qword ptr [rbp + 0x1b0], rax
0x001370FB: mov qword ptr [rbp + 0x1b8], rax
0x00137102: mov qword ptr [rbp + 0x1c0], rax
0x00137109: mov qword ptr [rbp + 0x1c8], rax
0x00137110: lea r8d, [rax + 0x20]
0x00137114: lea rdx, [rbp + 0x1b0]
0x0013711B: lea rcx, [rbp + 0x90]
0x00137122: call 0x1403d2f70
0x00137127: test eax, eax
0x00137129: je 0x140137178
0x0013712B: mov rax, qword ptr [rdi]
0x0013712E: mov rcx, rdi
0x00137131: call qword ptr [rax + 0x40]
0x00137134: mov eax, dword ptr [rdi + 0x88]
0x0013713A: cmp eax, 1
0x0013713D: jne 0x140137152
0x0013713F: movzx edx, al
0x00137142: mov rcx, rdi
0x00137145: call 0x140130170
0x0013714A: mov rcx, rdi
0x0013714D: call 0x140228140
0x00137152: lea rdx, [rbp - 0x70]
0x00137156: mov rcx, rdi
0x00137159: call 0x14006a320
0x0013715E: cmp dword ptr [rax + 0x2c], 0
0x00137162: jle 0x140137170
0x00137164: mov rax, qword ptr [rdi]
0x00137167: mov rcx, rdi
0x0013716A: call qword ptr [rax + 0x80]
0x00137170: xor eax, eax
0x00137172: xchg byte ptr [rdi + 0x53f], al
0x00137178: mov rdx, qword ptr [rbp + 0x118]
0x0013717F: test rdx, rdx
0x00137182: je 0x1401371b4
0x00137184: mov r8, qword ptr [rbp + 0x128]
0x0013718B: sub r8, rdx
0x0013718E: sar r8, 5
0x00137192: lea rcx, [rbp + 0x118]
0x00137199: call 0x14006f460
0x0013719E: mov qword ptr [rbp + 0x118], 0
0x001371A9: xorps xmm0, xmm0
0x001371AC: movdqa xmmword ptr [rbp + 0x120], xmm0
0x001371B4: lea rcx, [rbp + 0xf8]
0x001371BB: call 0x14006a240
0x001371C0: nop
0x001371C1: jmp 0x140137202
0x001371C3: mov eax, 1
0x001371C8: mov dword ptr [rsp + 0x30], eax
0x001371CC: call 0x140058850
0x001371D1: mov qword ptr [rsp + 0x38], rax
0x001371D6: movaps xmm0, xmmword ptr [rsp + 0x30]
0x001371DB: movdqa xmmword ptr [rsp + 0x50], xmm0
0x001371E1: lea rdx, [rsp + 0x50]
0x001371E6: lea rcx, [rsp + 0x60]
0x001371EB: call 0x140059100
0x001371F0: lea rdx, [rip + 0x654061]
0x001371F7: lea rcx, [rsp + 0x60]
0x001371FC: call 0x1403d25d0
0x00137201: nop
0x00137202: mov rcx, qword ptr [rbp + 0x220]
0x00137209: xor rcx, rsp
0x0013720C: call 0x1403b24c0
0x00137211: lea r11, [rsp + 0x330]
```

## 3. `0x0014B775` in `0x0014B700..0x0014B78F`

```asm
0x0014B700: mov qword ptr [rsp + 8], rbx
0x0014B705: mov qword ptr [rsp + 0x10], rsi
0x0014B70A: push rdi
0x0014B70B: sub rsp, 0x20
0x0014B70F: mov rdi, rdx
0x0014B712: movzx esi, r8b
0x0014B716: movsxd rdx, dword ptr [rcx + 0x2c]
0x0014B71A: mov rbx, rcx
0x0014B71D: test edx, edx
0x0014B71F: jle 0x14014b74f
0x0014B721: test r9b, r9b
0x0014B724: je 0x14014b72e
0x0014B726: mov qword ptr [rcx + 0x30], 0
0x0014B72E: mov rax, qword ptr [rcx + 0x30]
0x0014B732: cmp rdi, rax
0x0014B735: jb 0x14014b742
0x0014B737: mov rcx, rdi
0x0014B73A: sub rcx, rax
0x0014B73D: cmp rcx, rdx
0x0014B740: jb 0x14014b74f
0x0014B742: mov rax, qword ptr [rbx]
0x0014B745: mov rcx, rbx
0x0014B748: call qword ptr [rax + 0x78]
0x0014B74B: mov qword ptr [rbx + 0x30], rdi
0x0014B74F: movsxd rax, dword ptr [rbx + 0x38]
0x0014B753: test eax, eax
0x0014B755: jle 0x14014b77f
0x0014B757: mov rdx, qword ptr [rbx + 0x40]
0x0014B75B: cmp rdi, rdx
0x0014B75E: jb 0x14014b76b
0x0014B760: mov rcx, rdi
0x0014B763: sub rcx, rdx
0x0014B766: cmp rcx, rax
0x0014B769: jb 0x14014b77f
0x0014B76B: mov rax, qword ptr [rbx]
0x0014B76E: movzx edx, sil
0x0014B772: mov rcx, rbx
0x0014B775: call qword ptr [rax + 0x80]
0x0014B77B: mov qword ptr [rbx + 0x40], rdi
0x0014B77F: mov rbx, qword ptr [rsp + 0x30]
0x0014B784: mov rsi, qword ptr [rsp + 0x38]
0x0014B789: add rsp, 0x20
0x0014B78D: pop rdi
0x0014B78E: ret
```

## 4. `0x0016F8A8` in `0x0016ED70..0x0017044B`

```asm
0x0016F811: mov rcx, qword ptr [rax + 0x28]
0x0016F815: cmp rcx, qword ptr [rax + 0x20]
0x0016F819: jae 0x14016f82c
0x0016F81B: test rcx, rcx
0x0016F81E: je 0x14016f82c
0x0016F820: mov r13b, 1
0x0016F823: cmp edi, r14d
0x0016F826: cmovg edi, r14d
0x0016F82A: jmp 0x14016f82f
0x0016F82C: xor r13b, r13b
0x0016F82F: mov rcx, rsi
0x0016F832: call 0x14016ea50
0x0016F837: mov rbx, rax
0x0016F83A: test rax, rax
0x0016F83D: je 0x14016f889
0x0016F83F: mov edx, dword ptr [rsi + 0x78]
0x0016F842: mov ecx, edi
0x0016F844: call 0x140159840
0x0016F849: mov edx, dword ptr [rsi + 0x78]
0x0016F84C: mov rcx, rax
0x0016F84F: call 0x140159ba0
0x0016F854: cmp qword ptr [rsi + 0x80], 0
0x0016F85C: je 0x14016f87f
0x0016F85E: mov rcx, qword ptr [rsi + 0x80]
0x0016F865: mov rdx, qword ptr [rcx + 0x28]
0x0016F869: cmp rdx, qword ptr [rcx + 0x20]
0x0016F86D: jae 0x14016f87f
0x0016F86F: test rdx, rdx
0x0016F872: je 0x14016f87f
0x0016F874: cmp rdx, qword ptr [rcx + 0x20]
0x0016F878: jae 0x14016f889
0x0016F87A: cmp rbx, rdx
0x0016F87D: jae 0x14016f889
0x0016F87F: cmp rbx, rax
0x0016F882: setae al
0x0016F885: test al, al
0x0016F887: je 0x14016f88e
0x0016F889: test r13b, r13b
0x0016F88C: je 0x14016f897
0x0016F88E: cmp byte ptr [rsp + 0x30], 0
0x0016F893: cmovne r15d, r12d
0x0016F897: mov rcx, qword ptr [rsi + 0x80]
0x0016F89E: mov rax, qword ptr [rcx]
0x0016F8A1: cmp r15d, 1
0x0016F8A5: sete dl
0x0016F8A8: call qword ptr [rax + 0x80]
0x0016F8AE: mov eax, dword ptr [rsp + 0x38]
0x0016F8B2: mov r12d, 1
0x0016F8B8: cmp r15d, 2
0x0016F8BC: jne 0x14016f8cc
0x0016F8BE: cmp byte ptr [rsp + 0x31], 0
0x0016F8C3: je 0x14016f8cc
0x0016F8C5: cmp eax, r15d
0x0016F8C8: cmove eax, r12d
0x0016F8CC: mov dword ptr [rsp + 0x20], eax
0x0016F8D0: mov r9d, r15d
0x0016F8D3: mov r8d, r14d
0x0016F8D6: mov edx, edi
0x0016F8D8: mov rcx, rsi
0x0016F8DB: call 0x14016be60
0x0016F8E0: test eax, eax
0x0016F8E2: jne 0x140170427
0x0016F8E8: mov dword ptr [rsp + 0xf0], 0x26
0x0016F8F3: mov eax, dword ptr [rsp + 0xf0]
0x0016F8FA: add al, 0x26
0x0016F8FC: movsx ecx, al
0x0016F8FF: xor ecx, 0x46
0x0016F902: mov dword ptr [rsp + 0xf4], ecx
0x0016F909: mov eax, dword ptr [rsp + 0xf4]
0x0016F910: mov ecx, dword ptr [rsp + 0xf0]
0x0016F917: xor ecx, eax
0x0016F919: xor ecx, 0x7b
0x0016F91C: mov byte ptr [rsp + 0xf8], cl
0x0016F923: movsx ecx, byte ptr [rsp + 0xf8]
0x0016F92B: mov eax, dword ptr [rsp + 0xf0]
0x0016F932: inc al
0x0016F934: xor eax, ecx
0x0016F936: xor eax, 0x7d
0x0016F939: mov byte ptr [rsp + 0xf9], al
0x0016F940: movsx ecx, byte ptr [rsp + 0xf9]
```

## 5. `0x001DA858` in `0x001DA7FC..0x001DA869`

```asm
0x001DA7FC: mov qword ptr [rsp + 0x30], rdi
0x001DA801: xor edi, edi
0x001DA803: lea rcx, [rbx + 0x398]
0x001DA80A: mov qword ptr [rbx + 0x258], rdi
0x001DA811: mov r8d, 3
0x001DA817: mov qword ptr [rbx + 0x260], rax
0x001DA81E: mov dword ptr [rbx + 0x268], eax
0x001DA824: lea rax, [rcx + 3]
0x001DA828: cmp rcx, rax
0x001DA82B: cmova r8d, edi
0x001DA82F: ja 0x1401da850
0x001DA831: mov rdx, rcx
0x001DA834: neg rdx
0x001DA837: nop word ptr [rax + rax]
0x001DA840: mov byte ptr [rcx], dil
0x001DA843: lea rcx, [rcx + 1]
0x001DA847: lea rax, [rdx + rcx]
0x001DA84B: cmp rax, r8
0x001DA84E: jne 0x1401da840
0x001DA850: mov rax, qword ptr [rbx]
0x001DA853: xor edx, edx
0x001DA855: mov rcx, rbx
0x001DA858: call qword ptr [rax + 0x80]
0x001DA85E: mov dword ptr [rbx + 0x27c], edi
0x001DA864: mov rdi, qword ptr [rsp + 0x30]
```

## 6. `0x001F8B7B` in `0x001F7F40..0x001FB9C1`

```asm
0x001F8A9F: mov rcx, rbx
0x001F8AA2: call 0x14024ad10
0x001F8AA7: jmp 0x1401f8ae7
0x001F8AA9: lea rbx, [rdi + 0x258]
0x001F8AB0: lea rdx, [rbp + 0x7d0]
0x001F8AB7: mov rcx, rbx
0x001F8ABA: call 0x14009d3e0
0x001F8ABF: mov rax, qword ptr [rbp + 0x8a0]
0x001F8AC6: mov qword ptr [rbx + 0xd0], rax
0x001F8ACD: mov rax, qword ptr [rbp + 0x8a8]
0x001F8AD4: mov qword ptr [rbx + 0xd8], rax
0x001F8ADB: mov eax, dword ptr [rbp + 0x8b0]
0x001F8AE1: mov dword ptr [rbx + 0xe0], eax
0x001F8AE7: mov rax, qword ptr [rbp + 0x8a0]
0x001F8AEE: mov qword ptr [r13 + 0x18], rax
0x001F8AF2: mov rax, qword ptr [rbp + 0x8a8]
0x001F8AF9: mov qword ptr [r13 + 0x20], rax
0x001F8AFD: mov byte ptr [rdi + 0x254], 1
0x001F8B04: mov r14d, dword ptr [rbp + 0x8b0]
0x001F8B0B: cmp r14d, 2
0x001F8B0F: jne 0x1401f8b4e
0x001F8B11: mov rdx, rbx
0x001F8B14: lea rcx, [rbp + 0x1120]
0x001F8B1B: call 0x140408150
0x001F8B20: lea rcx, [rdi + 0x2d8]
0x001F8B27: call 0x1401aab70
0x001F8B2C: mov qword ptr [rbp - 0x78], rax
0x001F8B30: jmp 0x1401f8b4e
0x001F8B32: mov byte ptr [rdi + 0x254], 0
0x001F8B39: mov r14d, r12d
0x001F8B3C: xor edx, edx
0x001F8B3E: lea r8d, [rdx + 0x5c]
0x001F8B42: lea rcx, [rbp + 0x1120]
0x001F8B49: call 0x1403d3050
0x001F8B4E: mov r9d, 0x5c
0x001F8B54: lea r8, [rbp + 0x1120]
0x001F8B5B: xor edx, edx
0x001F8B5D: mov rcx, rdi
0x001F8B60: call 0x1401fdb70
0x001F8B65: nop
0x001F8B66: lea rcx, [rbp + 0x7d0]
0x001F8B6D: call 0x14012f910
0x001F8B72: mov rax, qword ptr [rdi]
0x001F8B75: mov edx, r14d
0x001F8B78: mov rcx, rdi
0x001F8B7B: call qword ptr [rax + 0x80]
0x001F8B81: test al, al
0x001F8B83: jne 0x1401f8bb7
0x001F8B85: lea rax, [rip + 0x23ade4]
0x001F8B8C: mov qword ptr [rbp + 0x230], rax
0x001F8B93: xor eax, eax
0x001F8B95: mov qword ptr [rbp + 0x238], rax
0x001F8B9C: mov qword ptr [rbp + 0x240], rax
0x001F8BA3: lea rdx, [rip + 0x59290e]
0x001F8BAA: lea rcx, [rbp + 0x230]
0x001F8BB1: call 0x1403d25d0
0x001F8BB6: int3
0x001F8BB7: lea r15, [rdi + 0x48]
0x001F8BBB: mov rax, qword ptr [rdi]
0x001F8BBE: mov rdx, r15
0x001F8BC1: mov rcx, rdi
0x001F8BC4: call qword ptr [rax + 0x50]
0x001F8BC7: mov ebx, eax
0x001F8BC9: mov dword ptr [rsp + 0x64], eax
0x001F8BCD: xor edx, edx
0x001F8BCF: div dword ptr [rdi + 0x1b0]
0x001F8BD5: mov dword ptr [rsp + 0x74], eax
0x001F8BD9: xor edx, edx
0x001F8BDB: mov r8d, 0x410
0x001F8BE1: lea rcx, [rbp + 0xce0]
0x001F8BE8: call 0x1403d3050
0x001F8BED: mov r14d, r12d
0x001F8BF0: mov r13d, r12d
0x001F8BF3: mov dword ptr [rsp + 0x58], r12d
0x001F8BF8: mov r9d, dword ptr [rdi + 0x70]
0x001F8BFC: mov dword ptr [rsp + 0x7c], r9d
0x001F8C01: mov eax, r12d
0x001F8C04: mov dword ptr [rsp + 0x5c], eax
0x001F8C08: mov dword ptr [rbp - 0x20], eax
0x001F8C0B: cmp dword ptr [rdi + 0x250], eax
```

## 7. `0x00211AE3` in `0x00211460..0x002148C7`

```asm
0x002119ED: mov r8, rax
0x002119F0: mov rcx, r8
0x002119F3: call 0x1403b20d4
0x002119F8: xorps xmm0, xmm0
0x002119FB: movdqu xmmword ptr [rbp + 0x180], xmm0
0x00211A03: mov qword ptr [rbp + 0x190], r13
0x00211A0A: lea rax, [rbp + 0x518]
0x00211A11: mov qword ptr [rbp + 0x510], rax
0x00211A18: mov qword ptr [rbp + 0x508], rdi
0x00211A1F: lea rdx, [rbp + 0xd70]
0x00211A26: lea rcx, [rbp + 0x518]
0x00211A2D: call 0x1400328e0
0x00211A32: lea rcx, [rbp + 0x508]
0x00211A39: call 0x14004afc0
0x00211A3E: nop
0x00211A3F: lea rcx, [rbp + 0xd70]
0x00211A46: call 0x140032dc0
0x00211A4B: lea rax, [rip + 0x222256]
0x00211A52: mov qword ptr [rbp + 0xd60], rax
0x00211A59: lea rcx, [rbp + 0x980]
0x00211A60: call 0x140032ef0
0x00211A65: lea rax, [rip + 0x221f04]
0x00211A6C: mov qword ptr [rbp + 0x118], rax
0x00211A73: xor eax, eax
0x00211A75: mov qword ptr [rbp + 0x120], rax
0x00211A7C: mov qword ptr [rbp + 0x128], rax
0x00211A83: mov rax, qword ptr [rbp - 0x18]
0x00211A87: mov qword ptr [rbp + 0x200], rax
0x00211A8E: mov byte ptr [rbp + 0x208], 1
0x00211A95: lea rdx, [rbp + 0x120]
0x00211A9C: lea rcx, [rbp + 0x200]
0x00211AA3: call 0x1403d23c8
0x00211AA8: lea rax, [rip + 0x221ed9]
0x00211AAF: mov qword ptr [rbp + 0x118], rax
0x00211AB6: lea rdx, [rip + 0x5794a3]
0x00211ABD: lea rcx, [rbp + 0x118]
0x00211AC4: call 0x1403d25d0
0x00211AC9: int3
0x00211ACA: mov rcx, rdi
0x00211ACD: call 0x1404088e0
0x00211AD2: mov byte ptr [rsp + 0x52], r13b
0x00211AD7: mov dword ptr [rbp - 8], r13d
0x00211ADB: mov rax, qword ptr [rdi]
0x00211ADE: xor edx, edx
0x00211AE0: mov rcx, rdi
0x00211AE3: call qword ptr [rax + 0x80]
0x00211AE9: test al, al
0x00211AEB: jne 0x140211b1f
0x00211AED: lea rax, [rip + 0x221e7c]
0x00211AF4: mov qword ptr [rbp + 0x260], rax
0x00211AFB: xor eax, eax
0x00211AFD: mov qword ptr [rbp + 0x268], rax
0x00211B04: mov qword ptr [rbp + 0x270], rax
0x00211B0B: lea rdx, [rip + 0x5799a6]
0x00211B12: lea rcx, [rbp + 0x260]
0x00211B19: call 0x1403d25d0
0x00211B1E: int3
0x00211B1F: lea rdx, [rdi + 0x48]
0x00211B23: mov rax, qword ptr [rdi]
0x00211B26: mov rcx, rdi
0x00211B29: call qword ptr [rax + 0x50]
0x00211B2C: mov dword ptr [rsp + 0x6c], eax
0x00211B30: xor edx, edx
0x00211B32: div dword ptr [rdi + 0x1b0]
0x00211B38: mov dword ptr [rsp + 0x70], eax
0x00211B3C: mov r14d, r13d
0x00211B3F: mov r15d, r13d
0x00211B42: mov dword ptr [rsp + 0x68], r13d
0x00211B47: mov ecx, dword ptr [rdi + 0x70]
0x00211B4A: mov dword ptr [rsp + 0x74], ecx
0x00211B4E: cmp qword ptr [rdi + 0x140], r13
0x00211B55: jg 0x140211b61
0x00211B57: cmp ecx, 3
0x00211B5A: je 0x140211b61
0x00211B5C: xor r12b, r12b
0x00211B5F: jmp 0x140211b64
0x00211B61: mov r12b, 1
0x00211B64: mov byte ptr [rsp + 0x50], r12b
0x00211B69: mov qword ptr [rbp - 0x78], r13
0x00211B6D: call 0x140391550
```

## 8. `0x00294749` in `0x002946CC..0x0029479F`

```asm
0x002946CC: mov qword ptr [rax + 0x290], r13
0x002946D3: test r13d, r13d
0x002946D6: jle 0x14029478e
0x002946DC: nop dword ptr [rax]
0x002946E0: mov rax, qword ptr [rsi + 0x80]
0x002946E7: test rax, rax
0x002946EA: je 0x140294720
0x002946EC: cmp ebp, 3
0x002946EF: jne 0x1402946f6
0x002946F1: cmp byte ptr [rbx], 0
0x002946F4: jne 0x14029475c
0x002946F6: cmp byte ptr [rbp + rbx - 2], 0
0x002946FB: jne 0x140294720
0x002946FD: cmp byte ptr [rbp + rbx - 1], 0xff
0x00294702: jne 0x140294720
0x00294704: cmp dword ptr [rsi + 0x28c], 0
0x0029470B: jne 0x1402947b6
0x00294711: mov dword ptr [rax + 0x49c], 1
0x0029471B: add rbx, rbp
0x0029471E: jmp 0x140294782
0x00294720: cmp ebp, 3
0x00294723: jne 0x14029472a
0x00294725: cmp byte ptr [rbx], 0
0x00294728: jne 0x14029475c
0x0029472A: cmp byte ptr [rbp + rbx - 2], 0x56
0x0029472F: jne 0x14029475c
0x00294731: cmp byte ptr [rbp + rbx - 1], 0
0x00294736: jne 0x14029475c
0x00294738: mov rax, qword ptr [rsi + 8]
0x0029473C: xor r9d, r9d
0x0029473F: xor r8d, r8d
0x00294742: mov rcx, rsi
0x00294745: lea edx, [r9 + 0x77]
0x00294749: call qword ptr [rax + 0x80]
0x0029474F: test eax, eax
0x00294751: je 0x1402947ed
0x00294757: add rbx, rbp
0x0029475A: jmp 0x140294782
0x0029475C: mov rdx, rbx
0x0029475F: mov rcx, rsi
0x00294762: call 0x1402a5260
0x00294767: add rbx, rbp
0x0029476A: test rax, rax
0x0029476D: je 0x140294782
0x0029476F: mov rdx, rax
0x00294772: mov rcx, r14
0x00294775: call 0x1402c7410
0x0029477A: test eax, eax
0x0029477C: je 0x14029482e
0x00294782: add r15d, ebp
0x00294785: cmp r15d, r13d
0x00294788: jl 0x1402946e0
0x0029478E: test r12, r12
0x00294791: je 0x140294797
0x00294793: mov qword ptr [r12], r14
0x00294797: mov rax, r14
0x0029479A: mov rdi, qword ptr [rsp + 0x60]
```

## 9. `0x002991B1` in `0x00298EC0..0x002991C8`

```asm
0x002990F0: mov rdx, qword ptr [rax + 0xc8]
0x002990F7: test byte ptr [rdx + 0x70], 8
0x002990FB: jne 0x14029919c
0x00299101: mov eax, dword ptr [rsi + 0x60]
0x00299104: mov rcx, qword ptr [rbp + 0x58]
0x00299108: add eax, 4
0x0029910B: movsxd rdx, eax
0x0029910E: call 0x1402d1e10
0x00299113: test eax, eax
0x00299115: jne 0x140299157
0x00299117: mov dword ptr [rsp + 0x20], 0x858
0x0029911F: lea r9, [rip + 0x4f87ca]
0x00299126: mov r8d, 7
0x0029912C: mov edx, 0x96
0x00299131: lea ecx, [r8 + 0xd]
0x00299135: call 0x1402c3c30
0x0029913A: mov dword ptr [rsi + 0x48], 5
0x00299141: or eax, 0xffffffff
0x00299144: jmp 0x1402991b7
0x00299146: mov dword ptr [rsp + 0x20], 0x83b
0x0029914E: lea r9, [rip + 0x4f878b]
0x00299155: jmp 0x140299126
0x00299157: mov rax, qword ptr [rsi + 0x50]
0x0029915B: movsxd rcx, dword ptr [rsi + 0x60]
0x0029915F: add rcx, qword ptr [rax + 8]
0x00299163: mov qword ptr [rbp + 0x50], rcx
0x00299167: mov byte ptr [rcx], 0xe
0x0029916A: mov rax, qword ptr [rbp + 0x50]
0x0029916E: inc rax
0x00299171: mov qword ptr [rbp + 0x50], rax
0x00299175: mov byte ptr [rax], 0
0x00299178: mov rax, qword ptr [rbp + 0x50]
0x0029917C: inc rax
0x0029917F: mov qword ptr [rbp + 0x50], rax
0x00299183: mov byte ptr [rax], 0
0x00299186: mov rax, qword ptr [rbp + 0x50]
0x0029918A: inc rax
0x0029918D: mov qword ptr [rbp + 0x50], rax
0x00299191: mov byte ptr [rax], 0
0x00299194: inc qword ptr [rbp + 0x50]
0x00299198: add dword ptr [rsi + 0x60], 4
0x0029919C: mov dword ptr [rsi + 0x48], 0x2161
0x002991A3: mov rax, qword ptr [rsi + 8]
0x002991A7: mov rcx, rsi
0x002991AA: mov rdx, qword ptr [rax + 0xc8]
0x002991B1: call qword ptr [rdx + 0x80]
0x002991B7: add rsp, 0x38
0x002991BB: pop r15
0x002991BD: pop r14
0x002991BF: pop r13
0x002991C1: pop r12
0x002991C3: pop rdi
0x002991C4: pop rsi
0x002991C5: pop rbx
0x002991C6: pop rbp
0x002991C7: ret
```

## 10. `0x00299691` in `0x00299220..0x002996F6`

```asm
0x002995C9: lea r8, [rsp + 0x3c]
0x002995CE: lea rcx, [rbp - 0x10]
0x002995D2: call 0x1402e1430
0x002995D7: test eax, eax
0x002995D9: je 0x1402996cf
0x002995DF: lea rcx, [rsp + 0x50]
0x002995E4: call 0x1402c45a0
0x002995E9: lea rcx, [rbp - 0x10]
0x002995ED: call 0x1402e1260
0x002995F2: mov r8, qword ptr [rsp + 0x30]
0x002995F7: mov rcx, qword ptr [rdi + 8]
0x002995FB: mov eax, dword ptr [rsp + 0x3c]
0x002995FF: mov rdx, qword ptr [rdi + 0x50]
0x00299603: add r8, rax
0x00299606: mov qword ptr [rsp + 0x30], r8
0x0029960B: mov rax, qword ptr [rcx + 0xc8]
0x00299612: sub r8d, dword ptr [rax + 0x74]
0x00299616: sub r8d, dword ptr [rdx + 8]
0x0029961A: mov dword ptr [rsp + 0x38], r8d
0x0029961F: mov rax, qword ptr [rcx + 0xc8]
0x00299626: mov rdx, qword ptr [rdx + 8]
0x0029962A: add rdx, 4
0x0029962E: mov ecx, dword ptr [rax + 0x74]
0x00299631: lea eax, [r8 - 6]
0x00299635: add rdx, rcx
0x00299638: sar eax, 8
0x0029963B: mov qword ptr [rsp + 0x30], rdx
0x00299640: mov byte ptr [rdx], al
0x00299642: mov edx, 4
0x00299647: mov rax, qword ptr [rsp + 0x30]
0x0029964C: movzx ecx, byte ptr [rsp + 0x38]
0x00299651: sub cl, 6
0x00299654: mov byte ptr [rax + 1], cl
0x00299657: mov rcx, rdi
0x0029965A: mov rax, qword ptr [rdi + 8]
0x0029965E: add qword ptr [rsp + 0x30], 2
0x00299664: mov r8d, dword ptr [rsp + 0x38]
0x00299669: mov r9, qword ptr [rax + 0xc8]
0x00299670: call qword ptr [r9 + 0x78]
0x00299674: mov rcx, r15
0x00299677: mov dword ptr [rdi + 0x48], 0x21f1
0x0029967E: call 0x1402d2350
0x00299683: mov rax, qword ptr [rdi + 8]
0x00299687: mov rcx, rdi
0x0029968A: mov rdx, qword ptr [rax + 0xc8]
0x00299691: call qword ptr [rdx + 0x80]
0x00299697: mov rcx, qword ptr [rbp + 0x130]
0x0029969E: xor rcx, rsp
0x002996A1: call 0x1403b24c0
0x002996A6: lea r11, [rsp + 0x240]
0x002996AE: mov rbx, qword ptr [r11 + 0x38]
0x002996B2: mov rsi, qword ptr [r11 + 0x40]
0x002996B6: mov rdi, qword ptr [r11 + 0x48]
0x002996BA: mov rsp, r11
0x002996BD: pop r15
0x002996BF: pop r14
0x002996C1: pop r13
0x002996C3: pop r12
0x002996C5: pop rbp
0x002996C6: ret
0x002996C7: mov rcx, rbx
0x002996CA: call 0x1402a63c0
0x002996CF: mov rcx, r15
0x002996D2: call 0x1402d2350
0x002996D7: lea rcx, [rsp + 0x50]
0x002996DC: call 0x1402c45a0
0x002996E1: lea rcx, [rbp - 0x10]
0x002996E5: call 0x1402e1260
0x002996EA: mov dword ptr [rdi + 0x48], 5
0x002996F1: or eax, 0xffffffff
0x002996F4: jmp 0x140299697
```

## 11. `0x00299A1B` in `0x00299957..0x00299A2F`

```asm
0x0029995E: mov byte ptr [rsi], al
0x00299960: mov rcx, rdi
0x00299963: inc rsi
0x00299966: call 0x1402e4ab0
0x0029996B: test eax, eax
0x0029996D: jg 0x1402999a9
0x0029996F: mov edx, 0xf2
0x00299974: mov dword ptr [rsp + 0x20], 0x617
0x0029997C: lea r9, [rip + 0x4f866d]
0x00299983: mov ecx, 0x14
0x00299988: lea r8d, [rdx + 0x21]
0x0029998C: call 0x1402c3c30
0x00299991: or eax, 0xffffffff
0x00299994: mov dword ptr [rdi + 0x48], 5
0x0029999B: mov rbp, qword ptr [rsp + 0x60]
0x002999A0: add rsp, 0x30
0x002999A4: pop r14
0x002999A6: pop rdi
0x002999A7: pop rsi
0x002999A8: ret
0x002999A9: lea r8, [rbp + 0x4000]
0x002999B0: mov rdx, rsi
0x002999B3: lea r9, [rsp + 0x50]
0x002999B8: mov rcx, rdi
0x002999BB: call 0x1402aa0c0
0x002999C0: mov rcx, rax
0x002999C3: mov edx, 2
0x002999C8: test rax, rax
0x002999CB: jne 0x1402999ee
0x002999CD: mov r8d, dword ptr [rsp + 0x50]
0x002999D2: mov rcx, rdi
0x002999D5: call 0x1402a8db0
0x002999DA: lea r9, [rip + 0x4f7d5f]
0x002999E1: mov dword ptr [rsp + 0x20], 0x61f
0x002999E9: jmp 0x1402998d0
0x002999EE: mov rax, qword ptr [rdi + 8]
0x002999F2: sub ecx, r14d
0x002999F5: mov r8d, ecx
0x002999F8: mov rcx, rdi
0x002999FB: mov r9, qword ptr [rax + 0xc8]
0x00299A02: call qword ptr [r9 + 0x78]
0x00299A06: mov dword ptr [rdi + 0x48], 0x2131
0x00299A0D: mov rax, qword ptr [rdi + 8]
0x00299A11: mov rcx, rdi
0x00299A14: mov rdx, qword ptr [rax + 0xc8]
0x00299A1B: call qword ptr [rdx + 0x80]
0x00299A21: mov rbp, qword ptr [rsp + 0x60]
0x00299A26: add rsp, 0x30
0x00299A2A: pop r14
0x00299A2C: pop rdi
0x00299A2D: pop rsi
0x00299A2E: ret
```

## 12. `0x0029A4B3` in `0x00299A30..0x0029A6E2`

```asm
0x0029A3F3: jle 0x14029a4e6
0x0029A3F9: movsxd rcx, dword ptr [rsp + 0x30]
0x0029A3FE: dec edi
0x0029A400: add r15, rcx
0x0029A403: add r12d, ecx
0x0029A406: test edi, edi
0x0029A408: jg 0x14029a340
0x0029A40E: mov rax, qword ptr [r13 + 0x20]
0x0029A412: lea r9, [rbx + 2]
0x0029A416: mov qword ptr [rsp + 0x28], rax
0x0029A41B: lea rdx, [rbp - 1]
0x0029A41F: lea rax, [rsp + 0x34]
0x0029A424: mov r8d, r12d
0x0029A427: mov ecx, 0x72
0x0029A42C: mov qword ptr [rsp + 0x20], rax
0x0029A431: call 0x1402da990
0x0029A436: test eax, eax
0x0029A438: jg 0x14029a461
0x0029A43A: mov ecx, 0x14
0x0029A43F: mov dword ptr [rsp + 0x20], 0x7cf
0x0029A447: lea r9, [rip + 0x4f7452]
0x0029A44E: mov edx, 0x9b
0x0029A453: lea r8d, [rcx - 0x10]
0x0029A457: call 0x1402c3c30
0x0029A45C: jmp 0x14029a6ac
0x0029A461: mov eax, dword ptr [rsp + 0x34]
0x0029A465: shr eax, 8
0x0029A468: mov byte ptr [rbx], al
0x0029A46A: movzx eax, byte ptr [rsp + 0x34]
0x0029A46F: mov byte ptr [rbx + 1], al
0x0029A472: mov eax, dword ptr [rsp + 0x34]
0x0029A476: add eax, 2
0x0029A479: add esi, eax
0x0029A47B: mov rax, qword ptr [r14 + 8]
0x0029A47F: mov r8d, esi
0x0029A482: mov edx, 0xc
0x0029A487: mov rcx, r14
0x0029A48A: mov rax, qword ptr [rax + 0xc8]
0x0029A491: call qword ptr [rax + 0x78]
0x0029A494: lea rcx, [rbp - 0x61]
0x0029A498: mov dword ptr [r14 + 0x48], 0x2151
0x0029A4A0: call 0x1402d57b0
0x0029A4A5: mov rax, qword ptr [r14 + 8]
0x0029A4A9: mov rcx, r14
0x0029A4AC: mov rdx, qword ptr [rax + 0xc8]
0x0029A4B3: call qword ptr [rdx + 0x80]
0x0029A4B9: mov rcx, qword ptr [rbp + 0x27]
0x0029A4BD: xor rcx, rsp
0x0029A4C0: call 0x1403b24c0
0x0029A4C5: lea r11, [rsp + 0x100]
0x0029A4CD: mov rbx, qword ptr [r11 + 0x38]
0x0029A4D1: mov rsi, qword ptr [r11 + 0x40]
0x0029A4D5: mov rdi, qword ptr [r11 + 0x48]
0x0029A4D9: mov rsp, r11
0x0029A4DC: pop r15
0x0029A4DE: pop r14
0x0029A4E0: pop r13
0x0029A4E2: pop r12
0x0029A4E4: pop rbp
0x0029A4E5: ret
0x0029A4E6: mov dword ptr [rsp + 0x20], 0x7c6
0x0029A4EE: lea r9, [rip + 0x4f739b]
0x0029A4F5: mov ecx, 0x14
0x0029A4FA: mov edx, 0x9b
0x0029A4FF: lea r8d, [rcx - 0xe]
0x0029A503: call 0x1402c3c30
0x0029A508: mov edi, 0x50
0x0029A50D: jmp 0x14029a69c
0x0029A512: mov rdx, qword ptr [rsp + 0x48]
0x0029A517: test rdx, rdx
0x0029A51A: je 0x14029a636
0x0029A520: mov rax, qword ptr [r14 + 8]
0x0029A524: mov rcx, qword ptr [rax + 0xc8]
0x0029A52B: test byte ptr [rcx + 0x70], 2
0x0029A52F: je 0x14029a567
0x0029A531: mov r8, rdx
0x0029A534: mov rcx, rbx
0x0029A537: mov rdx, r13
0x0029A53A: call 0x1402ac7a0
0x0029A53F: test eax, eax
```

## 13. `0x0029BD44` in `0x0029B930..0x0029BD63`

```asm
0x0029BC87: movzx ecx, byte ptr [rax]
0x0029BC8A: mov byte ptr [rbx], cl
0x0029BC8C: inc rbx
0x0029BC8F: cmp ebp, esi
0x0029BC91: jl 0x14029bc70
0x0029BC93: mov rcx, rdi
0x0029BC96: mov byte ptr [rbx], 0
0x0029BC99: call 0x1402aaea0
0x0029BC9E: test eax, eax
0x0029BCA0: jg 0x14029bcce
0x0029BCA2: mov edx, 0x83
0x0029BCA7: mov dword ptr [rsp + 0x20], 0x365
0x0029BCAF: lea r9, [rip + 0x4f698a]
0x0029BCB6: lea ecx, [rdx - 0x6f]
0x0029BCB9: lea r8d, [rdx + 0x5f]
0x0029BCBD: call 0x1402c3c30
0x0029BCC2: or eax, 0xffffffff
0x0029BCC5: mov dword ptr [rdi + 0x48], 5
0x0029BCCC: jmp 0x14029bd4a
0x0029BCCE: lea r8, [r15 + 0x4000]
0x0029BCD5: mov rcx, rdi
0x0029BCD8: lea rdx, [rbx + 1]
0x0029BCDC: lea r9, [rsp + 0x50]
0x0029BCE1: call 0x1402a9490
0x0029BCE6: mov rcx, rax
0x0029BCE9: test rax, rax
0x0029BCEC: jne 0x14029bd12
0x0029BCEE: mov r8d, dword ptr [rsp + 0x50]
0x0029BCF3: lea edx, [rax + 2]
0x0029BCF6: mov rcx, rdi
0x0029BCF9: call 0x1402a8db0
0x0029BCFE: lea r9, [rip + 0x4f694b]
0x0029BD05: mov dword ptr [rsp + 0x20], 0x36c
0x0029BD0D: jmp 0x14029bb32
0x0029BD12: mov rax, qword ptr [rdi + 8]
0x0029BD16: sub ecx, r14d
0x0029BD19: mov r8d, ecx
0x0029BD1C: mov edx, 1
0x0029BD21: mov rcx, rdi
0x0029BD24: mov r9, qword ptr [rax + 0xc8]
0x0029BD2B: call qword ptr [r9 + 0x78]
0x0029BD2F: mov dword ptr [rdi + 0x48], 0x1111
0x0029BD36: mov rax, qword ptr [rdi + 8]
0x0029BD3A: mov rcx, rdi
0x0029BD3D: mov rdx, qword ptr [rax + 0xc8]
0x0029BD44: call qword ptr [rdx + 0x80]
0x0029BD4A: mov rbx, qword ptr [rsp + 0x58]
0x0029BD4F: mov rbp, qword ptr [rsp + 0x60]
0x0029BD54: mov rsi, qword ptr [rsp + 0x68]
0x0029BD59: add rsp, 0x30
0x0029BD5D: pop r15
0x0029BD5F: pop r14
0x0029BD61: pop rdi
0x0029BD62: ret
```

## 14. `0x0029ED42` in `0x0029ED34..0x0029ED58`

```asm
0x0029ED34: mov rax, qword ptr [rbx + 8]
0x0029ED38: mov rcx, rbx
0x0029ED3B: mov rdx, qword ptr [rax + 0xc8]
0x0029ED42: call qword ptr [rdx + 0x80]
0x0029ED48: mov rsi, qword ptr [rsp + 0x60]
0x0029ED4D: mov rbx, qword ptr [rsp + 0x68]
0x0029ED52: add rsp, 0x40
0x0029ED56: pop rdi
0x0029ED57: ret
```

## 15. `0x0029F499` in `0x0029ED60..0x0029FB8B`

```asm
0x0029F3D9: mov rbx, rax
0x0029F3DC: call 0x1402d23f0
0x0029F3E1: mov r12, rax
0x0029F3E4: call 0x1402d8a00
0x0029F3E9: mov qword ptr [rsp + 0x48], rax
0x0029F3EE: test r12, r12
0x0029F3F1: je 0x14029f4cf
0x0029F3F7: test rax, rax
0x0029F3FA: je 0x14029f4cf
0x0029F400: mov rcx, r14
0x0029F403: movsxd rbx, ebx
0x0029F406: call 0x1402dde50
0x0029F40B: mov rdx, rax
0x0029F40E: mov r9, r12
0x0029F411: mov rax, qword ptr [rsp + 0x48]
0x0029F416: mov r8d, 4
0x0029F41C: mov qword ptr [rsp + 0x28], rax
0x0029F421: mov rcx, rdi
0x0029F424: mov qword ptr [rsp + 0x20], rbx
0x0029F429: call 0x1402e05c0
0x0029F42E: mov r14, rax
0x0029F431: movsxd r8, eax
0x0029F434: lea rcx, [r15 + 1]
0x0029F438: mov byte ptr [r15], r14b
0x0029F43B: mov rdx, r12
0x0029F43E: call 0x1403d1f90
0x0029F443: mov rcx, qword ptr [rsp + 0x48]
0x0029F448: inc r14d
0x0029F44B: call 0x1402d8930
0x0029F450: mov rcx, r12
0x0029F453: call 0x1402d2350
0x0029F458: mov rcx, qword ptr [rsp + 0x30]
0x0029F45D: call 0x1402e09e0
0x0029F462: mov rcx, r13
0x0029F465: call 0x1402d5da0
0x0029F46A: mov rax, qword ptr [rsi + 8]
0x0029F46E: mov r8d, r14d
0x0029F471: mov edx, 0x10
0x0029F476: mov rcx, rsi
0x0029F479: mov r9, qword ptr [rax + 0xc8]
0x0029F480: call qword ptr [r9 + 0x78]
0x0029F484: mov dword ptr [rsi + 0x48], 0x1181
0x0029F48B: mov rax, qword ptr [rsi + 8]
0x0029F48F: mov rcx, rsi
0x0029F492: mov rdx, qword ptr [rax + 0xc8]
0x0029F499: call qword ptr [rdx + 0x80]
0x0029F49F: mov rcx, qword ptr [rbp + 0x2c0]
0x0029F4A6: xor rcx, rsp
0x0029F4A9: call 0x1403b24c0
0x0029F4AE: lea r11, [rsp + 0x3d0]
0x0029F4B6: mov rbx, qword ptr [r11 + 0x38]
0x0029F4BA: mov rsi, qword ptr [r11 + 0x40]
0x0029F4BE: mov rdi, qword ptr [r11 + 0x48]
0x0029F4C2: mov rsp, r11
0x0029F4C5: pop r15
0x0029F4C7: pop r14
0x0029F4C9: pop r13
0x0029F4CB: pop r12
0x0029F4CD: pop rbp
0x0029F4CE: ret
0x0029F4CF: mov dword ptr [rsp + 0x20], 0xb8e
0x0029F4D7: lea r9, [rip + 0x4f2f62]
0x0029F4DE: jmp 0x14029f296
0x0029F4E3: mov dword ptr [rsp + 0x20], 0xb39
0x0029F4EB: lea r9, [rip + 0x4f2eae]
0x0029F4F2: jmp 0x14029ee13
0x0029F4F7: mov dword ptr [rsp + 0x20], 0xb2d
0x0029F4FF: lea r9, [rip + 0x4f2e8a]
0x0029F506: jmp 0x14029ee13
0x0029F50B: bt eax, 9
0x0029F50F: jae 0x14029f78c
0x0029F515: mov rax, qword ptr [rsi + 0x130]
0x0029F51C: mov rdx, qword ptr [rax + 0xa8]
0x0029F523: mov rcx, qword ptr [rdx + 0x1a0]
0x0029F52A: test rcx, rcx
0x0029F52D: jne 0x14029f564
0x0029F52F: mov rcx, qword ptr [rdx + 0x168]
0x0029F536: test rcx, rcx
0x0029F539: jne 0x14029f564
0x0029F53B: lea r9, [rip + 0x4f2f0e]
```

## 16. `0x0029FF9F` in `0x0029FB90..0x002A000E`

```asm
0x0029FEED: call 0x1402de890
0x0029FEF2: test eax, eax
0x0029FEF4: jg 0x14029ff0a
0x0029FEF6: mov dword ptr [rsp + 0x20], 0xd14
0x0029FEFE: lea r9, [rip + 0x4f26fb]
0x0029FF05: jmp 0x14029ffdc
0x0029FF0A: mov dword ptr [rsp + 0x30], edi
0x0029FF0E: lea rdx, [rbp + 0x25]
0x0029FF12: lea eax, [rdi + 2]
0x0029FF15: movsxd rcx, eax
0x0029FF18: movzx eax, byte ptr [rdx + 1]
0x0029FF1C: lea rdx, [rdx - 2]
0x0029FF20: mov byte ptr [rcx + rbx], al
0x0029FF23: mov eax, dword ptr [rsp + 0x30]
0x0029FF27: inc eax
0x0029FF29: mov dword ptr [rsp + 0x30], eax
0x0029FF2D: add eax, 2
0x0029FF30: movsxd rcx, eax
0x0029FF33: movzx eax, byte ptr [rdx + 2]
0x0029FF37: mov byte ptr [rcx + rbx], al
0x0029FF3A: mov edi, dword ptr [rsp + 0x30]
0x0029FF3E: inc edi
0x0029FF40: mov dword ptr [rsp + 0x30], edi
0x0029FF44: sub r14, 1
0x0029FF48: jne 0x14029ff12
0x0029FF4A: sar edi, 8
0x0029FF4D: mov byte ptr [rbx], dil
0x0029FF50: movzx eax, byte ptr [rsp + 0x30]
0x0029FF55: mov byte ptr [rbx + 1], al
0x0029FF58: mov ebx, dword ptr [rsp + 0x30]
0x0029FF5C: add ebx, 2
0x0029FF5F: mov rax, qword ptr [rsi + 8]
0x0029FF63: mov r8d, ebx
0x0029FF66: mov edx, 0xf
0x0029FF6B: mov rcx, rsi
0x0029FF6E: mov r9, qword ptr [rax + 0xc8]
0x0029FF75: call qword ptr [r9 + 0x78]
0x0029FF79: mov dword ptr [rsi + 0x48], 0x1191
0x0029FF80: lea rcx, [rbp - 0x79]
0x0029FF84: call 0x1402d57b0
0x0029FF89: mov rcx, r15
0x0029FF8C: call 0x1402ddde0
0x0029FF91: mov rax, qword ptr [rsi + 8]
0x0029FF95: mov rcx, rsi
0x0029FF98: mov rdx, qword ptr [rax + 0xc8]
0x0029FF9F: call qword ptr [rdx + 0x80]
0x0029FFA5: mov rcx, qword ptr [rbp + 0x27]
0x0029FFA9: xor rcx, rsp
0x0029FFAC: call 0x1403b24c0
0x0029FFB1: lea r11, [rsp + 0xf0]
0x0029FFB9: mov rbx, qword ptr [r11 + 0x38]
0x0029FFBD: mov rsi, qword ptr [r11 + 0x40]
0x0029FFC1: mov rsp, r11
0x0029FFC4: pop r15
0x0029FFC6: pop r14
0x0029FFC8: pop r12
0x0029FFCA: pop rdi
0x0029FFCB: pop rbp
0x0029FFCC: ret
0x0029FFCD: mov dword ptr [rsp + 0x20], 0xcbc
0x0029FFD5: lea r9, [rip + 0x4f2594]
0x0029FFDC: mov r8d, 0x44
0x0029FFE2: mov edx, 0x99
0x0029FFE7: mov ecx, 0x14
0x0029FFEC: call 0x1402c3c30
0x0029FFF1: lea rcx, [rbp - 0x79]
0x0029FFF5: call 0x1402d57b0
0x0029FFFA: mov rcx, r15
0x0029FFFD: call 0x1402ddde0
0x002A0002: or eax, 0xffffffff
0x002A0005: mov dword ptr [rsi + 0x48], 5
0x002A000C: jmp 0x14029ffa5
```

## 17. `0x002B2346` in `0x002B2338..0x002B2362`

```asm
0x002B2338: mov rax, qword ptr [rbx + 8]
0x002B233C: mov rcx, rbx
0x002B233F: mov rdx, qword ptr [rax + 0xc8]
0x002B2346: call qword ptr [rdx + 0x80]
0x002B234C: mov rbx, qword ptr [rsp + 0x38]
0x002B2351: mov rbp, qword ptr [rsp + 0x40]
0x002B2356: mov rdi, qword ptr [rsp + 0x48]
0x002B235B: add rsp, 0x20
0x002B235F: pop r14
0x002B2361: ret
```

## 18. `0x002CBE93` in `0x002CBE60..0x002CBF32`

```asm
0x002CBE60: mov qword ptr [rsp + 8], rbx
0x002CBE65: mov qword ptr [rsp + 0x10], rbp
0x002CBE6A: mov qword ptr [rsp + 0x18], rsi
0x002CBE6F: push rdi
0x002CBE70: mov eax, 0x30
0x002CBE75: call 0x1403b2500
0x002CBE7A: sub rsp, rax
0x002CBE7D: mov rbx, rcx
0x002CBE80: mov rbp, rdx
0x002CBE83: mov rcx, rdx
0x002CBE86: xor esi, esi
0x002CBE88: call 0x1402cc580
0x002CBE8D: mov rdx, rax
0x002CBE90: mov rcx, rbx
0x002CBE93: call qword ptr [rbx + 0x80]
0x002CBE99: mov rdi, rax
0x002CBE9C: test rax, rax
0x002CBE9F: je 0x1402cbf1d
0x002CBEA1: mov rcx, rdi
0x002CBEA4: xor ebx, ebx
0x002CBEA6: call 0x1402c7350
0x002CBEAB: test eax, eax
0x002CBEAD: jle 0x1402cbeda
0x002CBEAF: nop
0x002CBEB0: mov edx, ebx
0x002CBEB2: mov rcx, rdi
0x002CBEB5: call 0x1402c7510
0x002CBEBA: mov rdx, rbp
0x002CBEBD: mov rcx, rax
0x002CBEC0: mov rsi, rax
0x002CBEC3: call 0x1402cc480
0x002CBEC8: test eax, eax
0x002CBECA: je 0x1402cbeda
0x002CBECC: mov rcx, rdi
0x002CBECF: inc ebx
0x002CBED1: call 0x1402c7350
0x002CBED6: cmp ebx, eax
0x002CBED8: jl 0x1402cbeb0
0x002CBEDA: mov rcx, rdi
0x002CBEDD: call 0x1402c7350
0x002CBEE2: cmp ebx, eax
0x002CBEE4: jge 0x1402cbf09
0x002CBEE6: mov edx, 1
0x002CBEEB: mov dword ptr [rsp + 0x20], 0xb5
0x002CBEF3: lea rcx, [rsi + 0x1c]
0x002CBEF7: lea r9, [rip + 0x4d4c7a]
0x002CBEFE: lea r8d, [rdx + 2]
0x002CBF02: call 0x1402c1d30
0x002CBF07: jmp 0x1402cbf0b
```

## 19. `0x003388E7` in `0x003381A0..0x00338B05`

```asm
0x00338827: lea rcx, [rsp + 0xe8]
0x0033882F: call r12
0x00338832: test eax, eax
0x00338834: je 0x140338854
0x00338836: test r14, r14
0x00338839: je 0x14033884a
0x0033883B: call qword ptr [rip + 0xf7d2f]
0x00338841: sub eax, edi
0x00338843: cmp eax, 0x3e8
0x00338848: jae 0x140338854
0x0033884A: dec ebx
0x0033884C: mov dword ptr [rsp + 0x68], ebx
0x00338850: test ebx, ebx
0x00338852: jg 0x140338810
0x00338854: jmp 0x14033888a
0x00338856: mov r15d, dword ptr [rsp + 0x30]
0x0033885B: dec r15d
0x0033885E: mov dword ptr [rsp + 0x30], r15d
0x00338863: mov edi, dword ptr [rsp + 0x58]
0x00338867: mov r12, qword ptr [rsp + 0xa8]
0x0033886F: mov rsi, qword ptr [rsp + 0xb0]
0x00338877: mov r14, qword ptr [rsp + 0xb8]
0x0033887F: mov r13d, r14d
0x00338882: movsd xmm6, qword ptr [rip + 0x185ba6]
0x0033888A: lea rdx, [rsp + 0x120]
0x00338892: mov rcx, rsi
0x00338895: call qword ptr [rsp + 0xc0]
0x0033889C: test eax, eax
0x0033889E: je 0x1403388bd
0x003388A0: test r13d, r13d
0x003388A3: je 0x1403388b4
0x003388A5: call qword ptr [rip + 0xf7cc5]
0x003388AB: sub eax, edi
0x003388AD: cmp eax, 0x3e8
0x003388B2: jae 0x1403388bd
0x003388B4: test r15d, r15d
0x003388B7: jg 0x140338780
0x003388BD: mov r15, qword ptr [rsp + 0x78]
0x003388C2: mov dword ptr [rsp + 0x1a0], 0x238
0x003388CD: cmp dword ptr [rsp + 0x70], 0
0x003388D2: je 0x1403388dc
0x003388D4: call qword ptr [rip + 0xf7c96]
0x003388DA: mov edi, eax
0x003388DC: lea rdx, [rsp + 0x1a0]
0x003388E4: mov rcx, rsi
0x003388E7: call qword ptr [rsp + 0x80]
0x003388EE: movsd xmm6, qword ptr [rip + 0x3bd2b2]
0x003388F6: test eax, eax
0x003388F8: je 0x140338950
0x003388FA: mov rbx, qword ptr [rsp + 0xc8]
0x00338902: mov r15, qword ptr [rsp + 0x88]
0x0033890A: nop word ptr [rax + rax]
0x00338910: movaps xmm2, xmm6
0x00338913: mov edx, dword ptr [rsp + 0x1a0]
0x0033891A: lea rcx, [rsp + 0x1a0]
0x00338922: call 0x1402d8260
0x00338927: lea rdx, [rsp + 0x1a0]
0x0033892F: mov rcx, rsi
0x00338932: call r15
0x00338935: test eax, eax
0x00338937: je 0x14033894d
0x00338939: test rbx, rbx
0x0033893C: je 0x140338910
0x0033893E: call qword ptr [rip + 0xf7c2c]
0x00338944: sub eax, edi
0x00338946: cmp eax, 0x3e8
0x0033894B: jb 0x140338910
0x0033894D: mov r15, rbx
0x00338950: mov dword ptr [rsp + 0x140], 0x1c
0x0033895B: cmp dword ptr [rsp + 0x74], 0
0x00338960: je 0x14033896a
0x00338962: call qword ptr [rip + 0xf7c08]
0x00338968: mov edi, eax
0x0033896A: lea rdx, [rsp + 0x140]
0x00338972: mov rcx, rsi
0x00338975: call qword ptr [rsp + 0x90]
0x0033897C: test eax, eax
0x0033897E: je 0x1403389e0
0x00338980: movsd xmm7, qword ptr [rip + 0x106b98]
0x00338988: mov rbx, qword ptr [rsp + 0xd0]
```

## 20. `0x003844F4` in `0x00384380..0x0038460B`

```asm
0x0038442F: mov r8, rax
0x00384432: lea rdx, [rip + 0x37f27f]
0x00384439: mov rcx, rsi
0x0038443C: call 0x140377140
0x00384441: mov r8, qword ptr [rdi + 0xb8]
0x00384448: test r8, r8
0x0038444B: jne 0x140384456
0x0038444D: lea eax, [r8 + 0x1b]
0x00384451: jmp 0x1403845f4
0x00384456: mov rdx, qword ptr [rbx + 0x18]
0x0038445A: lea rax, [rbp - 9]
0x0038445E: mov r9d, dword ptr [rbx + 0x68]
0x00384462: lea rcx, [rbx + 0x6c]
0x00384466: mov qword ptr [rbp + 0x2f], rax
0x0038446A: mov qword ptr [rbp - 9], r15
0x0038446E: lea rax, [rdx + 0x10]
0x00384472: mov qword ptr [rbp - 1], r15
0x00384476: mov qword ptr [rsp + 0x58], rax
0x0038447B: lea rax, [rbp + 0x27]
0x0038447F: mov qword ptr [rsp + 0x50], rcx
0x00384484: mov rcx, qword ptr [rbx + 0x10]
0x00384488: mov qword ptr [rsp + 0x48], rax
0x0038448D: mov rax, qword ptr [rip + 0x467e8c]
0x00384494: mov qword ptr [rsp + 0x40], rdx
0x00384499: mov dword ptr [rsp + 0x38], r15d
0x0038449E: mov qword ptr [rsp + 0x30], r15
0x003844A3: mov dword ptr [rsp + 0x28], r15d
0x003844A8: mov dword ptr [rsp + 0x20], r15d
0x003844AD: mov dword ptr [rbp + 0x27], r15d
0x003844B1: mov dword ptr [rbp + 0x2b], 1
0x003844B8: call qword ptr [rax + 0x30]
0x003844BB: test eax, eax
0x003844BD: je 0x1403844c6
0x003844BF: cmp eax, 0x90317
0x003844C4: jne 0x140384524
0x003844C6: mov r9d, dword ptr [rbp - 9]
0x003844CA: lea rax, [rbp + 0x67]
0x003844CE: mov r8, qword ptr [rbp - 1]
0x003844D2: mov rcx, rdi
0x003844D5: mov rdx, qword ptr [rdi + r14*8 + 0x1d0]
0x003844DD: mov qword ptr [rsp + 0x20], rax
0x003844E2: call 0x140377650
0x003844E7: mov rdx, qword ptr [rip + 0x467e32]
0x003844EE: mov edi, eax
0x003844F0: mov rcx, qword ptr [rbp - 1]
0x003844F4: call qword ptr [rdx + 0x80]
0x003844FA: test edi, edi
0x003844FC: jne 0x140384507
0x003844FE: mov ecx, dword ptr [rbp - 9]
0x00384501: cmp rcx, qword ptr [rbp + 0x67]
0x00384505: je 0x140384524
0x00384507: mov ecx, edi
0x00384509: call 0x140389300
0x0038450E: mov r9, qword ptr [rbp + 0x67]
0x00384512: lea rdx, [rip + 0x37f1c7]
0x00384519: mov r8, rax
0x0038451C: mov rcx, rsi
0x0038451F: call 0x140377200
0x00384524: cmp qword ptr [rbx + 0x18], r15
0x00384528: je 0x140384555
0x0038452A: lea rdx, [rip + 0x37f1ef]
0x00384531: mov rcx, rsi
0x00384534: call 0x140377200
0x00384539: mov rax, qword ptr [rip + 0x467de0]
0x00384540: mov rcx, qword ptr [rbx + 0x18]
0x00384544: call qword ptr [rax + 0x48]
0x00384547: mov rcx, qword ptr [rbx + 0x18]
0x0038454B: call qword ptr [rip + 0x45226f]
0x00384551: mov qword ptr [rbx + 0x18], r15
0x00384555: mov rcx, qword ptr [rbx + 0x10]
0x00384559: test rcx, rcx
0x0038455C: je 0x1403845bc
0x0038455E: mov eax, dword ptr [rcx + 0x18]
0x00384561: test eax, eax
0x00384563: jle 0x140384581
0x00384565: dec eax
0x00384567: lea rdx, [rip + 0x37f1e2]
0x0038456E: mov dword ptr [rcx + 0x18], eax
0x00384571: mov rcx, rsi
0x00384574: mov rax, qword ptr [rbx + 0x10]
```

## 21. `0x00384C36` in `0x003847F0..0x00384CAB`

```asm
0x00384B6D: mov qword ptr [rsp + 0x50], rcx
0x00384B72: mov rcx, qword ptr [rsi + 0x10]
0x00384B76: mov qword ptr [rsp + 0x48], rax
0x00384B7B: lea rax, [rbp - 0x80]
0x00384B7F: mov qword ptr [rsp + 0x40], rdx
0x00384B84: xor edx, edx
0x00384B86: mov dword ptr [rsp + 0x38], r15d
0x00384B8B: mov qword ptr [rsp + 0x30], rax
0x00384B90: mov rax, qword ptr [rip + 0x467789]
0x00384B97: mov dword ptr [rsp + 0x28], r15d
0x00384B9C: mov dword ptr [rsp + 0x20], r15d
0x00384BA1: call qword ptr [rax + 0x30]
0x00384BA4: cmp eax, 0x90312
0x00384BA9: je 0x140384bf1
0x00384BAB: mov rcx, rbx
0x00384BAE: cmp eax, 0x80090322
0x00384BB3: jne 0x140384bc5
0x00384BB5: mov edx, eax
0x00384BB7: call 0x140388a20
0x00384BBC: lea rdx, [rip + 0x37de05]
0x00384BC3: jmp 0x140384bd3
0x00384BC5: mov edx, eax
0x00384BC7: call 0x140388a20
0x00384BCC: lea rdx, [rip + 0x37dec5]
0x00384BD3: mov r8, rax
0x00384BD6: mov rcx, rdi
0x00384BD9: call 0x140377140
0x00384BDE: mov rcx, qword ptr [rsi + 0x18]
0x00384BE2: call qword ptr [rip + 0x451bd8]
0x00384BE8: mov qword ptr [rsi + 0x18], r15
0x00384BEC: jmp 0x140384c80
0x00384BF1: mov r8d, dword ptr [rsp + 0x60]
0x00384BF6: lea rdx, [rip + 0x37ded3]
0x00384BFD: mov rcx, rdi
0x00384C00: call 0x140377200
0x00384C05: mov r9d, dword ptr [rsp + 0x60]
0x00384C0A: lea rax, [rbp - 0x68]
0x00384C0E: mov r8, qword ptr [rsp + 0x68]
0x00384C13: mov rcx, rbx
0x00384C16: mov rdx, qword ptr [rbx + r14*8 + 0x1d0]
0x00384C1E: mov qword ptr [rsp + 0x20], rax
0x00384C23: call 0x140377650
0x00384C28: mov rdx, qword ptr [rip + 0x4676f1]
0x00384C2F: mov ebx, eax
0x00384C31: mov rcx, qword ptr [rsp + 0x68]
0x00384C36: call qword ptr [rdx + 0x80]
0x00384C3C: mov r8, qword ptr [rbp - 0x68]
0x00384C40: mov r9d, dword ptr [rsp + 0x60]
0x00384C45: test ebx, ebx
0x00384C47: jne 0x140384c71
0x00384C49: cmp r9, r8
0x00384C4C: jne 0x140384c71
0x00384C4E: lea rdx, [rip + 0x37df03]
0x00384C55: mov rcx, rdi
0x00384C58: call 0x140377200
0x00384C5D: xor eax, eax
0x00384C5F: mov dword ptr [rsi + 0x70], r15d
0x00384C63: mov word ptr [rsi + 0x74], r15w
0x00384C68: mov dword ptr [rsi + 8], 1
0x00384C6F: jmp 0x140384c85
0x00384C71: lea rdx, [rip + 0x37de98]
0x00384C78: mov rcx, rdi
0x00384C7B: call 0x140377140
0x00384C80: mov eax, 0x23
0x00384C85: mov rcx, qword ptr [rbp + 0xa0]
0x00384C8C: xor rcx, rsp
0x00384C8F: call 0x1403b24c0
0x00384C94: mov rbx, qword ptr [rsp + 0x1f0]
0x00384C9C: add rsp, 0x1b0
0x00384CA3: pop r15
0x00384CA5: pop r14
0x00384CA7: pop rdi
0x00384CA8: pop rsi
0x00384CA9: pop rbp
0x00384CAA: ret
```

## 22. `0x00384FEB` in `0x00384DF0..0x0038509B`

```asm
0x00384F26: mov qword ptr [rsp + 0x40], rsi
0x00384F2B: mov dword ptr [rsp + 0x38], esi
0x00384F2F: mov qword ptr [rsp + 0x30], rax
0x00384F34: mov rax, qword ptr [rip + 0x4673e5]
0x00384F3B: mov dword ptr [rsp + 0x28], esi
0x00384F3F: mov dword ptr [rsp + 0x20], esi
0x00384F43: call qword ptr [rax + 0x30]
0x00384F46: mov rcx, qword ptr [rbp - 0x61]
0x00384F4A: mov r15d, eax
0x00384F4D: call qword ptr [rip + 0x45186d]
0x00384F53: mov qword ptr [rbp - 0x61], rsi
0x00384F57: cmp r15d, 0x80090318
0x00384F5E: je 0x14038517f
0x00384F64: cmp r15d, 0x90320
0x00384F6B: je 0x140385137
0x00384F71: cmp r15d, 0x90312
0x00384F78: je 0x140384f83
0x00384F7A: test r15d, r15d
0x00384F7D: jne 0x1403850c0
0x00384F83: lea rbx, [rbp - 0x19]
0x00384F87: cmp dword ptr [rbx + 4], 2
0x00384F8B: jne 0x140384fdb
0x00384F8D: mov r8d, dword ptr [rbx]
0x00384F90: test r8d, r8d
0x00384F93: je 0x140384fdb
0x00384F95: lea rdx, [rip + 0x37dd84]
0x00384F9C: mov rcx, r14
0x00384F9F: call 0x140377200
0x00384FA4: mov r9d, dword ptr [rbx]
0x00384FA7: lea rax, [rbp - 0x41]
0x00384FAB: mov r8, qword ptr [rbx + 8]
0x00384FAF: mov rcx, r12
0x00384FB2: mov rdx, qword ptr [r12 + r13*8 + 0x1d0]
0x00384FBA: mov qword ptr [rsp + 0x20], rax
0x00384FBF: call 0x140377650
0x00384FC4: mov r8, qword ptr [rbp - 0x41]
0x00384FC8: test eax, eax
0x00384FCA: jne 0x1403850dd
0x00384FD0: mov eax, dword ptr [rbx]
0x00384FD2: cmp rax, r8
0x00384FD5: jne 0x1403850dd
0x00384FDB: mov rcx, qword ptr [rbx + 8]
0x00384FDF: test rcx, rcx
0x00384FE2: je 0x140384ff1
0x00384FE4: mov rax, qword ptr [rip + 0x467335]
0x00384FEB: call qword ptr [rax + 0x80]
0x00384FF1: inc esi
0x00384FF3: add rbx, 0x10
0x00384FF7: cmp esi, 3
0x00384FFA: jl 0x140384f87
0x00384FFC: cmp dword ptr [rbp - 0x55], 5
0x00385000: jne 0x1403850fe
0x00385006: mov r8d, dword ptr [rbp - 0x59]
0x0038500A: test r8d, r8d
0x0038500D: je 0x1403850fe
0x00385013: lea rdx, [rip + 0x37ddc6]
0x0038501A: mov rcx, r14
0x0038501D: call 0x140377200
0x00385022: mov r8d, dword ptr [rbp - 0x59]
0x00385026: mov rdx, qword ptr [rdi + 0x48]
0x0038502A: cmp rdx, r8
0x0038502D: jbe 0x140385106
0x00385033: mov rcx, qword ptr [rdi + 0x58]
0x00385037: sub rdx, r8
0x0038503A: add rdx, rcx
0x0038503D: call 0x1403d1f90
0x00385042: mov eax, dword ptr [rbp - 0x59]
0x00385045: mov qword ptr [rdi + 0x48], rax
0x00385049: cmp r15d, 0x90312
0x00385050: jne 0x14038511b
0x00385056: xor bl, bl
0x00385058: xor esi, esi
0x0038505A: jmp 0x140384df8
0x0038505F: lea rdx, [rip + 0x37dbca]
0x00385066: mov rcx, r14
0x00385069: call 0x140377140
0x0038506E: mov eax, 0x23
0x00385073: jmp 0x140385093
0x00385075: cmp dword ptr [rdi + 8], 3
0x00385079: je 0x140385082
```

## 23. `0x0038B8B6` in `0x0038B8A2..0x0038BB3D`

```asm
0x0038B8A2: mov qword ptr [rsp + 0x180], rdi
0x0038B8AA: mov qword ptr [rsp + 0x140], r12
0x0038B8B2: mov r12d, dword ptr [rcx + 8]
0x0038B8B6: call qword ptr [rax + 0x80]
0x0038B8BC: mov ecx, r12d
0x0038B8BF: call qword ptr [rip + 0x44aef3]
0x0038B8C5: mov rdi, rax
0x0038B8C8: test rax, rax
0x0038B8CB: je 0x14038bacb
0x0038B8D1: test rbx, rbx
0x0038B8D4: je 0x14038b90f
0x0038B8D6: cmp byte ptr [rbx], 0
0x0038B8D9: je 0x14038b90f
0x0038B8DB: lea r8, [rbp - 0x48]
0x0038B8DF: mov rdx, r15
0x0038B8E2: mov rcx, rbx
0x0038B8E5: call 0x14036dd00
0x0038B8EA: test eax, eax
0x0038B8EC: jne 0x14038bacb
0x0038B8F2: mov rcx, qword ptr [r14]
0x0038B8F5: lea rdx, [rbp - 0x48]
0x0038B8F9: call 0x14038bc00
0x0038B8FE: test eax, eax
0x0038B900: jne 0x14038bacb
0x0038B906: lea rbx, [rbp - 0x48]
0x0038B90A: xor r15d, r15d
0x0038B90D: jmp 0x14038b915
0x0038B90F: xor r15d, r15d
0x0038B912: mov ebx, r15d
0x0038B915: lea rax, [rbp - 0x70]
0x0038B919: xor r9d, r9d
0x0038B91C: mov qword ptr [rsp + 0x40], rax
0x0038B921: lea rdx, [rip + 0x37aa88]
0x0038B928: lea rax, [rbp - 0x18]
0x0038B92C: xor ecx, ecx
0x0038B92E: mov qword ptr [rsp + 0x38], rax
0x0038B933: mov rax, qword ptr [rip + 0x4609e6]
0x0038B93A: lea r8d, [r9 + 2]
```

## 24. `0x0038BD9E` in `0x0038BD40..0x0038BDC1`

```asm
0x0038BD40: mov qword ptr [rsp + 0x18], rbx
0x0038BD45: push rbp
0x0038BD46: push rdi
0x0038BD47: push r14
0x0038BD49: sub rsp, 0xa0
0x0038BD50: mov rdi, rcx
0x0038BD53: mov r14, r9
0x0038BD56: mov rcx, r8
0x0038BD59: mov rbx, r8
0x0038BD5C: mov rbp, rdx
0x0038BD5F: call 0x14038c190
0x0038BD64: mov rax, qword ptr [rip + 0x4605b5]
0x0038BD6B: lea rdx, [rsp + 0x68]
0x0038BD70: lea rcx, [rip + 0x37510d]
0x0038BD77: call qword ptr [rax + 0x88]
0x0038BD7D: test eax, eax
0x0038BD7F: je 0x14038bd8b
0x0038BD81: mov eax, 4
0x0038BD86: jmp 0x14038bf8e
0x0038BD8B: mov rcx, qword ptr [rsp + 0x68]
0x0038BD90: mov eax, dword ptr [rcx + 8]
0x0038BD93: mov qword ptr [rbx + 0x50], rax
0x0038BD97: mov rax, qword ptr [rip + 0x460582]
0x0038BD9E: call qword ptr [rax + 0x80]
0x0038BDA4: mov rcx, qword ptr [rbx + 0x50]
0x0038BDA8: call qword ptr [rip + 0x44aa0a]
0x0038BDAE: mov qword ptr [rbx + 0x58], rax
0x0038BDB2: test rax, rax
0x0038BDB5: jne 0x14038bdc1
0x0038BDB7: mov eax, 0x1b
0x0038BDBC: jmp 0x14038bf8e
```

## 25. `0x0038C4A9` in `0x0038C220..0x0038CE78`

```asm
0x0038C3E6: lea edx, [rax - 0x90312]
0x0038C3EC: cmp edx, 2
0x0038C3EF: jbe 0x14038c440
0x0038C3F1: mov edx, eax
0x0038C3F3: mov rcx, r14
0x0038C3F6: call 0x140388a20
0x0038C3FB: mov rcx, qword ptr [r14]
0x0038C3FE: lea r8, [rip + 0x37a063]
0x0038C405: mov r9, rax
0x0038C408: lea rdx, [rip + 0x37a019]
0x0038C40F: call 0x140377140
0x0038C414: lea rdx, [rip + 0x37a06d]
0x0038C41B: mov rcx, rsi
0x0038C41E: call 0x140377140
0x0038C423: mov rcx, r15
0x0038C426: call qword ptr [rip + 0x44a394]
0x0038C42C: mov rax, qword ptr [rip + 0x45feed]
0x0038C433: lea rcx, [rbp + 8]
0x0038C437: call qword ptr [rax + 0x20]
0x0038C43A: jmp 0x14038ce4c
0x0038C43F: nop
0x0038C440: lea rax, [rbp - 0x40]
0x0038C444: mov r9d, 0x116
0x0038C44A: mov qword ptr [rsp + 0x58], rax
0x0038C44F: lea rcx, [rbp + 8]
0x0038C453: lea rax, [rbp - 0x68]
0x0038C457: mov r8, r15
0x0038C45A: mov qword ptr [rsp + 0x50], rax
0x0038C45F: mov rdx, r13
0x0038C462: lea rax, [rbp - 0x38]
0x0038C466: mov qword ptr [rsp + 0x48], rax
0x0038C46B: lea rax, [rbp - 8]
0x0038C46F: mov qword ptr [rsp + 0x40], rax
0x0038C474: lea rax, [rbp - 0x28]
0x0038C478: mov dword ptr [rsp + 0x38], edi
0x0038C47C: mov qword ptr [rsp + 0x30], rax
0x0038C481: mov rax, qword ptr [rip + 0x45fe98]
0x0038C488: mov dword ptr [rsp + 0x28], 0x10
0x0038C490: mov dword ptr [rsp + 0x20], edi
0x0038C494: call qword ptr [rax + 0x30]
0x0038C497: mov rcx, qword ptr [rbp - 0x78]
0x0038C49B: mov ebx, eax
0x0038C49D: test rcx, rcx
0x0038C4A0: je 0x14038c4b9
0x0038C4A2: mov rdx, qword ptr [rip + 0x45fe77]
0x0038C4A9: call qword ptr [rdx + 0x80]
0x0038C4AF: mov rcx, rdi
0x0038C4B2: mov dword ptr [rbp - 0x80], edi
0x0038C4B5: mov qword ptr [rbp - 0x78], rcx
0x0038C4B9: test ebx, ebx
0x0038C4BB: je 0x14038c4cc
0x0038C4BD: lea eax, [rbx - 0x90312]
0x0038C4C3: cmp eax, 2
0x0038C4C6: ja 0x14038c64d
0x0038C4CC: cmp dword ptr [rsp + 0x68], edi
0x0038C4D0: je 0x14038c55b
0x0038C4D6: movzx ecx, word ptr [rsp + 0x68]
0x0038C4DB: mov word ptr [rsp + 0x60], 0x101
0x0038C4E2: call qword ptr [rip + 0xa43b8]
0x0038C4E8: mov word ptr [rsp + 0x62], ax
0x0038C4ED: mov r9d, 4
0x0038C4F3: lea r8, [rsp + 0x60]
0x0038C4F8: mov rdx, r12
0x0038C4FB: lea rax, [rsp + 0x78]
0x0038C500: mov rcx, r14
0x0038C503: mov qword ptr [rsp + 0x20], rax
0x0038C508: call 0x140377650
0x0038C50D: test eax, eax
0x0038C50F: jne 0x14038c717
0x0038C515: cmp qword ptr [rsp + 0x78], 4
0x0038C51B: jne 0x14038c717
0x0038C521: mov r9d, dword ptr [rsp + 0x68]
0x0038C526: lea rax, [rsp + 0x78]
0x0038C52B: mov r8, qword ptr [rsp + 0x70]
0x0038C530: mov rdx, r12
0x0038C533: mov rcx, r14
0x0038C536: mov qword ptr [rsp + 0x20], rax
0x0038C53B: call 0x140377650
0x0038C540: test eax, eax
0x0038C542: jne 0x14038c6bf
```

## 26. `0x0038C56F` in `0x0038C220..0x0038CE78`

```asm
0x0038C4A2: mov rdx, qword ptr [rip + 0x45fe77]
0x0038C4A9: call qword ptr [rdx + 0x80]
0x0038C4AF: mov rcx, rdi
0x0038C4B2: mov dword ptr [rbp - 0x80], edi
0x0038C4B5: mov qword ptr [rbp - 0x78], rcx
0x0038C4B9: test ebx, ebx
0x0038C4BB: je 0x14038c4cc
0x0038C4BD: lea eax, [rbx - 0x90312]
0x0038C4C3: cmp eax, 2
0x0038C4C6: ja 0x14038c64d
0x0038C4CC: cmp dword ptr [rsp + 0x68], edi
0x0038C4D0: je 0x14038c55b
0x0038C4D6: movzx ecx, word ptr [rsp + 0x68]
0x0038C4DB: mov word ptr [rsp + 0x60], 0x101
0x0038C4E2: call qword ptr [rip + 0xa43b8]
0x0038C4E8: mov word ptr [rsp + 0x62], ax
0x0038C4ED: mov r9d, 4
0x0038C4F3: lea r8, [rsp + 0x60]
0x0038C4F8: mov rdx, r12
0x0038C4FB: lea rax, [rsp + 0x78]
0x0038C500: mov rcx, r14
0x0038C503: mov qword ptr [rsp + 0x20], rax
0x0038C508: call 0x140377650
0x0038C50D: test eax, eax
0x0038C50F: jne 0x14038c717
0x0038C515: cmp qword ptr [rsp + 0x78], 4
0x0038C51B: jne 0x14038c717
0x0038C521: mov r9d, dword ptr [rsp + 0x68]
0x0038C526: lea rax, [rsp + 0x78]
0x0038C52B: mov r8, qword ptr [rsp + 0x70]
0x0038C530: mov rdx, r12
0x0038C533: mov rcx, r14
0x0038C536: mov qword ptr [rsp + 0x20], rax
0x0038C53B: call 0x140377650
0x0038C540: test eax, eax
0x0038C542: jne 0x14038c6bf
0x0038C548: mov eax, dword ptr [rsp + 0x68]
0x0038C54C: cmp rax, qword ptr [rsp + 0x78]
0x0038C551: jne 0x14038c6bf
0x0038C557: mov rcx, qword ptr [rbp - 0x78]
0x0038C55B: mov rax, qword ptr [rsp + 0x70]
0x0038C560: test rax, rax
0x0038C563: je 0x14038c57e
0x0038C565: mov rcx, rax
0x0038C568: mov rax, qword ptr [rip + 0x45fdb1]
0x0038C56F: call qword ptr [rax + 0x80]
0x0038C575: mov rcx, qword ptr [rbp - 0x78]
0x0038C579: mov qword ptr [rsp + 0x70], rdi
0x0038C57E: mov dword ptr [rsp + 0x68], edi
0x0038C582: test rcx, rcx
0x0038C585: je 0x14038c598
0x0038C587: mov rax, qword ptr [rip + 0x45fd92]
0x0038C58E: call qword ptr [rax + 0x80]
0x0038C594: mov qword ptr [rbp - 0x78], rdi
0x0038C598: mov dword ptr [rbp - 0x80], edi
0x0038C59B: cmp ebx, 0x90312
0x0038C5A1: jne 0x14038c7be
0x0038C5A7: lea rax, [rbp - 0x70]
0x0038C5AB: mov r9d, 4
0x0038C5B1: lea r8, [rsp + 0x60]
0x0038C5B6: mov qword ptr [rsp + 0x20], rax
0x0038C5BB: mov rdx, r12
0x0038C5BE: mov rcx, r14
0x0038C5C1: call 0x140387a90
0x0038C5C6: test eax, eax
0x0038C5C8: jne 0x14038c7ad
0x0038C5CE: cmp qword ptr [rbp - 0x70], 4
0x0038C5D3: jne 0x14038c7ad
0x0038C5D9: movzx eax, byte ptr [rsp + 0x61]
0x0038C5DE: cmp al, 0xff
0x0038C5E0: je 0x14038c79e
0x0038C5E6: cmp al, 1
0x0038C5E8: jne 0x14038c769
0x0038C5EE: movzx ecx, word ptr [rsp + 0x62]
0x0038C5F3: call qword ptr [rip + 0xa421f]
0x0038C5F9: movzx ecx, ax
0x0038C5FC: movzx ebx, ax
0x0038C5FF: mov dword ptr [rbp - 0x80], ecx
0x0038C602: mov ecx, ebx
0x0038C604: call qword ptr [rip + 0x44a1ae]
```

## 27. `0x0038C58E` in `0x0038C220..0x0038CE78`

```asm
0x0038C4BD: lea eax, [rbx - 0x90312]
0x0038C4C3: cmp eax, 2
0x0038C4C6: ja 0x14038c64d
0x0038C4CC: cmp dword ptr [rsp + 0x68], edi
0x0038C4D0: je 0x14038c55b
0x0038C4D6: movzx ecx, word ptr [rsp + 0x68]
0x0038C4DB: mov word ptr [rsp + 0x60], 0x101
0x0038C4E2: call qword ptr [rip + 0xa43b8]
0x0038C4E8: mov word ptr [rsp + 0x62], ax
0x0038C4ED: mov r9d, 4
0x0038C4F3: lea r8, [rsp + 0x60]
0x0038C4F8: mov rdx, r12
0x0038C4FB: lea rax, [rsp + 0x78]
0x0038C500: mov rcx, r14
0x0038C503: mov qword ptr [rsp + 0x20], rax
0x0038C508: call 0x140377650
0x0038C50D: test eax, eax
0x0038C50F: jne 0x14038c717
0x0038C515: cmp qword ptr [rsp + 0x78], 4
0x0038C51B: jne 0x14038c717
0x0038C521: mov r9d, dword ptr [rsp + 0x68]
0x0038C526: lea rax, [rsp + 0x78]
0x0038C52B: mov r8, qword ptr [rsp + 0x70]
0x0038C530: mov rdx, r12
0x0038C533: mov rcx, r14
0x0038C536: mov qword ptr [rsp + 0x20], rax
0x0038C53B: call 0x140377650
0x0038C540: test eax, eax
0x0038C542: jne 0x14038c6bf
0x0038C548: mov eax, dword ptr [rsp + 0x68]
0x0038C54C: cmp rax, qword ptr [rsp + 0x78]
0x0038C551: jne 0x14038c6bf
0x0038C557: mov rcx, qword ptr [rbp - 0x78]
0x0038C55B: mov rax, qword ptr [rsp + 0x70]
0x0038C560: test rax, rax
0x0038C563: je 0x14038c57e
0x0038C565: mov rcx, rax
0x0038C568: mov rax, qword ptr [rip + 0x45fdb1]
0x0038C56F: call qword ptr [rax + 0x80]
0x0038C575: mov rcx, qword ptr [rbp - 0x78]
0x0038C579: mov qword ptr [rsp + 0x70], rdi
0x0038C57E: mov dword ptr [rsp + 0x68], edi
0x0038C582: test rcx, rcx
0x0038C585: je 0x14038c598
0x0038C587: mov rax, qword ptr [rip + 0x45fd92]
0x0038C58E: call qword ptr [rax + 0x80]
0x0038C594: mov qword ptr [rbp - 0x78], rdi
0x0038C598: mov dword ptr [rbp - 0x80], edi
0x0038C59B: cmp ebx, 0x90312
0x0038C5A1: jne 0x14038c7be
0x0038C5A7: lea rax, [rbp - 0x70]
0x0038C5AB: mov r9d, 4
0x0038C5B1: lea r8, [rsp + 0x60]
0x0038C5B6: mov qword ptr [rsp + 0x20], rax
0x0038C5BB: mov rdx, r12
0x0038C5BE: mov rcx, r14
0x0038C5C1: call 0x140387a90
0x0038C5C6: test eax, eax
0x0038C5C8: jne 0x14038c7ad
0x0038C5CE: cmp qword ptr [rbp - 0x70], 4
0x0038C5D3: jne 0x14038c7ad
0x0038C5D9: movzx eax, byte ptr [rsp + 0x61]
0x0038C5DE: cmp al, 0xff
0x0038C5E0: je 0x14038c79e
0x0038C5E6: cmp al, 1
0x0038C5E8: jne 0x14038c769
0x0038C5EE: movzx ecx, word ptr [rsp + 0x62]
0x0038C5F3: call qword ptr [rip + 0xa421f]
0x0038C5F9: movzx ecx, ax
0x0038C5FC: movzx ebx, ax
0x0038C5FF: mov dword ptr [rbp - 0x80], ecx
0x0038C602: mov ecx, ebx
0x0038C604: call qword ptr [rip + 0x44a1ae]
0x0038C60A: mov qword ptr [rbp - 0x78], rax
0x0038C60E: test rax, rax
0x0038C611: je 0x14038c73a
0x0038C617: mov r9d, dword ptr [rbp - 0x80]
0x0038C61B: lea rcx, [rbp - 0x70]
0x0038C61F: mov qword ptr [rsp + 0x20], rcx
0x0038C624: mov r8, rax
```

## 28. `0x0038C6A5` in `0x0038C220..0x0038CE78`

```asm
0x0038C5E6: cmp al, 1
0x0038C5E8: jne 0x14038c769
0x0038C5EE: movzx ecx, word ptr [rsp + 0x62]
0x0038C5F3: call qword ptr [rip + 0xa421f]
0x0038C5F9: movzx ecx, ax
0x0038C5FC: movzx ebx, ax
0x0038C5FF: mov dword ptr [rbp - 0x80], ecx
0x0038C602: mov ecx, ebx
0x0038C604: call qword ptr [rip + 0x44a1ae]
0x0038C60A: mov qword ptr [rbp - 0x78], rax
0x0038C60E: test rax, rax
0x0038C611: je 0x14038c73a
0x0038C617: mov r9d, dword ptr [rbp - 0x80]
0x0038C61B: lea rcx, [rbp - 0x70]
0x0038C61F: mov qword ptr [rsp + 0x20], rcx
0x0038C624: mov r8, rax
0x0038C627: mov rcx, r14
0x0038C62A: mov rdx, r12
0x0038C62D: call 0x140387a90
0x0038C632: test eax, eax
0x0038C634: jne 0x14038c720
0x0038C63A: cmp qword ptr [rbp - 0x70], rbx
0x0038C63E: jne 0x14038c720
0x0038C644: lea r13, [rbp - 8]
0x0038C648: jmp 0x14038c440
0x0038C64D: mov edx, ebx
0x0038C64F: mov rcx, r14
0x0038C652: call 0x140388a20
0x0038C657: mov rcx, qword ptr [r14]
0x0038C65A: lea r8, [rip + 0x379e47]
0x0038C661: mov r9, rax
0x0038C664: lea rdx, [rip + 0x379dbd]
0x0038C66B: call 0x140377140
0x0038C670: mov rcx, r15
0x0038C673: call qword ptr [rip + 0x44a147]
0x0038C679: mov rax, qword ptr [rip + 0x45fca0]
0x0038C680: lea rcx, [rbp + 8]
0x0038C684: call qword ptr [rax + 0x20]
0x0038C687: mov rax, qword ptr [rip + 0x45fc92]
0x0038C68E: lea rcx, [rbp - 8]
0x0038C692: call qword ptr [rax + 0x48]
0x0038C695: mov rcx, qword ptr [rbp - 0x78]
0x0038C699: test rcx, rcx
0x0038C69C: je 0x14038c6ab
0x0038C69E: mov rax, qword ptr [rip + 0x45fc7b]
0x0038C6A5: call qword ptr [rax + 0x80]
0x0038C6AB: lea rdx, [rip + 0x379e16]
0x0038C6B2: mov rcx, rsi
0x0038C6B5: call 0x140377140
0x0038C6BA: jmp 0x14038ce4c
0x0038C6BF: lea rdx, [rip + 0x379e5a]
0x0038C6C6: mov rcx, rsi
0x0038C6C9: call 0x140377140
0x0038C6CE: mov rcx, r15
0x0038C6D1: call qword ptr [rip + 0x44a0e9]
0x0038C6D7: mov rcx, qword ptr [rsp + 0x70]
0x0038C6DC: test rcx, rcx
0x0038C6DF: je 0x14038c6ee
0x0038C6E1: mov rax, qword ptr [rip + 0x45fc38]
0x0038C6E8: call qword ptr [rax + 0x80]
0x0038C6EE: mov rcx, qword ptr [rbp - 0x78]
0x0038C6F2: test rcx, rcx
0x0038C6F5: je 0x14038c704
0x0038C6F7: mov rax, qword ptr [rip + 0x45fc22]
0x0038C6FE: call qword ptr [rax + 0x80]
0x0038C704: mov rax, qword ptr [rip + 0x45fc15]
0x0038C70B: lea rcx, [rbp + 8]
0x0038C70F: call qword ptr [rax + 0x20]
0x0038C712: jmp 0x14038ce3e
0x0038C717: lea rdx, [rip + 0x379dd2]
0x0038C71E: jmp 0x14038c6c6
0x0038C720: lea rdx, [rip + 0x379ec1]
0x0038C727: mov rcx, rsi
0x0038C72A: call 0x140377140
0x0038C72F: mov rcx, r15
0x0038C732: call qword ptr [rip + 0x44a088]
0x0038C738: jmp 0x14038c6ee
0x0038C73A: mov rcx, r15
0x0038C73D: call qword ptr [rip + 0x44a07d]
0x0038C743: mov rax, qword ptr [rip + 0x45fbd6]
```

## 29. `0x0038C6E8` in `0x0038C220..0x0038CE78`

```asm
0x0038C61F: mov qword ptr [rsp + 0x20], rcx
0x0038C624: mov r8, rax
0x0038C627: mov rcx, r14
0x0038C62A: mov rdx, r12
0x0038C62D: call 0x140387a90
0x0038C632: test eax, eax
0x0038C634: jne 0x14038c720
0x0038C63A: cmp qword ptr [rbp - 0x70], rbx
0x0038C63E: jne 0x14038c720
0x0038C644: lea r13, [rbp - 8]
0x0038C648: jmp 0x14038c440
0x0038C64D: mov edx, ebx
0x0038C64F: mov rcx, r14
0x0038C652: call 0x140388a20
0x0038C657: mov rcx, qword ptr [r14]
0x0038C65A: lea r8, [rip + 0x379e47]
0x0038C661: mov r9, rax
0x0038C664: lea rdx, [rip + 0x379dbd]
0x0038C66B: call 0x140377140
0x0038C670: mov rcx, r15
0x0038C673: call qword ptr [rip + 0x44a147]
0x0038C679: mov rax, qword ptr [rip + 0x45fca0]
0x0038C680: lea rcx, [rbp + 8]
0x0038C684: call qword ptr [rax + 0x20]
0x0038C687: mov rax, qword ptr [rip + 0x45fc92]
0x0038C68E: lea rcx, [rbp - 8]
0x0038C692: call qword ptr [rax + 0x48]
0x0038C695: mov rcx, qword ptr [rbp - 0x78]
0x0038C699: test rcx, rcx
0x0038C69C: je 0x14038c6ab
0x0038C69E: mov rax, qword ptr [rip + 0x45fc7b]
0x0038C6A5: call qword ptr [rax + 0x80]
0x0038C6AB: lea rdx, [rip + 0x379e16]
0x0038C6B2: mov rcx, rsi
0x0038C6B5: call 0x140377140
0x0038C6BA: jmp 0x14038ce4c
0x0038C6BF: lea rdx, [rip + 0x379e5a]
0x0038C6C6: mov rcx, rsi
0x0038C6C9: call 0x140377140
0x0038C6CE: mov rcx, r15
0x0038C6D1: call qword ptr [rip + 0x44a0e9]
0x0038C6D7: mov rcx, qword ptr [rsp + 0x70]
0x0038C6DC: test rcx, rcx
0x0038C6DF: je 0x14038c6ee
0x0038C6E1: mov rax, qword ptr [rip + 0x45fc38]
0x0038C6E8: call qword ptr [rax + 0x80]
0x0038C6EE: mov rcx, qword ptr [rbp - 0x78]
0x0038C6F2: test rcx, rcx
0x0038C6F5: je 0x14038c704
0x0038C6F7: mov rax, qword ptr [rip + 0x45fc22]
0x0038C6FE: call qword ptr [rax + 0x80]
0x0038C704: mov rax, qword ptr [rip + 0x45fc15]
0x0038C70B: lea rcx, [rbp + 8]
0x0038C70F: call qword ptr [rax + 0x20]
0x0038C712: jmp 0x14038ce3e
0x0038C717: lea rdx, [rip + 0x379dd2]
0x0038C71E: jmp 0x14038c6c6
0x0038C720: lea rdx, [rip + 0x379ec1]
0x0038C727: mov rcx, rsi
0x0038C72A: call 0x140377140
0x0038C72F: mov rcx, r15
0x0038C732: call qword ptr [rip + 0x44a088]
0x0038C738: jmp 0x14038c6ee
0x0038C73A: mov rcx, r15
0x0038C73D: call qword ptr [rip + 0x44a07d]
0x0038C743: mov rax, qword ptr [rip + 0x45fbd6]
0x0038C74A: lea rcx, [rbp + 8]
0x0038C74E: call qword ptr [rax + 0x20]
0x0038C751: mov rax, qword ptr [rip + 0x45fbc8]
0x0038C758: lea rcx, [rbp - 8]
0x0038C75C: call qword ptr [rax + 0x48]
0x0038C75F: mov eax, 0x1b
0x0038C764: jmp 0x14038ce51
0x0038C769: movzx r9d, al
0x0038C76D: lea rdx, [rip + 0x379e3c]
0x0038C774: movzx r8d, byte ptr [rsp + 0x60]
0x0038C77A: mov rcx, rsi
0x0038C77D: call 0x140377140
0x0038C782: mov rcx, r15
0x0038C785: call qword ptr [rip + 0x44a035]
```

## 30. `0x0038C6FE` in `0x0038C220..0x0038CE78`

```asm
0x0038C632: test eax, eax
0x0038C634: jne 0x14038c720
0x0038C63A: cmp qword ptr [rbp - 0x70], rbx
0x0038C63E: jne 0x14038c720
0x0038C644: lea r13, [rbp - 8]
0x0038C648: jmp 0x14038c440
0x0038C64D: mov edx, ebx
0x0038C64F: mov rcx, r14
0x0038C652: call 0x140388a20
0x0038C657: mov rcx, qword ptr [r14]
0x0038C65A: lea r8, [rip + 0x379e47]
0x0038C661: mov r9, rax
0x0038C664: lea rdx, [rip + 0x379dbd]
0x0038C66B: call 0x140377140
0x0038C670: mov rcx, r15
0x0038C673: call qword ptr [rip + 0x44a147]
0x0038C679: mov rax, qword ptr [rip + 0x45fca0]
0x0038C680: lea rcx, [rbp + 8]
0x0038C684: call qword ptr [rax + 0x20]
0x0038C687: mov rax, qword ptr [rip + 0x45fc92]
0x0038C68E: lea rcx, [rbp - 8]
0x0038C692: call qword ptr [rax + 0x48]
0x0038C695: mov rcx, qword ptr [rbp - 0x78]
0x0038C699: test rcx, rcx
0x0038C69C: je 0x14038c6ab
0x0038C69E: mov rax, qword ptr [rip + 0x45fc7b]
0x0038C6A5: call qword ptr [rax + 0x80]
0x0038C6AB: lea rdx, [rip + 0x379e16]
0x0038C6B2: mov rcx, rsi
0x0038C6B5: call 0x140377140
0x0038C6BA: jmp 0x14038ce4c
0x0038C6BF: lea rdx, [rip + 0x379e5a]
0x0038C6C6: mov rcx, rsi
0x0038C6C9: call 0x140377140
0x0038C6CE: mov rcx, r15
0x0038C6D1: call qword ptr [rip + 0x44a0e9]
0x0038C6D7: mov rcx, qword ptr [rsp + 0x70]
0x0038C6DC: test rcx, rcx
0x0038C6DF: je 0x14038c6ee
0x0038C6E1: mov rax, qword ptr [rip + 0x45fc38]
0x0038C6E8: call qword ptr [rax + 0x80]
0x0038C6EE: mov rcx, qword ptr [rbp - 0x78]
0x0038C6F2: test rcx, rcx
0x0038C6F5: je 0x14038c704
0x0038C6F7: mov rax, qword ptr [rip + 0x45fc22]
0x0038C6FE: call qword ptr [rax + 0x80]
0x0038C704: mov rax, qword ptr [rip + 0x45fc15]
0x0038C70B: lea rcx, [rbp + 8]
0x0038C70F: call qword ptr [rax + 0x20]
0x0038C712: jmp 0x14038ce3e
0x0038C717: lea rdx, [rip + 0x379dd2]
0x0038C71E: jmp 0x14038c6c6
0x0038C720: lea rdx, [rip + 0x379ec1]
0x0038C727: mov rcx, rsi
0x0038C72A: call 0x140377140
0x0038C72F: mov rcx, r15
0x0038C732: call qword ptr [rip + 0x44a088]
0x0038C738: jmp 0x14038c6ee
0x0038C73A: mov rcx, r15
0x0038C73D: call qword ptr [rip + 0x44a07d]
0x0038C743: mov rax, qword ptr [rip + 0x45fbd6]
0x0038C74A: lea rcx, [rbp + 8]
0x0038C74E: call qword ptr [rax + 0x20]
0x0038C751: mov rax, qword ptr [rip + 0x45fbc8]
0x0038C758: lea rcx, [rbp - 8]
0x0038C75C: call qword ptr [rax + 0x48]
0x0038C75F: mov eax, 0x1b
0x0038C764: jmp 0x14038ce51
0x0038C769: movzx r9d, al
0x0038C76D: lea rdx, [rip + 0x379e3c]
0x0038C774: movzx r8d, byte ptr [rsp + 0x60]
0x0038C77A: mov rcx, rsi
0x0038C77D: call 0x140377140
0x0038C782: mov rcx, r15
0x0038C785: call qword ptr [rip + 0x44a035]
0x0038C78B: mov rax, qword ptr [rip + 0x45fb8e]
0x0038C792: lea rcx, [rbp + 8]
0x0038C796: call qword ptr [rax + 0x20]
0x0038C799: jmp 0x14038ce3e
0x0038C79E: mov r9d, 0xff
```

## 31. `0x0038C839` in `0x0038C220..0x0038CE78`

```asm
0x0038C774: movzx r8d, byte ptr [rsp + 0x60]
0x0038C77A: mov rcx, rsi
0x0038C77D: call 0x140377140
0x0038C782: mov rcx, r15
0x0038C785: call qword ptr [rip + 0x44a035]
0x0038C78B: mov rax, qword ptr [rip + 0x45fb8e]
0x0038C792: lea rcx, [rbp + 8]
0x0038C796: call qword ptr [rax + 0x20]
0x0038C799: jmp 0x14038ce3e
0x0038C79E: mov r9d, 0xff
0x0038C7A4: lea rdx, [rip + 0x379dd5]
0x0038C7AB: jmp 0x14038c774
0x0038C7AD: lea rdx, [rip + 0x379d9c]
0x0038C7B4: mov rcx, rsi
0x0038C7B7: call 0x140377140
0x0038C7BC: jmp 0x14038c782
0x0038C7BE: mov rcx, r15
0x0038C7C1: call qword ptr [rip + 0x449ff9]
0x0038C7C7: mov rax, qword ptr [rip + 0x45fb52]
0x0038C7CE: lea r8, [rbp - 0x60]
0x0038C7D2: mov edx, 1
0x0038C7D7: lea rcx, [rbp + 8]
0x0038C7DB: call qword ptr [rax + 0x10]
0x0038C7DE: mov rdx, qword ptr [rip + 0x45fb3b]
0x0038C7E5: lea rcx, [rbp + 8]
0x0038C7E9: mov ebx, eax
0x0038C7EB: call qword ptr [rdx + 0x20]
0x0038C7EE: test ebx, ebx
0x0038C7F0: je 0x14038c853
0x0038C7F2: lea ecx, [rbx - 0x90312]
0x0038C7F8: cmp ecx, 2
0x0038C7FB: jbe 0x14038c853
0x0038C7FD: mov edx, ebx
0x0038C7FF: mov rcx, r14
0x0038C802: call 0x140388a20
0x0038C807: mov rcx, qword ptr [r14]
0x0038C80A: lea r8, [rip + 0x379e07]
0x0038C811: mov r9, rax
0x0038C814: lea rdx, [rip + 0x379c0d]
0x0038C81B: call 0x140377140
0x0038C820: mov rax, qword ptr [rip + 0x45faf9]
0x0038C827: lea rcx, [rbp - 8]
0x0038C82B: call qword ptr [rax + 0x48]
0x0038C82E: mov rax, qword ptr [rip + 0x45faeb]
0x0038C835: mov rcx, qword ptr [rbp - 0x60]
0x0038C839: call qword ptr [rax + 0x80]
0x0038C83F: lea rdx, [rip + 0x379df2]
0x0038C846: mov rcx, rsi
0x0038C849: call 0x140377140
0x0038C84E: jmp 0x14038ce4c
0x0038C853: mov r8, qword ptr [rbp - 0x60]
0x0038C857: lea rdx, [rip + 0x379dfa]
0x0038C85E: mov rcx, rsi
0x0038C861: call 0x140377200
0x0038C866: mov rax, qword ptr [rip + 0x45fab3]
0x0038C86D: mov rcx, qword ptr [rbp - 0x60]
0x0038C871: call qword ptr [rax + 0x80]
0x0038C877: mov eax, dword ptr [rbp - 0x68]
0x0038C87A: mov word ptr [rsp + 0x60], 0x201
0x0038C881: test al, 0x10
0x0038C883: je 0x14038c889
0x0038C885: mov al, 2
0x0038C887: jmp 0x14038c891
0x0038C889: bt eax, 0x10
0x0038C88D: jae 0x14038c8a7
0x0038C88F: mov al, 1
0x0038C891: cmp al, 1
0x0038C893: lea rcx, [rip + 0x379df6]
0x0038C89A: lea r8, [rip + 0x379dff]
0x0038C8A1: cmove r8, rcx
0x0038C8A5: jmp 0x14038c8ae
0x0038C8A7: lea r8, [rip + 0x379dde]
0x0038C8AE: lea rdx, [rip + 0x379dfb]
0x0038C8B5: mov rcx, rsi
0x0038C8B8: call 0x140377200
0x0038C8BD: cmp byte ptr [rsi + 0x654], dil
0x0038C8C4: je 0x14038c8d0
0x0038C8C6: mov ecx, 1
0x0038C8CB: jmp 0x14038cafd
0x0038C8D0: mov rax, qword ptr [rip + 0x45fa49]
```

## 32. `0x0038C871` in `0x0038C220..0x0038CE78`

```asm
0x0038C7AB: jmp 0x14038c774
0x0038C7AD: lea rdx, [rip + 0x379d9c]
0x0038C7B4: mov rcx, rsi
0x0038C7B7: call 0x140377140
0x0038C7BC: jmp 0x14038c782
0x0038C7BE: mov rcx, r15
0x0038C7C1: call qword ptr [rip + 0x449ff9]
0x0038C7C7: mov rax, qword ptr [rip + 0x45fb52]
0x0038C7CE: lea r8, [rbp - 0x60]
0x0038C7D2: mov edx, 1
0x0038C7D7: lea rcx, [rbp + 8]
0x0038C7DB: call qword ptr [rax + 0x10]
0x0038C7DE: mov rdx, qword ptr [rip + 0x45fb3b]
0x0038C7E5: lea rcx, [rbp + 8]
0x0038C7E9: mov ebx, eax
0x0038C7EB: call qword ptr [rdx + 0x20]
0x0038C7EE: test ebx, ebx
0x0038C7F0: je 0x14038c853
0x0038C7F2: lea ecx, [rbx - 0x90312]
0x0038C7F8: cmp ecx, 2
0x0038C7FB: jbe 0x14038c853
0x0038C7FD: mov edx, ebx
0x0038C7FF: mov rcx, r14
0x0038C802: call 0x140388a20
0x0038C807: mov rcx, qword ptr [r14]
0x0038C80A: lea r8, [rip + 0x379e07]
0x0038C811: mov r9, rax
0x0038C814: lea rdx, [rip + 0x379c0d]
0x0038C81B: call 0x140377140
0x0038C820: mov rax, qword ptr [rip + 0x45faf9]
0x0038C827: lea rcx, [rbp - 8]
0x0038C82B: call qword ptr [rax + 0x48]
0x0038C82E: mov rax, qword ptr [rip + 0x45faeb]
0x0038C835: mov rcx, qword ptr [rbp - 0x60]
0x0038C839: call qword ptr [rax + 0x80]
0x0038C83F: lea rdx, [rip + 0x379df2]
0x0038C846: mov rcx, rsi
0x0038C849: call 0x140377140
0x0038C84E: jmp 0x14038ce4c
0x0038C853: mov r8, qword ptr [rbp - 0x60]
0x0038C857: lea rdx, [rip + 0x379dfa]
0x0038C85E: mov rcx, rsi
0x0038C861: call 0x140377200
0x0038C866: mov rax, qword ptr [rip + 0x45fab3]
0x0038C86D: mov rcx, qword ptr [rbp - 0x60]
0x0038C871: call qword ptr [rax + 0x80]
0x0038C877: mov eax, dword ptr [rbp - 0x68]
0x0038C87A: mov word ptr [rsp + 0x60], 0x201
0x0038C881: test al, 0x10
0x0038C883: je 0x14038c889
0x0038C885: mov al, 2
0x0038C887: jmp 0x14038c891
0x0038C889: bt eax, 0x10
0x0038C88D: jae 0x14038c8a7
0x0038C88F: mov al, 1
0x0038C891: cmp al, 1
0x0038C893: lea rcx, [rip + 0x379df6]
0x0038C89A: lea r8, [rip + 0x379dff]
0x0038C8A1: cmove r8, rcx
0x0038C8A5: jmp 0x14038c8ae
0x0038C8A7: lea r8, [rip + 0x379dde]
0x0038C8AE: lea rdx, [rip + 0x379dfb]
0x0038C8B5: mov rcx, rsi
0x0038C8B8: call 0x140377200
0x0038C8BD: cmp byte ptr [rsi + 0x654], dil
0x0038C8C4: je 0x14038c8d0
0x0038C8C6: mov ecx, 1
0x0038C8CB: jmp 0x14038cafd
0x0038C8D0: mov rax, qword ptr [rip + 0x45fa49]
0x0038C8D7: lea r8, [rbp - 0x18]
0x0038C8DB: xor edx, edx
0x0038C8DD: lea rcx, [rbp - 8]
0x0038C8E1: call qword ptr [rax + 0x58]
0x0038C8E4: lea r8, [rip + 0x379dfd]
0x0038C8EB: mov rcx, r14
0x0038C8EE: mov edx, eax
0x0038C8F0: call 0x14038ce80
0x0038C8F5: test eax, eax
0x0038C8F7: jne 0x14038c9f6
0x0038C8FD: mov eax, dword ptr [rbp - 0xc]
```

## 33. `0x0038C945` in `0x0038C220..0x0038CE78`

```asm
0x0038C885: mov al, 2
0x0038C887: jmp 0x14038c891
0x0038C889: bt eax, 0x10
0x0038C88D: jae 0x14038c8a7
0x0038C88F: mov al, 1
0x0038C891: cmp al, 1
0x0038C893: lea rcx, [rip + 0x379df6]
0x0038C89A: lea r8, [rip + 0x379dff]
0x0038C8A1: cmove r8, rcx
0x0038C8A5: jmp 0x14038c8ae
0x0038C8A7: lea r8, [rip + 0x379dde]
0x0038C8AE: lea rdx, [rip + 0x379dfb]
0x0038C8B5: mov rcx, rsi
0x0038C8B8: call 0x140377200
0x0038C8BD: cmp byte ptr [rsi + 0x654], dil
0x0038C8C4: je 0x14038c8d0
0x0038C8C6: mov ecx, 1
0x0038C8CB: jmp 0x14038cafd
0x0038C8D0: mov rax, qword ptr [rip + 0x45fa49]
0x0038C8D7: lea r8, [rbp - 0x18]
0x0038C8DB: xor edx, edx
0x0038C8DD: lea rcx, [rbp - 8]
0x0038C8E1: call qword ptr [rax + 0x58]
0x0038C8E4: lea r8, [rip + 0x379dfd]
0x0038C8EB: mov rcx, r14
0x0038C8EE: mov edx, eax
0x0038C8F0: call 0x14038ce80
0x0038C8F5: test eax, eax
0x0038C8F7: jne 0x14038c9f6
0x0038C8FD: mov eax, dword ptr [rbp - 0xc]
0x0038C900: mov ecx, eax
0x0038C902: mov dword ptr [rbp + 0x18], eax
0x0038C905: mov dword ptr [rbp + 0x1c], 2
0x0038C90C: call qword ptr [rip + 0x449ea6]
0x0038C912: mov qword ptr [rbp + 0x20], rax
0x0038C916: test rax, rax
0x0038C919: je 0x14038c751
0x0038C91F: mov ecx, 1
0x0038C924: mov dword ptr [rbp + 0x28], 1
0x0038C92B: call qword ptr [rip + 0x449e87]
0x0038C931: mov qword ptr [rbp + 0x30], rax
0x0038C935: test rax, rax
0x0038C938: jne 0x14038c950
0x0038C93A: mov rax, qword ptr [rip + 0x45f9df]
0x0038C941: mov rcx, qword ptr [rbp + 0x20]
0x0038C945: call qword ptr [rax + 0x80]
0x0038C94B: jmp 0x14038c751
0x0038C950: mov byte ptr [rax], dil
0x0038C953: mov eax, dword ptr [rbp - 0x10]
0x0038C956: mov ecx, eax
0x0038C958: mov dword ptr [rbp + 0x3c], 9
0x0038C95F: mov dword ptr [rbp + 0x38], eax
0x0038C962: call qword ptr [rip + 0x449e50]
0x0038C968: mov qword ptr [rbp + 0x40], rax
0x0038C96C: test rax, rax
0x0038C96F: mov rax, qword ptr [rip + 0x45f9aa]
0x0038C976: jne 0x14038c998
0x0038C978: mov rcx, qword ptr [rbp + 0x20]
0x0038C97C: call qword ptr [rax + 0x80]
0x0038C982: mov rax, qword ptr [rip + 0x45f997]
0x0038C989: mov rcx, qword ptr [rbp + 0x30]
0x0038C98D: call qword ptr [rax + 0x80]
0x0038C993: jmp 0x14038c751
0x0038C998: xor r9d, r9d
0x0038C99B: lea r8, [rbp - 0x58]
0x0038C99F: mov edx, 0x80000001
0x0038C9A4: lea rcx, [rbp - 8]
0x0038C9A8: call qword ptr [rax + 0xc8]
0x0038C9AE: lea r8, [rip + 0x379d7b]
0x0038C9B5: mov rcx, r14
0x0038C9B8: mov edx, eax
0x0038C9BA: call 0x14038ce80
0x0038C9BF: test eax, eax
0x0038C9C1: je 0x14038ca18
0x0038C9C3: mov rax, qword ptr [rip + 0x45f956]
0x0038C9CA: mov rcx, qword ptr [rbp + 0x20]
0x0038C9CE: call qword ptr [rax + 0x80]
0x0038C9D4: mov rax, qword ptr [rip + 0x45f945]
0x0038C9DB: mov rcx, qword ptr [rbp + 0x30]
0x0038C9DF: call qword ptr [rax + 0x80]
```

## 34. `0x0038C97C` in `0x0038C220..0x0038CE78`

```asm
0x0038C8B8: call 0x140377200
0x0038C8BD: cmp byte ptr [rsi + 0x654], dil
0x0038C8C4: je 0x14038c8d0
0x0038C8C6: mov ecx, 1
0x0038C8CB: jmp 0x14038cafd
0x0038C8D0: mov rax, qword ptr [rip + 0x45fa49]
0x0038C8D7: lea r8, [rbp - 0x18]
0x0038C8DB: xor edx, edx
0x0038C8DD: lea rcx, [rbp - 8]
0x0038C8E1: call qword ptr [rax + 0x58]
0x0038C8E4: lea r8, [rip + 0x379dfd]
0x0038C8EB: mov rcx, r14
0x0038C8EE: mov edx, eax
0x0038C8F0: call 0x14038ce80
0x0038C8F5: test eax, eax
0x0038C8F7: jne 0x14038c9f6
0x0038C8FD: mov eax, dword ptr [rbp - 0xc]
0x0038C900: mov ecx, eax
0x0038C902: mov dword ptr [rbp + 0x18], eax
0x0038C905: mov dword ptr [rbp + 0x1c], 2
0x0038C90C: call qword ptr [rip + 0x449ea6]
0x0038C912: mov qword ptr [rbp + 0x20], rax
0x0038C916: test rax, rax
0x0038C919: je 0x14038c751
0x0038C91F: mov ecx, 1
0x0038C924: mov dword ptr [rbp + 0x28], 1
0x0038C92B: call qword ptr [rip + 0x449e87]
0x0038C931: mov qword ptr [rbp + 0x30], rax
0x0038C935: test rax, rax
0x0038C938: jne 0x14038c950
0x0038C93A: mov rax, qword ptr [rip + 0x45f9df]
0x0038C941: mov rcx, qword ptr [rbp + 0x20]
0x0038C945: call qword ptr [rax + 0x80]
0x0038C94B: jmp 0x14038c751
0x0038C950: mov byte ptr [rax], dil
0x0038C953: mov eax, dword ptr [rbp - 0x10]
0x0038C956: mov ecx, eax
0x0038C958: mov dword ptr [rbp + 0x3c], 9
0x0038C95F: mov dword ptr [rbp + 0x38], eax
0x0038C962: call qword ptr [rip + 0x449e50]
0x0038C968: mov qword ptr [rbp + 0x40], rax
0x0038C96C: test rax, rax
0x0038C96F: mov rax, qword ptr [rip + 0x45f9aa]
0x0038C976: jne 0x14038c998
0x0038C978: mov rcx, qword ptr [rbp + 0x20]
0x0038C97C: call qword ptr [rax + 0x80]
0x0038C982: mov rax, qword ptr [rip + 0x45f997]
0x0038C989: mov rcx, qword ptr [rbp + 0x30]
0x0038C98D: call qword ptr [rax + 0x80]
0x0038C993: jmp 0x14038c751
0x0038C998: xor r9d, r9d
0x0038C99B: lea r8, [rbp - 0x58]
0x0038C99F: mov edx, 0x80000001
0x0038C9A4: lea rcx, [rbp - 8]
0x0038C9A8: call qword ptr [rax + 0xc8]
0x0038C9AE: lea r8, [rip + 0x379d7b]
0x0038C9B5: mov rcx, r14
0x0038C9B8: mov edx, eax
0x0038C9BA: call 0x14038ce80
0x0038C9BF: test eax, eax
0x0038C9C1: je 0x14038ca18
0x0038C9C3: mov rax, qword ptr [rip + 0x45f956]
0x0038C9CA: mov rcx, qword ptr [rbp + 0x20]
0x0038C9CE: call qword ptr [rax + 0x80]
0x0038C9D4: mov rax, qword ptr [rip + 0x45f945]
0x0038C9DB: mov rcx, qword ptr [rbp + 0x30]
0x0038C9DF: call qword ptr [rax + 0x80]
0x0038C9E5: mov rcx, qword ptr [rbp + 0x40]
0x0038C9E9: mov rax, qword ptr [rip + 0x45f930]
0x0038C9F0: call qword ptr [rax + 0x80]
0x0038C9F6: mov rax, qword ptr [rip + 0x45f923]
0x0038C9FD: lea rcx, [rbp - 8]
0x0038CA01: call qword ptr [rax + 0x48]
0x0038CA04: lea rdx, [rip + 0x379cf5]
0x0038CA0B: mov rcx, rsi
0x0038CA0E: call 0x140377140
0x0038CA13: jmp 0x14038ce4c
0x0038CA18: mov edx, dword ptr [rbp + 0x38]
0x0038CA1B: add edx, dword ptr [rbp + 0x28]
0x0038CA1E: add edx, dword ptr [rbp + 0x18]
```

## 35. `0x0038C98D` in `0x0038C220..0x0038CE78`

```asm
0x0038C8C6: mov ecx, 1
0x0038C8CB: jmp 0x14038cafd
0x0038C8D0: mov rax, qword ptr [rip + 0x45fa49]
0x0038C8D7: lea r8, [rbp - 0x18]
0x0038C8DB: xor edx, edx
0x0038C8DD: lea rcx, [rbp - 8]
0x0038C8E1: call qword ptr [rax + 0x58]
0x0038C8E4: lea r8, [rip + 0x379dfd]
0x0038C8EB: mov rcx, r14
0x0038C8EE: mov edx, eax
0x0038C8F0: call 0x14038ce80
0x0038C8F5: test eax, eax
0x0038C8F7: jne 0x14038c9f6
0x0038C8FD: mov eax, dword ptr [rbp - 0xc]
0x0038C900: mov ecx, eax
0x0038C902: mov dword ptr [rbp + 0x18], eax
0x0038C905: mov dword ptr [rbp + 0x1c], 2
0x0038C90C: call qword ptr [rip + 0x449ea6]
0x0038C912: mov qword ptr [rbp + 0x20], rax
0x0038C916: test rax, rax
0x0038C919: je 0x14038c751
0x0038C91F: mov ecx, 1
0x0038C924: mov dword ptr [rbp + 0x28], 1
0x0038C92B: call qword ptr [rip + 0x449e87]
0x0038C931: mov qword ptr [rbp + 0x30], rax
0x0038C935: test rax, rax
0x0038C938: jne 0x14038c950
0x0038C93A: mov rax, qword ptr [rip + 0x45f9df]
0x0038C941: mov rcx, qword ptr [rbp + 0x20]
0x0038C945: call qword ptr [rax + 0x80]
0x0038C94B: jmp 0x14038c751
0x0038C950: mov byte ptr [rax], dil
0x0038C953: mov eax, dword ptr [rbp - 0x10]
0x0038C956: mov ecx, eax
0x0038C958: mov dword ptr [rbp + 0x3c], 9
0x0038C95F: mov dword ptr [rbp + 0x38], eax
0x0038C962: call qword ptr [rip + 0x449e50]
0x0038C968: mov qword ptr [rbp + 0x40], rax
0x0038C96C: test rax, rax
0x0038C96F: mov rax, qword ptr [rip + 0x45f9aa]
0x0038C976: jne 0x14038c998
0x0038C978: mov rcx, qword ptr [rbp + 0x20]
0x0038C97C: call qword ptr [rax + 0x80]
0x0038C982: mov rax, qword ptr [rip + 0x45f997]
0x0038C989: mov rcx, qword ptr [rbp + 0x30]
0x0038C98D: call qword ptr [rax + 0x80]
0x0038C993: jmp 0x14038c751
0x0038C998: xor r9d, r9d
0x0038C99B: lea r8, [rbp - 0x58]
0x0038C99F: mov edx, 0x80000001
0x0038C9A4: lea rcx, [rbp - 8]
0x0038C9A8: call qword ptr [rax + 0xc8]
0x0038C9AE: lea r8, [rip + 0x379d7b]
0x0038C9B5: mov rcx, r14
0x0038C9B8: mov edx, eax
0x0038C9BA: call 0x14038ce80
0x0038C9BF: test eax, eax
0x0038C9C1: je 0x14038ca18
0x0038C9C3: mov rax, qword ptr [rip + 0x45f956]
0x0038C9CA: mov rcx, qword ptr [rbp + 0x20]
0x0038C9CE: call qword ptr [rax + 0x80]
0x0038C9D4: mov rax, qword ptr [rip + 0x45f945]
0x0038C9DB: mov rcx, qword ptr [rbp + 0x30]
0x0038C9DF: call qword ptr [rax + 0x80]
0x0038C9E5: mov rcx, qword ptr [rbp + 0x40]
0x0038C9E9: mov rax, qword ptr [rip + 0x45f930]
0x0038C9F0: call qword ptr [rax + 0x80]
0x0038C9F6: mov rax, qword ptr [rip + 0x45f923]
0x0038C9FD: lea rcx, [rbp - 8]
0x0038CA01: call qword ptr [rax + 0x48]
0x0038CA04: lea rdx, [rip + 0x379cf5]
0x0038CA0B: mov rcx, rsi
0x0038CA0E: call 0x140377140
0x0038CA13: jmp 0x14038ce4c
0x0038CA18: mov edx, dword ptr [rbp + 0x38]
0x0038CA1B: add edx, dword ptr [rbp + 0x28]
0x0038CA1E: add edx, dword ptr [rbp + 0x18]
0x0038CA21: mov ecx, edx
0x0038CA23: mov dword ptr [rsp + 0x68], edx
0x0038CA27: call qword ptr [rip + 0x449d8b]
```

## 36. `0x0038C9CE` in `0x0038C220..0x0038CE78`

```asm
0x0038C902: mov dword ptr [rbp + 0x18], eax
0x0038C905: mov dword ptr [rbp + 0x1c], 2
0x0038C90C: call qword ptr [rip + 0x449ea6]
0x0038C912: mov qword ptr [rbp + 0x20], rax
0x0038C916: test rax, rax
0x0038C919: je 0x14038c751
0x0038C91F: mov ecx, 1
0x0038C924: mov dword ptr [rbp + 0x28], 1
0x0038C92B: call qword ptr [rip + 0x449e87]
0x0038C931: mov qword ptr [rbp + 0x30], rax
0x0038C935: test rax, rax
0x0038C938: jne 0x14038c950
0x0038C93A: mov rax, qword ptr [rip + 0x45f9df]
0x0038C941: mov rcx, qword ptr [rbp + 0x20]
0x0038C945: call qword ptr [rax + 0x80]
0x0038C94B: jmp 0x14038c751
0x0038C950: mov byte ptr [rax], dil
0x0038C953: mov eax, dword ptr [rbp - 0x10]
0x0038C956: mov ecx, eax
0x0038C958: mov dword ptr [rbp + 0x3c], 9
0x0038C95F: mov dword ptr [rbp + 0x38], eax
0x0038C962: call qword ptr [rip + 0x449e50]
0x0038C968: mov qword ptr [rbp + 0x40], rax
0x0038C96C: test rax, rax
0x0038C96F: mov rax, qword ptr [rip + 0x45f9aa]
0x0038C976: jne 0x14038c998
0x0038C978: mov rcx, qword ptr [rbp + 0x20]
0x0038C97C: call qword ptr [rax + 0x80]
0x0038C982: mov rax, qword ptr [rip + 0x45f997]
0x0038C989: mov rcx, qword ptr [rbp + 0x30]
0x0038C98D: call qword ptr [rax + 0x80]
0x0038C993: jmp 0x14038c751
0x0038C998: xor r9d, r9d
0x0038C99B: lea r8, [rbp - 0x58]
0x0038C99F: mov edx, 0x80000001
0x0038C9A4: lea rcx, [rbp - 8]
0x0038C9A8: call qword ptr [rax + 0xc8]
0x0038C9AE: lea r8, [rip + 0x379d7b]
0x0038C9B5: mov rcx, r14
0x0038C9B8: mov edx, eax
0x0038C9BA: call 0x14038ce80
0x0038C9BF: test eax, eax
0x0038C9C1: je 0x14038ca18
0x0038C9C3: mov rax, qword ptr [rip + 0x45f956]
0x0038C9CA: mov rcx, qword ptr [rbp + 0x20]
0x0038C9CE: call qword ptr [rax + 0x80]
0x0038C9D4: mov rax, qword ptr [rip + 0x45f945]
0x0038C9DB: mov rcx, qword ptr [rbp + 0x30]
0x0038C9DF: call qword ptr [rax + 0x80]
0x0038C9E5: mov rcx, qword ptr [rbp + 0x40]
0x0038C9E9: mov rax, qword ptr [rip + 0x45f930]
0x0038C9F0: call qword ptr [rax + 0x80]
0x0038C9F6: mov rax, qword ptr [rip + 0x45f923]
0x0038C9FD: lea rcx, [rbp - 8]
0x0038CA01: call qword ptr [rax + 0x48]
0x0038CA04: lea rdx, [rip + 0x379cf5]
0x0038CA0B: mov rcx, rsi
0x0038CA0E: call 0x140377140
0x0038CA13: jmp 0x14038ce4c
0x0038CA18: mov edx, dword ptr [rbp + 0x38]
0x0038CA1B: add edx, dword ptr [rbp + 0x28]
0x0038CA1E: add edx, dword ptr [rbp + 0x18]
0x0038CA21: mov ecx, edx
0x0038CA23: mov dword ptr [rsp + 0x68], edx
0x0038CA27: call qword ptr [rip + 0x449d8b]
0x0038CA2D: mov qword ptr [rsp + 0x70], rax
0x0038CA32: test rax, rax
0x0038CA35: jne 0x14038ca6f
0x0038CA37: mov rax, qword ptr [rip + 0x45f8e2]
0x0038CA3E: mov rcx, qword ptr [rbp + 0x20]
0x0038CA42: call qword ptr [rax + 0x80]
0x0038CA48: mov rax, qword ptr [rip + 0x45f8d1]
0x0038CA4F: mov rcx, qword ptr [rbp + 0x30]
0x0038CA53: call qword ptr [rax + 0x80]
0x0038CA59: mov rax, qword ptr [rip + 0x45f8c0]
0x0038CA60: mov rcx, qword ptr [rbp + 0x40]
0x0038CA64: call qword ptr [rax + 0x80]
0x0038CA6A: jmp 0x14038c751
0x0038CA6F: mov r8d, dword ptr [rbp + 0x18]
0x0038CA73: mov rcx, rax
```

## 37. `0x0038C9DF` in `0x0038C220..0x0038CE78`

```asm
0x0038C912: mov qword ptr [rbp + 0x20], rax
0x0038C916: test rax, rax
0x0038C919: je 0x14038c751
0x0038C91F: mov ecx, 1
0x0038C924: mov dword ptr [rbp + 0x28], 1
0x0038C92B: call qword ptr [rip + 0x449e87]
0x0038C931: mov qword ptr [rbp + 0x30], rax
0x0038C935: test rax, rax
0x0038C938: jne 0x14038c950
0x0038C93A: mov rax, qword ptr [rip + 0x45f9df]
0x0038C941: mov rcx, qword ptr [rbp + 0x20]
0x0038C945: call qword ptr [rax + 0x80]
0x0038C94B: jmp 0x14038c751
0x0038C950: mov byte ptr [rax], dil
0x0038C953: mov eax, dword ptr [rbp - 0x10]
0x0038C956: mov ecx, eax
0x0038C958: mov dword ptr [rbp + 0x3c], 9
0x0038C95F: mov dword ptr [rbp + 0x38], eax
0x0038C962: call qword ptr [rip + 0x449e50]
0x0038C968: mov qword ptr [rbp + 0x40], rax
0x0038C96C: test rax, rax
0x0038C96F: mov rax, qword ptr [rip + 0x45f9aa]
0x0038C976: jne 0x14038c998
0x0038C978: mov rcx, qword ptr [rbp + 0x20]
0x0038C97C: call qword ptr [rax + 0x80]
0x0038C982: mov rax, qword ptr [rip + 0x45f997]
0x0038C989: mov rcx, qword ptr [rbp + 0x30]
0x0038C98D: call qword ptr [rax + 0x80]
0x0038C993: jmp 0x14038c751
0x0038C998: xor r9d, r9d
0x0038C99B: lea r8, [rbp - 0x58]
0x0038C99F: mov edx, 0x80000001
0x0038C9A4: lea rcx, [rbp - 8]
0x0038C9A8: call qword ptr [rax + 0xc8]
0x0038C9AE: lea r8, [rip + 0x379d7b]
0x0038C9B5: mov rcx, r14
0x0038C9B8: mov edx, eax
0x0038C9BA: call 0x14038ce80
0x0038C9BF: test eax, eax
0x0038C9C1: je 0x14038ca18
0x0038C9C3: mov rax, qword ptr [rip + 0x45f956]
0x0038C9CA: mov rcx, qword ptr [rbp + 0x20]
0x0038C9CE: call qword ptr [rax + 0x80]
0x0038C9D4: mov rax, qword ptr [rip + 0x45f945]
0x0038C9DB: mov rcx, qword ptr [rbp + 0x30]
0x0038C9DF: call qword ptr [rax + 0x80]
0x0038C9E5: mov rcx, qword ptr [rbp + 0x40]
0x0038C9E9: mov rax, qword ptr [rip + 0x45f930]
0x0038C9F0: call qword ptr [rax + 0x80]
0x0038C9F6: mov rax, qword ptr [rip + 0x45f923]
0x0038C9FD: lea rcx, [rbp - 8]
0x0038CA01: call qword ptr [rax + 0x48]
0x0038CA04: lea rdx, [rip + 0x379cf5]
0x0038CA0B: mov rcx, rsi
0x0038CA0E: call 0x140377140
0x0038CA13: jmp 0x14038ce4c
0x0038CA18: mov edx, dword ptr [rbp + 0x38]
0x0038CA1B: add edx, dword ptr [rbp + 0x28]
0x0038CA1E: add edx, dword ptr [rbp + 0x18]
0x0038CA21: mov ecx, edx
0x0038CA23: mov dword ptr [rsp + 0x68], edx
0x0038CA27: call qword ptr [rip + 0x449d8b]
0x0038CA2D: mov qword ptr [rsp + 0x70], rax
0x0038CA32: test rax, rax
0x0038CA35: jne 0x14038ca6f
0x0038CA37: mov rax, qword ptr [rip + 0x45f8e2]
0x0038CA3E: mov rcx, qword ptr [rbp + 0x20]
0x0038CA42: call qword ptr [rax + 0x80]
0x0038CA48: mov rax, qword ptr [rip + 0x45f8d1]
0x0038CA4F: mov rcx, qword ptr [rbp + 0x30]
0x0038CA53: call qword ptr [rax + 0x80]
0x0038CA59: mov rax, qword ptr [rip + 0x45f8c0]
0x0038CA60: mov rcx, qword ptr [rbp + 0x40]
0x0038CA64: call qword ptr [rax + 0x80]
0x0038CA6A: jmp 0x14038c751
0x0038CA6F: mov r8d, dword ptr [rbp + 0x18]
0x0038CA73: mov rcx, rax
0x0038CA76: mov rdx, qword ptr [rbp + 0x20]
0x0038CA7A: call 0x1403d1f90
0x0038CA7F: movsxd rcx, dword ptr [rbp + 0x18]
```

## 38. `0x0038C9F0` in `0x0038C220..0x0038CE78`

```asm
0x0038C91F: mov ecx, 1
0x0038C924: mov dword ptr [rbp + 0x28], 1
0x0038C92B: call qword ptr [rip + 0x449e87]
0x0038C931: mov qword ptr [rbp + 0x30], rax
0x0038C935: test rax, rax
0x0038C938: jne 0x14038c950
0x0038C93A: mov rax, qword ptr [rip + 0x45f9df]
0x0038C941: mov rcx, qword ptr [rbp + 0x20]
0x0038C945: call qword ptr [rax + 0x80]
0x0038C94B: jmp 0x14038c751
0x0038C950: mov byte ptr [rax], dil
0x0038C953: mov eax, dword ptr [rbp - 0x10]
0x0038C956: mov ecx, eax
0x0038C958: mov dword ptr [rbp + 0x3c], 9
0x0038C95F: mov dword ptr [rbp + 0x38], eax
0x0038C962: call qword ptr [rip + 0x449e50]
0x0038C968: mov qword ptr [rbp + 0x40], rax
0x0038C96C: test rax, rax
0x0038C96F: mov rax, qword ptr [rip + 0x45f9aa]
0x0038C976: jne 0x14038c998
0x0038C978: mov rcx, qword ptr [rbp + 0x20]
0x0038C97C: call qword ptr [rax + 0x80]
0x0038C982: mov rax, qword ptr [rip + 0x45f997]
0x0038C989: mov rcx, qword ptr [rbp + 0x30]
0x0038C98D: call qword ptr [rax + 0x80]
0x0038C993: jmp 0x14038c751
0x0038C998: xor r9d, r9d
0x0038C99B: lea r8, [rbp - 0x58]
0x0038C99F: mov edx, 0x80000001
0x0038C9A4: lea rcx, [rbp - 8]
0x0038C9A8: call qword ptr [rax + 0xc8]
0x0038C9AE: lea r8, [rip + 0x379d7b]
0x0038C9B5: mov rcx, r14
0x0038C9B8: mov edx, eax
0x0038C9BA: call 0x14038ce80
0x0038C9BF: test eax, eax
0x0038C9C1: je 0x14038ca18
0x0038C9C3: mov rax, qword ptr [rip + 0x45f956]
0x0038C9CA: mov rcx, qword ptr [rbp + 0x20]
0x0038C9CE: call qword ptr [rax + 0x80]
0x0038C9D4: mov rax, qword ptr [rip + 0x45f945]
0x0038C9DB: mov rcx, qword ptr [rbp + 0x30]
0x0038C9DF: call qword ptr [rax + 0x80]
0x0038C9E5: mov rcx, qword ptr [rbp + 0x40]
0x0038C9E9: mov rax, qword ptr [rip + 0x45f930]
0x0038C9F0: call qword ptr [rax + 0x80]
0x0038C9F6: mov rax, qword ptr [rip + 0x45f923]
0x0038C9FD: lea rcx, [rbp - 8]
0x0038CA01: call qword ptr [rax + 0x48]
0x0038CA04: lea rdx, [rip + 0x379cf5]
0x0038CA0B: mov rcx, rsi
0x0038CA0E: call 0x140377140
0x0038CA13: jmp 0x14038ce4c
0x0038CA18: mov edx, dword ptr [rbp + 0x38]
0x0038CA1B: add edx, dword ptr [rbp + 0x28]
0x0038CA1E: add edx, dword ptr [rbp + 0x18]
0x0038CA21: mov ecx, edx
0x0038CA23: mov dword ptr [rsp + 0x68], edx
0x0038CA27: call qword ptr [rip + 0x449d8b]
0x0038CA2D: mov qword ptr [rsp + 0x70], rax
0x0038CA32: test rax, rax
0x0038CA35: jne 0x14038ca6f
0x0038CA37: mov rax, qword ptr [rip + 0x45f8e2]
0x0038CA3E: mov rcx, qword ptr [rbp + 0x20]
0x0038CA42: call qword ptr [rax + 0x80]
0x0038CA48: mov rax, qword ptr [rip + 0x45f8d1]
0x0038CA4F: mov rcx, qword ptr [rbp + 0x30]
0x0038CA53: call qword ptr [rax + 0x80]
0x0038CA59: mov rax, qword ptr [rip + 0x45f8c0]
0x0038CA60: mov rcx, qword ptr [rbp + 0x40]
0x0038CA64: call qword ptr [rax + 0x80]
0x0038CA6A: jmp 0x14038c751
0x0038CA6F: mov r8d, dword ptr [rbp + 0x18]
0x0038CA73: mov rcx, rax
0x0038CA76: mov rdx, qword ptr [rbp + 0x20]
0x0038CA7A: call 0x1403d1f90
0x0038CA7F: movsxd rcx, dword ptr [rbp + 0x18]
0x0038CA83: add rcx, qword ptr [rsp + 0x70]
0x0038CA88: mov r8d, dword ptr [rbp + 0x28]
0x0038CA8C: mov rdx, qword ptr [rbp + 0x30]
```

## 39. `0x0038CA42` in `0x0038C220..0x0038CE78`

```asm
0x0038C976: jne 0x14038c998
0x0038C978: mov rcx, qword ptr [rbp + 0x20]
0x0038C97C: call qword ptr [rax + 0x80]
0x0038C982: mov rax, qword ptr [rip + 0x45f997]
0x0038C989: mov rcx, qword ptr [rbp + 0x30]
0x0038C98D: call qword ptr [rax + 0x80]
0x0038C993: jmp 0x14038c751
0x0038C998: xor r9d, r9d
0x0038C99B: lea r8, [rbp - 0x58]
0x0038C99F: mov edx, 0x80000001
0x0038C9A4: lea rcx, [rbp - 8]
0x0038C9A8: call qword ptr [rax + 0xc8]
0x0038C9AE: lea r8, [rip + 0x379d7b]
0x0038C9B5: mov rcx, r14
0x0038C9B8: mov edx, eax
0x0038C9BA: call 0x14038ce80
0x0038C9BF: test eax, eax
0x0038C9C1: je 0x14038ca18
0x0038C9C3: mov rax, qword ptr [rip + 0x45f956]
0x0038C9CA: mov rcx, qword ptr [rbp + 0x20]
0x0038C9CE: call qword ptr [rax + 0x80]
0x0038C9D4: mov rax, qword ptr [rip + 0x45f945]
0x0038C9DB: mov rcx, qword ptr [rbp + 0x30]
0x0038C9DF: call qword ptr [rax + 0x80]
0x0038C9E5: mov rcx, qword ptr [rbp + 0x40]
0x0038C9E9: mov rax, qword ptr [rip + 0x45f930]
0x0038C9F0: call qword ptr [rax + 0x80]
0x0038C9F6: mov rax, qword ptr [rip + 0x45f923]
0x0038C9FD: lea rcx, [rbp - 8]
0x0038CA01: call qword ptr [rax + 0x48]
0x0038CA04: lea rdx, [rip + 0x379cf5]
0x0038CA0B: mov rcx, rsi
0x0038CA0E: call 0x140377140
0x0038CA13: jmp 0x14038ce4c
0x0038CA18: mov edx, dword ptr [rbp + 0x38]
0x0038CA1B: add edx, dword ptr [rbp + 0x28]
0x0038CA1E: add edx, dword ptr [rbp + 0x18]
0x0038CA21: mov ecx, edx
0x0038CA23: mov dword ptr [rsp + 0x68], edx
0x0038CA27: call qword ptr [rip + 0x449d8b]
0x0038CA2D: mov qword ptr [rsp + 0x70], rax
0x0038CA32: test rax, rax
0x0038CA35: jne 0x14038ca6f
0x0038CA37: mov rax, qword ptr [rip + 0x45f8e2]
0x0038CA3E: mov rcx, qword ptr [rbp + 0x20]
0x0038CA42: call qword ptr [rax + 0x80]
0x0038CA48: mov rax, qword ptr [rip + 0x45f8d1]
0x0038CA4F: mov rcx, qword ptr [rbp + 0x30]
0x0038CA53: call qword ptr [rax + 0x80]
0x0038CA59: mov rax, qword ptr [rip + 0x45f8c0]
0x0038CA60: mov rcx, qword ptr [rbp + 0x40]
0x0038CA64: call qword ptr [rax + 0x80]
0x0038CA6A: jmp 0x14038c751
0x0038CA6F: mov r8d, dword ptr [rbp + 0x18]
0x0038CA73: mov rcx, rax
0x0038CA76: mov rdx, qword ptr [rbp + 0x20]
0x0038CA7A: call 0x1403d1f90
0x0038CA7F: movsxd rcx, dword ptr [rbp + 0x18]
0x0038CA83: add rcx, qword ptr [rsp + 0x70]
0x0038CA88: mov r8d, dword ptr [rbp + 0x28]
0x0038CA8C: mov rdx, qword ptr [rbp + 0x30]
0x0038CA90: call 0x1403d1f90
0x0038CA95: mov edx, dword ptr [rbp + 0x28]
0x0038CA98: add rdx, qword ptr [rsp + 0x70]
0x0038CA9D: mov ecx, dword ptr [rbp + 0x18]
0x0038CAA0: mov r8d, dword ptr [rbp + 0x38]
0x0038CAA4: add rcx, rdx
0x0038CAA7: mov rdx, qword ptr [rbp + 0x40]
0x0038CAAB: call 0x1403d1f90
0x0038CAB0: mov rax, qword ptr [rip + 0x45f869]
0x0038CAB7: mov rcx, qword ptr [rbp + 0x20]
0x0038CABB: call qword ptr [rax + 0x80]
0x0038CAC1: mov rax, qword ptr [rip + 0x45f858]
0x0038CAC8: mov rcx, qword ptr [rbp + 0x30]
0x0038CACC: mov qword ptr [rbp + 0x20], rdi
0x0038CAD0: mov dword ptr [rbp + 0x18], edi
0x0038CAD3: call qword ptr [rax + 0x80]
0x0038CAD9: mov rax, qword ptr [rip + 0x45f840]
0x0038CAE0: mov rcx, qword ptr [rbp + 0x40]
0x0038CAE4: mov qword ptr [rbp + 0x30], rdi
```

## 40. `0x0038CA53` in `0x0038C220..0x0038CE78`

```asm
0x0038C982: mov rax, qword ptr [rip + 0x45f997]
0x0038C989: mov rcx, qword ptr [rbp + 0x30]
0x0038C98D: call qword ptr [rax + 0x80]
0x0038C993: jmp 0x14038c751
0x0038C998: xor r9d, r9d
0x0038C99B: lea r8, [rbp - 0x58]
0x0038C99F: mov edx, 0x80000001
0x0038C9A4: lea rcx, [rbp - 8]
0x0038C9A8: call qword ptr [rax + 0xc8]
0x0038C9AE: lea r8, [rip + 0x379d7b]
0x0038C9B5: mov rcx, r14
0x0038C9B8: mov edx, eax
0x0038C9BA: call 0x14038ce80
0x0038C9BF: test eax, eax
0x0038C9C1: je 0x14038ca18
0x0038C9C3: mov rax, qword ptr [rip + 0x45f956]
0x0038C9CA: mov rcx, qword ptr [rbp + 0x20]
0x0038C9CE: call qword ptr [rax + 0x80]
0x0038C9D4: mov rax, qword ptr [rip + 0x45f945]
0x0038C9DB: mov rcx, qword ptr [rbp + 0x30]
0x0038C9DF: call qword ptr [rax + 0x80]
0x0038C9E5: mov rcx, qword ptr [rbp + 0x40]
0x0038C9E9: mov rax, qword ptr [rip + 0x45f930]
0x0038C9F0: call qword ptr [rax + 0x80]
0x0038C9F6: mov rax, qword ptr [rip + 0x45f923]
0x0038C9FD: lea rcx, [rbp - 8]
0x0038CA01: call qword ptr [rax + 0x48]
0x0038CA04: lea rdx, [rip + 0x379cf5]
0x0038CA0B: mov rcx, rsi
0x0038CA0E: call 0x140377140
0x0038CA13: jmp 0x14038ce4c
0x0038CA18: mov edx, dword ptr [rbp + 0x38]
0x0038CA1B: add edx, dword ptr [rbp + 0x28]
0x0038CA1E: add edx, dword ptr [rbp + 0x18]
0x0038CA21: mov ecx, edx
0x0038CA23: mov dword ptr [rsp + 0x68], edx
0x0038CA27: call qword ptr [rip + 0x449d8b]
0x0038CA2D: mov qword ptr [rsp + 0x70], rax
0x0038CA32: test rax, rax
0x0038CA35: jne 0x14038ca6f
0x0038CA37: mov rax, qword ptr [rip + 0x45f8e2]
0x0038CA3E: mov rcx, qword ptr [rbp + 0x20]
0x0038CA42: call qword ptr [rax + 0x80]
0x0038CA48: mov rax, qword ptr [rip + 0x45f8d1]
0x0038CA4F: mov rcx, qword ptr [rbp + 0x30]
0x0038CA53: call qword ptr [rax + 0x80]
0x0038CA59: mov rax, qword ptr [rip + 0x45f8c0]
0x0038CA60: mov rcx, qword ptr [rbp + 0x40]
0x0038CA64: call qword ptr [rax + 0x80]
0x0038CA6A: jmp 0x14038c751
0x0038CA6F: mov r8d, dword ptr [rbp + 0x18]
0x0038CA73: mov rcx, rax
0x0038CA76: mov rdx, qword ptr [rbp + 0x20]
0x0038CA7A: call 0x1403d1f90
0x0038CA7F: movsxd rcx, dword ptr [rbp + 0x18]
0x0038CA83: add rcx, qword ptr [rsp + 0x70]
0x0038CA88: mov r8d, dword ptr [rbp + 0x28]
0x0038CA8C: mov rdx, qword ptr [rbp + 0x30]
0x0038CA90: call 0x1403d1f90
0x0038CA95: mov edx, dword ptr [rbp + 0x28]
0x0038CA98: add rdx, qword ptr [rsp + 0x70]
0x0038CA9D: mov ecx, dword ptr [rbp + 0x18]
0x0038CAA0: mov r8d, dword ptr [rbp + 0x38]
0x0038CAA4: add rcx, rdx
0x0038CAA7: mov rdx, qword ptr [rbp + 0x40]
0x0038CAAB: call 0x1403d1f90
0x0038CAB0: mov rax, qword ptr [rip + 0x45f869]
0x0038CAB7: mov rcx, qword ptr [rbp + 0x20]
0x0038CABB: call qword ptr [rax + 0x80]
0x0038CAC1: mov rax, qword ptr [rip + 0x45f858]
0x0038CAC8: mov rcx, qword ptr [rbp + 0x30]
0x0038CACC: mov qword ptr [rbp + 0x20], rdi
0x0038CAD0: mov dword ptr [rbp + 0x18], edi
0x0038CAD3: call qword ptr [rax + 0x80]
0x0038CAD9: mov rax, qword ptr [rip + 0x45f840]
0x0038CAE0: mov rcx, qword ptr [rbp + 0x40]
0x0038CAE4: mov qword ptr [rbp + 0x30], rdi
0x0038CAE8: mov dword ptr [rbp + 0x28], edi
0x0038CAEB: call qword ptr [rax + 0x80]
0x0038CAF1: movzx ecx, word ptr [rsp + 0x68]
```

## 41. `0x0038CA64` in `0x0038C220..0x0038CE78`

```asm
0x0038C993: jmp 0x14038c751
0x0038C998: xor r9d, r9d
0x0038C99B: lea r8, [rbp - 0x58]
0x0038C99F: mov edx, 0x80000001
0x0038C9A4: lea rcx, [rbp - 8]
0x0038C9A8: call qword ptr [rax + 0xc8]
0x0038C9AE: lea r8, [rip + 0x379d7b]
0x0038C9B5: mov rcx, r14
0x0038C9B8: mov edx, eax
0x0038C9BA: call 0x14038ce80
0x0038C9BF: test eax, eax
0x0038C9C1: je 0x14038ca18
0x0038C9C3: mov rax, qword ptr [rip + 0x45f956]
0x0038C9CA: mov rcx, qword ptr [rbp + 0x20]
0x0038C9CE: call qword ptr [rax + 0x80]
0x0038C9D4: mov rax, qword ptr [rip + 0x45f945]
0x0038C9DB: mov rcx, qword ptr [rbp + 0x30]
0x0038C9DF: call qword ptr [rax + 0x80]
0x0038C9E5: mov rcx, qword ptr [rbp + 0x40]
0x0038C9E9: mov rax, qword ptr [rip + 0x45f930]
0x0038C9F0: call qword ptr [rax + 0x80]
0x0038C9F6: mov rax, qword ptr [rip + 0x45f923]
0x0038C9FD: lea rcx, [rbp - 8]
0x0038CA01: call qword ptr [rax + 0x48]
0x0038CA04: lea rdx, [rip + 0x379cf5]
0x0038CA0B: mov rcx, rsi
0x0038CA0E: call 0x140377140
0x0038CA13: jmp 0x14038ce4c
0x0038CA18: mov edx, dword ptr [rbp + 0x38]
0x0038CA1B: add edx, dword ptr [rbp + 0x28]
0x0038CA1E: add edx, dword ptr [rbp + 0x18]
0x0038CA21: mov ecx, edx
0x0038CA23: mov dword ptr [rsp + 0x68], edx
0x0038CA27: call qword ptr [rip + 0x449d8b]
0x0038CA2D: mov qword ptr [rsp + 0x70], rax
0x0038CA32: test rax, rax
0x0038CA35: jne 0x14038ca6f
0x0038CA37: mov rax, qword ptr [rip + 0x45f8e2]
0x0038CA3E: mov rcx, qword ptr [rbp + 0x20]
0x0038CA42: call qword ptr [rax + 0x80]
0x0038CA48: mov rax, qword ptr [rip + 0x45f8d1]
0x0038CA4F: mov rcx, qword ptr [rbp + 0x30]
0x0038CA53: call qword ptr [rax + 0x80]
0x0038CA59: mov rax, qword ptr [rip + 0x45f8c0]
0x0038CA60: mov rcx, qword ptr [rbp + 0x40]
0x0038CA64: call qword ptr [rax + 0x80]
0x0038CA6A: jmp 0x14038c751
0x0038CA6F: mov r8d, dword ptr [rbp + 0x18]
0x0038CA73: mov rcx, rax
0x0038CA76: mov rdx, qword ptr [rbp + 0x20]
0x0038CA7A: call 0x1403d1f90
0x0038CA7F: movsxd rcx, dword ptr [rbp + 0x18]
0x0038CA83: add rcx, qword ptr [rsp + 0x70]
0x0038CA88: mov r8d, dword ptr [rbp + 0x28]
0x0038CA8C: mov rdx, qword ptr [rbp + 0x30]
0x0038CA90: call 0x1403d1f90
0x0038CA95: mov edx, dword ptr [rbp + 0x28]
0x0038CA98: add rdx, qword ptr [rsp + 0x70]
0x0038CA9D: mov ecx, dword ptr [rbp + 0x18]
0x0038CAA0: mov r8d, dword ptr [rbp + 0x38]
0x0038CAA4: add rcx, rdx
0x0038CAA7: mov rdx, qword ptr [rbp + 0x40]
0x0038CAAB: call 0x1403d1f90
0x0038CAB0: mov rax, qword ptr [rip + 0x45f869]
0x0038CAB7: mov rcx, qword ptr [rbp + 0x20]
0x0038CABB: call qword ptr [rax + 0x80]
0x0038CAC1: mov rax, qword ptr [rip + 0x45f858]
0x0038CAC8: mov rcx, qword ptr [rbp + 0x30]
0x0038CACC: mov qword ptr [rbp + 0x20], rdi
0x0038CAD0: mov dword ptr [rbp + 0x18], edi
0x0038CAD3: call qword ptr [rax + 0x80]
0x0038CAD9: mov rax, qword ptr [rip + 0x45f840]
0x0038CAE0: mov rcx, qword ptr [rbp + 0x40]
0x0038CAE4: mov qword ptr [rbp + 0x30], rdi
0x0038CAE8: mov dword ptr [rbp + 0x28], edi
0x0038CAEB: call qword ptr [rax + 0x80]
0x0038CAF1: movzx ecx, word ptr [rsp + 0x68]
0x0038CAF6: mov qword ptr [rbp + 0x40], rdi
0x0038CAFA: mov dword ptr [rbp + 0x38], edi
0x0038CAFD: call qword ptr [rip + 0xa3d9d]
```

## 42. `0x0038CABB` in `0x0038C220..0x0038CE78`

```asm
0x0038C9F0: call qword ptr [rax + 0x80]
0x0038C9F6: mov rax, qword ptr [rip + 0x45f923]
0x0038C9FD: lea rcx, [rbp - 8]
0x0038CA01: call qword ptr [rax + 0x48]
0x0038CA04: lea rdx, [rip + 0x379cf5]
0x0038CA0B: mov rcx, rsi
0x0038CA0E: call 0x140377140
0x0038CA13: jmp 0x14038ce4c
0x0038CA18: mov edx, dword ptr [rbp + 0x38]
0x0038CA1B: add edx, dword ptr [rbp + 0x28]
0x0038CA1E: add edx, dword ptr [rbp + 0x18]
0x0038CA21: mov ecx, edx
0x0038CA23: mov dword ptr [rsp + 0x68], edx
0x0038CA27: call qword ptr [rip + 0x449d8b]
0x0038CA2D: mov qword ptr [rsp + 0x70], rax
0x0038CA32: test rax, rax
0x0038CA35: jne 0x14038ca6f
0x0038CA37: mov rax, qword ptr [rip + 0x45f8e2]
0x0038CA3E: mov rcx, qword ptr [rbp + 0x20]
0x0038CA42: call qword ptr [rax + 0x80]
0x0038CA48: mov rax, qword ptr [rip + 0x45f8d1]
0x0038CA4F: mov rcx, qword ptr [rbp + 0x30]
0x0038CA53: call qword ptr [rax + 0x80]
0x0038CA59: mov rax, qword ptr [rip + 0x45f8c0]
0x0038CA60: mov rcx, qword ptr [rbp + 0x40]
0x0038CA64: call qword ptr [rax + 0x80]
0x0038CA6A: jmp 0x14038c751
0x0038CA6F: mov r8d, dword ptr [rbp + 0x18]
0x0038CA73: mov rcx, rax
0x0038CA76: mov rdx, qword ptr [rbp + 0x20]
0x0038CA7A: call 0x1403d1f90
0x0038CA7F: movsxd rcx, dword ptr [rbp + 0x18]
0x0038CA83: add rcx, qword ptr [rsp + 0x70]
0x0038CA88: mov r8d, dword ptr [rbp + 0x28]
0x0038CA8C: mov rdx, qword ptr [rbp + 0x30]
0x0038CA90: call 0x1403d1f90
0x0038CA95: mov edx, dword ptr [rbp + 0x28]
0x0038CA98: add rdx, qword ptr [rsp + 0x70]
0x0038CA9D: mov ecx, dword ptr [rbp + 0x18]
0x0038CAA0: mov r8d, dword ptr [rbp + 0x38]
0x0038CAA4: add rcx, rdx
0x0038CAA7: mov rdx, qword ptr [rbp + 0x40]
0x0038CAAB: call 0x1403d1f90
0x0038CAB0: mov rax, qword ptr [rip + 0x45f869]
0x0038CAB7: mov rcx, qword ptr [rbp + 0x20]
0x0038CABB: call qword ptr [rax + 0x80]
0x0038CAC1: mov rax, qword ptr [rip + 0x45f858]
0x0038CAC8: mov rcx, qword ptr [rbp + 0x30]
0x0038CACC: mov qword ptr [rbp + 0x20], rdi
0x0038CAD0: mov dword ptr [rbp + 0x18], edi
0x0038CAD3: call qword ptr [rax + 0x80]
0x0038CAD9: mov rax, qword ptr [rip + 0x45f840]
0x0038CAE0: mov rcx, qword ptr [rbp + 0x40]
0x0038CAE4: mov qword ptr [rbp + 0x30], rdi
0x0038CAE8: mov dword ptr [rbp + 0x28], edi
0x0038CAEB: call qword ptr [rax + 0x80]
0x0038CAF1: movzx ecx, word ptr [rsp + 0x68]
0x0038CAF6: mov qword ptr [rbp + 0x40], rdi
0x0038CAFA: mov dword ptr [rbp + 0x38], edi
0x0038CAFD: call qword ptr [rip + 0xa3d9d]
0x0038CB03: mov word ptr [rsp + 0x62], ax
0x0038CB08: mov r9d, 4
0x0038CB0E: lea r8, [rsp + 0x60]
0x0038CB13: mov rdx, r12
0x0038CB16: lea rax, [rsp + 0x78]
0x0038CB1B: mov rcx, r14
0x0038CB1E: mov qword ptr [rsp + 0x20], rax
0x0038CB23: call 0x140377650
0x0038CB28: test eax, eax
0x0038CB2A: jne 0x14038ce18
0x0038CB30: cmp qword ptr [rsp + 0x78], 4
0x0038CB36: jne 0x14038ce18
0x0038CB3C: lea rax, [rsp + 0x78]
0x0038CB41: mov rdx, r12
0x0038CB44: mov rcx, r14
0x0038CB47: mov qword ptr [rsp + 0x20], rax
0x0038CB4C: cmp byte ptr [rsi + 0x654], dil
0x0038CB53: je 0x14038cb8a
0x0038CB55: mov r9d, 1
0x0038CB5B: mov byte ptr [rsp + 0x60], dil
```

## 43. `0x0038CAD3` in `0x0038C220..0x0038CE78`

```asm
0x0038CA0B: mov rcx, rsi
0x0038CA0E: call 0x140377140
0x0038CA13: jmp 0x14038ce4c
0x0038CA18: mov edx, dword ptr [rbp + 0x38]
0x0038CA1B: add edx, dword ptr [rbp + 0x28]
0x0038CA1E: add edx, dword ptr [rbp + 0x18]
0x0038CA21: mov ecx, edx
0x0038CA23: mov dword ptr [rsp + 0x68], edx
0x0038CA27: call qword ptr [rip + 0x449d8b]
0x0038CA2D: mov qword ptr [rsp + 0x70], rax
0x0038CA32: test rax, rax
0x0038CA35: jne 0x14038ca6f
0x0038CA37: mov rax, qword ptr [rip + 0x45f8e2]
0x0038CA3E: mov rcx, qword ptr [rbp + 0x20]
0x0038CA42: call qword ptr [rax + 0x80]
0x0038CA48: mov rax, qword ptr [rip + 0x45f8d1]
0x0038CA4F: mov rcx, qword ptr [rbp + 0x30]
0x0038CA53: call qword ptr [rax + 0x80]
0x0038CA59: mov rax, qword ptr [rip + 0x45f8c0]
0x0038CA60: mov rcx, qword ptr [rbp + 0x40]
0x0038CA64: call qword ptr [rax + 0x80]
0x0038CA6A: jmp 0x14038c751
0x0038CA6F: mov r8d, dword ptr [rbp + 0x18]
0x0038CA73: mov rcx, rax
0x0038CA76: mov rdx, qword ptr [rbp + 0x20]
0x0038CA7A: call 0x1403d1f90
0x0038CA7F: movsxd rcx, dword ptr [rbp + 0x18]
0x0038CA83: add rcx, qword ptr [rsp + 0x70]
0x0038CA88: mov r8d, dword ptr [rbp + 0x28]
0x0038CA8C: mov rdx, qword ptr [rbp + 0x30]
0x0038CA90: call 0x1403d1f90
0x0038CA95: mov edx, dword ptr [rbp + 0x28]
0x0038CA98: add rdx, qword ptr [rsp + 0x70]
0x0038CA9D: mov ecx, dword ptr [rbp + 0x18]
0x0038CAA0: mov r8d, dword ptr [rbp + 0x38]
0x0038CAA4: add rcx, rdx
0x0038CAA7: mov rdx, qword ptr [rbp + 0x40]
0x0038CAAB: call 0x1403d1f90
0x0038CAB0: mov rax, qword ptr [rip + 0x45f869]
0x0038CAB7: mov rcx, qword ptr [rbp + 0x20]
0x0038CABB: call qword ptr [rax + 0x80]
0x0038CAC1: mov rax, qword ptr [rip + 0x45f858]
0x0038CAC8: mov rcx, qword ptr [rbp + 0x30]
0x0038CACC: mov qword ptr [rbp + 0x20], rdi
0x0038CAD0: mov dword ptr [rbp + 0x18], edi
0x0038CAD3: call qword ptr [rax + 0x80]
0x0038CAD9: mov rax, qword ptr [rip + 0x45f840]
0x0038CAE0: mov rcx, qword ptr [rbp + 0x40]
0x0038CAE4: mov qword ptr [rbp + 0x30], rdi
0x0038CAE8: mov dword ptr [rbp + 0x28], edi
0x0038CAEB: call qword ptr [rax + 0x80]
0x0038CAF1: movzx ecx, word ptr [rsp + 0x68]
0x0038CAF6: mov qword ptr [rbp + 0x40], rdi
0x0038CAFA: mov dword ptr [rbp + 0x38], edi
0x0038CAFD: call qword ptr [rip + 0xa3d9d]
0x0038CB03: mov word ptr [rsp + 0x62], ax
0x0038CB08: mov r9d, 4
0x0038CB0E: lea r8, [rsp + 0x60]
0x0038CB13: mov rdx, r12
0x0038CB16: lea rax, [rsp + 0x78]
0x0038CB1B: mov rcx, r14
0x0038CB1E: mov qword ptr [rsp + 0x20], rax
0x0038CB23: call 0x140377650
0x0038CB28: test eax, eax
0x0038CB2A: jne 0x14038ce18
0x0038CB30: cmp qword ptr [rsp + 0x78], 4
0x0038CB36: jne 0x14038ce18
0x0038CB3C: lea rax, [rsp + 0x78]
0x0038CB41: mov rdx, r12
0x0038CB44: mov rcx, r14
0x0038CB47: mov qword ptr [rsp + 0x20], rax
0x0038CB4C: cmp byte ptr [rsi + 0x654], dil
0x0038CB53: je 0x14038cb8a
0x0038CB55: mov r9d, 1
0x0038CB5B: mov byte ptr [rsp + 0x60], dil
0x0038CB60: lea r8, [rsp + 0x60]
0x0038CB65: call 0x140377650
0x0038CB6A: test eax, eax
0x0038CB6C: jne 0x14038cb76
0x0038CB6E: cmp qword ptr [rsp + 0x78], 1
```

## 44. `0x0038CAEB` in `0x0038C220..0x0038CE78`

```asm
0x0038CA1E: add edx, dword ptr [rbp + 0x18]
0x0038CA21: mov ecx, edx
0x0038CA23: mov dword ptr [rsp + 0x68], edx
0x0038CA27: call qword ptr [rip + 0x449d8b]
0x0038CA2D: mov qword ptr [rsp + 0x70], rax
0x0038CA32: test rax, rax
0x0038CA35: jne 0x14038ca6f
0x0038CA37: mov rax, qword ptr [rip + 0x45f8e2]
0x0038CA3E: mov rcx, qword ptr [rbp + 0x20]
0x0038CA42: call qword ptr [rax + 0x80]
0x0038CA48: mov rax, qword ptr [rip + 0x45f8d1]
0x0038CA4F: mov rcx, qword ptr [rbp + 0x30]
0x0038CA53: call qword ptr [rax + 0x80]
0x0038CA59: mov rax, qword ptr [rip + 0x45f8c0]
0x0038CA60: mov rcx, qword ptr [rbp + 0x40]
0x0038CA64: call qword ptr [rax + 0x80]
0x0038CA6A: jmp 0x14038c751
0x0038CA6F: mov r8d, dword ptr [rbp + 0x18]
0x0038CA73: mov rcx, rax
0x0038CA76: mov rdx, qword ptr [rbp + 0x20]
0x0038CA7A: call 0x1403d1f90
0x0038CA7F: movsxd rcx, dword ptr [rbp + 0x18]
0x0038CA83: add rcx, qword ptr [rsp + 0x70]
0x0038CA88: mov r8d, dword ptr [rbp + 0x28]
0x0038CA8C: mov rdx, qword ptr [rbp + 0x30]
0x0038CA90: call 0x1403d1f90
0x0038CA95: mov edx, dword ptr [rbp + 0x28]
0x0038CA98: add rdx, qword ptr [rsp + 0x70]
0x0038CA9D: mov ecx, dword ptr [rbp + 0x18]
0x0038CAA0: mov r8d, dword ptr [rbp + 0x38]
0x0038CAA4: add rcx, rdx
0x0038CAA7: mov rdx, qword ptr [rbp + 0x40]
0x0038CAAB: call 0x1403d1f90
0x0038CAB0: mov rax, qword ptr [rip + 0x45f869]
0x0038CAB7: mov rcx, qword ptr [rbp + 0x20]
0x0038CABB: call qword ptr [rax + 0x80]
0x0038CAC1: mov rax, qword ptr [rip + 0x45f858]
0x0038CAC8: mov rcx, qword ptr [rbp + 0x30]
0x0038CACC: mov qword ptr [rbp + 0x20], rdi
0x0038CAD0: mov dword ptr [rbp + 0x18], edi
0x0038CAD3: call qword ptr [rax + 0x80]
0x0038CAD9: mov rax, qword ptr [rip + 0x45f840]
0x0038CAE0: mov rcx, qword ptr [rbp + 0x40]
0x0038CAE4: mov qword ptr [rbp + 0x30], rdi
0x0038CAE8: mov dword ptr [rbp + 0x28], edi
0x0038CAEB: call qword ptr [rax + 0x80]
0x0038CAF1: movzx ecx, word ptr [rsp + 0x68]
0x0038CAF6: mov qword ptr [rbp + 0x40], rdi
0x0038CAFA: mov dword ptr [rbp + 0x38], edi
0x0038CAFD: call qword ptr [rip + 0xa3d9d]
0x0038CB03: mov word ptr [rsp + 0x62], ax
0x0038CB08: mov r9d, 4
0x0038CB0E: lea r8, [rsp + 0x60]
0x0038CB13: mov rdx, r12
0x0038CB16: lea rax, [rsp + 0x78]
0x0038CB1B: mov rcx, r14
0x0038CB1E: mov qword ptr [rsp + 0x20], rax
0x0038CB23: call 0x140377650
0x0038CB28: test eax, eax
0x0038CB2A: jne 0x14038ce18
0x0038CB30: cmp qword ptr [rsp + 0x78], 4
0x0038CB36: jne 0x14038ce18
0x0038CB3C: lea rax, [rsp + 0x78]
0x0038CB41: mov rdx, r12
0x0038CB44: mov rcx, r14
0x0038CB47: mov qword ptr [rsp + 0x20], rax
0x0038CB4C: cmp byte ptr [rsi + 0x654], dil
0x0038CB53: je 0x14038cb8a
0x0038CB55: mov r9d, 1
0x0038CB5B: mov byte ptr [rsp + 0x60], dil
0x0038CB60: lea r8, [rsp + 0x60]
0x0038CB65: call 0x140377650
0x0038CB6A: test eax, eax
0x0038CB6C: jne 0x14038cb76
0x0038CB6E: cmp qword ptr [rsp + 0x78], 1
0x0038CB74: je 0x14038cbc7
0x0038CB76: lea rdx, [rip + 0x379beb]
0x0038CB7D: mov rcx, rsi
0x0038CB80: call 0x140377140
0x0038CB85: jmp 0x14038ce3e
```

## 45. `0x0038CBC1` in `0x0038C220..0x0038CE78`

```asm
0x0038CAF6: mov qword ptr [rbp + 0x40], rdi
0x0038CAFA: mov dword ptr [rbp + 0x38], edi
0x0038CAFD: call qword ptr [rip + 0xa3d9d]
0x0038CB03: mov word ptr [rsp + 0x62], ax
0x0038CB08: mov r9d, 4
0x0038CB0E: lea r8, [rsp + 0x60]
0x0038CB13: mov rdx, r12
0x0038CB16: lea rax, [rsp + 0x78]
0x0038CB1B: mov rcx, r14
0x0038CB1E: mov qword ptr [rsp + 0x20], rax
0x0038CB23: call 0x140377650
0x0038CB28: test eax, eax
0x0038CB2A: jne 0x14038ce18
0x0038CB30: cmp qword ptr [rsp + 0x78], 4
0x0038CB36: jne 0x14038ce18
0x0038CB3C: lea rax, [rsp + 0x78]
0x0038CB41: mov rdx, r12
0x0038CB44: mov rcx, r14
0x0038CB47: mov qword ptr [rsp + 0x20], rax
0x0038CB4C: cmp byte ptr [rsi + 0x654], dil
0x0038CB53: je 0x14038cb8a
0x0038CB55: mov r9d, 1
0x0038CB5B: mov byte ptr [rsp + 0x60], dil
0x0038CB60: lea r8, [rsp + 0x60]
0x0038CB65: call 0x140377650
0x0038CB6A: test eax, eax
0x0038CB6C: jne 0x14038cb76
0x0038CB6E: cmp qword ptr [rsp + 0x78], 1
0x0038CB74: je 0x14038cbc7
0x0038CB76: lea rdx, [rip + 0x379beb]
0x0038CB7D: mov rcx, rsi
0x0038CB80: call 0x140377140
0x0038CB85: jmp 0x14038ce3e
0x0038CB8A: mov r9d, dword ptr [rsp + 0x68]
0x0038CB8F: mov r8, qword ptr [rsp + 0x70]
0x0038CB94: call 0x140377650
0x0038CB99: test eax, eax
0x0038CB9B: jne 0x14038ce0f
0x0038CBA1: mov eax, dword ptr [rsp + 0x68]
0x0038CBA5: cmp rax, qword ptr [rsp + 0x78]
0x0038CBAA: jne 0x14038ce0f
0x0038CBB0: mov rcx, qword ptr [rsp + 0x70]
0x0038CBB5: test rcx, rcx
0x0038CBB8: je 0x14038cbc7
0x0038CBBA: mov rax, qword ptr [rip + 0x45f75f]
0x0038CBC1: call qword ptr [rax + 0x80]
0x0038CBC7: lea rax, [rbp - 0x70]
0x0038CBCB: mov r9d, 4
0x0038CBD1: lea r8, [rsp + 0x60]
0x0038CBD6: mov qword ptr [rsp + 0x20], rax
0x0038CBDB: mov rdx, r12
0x0038CBDE: mov rcx, r14
0x0038CBE1: call 0x140387a90
0x0038CBE6: test eax, eax
0x0038CBE8: jne 0x14038cdfe
0x0038CBEE: cmp qword ptr [rbp - 0x70], 4
0x0038CBF3: jne 0x14038cdfe
0x0038CBF9: movzx eax, byte ptr [rsp + 0x61]
0x0038CBFE: cmp al, 0xff
0x0038CC00: jne 0x14038cc22
0x0038CC02: movzx r8d, byte ptr [rsp + 0x60]
0x0038CC08: lea rdx, [rip + 0x379971]
0x0038CC0F: mov r9d, 0xff
0x0038CC15: mov rcx, rsi
0x0038CC18: call 0x140377140
0x0038CC1D: jmp 0x14038ce3e
0x0038CC22: cmp al, 2
0x0038CC24: je 0x14038cc44
0x0038CC26: movzx r8d, byte ptr [rsp + 0x60]
0x0038CC2C: lea rdx, [rip + 0x379b8d]
0x0038CC33: movzx r9d, al
0x0038CC37: mov rcx, rsi
0x0038CC3A: call 0x140377140
0x0038CC3F: jmp 0x14038ce3e
0x0038CC44: movzx ecx, word ptr [rsp + 0x62]
0x0038CC49: call qword ptr [rip + 0xa3bc9]
0x0038CC4F: movzx ecx, ax
0x0038CC52: movzx ebx, ax
0x0038CC55: mov dword ptr [rbp + 0x18], ecx
0x0038CC58: mov ecx, ebx
```

## 46. `0x0038CD04` in `0x0038C220..0x0038CE78`

```asm
0x0038CC3F: jmp 0x14038ce3e
0x0038CC44: movzx ecx, word ptr [rsp + 0x62]
0x0038CC49: call qword ptr [rip + 0xa3bc9]
0x0038CC4F: movzx ecx, ax
0x0038CC52: movzx ebx, ax
0x0038CC55: mov dword ptr [rbp + 0x18], ecx
0x0038CC58: mov ecx, ebx
0x0038CC5A: call qword ptr [rip + 0x449b58]
0x0038CC60: mov qword ptr [rbp + 0x20], rax
0x0038CC64: test rax, rax
0x0038CC67: je 0x14038c751
0x0038CC6D: mov r9d, dword ptr [rbp + 0x18]
0x0038CC71: lea rcx, [rbp - 0x70]
0x0038CC75: mov qword ptr [rsp + 0x20], rcx
0x0038CC7A: mov r8, rax
0x0038CC7D: mov rcx, r14
0x0038CC80: mov rdx, r12
0x0038CC83: call 0x140387a90
0x0038CC88: test eax, eax
0x0038CC8A: jne 0x14038cde9
0x0038CC90: cmp qword ptr [rbp - 0x70], rbx
0x0038CC94: jne 0x14038cde9
0x0038CC9A: cmp byte ptr [rsi + 0x654], dil
0x0038CCA1: jne 0x14038cd76
0x0038CCA7: mov rax, qword ptr [rip + 0x45f672]
0x0038CCAE: lea r9, [rbp - 0x48]
0x0038CCB2: xor r8d, r8d
0x0038CCB5: mov dword ptr [rbp - 0x54], 2
0x0038CCBC: lea rdx, [rbp - 0x58]
0x0038CCC0: mov dword ptr [rbp + 0x1c], 0xa
0x0038CCC7: lea rcx, [rbp - 8]
0x0038CCCB: mov dword ptr [rbp + 0x2c], 1
0x0038CCD2: mov dword ptr [rbp + 0x28], edi
0x0038CCD5: mov qword ptr [rbp + 0x30], rdi
0x0038CCD9: call qword ptr [rax + 0xd0]
0x0038CCDF: lea r8, [rip + 0x379b32]
0x0038CCE6: mov rcx, r14
0x0038CCE9: mov edx, eax
0x0038CCEB: call 0x14038ce80
0x0038CCF0: test eax, eax
0x0038CCF2: je 0x14038cd1c
0x0038CCF4: mov rcx, qword ptr [rbp + 0x20]
0x0038CCF8: test rcx, rcx
0x0038CCFB: je 0x14038cd0a
0x0038CCFD: mov rax, qword ptr [rip + 0x45f61c]
0x0038CD04: call qword ptr [rax + 0x80]
0x0038CD0A: mov rcx, qword ptr [rbp + 0x30]
0x0038CD0E: test rcx, rcx
0x0038CD11: je 0x14038c9f6
0x0038CD17: jmp 0x14038c9e9
0x0038CD1C: mov r8d, dword ptr [rbp + 0x28]
0x0038CD20: cmp r8d, 1
0x0038CD24: je 0x14038cd54
0x0038CD26: lea rdx, [rip + 0x379afb]
0x0038CD2D: mov rcx, rsi
0x0038CD30: call 0x140377140
0x0038CD35: mov rcx, qword ptr [rbp + 0x20]
0x0038CD39: test rcx, rcx
0x0038CD3C: je 0x14038cd4b
0x0038CD3E: mov rax, qword ptr [rip + 0x45f5db]
0x0038CD45: call qword ptr [rax + 0x80]
0x0038CD4B: mov rcx, qword ptr [rbp + 0x30]
0x0038CD4F: jmp 0x14038ce2c
0x0038CD54: mov rax, qword ptr [rbp + 0x30]
0x0038CD58: movzx ecx, byte ptr [rax]
0x0038CD5B: mov rax, qword ptr [rip + 0x45f5be]
0x0038CD62: mov byte ptr [rsp + 0x60], cl
0x0038CD66: mov rcx, qword ptr [rbp + 0x20]
0x0038CD6A: call qword ptr [rax + 0x80]
0x0038CD70: mov rcx, qword ptr [rbp + 0x30]
0x0038CD74: jmp 0x14038cda3
0x0038CD76: mov r8d, dword ptr [rbp + 0x18]
0x0038CD7A: cmp r8d, 1
0x0038CD7E: je 0x14038cd98
0x0038CD80: lea rdx, [rip + 0x379aa1]
0x0038CD87: mov rcx, rsi
0x0038CD8A: call 0x140377140
0x0038CD8F: mov rcx, qword ptr [rbp + 0x20]
0x0038CD93: jmp 0x14038ce31
0x0038CD98: mov rcx, qword ptr [rbp + 0x20]
```

## 47. `0x0038CD45` in `0x0038C220..0x0038CE78`

```asm
0x0038CC7D: mov rcx, r14
0x0038CC80: mov rdx, r12
0x0038CC83: call 0x140387a90
0x0038CC88: test eax, eax
0x0038CC8A: jne 0x14038cde9
0x0038CC90: cmp qword ptr [rbp - 0x70], rbx
0x0038CC94: jne 0x14038cde9
0x0038CC9A: cmp byte ptr [rsi + 0x654], dil
0x0038CCA1: jne 0x14038cd76
0x0038CCA7: mov rax, qword ptr [rip + 0x45f672]
0x0038CCAE: lea r9, [rbp - 0x48]
0x0038CCB2: xor r8d, r8d
0x0038CCB5: mov dword ptr [rbp - 0x54], 2
0x0038CCBC: lea rdx, [rbp - 0x58]
0x0038CCC0: mov dword ptr [rbp + 0x1c], 0xa
0x0038CCC7: lea rcx, [rbp - 8]
0x0038CCCB: mov dword ptr [rbp + 0x2c], 1
0x0038CCD2: mov dword ptr [rbp + 0x28], edi
0x0038CCD5: mov qword ptr [rbp + 0x30], rdi
0x0038CCD9: call qword ptr [rax + 0xd0]
0x0038CCDF: lea r8, [rip + 0x379b32]
0x0038CCE6: mov rcx, r14
0x0038CCE9: mov edx, eax
0x0038CCEB: call 0x14038ce80
0x0038CCF0: test eax, eax
0x0038CCF2: je 0x14038cd1c
0x0038CCF4: mov rcx, qword ptr [rbp + 0x20]
0x0038CCF8: test rcx, rcx
0x0038CCFB: je 0x14038cd0a
0x0038CCFD: mov rax, qword ptr [rip + 0x45f61c]
0x0038CD04: call qword ptr [rax + 0x80]
0x0038CD0A: mov rcx, qword ptr [rbp + 0x30]
0x0038CD0E: test rcx, rcx
0x0038CD11: je 0x14038c9f6
0x0038CD17: jmp 0x14038c9e9
0x0038CD1C: mov r8d, dword ptr [rbp + 0x28]
0x0038CD20: cmp r8d, 1
0x0038CD24: je 0x14038cd54
0x0038CD26: lea rdx, [rip + 0x379afb]
0x0038CD2D: mov rcx, rsi
0x0038CD30: call 0x140377140
0x0038CD35: mov rcx, qword ptr [rbp + 0x20]
0x0038CD39: test rcx, rcx
0x0038CD3C: je 0x14038cd4b
0x0038CD3E: mov rax, qword ptr [rip + 0x45f5db]
0x0038CD45: call qword ptr [rax + 0x80]
0x0038CD4B: mov rcx, qword ptr [rbp + 0x30]
0x0038CD4F: jmp 0x14038ce2c
0x0038CD54: mov rax, qword ptr [rbp + 0x30]
0x0038CD58: movzx ecx, byte ptr [rax]
0x0038CD5B: mov rax, qword ptr [rip + 0x45f5be]
0x0038CD62: mov byte ptr [rsp + 0x60], cl
0x0038CD66: mov rcx, qword ptr [rbp + 0x20]
0x0038CD6A: call qword ptr [rax + 0x80]
0x0038CD70: mov rcx, qword ptr [rbp + 0x30]
0x0038CD74: jmp 0x14038cda3
0x0038CD76: mov r8d, dword ptr [rbp + 0x18]
0x0038CD7A: cmp r8d, 1
0x0038CD7E: je 0x14038cd98
0x0038CD80: lea rdx, [rip + 0x379aa1]
0x0038CD87: mov rcx, rsi
0x0038CD8A: call 0x140377140
0x0038CD8F: mov rcx, qword ptr [rbp + 0x20]
0x0038CD93: jmp 0x14038ce31
0x0038CD98: mov rcx, qword ptr [rbp + 0x20]
0x0038CD9C: movzx eax, byte ptr [rcx]
0x0038CD9F: mov byte ptr [rsp + 0x60], al
0x0038CDA3: mov rax, qword ptr [rip + 0x45f576]
0x0038CDAA: call qword ptr [rax + 0x80]
0x0038CDB0: movzx eax, byte ptr [rsp + 0x60]
0x0038CDB5: test al, al
0x0038CDB7: jne 0x14038cdc2
0x0038CDB9: lea r8, [rip + 0x379a98]
0x0038CDC0: jmp 0x14038cdd6
0x0038CDC2: cmp al, 1
0x0038CDC4: lea rcx, [rip + 0x379aa5]
0x0038CDCB: lea r8, [rip + 0x379ab6]
0x0038CDD2: cmove r8, rcx
0x0038CDD6: lea rdx, [rip + 0x379acb]
0x0038CDDD: mov rcx, rsi
```

## 48. `0x0038CD6A` in `0x0038C220..0x0038CE78`

```asm
0x0038CCA1: jne 0x14038cd76
0x0038CCA7: mov rax, qword ptr [rip + 0x45f672]
0x0038CCAE: lea r9, [rbp - 0x48]
0x0038CCB2: xor r8d, r8d
0x0038CCB5: mov dword ptr [rbp - 0x54], 2
0x0038CCBC: lea rdx, [rbp - 0x58]
0x0038CCC0: mov dword ptr [rbp + 0x1c], 0xa
0x0038CCC7: lea rcx, [rbp - 8]
0x0038CCCB: mov dword ptr [rbp + 0x2c], 1
0x0038CCD2: mov dword ptr [rbp + 0x28], edi
0x0038CCD5: mov qword ptr [rbp + 0x30], rdi
0x0038CCD9: call qword ptr [rax + 0xd0]
0x0038CCDF: lea r8, [rip + 0x379b32]
0x0038CCE6: mov rcx, r14
0x0038CCE9: mov edx, eax
0x0038CCEB: call 0x14038ce80
0x0038CCF0: test eax, eax
0x0038CCF2: je 0x14038cd1c
0x0038CCF4: mov rcx, qword ptr [rbp + 0x20]
0x0038CCF8: test rcx, rcx
0x0038CCFB: je 0x14038cd0a
0x0038CCFD: mov rax, qword ptr [rip + 0x45f61c]
0x0038CD04: call qword ptr [rax + 0x80]
0x0038CD0A: mov rcx, qword ptr [rbp + 0x30]
0x0038CD0E: test rcx, rcx
0x0038CD11: je 0x14038c9f6
0x0038CD17: jmp 0x14038c9e9
0x0038CD1C: mov r8d, dword ptr [rbp + 0x28]
0x0038CD20: cmp r8d, 1
0x0038CD24: je 0x14038cd54
0x0038CD26: lea rdx, [rip + 0x379afb]
0x0038CD2D: mov rcx, rsi
0x0038CD30: call 0x140377140
0x0038CD35: mov rcx, qword ptr [rbp + 0x20]
0x0038CD39: test rcx, rcx
0x0038CD3C: je 0x14038cd4b
0x0038CD3E: mov rax, qword ptr [rip + 0x45f5db]
0x0038CD45: call qword ptr [rax + 0x80]
0x0038CD4B: mov rcx, qword ptr [rbp + 0x30]
0x0038CD4F: jmp 0x14038ce2c
0x0038CD54: mov rax, qword ptr [rbp + 0x30]
0x0038CD58: movzx ecx, byte ptr [rax]
0x0038CD5B: mov rax, qword ptr [rip + 0x45f5be]
0x0038CD62: mov byte ptr [rsp + 0x60], cl
0x0038CD66: mov rcx, qword ptr [rbp + 0x20]
0x0038CD6A: call qword ptr [rax + 0x80]
0x0038CD70: mov rcx, qword ptr [rbp + 0x30]
0x0038CD74: jmp 0x14038cda3
0x0038CD76: mov r8d, dword ptr [rbp + 0x18]
0x0038CD7A: cmp r8d, 1
0x0038CD7E: je 0x14038cd98
0x0038CD80: lea rdx, [rip + 0x379aa1]
0x0038CD87: mov rcx, rsi
0x0038CD8A: call 0x140377140
0x0038CD8F: mov rcx, qword ptr [rbp + 0x20]
0x0038CD93: jmp 0x14038ce31
0x0038CD98: mov rcx, qword ptr [rbp + 0x20]
0x0038CD9C: movzx eax, byte ptr [rcx]
0x0038CD9F: mov byte ptr [rsp + 0x60], al
0x0038CDA3: mov rax, qword ptr [rip + 0x45f576]
0x0038CDAA: call qword ptr [rax + 0x80]
0x0038CDB0: movzx eax, byte ptr [rsp + 0x60]
0x0038CDB5: test al, al
0x0038CDB7: jne 0x14038cdc2
0x0038CDB9: lea r8, [rip + 0x379a98]
0x0038CDC0: jmp 0x14038cdd6
0x0038CDC2: cmp al, 1
0x0038CDC4: lea rcx, [rip + 0x379aa5]
0x0038CDCB: lea r8, [rip + 0x379ab6]
0x0038CDD2: cmove r8, rcx
0x0038CDD6: lea rdx, [rip + 0x379acb]
0x0038CDDD: mov rcx, rsi
0x0038CDE0: call 0x140377200
0x0038CDE5: xor eax, eax
0x0038CDE7: jmp 0x14038ce51
0x0038CDE9: lea rdx, [rip + 0x379a00]
0x0038CDF0: mov rcx, rsi
0x0038CDF3: call 0x140377140
0x0038CDF8: mov rcx, qword ptr [rbp + 0x20]
0x0038CDFC: jmp 0x14038ce31
```

## 49. `0x0038CDAA` in `0x0038C220..0x0038CE78`

```asm
0x0038CCEB: call 0x14038ce80
0x0038CCF0: test eax, eax
0x0038CCF2: je 0x14038cd1c
0x0038CCF4: mov rcx, qword ptr [rbp + 0x20]
0x0038CCF8: test rcx, rcx
0x0038CCFB: je 0x14038cd0a
0x0038CCFD: mov rax, qword ptr [rip + 0x45f61c]
0x0038CD04: call qword ptr [rax + 0x80]
0x0038CD0A: mov rcx, qword ptr [rbp + 0x30]
0x0038CD0E: test rcx, rcx
0x0038CD11: je 0x14038c9f6
0x0038CD17: jmp 0x14038c9e9
0x0038CD1C: mov r8d, dword ptr [rbp + 0x28]
0x0038CD20: cmp r8d, 1
0x0038CD24: je 0x14038cd54
0x0038CD26: lea rdx, [rip + 0x379afb]
0x0038CD2D: mov rcx, rsi
0x0038CD30: call 0x140377140
0x0038CD35: mov rcx, qword ptr [rbp + 0x20]
0x0038CD39: test rcx, rcx
0x0038CD3C: je 0x14038cd4b
0x0038CD3E: mov rax, qword ptr [rip + 0x45f5db]
0x0038CD45: call qword ptr [rax + 0x80]
0x0038CD4B: mov rcx, qword ptr [rbp + 0x30]
0x0038CD4F: jmp 0x14038ce2c
0x0038CD54: mov rax, qword ptr [rbp + 0x30]
0x0038CD58: movzx ecx, byte ptr [rax]
0x0038CD5B: mov rax, qword ptr [rip + 0x45f5be]
0x0038CD62: mov byte ptr [rsp + 0x60], cl
0x0038CD66: mov rcx, qword ptr [rbp + 0x20]
0x0038CD6A: call qword ptr [rax + 0x80]
0x0038CD70: mov rcx, qword ptr [rbp + 0x30]
0x0038CD74: jmp 0x14038cda3
0x0038CD76: mov r8d, dword ptr [rbp + 0x18]
0x0038CD7A: cmp r8d, 1
0x0038CD7E: je 0x14038cd98
0x0038CD80: lea rdx, [rip + 0x379aa1]
0x0038CD87: mov rcx, rsi
0x0038CD8A: call 0x140377140
0x0038CD8F: mov rcx, qword ptr [rbp + 0x20]
0x0038CD93: jmp 0x14038ce31
0x0038CD98: mov rcx, qword ptr [rbp + 0x20]
0x0038CD9C: movzx eax, byte ptr [rcx]
0x0038CD9F: mov byte ptr [rsp + 0x60], al
0x0038CDA3: mov rax, qword ptr [rip + 0x45f576]
0x0038CDAA: call qword ptr [rax + 0x80]
0x0038CDB0: movzx eax, byte ptr [rsp + 0x60]
0x0038CDB5: test al, al
0x0038CDB7: jne 0x14038cdc2
0x0038CDB9: lea r8, [rip + 0x379a98]
0x0038CDC0: jmp 0x14038cdd6
0x0038CDC2: cmp al, 1
0x0038CDC4: lea rcx, [rip + 0x379aa5]
0x0038CDCB: lea r8, [rip + 0x379ab6]
0x0038CDD2: cmove r8, rcx
0x0038CDD6: lea rdx, [rip + 0x379acb]
0x0038CDDD: mov rcx, rsi
0x0038CDE0: call 0x140377200
0x0038CDE5: xor eax, eax
0x0038CDE7: jmp 0x14038ce51
0x0038CDE9: lea rdx, [rip + 0x379a00]
0x0038CDF0: mov rcx, rsi
0x0038CDF3: call 0x140377140
0x0038CDF8: mov rcx, qword ptr [rbp + 0x20]
0x0038CDFC: jmp 0x14038ce31
0x0038CDFE: lea rdx, [rip + 0x37998b]
0x0038CE05: mov rcx, rsi
0x0038CE08: call 0x140377140
0x0038CE0D: jmp 0x14038ce3e
0x0038CE0F: lea rdx, [rip + 0x379952]
0x0038CE16: jmp 0x14038ce1f
0x0038CE18: lea rdx, [rip + 0x379921]
0x0038CE1F: mov rcx, rsi
0x0038CE22: call 0x140377140
0x0038CE27: mov rcx, qword ptr [rsp + 0x70]
0x0038CE2C: test rcx, rcx
0x0038CE2F: je 0x14038ce3e
0x0038CE31: mov rax, qword ptr [rip + 0x45f4e8]
0x0038CE38: call qword ptr [rax + 0x80]
0x0038CE3E: mov rax, qword ptr [rip + 0x45f4db]
```

## 50. `0x0038CE38` in `0x0038C220..0x0038CE78`

```asm
0x0038CD76: mov r8d, dword ptr [rbp + 0x18]
0x0038CD7A: cmp r8d, 1
0x0038CD7E: je 0x14038cd98
0x0038CD80: lea rdx, [rip + 0x379aa1]
0x0038CD87: mov rcx, rsi
0x0038CD8A: call 0x140377140
0x0038CD8F: mov rcx, qword ptr [rbp + 0x20]
0x0038CD93: jmp 0x14038ce31
0x0038CD98: mov rcx, qword ptr [rbp + 0x20]
0x0038CD9C: movzx eax, byte ptr [rcx]
0x0038CD9F: mov byte ptr [rsp + 0x60], al
0x0038CDA3: mov rax, qword ptr [rip + 0x45f576]
0x0038CDAA: call qword ptr [rax + 0x80]
0x0038CDB0: movzx eax, byte ptr [rsp + 0x60]
0x0038CDB5: test al, al
0x0038CDB7: jne 0x14038cdc2
0x0038CDB9: lea r8, [rip + 0x379a98]
0x0038CDC0: jmp 0x14038cdd6
0x0038CDC2: cmp al, 1
0x0038CDC4: lea rcx, [rip + 0x379aa5]
0x0038CDCB: lea r8, [rip + 0x379ab6]
0x0038CDD2: cmove r8, rcx
0x0038CDD6: lea rdx, [rip + 0x379acb]
0x0038CDDD: mov rcx, rsi
0x0038CDE0: call 0x140377200
0x0038CDE5: xor eax, eax
0x0038CDE7: jmp 0x14038ce51
0x0038CDE9: lea rdx, [rip + 0x379a00]
0x0038CDF0: mov rcx, rsi
0x0038CDF3: call 0x140377140
0x0038CDF8: mov rcx, qword ptr [rbp + 0x20]
0x0038CDFC: jmp 0x14038ce31
0x0038CDFE: lea rdx, [rip + 0x37998b]
0x0038CE05: mov rcx, rsi
0x0038CE08: call 0x140377140
0x0038CE0D: jmp 0x14038ce3e
0x0038CE0F: lea rdx, [rip + 0x379952]
0x0038CE16: jmp 0x14038ce1f
0x0038CE18: lea rdx, [rip + 0x379921]
0x0038CE1F: mov rcx, rsi
0x0038CE22: call 0x140377140
0x0038CE27: mov rcx, qword ptr [rsp + 0x70]
0x0038CE2C: test rcx, rcx
0x0038CE2F: je 0x14038ce3e
0x0038CE31: mov rax, qword ptr [rip + 0x45f4e8]
0x0038CE38: call qword ptr [rax + 0x80]
0x0038CE3E: mov rax, qword ptr [rip + 0x45f4db]
0x0038CE45: lea rcx, [rbp - 8]
0x0038CE49: call qword ptr [rax + 0x48]
0x0038CE4C: mov eax, 7
0x0038CE51: mov rcx, qword ptr [rbp + 0x48]
0x0038CE55: xor rcx, rsp
0x0038CE58: call 0x1403b24c0
0x0038CE5D: mov rbx, qword ptr [rsp + 0x1a0]
0x0038CE65: add rsp, 0x150
0x0038CE6C: pop r15
0x0038CE6E: pop r14
0x0038CE70: pop r13
0x0038CE72: pop r12
0x0038CE74: pop rdi
0x0038CE75: pop rsi
0x0038CE76: pop rbp
0x0038CE77: ret
```

## 51. `0x0038CFEF` in `0x0038CF30..0x0038D008`

```asm
0x0038CF40: push r15
0x0038CF42: lea rbp, [rsp - 0x1f]
0x0038CF47: sub rsp, 0xc0
0x0038CF4E: mov rbx, qword ptr [rbp + 0x7f]
0x0038CF52: xor r13d, r13d
0x0038CF55: mov edi, r13d
0x0038CF58: mov qword ptr [rbp - 0x39], r13
0x0038CF5C: mov r15, r8
0x0038CF5F: mov qword ptr [rbp - 0x41], r13
0x0038CF63: mov rsi, rdx
0x0038CF66: mov r12, rcx
0x0038CF69: cmp qword ptr [rbx + 0x10], rdi
0x0038CF6D: je 0x14038cf86
0x0038CF6F: cmp dword ptr [rbx + 4], r13d
0x0038CF73: jne 0x14038cf86
0x0038CF75: mov rcx, rbx
0x0038CF78: call 0x14038d270
0x0038CF7D: lea eax, [r13 + 0x43]
0x0038CF81: jmp 0x14038d246
0x0038CF86: cmp qword ptr [rbx + 0x50], rdi
0x0038CF8A: jne 0x14038cfae
0x0038CF8C: mov rdx, qword ptr [rbp + 0x6f]
0x0038CF90: xor r8d, r8d
0x0038CF93: mov rcx, r9
0x0038CF96: call 0x14038d300
0x0038CF9B: mov qword ptr [rbx + 0x50], rax
0x0038CF9F: test rax, rax
0x0038CFA2: jne 0x14038cfae
0x0038CFA4: mov eax, 0x1b
0x0038CFA9: jmp 0x14038d246
0x0038CFAE: cmp qword ptr [rbx + 0x60], rdi
0x0038CFB2: jne 0x14038d008
0x0038CFB4: mov rax, qword ptr [rip + 0x45f365]
0x0038CFBB: lea rdx, [rbp - 0x31]
0x0038CFBF: lea rcx, [rip + 0x373eb2]
0x0038CFC6: call qword ptr [rax + 0x88]
0x0038CFCC: mov dword ptr [rbx + 4], eax
0x0038CFCF: test eax, eax
0x0038CFD1: je 0x14038cfdd
0x0038CFD3: mov eax, 4
0x0038CFD8: jmp 0x14038d246
0x0038CFDD: mov rcx, qword ptr [rbp - 0x31]
0x0038CFE1: mov eax, dword ptr [rcx + 8]
0x0038CFE4: mov qword ptr [rbx + 0x58], rax
0x0038CFE8: mov rax, qword ptr [rip + 0x45f331]
0x0038CFEF: call qword ptr [rax + 0x80]
0x0038CFF5: mov rcx, qword ptr [rbx + 0x58]
0x0038CFF9: call qword ptr [rip + 0x4497b9]
0x0038CFFF: mov qword ptr [rbx + 0x60], rax
0x0038D003: test rax, rax
0x0038D006: je 0x14038cfa4
```

## 52. `0x004151B9` in `0x0041518C..0x0041520B`

```asm
0x0041518C: mov qword ptr [rsp + 0x10], rdx
0x00415191: push rbx
0x00415192: push rbp
0x00415193: push rdi
0x00415194: sub rsp, 0x30
0x00415198: mov rbp, rdx
0x0041519B: mov rdi, qword ptr [rbp + 0x50]
0x0041519F: mov rcx, qword ptr [rdi + 0x90]
0x004151A6: test rcx, rcx
0x004151A9: je 0x1404151b3
0x004151AB: mov rax, qword ptr [rcx]
0x004151AE: mov dl, 1
0x004151B0: call qword ptr [rax + 0x18]
0x004151B3: mov rax, qword ptr [rdi]
0x004151B6: mov rcx, rdi
0x004151B9: call qword ptr [rax + 0x80]
0x004151BF: lea rcx, [rdi + 0xa8]
0x004151C6: call 0x140391ac4
0x004151CB: test eax, eax
0x004151CD: je 0x1404151d6
0x004151CF: mov ecx, eax
0x004151D1: call 0x14039219c
0x004151D6: lea rcx, [rdi + 0xf8]
0x004151DD: call 0x140135910
0x004151E2: nop
0x004151E3: lea rcx, [rdi + 0xa8]
0x004151EA: call 0x140391b24
0x004151EF: test eax, eax
0x004151F1: je 0x1404151fb
0x004151F3: mov ecx, eax
0x004151F5: call 0x14039219c
0x004151FA: nop
0x004151FB: lea rax, [rip - 0x2e33bb]
0x00415202: add rsp, 0x30
0x00415206: pop rdi
0x00415207: pop rbp
0x00415208: pop rbx
0x00415209: ret
0x0041520A: int3
```

## 53. `0x0041522E` in `0x0041520B..0x004152C7`

```asm
0x0041520B: mov qword ptr [rsp + 0x10], rdx
0x00415210: push rbx
0x00415211: push rbp
0x00415212: push rsi
0x00415213: push rdi
0x00415214: sub rsp, 0x38
0x00415218: mov rbp, rdx
0x0041521B: mov rsi, qword ptr [rbp + 0x50]
0x0041521F: mov rax, qword ptr [rsi]
0x00415222: mov rcx, rsi
0x00415225: call qword ptr [rax + 0x28]
0x00415228: mov rax, qword ptr [rsi]
0x0041522B: mov rcx, rsi
0x0041522E: call qword ptr [rax + 0x80]
0x00415234: lea rbx, [rsi + 0xa8]
0x0041523B: mov qword ptr [rbp + 0x1d0], rbx
0x00415242: mov rcx, rbx
0x00415245: call 0x140391ac4
0x0041524A: test eax, eax
0x0041524C: je 0x140415256
0x0041524E: mov ecx, eax
0x00415250: call 0x14039219c
0x00415255: nop
0x00415256: lea rcx, [rsi + 0xf8]
0x0041525D: call 0x140135910
0x00415262: mov r8, qword ptr [rip + 0x3d11a7]
0x00415269: sub r8, qword ptr [rip + 0x3d1198]
0x00415270: movabs rax, 0xc30c30c30c30c30d
0x0041527A: imul r8
0x0041527D: lea rdi, [r8 + rdx]
0x00415281: sar rdi, 7
0x00415285: mov rax, rdi
0x00415288: shr rax, 0x3f
0x0041528C: add rdi, rax
0x0041528F: mov rcx, rsi
0x00415292: call 0x140132280
0x00415297: mov rdx, rax
0x0041529A: mov ecx, edi
0x0041529C: call 0x140227010
0x004152A1: nop
0x004152A2: mov rcx, rbx
0x004152A5: call 0x140391b24
0x004152AA: test eax, eax
0x004152AC: je 0x1404152b6
0x004152AE: mov ecx, eax
0x004152B0: call 0x14039219c
0x004152B5: nop
0x004152B6: lea rax, [rip - 0x2e3476]
```
