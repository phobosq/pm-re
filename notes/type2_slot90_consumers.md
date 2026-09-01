# Type2 slot +0x90 child accessor consumers

Type2 vtable +0x90 is `0x1CF880` -> returns `[this+0x840]` NVIDIA child.

raw slot+0x90 callsites: `12`

## `0x00130628` function `0x001305F0..0x001309D9` score `1`

Timing/config displacement hits:
- `0x0013064F` disp `+0xB8`: `mov edx, dword ptr [rbp + 0xb8]`
- `0x0013069D` disp `+0x98`: `mov eax, dword ptr [rbx + 0x98]`
- `0x00130746` disp `+0x98`: `mov r8d, dword ptr [rbp + 0x98]`
- `0x0013074F` disp `+0xB0`: `mov r9d, dword ptr [rbp + 0xb0]`
- `0x00130794` disp `+0xB0`: `mov eax, dword ptr [rbp + 0xb0]`
- `0x001307A1` disp `+0x98`: `mov eax, dword ptr [rbp + 0x98]`
- `0x001307CB` disp `+0x98`: `mov r8d, dword ptr [rbp + 0x98]`
- `0x00130805` disp `+0x98`: `cmp dword ptr [rbp + 0x98], 0`

```asm
0x001305C8: call 0x14021c820
0x001305CD: mov rax, rbx
0x001305D0: mov rcx, qword ptr [rbp - 8]
0x001305D4: xor rcx, rsp
0x001305D7: call 0x1403b24c0
0x001305DC: mov rbx, qword ptr [rsp + 0x98]
0x001305E4: add rsp, 0x80
0x001305EB: pop rbp
0x001305EC: ret
0x001305ED: int3
0x001305EE: int3
0x001305EF: int3
0x001305F0: mov qword ptr [rsp + 0x10], rbx
0x001305F5: mov qword ptr [rsp + 0x18], rsi
0x001305FA: mov qword ptr [rsp + 0x20], rdi
0x001305FF: push rbp
0x00130600: lea rbp, [rsp - 0x110]
0x00130608: sub rsp, 0x210
0x0013060F: mov rax, qword ptr [rip + 0x6a62da]
0x00130616: xor rax, rsp
0x00130619: mov qword ptr [rbp + 0x100], rax
0x00130620: mov rax, qword ptr [rcx]
0x00130623: mov esi, edx
0x00130625: mov rbx, rcx
0x00130628: call qword ptr [rax + 0x90]
0x0013062E: mov rdi, rax
0x00130631: test rax, rax
0x00130634: je 0x1401309b1
0x0013063A: lea rdx, [rbp + 0x20]
0x0013063E: mov rcx, rbx
0x00130641: call 0x14006a320
0x00130646: cmp esi, 1
0x00130649: ja 0x140130705
0x0013064F: mov edx, dword ptr [rbp + 0xb8]
0x00130655: test edx, edx
0x00130657: js 0x14013066c
0x00130659: mov r8, qword ptr [rdi]
0x0013065C: mov rcx, rdi
0x0013065F: call qword ptr [r8 + 0x38]
0x00130663: mov byte ptr [rbx + 0x544], 1
0x0013066A: jmp 0x140130687
0x0013066C: cmp byte ptr [rbx + 0x544], 0
0x00130673: je 0x140130687
0x00130675: mov rax, qword ptr [rdi]
0x00130678: xor edx, edx
0x0013067A: mov rcx, rdi
0x0013067D: call qword ptr [rax + 0x38]
0x00130680: mov byte ptr [rbx + 0x544], 0
0x00130687: mov edx, dword ptr [rbp + 0xcc]
0x0013068D: mov r8d, dword ptr [rbp + 0xd0]
0x00130694: test edx, edx
0x00130696: jg 0x1401306ef
0x00130698: test r8d, r8d
0x0013069B: jne 0x1401306ef
0x0013069D: mov eax, dword ptr [rbx + 0x98]
0x001306A3: imul rcx, rax, 0xa8
```

## `0x00131790` function `0x001312E0..0x00131E84` score `1`

Timing/config displacement hits:
- `0x00131743` disp `+0x98`: `mov eax, dword ptr [rbx + 0x98]`
- `0x001318F5` disp `+0x98`: `mov dword ptr [rsp + 0x98], r8d`
- `0x00131926` disp `+0x98`: `mov eax, dword ptr [rbx + 0x98]`
- `0x00131B8D` disp `+0x98`: `mov eax, dword ptr [rbx + 0x98]`
- `0x00131CAC` disp `+0xB0`: `lea rcx, [rsp + 0xb0]`
- `0x00131CD5` disp `+0xB0`: `lea rdx, [rsp + 0xb0]`
- `0x00131CE2` disp `+0xB8`: `cmp dword ptr [rsp + 0xb8], 0`
- `0x00131D37` disp `+0x98`: `mov edx, dword ptr [rbx + 0x98]`

```asm
0x0013171A: test r13b, r13b
0x0013171D: je 0x140131926
0x00131723: cmp byte ptr [rsp + 0x3b4], dil
0x0013172B: je 0x140131926
0x00131731: cmp dword ptr [rsp + 0x39c], edi
0x00131738: jg 0x14013178a
0x0013173A: cmp dword ptr [rsp + 0x3a0], edi
0x00131741: jne 0x14013178a
0x00131743: mov eax, dword ptr [rbx + 0x98]
0x00131749: imul rcx, rax, 0xa8
0x00131750: mov rax, qword ptr [rip + 0x6b4cb1]
0x00131757: cmp dword ptr [rcx + rax + 0xc], 2
0x0013175C: jne 0x140131926
0x00131762: lea rax, [rsp + 0x3a4]
0x0013176A: nop word ptr [rax + rax]
0x00131770: cmp dword ptr [rax], edi
0x00131772: jne 0x14013178a
0x00131774: add rax, 4
0x00131778: lea rcx, [rsp + 0x3b0]
0x00131780: cmp rax, rcx
0x00131783: jne 0x140131770
0x00131785: jmp 0x140131926
0x0013178A: mov rax, qword ptr [rbx]
0x0013178D: mov rcx, rbx
0x00131790: call qword ptr [rax + 0x90]
0x00131796: test rax, rax
0x00131799: je 0x140131861
0x0013179F: mov rcx, rax
0x001317A2: call 0x14014b9d0
0x001317A7: call 0x140391638
0x001317AC: mov qword ptr [rsp + 0x1e0], rax
0x001317B4: imul rcx, rax, 0x64
0x001317B8: mov qword ptr [rsp + 0x1e8], rcx
0x001317C0: mov qword ptr [rsp + 0x1f0], rcx
0x001317C8: movabs rax, 0x12a05f200
0x001317D2: mov qword ptr [rsp + 0x218], rax
0x001317DA: mov qword ptr [rsp + 0x220], rax
0x001317E2: lea r8, [rcx + rax]
0x001317E6: movabs rax, 0x112e0be826d694b3
0x001317F0: imul r8
0x001317F3: sar rdx, 0x1a
0x001317F7: mov rax, rdx
0x001317FA: shr rax, 0x3f
0x001317FE: add rdx, rax
0x00131801: mov qword ptr [rsp + 0x100], rdx
0x00131809: mov qword ptr [rsp + 0x108], rdx
0x00131811: mov qword ptr [rsp + 0x110], rdx
0x00131819: mov qword ptr [rsp + 0x80], rdx
0x00131821: imul rax, rdx, 0x3b9aca00
0x00131828: mov qword ptr [rsp + 0x118], rax
0x00131830: mov qword ptr [rsp + 0x120], rax
0x00131838: sub r8, rax
0x0013183B: mov dword ptr [rsp + 0x88], r8d
0x00131843: movaps xmm0, xmmword ptr [rsp + 0x80]
0x0013184B: movdqa xmmword ptr [rsp + 0x280], xmm0
0x00131854: lea rcx, [rsp + 0x280]
```

## `0x0013196F` function `0x001312E0..0x00131E84` score `1`

Timing/config displacement hits:
- `0x00131743` disp `+0x98`: `mov eax, dword ptr [rbx + 0x98]`
- `0x001318F5` disp `+0x98`: `mov dword ptr [rsp + 0x98], r8d`
- `0x00131926` disp `+0x98`: `mov eax, dword ptr [rbx + 0x98]`
- `0x00131B8D` disp `+0x98`: `mov eax, dword ptr [rbx + 0x98]`
- `0x00131CAC` disp `+0xB0`: `lea rcx, [rsp + 0xb0]`
- `0x00131CD5` disp `+0xB0`: `lea rdx, [rsp + 0xb0]`
- `0x00131CE2` disp `+0xB8`: `cmp dword ptr [rsp + 0xb8], 0`
- `0x00131D37` disp `+0x98`: `mov edx, dword ptr [rbx + 0x98]`

```asm
0x001318DB: imul rax, rdx, 0x3b9aca00
0x001318E2: mov qword ptr [rsp + 0x168], rax
0x001318EA: mov qword ptr [rsp + 0x170], rax
0x001318F2: sub r8, rax
0x001318F5: mov dword ptr [rsp + 0x98], r8d
0x001318FD: movaps xmm0, xmmword ptr [rsp + 0x90]
0x00131905: movdqa xmmword ptr [rsp + 0x290], xmm0
0x0013190E: lea rcx, [rsp + 0x290]
0x00131916: call 0x140391484
0x0013191B: mov eax, r15d
0x0013191E: lock xadd dword ptr [rbx + 0xa0], eax
0x00131926: mov eax, dword ptr [rbx + 0x98]
0x0013192C: imul rcx, rax, 0xa8
0x00131933: mov rax, qword ptr [rip + 0x6b4ace]
0x0013193A: cmp dword ptr [rcx + rax + 0xc], 2
0x0013193F: jne 0x140131a52
0x00131945: cmp byte ptr [rsp + 0x3b5], dil
0x0013194D: je 0x140131a52
0x00131953: cmp dword ptr [rsp + 0x350], edi
0x0013195A: jg 0x140131969
0x0013195C: cmp dword ptr [rsp + 0x354], edi
0x00131963: jle 0x140131a52
0x00131969: mov rax, qword ptr [rbx]
0x0013196C: mov rcx, rbx
0x0013196F: call qword ptr [rax + 0x90]
0x00131975: mov rcx, rax
0x00131978: test rax, rax
0x0013197B: je 0x140131a52
0x00131981: mov rax, qword ptr [rax]
0x00131984: call qword ptr [rax + 0x40]
0x00131987: mov eax, r15d
0x0013198A: lock xadd dword ptr [rbx + 0xa0], eax
0x00131992: call 0x140391638
0x00131997: mov qword ptr [rsp + 0x178], rax
0x0013199F: imul rcx, rax, 0x64
0x001319A3: mov qword ptr [rsp + 0x180], rcx
0x001319AB: mov qword ptr [rsp + 0x188], rcx
0x001319B3: mov eax, 0xb2d05e00
0x001319B8: mov qword ptr [rsp + 0x190], rax
0x001319C0: mov qword ptr [rsp + 0x198], rax
0x001319C8: lea r8, [rcx + rax]
0x001319CC: movabs rax, 0x112e0be826d694b3
0x001319D6: imul r8
0x001319D9: sar rdx, 0x1a
0x001319DD: mov rax, rdx
0x001319E0: shr rax, 0x3f
0x001319E4: add rdx, rax
0x001319E7: mov qword ptr [rsp + 0x1a0], rdx
0x001319EF: mov qword ptr [rsp + 0x1a8], rdx
0x001319F7: mov qword ptr [rsp + 0x1b0], rdx
0x001319FF: mov qword ptr [rsp + 0xa0], rdx
0x00131A07: imul rax, rdx, 0x3b9aca00
0x00131A0E: mov qword ptr [rsp + 0x1b8], rax
0x00131A16: mov qword ptr [rsp + 0x1c0], rax
0x00131A1E: sub r8, rax
0x00131A21: mov dword ptr [rsp + 0xa8], r8d
```

## `0x00134DF3` function `0x00134D80..0x00134FE0` score `1`

Timing/config displacement hits:
- `0x00134EB4` disp `+0x98`: `mov eax, dword ptr [rsi + 0x98]`
- `0x00134F57` disp `+0x440`: `mov dword ptr [rsi + 0x440], r14d`

```asm
0x00134D97: mov qword ptr [rsp + 0x38], 0xfffffffffffffffe
0x00134DA0: mov qword ptr [rsp + 0x230], rbx
0x00134DA8: mov rsi, rcx
0x00134DAB: lea rdx, [rsp + 0x40]
0x00134DB0: call 0x14006a320
0x00134DB5: lea rdx, [rbp + 0x20]
0x00134DB9: mov rcx, rsi
0x00134DBC: call 0x140084a60
0x00134DC1: xor eax, eax
0x00134DC3: mov ebx, eax
0x00134DC5: mov eax, 1
0x00134DCA: cmp dword ptr [rbp - 0x44], ebx
0x00134DCD: cmovg ebx, eax
0x00134DD0: cmp dword ptr [rbp - 0x40], 0
0x00134DD4: jle 0x140134dd9
0x00134DD6: or ebx, 4
0x00134DD9: mov r14d, dword ptr [rbp - 0x3c]
0x00134DDD: test r14d, r14d
0x00134DE0: jle 0x140134de5
0x00134DE2: or ebx, 2
0x00134DE5: test ebx, ebx
0x00134DE7: je 0x140134fc9
0x00134DED: mov rax, qword ptr [rsi]
0x00134DF0: mov rcx, rsi
0x00134DF3: call qword ptr [rax + 0x90]
0x00134DF9: test rax, rax
0x00134DFC: je 0x140134fc9
0x00134E02: mov r8d, ebx
0x00134E05: lea rdx, [rbp + 0x140]
0x00134E0C: mov rcx, rax
0x00134E0F: call 0x14014b790
0x00134E14: mov ebx, dword ptr [rsp + 0x44]
0x00134E18: mov edi, ebx
0x00134E1A: mov dword ptr [rbp + 0x138], ebx
0x00134E20: mov r12d, dword ptr [rbp + 0x24]
0x00134E24: cmp dword ptr [rbp - 0x44], 0
0x00134E28: jle 0x140134e55
0x00134E2A: movsx r8d, word ptr [rbp + 0x140]
0x00134E32: mov byte ptr [rsp + 0x28], 0
0x00134E37: mov dword ptr [rsp + 0x20], r12d
0x00134E3C: mov r9d, dword ptr [rbp - 0x44]
0x00134E40: mov edx, ebx
0x00134E42: mov rcx, rsi
0x00134E45: call 0x140131020
0x00134E4A: test eax, eax
0x00134E4C: cmovns edi, eax
0x00134E4F: mov dword ptr [rbp + 0x138], edi
0x00134E55: cmp dword ptr [rbp - 0x40], 0
0x00134E59: jle 0x140134eaf
0x00134E5B: movsx r8d, word ptr [rbp + 0x144]
0x00134E63: mov byte ptr [rsp + 0x28], 0
0x00134E68: mov dword ptr [rsp + 0x20], r12d
0x00134E6D: mov r9d, dword ptr [rbp - 0x40]
0x00134E71: mov edx, ebx
0x00134E73: mov rcx, rsi
0x00134E76: call 0x140131020
```

## `0x001C4543` function `0x001C44F0..0x001C5118` score `1`

Timing/config displacement hits:
- `0x001C4568` disp `+0x98`: `call qword ptr [rax + 0x98]`
- `0x001C4597` disp `+0x98`: `call qword ptr [rax + 0x98]`

```asm
0x001C44EB: int3
0x001C44EC: int3
0x001C44ED: int3
0x001C44EE: int3
0x001C44EF: int3
0x001C44F0: mov rax, rsp
0x001C44F3: push rbp
0x001C44F4: lea rbp, [rax - 0x2b8]
0x001C44FB: sub rsp, 0x3b0
0x001C4502: mov qword ptr [rsp + 0x20], 0xfffffffffffffffe
0x001C450B: mov qword ptr [rax + 0x10], rbx
0x001C450F: mov qword ptr [rax + 0x18], rsi
0x001C4513: mov qword ptr [rax + 0x20], rdi
0x001C4517: mov rax, qword ptr [rip + 0x6123d2]
0x001C451E: xor rax, rsp
0x001C4521: mov qword ptr [rbp + 0x2a0], rax
0x001C4528: movzx ebx, dl
0x001C452B: mov rdi, rcx
0x001C452E: mov eax, dword ptr [rcx + 0x3c]
0x001C4531: sub eax, 2
0x001C4534: cmp eax, 1
0x001C4537: jbe 0x1401c50f0
0x001C453D: mov rcx, qword ptr [rcx]
0x001C4540: mov rax, qword ptr [rcx]
0x001C4543: call qword ptr [rax + 0x90]
0x001C4549: mov esi, eax
0x001C454B: test eax, eax
0x001C454D: js 0x1401c50f0
0x001C4553: cmp eax, dword ptr [rdi + 0x4c]
0x001C4556: jle 0x1401c455b
0x001C4558: mov dword ptr [rdi + 0x4c], eax
0x001C455B: cmp esi, dword ptr [rdi + 0x48]
0x001C455E: je 0x1401c458f
0x001C4560: mov rcx, qword ptr [rdi]
0x001C4563: mov rax, qword ptr [rcx]
0x001C4566: mov edx, esi
0x001C4568: call qword ptr [rax + 0x98]
0x001C456E: test al, al
0x001C4570: je 0x1401c4576
0x001C4572: mov byte ptr [rdi + 0x44], 0
0x001C4576: mov eax, esi
0x001C4578: sub eax, dword ptr [rdi + 0x48]
0x001C457B: cdq
0x001C457C: xor eax, edx
0x001C457E: sub eax, edx
0x001C4580: cmp eax, 5
0x001C4583: jle 0x1401c458f
0x001C4585: mov dword ptr [rdi + 0x50], 0
0x001C458C: mov dword ptr [rdi + 0x48], esi
0x001C458F: mov rcx, qword ptr [rdi]
0x001C4592: mov rax, qword ptr [rcx]
0x001C4595: mov edx, esi
0x001C4597: call qword ptr [rax + 0x98]
0x001C459D: test al, al
0x001C459F: jne 0x1401c45ad
0x001C45A1: mov dword ptr [rdi + 0x54], 0
```

## `0x001F8F25` function `0x001F7F40..0x001FB9C1` score `1`

Timing/config displacement hits:
- `0x001F8020` disp `+0x418`: `cmp qword ptr [rdi + 0x418], 0`
- `0x001F80E3` disp `+0xB8`: `cmp qword ptr [rsi + 0xb8], 0`
- `0x001F8149` disp `+0xB8`: `sub rdx, qword ptr [rsi + 0xb8]`
- `0x001F8176` disp `+0xB8`: `mov qword ptr [rsi + 0xb8], r14`
- `0x001F8192` disp `+0x98`: `mov qword ptr [rsi + 0x98], r14`
- `0x001F857C` disp `+0xB8`: `mov qword ptr [rsi + 0xb8], r14`
- `0x001F8598` disp `+0x98`: `mov qword ptr [rsi + 0x98], r14`
- `0x001F8E31` disp `+0x98`: `mov dword ptr [rbp + 0x98], eax`
- `0x001F8E37` disp `+0x98`: `lea rcx, [rbp + 0x98]`
- `0x001F8EA8` disp `+0xB0`: `cmp r14d, dword ptr [rsi + 0xb0]`
- `0x001F90CA` disp `+0xB0`: `mov qword ptr [rbp + 0xb0], rcx`
- `0x001F9466` disp `+0xB0`: `mov rax, qword ptr [rbp + 0xb0]`
- `0x001FB812` disp `+0x368`: `lea rax, [rbp + 0x368]`
- `0x001FB83B` disp `+0x368`: `lea rcx, [rbp + 0x368]`
- `0x001FB901` disp `+0xB8`: `mov qword ptr [rbp + 0xb8], rax`
- `0x001FB944` disp `+0xB8`: `mov qword ptr [rbp + 0xb8], rax`
- `0x001FB952` disp `+0xB8`: `lea rcx, [rbp + 0xb8]`

```asm
0x001F8EAF: je 0x1401f8f40
0x001F8EB5: mov eax, r11d
0x001F8EB8: imul eax, dword ptr [rdi + 0x1b0]
0x001F8EBF: xorps xmm0, xmm0
0x001F8EC2: cvtsi2sd xmm0, rax
0x001F8EC7: mulsd xmm0, qword ptr [rdi + 0x3e0]
0x001F8ECF: addsd xmm0, xmm14
0x001F8ED4: mulsd xmm0, xmm15
0x001F8ED9: cvttsd2si rbx, xmm0
0x001F8EDE: movsxd r12, r14d
0x001F8EE1: mov r10, qword ptr [rdi]
0x001F8EE4: mov dword ptr [rsp + 0x48], r14d
0x001F8EE9: mov eax, dword ptr [rsp + 0x5c]
0x001F8EED: mov dword ptr [rsp + 0x40], eax
0x001F8EF1: mov rax, qword ptr [rbp - 0x78]
0x001F8EF5: mov dword ptr [rsp + 0x38], eax
0x001F8EF9: mov rax, qword ptr [rdi + r12*8 + 0x200]
0x001F8F01: mov qword ptr [rsp + 0x30], rax
0x001F8F06: mov qword ptr [rsp + 0x28], r13
0x001F8F0B: mov dword ptr [rsp + 0x20], ebx
0x001F8F0F: mov r9, qword ptr [rbp - 0x10]
0x001F8F13: mov r8, qword ptr [rbp + 0x1290]
0x001F8F1A: mov rdx, qword ptr [rdi + r12*8 + 0x1b8]
0x001F8F22: mov rcx, rdi
0x001F8F25: call qword ptr [r10 + 0x90]
0x001F8F2C: shl ebx, 6
0x001F8F2F: mov ecx, ebx
0x001F8F31: mov qword ptr [rsi + 0x68], rcx
0x001F8F35: add qword ptr [rsi + 0x58], rcx
0x001F8F39: inc dword ptr [rsi + 0x38]
0x001F8F3C: mov ebx, eax
0x001F8F3E: jmp 0x1401f8fb2
0x001F8F40: movsxd r12, r14d
0x001F8F43: mov r10, qword ptr [rdi]
0x001F8F46: mov dword ptr [rsp + 0x48], r14d
0x001F8F4B: mov eax, dword ptr [rsp + 0x5c]
0x001F8F4F: mov dword ptr [rsp + 0x40], eax
0x001F8F53: mov rax, qword ptr [rbp - 0x78]
0x001F8F57: mov dword ptr [rsp + 0x38], eax
0x001F8F5B: mov rax, qword ptr [rdi + r12*8 + 0x200]
0x001F8F63: mov qword ptr [rsp + 0x30], rax
0x001F8F68: mov qword ptr [rsp + 0x28], r13
0x001F8F6D: mov dword ptr [rsp + 0x20], r11d
0x001F8F72: mov r9, qword ptr [rbp - 0x10]
0x001F8F76: mov r8, qword ptr [rbp + 0x1290]
0x001F8F7D: mov rdx, qword ptr [rdi + r12*8 + 0x1b8]
0x001F8F85: mov rcx, rdi
0x001F8F88: call qword ptr [r10 + 0x88]
0x001F8F8F: mov ebx, eax
0x001F8F91: mov ecx, dword ptr [rsp + 0x74]
0x001F8F95: imul ecx, dword ptr [rdi + 0x1b0]
0x001F8F9C: mov qword ptr [rsi + 0x60], rcx
0x001F8FA0: add qword ptr [rsi + 0x50], rcx
0x001F8FA4: cmp dword ptr [rsi + 0x2c], 0
0x001F8FA8: jne 0x1401f8faf
0x001F8FAA: inc dword ptr [rsi + 0x38]
```

## `0x00338975` function `0x003381A0..0x00338B05` score `1`

Timing/config displacement hits:
- `0x00338628` disp `+0x98`: `mov qword ptr [rsp + 0x98], rax`
- `0x003386B8` disp `+0x98`: `cmp qword ptr [rsp + 0x98], rdi`
- `0x003386E4` disp `+0xB0`: `mov qword ptr [rsp + 0xb0], rax`
- `0x00338748` disp `+0xB8`: `mov qword ptr [rsp + 0xb8], r13`
- `0x0033886F` disp `+0xB0`: `mov rsi, qword ptr [rsp + 0xb0]`
- `0x00338877` disp `+0xB8`: `mov r14, qword ptr [rsp + 0xb8]`
- `0x00338990` disp `+0x98`: `mov r15, qword ptr [rsp + 0x98]`

```asm
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
0x00338990: mov r15, qword ptr [rsp + 0x98]
0x00338998: nop dword ptr [rax + rax]
0x003389A0: movaps xmm2, xmm7
0x003389A3: mov edx, dword ptr [rsp + 0x140]
0x003389AA: lea rcx, [rsp + 0x140]
0x003389B2: call 0x1402d8260
0x003389B7: lea rdx, [rsp + 0x140]
0x003389BF: mov rcx, rsi
0x003389C2: call r15
0x003389C5: test eax, eax
0x003389C7: je 0x1403389dd
0x003389C9: test rbx, rbx
0x003389CC: je 0x1403389a0
0x003389CE: call qword ptr [rip + 0xf7b9c]
0x003389D4: sub eax, edi
0x003389D6: cmp eax, 0x3e8
0x003389DB: jb 0x1403389a0
0x003389DD: mov r15, rbx
0x003389E0: mov dword ptr [rsp + 0x3e0], 0x438
0x003389EB: cmp dword ptr [rsp + 0x48], 0
0x003389F0: je 0x1403389fa
0x003389F2: call qword ptr [rip + 0xf7b78]
0x003389F8: mov edi, eax
0x003389FA: lea rdx, [rsp + 0x3e0]
0x00338A02: mov rcx, rsi
0x00338A05: call qword ptr [rsp + 0x60]
0x00338A09: test eax, eax
```
