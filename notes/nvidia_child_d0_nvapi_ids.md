# NVIDIA child +0xD0 NvAPI function provenance

Find calls whose RCX is loaded from child `+0xD0`, then resolve RIP-global function slots and their initialization sites.

calls: `56`

## call `0x001D51F6` function slot `0x007E7AF0`

```asm
0x001D51B9: jmp 0x1401d51cf
0x001D51BB: mov rcx, qword ptr [r10 + rax*8]
0x001D51BF: mov qword ptr [rbx + 0xd0], rcx
0x001D51C6: mov dword ptr [r10 + rax*8 + 8], 0xffffffff
0x001D51CF: mov rcx, qword ptr [rbx + 0xd0]
0x001D51D6: test rcx, rcx
0x001D51D9: je 0x1401d5b26
0x001D51DF: mov rax, qword ptr [rip + 0x61290a]
0x001D51E6: test rax, rax
0x001D51E9: je 0x1401d5435
0x001D51EF: lea rdx, [rbx + 0xdc]
0x001D51F6: call rax
0x001D51F8: mov dword ptr [rsp + 0x38], eax
0x001D51FC: test eax, eax
0x001D51FE: je 0x1401d5435
```

### refs to global slot `0x007E7AF0`: `2`

#### ref `0x001D51DF`

```asm
0x001D5193: and r9, rcx
0x001D5196: nop word ptr [rax + rax]
0x001D51A0: add rax, rax
0x001D51A3: mov ecx, dword ptr [r10 + rax*8 + 8]
0x001D51A8: shl ecx, 0x10
0x001D51AB: cmp rcx, r9
0x001D51AE: je 0x1401d51bb
0x001D51B0: inc edx
0x001D51B2: mov eax, edx
0x001D51B4: cmp rax, r8
0x001D51B7: jb 0x1401d51a0
0x001D51B9: jmp 0x1401d51cf
0x001D51BB: mov rcx, qword ptr [r10 + rax*8]
0x001D51BF: mov qword ptr [rbx + 0xd0], rcx
0x001D51C6: mov dword ptr [r10 + rax*8 + 8], 0xffffffff
0x001D51CF: mov rcx, qword ptr [rbx + 0xd0]
0x001D51D6: test rcx, rcx
0x001D51D9: je 0x1401d5b26
0x001D51DF: mov rax, qword ptr [rip + 0x61290a]
0x001D51E6: test rax, rax
0x001D51E9: je 0x1401d5435
0x001D51EF: lea rdx, [rbx + 0xdc]
0x001D51F6: call rax
0x001D51F8: mov dword ptr [rsp + 0x38], eax
0x001D51FC: test eax, eax
0x001D51FE: je 0x1401d5435
```

#### ref `0x001FE69F`

```asm
0x001FE633: mov qword ptr [rip + 0x5e9486], rax
0x001FE63A: call qword ptr [rip + 0x5e93b8]
0x001FE640: mov ecx, 0xfb85b01e
0x001FE645: mov qword ptr [rip + 0x5e947c], rax
0x001FE64C: call qword ptr [rip + 0x5e93a6]
0x001FE652: mov ecx, 0x35aed5e8
0x001FE657: mov qword ptr [rip + 0x5e9472], rax
0x001FE65E: call qword ptr [rip + 0x5e9394]
0x001FE664: mov ecx, 0x814b209f
0x001FE669: mov qword ptr [rip + 0x5e9468], rax
0x001FE670: call qword ptr [rip + 0x5e9382]
0x001FE676: mov ecx, 0xa58971a5
0x001FE67B: mov qword ptr [rip + 0x5e945e], rax
0x001FE682: call qword ptr [rip + 0x5e9370]
0x001FE688: mov ecx, 0x57f7caac
0x001FE68D: mov qword ptr [rip + 0x5e9454], rax
0x001FE694: call qword ptr [rip + 0x5e935e]
0x001FE69A: mov ecx, 0x42aea16a
0x001FE69F: mov qword ptr [rip + 0x5e944a], rax
0x001FE6A6: call qword ptr [rip + 0x5e934c]
0x001FE6AC: mov ecx, 0x2ddfb66e
0x001FE6B1: mov qword ptr [rip + 0x5e9440], rax
0x001FE6B8: call qword ptr [rip + 0x5e933a]
0x001FE6BE: mov ecx, 0x2eb3c140
0x001FE6C3: mov qword ptr [rip + 0x5e9436], rax
0x001FE6CA: call qword ptr [rip + 0x5e9328]
```

## call `0x001D5453` function slot `0x007E7AF8`

```asm
0x001D5435: mov rax, qword ptr [rip + 0x6126bc]
0x001D543C: test rax, rax
0x001D543F: je 0x1401d57a2
0x001D5445: lea rdx, [rbx + 0xe0]
0x001D544C: mov rcx, qword ptr [rbx + 0xd0]
0x001D5453: call rax
0x001D5455: mov dword ptr [rsp + 0x40], eax
0x001D5459: test eax, eax
0x001D545B: je 0x1401d57a2
```

### refs to global slot `0x007E7AF8`: `2`

#### ref `0x001D5435`

```asm
0x001D53EB: jb 0x1401d53f3
0x001D53ED: call 0x1403db020
0x001D53F2: int3
0x001D53F3: sub rcx, rax
0x001D53F6: cmp rcx, 8
0x001D53FA: jae 0x1401d5402
0x001D53FC: call 0x1403db020
0x001D5401: int3
0x001D5402: cmp rcx, 0x27
0x001D5406: jbe 0x1401d540e
0x001D5408: call 0x1403db020
0x001D540D: int3
0x001D540E: mov rcx, rax
0x001D5411: call 0x1403b20d4
0x001D5416: mov qword ptr [rbp + 0x118], 0xf
0x001D5421: mov qword ptr [rbp + 0x110], rdi
0x001D5428: mov byte ptr [rbp + 0x100], 0
0x001D542F: mov dword ptr [rbx + 0xdc], edi
0x001D5435: mov rax, qword ptr [rip + 0x6126bc]
0x001D543C: test rax, rax
0x001D543F: je 0x1401d57a2
0x001D5445: lea rdx, [rbx + 0xe0]
0x001D544C: mov rcx, qword ptr [rbx + 0xd0]
0x001D5453: call rax
0x001D5455: mov dword ptr [rsp + 0x40], eax
0x001D5459: test eax, eax
```

#### ref `0x001FE6B1`

```asm
0x001FE645: mov qword ptr [rip + 0x5e947c], rax
0x001FE64C: call qword ptr [rip + 0x5e93a6]
0x001FE652: mov ecx, 0x35aed5e8
0x001FE657: mov qword ptr [rip + 0x5e9472], rax
0x001FE65E: call qword ptr [rip + 0x5e9394]
0x001FE664: mov ecx, 0x814b209f
0x001FE669: mov qword ptr [rip + 0x5e9468], rax
0x001FE670: call qword ptr [rip + 0x5e9382]
0x001FE676: mov ecx, 0xa58971a5
0x001FE67B: mov qword ptr [rip + 0x5e945e], rax
0x001FE682: call qword ptr [rip + 0x5e9370]
0x001FE688: mov ecx, 0x57f7caac
0x001FE68D: mov qword ptr [rip + 0x5e9454], rax
0x001FE694: call qword ptr [rip + 0x5e935e]
0x001FE69A: mov ecx, 0x42aea16a
0x001FE69F: mov qword ptr [rip + 0x5e944a], rax
0x001FE6A6: call qword ptr [rip + 0x5e934c]
0x001FE6AC: mov ecx, 0x2ddfb66e
0x001FE6B1: mov qword ptr [rip + 0x5e9440], rax
0x001FE6B8: call qword ptr [rip + 0x5e933a]
0x001FE6BE: mov ecx, 0x2eb3c140
0x001FE6C3: mov qword ptr [rip + 0x5e9436], rax
0x001FE6CA: call qword ptr [rip + 0x5e9328]
0x001FE6D0: mov ecx, 0x65fe3aad
0x001FE6D5: mov qword ptr [rip + 0x5e942c], rax
0x001FE6DC: call qword ptr [rip + 0x5e9316]
```

## call `0x001D57D2` function slot `0x007E7B00`

```asm
0x001D57B7: mov qword ptr [rsp + 0x20], rcx
0x001D57BC: lea r9, [rsp + 0x58]
0x001D57C1: lea r8, [rsp + 0x5c]
0x001D57C6: lea rdx, [rsp + 0x50]
0x001D57CB: mov rcx, qword ptr [rbx + 0xd0]
0x001D57D2: call rax
0x001D57D4: mov dword ptr [rsp + 0x48], eax
0x001D57D8: test eax, eax
0x001D57DA: je 0x1401d5aca
```

### refs to global slot `0x007E7B00`: `2`

#### ref `0x001D57A2`

```asm
0x001D5758: jb 0x1401d5760
0x001D575A: call 0x1403db020
0x001D575F: int3
0x001D5760: sub rcx, rax
0x001D5763: cmp rcx, 8
0x001D5767: jae 0x1401d576f
0x001D5769: call 0x1403db020
0x001D576E: int3
0x001D576F: cmp rcx, 0x27
0x001D5773: jbe 0x1401d577b
0x001D5775: call 0x1403db020
0x001D577A: int3
0x001D577B: mov rcx, rax
0x001D577E: call 0x1403b20d4
0x001D5783: mov qword ptr [rbp + 0x138], 0xf
0x001D578E: mov qword ptr [rbp + 0x130], rdi
0x001D5795: mov byte ptr [rbp + 0x120], 0
0x001D579C: mov dword ptr [rbx + 0xe0], edi
0x001D57A2: mov rax, qword ptr [rip + 0x612357]
0x001D57A9: test rax, rax
0x001D57AC: je 0x1401d5ad4
0x001D57B2: lea rcx, [rsp + 0x54]
0x001D57B7: mov qword ptr [rsp + 0x20], rcx
0x001D57BC: lea r9, [rsp + 0x58]
0x001D57C1: lea r8, [rsp + 0x5c]
0x001D57C6: lea rdx, [rsp + 0x50]
```

#### ref `0x001FE6C3`

```asm
0x001FE657: mov qword ptr [rip + 0x5e9472], rax
0x001FE65E: call qword ptr [rip + 0x5e9394]
0x001FE664: mov ecx, 0x814b209f
0x001FE669: mov qword ptr [rip + 0x5e9468], rax
0x001FE670: call qword ptr [rip + 0x5e9382]
0x001FE676: mov ecx, 0xa58971a5
0x001FE67B: mov qword ptr [rip + 0x5e945e], rax
0x001FE682: call qword ptr [rip + 0x5e9370]
0x001FE688: mov ecx, 0x57f7caac
0x001FE68D: mov qword ptr [rip + 0x5e9454], rax
0x001FE694: call qword ptr [rip + 0x5e935e]
0x001FE69A: mov ecx, 0x42aea16a
0x001FE69F: mov qword ptr [rip + 0x5e944a], rax
0x001FE6A6: call qword ptr [rip + 0x5e934c]
0x001FE6AC: mov ecx, 0x2ddfb66e
0x001FE6B1: mov qword ptr [rip + 0x5e9440], rax
0x001FE6B8: call qword ptr [rip + 0x5e933a]
0x001FE6BE: mov ecx, 0x2eb3c140
0x001FE6C3: mov qword ptr [rip + 0x5e9436], rax
0x001FE6CA: call qword ptr [rip + 0x5e9328]
0x001FE6D0: mov ecx, 0x65fe3aad
0x001FE6D5: mov qword ptr [rip + 0x5e942c], rax
0x001FE6DC: call qword ptr [rip + 0x5e9316]
0x001FE6E2: mov qword ptr [rip + 0x5e9427], rax
0x001FE6E9: mov al, 1
0x001FE6EB: mov rcx, qword ptr [rbp + 0x4f]
```

## call `0x001D5B10` function slot `0x007E7AD0`

```asm
0x001D5AF0: mov r8d, 0x628
0x001D5AF6: lea rcx, [rbp + 0x184]
0x001D5AFD: call 0x1403d3050
0x001D5B02: lea rdx, [rbp + 0x180]
0x001D5B09: mov rcx, qword ptr [rbx + 0xd0]
0x001D5B10: call rdi
0x001D5B12: test eax, eax
0x001D5B14: jne 0x1401d5da3
0x001D5B1A: mov byte ptr [rbx + 0xd8], 1
```

### refs to global slot `0x007E7AD0`: `2`

#### ref `0x001D5AD4`

```asm
0x001D5A89: cmp qword ptr [rax + 0x18], 0x10
0x001D5A8E: jb 0x1401d5a93
0x001D5A90: mov rax, qword ptr [rax]
0x001D5A93: lea r8, [rsp + 0x48]
0x001D5A98: lea rdx, [rsp + 0x4c]
0x001D5A9D: mov rcx, rax
0x001D5AA0: call 0x1401d3fc0
0x001D5AA5: nop
0x001D5AA6: mov rdx, qword ptr [rbp + 0x158]
0x001D5AAD: cmp rdx, 0x10
0x001D5AB1: jb 0x1401d5ace
0x001D5AB3: inc rdx
0x001D5AB6: mov r8d, 1
0x001D5ABC: mov rcx, qword ptr [rbp + 0x140]
0x001D5AC3: call 0x140033d30
0x001D5AC8: jmp 0x1401d5ace
0x001D5ACA: mov edi, dword ptr [rsp + 0x50]
0x001D5ACE: mov dword ptr [rbx + 0x39c], edi
0x001D5AD4: mov rdi, qword ptr [rip + 0x611ff5]
0x001D5ADB: test rdi, rdi
0x001D5ADE: je 0x1401d5da3
0x001D5AE4: mov dword ptr [rbp + 0x180], 0x1062c
0x001D5AEE: xor edx, edx
0x001D5AF0: mov r8d, 0x628
0x001D5AF6: lea rcx, [rbp + 0x184]
0x001D5AFD: call 0x1403d3050
```

#### ref `0x001FE657`

```asm
0x001FE5EB: mov qword ptr [rip + 0x5e94ae], rax
0x001FE5F2: call qword ptr [rip + 0x5e9400]
0x001FE5F8: mov ecx, 0xedcf624e
0x001FE5FD: mov qword ptr [rip + 0x5e94a4], rax
0x001FE604: call qword ptr [rip + 0x5e93ee]
0x001FE60A: mov ecx, 0x34206d86
0x001FE60F: mov qword ptr [rip + 0x5e949a], rax
0x001FE616: call qword ptr [rip + 0x5e93dc]
0x001FE61C: mov ecx, 0x70916171
0x001FE621: mov qword ptr [rip + 0x5e9490], rax
0x001FE628: call qword ptr [rip + 0x5e93ca]
0x001FE62E: mov ecx, 0xad95f5ed
0x001FE633: mov qword ptr [rip + 0x5e9486], rax
0x001FE63A: call qword ptr [rip + 0x5e93b8]
0x001FE640: mov ecx, 0xfb85b01e
0x001FE645: mov qword ptr [rip + 0x5e947c], rax
0x001FE64C: call qword ptr [rip + 0x5e93a6]
0x001FE652: mov ecx, 0x35aed5e8
0x001FE657: mov qword ptr [rip + 0x5e9472], rax
0x001FE65E: call qword ptr [rip + 0x5e9394]
0x001FE664: mov ecx, 0x814b209f
0x001FE669: mov qword ptr [rip + 0x5e9468], rax
0x001FE670: call qword ptr [rip + 0x5e9382]
0x001FE676: mov ecx, 0xa58971a5
0x001FE67B: mov qword ptr [rip + 0x5e945e], rax
0x001FE682: call qword ptr [rip + 0x5e9370]
```

## call `0x001D624F` function slot `unknown`

```asm
0x001D622F: mov r8d, 0x5a8
0x001D6235: lea rcx, [rbp + 0x154]
0x001D623C: call 0x1403d3050
0x001D6241: lea rdx, [rbp + 0x150]
0x001D6248: mov rcx, qword ptr [rsi + 0xd0]
0x001D624F: call r15
0x001D6252: test eax, eax
0x001D6254: jne 0x1401d6e0c
0x001D625A: mov ecx, ebx
```

## call `0x001D62C5` function slot `0x007E7AE8`

```asm
0x001D62AD: inc ebx
0x001D62AF: cmp ebx, dword ptr [rbp + 0x158]
0x001D62B5: jb 0x1401d6295
0x001D62B7: lea rdx, [rbp + 0x150]
0x001D62BE: mov rcx, qword ptr [rsi + 0xd0]
0x001D62C5: call qword ptr [rip + 0x61181d]
0x001D62CB: mov ebx, eax
0x001D62CD: mov dword ptr [rsp + 0x20], eax
0x001D62D1: jmp 0x1401d67e4
```

### refs to global slot `0x007E7AE8`: `5`

#### ref `0x001D6216`

```asm
0x001D61B7: mov qword ptr [rsp + 0x40], 0xfffffffffffffffe
0x001D61C0: mov qword ptr [rsp + 0x850], rbx
0x001D61C8: mov rax, qword ptr [rip + 0x600721]
0x001D61CF: xor rax, rsp
0x001D61D2: mov qword ptr [rbp + 0x700], rax
0x001D61D9: movzx r12d, r8b
0x001D61DD: mov edi, edx
0x001D61DF: mov rsi, rcx
0x001D61E2: mov dword ptr [rsp + 0x28], edx
0x001D61E6: cmp qword ptr [rcx + 0xd0], 0
0x001D61EE: je 0x1401d6e0c
0x001D61F4: xor ebx, ebx
0x001D61F6: mov dword ptr [rsp + 0x20], ebx
0x001D61FA: cmp byte ptr [rcx + 0xd8], bl
0x001D6200: je 0x1401d62d6
0x001D6206: mov r15, qword ptr [rip + 0x6118d3]
0x001D620D: test r15, r15
0x001D6210: je 0x1401d6e0c
0x001D6216: cmp qword ptr [rip + 0x6118cb], rbx
0x001D621D: je 0x1401d6e0c
0x001D6223: mov dword ptr [rbp + 0x150], 0x105ac
0x001D622D: xor edx, edx
0x001D622F: mov r8d, 0x5a8
0x001D6235: lea rcx, [rbp + 0x154]
0x001D623C: call 0x1403d3050
0x001D6241: lea rdx, [rbp + 0x150]
```

#### ref `0x001D62C5`

```asm
0x001D6272: imul rdx, rax, 0x2c
0x001D6276: cmp dword ptr [rbp + rdx + 0x180], edi
0x001D627D: jne 0x1401d6295
0x001D627F: cmp dword ptr [rbp + rdx + 0x184], 1
0x001D6287: jne 0x1401d6295
0x001D6289: inc ecx
0x001D628B: cmp ecx, r8d
0x001D628E: jb 0x1401d6270
0x001D6290: jmp 0x1401d6e0c
0x001D6295: mov eax, ebx
0x001D6297: imul rcx, rax, 0x2c
0x001D629B: mov dword ptr [rbp + rcx + 0x184], 1
0x001D62A6: mov dword ptr [rbp + rcx + 0x180], edi
0x001D62AD: inc ebx
0x001D62AF: cmp ebx, dword ptr [rbp + 0x158]
0x001D62B5: jb 0x1401d6295
0x001D62B7: lea rdx, [rbp + 0x150]
0x001D62BE: mov rcx, qword ptr [rsi + 0xd0]
0x001D62C5: call qword ptr [rip + 0x61181d]
0x001D62CB: mov ebx, eax
0x001D62CD: mov dword ptr [rsp + 0x20], eax
0x001D62D1: jmp 0x1401d67e4
0x001D62D6: xor edx, edx
0x001D62D8: mov r8d, 0x98
0x001D62DE: lea rcx, [rbp + 0xb0]
0x001D62E5: call 0x1403d3050
```

#### ref `0x001D9A40`

```asm
0x001D99E2: mov qword ptr [rsp + 0x40], 0xfffffffffffffffe
0x001D99EB: mov qword ptr [rax + 0x10], rbx
0x001D99EF: mov qword ptr [rax + 0x18], rdi
0x001D99F3: mov qword ptr [rax + 0x20], r14
0x001D99F7: mov rax, qword ptr [rip + 0x5fcef2]
0x001D99FE: xor rax, rsp
0x001D9A01: mov qword ptr [rbp + 0x740], rax
0x001D9A08: mov rdi, rcx
0x001D9A0B: cmp qword ptr [rcx + 0xd0], 0
0x001D9A13: je 0x1401da77b
0x001D9A19: xor r14d, r14d
0x001D9A1C: mov ebx, r14d
0x001D9A1F: mov dword ptr [rsp + 0x20], ebx
0x001D9A23: cmp byte ptr [rcx + 0xd8], r14b
0x001D9A2A: je 0x1401d9ad7
0x001D9A30: mov rbx, qword ptr [rip + 0x60e0a9]
0x001D9A37: test rbx, rbx
0x001D9A3A: je 0x1401da262
0x001D9A40: cmp qword ptr [rip + 0x60e0a1], r14
0x001D9A47: je 0x1401da262
0x001D9A4D: mov dword ptr [rbp + 0x190], 0x105ac
0x001D9A57: xor edx, edx
0x001D9A59: mov r8d, 0x5a8
0x001D9A5F: lea rcx, [rbp + 0x194]
0x001D9A66: call 0x1403d3050
0x001D9A6B: lea rdx, [rbp + 0x190]
```

#### ref `0x001D9AC6`

```asm
0x001D9A72: mov rcx, qword ptr [rdi + 0xd0]
0x001D9A79: call rbx
0x001D9A7B: mov dword ptr [rsp + 0x20], eax
0x001D9A7F: test eax, eax
0x001D9A81: jne 0x1401da3bd
0x001D9A87: mov eax, r14d
0x001D9A8A: cmp dword ptr [rbp + 0x198], r14d
0x001D9A91: jbe 0x1401d9ab8
0x001D9A93: nop dword ptr [rax]
0x001D9A97: nop word ptr [rax + rax]
0x001D9AA0: mov ecx, eax
0x001D9AA2: imul rdx, rcx, 0x2c
0x001D9AA6: mov qword ptr [rbp + rdx + 0x1c0], r14
0x001D9AAE: inc eax
0x001D9AB0: cmp eax, dword ptr [rbp + 0x198]
0x001D9AB6: jb 0x1401d9aa0
0x001D9AB8: lea rdx, [rbp + 0x190]
0x001D9ABF: mov rcx, qword ptr [rdi + 0xd0]
0x001D9AC6: call qword ptr [rip + 0x60e01c]
0x001D9ACC: mov ebx, eax
0x001D9ACE: mov dword ptr [rsp + 0x20], eax
0x001D9AD2: jmp 0x1401da25a
0x001D9AD7: xor edx, edx
0x001D9AD9: mov r8d, 0x98
0x001D9ADF: lea rcx, [rbp + 0xf0]
0x001D9AE6: call 0x1403d3050
```

#### ref `0x001FE68D`

```asm
0x001FE621: mov qword ptr [rip + 0x5e9490], rax
0x001FE628: call qword ptr [rip + 0x5e93ca]
0x001FE62E: mov ecx, 0xad95f5ed
0x001FE633: mov qword ptr [rip + 0x5e9486], rax
0x001FE63A: call qword ptr [rip + 0x5e93b8]
0x001FE640: mov ecx, 0xfb85b01e
0x001FE645: mov qword ptr [rip + 0x5e947c], rax
0x001FE64C: call qword ptr [rip + 0x5e93a6]
0x001FE652: mov ecx, 0x35aed5e8
0x001FE657: mov qword ptr [rip + 0x5e9472], rax
0x001FE65E: call qword ptr [rip + 0x5e9394]
0x001FE664: mov ecx, 0x814b209f
0x001FE669: mov qword ptr [rip + 0x5e9468], rax
0x001FE670: call qword ptr [rip + 0x5e9382]
0x001FE676: mov ecx, 0xa58971a5
0x001FE67B: mov qword ptr [rip + 0x5e945e], rax
0x001FE682: call qword ptr [rip + 0x5e9370]
0x001FE688: mov ecx, 0x57f7caac
0x001FE68D: mov qword ptr [rip + 0x5e9454], rax
0x001FE694: call qword ptr [rip + 0x5e935e]
0x001FE69A: mov ecx, 0x42aea16a
0x001FE69F: mov qword ptr [rip + 0x5e944a], rax
0x001FE6A6: call qword ptr [rip + 0x5e934c]
0x001FE6AC: mov ecx, 0x2ddfb66e
0x001FE6B1: mov qword ptr [rip + 0x5e9440], rax
0x001FE6B8: call qword ptr [rip + 0x5e933a]
```

## call `0x001D62E5` function slot `unknown`

```asm
0x001D62AD: inc ebx
0x001D62AF: cmp ebx, dword ptr [rbp + 0x158]
0x001D62B5: jb 0x1401d6295
0x001D62B7: lea rdx, [rbp + 0x150]
0x001D62BE: mov rcx, qword ptr [rsi + 0xd0]
0x001D62C5: call qword ptr [rip + 0x61181d]
0x001D62CB: mov ebx, eax
0x001D62CD: mov dword ptr [rsp + 0x20], eax
0x001D62D1: jmp 0x1401d67e4
0x001D62D6: xor edx, edx
0x001D62D8: mov r8d, 0x98
0x001D62DE: lea rcx, [rbp + 0xb0]
0x001D62E5: call 0x1403d3050
0x001D62EA: mov dword ptr [rbp + 0xb0], 0x10098
0x001D62F4: lea r8, [rbp + 0xb0]
0x001D62FB: mov edx, 7
```

## call `0x001D6307` function slot `0x007E7A38`

```asm
0x001D62E5: call 0x1403d3050
0x001D62EA: mov dword ptr [rbp + 0xb0], 0x10098
0x001D62F4: lea r8, [rbp + 0xb0]
0x001D62FB: mov edx, 7
0x001D6300: mov rcx, qword ptr [rsi + 0xd0]
0x001D6307: call qword ptr [rip + 0x61172b]
0x001D630D: mov dword ptr [rsp + 0x30], eax
0x001D6311: test eax, eax
0x001D6313: je 0x1401d652d
```

### refs to global slot `0x007E7A38`: `4`

#### ref `0x001D6307`

```asm
0x001D62A6: mov dword ptr [rbp + rcx + 0x180], edi
0x001D62AD: inc ebx
0x001D62AF: cmp ebx, dword ptr [rbp + 0x158]
0x001D62B5: jb 0x1401d6295
0x001D62B7: lea rdx, [rbp + 0x150]
0x001D62BE: mov rcx, qword ptr [rsi + 0xd0]
0x001D62C5: call qword ptr [rip + 0x61181d]
0x001D62CB: mov ebx, eax
0x001D62CD: mov dword ptr [rsp + 0x20], eax
0x001D62D1: jmp 0x1401d67e4
0x001D62D6: xor edx, edx
0x001D62D8: mov r8d, 0x98
0x001D62DE: lea rcx, [rbp + 0xb0]
0x001D62E5: call 0x1403d3050
0x001D62EA: mov dword ptr [rbp + 0xb0], 0x10098
0x001D62F4: lea r8, [rbp + 0xb0]
0x001D62FB: mov edx, 7
0x001D6300: mov rcx, qword ptr [rsi + 0xd0]
0x001D6307: call qword ptr [rip + 0x61172b]
0x001D630D: mov dword ptr [rsp + 0x30], eax
0x001D6311: test eax, eax
0x001D6313: je 0x1401d652d
0x001D6319: mov dword ptr [rsp + 0x34], 0x45b
0x001D6321: mov dword ptr [rbp - 0x58], 0x7b
0x001D6328: mov dword ptr [rbp - 0x54], 0x32
0x001D632F: mov eax, dword ptr [rbp - 0x54]
```

#### ref `0x001D9B08`

```asm
0x001D9AA6: mov qword ptr [rbp + rdx + 0x1c0], r14
0x001D9AAE: inc eax
0x001D9AB0: cmp eax, dword ptr [rbp + 0x198]
0x001D9AB6: jb 0x1401d9aa0
0x001D9AB8: lea rdx, [rbp + 0x190]
0x001D9ABF: mov rcx, qword ptr [rdi + 0xd0]
0x001D9AC6: call qword ptr [rip + 0x60e01c]
0x001D9ACC: mov ebx, eax
0x001D9ACE: mov dword ptr [rsp + 0x20], eax
0x001D9AD2: jmp 0x1401da25a
0x001D9AD7: xor edx, edx
0x001D9AD9: mov r8d, 0x98
0x001D9ADF: lea rcx, [rbp + 0xf0]
0x001D9AE6: call 0x1403d3050
0x001D9AEB: mov dword ptr [rbp + 0xf0], 0x10098
0x001D9AF5: lea r8, [rbp + 0xf0]
0x001D9AFC: mov edx, 7
0x001D9B01: mov rcx, qword ptr [rdi + 0xd0]
0x001D9B08: call qword ptr [rip + 0x60df2a]
0x001D9B0E: mov dword ptr [rsp + 0x24], eax
0x001D9B12: test eax, eax
0x001D9B14: je 0x1401d9d85
0x001D9B1A: mov dword ptr [rsp + 0x30], 0x4f0
0x001D9B22: mov dword ptr [rbp - 0x80], 0x53
0x001D9B29: mov eax, dword ptr [rbp - 0x80]
0x001D9B2C: xor eax, 0x4e
```

#### ref `0x001DACE7`

```asm
0x001DAC80: mov byte ptr [rbp + 0x118], 0
0x001DAC87: mov esi, dword ptr [rsp + 0x30]
0x001DAC8B: jmp 0x1401db06d
0x001DAC90: cmp dword ptr [rbp + 0x264], 1
0x001DAC97: jb 0x1401db06d
0x001DAC9D: mov eax, dword ptr [rbp + 0x290]
0x001DACA3: test eax, eax
0x001DACA5: js 0x1401db06d
0x001DACAB: mov ecx, dword ptr [rbp + 0x294]
0x001DACB1: jmp 0x1401db053
0x001DACB6: xor edx, edx
0x001DACB8: mov r8d, 0x98
0x001DACBE: lea rcx, [rbp + 0x1c0]
0x001DACC5: call 0x1403d3050
0x001DACCA: mov dword ptr [rbp + 0x1c0], 0x10098
0x001DACD4: lea r8, [rbp + 0x1c0]
0x001DACDB: mov edx, 7
0x001DACE0: mov rcx, qword ptr [rdi + 0xd0]
0x001DACE7: call qword ptr [rip + 0x60cd4b]
0x001DACED: mov dword ptr [rsp + 0x68], eax
0x001DACF1: test eax, eax
0x001DACF3: je 0x1401db03a
0x001DACF9: mov dword ptr [rsp + 0x6c], 0x4aa
0x001DAD01: mov dword ptr [rbp - 8], 0x71
0x001DAD08: mov eax, dword ptr [rbp - 8]
0x001DAD0B: add al, 0x71
```

#### ref `0x001FE4C6`

```asm
0x001FE464: je 0x1401fe296
0x001FE46A: mov ecx, 0xd9930b07
0x001FE46F: call qword ptr [rip + 0x5e9583]
0x001FE475: mov qword ptr [rip + 0x5e95a4], rax
0x001FE47C: test rax, rax
0x001FE47F: je 0x1401fe296
0x001FE485: mov ecx, 0xceee8e9f
0x001FE48A: call qword ptr [rip + 0x5e9568]
0x001FE490: mov qword ptr [rip + 0x5e9591], rax
0x001FE497: test rax, rax
0x001FE49A: je 0x1401fe296
0x001FE4A0: mov ecx, 0x1be0b8e5
0x001FE4A5: call qword ptr [rip + 0x5e954d]
0x001FE4AB: mov qword ptr [rip + 0x5e957e], rax
0x001FE4B2: test rax, rax
0x001FE4B5: je 0x1401fe296
0x001FE4BB: mov ecx, 0xda141340
0x001FE4C0: call qword ptr [rip + 0x5e9532]
0x001FE4C6: mov qword ptr [rip + 0x5e956b], rax
0x001FE4CD: test rax, rax
0x001FE4D0: je 0x1401fe296
0x001FE4D6: mov ecx, 0x891fa0ae
0x001FE4DB: call qword ptr [rip + 0x5e9517]
0x001FE4E1: mov qword ptr [rip + 0x5e9558], rax
0x001FE4E8: test rax, rax
0x001FE4EB: je 0x1401fe296
```

## call `0x001D65A9` function slot `0x007E7A40`

```asm
0x001D6591: mov dword ptr [rbp + 0x1c], edi
0x001D6594: mov dword ptr [rbp + 0x20], 1
0x001D659B: lea r8, [rbp + 8]
0x001D659F: lea edx, [rax + 7]
0x001D65A2: mov rcx, qword ptr [rsi + 0xd0]
0x001D65A9: call qword ptr [rip + 0x611491]
0x001D65AF: mov dword ptr [rsp + 0x24], eax
0x001D65B3: test eax, eax
0x001D65B5: je 0x1401d67e4
```

### refs to global slot `0x007E7A40`: `3`

#### ref `0x001D65A9`

```asm
0x001D655C: inc edx
0x001D655E: cmp edx, r8d
0x001D6561: jb 0x1401d6540
0x001D6563: jmp 0x1401d6e0c
0x001D6568: xor eax, eax
0x001D656A: mov qword ptr [rbp + 8], rax
0x001D656E: mov qword ptr [rbp + 0x10], rax
0x001D6572: mov qword ptr [rbp + 0x18], rax
0x001D6576: mov dword ptr [rbp + 8], 0x1001c
0x001D657D: mov dword ptr [rbp + 0xc], edi
0x001D6580: mov dword ptr [rbp + 0x10], 1
0x001D6587: mov dword ptr [rbp + 0x14], edi
0x001D658A: mov dword ptr [rbp + 0x18], 1
0x001D6591: mov dword ptr [rbp + 0x1c], edi
0x001D6594: mov dword ptr [rbp + 0x20], 1
0x001D659B: lea r8, [rbp + 8]
0x001D659F: lea edx, [rax + 7]
0x001D65A2: mov rcx, qword ptr [rsi + 0xd0]
0x001D65A9: call qword ptr [rip + 0x611491]
0x001D65AF: mov dword ptr [rsp + 0x24], eax
0x001D65B3: test eax, eax
0x001D65B5: je 0x1401d67e4
0x001D65BB: mov dword ptr [rsp + 0x38], 0x46f
0x001D65C3: mov dword ptr [rbp - 0x28], 0x26
0x001D65CA: mov dword ptr [rbp - 0x24], 0x54
0x001D65D1: mov eax, dword ptr [rbp - 0x24]
```

#### ref `0x001D9DBA`

```asm
0x001D9D67: call 0x1403b20d4
0x001D9D6C: mov qword ptr [rbp + 0x68], 0xf
0x001D9D74: mov qword ptr [rbp + 0x60], r14
0x001D9D78: mov byte ptr [rbp + 0x50], 0
0x001D9D7C: mov ebx, dword ptr [rsp + 0x24]
0x001D9D80: jmp 0x1401d9ff1
0x001D9D85: mov dword ptr [rbp + 0x30], 0x1001c
0x001D9D8C: mov ecx, dword ptr [rbp + 0x100]
0x001D9D92: mov dword ptr [rbp + 0x34], ecx
0x001D9D95: mov eax, dword ptr [rbp + 0x114]
0x001D9D9B: mov dword ptr [rbp + 0x38], eax
0x001D9D9E: mov dword ptr [rbp + 0x3c], ecx
0x001D9DA1: mov dword ptr [rbp + 0x40], eax
0x001D9DA4: mov dword ptr [rbp + 0x44], ecx
0x001D9DA7: mov dword ptr [rbp + 0x48], eax
0x001D9DAA: lea r8, [rbp + 0x30]
0x001D9DAE: mov edx, 7
0x001D9DB3: mov rcx, qword ptr [rdi + 0xd0]
0x001D9DBA: call qword ptr [rip + 0x60dc80]
0x001D9DC0: mov dword ptr [rsp + 0x28], eax
0x001D9DC4: test eax, eax
0x001D9DC6: je 0x1401d9ff5
0x001D9DCC: mov dword ptr [rsp + 0x34], 0x4fa
0x001D9DD4: mov dword ptr [rbp - 0x50], 5
0x001D9DDB: mov eax, dword ptr [rbp - 0x50]
0x001D9DDE: xor eax, 0x4e
```

#### ref `0x001FE4E1`

```asm
0x001FE47F: je 0x1401fe296
0x001FE485: mov ecx, 0xceee8e9f
0x001FE48A: call qword ptr [rip + 0x5e9568]
0x001FE490: mov qword ptr [rip + 0x5e9591], rax
0x001FE497: test rax, rax
0x001FE49A: je 0x1401fe296
0x001FE4A0: mov ecx, 0x1be0b8e5
0x001FE4A5: call qword ptr [rip + 0x5e954d]
0x001FE4AB: mov qword ptr [rip + 0x5e957e], rax
0x001FE4B2: test rax, rax
0x001FE4B5: je 0x1401fe296
0x001FE4BB: mov ecx, 0xda141340
0x001FE4C0: call qword ptr [rip + 0x5e9532]
0x001FE4C6: mov qword ptr [rip + 0x5e956b], rax
0x001FE4CD: test rax, rax
0x001FE4D0: je 0x1401fe296
0x001FE4D6: mov ecx, 0x891fa0ae
0x001FE4DB: call qword ptr [rip + 0x5e9517]
0x001FE4E1: mov qword ptr [rip + 0x5e9558], rax
0x001FE4E8: test rax, rax
0x001FE4EB: je 0x1401fe296
0x001FE4F1: mov ecx, 0x8f6ed0fb
0x001FE4F6: call qword ptr [rip + 0x5e94fc]
0x001FE4FC: mov ecx, 0xd258bb5
0x001FE501: mov qword ptr [rip + 0x5e9540], rax
0x001FE508: call qword ptr [rip + 0x5e94ea]
```

## call `0x001D7769` function slot `unknown`

```asm
0x001D774B: mov qword ptr [rbp - 0x80], rcx
0x001D774F: mov qword ptr [rbp - 0x78], rcx
0x001D7753: mov qword ptr [rbp - 0x70], rcx
0x001D7757: mov dword ptr [rbp - 0x68], ecx
0x001D775A: mov rcx, qword ptr [rdi + 0xd0]
0x001D7761: mov dword ptr [rsp + 0x50], 0x1004c
0x001D7769: call r8
0x001D776C: test eax, eax
0x001D776E: jne 0x1401d777b
0x001D7770: mov eax, 0x10624dd3
```

## call `0x001D7794` function slot `unknown`

```asm
0x001D774B: mov qword ptr [rbp - 0x80], rcx
0x001D774F: mov qword ptr [rbp - 0x78], rcx
0x001D7753: mov qword ptr [rbp - 0x70], rcx
0x001D7757: mov dword ptr [rbp - 0x68], ecx
0x001D775A: mov rcx, qword ptr [rdi + 0xd0]
0x001D7761: mov dword ptr [rsp + 0x50], 0x1004c
0x001D7769: call r8
0x001D776C: test eax, eax
0x001D776E: jne 0x1401d777b
0x001D7770: mov eax, 0x10624dd3
0x001D7775: mul dword ptr [rsp + 0x78]
0x001D7779: jmp 0x1401d77c2
0x001D777B: mov rsi, qword ptr [rip + 0x6102fe]
0x001D7782: test rsi, rsi
0x001D7785: je 0x1401d77c9
0x001D7787: xor edx, edx
0x001D7789: lea rcx, [rsp + 0x50]
0x001D778E: mov r8d, 0x8c
0x001D7794: call 0x1403d3050
0x001D7799: mov rcx, qword ptr [rdi + 0xd0]
0x001D77A0: lea rdx, [rsp + 0x50]
0x001D77A5: mov dword ptr [rsp + 0x50], 0x1008c
```

## call `0x001D77AD` function slot `0x007E7A80`

```asm
0x001D7787: xor edx, edx
0x001D7789: lea rcx, [rsp + 0x50]
0x001D778E: mov r8d, 0x8c
0x001D7794: call 0x1403d3050
0x001D7799: mov rcx, qword ptr [rdi + 0xd0]
0x001D77A0: lea rdx, [rsp + 0x50]
0x001D77A5: mov dword ptr [rsp + 0x50], 0x1008c
0x001D77AD: call rsi
0x001D77AF: test eax, eax
0x001D77B1: jne 0x1401d77c9
0x001D77B3: mov ecx, dword ptr [rsp + 0x60]
```

### refs to global slot `0x007E7A80`: `2`

#### ref `0x001D777B`

```asm
0x001D772D: mov qword ptr [rsp + 0x50], rcx
0x001D7732: mov qword ptr [rsp + 0x58], rcx
0x001D7737: mov qword ptr [rsp + 0x60], rcx
0x001D773C: mov qword ptr [rsp + 0x68], rcx
0x001D7741: mov qword ptr [rsp + 0x70], rcx
0x001D7746: mov qword ptr [rsp + 0x78], rcx
0x001D774B: mov qword ptr [rbp - 0x80], rcx
0x001D774F: mov qword ptr [rbp - 0x78], rcx
0x001D7753: mov qword ptr [rbp - 0x70], rcx
0x001D7757: mov dword ptr [rbp - 0x68], ecx
0x001D775A: mov rcx, qword ptr [rdi + 0xd0]
0x001D7761: mov dword ptr [rsp + 0x50], 0x1004c
0x001D7769: call r8
0x001D776C: test eax, eax
0x001D776E: jne 0x1401d777b
0x001D7770: mov eax, 0x10624dd3
0x001D7775: mul dword ptr [rsp + 0x78]
0x001D7779: jmp 0x1401d77c2
0x001D777B: mov rsi, qword ptr [rip + 0x6102fe]
0x001D7782: test rsi, rsi
0x001D7785: je 0x1401d77c9
0x001D7787: xor edx, edx
0x001D7789: lea rcx, [rsp + 0x50]
0x001D778E: mov r8d, 0x8c
0x001D7794: call 0x1403d3050
0x001D7799: mov rcx, qword ptr [rdi + 0xd0]
```

#### ref `0x001FE5A3`

```asm
0x001FE53E: call qword ptr [rip + 0x5e94b4]
0x001FE544: mov qword ptr [rip + 0x5e9515], rax
0x001FE54B: test rax, rax
0x001FE54E: je 0x1401fe296
0x001FE554: mov ecx, 0xe3640a56
0x001FE559: call qword ptr [rip + 0x5e9499]
0x001FE55F: mov qword ptr [rip + 0x5e9502], rax
0x001FE566: test rax, rax
0x001FE569: je 0x1401fe296
0x001FE56F: mov ecx, 0xdcb616c3
0x001FE574: call qword ptr [rip + 0x5e947e]
0x001FE57A: mov ecx, 0x1bd69f49
0x001FE57F: mov qword ptr [rip + 0x5e94ea], rax
0x001FE586: call qword ptr [rip + 0x5e946c]
0x001FE58C: mov ecx, 0xc16c7e2c
0x001FE591: mov qword ptr [rip + 0x5e94e0], rax
0x001FE598: call qword ptr [rip + 0x5e945a]
0x001FE59E: mov ecx, 0x465f9bcf
0x001FE5A3: mov qword ptr [rip + 0x5e94d6], rax
0x001FE5AA: call qword ptr [rip + 0x5e9448]
0x001FE5B0: mov ecx, 0x927da4f6
0x001FE5B5: mov qword ptr [rip + 0x5e94cc], rax
0x001FE5BC: call qword ptr [rip + 0x5e9436]
0x001FE5C2: mov ecx, 0x6ff81213
0x001FE5C7: mov qword ptr [rip + 0x5e94c2], rax
0x001FE5CE: call qword ptr [rip + 0x5e9424]
```

## call `0x001D77E6` function slot `0x007E7A90`

```asm
0x001D77C5: mov word ptr [rbx + 0xe], dx
0x001D77C9: mov rax, qword ptr [rip + 0x6102c0]
0x001D77D0: test rax, rax
0x001D77D3: je 0x1401d77f6
0x001D77D5: mov rcx, qword ptr [rdi + 0xd0]
0x001D77DC: lea rdx, [rsp + 0x30]
0x001D77E1: mov dword ptr [rsp + 0x30], r12d
0x001D77E6: call rax
0x001D77E8: test eax, eax
0x001D77EA: jne 0x1401d77f6
0x001D77EC: movzx eax, byte ptr [rsp + 0x30]
```

### refs to global slot `0x007E7A90`: `3`

#### ref `0x001D77C9`

```asm
0x001D7785: je 0x1401d77c9
0x001D7787: xor edx, edx
0x001D7789: lea rcx, [rsp + 0x50]
0x001D778E: mov r8d, 0x8c
0x001D7794: call 0x1403d3050
0x001D7799: mov rcx, qword ptr [rdi + 0xd0]
0x001D77A0: lea rdx, [rsp + 0x50]
0x001D77A5: mov dword ptr [rsp + 0x50], 0x1008c
0x001D77AD: call rsi
0x001D77AF: test eax, eax
0x001D77B1: jne 0x1401d77c9
0x001D77B3: mov ecx, dword ptr [rsp + 0x60]
0x001D77B7: test ecx, ecx
0x001D77B9: je 0x1401d77c9
0x001D77BB: mov eax, 0x10624dd3
0x001D77C0: mul ecx
0x001D77C2: shr edx, 6
0x001D77C5: mov word ptr [rbx + 0xe], dx
0x001D77C9: mov rax, qword ptr [rip + 0x6102c0]
0x001D77D0: test rax, rax
0x001D77D3: je 0x1401d77f6
0x001D77D5: mov rcx, qword ptr [rdi + 0xd0]
0x001D77DC: lea rdx, [rsp + 0x30]
0x001D77E1: mov dword ptr [rsp + 0x30], r12d
0x001D77E6: call rax
0x001D77E8: test eax, eax
```

#### ref `0x001DE8EE`

```asm
0x001DE8AB: int3
0x001DE8AC: int3
0x001DE8AD: int3
0x001DE8AE: int3
0x001DE8AF: int3
0x001DE8B0: mov rax, rsp
0x001DE8B3: push rbp
0x001DE8B4: lea rbp, [rax - 0x138]
0x001DE8BB: sub rsp, 0x230
0x001DE8C2: mov qword ptr [rsp + 0x28], 0xfffffffffffffffe
0x001DE8CB: mov qword ptr [rax + 0x10], rbx
0x001DE8CF: mov qword ptr [rax + 0x18], rsi
0x001DE8D3: mov qword ptr [rax + 0x20], rdi
0x001DE8D7: mov rax, qword ptr [rip + 0x5f8012]
0x001DE8DE: xor rax, rsp
0x001DE8E1: mov qword ptr [rbp + 0x120], rax
0x001DE8E8: movzx esi, dl
0x001DE8EB: mov rbx, rcx
0x001DE8EE: mov rax, qword ptr [rip + 0x60919b]
0x001DE8F5: test rax, rax
0x001DE8F8: je 0x1401de91e
0x001DE8FA: mov dword ptr [rsp + 0x20], 0x10
0x001DE902: lea rdx, [rsp + 0x20]
0x001DE907: mov rcx, qword ptr [rcx + 0xd0]
0x001DE90E: call rax
0x001DE910: test eax, eax
```

#### ref `0x001FE5C7`

```asm
0x001FE55F: mov qword ptr [rip + 0x5e9502], rax
0x001FE566: test rax, rax
0x001FE569: je 0x1401fe296
0x001FE56F: mov ecx, 0xdcb616c3
0x001FE574: call qword ptr [rip + 0x5e947e]
0x001FE57A: mov ecx, 0x1bd69f49
0x001FE57F: mov qword ptr [rip + 0x5e94ea], rax
0x001FE586: call qword ptr [rip + 0x5e946c]
0x001FE58C: mov ecx, 0xc16c7e2c
0x001FE591: mov qword ptr [rip + 0x5e94e0], rax
0x001FE598: call qword ptr [rip + 0x5e945a]
0x001FE59E: mov ecx, 0x465f9bcf
0x001FE5A3: mov qword ptr [rip + 0x5e94d6], rax
0x001FE5AA: call qword ptr [rip + 0x5e9448]
0x001FE5B0: mov ecx, 0x927da4f6
0x001FE5B5: mov qword ptr [rip + 0x5e94cc], rax
0x001FE5BC: call qword ptr [rip + 0x5e9436]
0x001FE5C2: mov ecx, 0x6ff81213
0x001FE5C7: mov qword ptr [rip + 0x5e94c2], rax
0x001FE5CE: call qword ptr [rip + 0x5e9424]
0x001FE5D4: mov ecx, 0xf4dae6b
0x001FE5D9: mov qword ptr [rip + 0x5e94b8], rax
0x001FE5E0: call qword ptr [rip + 0x5e9412]
0x001FE5E6: mov ecx, 0x843c0256
0x001FE5EB: mov qword ptr [rip + 0x5e94ae], rax
0x001FE5F2: call qword ptr [rip + 0x5e9400]
```

## call `0x001D98A8` function slot `unknown`

```asm
0x001D987A: xor edx, edx
0x001D987C: lea rcx, [rsp + 0x20]
0x001D9881: mov r8d, 0xa8
0x001D9887: call 0x1403d3050
0x001D988C: mov rcx, qword ptr [rdi + 0xd0]
0x001D9893: lea rdx, [rsp + 0x20]
0x001D9898: mov dword ptr [rsp + 0x20], 0x200a8
0x001D98A0: mov dword ptr [rsp + 0x24], 0x3ff
0x001D98A8: call rsi
0x001D98AA: test eax, eax
0x001D98AC: je 0x1401d98d8
0x001D98AE: mov rcx, qword ptr [rdi + 0xd0]
```

## call `0x001D98C2` function slot `0x007E7B10`

```asm
0x001D98A0: mov dword ptr [rsp + 0x24], 0x3ff
0x001D98A8: call rsi
0x001D98AA: test eax, eax
0x001D98AC: je 0x1401d98d8
0x001D98AE: mov rcx, qword ptr [rdi + 0xd0]
0x001D98B5: lea rdx, [rsp + 0x20]
0x001D98BA: mov dword ptr [rsp + 0x24], 3
0x001D98C2: call qword ptr [rip + 0x60e248]
0x001D98C8: test eax, eax
0x001D98CA: je 0x1401d98d8
0x001D98CC: mov dword ptr [rdi + 0x3a4], 0
```

### refs to global slot `0x007E7B10`: `4`

#### ref `0x001D9864`

```asm
0x001D9815: mov qword ptr [rsp + 0x20], rbp
0x001D981A: push rsi
0x001D981B: push rdi
0x001D981C: push r15
0x001D981E: sub rsp, 0xe0
0x001D9825: mov rax, qword ptr [rip + 0x5fd0c4]
0x001D982C: xor rax, rsp
0x001D982F: mov qword ptr [rsp + 0xd0], rax
0x001D9837: or r15d, 0xffffffff
0x001D983B: mov ebp, r8d
0x001D983E: mov word ptr [rdx], r15w
0x001D9842: mov rbx, rdx
0x001D9845: mov word ptr [rdx + 2], r15w
0x001D984A: mov rdi, rcx
0x001D984D: mov word ptr [rdx + 4], r15w
0x001D9852: mov word ptr [rdx + 6], r15w
0x001D9857: cmp dword ptr [rcx + 0x3a4], -1
0x001D985E: jne 0x1401d98ee
0x001D9864: mov rsi, qword ptr [rip + 0x60e2a5]
0x001D986B: test rsi, rsi
0x001D986E: je 0x1401d98e4
0x001D9870: cmp qword ptr [rcx + 0xd0], 0
0x001D9878: je 0x1401d98e4
0x001D987A: xor edx, edx
0x001D987C: lea rcx, [rsp + 0x20]
0x001D9881: mov r8d, 0xa8
```

#### ref `0x001D98C2`

```asm
0x001D986B: test rsi, rsi
0x001D986E: je 0x1401d98e4
0x001D9870: cmp qword ptr [rcx + 0xd0], 0
0x001D9878: je 0x1401d98e4
0x001D987A: xor edx, edx
0x001D987C: lea rcx, [rsp + 0x20]
0x001D9881: mov r8d, 0xa8
0x001D9887: call 0x1403d3050
0x001D988C: mov rcx, qword ptr [rdi + 0xd0]
0x001D9893: lea rdx, [rsp + 0x20]
0x001D9898: mov dword ptr [rsp + 0x20], 0x200a8
0x001D98A0: mov dword ptr [rsp + 0x24], 0x3ff
0x001D98A8: call rsi
0x001D98AA: test eax, eax
0x001D98AC: je 0x1401d98d8
0x001D98AE: mov rcx, qword ptr [rdi + 0xd0]
0x001D98B5: lea rdx, [rsp + 0x20]
0x001D98BA: mov dword ptr [rsp + 0x24], 3
0x001D98C2: call qword ptr [rip + 0x60e248]
0x001D98C8: test eax, eax
0x001D98CA: je 0x1401d98d8
0x001D98CC: mov dword ptr [rdi + 0x3a4], 0
0x001D98D6: jmp 0x1401d98ee
0x001D98D8: mov eax, dword ptr [rsp + 0x24]
0x001D98DC: mov dword ptr [rdi + 0x3a4], eax
0x001D98E2: jmp 0x1401d98ee
```

#### ref `0x001D9922`

```asm
0x001D98CA: je 0x1401d98d8
0x001D98CC: mov dword ptr [rdi + 0x3a4], 0
0x001D98D6: jmp 0x1401d98ee
0x001D98D8: mov eax, dword ptr [rsp + 0x24]
0x001D98DC: mov dword ptr [rdi + 0x3a4], eax
0x001D98E2: jmp 0x1401d98ee
0x001D98E4: mov dword ptr [rcx + 0x3a4], 0
0x001D98EE: mov esi, dword ptr [rdi + 0x3a4]
0x001D98F4: test esi, esi
0x001D98F6: je 0x1401d9961
0x001D98F8: xor edx, edx
0x001D98FA: lea rcx, [rsp + 0x20]
0x001D98FF: mov r8d, 0xa8
0x001D9905: call 0x1403d3050
0x001D990A: mov rcx, qword ptr [rdi + 0xd0]
0x001D9911: lea rdx, [rsp + 0x20]
0x001D9916: mov dword ptr [rsp + 0x20], 0x200a8
0x001D991E: mov dword ptr [rsp + 0x24], esi
0x001D9922: call qword ptr [rip + 0x60e1e8]
0x001D9928: test eax, eax
0x001D992A: jne 0x1401d9961
0x001D992C: mov eax, dword ptr [rsp + 0x48]
0x001D9930: test eax, eax
0x001D9932: je 0x1401d993d
0x001D9934: sub eax, -0x80
0x001D9937: shr eax, 8
```

#### ref `0x001FE6E2`

```asm
0x001FE676: mov ecx, 0xa58971a5
0x001FE67B: mov qword ptr [rip + 0x5e945e], rax
0x001FE682: call qword ptr [rip + 0x5e9370]
0x001FE688: mov ecx, 0x57f7caac
0x001FE68D: mov qword ptr [rip + 0x5e9454], rax
0x001FE694: call qword ptr [rip + 0x5e935e]
0x001FE69A: mov ecx, 0x42aea16a
0x001FE69F: mov qword ptr [rip + 0x5e944a], rax
0x001FE6A6: call qword ptr [rip + 0x5e934c]
0x001FE6AC: mov ecx, 0x2ddfb66e
0x001FE6B1: mov qword ptr [rip + 0x5e9440], rax
0x001FE6B8: call qword ptr [rip + 0x5e933a]
0x001FE6BE: mov ecx, 0x2eb3c140
0x001FE6C3: mov qword ptr [rip + 0x5e9436], rax
0x001FE6CA: call qword ptr [rip + 0x5e9328]
0x001FE6D0: mov ecx, 0x65fe3aad
0x001FE6D5: mov qword ptr [rip + 0x5e942c], rax
0x001FE6DC: call qword ptr [rip + 0x5e9316]
0x001FE6E2: mov qword ptr [rip + 0x5e9427], rax
0x001FE6E9: mov al, 1
0x001FE6EB: mov rcx, qword ptr [rbp + 0x4f]
0x001FE6EF: xor rcx, rsp
0x001FE6F2: call 0x1403b24c0
0x001FE6F7: add rsp, 0xa0
0x001FE6FE: pop rbp
0x001FE6FF: ret
```

## call `0x001D9905` function slot `unknown`

```asm
0x001D98A0: mov dword ptr [rsp + 0x24], 0x3ff
0x001D98A8: call rsi
0x001D98AA: test eax, eax
0x001D98AC: je 0x1401d98d8
0x001D98AE: mov rcx, qword ptr [rdi + 0xd0]
0x001D98B5: lea rdx, [rsp + 0x20]
0x001D98BA: mov dword ptr [rsp + 0x24], 3
0x001D98C2: call qword ptr [rip + 0x60e248]
0x001D98C8: test eax, eax
0x001D98CA: je 0x1401d98d8
0x001D98CC: mov dword ptr [rdi + 0x3a4], 0
0x001D98D6: jmp 0x1401d98ee
0x001D98D8: mov eax, dword ptr [rsp + 0x24]
0x001D98DC: mov dword ptr [rdi + 0x3a4], eax
0x001D98E2: jmp 0x1401d98ee
0x001D98E4: mov dword ptr [rcx + 0x3a4], 0
0x001D98EE: mov esi, dword ptr [rdi + 0x3a4]
0x001D98F4: test esi, esi
0x001D98F6: je 0x1401d9961
0x001D98F8: xor edx, edx
0x001D98FA: lea rcx, [rsp + 0x20]
0x001D98FF: mov r8d, 0xa8
0x001D9905: call 0x1403d3050
0x001D990A: mov rcx, qword ptr [rdi + 0xd0]
0x001D9911: lea rdx, [rsp + 0x20]
0x001D9916: mov dword ptr [rsp + 0x20], 0x200a8
```

## call `0x001D9922` function slot `0x007E7B10`

```asm
0x001D98F8: xor edx, edx
0x001D98FA: lea rcx, [rsp + 0x20]
0x001D98FF: mov r8d, 0xa8
0x001D9905: call 0x1403d3050
0x001D990A: mov rcx, qword ptr [rdi + 0xd0]
0x001D9911: lea rdx, [rsp + 0x20]
0x001D9916: mov dword ptr [rsp + 0x20], 0x200a8
0x001D991E: mov dword ptr [rsp + 0x24], esi
0x001D9922: call qword ptr [rip + 0x60e1e8]
0x001D9928: test eax, eax
0x001D992A: jne 0x1401d9961
0x001D992C: mov eax, dword ptr [rsp + 0x48]
```

### refs to global slot `0x007E7B10`: `4`

#### ref `0x001D9864`

```asm
0x001D9815: mov qword ptr [rsp + 0x20], rbp
0x001D981A: push rsi
0x001D981B: push rdi
0x001D981C: push r15
0x001D981E: sub rsp, 0xe0
0x001D9825: mov rax, qword ptr [rip + 0x5fd0c4]
0x001D982C: xor rax, rsp
0x001D982F: mov qword ptr [rsp + 0xd0], rax
0x001D9837: or r15d, 0xffffffff
0x001D983B: mov ebp, r8d
0x001D983E: mov word ptr [rdx], r15w
0x001D9842: mov rbx, rdx
0x001D9845: mov word ptr [rdx + 2], r15w
0x001D984A: mov rdi, rcx
0x001D984D: mov word ptr [rdx + 4], r15w
0x001D9852: mov word ptr [rdx + 6], r15w
0x001D9857: cmp dword ptr [rcx + 0x3a4], -1
0x001D985E: jne 0x1401d98ee
0x001D9864: mov rsi, qword ptr [rip + 0x60e2a5]
0x001D986B: test rsi, rsi
0x001D986E: je 0x1401d98e4
0x001D9870: cmp qword ptr [rcx + 0xd0], 0
0x001D9878: je 0x1401d98e4
0x001D987A: xor edx, edx
0x001D987C: lea rcx, [rsp + 0x20]
0x001D9881: mov r8d, 0xa8
```

#### ref `0x001D98C2`

```asm
0x001D986B: test rsi, rsi
0x001D986E: je 0x1401d98e4
0x001D9870: cmp qword ptr [rcx + 0xd0], 0
0x001D9878: je 0x1401d98e4
0x001D987A: xor edx, edx
0x001D987C: lea rcx, [rsp + 0x20]
0x001D9881: mov r8d, 0xa8
0x001D9887: call 0x1403d3050
0x001D988C: mov rcx, qword ptr [rdi + 0xd0]
0x001D9893: lea rdx, [rsp + 0x20]
0x001D9898: mov dword ptr [rsp + 0x20], 0x200a8
0x001D98A0: mov dword ptr [rsp + 0x24], 0x3ff
0x001D98A8: call rsi
0x001D98AA: test eax, eax
0x001D98AC: je 0x1401d98d8
0x001D98AE: mov rcx, qword ptr [rdi + 0xd0]
0x001D98B5: lea rdx, [rsp + 0x20]
0x001D98BA: mov dword ptr [rsp + 0x24], 3
0x001D98C2: call qword ptr [rip + 0x60e248]
0x001D98C8: test eax, eax
0x001D98CA: je 0x1401d98d8
0x001D98CC: mov dword ptr [rdi + 0x3a4], 0
0x001D98D6: jmp 0x1401d98ee
0x001D98D8: mov eax, dword ptr [rsp + 0x24]
0x001D98DC: mov dword ptr [rdi + 0x3a4], eax
0x001D98E2: jmp 0x1401d98ee
```

#### ref `0x001D9922`

```asm
0x001D98CA: je 0x1401d98d8
0x001D98CC: mov dword ptr [rdi + 0x3a4], 0
0x001D98D6: jmp 0x1401d98ee
0x001D98D8: mov eax, dword ptr [rsp + 0x24]
0x001D98DC: mov dword ptr [rdi + 0x3a4], eax
0x001D98E2: jmp 0x1401d98ee
0x001D98E4: mov dword ptr [rcx + 0x3a4], 0
0x001D98EE: mov esi, dword ptr [rdi + 0x3a4]
0x001D98F4: test esi, esi
0x001D98F6: je 0x1401d9961
0x001D98F8: xor edx, edx
0x001D98FA: lea rcx, [rsp + 0x20]
0x001D98FF: mov r8d, 0xa8
0x001D9905: call 0x1403d3050
0x001D990A: mov rcx, qword ptr [rdi + 0xd0]
0x001D9911: lea rdx, [rsp + 0x20]
0x001D9916: mov dword ptr [rsp + 0x20], 0x200a8
0x001D991E: mov dword ptr [rsp + 0x24], esi
0x001D9922: call qword ptr [rip + 0x60e1e8]
0x001D9928: test eax, eax
0x001D992A: jne 0x1401d9961
0x001D992C: mov eax, dword ptr [rsp + 0x48]
0x001D9930: test eax, eax
0x001D9932: je 0x1401d993d
0x001D9934: sub eax, -0x80
0x001D9937: shr eax, 8
```

#### ref `0x001FE6E2`

```asm
0x001FE676: mov ecx, 0xa58971a5
0x001FE67B: mov qword ptr [rip + 0x5e945e], rax
0x001FE682: call qword ptr [rip + 0x5e9370]
0x001FE688: mov ecx, 0x57f7caac
0x001FE68D: mov qword ptr [rip + 0x5e9454], rax
0x001FE694: call qword ptr [rip + 0x5e935e]
0x001FE69A: mov ecx, 0x42aea16a
0x001FE69F: mov qword ptr [rip + 0x5e944a], rax
0x001FE6A6: call qword ptr [rip + 0x5e934c]
0x001FE6AC: mov ecx, 0x2ddfb66e
0x001FE6B1: mov qword ptr [rip + 0x5e9440], rax
0x001FE6B8: call qword ptr [rip + 0x5e933a]
0x001FE6BE: mov ecx, 0x2eb3c140
0x001FE6C3: mov qword ptr [rip + 0x5e9436], rax
0x001FE6CA: call qword ptr [rip + 0x5e9328]
0x001FE6D0: mov ecx, 0x65fe3aad
0x001FE6D5: mov qword ptr [rip + 0x5e942c], rax
0x001FE6DC: call qword ptr [rip + 0x5e9316]
0x001FE6E2: mov qword ptr [rip + 0x5e9427], rax
0x001FE6E9: mov al, 1
0x001FE6EB: mov rcx, qword ptr [rbp + 0x4f]
0x001FE6EF: xor rcx, rsp
0x001FE6F2: call 0x1403b24c0
0x001FE6F7: add rsp, 0xa0
0x001FE6FE: pop rbp
0x001FE6FF: ret
```

## call `0x001D99AA` function slot `unknown`

```asm
0x001D9992: jge 0x1401d999f
0x001D9994: test bpl, 2
0x001D9998: je 0x1401d999f
0x001D999A: mov word ptr [rbx + 2], r15w
0x001D999F: mov rcx, qword ptr [rsp + 0xd0]
0x001D99A7: xor rcx, rsp
0x001D99AA: call 0x1403b24c0
0x001D99AF: lea r11, [rsp + 0xe0]
0x001D99B7: mov rbx, qword ptr [r11 + 0x30]
0x001D99BB: mov rbp, qword ptr [r11 + 0x38]
```

## call `0x001D9A79` function slot `unknown`

```asm
0x001D9A59: mov r8d, 0x5a8
0x001D9A5F: lea rcx, [rbp + 0x194]
0x001D9A66: call 0x1403d3050
0x001D9A6B: lea rdx, [rbp + 0x190]
0x001D9A72: mov rcx, qword ptr [rdi + 0xd0]
0x001D9A79: call rbx
0x001D9A7B: mov dword ptr [rsp + 0x20], eax
0x001D9A7F: test eax, eax
0x001D9A81: jne 0x1401da3bd
```

## call `0x001D9AC6` function slot `0x007E7AE8`

```asm
0x001D9AAE: inc eax
0x001D9AB0: cmp eax, dword ptr [rbp + 0x198]
0x001D9AB6: jb 0x1401d9aa0
0x001D9AB8: lea rdx, [rbp + 0x190]
0x001D9ABF: mov rcx, qword ptr [rdi + 0xd0]
0x001D9AC6: call qword ptr [rip + 0x60e01c]
0x001D9ACC: mov ebx, eax
0x001D9ACE: mov dword ptr [rsp + 0x20], eax
0x001D9AD2: jmp 0x1401da25a
```

### refs to global slot `0x007E7AE8`: `5`

#### ref `0x001D6216`

```asm
0x001D61B7: mov qword ptr [rsp + 0x40], 0xfffffffffffffffe
0x001D61C0: mov qword ptr [rsp + 0x850], rbx
0x001D61C8: mov rax, qword ptr [rip + 0x600721]
0x001D61CF: xor rax, rsp
0x001D61D2: mov qword ptr [rbp + 0x700], rax
0x001D61D9: movzx r12d, r8b
0x001D61DD: mov edi, edx
0x001D61DF: mov rsi, rcx
0x001D61E2: mov dword ptr [rsp + 0x28], edx
0x001D61E6: cmp qword ptr [rcx + 0xd0], 0
0x001D61EE: je 0x1401d6e0c
0x001D61F4: xor ebx, ebx
0x001D61F6: mov dword ptr [rsp + 0x20], ebx
0x001D61FA: cmp byte ptr [rcx + 0xd8], bl
0x001D6200: je 0x1401d62d6
0x001D6206: mov r15, qword ptr [rip + 0x6118d3]
0x001D620D: test r15, r15
0x001D6210: je 0x1401d6e0c
0x001D6216: cmp qword ptr [rip + 0x6118cb], rbx
0x001D621D: je 0x1401d6e0c
0x001D6223: mov dword ptr [rbp + 0x150], 0x105ac
0x001D622D: xor edx, edx
0x001D622F: mov r8d, 0x5a8
0x001D6235: lea rcx, [rbp + 0x154]
0x001D623C: call 0x1403d3050
0x001D6241: lea rdx, [rbp + 0x150]
```

#### ref `0x001D62C5`

```asm
0x001D6272: imul rdx, rax, 0x2c
0x001D6276: cmp dword ptr [rbp + rdx + 0x180], edi
0x001D627D: jne 0x1401d6295
0x001D627F: cmp dword ptr [rbp + rdx + 0x184], 1
0x001D6287: jne 0x1401d6295
0x001D6289: inc ecx
0x001D628B: cmp ecx, r8d
0x001D628E: jb 0x1401d6270
0x001D6290: jmp 0x1401d6e0c
0x001D6295: mov eax, ebx
0x001D6297: imul rcx, rax, 0x2c
0x001D629B: mov dword ptr [rbp + rcx + 0x184], 1
0x001D62A6: mov dword ptr [rbp + rcx + 0x180], edi
0x001D62AD: inc ebx
0x001D62AF: cmp ebx, dword ptr [rbp + 0x158]
0x001D62B5: jb 0x1401d6295
0x001D62B7: lea rdx, [rbp + 0x150]
0x001D62BE: mov rcx, qword ptr [rsi + 0xd0]
0x001D62C5: call qword ptr [rip + 0x61181d]
0x001D62CB: mov ebx, eax
0x001D62CD: mov dword ptr [rsp + 0x20], eax
0x001D62D1: jmp 0x1401d67e4
0x001D62D6: xor edx, edx
0x001D62D8: mov r8d, 0x98
0x001D62DE: lea rcx, [rbp + 0xb0]
0x001D62E5: call 0x1403d3050
```

#### ref `0x001D9A40`

```asm
0x001D99E2: mov qword ptr [rsp + 0x40], 0xfffffffffffffffe
0x001D99EB: mov qword ptr [rax + 0x10], rbx
0x001D99EF: mov qword ptr [rax + 0x18], rdi
0x001D99F3: mov qword ptr [rax + 0x20], r14
0x001D99F7: mov rax, qword ptr [rip + 0x5fcef2]
0x001D99FE: xor rax, rsp
0x001D9A01: mov qword ptr [rbp + 0x740], rax
0x001D9A08: mov rdi, rcx
0x001D9A0B: cmp qword ptr [rcx + 0xd0], 0
0x001D9A13: je 0x1401da77b
0x001D9A19: xor r14d, r14d
0x001D9A1C: mov ebx, r14d
0x001D9A1F: mov dword ptr [rsp + 0x20], ebx
0x001D9A23: cmp byte ptr [rcx + 0xd8], r14b
0x001D9A2A: je 0x1401d9ad7
0x001D9A30: mov rbx, qword ptr [rip + 0x60e0a9]
0x001D9A37: test rbx, rbx
0x001D9A3A: je 0x1401da262
0x001D9A40: cmp qword ptr [rip + 0x60e0a1], r14
0x001D9A47: je 0x1401da262
0x001D9A4D: mov dword ptr [rbp + 0x190], 0x105ac
0x001D9A57: xor edx, edx
0x001D9A59: mov r8d, 0x5a8
0x001D9A5F: lea rcx, [rbp + 0x194]
0x001D9A66: call 0x1403d3050
0x001D9A6B: lea rdx, [rbp + 0x190]
```

#### ref `0x001D9AC6`

```asm
0x001D9A72: mov rcx, qword ptr [rdi + 0xd0]
0x001D9A79: call rbx
0x001D9A7B: mov dword ptr [rsp + 0x20], eax
0x001D9A7F: test eax, eax
0x001D9A81: jne 0x1401da3bd
0x001D9A87: mov eax, r14d
0x001D9A8A: cmp dword ptr [rbp + 0x198], r14d
0x001D9A91: jbe 0x1401d9ab8
0x001D9A93: nop dword ptr [rax]
0x001D9A97: nop word ptr [rax + rax]
0x001D9AA0: mov ecx, eax
0x001D9AA2: imul rdx, rcx, 0x2c
0x001D9AA6: mov qword ptr [rbp + rdx + 0x1c0], r14
0x001D9AAE: inc eax
0x001D9AB0: cmp eax, dword ptr [rbp + 0x198]
0x001D9AB6: jb 0x1401d9aa0
0x001D9AB8: lea rdx, [rbp + 0x190]
0x001D9ABF: mov rcx, qword ptr [rdi + 0xd0]
0x001D9AC6: call qword ptr [rip + 0x60e01c]
0x001D9ACC: mov ebx, eax
0x001D9ACE: mov dword ptr [rsp + 0x20], eax
0x001D9AD2: jmp 0x1401da25a
0x001D9AD7: xor edx, edx
0x001D9AD9: mov r8d, 0x98
0x001D9ADF: lea rcx, [rbp + 0xf0]
0x001D9AE6: call 0x1403d3050
```

#### ref `0x001FE68D`

```asm
0x001FE621: mov qword ptr [rip + 0x5e9490], rax
0x001FE628: call qword ptr [rip + 0x5e93ca]
0x001FE62E: mov ecx, 0xad95f5ed
0x001FE633: mov qword ptr [rip + 0x5e9486], rax
0x001FE63A: call qword ptr [rip + 0x5e93b8]
0x001FE640: mov ecx, 0xfb85b01e
0x001FE645: mov qword ptr [rip + 0x5e947c], rax
0x001FE64C: call qword ptr [rip + 0x5e93a6]
0x001FE652: mov ecx, 0x35aed5e8
0x001FE657: mov qword ptr [rip + 0x5e9472], rax
0x001FE65E: call qword ptr [rip + 0x5e9394]
0x001FE664: mov ecx, 0x814b209f
0x001FE669: mov qword ptr [rip + 0x5e9468], rax
0x001FE670: call qword ptr [rip + 0x5e9382]
0x001FE676: mov ecx, 0xa58971a5
0x001FE67B: mov qword ptr [rip + 0x5e945e], rax
0x001FE682: call qword ptr [rip + 0x5e9370]
0x001FE688: mov ecx, 0x57f7caac
0x001FE68D: mov qword ptr [rip + 0x5e9454], rax
0x001FE694: call qword ptr [rip + 0x5e935e]
0x001FE69A: mov ecx, 0x42aea16a
0x001FE69F: mov qword ptr [rip + 0x5e944a], rax
0x001FE6A6: call qword ptr [rip + 0x5e934c]
0x001FE6AC: mov ecx, 0x2ddfb66e
0x001FE6B1: mov qword ptr [rip + 0x5e9440], rax
0x001FE6B8: call qword ptr [rip + 0x5e933a]
```

## call `0x001D9AE6` function slot `unknown`

```asm
0x001D9AAE: inc eax
0x001D9AB0: cmp eax, dword ptr [rbp + 0x198]
0x001D9AB6: jb 0x1401d9aa0
0x001D9AB8: lea rdx, [rbp + 0x190]
0x001D9ABF: mov rcx, qword ptr [rdi + 0xd0]
0x001D9AC6: call qword ptr [rip + 0x60e01c]
0x001D9ACC: mov ebx, eax
0x001D9ACE: mov dword ptr [rsp + 0x20], eax
0x001D9AD2: jmp 0x1401da25a
0x001D9AD7: xor edx, edx
0x001D9AD9: mov r8d, 0x98
0x001D9ADF: lea rcx, [rbp + 0xf0]
0x001D9AE6: call 0x1403d3050
0x001D9AEB: mov dword ptr [rbp + 0xf0], 0x10098
0x001D9AF5: lea r8, [rbp + 0xf0]
0x001D9AFC: mov edx, 7
```

## call `0x001D9B08` function slot `0x007E7A38`

```asm
0x001D9AE6: call 0x1403d3050
0x001D9AEB: mov dword ptr [rbp + 0xf0], 0x10098
0x001D9AF5: lea r8, [rbp + 0xf0]
0x001D9AFC: mov edx, 7
0x001D9B01: mov rcx, qword ptr [rdi + 0xd0]
0x001D9B08: call qword ptr [rip + 0x60df2a]
0x001D9B0E: mov dword ptr [rsp + 0x24], eax
0x001D9B12: test eax, eax
0x001D9B14: je 0x1401d9d85
```

### refs to global slot `0x007E7A38`: `4`

#### ref `0x001D6307`

```asm
0x001D62A6: mov dword ptr [rbp + rcx + 0x180], edi
0x001D62AD: inc ebx
0x001D62AF: cmp ebx, dword ptr [rbp + 0x158]
0x001D62B5: jb 0x1401d6295
0x001D62B7: lea rdx, [rbp + 0x150]
0x001D62BE: mov rcx, qword ptr [rsi + 0xd0]
0x001D62C5: call qword ptr [rip + 0x61181d]
0x001D62CB: mov ebx, eax
0x001D62CD: mov dword ptr [rsp + 0x20], eax
0x001D62D1: jmp 0x1401d67e4
0x001D62D6: xor edx, edx
0x001D62D8: mov r8d, 0x98
0x001D62DE: lea rcx, [rbp + 0xb0]
0x001D62E5: call 0x1403d3050
0x001D62EA: mov dword ptr [rbp + 0xb0], 0x10098
0x001D62F4: lea r8, [rbp + 0xb0]
0x001D62FB: mov edx, 7
0x001D6300: mov rcx, qword ptr [rsi + 0xd0]
0x001D6307: call qword ptr [rip + 0x61172b]
0x001D630D: mov dword ptr [rsp + 0x30], eax
0x001D6311: test eax, eax
0x001D6313: je 0x1401d652d
0x001D6319: mov dword ptr [rsp + 0x34], 0x45b
0x001D6321: mov dword ptr [rbp - 0x58], 0x7b
0x001D6328: mov dword ptr [rbp - 0x54], 0x32
0x001D632F: mov eax, dword ptr [rbp - 0x54]
```

#### ref `0x001D9B08`

```asm
0x001D9AA6: mov qword ptr [rbp + rdx + 0x1c0], r14
0x001D9AAE: inc eax
0x001D9AB0: cmp eax, dword ptr [rbp + 0x198]
0x001D9AB6: jb 0x1401d9aa0
0x001D9AB8: lea rdx, [rbp + 0x190]
0x001D9ABF: mov rcx, qword ptr [rdi + 0xd0]
0x001D9AC6: call qword ptr [rip + 0x60e01c]
0x001D9ACC: mov ebx, eax
0x001D9ACE: mov dword ptr [rsp + 0x20], eax
0x001D9AD2: jmp 0x1401da25a
0x001D9AD7: xor edx, edx
0x001D9AD9: mov r8d, 0x98
0x001D9ADF: lea rcx, [rbp + 0xf0]
0x001D9AE6: call 0x1403d3050
0x001D9AEB: mov dword ptr [rbp + 0xf0], 0x10098
0x001D9AF5: lea r8, [rbp + 0xf0]
0x001D9AFC: mov edx, 7
0x001D9B01: mov rcx, qword ptr [rdi + 0xd0]
0x001D9B08: call qword ptr [rip + 0x60df2a]
0x001D9B0E: mov dword ptr [rsp + 0x24], eax
0x001D9B12: test eax, eax
0x001D9B14: je 0x1401d9d85
0x001D9B1A: mov dword ptr [rsp + 0x30], 0x4f0
0x001D9B22: mov dword ptr [rbp - 0x80], 0x53
0x001D9B29: mov eax, dword ptr [rbp - 0x80]
0x001D9B2C: xor eax, 0x4e
```

#### ref `0x001DACE7`

```asm
0x001DAC80: mov byte ptr [rbp + 0x118], 0
0x001DAC87: mov esi, dword ptr [rsp + 0x30]
0x001DAC8B: jmp 0x1401db06d
0x001DAC90: cmp dword ptr [rbp + 0x264], 1
0x001DAC97: jb 0x1401db06d
0x001DAC9D: mov eax, dword ptr [rbp + 0x290]
0x001DACA3: test eax, eax
0x001DACA5: js 0x1401db06d
0x001DACAB: mov ecx, dword ptr [rbp + 0x294]
0x001DACB1: jmp 0x1401db053
0x001DACB6: xor edx, edx
0x001DACB8: mov r8d, 0x98
0x001DACBE: lea rcx, [rbp + 0x1c0]
0x001DACC5: call 0x1403d3050
0x001DACCA: mov dword ptr [rbp + 0x1c0], 0x10098
0x001DACD4: lea r8, [rbp + 0x1c0]
0x001DACDB: mov edx, 7
0x001DACE0: mov rcx, qword ptr [rdi + 0xd0]
0x001DACE7: call qword ptr [rip + 0x60cd4b]
0x001DACED: mov dword ptr [rsp + 0x68], eax
0x001DACF1: test eax, eax
0x001DACF3: je 0x1401db03a
0x001DACF9: mov dword ptr [rsp + 0x6c], 0x4aa
0x001DAD01: mov dword ptr [rbp - 8], 0x71
0x001DAD08: mov eax, dword ptr [rbp - 8]
0x001DAD0B: add al, 0x71
```

#### ref `0x001FE4C6`

```asm
0x001FE464: je 0x1401fe296
0x001FE46A: mov ecx, 0xd9930b07
0x001FE46F: call qword ptr [rip + 0x5e9583]
0x001FE475: mov qword ptr [rip + 0x5e95a4], rax
0x001FE47C: test rax, rax
0x001FE47F: je 0x1401fe296
0x001FE485: mov ecx, 0xceee8e9f
0x001FE48A: call qword ptr [rip + 0x5e9568]
0x001FE490: mov qword ptr [rip + 0x5e9591], rax
0x001FE497: test rax, rax
0x001FE49A: je 0x1401fe296
0x001FE4A0: mov ecx, 0x1be0b8e5
0x001FE4A5: call qword ptr [rip + 0x5e954d]
0x001FE4AB: mov qword ptr [rip + 0x5e957e], rax
0x001FE4B2: test rax, rax
0x001FE4B5: je 0x1401fe296
0x001FE4BB: mov ecx, 0xda141340
0x001FE4C0: call qword ptr [rip + 0x5e9532]
0x001FE4C6: mov qword ptr [rip + 0x5e956b], rax
0x001FE4CD: test rax, rax
0x001FE4D0: je 0x1401fe296
0x001FE4D6: mov ecx, 0x891fa0ae
0x001FE4DB: call qword ptr [rip + 0x5e9517]
0x001FE4E1: mov qword ptr [rip + 0x5e9558], rax
0x001FE4E8: test rax, rax
0x001FE4EB: je 0x1401fe296
```

## call `0x001D9DBA` function slot `0x007E7A40`

```asm
0x001D9DA4: mov dword ptr [rbp + 0x44], ecx
0x001D9DA7: mov dword ptr [rbp + 0x48], eax
0x001D9DAA: lea r8, [rbp + 0x30]
0x001D9DAE: mov edx, 7
0x001D9DB3: mov rcx, qword ptr [rdi + 0xd0]
0x001D9DBA: call qword ptr [rip + 0x60dc80]
0x001D9DC0: mov dword ptr [rsp + 0x28], eax
0x001D9DC4: test eax, eax
0x001D9DC6: je 0x1401d9ff5
```

### refs to global slot `0x007E7A40`: `3`

#### ref `0x001D65A9`

```asm
0x001D655C: inc edx
0x001D655E: cmp edx, r8d
0x001D6561: jb 0x1401d6540
0x001D6563: jmp 0x1401d6e0c
0x001D6568: xor eax, eax
0x001D656A: mov qword ptr [rbp + 8], rax
0x001D656E: mov qword ptr [rbp + 0x10], rax
0x001D6572: mov qword ptr [rbp + 0x18], rax
0x001D6576: mov dword ptr [rbp + 8], 0x1001c
0x001D657D: mov dword ptr [rbp + 0xc], edi
0x001D6580: mov dword ptr [rbp + 0x10], 1
0x001D6587: mov dword ptr [rbp + 0x14], edi
0x001D658A: mov dword ptr [rbp + 0x18], 1
0x001D6591: mov dword ptr [rbp + 0x1c], edi
0x001D6594: mov dword ptr [rbp + 0x20], 1
0x001D659B: lea r8, [rbp + 8]
0x001D659F: lea edx, [rax + 7]
0x001D65A2: mov rcx, qword ptr [rsi + 0xd0]
0x001D65A9: call qword ptr [rip + 0x611491]
0x001D65AF: mov dword ptr [rsp + 0x24], eax
0x001D65B3: test eax, eax
0x001D65B5: je 0x1401d67e4
0x001D65BB: mov dword ptr [rsp + 0x38], 0x46f
0x001D65C3: mov dword ptr [rbp - 0x28], 0x26
0x001D65CA: mov dword ptr [rbp - 0x24], 0x54
0x001D65D1: mov eax, dword ptr [rbp - 0x24]
```

#### ref `0x001D9DBA`

```asm
0x001D9D67: call 0x1403b20d4
0x001D9D6C: mov qword ptr [rbp + 0x68], 0xf
0x001D9D74: mov qword ptr [rbp + 0x60], r14
0x001D9D78: mov byte ptr [rbp + 0x50], 0
0x001D9D7C: mov ebx, dword ptr [rsp + 0x24]
0x001D9D80: jmp 0x1401d9ff1
0x001D9D85: mov dword ptr [rbp + 0x30], 0x1001c
0x001D9D8C: mov ecx, dword ptr [rbp + 0x100]
0x001D9D92: mov dword ptr [rbp + 0x34], ecx
0x001D9D95: mov eax, dword ptr [rbp + 0x114]
0x001D9D9B: mov dword ptr [rbp + 0x38], eax
0x001D9D9E: mov dword ptr [rbp + 0x3c], ecx
0x001D9DA1: mov dword ptr [rbp + 0x40], eax
0x001D9DA4: mov dword ptr [rbp + 0x44], ecx
0x001D9DA7: mov dword ptr [rbp + 0x48], eax
0x001D9DAA: lea r8, [rbp + 0x30]
0x001D9DAE: mov edx, 7
0x001D9DB3: mov rcx, qword ptr [rdi + 0xd0]
0x001D9DBA: call qword ptr [rip + 0x60dc80]
0x001D9DC0: mov dword ptr [rsp + 0x28], eax
0x001D9DC4: test eax, eax
0x001D9DC6: je 0x1401d9ff5
0x001D9DCC: mov dword ptr [rsp + 0x34], 0x4fa
0x001D9DD4: mov dword ptr [rbp - 0x50], 5
0x001D9DDB: mov eax, dword ptr [rbp - 0x50]
0x001D9DDE: xor eax, 0x4e
```

#### ref `0x001FE4E1`

```asm
0x001FE47F: je 0x1401fe296
0x001FE485: mov ecx, 0xceee8e9f
0x001FE48A: call qword ptr [rip + 0x5e9568]
0x001FE490: mov qword ptr [rip + 0x5e9591], rax
0x001FE497: test rax, rax
0x001FE49A: je 0x1401fe296
0x001FE4A0: mov ecx, 0x1be0b8e5
0x001FE4A5: call qword ptr [rip + 0x5e954d]
0x001FE4AB: mov qword ptr [rip + 0x5e957e], rax
0x001FE4B2: test rax, rax
0x001FE4B5: je 0x1401fe296
0x001FE4BB: mov ecx, 0xda141340
0x001FE4C0: call qword ptr [rip + 0x5e9532]
0x001FE4C6: mov qword ptr [rip + 0x5e956b], rax
0x001FE4CD: test rax, rax
0x001FE4D0: je 0x1401fe296
0x001FE4D6: mov ecx, 0x891fa0ae
0x001FE4DB: call qword ptr [rip + 0x5e9517]
0x001FE4E1: mov qword ptr [rip + 0x5e9558], rax
0x001FE4E8: test rax, rax
0x001FE4EB: je 0x1401fe296
0x001FE4F1: mov ecx, 0x8f6ed0fb
0x001FE4F6: call qword ptr [rip + 0x5e94fc]
0x001FE4FC: mov ecx, 0xd258bb5
0x001FE501: mov qword ptr [rip + 0x5e9540], rax
0x001FE508: call qword ptr [rip + 0x5e94ea]
```

## call `0x001DA011` function slot `0x007E7A48`

```asm
0x001D9FFC: test rax, rax
0x001D9FFF: je 0x1401da25a
0x001DA005: xor r8d, r8d
0x001DA008: xor edx, edx
0x001DA00A: mov rcx, qword ptr [rdi + 0xd0]
0x001DA011: call rax
0x001DA013: mov dword ptr [rsp + 0x2c], eax
0x001DA017: test eax, eax
0x001DA019: je 0x1401da25a
```

### refs to global slot `0x007E7A48`: `2`

#### ref `0x001D9FF5`

```asm
0x001D9FAE: call 0x1403db020
0x001D9FB3: int3
0x001D9FB4: sub rcx, rax
0x001D9FB7: cmp rcx, 8
0x001D9FBB: jae 0x1401d9fc3
0x001D9FBD: call 0x1403db020
0x001D9FC2: int3
0x001D9FC3: cmp rcx, 0x27
0x001D9FC7: jbe 0x1401d9fcf
0x001D9FC9: call 0x1403db020
0x001D9FCE: int3
0x001D9FCF: mov rcx, rax
0x001D9FD2: call 0x1403b20d4
0x001D9FD7: mov qword ptr [rbp + 0x88], 0xf
0x001D9FE2: mov qword ptr [rbp + 0x80], r14
0x001D9FE9: mov byte ptr [rbp + 0x70], 0
0x001D9FED: mov ebx, dword ptr [rsp + 0x28]
0x001D9FF1: mov dword ptr [rsp + 0x20], ebx
0x001D9FF5: mov rax, qword ptr [rip + 0x60da4c]
0x001D9FFC: test rax, rax
0x001D9FFF: je 0x1401da25a
0x001DA005: xor r8d, r8d
0x001DA008: xor edx, edx
0x001DA00A: mov rcx, qword ptr [rdi + 0xd0]
0x001DA011: call rax
0x001DA013: mov dword ptr [rsp + 0x2c], eax
```

#### ref `0x001FE501`

```asm
0x001FE4A0: mov ecx, 0x1be0b8e5
0x001FE4A5: call qword ptr [rip + 0x5e954d]
0x001FE4AB: mov qword ptr [rip + 0x5e957e], rax
0x001FE4B2: test rax, rax
0x001FE4B5: je 0x1401fe296
0x001FE4BB: mov ecx, 0xda141340
0x001FE4C0: call qword ptr [rip + 0x5e9532]
0x001FE4C6: mov qword ptr [rip + 0x5e956b], rax
0x001FE4CD: test rax, rax
0x001FE4D0: je 0x1401fe296
0x001FE4D6: mov ecx, 0x891fa0ae
0x001FE4DB: call qword ptr [rip + 0x5e9517]
0x001FE4E1: mov qword ptr [rip + 0x5e9558], rax
0x001FE4E8: test rax, rax
0x001FE4EB: je 0x1401fe296
0x001FE4F1: mov ecx, 0x8f6ed0fb
0x001FE4F6: call qword ptr [rip + 0x5e94fc]
0x001FE4FC: mov ecx, 0xd258bb5
0x001FE501: mov qword ptr [rip + 0x5e9540], rax
0x001FE508: call qword ptr [rip + 0x5e94ea]
0x001FE50E: mov qword ptr [rip + 0x5e953b], rax
0x001FE515: test rax, rax
0x001FE518: je 0x1401fe296
0x001FE51E: mov ecx, 0xe9c425a1
0x001FE523: call qword ptr [rip + 0x5e94cf]
0x001FE529: mov qword ptr [rip + 0x5e9528], rax
```

## call `0x001DA93E` function slot `0x007E7AD8`

```asm
0x001DA91E: mov r8d, 0x6a4
0x001DA924: lea rcx, [rbp + 0x264]
0x001DA92B: call 0x1403d3050
0x001DA930: lea rdx, [rbp + 0x260]
0x001DA937: mov rcx, qword ptr [rdi + 0xd0]
0x001DA93E: call rbx
0x001DA940: mov dword ptr [rsp + 0x60], eax
0x001DA944: test eax, eax
0x001DA946: je 0x1401dac90
```

### refs to global slot `0x007E7AD8`: `3`

#### ref `0x001D6FA3`

```asm
0x001D6F4B: mov qword ptr [rax + 0x10], rbx
0x001D6F4F: mov qword ptr [rax + 0x18], rdi
0x001D6F53: mov rax, qword ptr [rip + 0x5ff996]
0x001D6F5A: xor rax, rsp
0x001D6F5D: mov qword ptr [rbp + 0x660], rax
0x001D6F64: mov rdi, rcx
0x001D6F67: cmp byte ptr [rcx + 0xd8], 0
0x001D6F6E: je 0x1401d70e9
0x001D6F74: mov rbx, qword ptr [rcx + 0xd0]
0x001D6F7B: test rbx, rbx
0x001D6F7E: je 0x1401d70e9
0x001D6F84: mov dword ptr [rbp - 0x50], 0x106a8
0x001D6F8B: xor edx, edx
0x001D6F8D: mov r8d, 0x6a4
0x001D6F93: lea rcx, [rbp - 0x4c]
0x001D6F97: call 0x1403d3050
0x001D6F9C: lea rdx, [rbp - 0x50]
0x001D6FA0: mov rcx, rbx
0x001D6FA3: call qword ptr [rip + 0x610b2f]
0x001D6FA9: test eax, eax
0x001D6FAB: jne 0x1401d70e9
0x001D6FB1: mov ebx, dword ptr [rbp - 0x4c]
0x001D6FB4: test ebx, ebx
0x001D6FB6: je 0x1401d70e9
0x001D6FBC: xor r8d, r8d
0x001D6FBF: mov r11d, r8d
```

#### ref `0x001DA902`

```asm
0x001DA8AD: mov dword ptr [rsp + 0x38], r8d
0x001DA8B2: mov dword ptr [rsp + 0x40], r9d
0x001DA8B7: mov eax, dword ptr [rbp + 0x980]
0x001DA8BD: xor r12d, r12d
0x001DA8C0: test eax, eax
0x001DA8C2: cmovs eax, r12d
0x001DA8C6: mov dword ptr [rbp + 0x980], eax
0x001DA8CC: mov eax, dword ptr [rbp + 0x988]
0x001DA8D2: mov ecx, 0x64
0x001DA8D7: test eax, eax
0x001DA8D9: cmovs eax, ecx
0x001DA8DC: mov dword ptr [rbp + 0x988], eax
0x001DA8E2: mov dword ptr [rsp + 0x58], ecx
0x001DA8E6: mov dword ptr [rsp + 0x50], r12d
0x001DA8EB: cmp byte ptr [rdi + 0x28], r12b
0x001DA8EF: jne 0x1401db06d
0x001DA8F5: cmp byte ptr [rdi + 0xd8], r12b
0x001DA8FC: je 0x1401dacb6
0x001DA902: mov rbx, qword ptr [rip + 0x60d1cf]
0x001DA909: test rbx, rbx
0x001DA90C: je 0x1401db06d
0x001DA912: mov dword ptr [rbp + 0x260], 0x106a8
0x001DA91C: xor edx, edx
0x001DA91E: mov r8d, 0x6a4
0x001DA924: lea rcx, [rbp + 0x264]
0x001DA92B: call 0x1403d3050
```

#### ref `0x001FE669`

```asm
0x001FE5FD: mov qword ptr [rip + 0x5e94a4], rax
0x001FE604: call qword ptr [rip + 0x5e93ee]
0x001FE60A: mov ecx, 0x34206d86
0x001FE60F: mov qword ptr [rip + 0x5e949a], rax
0x001FE616: call qword ptr [rip + 0x5e93dc]
0x001FE61C: mov ecx, 0x70916171
0x001FE621: mov qword ptr [rip + 0x5e9490], rax
0x001FE628: call qword ptr [rip + 0x5e93ca]
0x001FE62E: mov ecx, 0xad95f5ed
0x001FE633: mov qword ptr [rip + 0x5e9486], rax
0x001FE63A: call qword ptr [rip + 0x5e93b8]
0x001FE640: mov ecx, 0xfb85b01e
0x001FE645: mov qword ptr [rip + 0x5e947c], rax
0x001FE64C: call qword ptr [rip + 0x5e93a6]
0x001FE652: mov ecx, 0x35aed5e8
0x001FE657: mov qword ptr [rip + 0x5e9472], rax
0x001FE65E: call qword ptr [rip + 0x5e9394]
0x001FE664: mov ecx, 0x814b209f
0x001FE669: mov qword ptr [rip + 0x5e9468], rax
0x001FE670: call qword ptr [rip + 0x5e9382]
0x001FE676: mov ecx, 0xa58971a5
0x001FE67B: mov qword ptr [rip + 0x5e945e], rax
0x001FE682: call qword ptr [rip + 0x5e9370]
0x001FE688: mov ecx, 0x57f7caac
0x001FE68D: mov qword ptr [rip + 0x5e9454], rax
0x001FE694: call qword ptr [rip + 0x5e935e]
```

## call `0x001DACE7` function slot `0x007E7A38`

```asm
0x001DACC5: call 0x1403d3050
0x001DACCA: mov dword ptr [rbp + 0x1c0], 0x10098
0x001DACD4: lea r8, [rbp + 0x1c0]
0x001DACDB: mov edx, 7
0x001DACE0: mov rcx, qword ptr [rdi + 0xd0]
0x001DACE7: call qword ptr [rip + 0x60cd4b]
0x001DACED: mov dword ptr [rsp + 0x68], eax
0x001DACF1: test eax, eax
0x001DACF3: je 0x1401db03a
```

### refs to global slot `0x007E7A38`: `4`

#### ref `0x001D6307`

```asm
0x001D62A6: mov dword ptr [rbp + rcx + 0x180], edi
0x001D62AD: inc ebx
0x001D62AF: cmp ebx, dword ptr [rbp + 0x158]
0x001D62B5: jb 0x1401d6295
0x001D62B7: lea rdx, [rbp + 0x150]
0x001D62BE: mov rcx, qword ptr [rsi + 0xd0]
0x001D62C5: call qword ptr [rip + 0x61181d]
0x001D62CB: mov ebx, eax
0x001D62CD: mov dword ptr [rsp + 0x20], eax
0x001D62D1: jmp 0x1401d67e4
0x001D62D6: xor edx, edx
0x001D62D8: mov r8d, 0x98
0x001D62DE: lea rcx, [rbp + 0xb0]
0x001D62E5: call 0x1403d3050
0x001D62EA: mov dword ptr [rbp + 0xb0], 0x10098
0x001D62F4: lea r8, [rbp + 0xb0]
0x001D62FB: mov edx, 7
0x001D6300: mov rcx, qword ptr [rsi + 0xd0]
0x001D6307: call qword ptr [rip + 0x61172b]
0x001D630D: mov dword ptr [rsp + 0x30], eax
0x001D6311: test eax, eax
0x001D6313: je 0x1401d652d
0x001D6319: mov dword ptr [rsp + 0x34], 0x45b
0x001D6321: mov dword ptr [rbp - 0x58], 0x7b
0x001D6328: mov dword ptr [rbp - 0x54], 0x32
0x001D632F: mov eax, dword ptr [rbp - 0x54]
```

#### ref `0x001D9B08`

```asm
0x001D9AA6: mov qword ptr [rbp + rdx + 0x1c0], r14
0x001D9AAE: inc eax
0x001D9AB0: cmp eax, dword ptr [rbp + 0x198]
0x001D9AB6: jb 0x1401d9aa0
0x001D9AB8: lea rdx, [rbp + 0x190]
0x001D9ABF: mov rcx, qword ptr [rdi + 0xd0]
0x001D9AC6: call qword ptr [rip + 0x60e01c]
0x001D9ACC: mov ebx, eax
0x001D9ACE: mov dword ptr [rsp + 0x20], eax
0x001D9AD2: jmp 0x1401da25a
0x001D9AD7: xor edx, edx
0x001D9AD9: mov r8d, 0x98
0x001D9ADF: lea rcx, [rbp + 0xf0]
0x001D9AE6: call 0x1403d3050
0x001D9AEB: mov dword ptr [rbp + 0xf0], 0x10098
0x001D9AF5: lea r8, [rbp + 0xf0]
0x001D9AFC: mov edx, 7
0x001D9B01: mov rcx, qword ptr [rdi + 0xd0]
0x001D9B08: call qword ptr [rip + 0x60df2a]
0x001D9B0E: mov dword ptr [rsp + 0x24], eax
0x001D9B12: test eax, eax
0x001D9B14: je 0x1401d9d85
0x001D9B1A: mov dword ptr [rsp + 0x30], 0x4f0
0x001D9B22: mov dword ptr [rbp - 0x80], 0x53
0x001D9B29: mov eax, dword ptr [rbp - 0x80]
0x001D9B2C: xor eax, 0x4e
```

#### ref `0x001DACE7`

```asm
0x001DAC80: mov byte ptr [rbp + 0x118], 0
0x001DAC87: mov esi, dword ptr [rsp + 0x30]
0x001DAC8B: jmp 0x1401db06d
0x001DAC90: cmp dword ptr [rbp + 0x264], 1
0x001DAC97: jb 0x1401db06d
0x001DAC9D: mov eax, dword ptr [rbp + 0x290]
0x001DACA3: test eax, eax
0x001DACA5: js 0x1401db06d
0x001DACAB: mov ecx, dword ptr [rbp + 0x294]
0x001DACB1: jmp 0x1401db053
0x001DACB6: xor edx, edx
0x001DACB8: mov r8d, 0x98
0x001DACBE: lea rcx, [rbp + 0x1c0]
0x001DACC5: call 0x1403d3050
0x001DACCA: mov dword ptr [rbp + 0x1c0], 0x10098
0x001DACD4: lea r8, [rbp + 0x1c0]
0x001DACDB: mov edx, 7
0x001DACE0: mov rcx, qword ptr [rdi + 0xd0]
0x001DACE7: call qword ptr [rip + 0x60cd4b]
0x001DACED: mov dword ptr [rsp + 0x68], eax
0x001DACF1: test eax, eax
0x001DACF3: je 0x1401db03a
0x001DACF9: mov dword ptr [rsp + 0x6c], 0x4aa
0x001DAD01: mov dword ptr [rbp - 8], 0x71
0x001DAD08: mov eax, dword ptr [rbp - 8]
0x001DAD0B: add al, 0x71
```

#### ref `0x001FE4C6`

```asm
0x001FE464: je 0x1401fe296
0x001FE46A: mov ecx, 0xd9930b07
0x001FE46F: call qword ptr [rip + 0x5e9583]
0x001FE475: mov qword ptr [rip + 0x5e95a4], rax
0x001FE47C: test rax, rax
0x001FE47F: je 0x1401fe296
0x001FE485: mov ecx, 0xceee8e9f
0x001FE48A: call qword ptr [rip + 0x5e9568]
0x001FE490: mov qword ptr [rip + 0x5e9591], rax
0x001FE497: test rax, rax
0x001FE49A: je 0x1401fe296
0x001FE4A0: mov ecx, 0x1be0b8e5
0x001FE4A5: call qword ptr [rip + 0x5e954d]
0x001FE4AB: mov qword ptr [rip + 0x5e957e], rax
0x001FE4B2: test rax, rax
0x001FE4B5: je 0x1401fe296
0x001FE4BB: mov ecx, 0xda141340
0x001FE4C0: call qword ptr [rip + 0x5e9532]
0x001FE4C6: mov qword ptr [rip + 0x5e956b], rax
0x001FE4CD: test rax, rax
0x001FE4D0: je 0x1401fe296
0x001FE4D6: mov ecx, 0x891fa0ae
0x001FE4DB: call qword ptr [rip + 0x5e9517]
0x001FE4E1: mov qword ptr [rip + 0x5e9558], rax
0x001FE4E8: test rax, rax
0x001FE4EB: je 0x1401fe296
```

## call `0x001DE90E` function slot `0x007E7A90`

```asm
0x001DE8F5: test rax, rax
0x001DE8F8: je 0x1401de91e
0x001DE8FA: mov dword ptr [rsp + 0x20], 0x10
0x001DE902: lea rdx, [rsp + 0x20]
0x001DE907: mov rcx, qword ptr [rcx + 0xd0]
0x001DE90E: call rax
0x001DE910: test eax, eax
0x001DE912: jne 0x1401df608
0x001DE918: mov edi, dword ptr [rsp + 0x20]
```

### refs to global slot `0x007E7A90`: `3`

#### ref `0x001D77C9`

```asm
0x001D7785: je 0x1401d77c9
0x001D7787: xor edx, edx
0x001D7789: lea rcx, [rsp + 0x50]
0x001D778E: mov r8d, 0x8c
0x001D7794: call 0x1403d3050
0x001D7799: mov rcx, qword ptr [rdi + 0xd0]
0x001D77A0: lea rdx, [rsp + 0x50]
0x001D77A5: mov dword ptr [rsp + 0x50], 0x1008c
0x001D77AD: call rsi
0x001D77AF: test eax, eax
0x001D77B1: jne 0x1401d77c9
0x001D77B3: mov ecx, dword ptr [rsp + 0x60]
0x001D77B7: test ecx, ecx
0x001D77B9: je 0x1401d77c9
0x001D77BB: mov eax, 0x10624dd3
0x001D77C0: mul ecx
0x001D77C2: shr edx, 6
0x001D77C5: mov word ptr [rbx + 0xe], dx
0x001D77C9: mov rax, qword ptr [rip + 0x6102c0]
0x001D77D0: test rax, rax
0x001D77D3: je 0x1401d77f6
0x001D77D5: mov rcx, qword ptr [rdi + 0xd0]
0x001D77DC: lea rdx, [rsp + 0x30]
0x001D77E1: mov dword ptr [rsp + 0x30], r12d
0x001D77E6: call rax
0x001D77E8: test eax, eax
```

#### ref `0x001DE8EE`

```asm
0x001DE8AB: int3
0x001DE8AC: int3
0x001DE8AD: int3
0x001DE8AE: int3
0x001DE8AF: int3
0x001DE8B0: mov rax, rsp
0x001DE8B3: push rbp
0x001DE8B4: lea rbp, [rax - 0x138]
0x001DE8BB: sub rsp, 0x230
0x001DE8C2: mov qword ptr [rsp + 0x28], 0xfffffffffffffffe
0x001DE8CB: mov qword ptr [rax + 0x10], rbx
0x001DE8CF: mov qword ptr [rax + 0x18], rsi
0x001DE8D3: mov qword ptr [rax + 0x20], rdi
0x001DE8D7: mov rax, qword ptr [rip + 0x5f8012]
0x001DE8DE: xor rax, rsp
0x001DE8E1: mov qword ptr [rbp + 0x120], rax
0x001DE8E8: movzx esi, dl
0x001DE8EB: mov rbx, rcx
0x001DE8EE: mov rax, qword ptr [rip + 0x60919b]
0x001DE8F5: test rax, rax
0x001DE8F8: je 0x1401de91e
0x001DE8FA: mov dword ptr [rsp + 0x20], 0x10
0x001DE902: lea rdx, [rsp + 0x20]
0x001DE907: mov rcx, qword ptr [rcx + 0xd0]
0x001DE90E: call rax
0x001DE910: test eax, eax
```

#### ref `0x001FE5C7`

```asm
0x001FE55F: mov qword ptr [rip + 0x5e9502], rax
0x001FE566: test rax, rax
0x001FE569: je 0x1401fe296
0x001FE56F: mov ecx, 0xdcb616c3
0x001FE574: call qword ptr [rip + 0x5e947e]
0x001FE57A: mov ecx, 0x1bd69f49
0x001FE57F: mov qword ptr [rip + 0x5e94ea], rax
0x001FE586: call qword ptr [rip + 0x5e946c]
0x001FE58C: mov ecx, 0xc16c7e2c
0x001FE591: mov qword ptr [rip + 0x5e94e0], rax
0x001FE598: call qword ptr [rip + 0x5e945a]
0x001FE59E: mov ecx, 0x465f9bcf
0x001FE5A3: mov qword ptr [rip + 0x5e94d6], rax
0x001FE5AA: call qword ptr [rip + 0x5e9448]
0x001FE5B0: mov ecx, 0x927da4f6
0x001FE5B5: mov qword ptr [rip + 0x5e94cc], rax
0x001FE5BC: call qword ptr [rip + 0x5e9436]
0x001FE5C2: mov ecx, 0x6ff81213
0x001FE5C7: mov qword ptr [rip + 0x5e94c2], rax
0x001FE5CE: call qword ptr [rip + 0x5e9424]
0x001FE5D4: mov ecx, 0xf4dae6b
0x001FE5D9: mov qword ptr [rip + 0x5e94b8], rax
0x001FE5E0: call qword ptr [rip + 0x5e9412]
0x001FE5E6: mov ecx, 0x843c0256
0x001FE5EB: mov qword ptr [rip + 0x5e94ae], rax
0x001FE5F2: call qword ptr [rip + 0x5e9400]
```

## call `0x001E0D6F` function slot `unknown`

```asm
0x001E0CE7: xor edx, edx
0x001E0CE9: lea rcx, [rsp + 0x20]
0x001E0CEE: mov r8d, 0x1808
0x001E0CF4: call 0x1403d3050
0x001E0CF9: mov rcx, qword ptr [rsi + 0xd0]
0x001E0D00: lea rdx, [rsp + 0x20]
0x001E0D05: mov eax, 0x15
0x001E0D0A: mov dword ptr [rsp + 0x20], 0x11808
0x001E0D12: mov word ptr [rsp + 0x28], ax
0x001E0D17: mov word ptr [rsp + 0x40], ax
0x001E0D1C: mov word ptr [rsp + 0x58], ax
0x001E0D21: mov word ptr [rsp + 0x70], ax
0x001E0D26: mov word ptr [rbp - 0x78], ax
0x001E0D2A: mov word ptr [rbp - 0x60], ax
0x001E0D2E: mov word ptr [rbp - 0x48], ax
0x001E0D32: mov dword ptr [rsp + 0x24], 7
0x001E0D3A: mov dword ptr [rsp + 0x2c], 0x9a0290
0x001E0D42: mov dword ptr [rsp + 0x44], 0x9a0294
0x001E0D4A: mov dword ptr [rsp + 0x5c], 0x9a0298
0x001E0D52: mov dword ptr [rsp + 0x74], 0x9a029c
0x001E0D5A: mov dword ptr [rbp - 0x74], 0x9a02a0
0x001E0D61: mov dword ptr [rbp - 0x5c], 0x9a02a4
0x001E0D68: mov dword ptr [rbp - 0x44], 0x9a02a8
0x001E0D6F: call rdi
0x001E0D71: test eax, eax
0x001E0D73: jne 0x1401e0ce0
0x001E0D79: mov rcx, qword ptr [rsp + 0x38]
```

## call `0x001E1199` function slot `0x007E7AA0`

```asm
0x001E117A: mov eax, dword ptr [r9 + 0x30]
0x001E117E: mov dword ptr [rbp + 0x2214], eax
0x001E1184: mov dword ptr [rbp + 0x21f8], r14d
0x001E118B: lea rdx, [rbp + 0x21d0]
0x001E1192: mov rcx, qword ptr [rsi + 0xd0]
0x001E1199: call qword ptr [rip + 0x606901]
0x001E119F: mov dword ptr [rsp + 0x20], eax
0x001E11A3: cmp eax, -1
0x001E11A6: jne 0x1401e128f
```

### refs to global slot `0x007E7AA0`: `5`

#### ref `0x001E1199`

```asm
0x001E1136: movups xmmword ptr [rcx + 0x10], xmm1
0x001E113A: movups xmm0, xmmword ptr [r8 + 0x20]
0x001E113F: movups xmmword ptr [rcx + 0x20], xmm0
0x001E1143: movups xmm1, xmmword ptr [r8 + 0x30]
0x001E1148: movups xmmword ptr [rcx + 0x30], xmm1
0x001E114C: mov rax, qword ptr [r8 + 0x40]
0x001E1150: mov qword ptr [rcx + 0x40], rax
0x001E1154: movups xmm0, xmmword ptr [r9 + 8]
0x001E1159: movups xmmword ptr [rbp + 0x21ec], xmm0
0x001E1160: movups xmm1, xmmword ptr [r9 + 0x18]
0x001E1165: movups xmmword ptr [rbp + 0x21fc], xmm1
0x001E116C: movsd xmm0, qword ptr [r9 + 0x28]
0x001E1172: movsd qword ptr [rbp + 0x220c], xmm0
0x001E117A: mov eax, dword ptr [r9 + 0x30]
0x001E117E: mov dword ptr [rbp + 0x2214], eax
0x001E1184: mov dword ptr [rbp + 0x21f8], r14d
0x001E118B: lea rdx, [rbp + 0x21d0]
0x001E1192: mov rcx, qword ptr [rsi + 0xd0]
0x001E1199: call qword ptr [rip + 0x606901]
0x001E119F: mov dword ptr [rsp + 0x20], eax
0x001E11A3: cmp eax, -1
0x001E11A6: jne 0x1401e128f
0x001E11AC: lea rdx, [rbp + 0x4d0]
0x001E11B3: mov rcx, qword ptr [rsi + 0xd0]
0x001E11BA: call qword ptr [rip + 0x6068d8]
0x001E11C0: test eax, eax
```

#### ref `0x001E2249`

```asm
0x001E21E6: movups xmmword ptr [rcx + 0x10], xmm1
0x001E21EA: movups xmm0, xmmword ptr [r8 + 0x20]
0x001E21EF: movups xmmword ptr [rcx + 0x20], xmm0
0x001E21F3: movups xmm1, xmmword ptr [r8 + 0x30]
0x001E21F8: movups xmmword ptr [rcx + 0x30], xmm1
0x001E21FC: mov rax, qword ptr [r8 + 0x40]
0x001E2200: mov qword ptr [rcx + 0x40], rax
0x001E2204: movups xmm0, xmmword ptr [r9 + 8]
0x001E2209: movups xmmword ptr [rbp + 0x21fc], xmm0
0x001E2210: movups xmm1, xmmword ptr [r9 + 0x18]
0x001E2215: movups xmmword ptr [rbp + 0x220c], xmm1
0x001E221C: movsd xmm0, qword ptr [r9 + 0x28]
0x001E2222: movsd qword ptr [rbp + 0x221c], xmm0
0x001E222A: mov eax, dword ptr [r9 + 0x30]
0x001E222E: mov dword ptr [rbp + 0x2224], eax
0x001E2234: mov dword ptr [rbp + 0x2208], r14d
0x001E223B: lea rdx, [rbp + 0x21e0]
0x001E2242: mov rcx, qword ptr [rsi + 0xd0]
0x001E2249: call qword ptr [rip + 0x605851]
0x001E224F: mov dword ptr [rsp + 0x20], eax
0x001E2253: cmp eax, -1
0x001E2256: jne 0x1401e2340
0x001E225C: lea rdx, [rbp + 0x4e0]
0x001E2263: mov rcx, qword ptr [rsi + 0xd0]
0x001E226A: call qword ptr [rip + 0x605828]
0x001E2270: test eax, eax
```

#### ref `0x001E5CA8`

```asm
0x001E5C46: movups xmmword ptr [rcx + 0x10], xmm1
0x001E5C4A: movups xmm0, xmmword ptr [r9 + 0x20]
0x001E5C4F: movups xmmword ptr [rcx + 0x20], xmm0
0x001E5C53: movups xmm1, xmmword ptr [r9 + 0x30]
0x001E5C58: movups xmmword ptr [rcx + 0x30], xmm1
0x001E5C5C: mov rax, qword ptr [r9 + 0x40]
0x001E5C60: mov qword ptr [rcx + 0x40], rax
0x001E5C64: movups xmm0, xmmword ptr [r10 + 8]
0x001E5C69: movups xmmword ptr [rbp + 0x23ec], xmm0
0x001E5C70: movups xmm1, xmmword ptr [r10 + 0x18]
0x001E5C75: movups xmmword ptr [rbp + 0x23fc], xmm1
0x001E5C7C: movsd xmm0, qword ptr [r10 + 0x28]
0x001E5C82: movsd qword ptr [rbp + 0x240c], xmm0
0x001E5C8A: mov eax, dword ptr [r10 + 0x30]
0x001E5C8E: mov dword ptr [rbp + 0x2414], eax
0x001E5C94: mov dword ptr [rbp + 0x23f8], ebx
0x001E5C9A: lea rdx, [rbp + 0x23d0]
0x001E5CA1: mov rcx, qword ptr [rsi + 0xd0]
0x001E5CA8: call qword ptr [rip + 0x601df2]
0x001E5CAE: mov dword ptr [rsp + 0x20], eax
0x001E5CB2: cmp eax, -1
0x001E5CB5: jne 0x1401e5da0
0x001E5CBB: lea rdx, [rbp + 0x6d0]
0x001E5CC2: mov rcx, qword ptr [rsi + 0xd0]
0x001E5CC9: call qword ptr [rip + 0x601dc9]
0x001E5CCF: test eax, eax
```

#### ref `0x001E7A88`

```asm
0x001E7A26: movups xmmword ptr [rcx + 0x10], xmm1
0x001E7A2A: movups xmm0, xmmword ptr [r9 + 0x20]
0x001E7A2F: movups xmmword ptr [rcx + 0x20], xmm0
0x001E7A33: movups xmm1, xmmword ptr [r9 + 0x30]
0x001E7A38: movups xmmword ptr [rcx + 0x30], xmm1
0x001E7A3C: mov rax, qword ptr [r9 + 0x40]
0x001E7A40: mov qword ptr [rcx + 0x40], rax
0x001E7A44: movups xmm0, xmmword ptr [r10 + 8]
0x001E7A49: movups xmmword ptr [rbp + 0x23fc], xmm0
0x001E7A50: movups xmm1, xmmword ptr [r10 + 0x18]
0x001E7A55: movups xmmword ptr [rbp + 0x240c], xmm1
0x001E7A5C: movsd xmm0, qword ptr [r10 + 0x28]
0x001E7A62: movsd qword ptr [rbp + 0x241c], xmm0
0x001E7A6A: mov eax, dword ptr [r10 + 0x30]
0x001E7A6E: mov dword ptr [rbp + 0x2424], eax
0x001E7A74: mov dword ptr [rbp + 0x2408], ebx
0x001E7A7A: lea rdx, [rbp + 0x23e0]
0x001E7A81: mov rcx, qword ptr [rsi + 0xd0]
0x001E7A88: call qword ptr [rip + 0x600012]
0x001E7A8E: mov dword ptr [rsp + 0x20], eax
0x001E7A92: cmp eax, -1
0x001E7A95: jne 0x1401e7b81
0x001E7A9B: lea rdx, [rbp + 0x6e0]
0x001E7AA2: mov rcx, qword ptr [rsi + 0xd0]
0x001E7AA9: call qword ptr [rip + 0x5fffe9]
0x001E7AAF: test eax, eax
```

#### ref `0x001FE5EB`

```asm
0x001FE57F: mov qword ptr [rip + 0x5e94ea], rax
0x001FE586: call qword ptr [rip + 0x5e946c]
0x001FE58C: mov ecx, 0xc16c7e2c
0x001FE591: mov qword ptr [rip + 0x5e94e0], rax
0x001FE598: call qword ptr [rip + 0x5e945a]
0x001FE59E: mov ecx, 0x465f9bcf
0x001FE5A3: mov qword ptr [rip + 0x5e94d6], rax
0x001FE5AA: call qword ptr [rip + 0x5e9448]
0x001FE5B0: mov ecx, 0x927da4f6
0x001FE5B5: mov qword ptr [rip + 0x5e94cc], rax
0x001FE5BC: call qword ptr [rip + 0x5e9436]
0x001FE5C2: mov ecx, 0x6ff81213
0x001FE5C7: mov qword ptr [rip + 0x5e94c2], rax
0x001FE5CE: call qword ptr [rip + 0x5e9424]
0x001FE5D4: mov ecx, 0xf4dae6b
0x001FE5D9: mov qword ptr [rip + 0x5e94b8], rax
0x001FE5E0: call qword ptr [rip + 0x5e9412]
0x001FE5E6: mov ecx, 0x843c0256
0x001FE5EB: mov qword ptr [rip + 0x5e94ae], rax
0x001FE5F2: call qword ptr [rip + 0x5e9400]
0x001FE5F8: mov ecx, 0xedcf624e
0x001FE5FD: mov qword ptr [rip + 0x5e94a4], rax
0x001FE604: call qword ptr [rip + 0x5e93ee]
0x001FE60A: mov ecx, 0x34206d86
0x001FE60F: mov qword ptr [rip + 0x5e949a], rax
0x001FE616: call qword ptr [rip + 0x5e93dc]
```

## call `0x001E11BA` function slot `0x007E7A98`

```asm
0x001E119F: mov dword ptr [rsp + 0x20], eax
0x001E11A3: cmp eax, -1
0x001E11A6: jne 0x1401e128f
0x001E11AC: lea rdx, [rbp + 0x4d0]
0x001E11B3: mov rcx, qword ptr [rsi + 0xd0]
0x001E11BA: call qword ptr [rip + 0x6068d8]
0x001E11C0: test eax, eax
0x001E11C2: jne 0x1401e1515
0x001E11C8: mov edx, r14d
```

### refs to global slot `0x007E7A98`: `9`

#### ref `0x001E0F3F`

```asm
0x001E0ED7: sub rsp, rax
0x001E0EDA: mov qword ptr [rsp + 0x70], 0xfffffffffffffffe
0x001E0EE3: mov qword ptr [rsp + 0x4058], rbx
0x001E0EEB: mov qword ptr [rsp + 0x4060], rsi
0x001E0EF3: mov rax, qword ptr [rip + 0x5f59f6]
0x001E0EFA: xor rax, rsp
0x001E0EFD: mov qword ptr [rbp + 0x3f20], rax
0x001E0F04: mov rsi, rcx
0x001E0F07: mov rbx, qword ptr [rcx + 0xd0]
0x001E0F0E: test rbx, rbx
0x001E0F11: je 0x1401e1f3e
0x001E0F17: xor edx, edx
0x001E0F19: mov r8d, 0x1cf8
0x001E0F1F: lea rcx, [rbp + 0x4d0]
0x001E0F26: call 0x1403d3050
0x001E0F2B: mov dword ptr [rbp + 0x4d0], 0x31cf8
0x001E0F35: lea rdx, [rbp + 0x4d0]
0x001E0F3C: mov rcx, rbx
0x001E0F3F: call qword ptr [rip + 0x606b53]
0x001E0F45: mov dword ptr [rsp + 0x20], eax
0x001E0F49: test eax, eax
0x001E0F4B: jne 0x1401e1f3e
0x001E0F51: xor r14d, r14d
0x001E0F54: mov ebx, r14d
0x001E0F57: mov r8d, dword ptr [rbp + 0x4d8]
0x001E0F5E: test r8d, r8d
```

#### ref `0x001E11BA`

```asm
0x001E1150: mov qword ptr [rcx + 0x40], rax
0x001E1154: movups xmm0, xmmword ptr [r9 + 8]
0x001E1159: movups xmmword ptr [rbp + 0x21ec], xmm0
0x001E1160: movups xmm1, xmmword ptr [r9 + 0x18]
0x001E1165: movups xmmword ptr [rbp + 0x21fc], xmm1
0x001E116C: movsd xmm0, qword ptr [r9 + 0x28]
0x001E1172: movsd qword ptr [rbp + 0x220c], xmm0
0x001E117A: mov eax, dword ptr [r9 + 0x30]
0x001E117E: mov dword ptr [rbp + 0x2214], eax
0x001E1184: mov dword ptr [rbp + 0x21f8], r14d
0x001E118B: lea rdx, [rbp + 0x21d0]
0x001E1192: mov rcx, qword ptr [rsi + 0xd0]
0x001E1199: call qword ptr [rip + 0x606901]
0x001E119F: mov dword ptr [rsp + 0x20], eax
0x001E11A3: cmp eax, -1
0x001E11A6: jne 0x1401e128f
0x001E11AC: lea rdx, [rbp + 0x4d0]
0x001E11B3: mov rcx, qword ptr [rsi + 0xd0]
0x001E11BA: call qword ptr [rip + 0x6068d8]
0x001E11C0: test eax, eax
0x001E11C2: jne 0x1401e1515
0x001E11C8: mov edx, r14d
0x001E11CB: mov r10d, dword ptr [rbp + 0x4d8]
0x001E11D2: test r10d, r10d
0x001E11D5: je 0x1401e1515
0x001E11DB: nop dword ptr [rax + rax]
```

#### ref `0x001E1FEF`

```asm
0x001E1F87: sub rsp, rax
0x001E1F8A: mov qword ptr [rsp + 0x70], 0xfffffffffffffffe
0x001E1F93: mov qword ptr [rsp + 0x4068], rbx
0x001E1F9B: mov qword ptr [rsp + 0x4070], rsi
0x001E1FA3: mov rax, qword ptr [rip + 0x5f4946]
0x001E1FAA: xor rax, rsp
0x001E1FAD: mov qword ptr [rbp + 0x3f30], rax
0x001E1FB4: mov rsi, rcx
0x001E1FB7: mov rbx, qword ptr [rcx + 0xd0]
0x001E1FBE: test rbx, rbx
0x001E1FC1: je 0x1401e2fb2
0x001E1FC7: xor edx, edx
0x001E1FC9: mov r8d, 0x1cf8
0x001E1FCF: lea rcx, [rbp + 0x4e0]
0x001E1FD6: call 0x1403d3050
0x001E1FDB: mov dword ptr [rbp + 0x4e0], 0x31cf8
0x001E1FE5: lea rdx, [rbp + 0x4e0]
0x001E1FEC: mov rcx, rbx
0x001E1FEF: call qword ptr [rip + 0x605aa3]
0x001E1FF5: mov dword ptr [rsp + 0x20], eax
0x001E1FF9: test eax, eax
0x001E1FFB: jne 0x1401e2fb2
0x001E2001: xor r14d, r14d
0x001E2004: mov ebx, r14d
0x001E2007: mov r8d, dword ptr [rbp + 0x4e8]
0x001E200E: test r8d, r8d
```

#### ref `0x001E226A`

```asm
0x001E2200: mov qword ptr [rcx + 0x40], rax
0x001E2204: movups xmm0, xmmword ptr [r9 + 8]
0x001E2209: movups xmmword ptr [rbp + 0x21fc], xmm0
0x001E2210: movups xmm1, xmmword ptr [r9 + 0x18]
0x001E2215: movups xmmword ptr [rbp + 0x220c], xmm1
0x001E221C: movsd xmm0, qword ptr [r9 + 0x28]
0x001E2222: movsd qword ptr [rbp + 0x221c], xmm0
0x001E222A: mov eax, dword ptr [r9 + 0x30]
0x001E222E: mov dword ptr [rbp + 0x2224], eax
0x001E2234: mov dword ptr [rbp + 0x2208], r14d
0x001E223B: lea rdx, [rbp + 0x21e0]
0x001E2242: mov rcx, qword ptr [rsi + 0xd0]
0x001E2249: call qword ptr [rip + 0x605851]
0x001E224F: mov dword ptr [rsp + 0x20], eax
0x001E2253: cmp eax, -1
0x001E2256: jne 0x1401e2340
0x001E225C: lea rdx, [rbp + 0x4e0]
0x001E2263: mov rcx, qword ptr [rsi + 0xd0]
0x001E226A: call qword ptr [rip + 0x605828]
0x001E2270: test eax, eax
0x001E2272: jne 0x1401e2770
0x001E2278: mov edx, r14d
0x001E227B: mov r10d, dword ptr [rbp + 0x4e8]
0x001E2282: test r10d, r10d
0x001E2285: je 0x1401e2770
0x001E228B: nop dword ptr [rax + rax]
```

#### ref `0x001E59FD`

```asm
0x001E59AC: cmp rcx, 8
0x001E59B0: jae 0x1401e59b8
0x001E59B2: call 0x1403db020
0x001E59B7: int3
0x001E59B8: cmp rcx, 0x27
0x001E59BC: jbe 0x1401e59c4
0x001E59BE: call 0x1403db020
0x001E59C3: int3
0x001E59C4: mov rcx, rax
0x001E59C7: call 0x1403b20d4
0x001E59CC: jmp 0x1401e6c57
0x001E59D1: xor edx, edx
0x001E59D3: mov r8d, 0x1cf8
0x001E59D9: lea rcx, [rbp + 0x6d0]
0x001E59E0: call 0x1403d3050
0x001E59E5: mov dword ptr [rbp + 0x6d0], 0x31cf8
0x001E59EF: lea rdx, [rbp + 0x6d0]
0x001E59F6: mov rcx, qword ptr [rsi + 0xd0]
0x001E59FD: call qword ptr [rip + 0x602095]
0x001E5A03: mov dword ptr [rsp + 0x20], eax
0x001E5A07: test eax, eax
0x001E5A09: jne 0x1401e6c57
0x001E5A0F: mov ebx, r15d
0x001E5A12: mov r8d, dword ptr [rbp + 0x6d8]
0x001E5A19: test r8d, r8d
0x001E5A1C: je 0x1401e6627
```

#### ref `0x001E5CC9`

```asm
0x001E5C60: mov qword ptr [rcx + 0x40], rax
0x001E5C64: movups xmm0, xmmword ptr [r10 + 8]
0x001E5C69: movups xmmword ptr [rbp + 0x23ec], xmm0
0x001E5C70: movups xmm1, xmmword ptr [r10 + 0x18]
0x001E5C75: movups xmmword ptr [rbp + 0x23fc], xmm1
0x001E5C7C: movsd xmm0, qword ptr [r10 + 0x28]
0x001E5C82: movsd qword ptr [rbp + 0x240c], xmm0
0x001E5C8A: mov eax, dword ptr [r10 + 0x30]
0x001E5C8E: mov dword ptr [rbp + 0x2414], eax
0x001E5C94: mov dword ptr [rbp + 0x23f8], ebx
0x001E5C9A: lea rdx, [rbp + 0x23d0]
0x001E5CA1: mov rcx, qword ptr [rsi + 0xd0]
0x001E5CA8: call qword ptr [rip + 0x601df2]
0x001E5CAE: mov dword ptr [rsp + 0x20], eax
0x001E5CB2: cmp eax, -1
0x001E5CB5: jne 0x1401e5da0
0x001E5CBB: lea rdx, [rbp + 0x6d0]
0x001E5CC2: mov rcx, qword ptr [rsi + 0xd0]
0x001E5CC9: call qword ptr [rip + 0x601dc9]
0x001E5CCF: test eax, eax
0x001E5CD1: jne 0x1401e602b
0x001E5CD7: mov r8d, r15d
0x001E5CDA: mov r10d, dword ptr [rbp + 0x6d8]
0x001E5CE1: test r10d, r10d
0x001E5CE4: je 0x1401e602b
0x001E5CEA: nop word ptr [rax + rax]
```

#### ref `0x001E77DE`

```asm
0x001E7786: call 0x1403db020
0x001E778B: int3
0x001E778C: cmp rcx, 0x27
0x001E7790: jbe 0x1401e7798
0x001E7792: call 0x1403db020
0x001E7797: int3
0x001E7798: mov rcx, rax
0x001E779B: call 0x1403b20d4
0x001E77A0: jmp 0x1401e89e4
0x001E77A5: cmp byte ptr [rbp + 0x4190], r15b
0x001E77AC: jne 0x1401e89e4
0x001E77B2: xor edx, edx
0x001E77B4: mov r8d, 0x1cf8
0x001E77BA: lea rcx, [rbp + 0x6e0]
0x001E77C1: call 0x1403d3050
0x001E77C6: mov dword ptr [rbp + 0x6e0], 0x31cf8
0x001E77D0: lea rdx, [rbp + 0x6e0]
0x001E77D7: mov rcx, qword ptr [rsi + 0xd0]
0x001E77DE: call qword ptr [rip + 0x6002b4]
0x001E77E4: mov dword ptr [rsp + 0x20], eax
0x001E77E8: test eax, eax
0x001E77EA: jne 0x1401e89e4
0x001E77F0: mov ebx, r15d
0x001E77F3: mov r8d, dword ptr [rbp + 0x6e8]
0x001E77FA: test r8d, r8d
0x001E77FD: je 0x1401e83b4
```

#### ref `0x001E7AA9`

```asm
0x001E7A40: mov qword ptr [rcx + 0x40], rax
0x001E7A44: movups xmm0, xmmword ptr [r10 + 8]
0x001E7A49: movups xmmword ptr [rbp + 0x23fc], xmm0
0x001E7A50: movups xmm1, xmmword ptr [r10 + 0x18]
0x001E7A55: movups xmmword ptr [rbp + 0x240c], xmm1
0x001E7A5C: movsd xmm0, qword ptr [r10 + 0x28]
0x001E7A62: movsd qword ptr [rbp + 0x241c], xmm0
0x001E7A6A: mov eax, dword ptr [r10 + 0x30]
0x001E7A6E: mov dword ptr [rbp + 0x2424], eax
0x001E7A74: mov dword ptr [rbp + 0x2408], ebx
0x001E7A7A: lea rdx, [rbp + 0x23e0]
0x001E7A81: mov rcx, qword ptr [rsi + 0xd0]
0x001E7A88: call qword ptr [rip + 0x600012]
0x001E7A8E: mov dword ptr [rsp + 0x20], eax
0x001E7A92: cmp eax, -1
0x001E7A95: jne 0x1401e7b81
0x001E7A9B: lea rdx, [rbp + 0x6e0]
0x001E7AA2: mov rcx, qword ptr [rsi + 0xd0]
0x001E7AA9: call qword ptr [rip + 0x5fffe9]
0x001E7AAF: test eax, eax
0x001E7AB1: jne 0x1401e7fac
0x001E7AB7: mov r8d, r15d
0x001E7ABA: mov r10d, dword ptr [rbp + 0x6e8]
0x001E7AC1: test r10d, r10d
0x001E7AC4: je 0x1401e7fac
0x001E7ACA: nop word ptr [rax + rax]
```

#### ref `0x001FE5D9`

```asm
0x001FE56F: mov ecx, 0xdcb616c3
0x001FE574: call qword ptr [rip + 0x5e947e]
0x001FE57A: mov ecx, 0x1bd69f49
0x001FE57F: mov qword ptr [rip + 0x5e94ea], rax
0x001FE586: call qword ptr [rip + 0x5e946c]
0x001FE58C: mov ecx, 0xc16c7e2c
0x001FE591: mov qword ptr [rip + 0x5e94e0], rax
0x001FE598: call qword ptr [rip + 0x5e945a]
0x001FE59E: mov ecx, 0x465f9bcf
0x001FE5A3: mov qword ptr [rip + 0x5e94d6], rax
0x001FE5AA: call qword ptr [rip + 0x5e9448]
0x001FE5B0: mov ecx, 0x927da4f6
0x001FE5B5: mov qword ptr [rip + 0x5e94cc], rax
0x001FE5BC: call qword ptr [rip + 0x5e9436]
0x001FE5C2: mov ecx, 0x6ff81213
0x001FE5C7: mov qword ptr [rip + 0x5e94c2], rax
0x001FE5CE: call qword ptr [rip + 0x5e9424]
0x001FE5D4: mov ecx, 0xf4dae6b
0x001FE5D9: mov qword ptr [rip + 0x5e94b8], rax
0x001FE5E0: call qword ptr [rip + 0x5e9412]
0x001FE5E6: mov ecx, 0x843c0256
0x001FE5EB: mov qword ptr [rip + 0x5e94ae], rax
0x001FE5F2: call qword ptr [rip + 0x5e9400]
0x001FE5F8: mov ecx, 0xedcf624e
0x001FE5FD: mov qword ptr [rip + 0x5e94a4], rax
0x001FE604: call qword ptr [rip + 0x5e93ee]
```

## call `0x001E2249` function slot `0x007E7AA0`

```asm
0x001E222A: mov eax, dword ptr [r9 + 0x30]
0x001E222E: mov dword ptr [rbp + 0x2224], eax
0x001E2234: mov dword ptr [rbp + 0x2208], r14d
0x001E223B: lea rdx, [rbp + 0x21e0]
0x001E2242: mov rcx, qword ptr [rsi + 0xd0]
0x001E2249: call qword ptr [rip + 0x605851]
0x001E224F: mov dword ptr [rsp + 0x20], eax
0x001E2253: cmp eax, -1
0x001E2256: jne 0x1401e2340
```

### refs to global slot `0x007E7AA0`: `5`

#### ref `0x001E1199`

```asm
0x001E1136: movups xmmword ptr [rcx + 0x10], xmm1
0x001E113A: movups xmm0, xmmword ptr [r8 + 0x20]
0x001E113F: movups xmmword ptr [rcx + 0x20], xmm0
0x001E1143: movups xmm1, xmmword ptr [r8 + 0x30]
0x001E1148: movups xmmword ptr [rcx + 0x30], xmm1
0x001E114C: mov rax, qword ptr [r8 + 0x40]
0x001E1150: mov qword ptr [rcx + 0x40], rax
0x001E1154: movups xmm0, xmmword ptr [r9 + 8]
0x001E1159: movups xmmword ptr [rbp + 0x21ec], xmm0
0x001E1160: movups xmm1, xmmword ptr [r9 + 0x18]
0x001E1165: movups xmmword ptr [rbp + 0x21fc], xmm1
0x001E116C: movsd xmm0, qword ptr [r9 + 0x28]
0x001E1172: movsd qword ptr [rbp + 0x220c], xmm0
0x001E117A: mov eax, dword ptr [r9 + 0x30]
0x001E117E: mov dword ptr [rbp + 0x2214], eax
0x001E1184: mov dword ptr [rbp + 0x21f8], r14d
0x001E118B: lea rdx, [rbp + 0x21d0]
0x001E1192: mov rcx, qword ptr [rsi + 0xd0]
0x001E1199: call qword ptr [rip + 0x606901]
0x001E119F: mov dword ptr [rsp + 0x20], eax
0x001E11A3: cmp eax, -1
0x001E11A6: jne 0x1401e128f
0x001E11AC: lea rdx, [rbp + 0x4d0]
0x001E11B3: mov rcx, qword ptr [rsi + 0xd0]
0x001E11BA: call qword ptr [rip + 0x6068d8]
0x001E11C0: test eax, eax
```

#### ref `0x001E2249`

```asm
0x001E21E6: movups xmmword ptr [rcx + 0x10], xmm1
0x001E21EA: movups xmm0, xmmword ptr [r8 + 0x20]
0x001E21EF: movups xmmword ptr [rcx + 0x20], xmm0
0x001E21F3: movups xmm1, xmmword ptr [r8 + 0x30]
0x001E21F8: movups xmmword ptr [rcx + 0x30], xmm1
0x001E21FC: mov rax, qword ptr [r8 + 0x40]
0x001E2200: mov qword ptr [rcx + 0x40], rax
0x001E2204: movups xmm0, xmmword ptr [r9 + 8]
0x001E2209: movups xmmword ptr [rbp + 0x21fc], xmm0
0x001E2210: movups xmm1, xmmword ptr [r9 + 0x18]
0x001E2215: movups xmmword ptr [rbp + 0x220c], xmm1
0x001E221C: movsd xmm0, qword ptr [r9 + 0x28]
0x001E2222: movsd qword ptr [rbp + 0x221c], xmm0
0x001E222A: mov eax, dword ptr [r9 + 0x30]
0x001E222E: mov dword ptr [rbp + 0x2224], eax
0x001E2234: mov dword ptr [rbp + 0x2208], r14d
0x001E223B: lea rdx, [rbp + 0x21e0]
0x001E2242: mov rcx, qword ptr [rsi + 0xd0]
0x001E2249: call qword ptr [rip + 0x605851]
0x001E224F: mov dword ptr [rsp + 0x20], eax
0x001E2253: cmp eax, -1
0x001E2256: jne 0x1401e2340
0x001E225C: lea rdx, [rbp + 0x4e0]
0x001E2263: mov rcx, qword ptr [rsi + 0xd0]
0x001E226A: call qword ptr [rip + 0x605828]
0x001E2270: test eax, eax
```

#### ref `0x001E5CA8`

```asm
0x001E5C46: movups xmmword ptr [rcx + 0x10], xmm1
0x001E5C4A: movups xmm0, xmmword ptr [r9 + 0x20]
0x001E5C4F: movups xmmword ptr [rcx + 0x20], xmm0
0x001E5C53: movups xmm1, xmmword ptr [r9 + 0x30]
0x001E5C58: movups xmmword ptr [rcx + 0x30], xmm1
0x001E5C5C: mov rax, qword ptr [r9 + 0x40]
0x001E5C60: mov qword ptr [rcx + 0x40], rax
0x001E5C64: movups xmm0, xmmword ptr [r10 + 8]
0x001E5C69: movups xmmword ptr [rbp + 0x23ec], xmm0
0x001E5C70: movups xmm1, xmmword ptr [r10 + 0x18]
0x001E5C75: movups xmmword ptr [rbp + 0x23fc], xmm1
0x001E5C7C: movsd xmm0, qword ptr [r10 + 0x28]
0x001E5C82: movsd qword ptr [rbp + 0x240c], xmm0
0x001E5C8A: mov eax, dword ptr [r10 + 0x30]
0x001E5C8E: mov dword ptr [rbp + 0x2414], eax
0x001E5C94: mov dword ptr [rbp + 0x23f8], ebx
0x001E5C9A: lea rdx, [rbp + 0x23d0]
0x001E5CA1: mov rcx, qword ptr [rsi + 0xd0]
0x001E5CA8: call qword ptr [rip + 0x601df2]
0x001E5CAE: mov dword ptr [rsp + 0x20], eax
0x001E5CB2: cmp eax, -1
0x001E5CB5: jne 0x1401e5da0
0x001E5CBB: lea rdx, [rbp + 0x6d0]
0x001E5CC2: mov rcx, qword ptr [rsi + 0xd0]
0x001E5CC9: call qword ptr [rip + 0x601dc9]
0x001E5CCF: test eax, eax
```

#### ref `0x001E7A88`

```asm
0x001E7A26: movups xmmword ptr [rcx + 0x10], xmm1
0x001E7A2A: movups xmm0, xmmword ptr [r9 + 0x20]
0x001E7A2F: movups xmmword ptr [rcx + 0x20], xmm0
0x001E7A33: movups xmm1, xmmword ptr [r9 + 0x30]
0x001E7A38: movups xmmword ptr [rcx + 0x30], xmm1
0x001E7A3C: mov rax, qword ptr [r9 + 0x40]
0x001E7A40: mov qword ptr [rcx + 0x40], rax
0x001E7A44: movups xmm0, xmmword ptr [r10 + 8]
0x001E7A49: movups xmmword ptr [rbp + 0x23fc], xmm0
0x001E7A50: movups xmm1, xmmword ptr [r10 + 0x18]
0x001E7A55: movups xmmword ptr [rbp + 0x240c], xmm1
0x001E7A5C: movsd xmm0, qword ptr [r10 + 0x28]
0x001E7A62: movsd qword ptr [rbp + 0x241c], xmm0
0x001E7A6A: mov eax, dword ptr [r10 + 0x30]
0x001E7A6E: mov dword ptr [rbp + 0x2424], eax
0x001E7A74: mov dword ptr [rbp + 0x2408], ebx
0x001E7A7A: lea rdx, [rbp + 0x23e0]
0x001E7A81: mov rcx, qword ptr [rsi + 0xd0]
0x001E7A88: call qword ptr [rip + 0x600012]
0x001E7A8E: mov dword ptr [rsp + 0x20], eax
0x001E7A92: cmp eax, -1
0x001E7A95: jne 0x1401e7b81
0x001E7A9B: lea rdx, [rbp + 0x6e0]
0x001E7AA2: mov rcx, qword ptr [rsi + 0xd0]
0x001E7AA9: call qword ptr [rip + 0x5fffe9]
0x001E7AAF: test eax, eax
```

#### ref `0x001FE5EB`

```asm
0x001FE57F: mov qword ptr [rip + 0x5e94ea], rax
0x001FE586: call qword ptr [rip + 0x5e946c]
0x001FE58C: mov ecx, 0xc16c7e2c
0x001FE591: mov qword ptr [rip + 0x5e94e0], rax
0x001FE598: call qword ptr [rip + 0x5e945a]
0x001FE59E: mov ecx, 0x465f9bcf
0x001FE5A3: mov qword ptr [rip + 0x5e94d6], rax
0x001FE5AA: call qword ptr [rip + 0x5e9448]
0x001FE5B0: mov ecx, 0x927da4f6
0x001FE5B5: mov qword ptr [rip + 0x5e94cc], rax
0x001FE5BC: call qword ptr [rip + 0x5e9436]
0x001FE5C2: mov ecx, 0x6ff81213
0x001FE5C7: mov qword ptr [rip + 0x5e94c2], rax
0x001FE5CE: call qword ptr [rip + 0x5e9424]
0x001FE5D4: mov ecx, 0xf4dae6b
0x001FE5D9: mov qword ptr [rip + 0x5e94b8], rax
0x001FE5E0: call qword ptr [rip + 0x5e9412]
0x001FE5E6: mov ecx, 0x843c0256
0x001FE5EB: mov qword ptr [rip + 0x5e94ae], rax
0x001FE5F2: call qword ptr [rip + 0x5e9400]
0x001FE5F8: mov ecx, 0xedcf624e
0x001FE5FD: mov qword ptr [rip + 0x5e94a4], rax
0x001FE604: call qword ptr [rip + 0x5e93ee]
0x001FE60A: mov ecx, 0x34206d86
0x001FE60F: mov qword ptr [rip + 0x5e949a], rax
0x001FE616: call qword ptr [rip + 0x5e93dc]
```

## call `0x001E226A` function slot `0x007E7A98`

```asm
0x001E224F: mov dword ptr [rsp + 0x20], eax
0x001E2253: cmp eax, -1
0x001E2256: jne 0x1401e2340
0x001E225C: lea rdx, [rbp + 0x4e0]
0x001E2263: mov rcx, qword ptr [rsi + 0xd0]
0x001E226A: call qword ptr [rip + 0x605828]
0x001E2270: test eax, eax
0x001E2272: jne 0x1401e2770
0x001E2278: mov edx, r14d
```

### refs to global slot `0x007E7A98`: `9`

#### ref `0x001E0F3F`

```asm
0x001E0ED7: sub rsp, rax
0x001E0EDA: mov qword ptr [rsp + 0x70], 0xfffffffffffffffe
0x001E0EE3: mov qword ptr [rsp + 0x4058], rbx
0x001E0EEB: mov qword ptr [rsp + 0x4060], rsi
0x001E0EF3: mov rax, qword ptr [rip + 0x5f59f6]
0x001E0EFA: xor rax, rsp
0x001E0EFD: mov qword ptr [rbp + 0x3f20], rax
0x001E0F04: mov rsi, rcx
0x001E0F07: mov rbx, qword ptr [rcx + 0xd0]
0x001E0F0E: test rbx, rbx
0x001E0F11: je 0x1401e1f3e
0x001E0F17: xor edx, edx
0x001E0F19: mov r8d, 0x1cf8
0x001E0F1F: lea rcx, [rbp + 0x4d0]
0x001E0F26: call 0x1403d3050
0x001E0F2B: mov dword ptr [rbp + 0x4d0], 0x31cf8
0x001E0F35: lea rdx, [rbp + 0x4d0]
0x001E0F3C: mov rcx, rbx
0x001E0F3F: call qword ptr [rip + 0x606b53]
0x001E0F45: mov dword ptr [rsp + 0x20], eax
0x001E0F49: test eax, eax
0x001E0F4B: jne 0x1401e1f3e
0x001E0F51: xor r14d, r14d
0x001E0F54: mov ebx, r14d
0x001E0F57: mov r8d, dword ptr [rbp + 0x4d8]
0x001E0F5E: test r8d, r8d
```

#### ref `0x001E11BA`

```asm
0x001E1150: mov qword ptr [rcx + 0x40], rax
0x001E1154: movups xmm0, xmmword ptr [r9 + 8]
0x001E1159: movups xmmword ptr [rbp + 0x21ec], xmm0
0x001E1160: movups xmm1, xmmword ptr [r9 + 0x18]
0x001E1165: movups xmmword ptr [rbp + 0x21fc], xmm1
0x001E116C: movsd xmm0, qword ptr [r9 + 0x28]
0x001E1172: movsd qword ptr [rbp + 0x220c], xmm0
0x001E117A: mov eax, dword ptr [r9 + 0x30]
0x001E117E: mov dword ptr [rbp + 0x2214], eax
0x001E1184: mov dword ptr [rbp + 0x21f8], r14d
0x001E118B: lea rdx, [rbp + 0x21d0]
0x001E1192: mov rcx, qword ptr [rsi + 0xd0]
0x001E1199: call qword ptr [rip + 0x606901]
0x001E119F: mov dword ptr [rsp + 0x20], eax
0x001E11A3: cmp eax, -1
0x001E11A6: jne 0x1401e128f
0x001E11AC: lea rdx, [rbp + 0x4d0]
0x001E11B3: mov rcx, qword ptr [rsi + 0xd0]
0x001E11BA: call qword ptr [rip + 0x6068d8]
0x001E11C0: test eax, eax
0x001E11C2: jne 0x1401e1515
0x001E11C8: mov edx, r14d
0x001E11CB: mov r10d, dword ptr [rbp + 0x4d8]
0x001E11D2: test r10d, r10d
0x001E11D5: je 0x1401e1515
0x001E11DB: nop dword ptr [rax + rax]
```

#### ref `0x001E1FEF`

```asm
0x001E1F87: sub rsp, rax
0x001E1F8A: mov qword ptr [rsp + 0x70], 0xfffffffffffffffe
0x001E1F93: mov qword ptr [rsp + 0x4068], rbx
0x001E1F9B: mov qword ptr [rsp + 0x4070], rsi
0x001E1FA3: mov rax, qword ptr [rip + 0x5f4946]
0x001E1FAA: xor rax, rsp
0x001E1FAD: mov qword ptr [rbp + 0x3f30], rax
0x001E1FB4: mov rsi, rcx
0x001E1FB7: mov rbx, qword ptr [rcx + 0xd0]
0x001E1FBE: test rbx, rbx
0x001E1FC1: je 0x1401e2fb2
0x001E1FC7: xor edx, edx
0x001E1FC9: mov r8d, 0x1cf8
0x001E1FCF: lea rcx, [rbp + 0x4e0]
0x001E1FD6: call 0x1403d3050
0x001E1FDB: mov dword ptr [rbp + 0x4e0], 0x31cf8
0x001E1FE5: lea rdx, [rbp + 0x4e0]
0x001E1FEC: mov rcx, rbx
0x001E1FEF: call qword ptr [rip + 0x605aa3]
0x001E1FF5: mov dword ptr [rsp + 0x20], eax
0x001E1FF9: test eax, eax
0x001E1FFB: jne 0x1401e2fb2
0x001E2001: xor r14d, r14d
0x001E2004: mov ebx, r14d
0x001E2007: mov r8d, dword ptr [rbp + 0x4e8]
0x001E200E: test r8d, r8d
```

#### ref `0x001E226A`

```asm
0x001E2200: mov qword ptr [rcx + 0x40], rax
0x001E2204: movups xmm0, xmmword ptr [r9 + 8]
0x001E2209: movups xmmword ptr [rbp + 0x21fc], xmm0
0x001E2210: movups xmm1, xmmword ptr [r9 + 0x18]
0x001E2215: movups xmmword ptr [rbp + 0x220c], xmm1
0x001E221C: movsd xmm0, qword ptr [r9 + 0x28]
0x001E2222: movsd qword ptr [rbp + 0x221c], xmm0
0x001E222A: mov eax, dword ptr [r9 + 0x30]
0x001E222E: mov dword ptr [rbp + 0x2224], eax
0x001E2234: mov dword ptr [rbp + 0x2208], r14d
0x001E223B: lea rdx, [rbp + 0x21e0]
0x001E2242: mov rcx, qword ptr [rsi + 0xd0]
0x001E2249: call qword ptr [rip + 0x605851]
0x001E224F: mov dword ptr [rsp + 0x20], eax
0x001E2253: cmp eax, -1
0x001E2256: jne 0x1401e2340
0x001E225C: lea rdx, [rbp + 0x4e0]
0x001E2263: mov rcx, qword ptr [rsi + 0xd0]
0x001E226A: call qword ptr [rip + 0x605828]
0x001E2270: test eax, eax
0x001E2272: jne 0x1401e2770
0x001E2278: mov edx, r14d
0x001E227B: mov r10d, dword ptr [rbp + 0x4e8]
0x001E2282: test r10d, r10d
0x001E2285: je 0x1401e2770
0x001E228B: nop dword ptr [rax + rax]
```

#### ref `0x001E59FD`

```asm
0x001E59AC: cmp rcx, 8
0x001E59B0: jae 0x1401e59b8
0x001E59B2: call 0x1403db020
0x001E59B7: int3
0x001E59B8: cmp rcx, 0x27
0x001E59BC: jbe 0x1401e59c4
0x001E59BE: call 0x1403db020
0x001E59C3: int3
0x001E59C4: mov rcx, rax
0x001E59C7: call 0x1403b20d4
0x001E59CC: jmp 0x1401e6c57
0x001E59D1: xor edx, edx
0x001E59D3: mov r8d, 0x1cf8
0x001E59D9: lea rcx, [rbp + 0x6d0]
0x001E59E0: call 0x1403d3050
0x001E59E5: mov dword ptr [rbp + 0x6d0], 0x31cf8
0x001E59EF: lea rdx, [rbp + 0x6d0]
0x001E59F6: mov rcx, qword ptr [rsi + 0xd0]
0x001E59FD: call qword ptr [rip + 0x602095]
0x001E5A03: mov dword ptr [rsp + 0x20], eax
0x001E5A07: test eax, eax
0x001E5A09: jne 0x1401e6c57
0x001E5A0F: mov ebx, r15d
0x001E5A12: mov r8d, dword ptr [rbp + 0x6d8]
0x001E5A19: test r8d, r8d
0x001E5A1C: je 0x1401e6627
```

#### ref `0x001E5CC9`

```asm
0x001E5C60: mov qword ptr [rcx + 0x40], rax
0x001E5C64: movups xmm0, xmmword ptr [r10 + 8]
0x001E5C69: movups xmmword ptr [rbp + 0x23ec], xmm0
0x001E5C70: movups xmm1, xmmword ptr [r10 + 0x18]
0x001E5C75: movups xmmword ptr [rbp + 0x23fc], xmm1
0x001E5C7C: movsd xmm0, qword ptr [r10 + 0x28]
0x001E5C82: movsd qword ptr [rbp + 0x240c], xmm0
0x001E5C8A: mov eax, dword ptr [r10 + 0x30]
0x001E5C8E: mov dword ptr [rbp + 0x2414], eax
0x001E5C94: mov dword ptr [rbp + 0x23f8], ebx
0x001E5C9A: lea rdx, [rbp + 0x23d0]
0x001E5CA1: mov rcx, qword ptr [rsi + 0xd0]
0x001E5CA8: call qword ptr [rip + 0x601df2]
0x001E5CAE: mov dword ptr [rsp + 0x20], eax
0x001E5CB2: cmp eax, -1
0x001E5CB5: jne 0x1401e5da0
0x001E5CBB: lea rdx, [rbp + 0x6d0]
0x001E5CC2: mov rcx, qword ptr [rsi + 0xd0]
0x001E5CC9: call qword ptr [rip + 0x601dc9]
0x001E5CCF: test eax, eax
0x001E5CD1: jne 0x1401e602b
0x001E5CD7: mov r8d, r15d
0x001E5CDA: mov r10d, dword ptr [rbp + 0x6d8]
0x001E5CE1: test r10d, r10d
0x001E5CE4: je 0x1401e602b
0x001E5CEA: nop word ptr [rax + rax]
```

#### ref `0x001E77DE`

```asm
0x001E7786: call 0x1403db020
0x001E778B: int3
0x001E778C: cmp rcx, 0x27
0x001E7790: jbe 0x1401e7798
0x001E7792: call 0x1403db020
0x001E7797: int3
0x001E7798: mov rcx, rax
0x001E779B: call 0x1403b20d4
0x001E77A0: jmp 0x1401e89e4
0x001E77A5: cmp byte ptr [rbp + 0x4190], r15b
0x001E77AC: jne 0x1401e89e4
0x001E77B2: xor edx, edx
0x001E77B4: mov r8d, 0x1cf8
0x001E77BA: lea rcx, [rbp + 0x6e0]
0x001E77C1: call 0x1403d3050
0x001E77C6: mov dword ptr [rbp + 0x6e0], 0x31cf8
0x001E77D0: lea rdx, [rbp + 0x6e0]
0x001E77D7: mov rcx, qword ptr [rsi + 0xd0]
0x001E77DE: call qword ptr [rip + 0x6002b4]
0x001E77E4: mov dword ptr [rsp + 0x20], eax
0x001E77E8: test eax, eax
0x001E77EA: jne 0x1401e89e4
0x001E77F0: mov ebx, r15d
0x001E77F3: mov r8d, dword ptr [rbp + 0x6e8]
0x001E77FA: test r8d, r8d
0x001E77FD: je 0x1401e83b4
```

#### ref `0x001E7AA9`

```asm
0x001E7A40: mov qword ptr [rcx + 0x40], rax
0x001E7A44: movups xmm0, xmmword ptr [r10 + 8]
0x001E7A49: movups xmmword ptr [rbp + 0x23fc], xmm0
0x001E7A50: movups xmm1, xmmword ptr [r10 + 0x18]
0x001E7A55: movups xmmword ptr [rbp + 0x240c], xmm1
0x001E7A5C: movsd xmm0, qword ptr [r10 + 0x28]
0x001E7A62: movsd qword ptr [rbp + 0x241c], xmm0
0x001E7A6A: mov eax, dword ptr [r10 + 0x30]
0x001E7A6E: mov dword ptr [rbp + 0x2424], eax
0x001E7A74: mov dword ptr [rbp + 0x2408], ebx
0x001E7A7A: lea rdx, [rbp + 0x23e0]
0x001E7A81: mov rcx, qword ptr [rsi + 0xd0]
0x001E7A88: call qword ptr [rip + 0x600012]
0x001E7A8E: mov dword ptr [rsp + 0x20], eax
0x001E7A92: cmp eax, -1
0x001E7A95: jne 0x1401e7b81
0x001E7A9B: lea rdx, [rbp + 0x6e0]
0x001E7AA2: mov rcx, qword ptr [rsi + 0xd0]
0x001E7AA9: call qword ptr [rip + 0x5fffe9]
0x001E7AAF: test eax, eax
0x001E7AB1: jne 0x1401e7fac
0x001E7AB7: mov r8d, r15d
0x001E7ABA: mov r10d, dword ptr [rbp + 0x6e8]
0x001E7AC1: test r10d, r10d
0x001E7AC4: je 0x1401e7fac
0x001E7ACA: nop word ptr [rax + rax]
```

#### ref `0x001FE5D9`

```asm
0x001FE56F: mov ecx, 0xdcb616c3
0x001FE574: call qword ptr [rip + 0x5e947e]
0x001FE57A: mov ecx, 0x1bd69f49
0x001FE57F: mov qword ptr [rip + 0x5e94ea], rax
0x001FE586: call qword ptr [rip + 0x5e946c]
0x001FE58C: mov ecx, 0xc16c7e2c
0x001FE591: mov qword ptr [rip + 0x5e94e0], rax
0x001FE598: call qword ptr [rip + 0x5e945a]
0x001FE59E: mov ecx, 0x465f9bcf
0x001FE5A3: mov qword ptr [rip + 0x5e94d6], rax
0x001FE5AA: call qword ptr [rip + 0x5e9448]
0x001FE5B0: mov ecx, 0x927da4f6
0x001FE5B5: mov qword ptr [rip + 0x5e94cc], rax
0x001FE5BC: call qword ptr [rip + 0x5e9436]
0x001FE5C2: mov ecx, 0x6ff81213
0x001FE5C7: mov qword ptr [rip + 0x5e94c2], rax
0x001FE5CE: call qword ptr [rip + 0x5e9424]
0x001FE5D4: mov ecx, 0xf4dae6b
0x001FE5D9: mov qword ptr [rip + 0x5e94b8], rax
0x001FE5E0: call qword ptr [rip + 0x5e9412]
0x001FE5E6: mov ecx, 0x843c0256
0x001FE5EB: mov qword ptr [rip + 0x5e94ae], rax
0x001FE5F2: call qword ptr [rip + 0x5e9400]
0x001FE5F8: mov ecx, 0xedcf624e
0x001FE5FD: mov qword ptr [rip + 0x5e94a4], rax
0x001FE604: call qword ptr [rip + 0x5e93ee]
```

## call `0x001E30B8` function slot `0x007E7AC0`

```asm
0x001E3096: mov qword ptr [rbp + 0xd4], rax
0x001E309D: mov qword ptr [rbp + 0xdc], rax
0x001E30A4: mov dword ptr [rbp + 0xe4], eax
0x001E30AA: lea rdx, [rbp + 0xa0]
0x001E30B1: mov rcx, qword ptr [rbx + 0xd0]
0x001E30B8: call qword ptr [rip + 0x604a02]
0x001E30BE: mov dword ptr [rsp + 0x24], eax
0x001E30C2: test eax, eax
0x001E30C4: je 0x1401e3363
```

### refs to global slot `0x007E7AC0`: `5`

#### ref `0x001E3029`

```asm
0x001E2FDC: int3
0x001E2FDD: int3
0x001E2FDE: int3
0x001E2FDF: int3
0x001E2FE0: mov rax, rsp
0x001E2FE3: push rbp
0x001E2FE4: lea rbp, [rax - 0x168]
0x001E2FEB: sub rsp, 0x260
0x001E2FF2: mov qword ptr [rsp + 0x40], 0xfffffffffffffffe
0x001E2FFB: mov qword ptr [rax + 0x10], rbx
0x001E2FFF: mov qword ptr [rax + 0x18], rsi
0x001E3003: mov qword ptr [rax + 0x20], rdi
0x001E3007: mov rax, qword ptr [rip + 0x5f38e2]
0x001E300E: xor rax, rsp
0x001E3011: mov qword ptr [rbp + 0x150], rax
0x001E3018: mov rbx, rcx
0x001E301B: cmp qword ptr [rcx + 0xd0], 0
0x001E3023: je 0x1401e3e0c
0x001E3029: cmp qword ptr [rip + 0x604a8f], 0
0x001E3031: je 0x1401e3e04
0x001E3037: cmp qword ptr [rip + 0x604a89], 0
0x001E303F: je 0x1401e3e04
0x001E3045: cmp qword ptr [rip + 0x604a6b], 0
0x001E304D: je 0x1401e3e04
0x001E3053: xor esi, esi
0x001E3055: mov edi, esi
```

#### ref `0x001E30B8`

```asm
0x001E304D: je 0x1401e3e04
0x001E3053: xor esi, esi
0x001E3055: mov edi, esi
0x001E3057: mov dword ptr [rsp + 0x20], esi
0x001E305B: call 0x1401ed0b0
0x001E3060: mov dword ptr [rbp + 0xa0], 0x10048
0x001E306A: xor eax, eax
0x001E306C: mov qword ptr [rbp + 0xa4], rax
0x001E3073: mov qword ptr [rbp + 0xac], rax
0x001E307A: mov qword ptr [rbp + 0xb4], rax
0x001E3081: mov qword ptr [rbp + 0xbc], rax
0x001E3088: mov qword ptr [rbp + 0xc4], rax
0x001E308F: mov qword ptr [rbp + 0xcc], rax
0x001E3096: mov qword ptr [rbp + 0xd4], rax
0x001E309D: mov qword ptr [rbp + 0xdc], rax
0x001E30A4: mov dword ptr [rbp + 0xe4], eax
0x001E30AA: lea rdx, [rbp + 0xa0]
0x001E30B1: mov rcx, qword ptr [rbx + 0xd0]
0x001E30B8: call qword ptr [rip + 0x604a02]
0x001E30BE: mov dword ptr [rsp + 0x24], eax
0x001E30C2: test eax, eax
0x001E30C4: je 0x1401e3363
0x001E30CA: mov dword ptr [rsp + 0x28], 0x5e6
0x001E30D2: mov dword ptr [rbp + 0x20], 0x1d
0x001E30D9: mov eax, dword ptr [rbp + 0x20]
0x001E30DC: xor eax, 0x4e
```

#### ref `0x001E8A62`

```asm
0x001E8A13: push rsi
0x001E8A14: push rdi
0x001E8A15: push r14
0x001E8A17: lea rbp, [rsp - 0x150]
0x001E8A1F: sub rsp, 0x250
0x001E8A26: mov qword ptr [rsp + 0x40], 0xfffffffffffffffe
0x001E8A2F: mov rax, qword ptr [rip + 0x5edeba]
0x001E8A36: xor rax, rsp
0x001E8A39: mov qword ptr [rbp + 0x140], rax
0x001E8A40: mov esi, r8d
0x001E8A43: mov rdi, rcx
0x001E8A46: cmp qword ptr [rcx + 0xd0], 0
0x001E8A4E: jne 0x1401e8a62
0x001E8A50: xor eax, eax
0x001E8A52: mov ecx, 2
0x001E8A57: test r8d, r8d
0x001E8A5A: cmovg eax, ecx
0x001E8A5D: jmp 0x1401e9913
0x001E8A62: cmp qword ptr [rip + 0x5ff056], 0
0x001E8A6A: je 0x1401e98f8
0x001E8A70: cmp qword ptr [rip + 0x5ff050], 0
0x001E8A78: je 0x1401e98f8
0x001E8A7E: cmp qword ptr [rip + 0x5ff032], 0
0x001E8A86: je 0x1401e98f8
0x001E8A8C: xor eax, eax
0x001E8A8E: mov dword ptr [rsp + 0x24], eax
```

#### ref `0x001E8B20`

```asm
0x001E8AC3: lea rcx, [rsp + 0x20]
0x001E8AC8: cmp edx, dword ptr [rax]
0x001E8ACA: cmovl rcx, rax
0x001E8ACE: mov ebx, dword ptr [rcx]
0x001E8AD0: mov dword ptr [rsp + 0x20], ebx
0x001E8AD4: mov dword ptr [rbp + 0x70], 0x10048
0x001E8ADB: xor eax, eax
0x001E8ADD: mov qword ptr [rbp + 0x74], rax
0x001E8AE1: mov qword ptr [rbp + 0x7c], rax
0x001E8AE5: mov qword ptr [rbp + 0x84], rax
0x001E8AEC: mov qword ptr [rbp + 0x8c], rax
0x001E8AF3: mov qword ptr [rbp + 0x94], rax
0x001E8AFA: mov qword ptr [rbp + 0x9c], rax
0x001E8B01: mov qword ptr [rbp + 0xa4], rax
0x001E8B08: mov qword ptr [rbp + 0xac], rax
0x001E8B0F: mov dword ptr [rbp + 0xb4], eax
0x001E8B15: lea rdx, [rbp + 0x70]
0x001E8B19: mov rcx, qword ptr [rdi + 0xd0]
0x001E8B20: call qword ptr [rip + 0x5fef9a]
0x001E8B26: mov dword ptr [rsp + 0x28], eax
0x001E8B2A: test eax, eax
0x001E8B2C: je 0x1401e8d55
0x001E8B32: mov dword ptr [rsp + 0x2c], 0x5b5
0x001E8B3A: mov dword ptr [rbp + 0x40], 0x18
0x001E8B41: mov dword ptr [rbp + 0x44], 0x38
0x001E8B48: mov eax, dword ptr [rbp + 0x44]
```

#### ref `0x001FE633`

```asm
0x001FE5C7: mov qword ptr [rip + 0x5e94c2], rax
0x001FE5CE: call qword ptr [rip + 0x5e9424]
0x001FE5D4: mov ecx, 0xf4dae6b
0x001FE5D9: mov qword ptr [rip + 0x5e94b8], rax
0x001FE5E0: call qword ptr [rip + 0x5e9412]
0x001FE5E6: mov ecx, 0x843c0256
0x001FE5EB: mov qword ptr [rip + 0x5e94ae], rax
0x001FE5F2: call qword ptr [rip + 0x5e9400]
0x001FE5F8: mov ecx, 0xedcf624e
0x001FE5FD: mov qword ptr [rip + 0x5e94a4], rax
0x001FE604: call qword ptr [rip + 0x5e93ee]
0x001FE60A: mov ecx, 0x34206d86
0x001FE60F: mov qword ptr [rip + 0x5e949a], rax
0x001FE616: call qword ptr [rip + 0x5e93dc]
0x001FE61C: mov ecx, 0x70916171
0x001FE621: mov qword ptr [rip + 0x5e9490], rax
0x001FE628: call qword ptr [rip + 0x5e93ca]
0x001FE62E: mov ecx, 0xad95f5ed
0x001FE633: mov qword ptr [rip + 0x5e9486], rax
0x001FE63A: call qword ptr [rip + 0x5e93b8]
0x001FE640: mov ecx, 0xfb85b01e
0x001FE645: mov qword ptr [rip + 0x5e947c], rax
0x001FE64C: call qword ptr [rip + 0x5e93a6]
0x001FE652: mov ecx, 0x35aed5e8
0x001FE657: mov qword ptr [rip + 0x5e9472], rax
0x001FE65E: call qword ptr [rip + 0x5e9394]
```

## call `0x001E3393` function slot `0x007E7AC8`

```asm
0x001E3373: mov esi, dword ptr [rbp + 0xb0]
0x001E3379: mov eax, dword ptr [rbx + 0x140]
0x001E337F: mov dword ptr [rbp + 0xb0], eax
0x001E3385: lea rdx, [rbp + 0xa0]
0x001E338C: mov rcx, qword ptr [rbx + 0xd0]
0x001E3393: call qword ptr [rip + 0x60472f]
0x001E3399: mov edi, eax
0x001E339B: mov dword ptr [rsp + 0x20], eax
0x001E339F: test eax, eax
```

### refs to global slot `0x007E7AC8`: `5`

#### ref `0x001E3037`

```asm
0x001E2FDE: int3
0x001E2FDF: int3
0x001E2FE0: mov rax, rsp
0x001E2FE3: push rbp
0x001E2FE4: lea rbp, [rax - 0x168]
0x001E2FEB: sub rsp, 0x260
0x001E2FF2: mov qword ptr [rsp + 0x40], 0xfffffffffffffffe
0x001E2FFB: mov qword ptr [rax + 0x10], rbx
0x001E2FFF: mov qword ptr [rax + 0x18], rsi
0x001E3003: mov qword ptr [rax + 0x20], rdi
0x001E3007: mov rax, qword ptr [rip + 0x5f38e2]
0x001E300E: xor rax, rsp
0x001E3011: mov qword ptr [rbp + 0x150], rax
0x001E3018: mov rbx, rcx
0x001E301B: cmp qword ptr [rcx + 0xd0], 0
0x001E3023: je 0x1401e3e0c
0x001E3029: cmp qword ptr [rip + 0x604a8f], 0
0x001E3031: je 0x1401e3e04
0x001E3037: cmp qword ptr [rip + 0x604a89], 0
0x001E303F: je 0x1401e3e04
0x001E3045: cmp qword ptr [rip + 0x604a6b], 0
0x001E304D: je 0x1401e3e04
0x001E3053: xor esi, esi
0x001E3055: mov edi, esi
0x001E3057: mov dword ptr [rsp + 0x20], esi
0x001E305B: call 0x1401ed0b0
```

#### ref `0x001E3393`

```asm
0x001E3337: call 0x1403db020
0x001E333C: int3
0x001E333D: mov rcx, rax
0x001E3340: call 0x1403b20d4
0x001E3345: mov qword ptr [rbp + 0x90], 0xf
0x001E3350: mov qword ptr [rbp + 0x88], rsi
0x001E3357: mov byte ptr [rbp + 0x78], 0
0x001E335B: mov edi, dword ptr [rsp + 0x24]
0x001E335F: mov dword ptr [rsp + 0x20], edi
0x001E3363: test edi, edi
0x001E3365: jne 0x1401e351f
0x001E336B: cmp dword ptr [rbp + 0xa4], edi
0x001E3371: jbe 0x1401e33a7
0x001E3373: mov esi, dword ptr [rbp + 0xb0]
0x001E3379: mov eax, dword ptr [rbx + 0x140]
0x001E337F: mov dword ptr [rbp + 0xb0], eax
0x001E3385: lea rdx, [rbp + 0xa0]
0x001E338C: mov rcx, qword ptr [rbx + 0xd0]
0x001E3393: call qword ptr [rip + 0x60472f]
0x001E3399: mov edi, eax
0x001E339B: mov dword ptr [rsp + 0x20], eax
0x001E339F: test eax, eax
0x001E33A1: jne 0x1401e351f
0x001E33A7: mov eax, 0x10624dd3
0x001E33AC: imul dword ptr [rbx + 0x140]
0x001E33B2: sar edx, 6
```

#### ref `0x001E8A70`

```asm
0x001E8A15: push r14
0x001E8A17: lea rbp, [rsp - 0x150]
0x001E8A1F: sub rsp, 0x250
0x001E8A26: mov qword ptr [rsp + 0x40], 0xfffffffffffffffe
0x001E8A2F: mov rax, qword ptr [rip + 0x5edeba]
0x001E8A36: xor rax, rsp
0x001E8A39: mov qword ptr [rbp + 0x140], rax
0x001E8A40: mov esi, r8d
0x001E8A43: mov rdi, rcx
0x001E8A46: cmp qword ptr [rcx + 0xd0], 0
0x001E8A4E: jne 0x1401e8a62
0x001E8A50: xor eax, eax
0x001E8A52: mov ecx, 2
0x001E8A57: test r8d, r8d
0x001E8A5A: cmovg eax, ecx
0x001E8A5D: jmp 0x1401e9913
0x001E8A62: cmp qword ptr [rip + 0x5ff056], 0
0x001E8A6A: je 0x1401e98f8
0x001E8A70: cmp qword ptr [rip + 0x5ff050], 0
0x001E8A78: je 0x1401e98f8
0x001E8A7E: cmp qword ptr [rip + 0x5ff032], 0
0x001E8A86: je 0x1401e98f8
0x001E8A8C: xor eax, eax
0x001E8A8E: mov dword ptr [rsp + 0x24], eax
0x001E8A92: lea eax, [rdx + 0x64]
0x001E8A95: imul ebx, eax, 0x3e8
```

#### ref `0x001E8D8C`

```asm
0x001E8D42: call 0x1403db020
0x001E8D47: int3
0x001E8D48: mov rcx, rax
0x001E8D4B: call 0x1403b20d4
0x001E8D50: jmp 0x1401e98f8
0x001E8D55: cmp dword ptr [rbp + 0x74], 0
0x001E8D59: jbe 0x1401e98f8
0x001E8D5F: mov eax, ebx
0x001E8D61: mov r14d, dword ptr [rbp + 0x80]
0x001E8D68: sub eax, r14d
0x001E8D6B: cdq
0x001E8D6C: xor eax, edx
0x001E8D6E: sub eax, edx
0x001E8D70: cmp eax, 0x3e8
0x001E8D75: jl 0x1401e98f8
0x001E8D7B: mov dword ptr [rbp + 0x80], ebx
0x001E8D81: lea rdx, [rbp + 0x70]
0x001E8D85: mov rcx, qword ptr [rdi + 0xd0]
0x001E8D8C: call qword ptr [rip + 0x5fed36]
0x001E8D92: mov dword ptr [rsp + 0x24], eax
0x001E8D96: test eax, eax
0x001E8D98: jne 0x1401e8f4c
0x001E8D9E: mov eax, 0x10624dd3
0x001E8DA3: imul ebx
0x001E8DA5: sar edx, 6
0x001E8DA8: mov eax, edx
```

#### ref `0x001FE645`

```asm
0x001FE5D9: mov qword ptr [rip + 0x5e94b8], rax
0x001FE5E0: call qword ptr [rip + 0x5e9412]
0x001FE5E6: mov ecx, 0x843c0256
0x001FE5EB: mov qword ptr [rip + 0x5e94ae], rax
0x001FE5F2: call qword ptr [rip + 0x5e9400]
0x001FE5F8: mov ecx, 0xedcf624e
0x001FE5FD: mov qword ptr [rip + 0x5e94a4], rax
0x001FE604: call qword ptr [rip + 0x5e93ee]
0x001FE60A: mov ecx, 0x34206d86
0x001FE60F: mov qword ptr [rip + 0x5e949a], rax
0x001FE616: call qword ptr [rip + 0x5e93dc]
0x001FE61C: mov ecx, 0x70916171
0x001FE621: mov qword ptr [rip + 0x5e9490], rax
0x001FE628: call qword ptr [rip + 0x5e93ca]
0x001FE62E: mov ecx, 0xad95f5ed
0x001FE633: mov qword ptr [rip + 0x5e9486], rax
0x001FE63A: call qword ptr [rip + 0x5e93b8]
0x001FE640: mov ecx, 0xfb85b01e
0x001FE645: mov qword ptr [rip + 0x5e947c], rax
0x001FE64C: call qword ptr [rip + 0x5e93a6]
0x001FE652: mov ecx, 0x35aed5e8
0x001FE657: mov qword ptr [rip + 0x5e9472], rax
0x001FE65E: call qword ptr [rip + 0x5e9394]
0x001FE664: mov ecx, 0x814b209f
0x001FE669: mov qword ptr [rip + 0x5e9468], rax
0x001FE670: call qword ptr [rip + 0x5e9382]
```

## call `0x001E3EC8` function slot `0x007E7A50`

```asm
0x001E3EA4: lea rcx, [rbp + 0x1a0]
0x001E3EAB: call 0x1403d3050
0x001E3EB0: mov dword ptr [rbp + 0x1a0], 0x20068
0x001E3EBA: lea rdx, [rbp + 0x1a0]
0x001E3EC1: mov rcx, qword ptr [rdi + 0xd0]
0x001E3EC8: call qword ptr [rip + 0x603b82]
0x001E3ECE: mov dword ptr [rsp + 0x2c], eax
0x001E3ED2: test eax, eax
0x001E3ED4: je 0x1401e41b1
```

### refs to global slot `0x007E7A50`: `3`

#### ref `0x001E3EC8`

```asm
0x001E3E67: mov rax, qword ptr [rip + 0x5f2a82]
0x001E3E6E: xor rax, rsp
0x001E3E71: mov qword ptr [rbp + 0x210], rax
0x001E3E78: mov rdi, rcx
0x001E3E7B: cmp byte ptr [rcx + 0xe4], 0
0x001E3E82: je 0x1401e512e
0x001E3E88: cmp qword ptr [rcx + 0xd0], 0
0x001E3E90: je 0x1401e512e
0x001E3E96: xor ebx, ebx
0x001E3E98: mov esi, ebx
0x001E3E9A: mov dword ptr [rsp + 0x20], ebx
0x001E3E9E: xor edx, edx
0x001E3EA0: lea r8d, [rbx + 0x68]
0x001E3EA4: lea rcx, [rbp + 0x1a0]
0x001E3EAB: call 0x1403d3050
0x001E3EB0: mov dword ptr [rbp + 0x1a0], 0x20068
0x001E3EBA: lea rdx, [rbp + 0x1a0]
0x001E3EC1: mov rcx, qword ptr [rdi + 0xd0]
0x001E3EC8: call qword ptr [rip + 0x603b82]
0x001E3ECE: mov dword ptr [rsp + 0x2c], eax
0x001E3ED2: test eax, eax
0x001E3ED4: je 0x1401e41b1
0x001E3EDA: mov dword ptr [rsp + 0x34], 0x55a
0x001E3EE2: mov dword ptr [rbp + 0x60], 0x7f
0x001E3EE9: mov eax, dword ptr [rbp + 0x60]
0x001E3EEC: xor eax, 0x4e
```

#### ref `0x001E99B4`

```asm
0x001E9960: mov qword ptr [rbp + 0x200], rax
0x001E9967: mov ebx, edx
0x001E9969: mov rdi, rcx
0x001E996C: mov dword ptr [rsp + 0x28], edx
0x001E9970: xor r14b, r14b
0x001E9973: cmp qword ptr [rcx + 0xd0], 0
0x001E997B: jne 0x1401e9984
0x001E997D: xor al, al
0x001E997F: jmp 0x1401eae3d
0x001E9984: xor esi, esi
0x001E9986: mov dword ptr [rsp + 0x20], esi
0x001E998A: xor edx, edx
0x001E998C: lea r8d, [rsi + 0x68]
0x001E9990: lea rcx, [rbp + 0x130]
0x001E9997: call 0x1403d3050
0x001E999C: mov dword ptr [rbp + 0x130], 0x20068
0x001E99A6: lea rdx, [rbp + 0x130]
0x001E99AD: mov rcx, qword ptr [rdi + 0xd0]
0x001E99B4: call qword ptr [rip + 0x5fe096]
0x001E99BA: mov dword ptr [rsp + 0x24], eax
0x001E99BE: test eax, eax
0x001E99C0: je 0x1401e9c27
0x001E99C6: mov dword ptr [rsp + 0x3c], 0x518
0x001E99CE: mov dword ptr [rbp + 0x58], 0x25
0x001E99D5: mov dword ptr [rbp + 0x5c], 0x46
0x001E99DC: mov eax, dword ptr [rbp + 0x5c]
```

#### ref `0x001FE50E`

```asm
0x001FE4AB: mov qword ptr [rip + 0x5e957e], rax
0x001FE4B2: test rax, rax
0x001FE4B5: je 0x1401fe296
0x001FE4BB: mov ecx, 0xda141340
0x001FE4C0: call qword ptr [rip + 0x5e9532]
0x001FE4C6: mov qword ptr [rip + 0x5e956b], rax
0x001FE4CD: test rax, rax
0x001FE4D0: je 0x1401fe296
0x001FE4D6: mov ecx, 0x891fa0ae
0x001FE4DB: call qword ptr [rip + 0x5e9517]
0x001FE4E1: mov qword ptr [rip + 0x5e9558], rax
0x001FE4E8: test rax, rax
0x001FE4EB: je 0x1401fe296
0x001FE4F1: mov ecx, 0x8f6ed0fb
0x001FE4F6: call qword ptr [rip + 0x5e94fc]
0x001FE4FC: mov ecx, 0xd258bb5
0x001FE501: mov qword ptr [rip + 0x5e9540], rax
0x001FE508: call qword ptr [rip + 0x5e94ea]
0x001FE50E: mov qword ptr [rip + 0x5e953b], rax
0x001FE515: test rax, rax
0x001FE518: je 0x1401fe296
0x001FE51E: mov ecx, 0xe9c425a1
0x001FE523: call qword ptr [rip + 0x5e94cf]
0x001FE529: mov qword ptr [rip + 0x5e9528], rax
0x001FE530: test rax, rax
0x001FE533: je 0x1401fe296
```

## call `0x001E425E` function slot `0x007E7A58`

```asm
0x001E4238: mov qword ptr [rbp + 0xe8], rax
0x001E423F: mov qword ptr [rbp + 0xf0], rax
0x001E4246: mov dword ptr [rbp + 0xc0], 0x20038
0x001E4250: lea rdx, [rbp + 0xc0]
0x001E4257: mov rcx, qword ptr [rdi + 0xd0]
0x001E425E: call qword ptr [rip + 0x6037f4]
0x001E4264: mov dword ptr [rsp + 0x3c], eax
0x001E4268: test eax, eax
0x001E426A: je 0x1401e45e4
```

### refs to global slot `0x007E7A58`: `3`

#### ref `0x001E425E`

```asm
0x001E41FA: cmp eax, 0x37
0x001E41FD: cmovle rcx, rdx
0x001E4201: lea rax, [rsp + 0x38]
0x001E4206: cmp dword ptr [rcx], 0x5a
0x001E4209: cmovl rax, rcx
0x001E420D: mov ebx, dword ptr [rax]
0x001E420F: mov dword ptr [rsp + 0x24], ebx
0x001E4213: xor eax, eax
0x001E4215: mov qword ptr [rbp + 0xc0], rax
0x001E421C: mov qword ptr [rbp + 0xc8], rax
0x001E4223: mov qword ptr [rbp + 0xd0], rax
0x001E422A: mov qword ptr [rbp + 0xd8], rax
0x001E4231: mov qword ptr [rbp + 0xe0], rax
0x001E4238: mov qword ptr [rbp + 0xe8], rax
0x001E423F: mov qword ptr [rbp + 0xf0], rax
0x001E4246: mov dword ptr [rbp + 0xc0], 0x20038
0x001E4250: lea rdx, [rbp + 0xc0]
0x001E4257: mov rcx, qword ptr [rdi + 0xd0]
0x001E425E: call qword ptr [rip + 0x6037f4]
0x001E4264: mov dword ptr [rsp + 0x3c], eax
0x001E4268: test eax, eax
0x001E426A: je 0x1401e45e4
0x001E4270: mov dword ptr [rsp + 0x40], 0x568
0x001E4278: mov dword ptr [rbp + 0x90], 8
0x001E4282: mov eax, dword ptr [rbp + 0x90]
0x001E4288: xor eax, 0x4e
```

#### ref `0x001E9CD3`

```asm
0x001E9C71: cmp eax, ebx
0x001E9C73: cmovge rcx, r8
0x001E9C77: lea rax, [rsp + 0x40]
0x001E9C7C: cmp dword ptr [rcx], edx
0x001E9C7E: cmovl rax, rcx
0x001E9C82: mov ebx, dword ptr [rax]
0x001E9C84: mov dword ptr [rsp + 0x34], ebx
0x001E9C88: xor eax, eax
0x001E9C8A: mov qword ptr [rbp + 0xb8], rax
0x001E9C91: mov qword ptr [rbp + 0xc0], rax
0x001E9C98: mov qword ptr [rbp + 0xc8], rax
0x001E9C9F: mov qword ptr [rbp + 0xd0], rax
0x001E9CA6: mov qword ptr [rbp + 0xd8], rax
0x001E9CAD: mov qword ptr [rbp + 0xe0], rax
0x001E9CB4: mov qword ptr [rbp + 0xe8], rax
0x001E9CBB: mov dword ptr [rbp + 0xb8], 0x20038
0x001E9CC5: lea rdx, [rbp + 0xb8]
0x001E9CCC: mov rcx, qword ptr [rdi + 0xd0]
0x001E9CD3: call qword ptr [rip + 0x5fdd7f]
0x001E9CD9: mov dword ptr [rsp + 0x44], eax
0x001E9CDD: test eax, eax
0x001E9CDF: je 0x1401e9ff5
0x001E9CE5: mov dword ptr [rsp + 0x48], 0x528
0x001E9CED: mov dword ptr [rbp + 0x88], 0x1c
0x001E9CF7: mov dword ptr [rbp + 0x8c], 0x63
0x001E9D01: mov eax, dword ptr [rbp + 0x8c]
```

#### ref `0x001FE529`

```asm
0x001FE4C6: mov qword ptr [rip + 0x5e956b], rax
0x001FE4CD: test rax, rax
0x001FE4D0: je 0x1401fe296
0x001FE4D6: mov ecx, 0x891fa0ae
0x001FE4DB: call qword ptr [rip + 0x5e9517]
0x001FE4E1: mov qword ptr [rip + 0x5e9558], rax
0x001FE4E8: test rax, rax
0x001FE4EB: je 0x1401fe296
0x001FE4F1: mov ecx, 0x8f6ed0fb
0x001FE4F6: call qword ptr [rip + 0x5e94fc]
0x001FE4FC: mov ecx, 0xd258bb5
0x001FE501: mov qword ptr [rip + 0x5e9540], rax
0x001FE508: call qword ptr [rip + 0x5e94ea]
0x001FE50E: mov qword ptr [rip + 0x5e953b], rax
0x001FE515: test rax, rax
0x001FE518: je 0x1401fe296
0x001FE51E: mov ecx, 0xe9c425a1
0x001FE523: call qword ptr [rip + 0x5e94cf]
0x001FE529: mov qword ptr [rip + 0x5e9528], rax
0x001FE530: test rax, rax
0x001FE533: je 0x1401fe296
0x001FE539: mov ecx, 0x34c0b13d
0x001FE53E: call qword ptr [rip + 0x5e94b4]
0x001FE544: mov qword ptr [rip + 0x5e9515], rax
0x001FE54B: test rax, rax
0x001FE54E: je 0x1401fe296
```

## call `0x001E4624` function slot `0x007E7A60`

```asm
0x001E4607: mov dword ptr [rbp + 0xcc], ebx
0x001E460D: or ecx, 1
0x001E4610: mov dword ptr [rbp + 0xd0], ecx
0x001E4616: lea rdx, [rbp + 0xc0]
0x001E461D: mov rcx, qword ptr [rdi + 0xd0]
0x001E4624: call qword ptr [rip + 0x603436]
0x001E462A: mov dword ptr [rsp + 0x20], eax
0x001E462E: test eax, eax
0x001E4630: jne 0x1401e47f1
```

### refs to global slot `0x007E7A60`: `3`

#### ref `0x001E4624`

```asm
0x001E45D6: int3
0x001E45D7: mov rcx, rax
0x001E45DA: call 0x1403b20d4
0x001E45DF: jmp 0x1401e512e
0x001E45E4: mov eax, dword ptr [rbp + 0xcc]
0x001E45EA: shr eax, 8
0x001E45ED: mov dword ptr [rsp + 0x30], eax
0x001E45F1: mov ecx, dword ptr [rbp + 0xd0]
0x001E45F7: cmp eax, ebx
0x001E45F9: jne 0x1401e4604
0x001E45FB: test cl, 1
0x001E45FE: jne 0x1401e512e
0x001E4604: shl ebx, 8
0x001E4607: mov dword ptr [rbp + 0xcc], ebx
0x001E460D: or ecx, 1
0x001E4610: mov dword ptr [rbp + 0xd0], ecx
0x001E4616: lea rdx, [rbp + 0xc0]
0x001E461D: mov rcx, qword ptr [rdi + 0xd0]
0x001E4624: call qword ptr [rip + 0x603436]
0x001E462A: mov dword ptr [rsp + 0x20], eax
0x001E462E: test eax, eax
0x001E4630: jne 0x1401e47f1
0x001E4636: mov dword ptr [rbp - 0x10], 0x3e
0x001E463D: mov eax, dword ptr [rbp - 0x10]
0x001E4640: xor eax, 0x7b
0x001E4643: inc eax
```

#### ref `0x001EA039`

```asm
0x001E9FEB: call 0x1403b20d4
0x001E9FF0: jmp 0x1401eae32
0x001E9FF5: mov eax, dword ptr [rbp + 0xc4]
0x001E9FFB: shr eax, 8
0x001E9FFE: mov dword ptr [rsp + 0x30], eax
0x001EA002: mov ecx, dword ptr [rbp + 0xc8]
0x001EA008: cmp eax, ebx
0x001EA00A: jne 0x1401ea019
0x001EA00C: test cl, 1
0x001EA00F: je 0x1401ea019
0x001EA011: mov r14b, 1
0x001EA014: jmp 0x1401eae32
0x001EA019: shl ebx, 8
0x001EA01C: mov dword ptr [rbp + 0xc4], ebx
0x001EA022: or ecx, 1
0x001EA025: mov dword ptr [rbp + 0xc8], ecx
0x001EA02B: lea rdx, [rbp + 0xb8]
0x001EA032: mov rcx, qword ptr [rdi + 0xd0]
0x001EA039: call qword ptr [rip + 0x5fda21]
0x001EA03F: mov dword ptr [rsp + 0x20], eax
0x001EA043: test eax, eax
0x001EA045: jne 0x1401ea20e
0x001EA04B: mov r14b, 1
0x001EA04E: mov dword ptr [rbp + 0x30], 0xffffff83
0x001EA055: mov eax, dword ptr [rbp + 0x30]
0x001EA058: xor eax, 0x7b
```

#### ref `0x001FE544`

```asm
0x001FE4E1: mov qword ptr [rip + 0x5e9558], rax
0x001FE4E8: test rax, rax
0x001FE4EB: je 0x1401fe296
0x001FE4F1: mov ecx, 0x8f6ed0fb
0x001FE4F6: call qword ptr [rip + 0x5e94fc]
0x001FE4FC: mov ecx, 0xd258bb5
0x001FE501: mov qword ptr [rip + 0x5e9540], rax
0x001FE508: call qword ptr [rip + 0x5e94ea]
0x001FE50E: mov qword ptr [rip + 0x5e953b], rax
0x001FE515: test rax, rax
0x001FE518: je 0x1401fe296
0x001FE51E: mov ecx, 0xe9c425a1
0x001FE523: call qword ptr [rip + 0x5e94cf]
0x001FE529: mov qword ptr [rip + 0x5e9528], rax
0x001FE530: test rax, rax
0x001FE533: je 0x1401fe296
0x001FE539: mov ecx, 0x34c0b13d
0x001FE53E: call qword ptr [rip + 0x5e94b4]
0x001FE544: mov qword ptr [rip + 0x5e9515], rax
0x001FE54B: test rax, rax
0x001FE54E: je 0x1401fe296
0x001FE554: mov ecx, 0xe3640a56
0x001FE559: call qword ptr [rip + 0x5e9499]
0x001FE55F: mov qword ptr [rip + 0x5e9502], rax
0x001FE566: test rax, rax
0x001FE569: je 0x1401fe296
```

## call `0x001E59FD` function slot `0x007E7A98`

```asm
0x001E59D9: lea rcx, [rbp + 0x6d0]
0x001E59E0: call 0x1403d3050
0x001E59E5: mov dword ptr [rbp + 0x6d0], 0x31cf8
0x001E59EF: lea rdx, [rbp + 0x6d0]
0x001E59F6: mov rcx, qword ptr [rsi + 0xd0]
0x001E59FD: call qword ptr [rip + 0x602095]
0x001E5A03: mov dword ptr [rsp + 0x20], eax
0x001E5A07: test eax, eax
0x001E5A09: jne 0x1401e6c57
```

### refs to global slot `0x007E7A98`: `9`

#### ref `0x001E0F3F`

```asm
0x001E0ED7: sub rsp, rax
0x001E0EDA: mov qword ptr [rsp + 0x70], 0xfffffffffffffffe
0x001E0EE3: mov qword ptr [rsp + 0x4058], rbx
0x001E0EEB: mov qword ptr [rsp + 0x4060], rsi
0x001E0EF3: mov rax, qword ptr [rip + 0x5f59f6]
0x001E0EFA: xor rax, rsp
0x001E0EFD: mov qword ptr [rbp + 0x3f20], rax
0x001E0F04: mov rsi, rcx
0x001E0F07: mov rbx, qword ptr [rcx + 0xd0]
0x001E0F0E: test rbx, rbx
0x001E0F11: je 0x1401e1f3e
0x001E0F17: xor edx, edx
0x001E0F19: mov r8d, 0x1cf8
0x001E0F1F: lea rcx, [rbp + 0x4d0]
0x001E0F26: call 0x1403d3050
0x001E0F2B: mov dword ptr [rbp + 0x4d0], 0x31cf8
0x001E0F35: lea rdx, [rbp + 0x4d0]
0x001E0F3C: mov rcx, rbx
0x001E0F3F: call qword ptr [rip + 0x606b53]
0x001E0F45: mov dword ptr [rsp + 0x20], eax
0x001E0F49: test eax, eax
0x001E0F4B: jne 0x1401e1f3e
0x001E0F51: xor r14d, r14d
0x001E0F54: mov ebx, r14d
0x001E0F57: mov r8d, dword ptr [rbp + 0x4d8]
0x001E0F5E: test r8d, r8d
```

#### ref `0x001E11BA`

```asm
0x001E1150: mov qword ptr [rcx + 0x40], rax
0x001E1154: movups xmm0, xmmword ptr [r9 + 8]
0x001E1159: movups xmmword ptr [rbp + 0x21ec], xmm0
0x001E1160: movups xmm1, xmmword ptr [r9 + 0x18]
0x001E1165: movups xmmword ptr [rbp + 0x21fc], xmm1
0x001E116C: movsd xmm0, qword ptr [r9 + 0x28]
0x001E1172: movsd qword ptr [rbp + 0x220c], xmm0
0x001E117A: mov eax, dword ptr [r9 + 0x30]
0x001E117E: mov dword ptr [rbp + 0x2214], eax
0x001E1184: mov dword ptr [rbp + 0x21f8], r14d
0x001E118B: lea rdx, [rbp + 0x21d0]
0x001E1192: mov rcx, qword ptr [rsi + 0xd0]
0x001E1199: call qword ptr [rip + 0x606901]
0x001E119F: mov dword ptr [rsp + 0x20], eax
0x001E11A3: cmp eax, -1
0x001E11A6: jne 0x1401e128f
0x001E11AC: lea rdx, [rbp + 0x4d0]
0x001E11B3: mov rcx, qword ptr [rsi + 0xd0]
0x001E11BA: call qword ptr [rip + 0x6068d8]
0x001E11C0: test eax, eax
0x001E11C2: jne 0x1401e1515
0x001E11C8: mov edx, r14d
0x001E11CB: mov r10d, dword ptr [rbp + 0x4d8]
0x001E11D2: test r10d, r10d
0x001E11D5: je 0x1401e1515
0x001E11DB: nop dword ptr [rax + rax]
```

#### ref `0x001E1FEF`

```asm
0x001E1F87: sub rsp, rax
0x001E1F8A: mov qword ptr [rsp + 0x70], 0xfffffffffffffffe
0x001E1F93: mov qword ptr [rsp + 0x4068], rbx
0x001E1F9B: mov qword ptr [rsp + 0x4070], rsi
0x001E1FA3: mov rax, qword ptr [rip + 0x5f4946]
0x001E1FAA: xor rax, rsp
0x001E1FAD: mov qword ptr [rbp + 0x3f30], rax
0x001E1FB4: mov rsi, rcx
0x001E1FB7: mov rbx, qword ptr [rcx + 0xd0]
0x001E1FBE: test rbx, rbx
0x001E1FC1: je 0x1401e2fb2
0x001E1FC7: xor edx, edx
0x001E1FC9: mov r8d, 0x1cf8
0x001E1FCF: lea rcx, [rbp + 0x4e0]
0x001E1FD6: call 0x1403d3050
0x001E1FDB: mov dword ptr [rbp + 0x4e0], 0x31cf8
0x001E1FE5: lea rdx, [rbp + 0x4e0]
0x001E1FEC: mov rcx, rbx
0x001E1FEF: call qword ptr [rip + 0x605aa3]
0x001E1FF5: mov dword ptr [rsp + 0x20], eax
0x001E1FF9: test eax, eax
0x001E1FFB: jne 0x1401e2fb2
0x001E2001: xor r14d, r14d
0x001E2004: mov ebx, r14d
0x001E2007: mov r8d, dword ptr [rbp + 0x4e8]
0x001E200E: test r8d, r8d
```

#### ref `0x001E226A`

```asm
0x001E2200: mov qword ptr [rcx + 0x40], rax
0x001E2204: movups xmm0, xmmword ptr [r9 + 8]
0x001E2209: movups xmmword ptr [rbp + 0x21fc], xmm0
0x001E2210: movups xmm1, xmmword ptr [r9 + 0x18]
0x001E2215: movups xmmword ptr [rbp + 0x220c], xmm1
0x001E221C: movsd xmm0, qword ptr [r9 + 0x28]
0x001E2222: movsd qword ptr [rbp + 0x221c], xmm0
0x001E222A: mov eax, dword ptr [r9 + 0x30]
0x001E222E: mov dword ptr [rbp + 0x2224], eax
0x001E2234: mov dword ptr [rbp + 0x2208], r14d
0x001E223B: lea rdx, [rbp + 0x21e0]
0x001E2242: mov rcx, qword ptr [rsi + 0xd0]
0x001E2249: call qword ptr [rip + 0x605851]
0x001E224F: mov dword ptr [rsp + 0x20], eax
0x001E2253: cmp eax, -1
0x001E2256: jne 0x1401e2340
0x001E225C: lea rdx, [rbp + 0x4e0]
0x001E2263: mov rcx, qword ptr [rsi + 0xd0]
0x001E226A: call qword ptr [rip + 0x605828]
0x001E2270: test eax, eax
0x001E2272: jne 0x1401e2770
0x001E2278: mov edx, r14d
0x001E227B: mov r10d, dword ptr [rbp + 0x4e8]
0x001E2282: test r10d, r10d
0x001E2285: je 0x1401e2770
0x001E228B: nop dword ptr [rax + rax]
```

#### ref `0x001E59FD`

```asm
0x001E59AC: cmp rcx, 8
0x001E59B0: jae 0x1401e59b8
0x001E59B2: call 0x1403db020
0x001E59B7: int3
0x001E59B8: cmp rcx, 0x27
0x001E59BC: jbe 0x1401e59c4
0x001E59BE: call 0x1403db020
0x001E59C3: int3
0x001E59C4: mov rcx, rax
0x001E59C7: call 0x1403b20d4
0x001E59CC: jmp 0x1401e6c57
0x001E59D1: xor edx, edx
0x001E59D3: mov r8d, 0x1cf8
0x001E59D9: lea rcx, [rbp + 0x6d0]
0x001E59E0: call 0x1403d3050
0x001E59E5: mov dword ptr [rbp + 0x6d0], 0x31cf8
0x001E59EF: lea rdx, [rbp + 0x6d0]
0x001E59F6: mov rcx, qword ptr [rsi + 0xd0]
0x001E59FD: call qword ptr [rip + 0x602095]
0x001E5A03: mov dword ptr [rsp + 0x20], eax
0x001E5A07: test eax, eax
0x001E5A09: jne 0x1401e6c57
0x001E5A0F: mov ebx, r15d
0x001E5A12: mov r8d, dword ptr [rbp + 0x6d8]
0x001E5A19: test r8d, r8d
0x001E5A1C: je 0x1401e6627
```

#### ref `0x001E5CC9`

```asm
0x001E5C60: mov qword ptr [rcx + 0x40], rax
0x001E5C64: movups xmm0, xmmword ptr [r10 + 8]
0x001E5C69: movups xmmword ptr [rbp + 0x23ec], xmm0
0x001E5C70: movups xmm1, xmmword ptr [r10 + 0x18]
0x001E5C75: movups xmmword ptr [rbp + 0x23fc], xmm1
0x001E5C7C: movsd xmm0, qword ptr [r10 + 0x28]
0x001E5C82: movsd qword ptr [rbp + 0x240c], xmm0
0x001E5C8A: mov eax, dword ptr [r10 + 0x30]
0x001E5C8E: mov dword ptr [rbp + 0x2414], eax
0x001E5C94: mov dword ptr [rbp + 0x23f8], ebx
0x001E5C9A: lea rdx, [rbp + 0x23d0]
0x001E5CA1: mov rcx, qword ptr [rsi + 0xd0]
0x001E5CA8: call qword ptr [rip + 0x601df2]
0x001E5CAE: mov dword ptr [rsp + 0x20], eax
0x001E5CB2: cmp eax, -1
0x001E5CB5: jne 0x1401e5da0
0x001E5CBB: lea rdx, [rbp + 0x6d0]
0x001E5CC2: mov rcx, qword ptr [rsi + 0xd0]
0x001E5CC9: call qword ptr [rip + 0x601dc9]
0x001E5CCF: test eax, eax
0x001E5CD1: jne 0x1401e602b
0x001E5CD7: mov r8d, r15d
0x001E5CDA: mov r10d, dword ptr [rbp + 0x6d8]
0x001E5CE1: test r10d, r10d
0x001E5CE4: je 0x1401e602b
0x001E5CEA: nop word ptr [rax + rax]
```

#### ref `0x001E77DE`

```asm
0x001E7786: call 0x1403db020
0x001E778B: int3
0x001E778C: cmp rcx, 0x27
0x001E7790: jbe 0x1401e7798
0x001E7792: call 0x1403db020
0x001E7797: int3
0x001E7798: mov rcx, rax
0x001E779B: call 0x1403b20d4
0x001E77A0: jmp 0x1401e89e4
0x001E77A5: cmp byte ptr [rbp + 0x4190], r15b
0x001E77AC: jne 0x1401e89e4
0x001E77B2: xor edx, edx
0x001E77B4: mov r8d, 0x1cf8
0x001E77BA: lea rcx, [rbp + 0x6e0]
0x001E77C1: call 0x1403d3050
0x001E77C6: mov dword ptr [rbp + 0x6e0], 0x31cf8
0x001E77D0: lea rdx, [rbp + 0x6e0]
0x001E77D7: mov rcx, qword ptr [rsi + 0xd0]
0x001E77DE: call qword ptr [rip + 0x6002b4]
0x001E77E4: mov dword ptr [rsp + 0x20], eax
0x001E77E8: test eax, eax
0x001E77EA: jne 0x1401e89e4
0x001E77F0: mov ebx, r15d
0x001E77F3: mov r8d, dword ptr [rbp + 0x6e8]
0x001E77FA: test r8d, r8d
0x001E77FD: je 0x1401e83b4
```

#### ref `0x001E7AA9`

```asm
0x001E7A40: mov qword ptr [rcx + 0x40], rax
0x001E7A44: movups xmm0, xmmword ptr [r10 + 8]
0x001E7A49: movups xmmword ptr [rbp + 0x23fc], xmm0
0x001E7A50: movups xmm1, xmmword ptr [r10 + 0x18]
0x001E7A55: movups xmmword ptr [rbp + 0x240c], xmm1
0x001E7A5C: movsd xmm0, qword ptr [r10 + 0x28]
0x001E7A62: movsd qword ptr [rbp + 0x241c], xmm0
0x001E7A6A: mov eax, dword ptr [r10 + 0x30]
0x001E7A6E: mov dword ptr [rbp + 0x2424], eax
0x001E7A74: mov dword ptr [rbp + 0x2408], ebx
0x001E7A7A: lea rdx, [rbp + 0x23e0]
0x001E7A81: mov rcx, qword ptr [rsi + 0xd0]
0x001E7A88: call qword ptr [rip + 0x600012]
0x001E7A8E: mov dword ptr [rsp + 0x20], eax
0x001E7A92: cmp eax, -1
0x001E7A95: jne 0x1401e7b81
0x001E7A9B: lea rdx, [rbp + 0x6e0]
0x001E7AA2: mov rcx, qword ptr [rsi + 0xd0]
0x001E7AA9: call qword ptr [rip + 0x5fffe9]
0x001E7AAF: test eax, eax
0x001E7AB1: jne 0x1401e7fac
0x001E7AB7: mov r8d, r15d
0x001E7ABA: mov r10d, dword ptr [rbp + 0x6e8]
0x001E7AC1: test r10d, r10d
0x001E7AC4: je 0x1401e7fac
0x001E7ACA: nop word ptr [rax + rax]
```

#### ref `0x001FE5D9`

```asm
0x001FE56F: mov ecx, 0xdcb616c3
0x001FE574: call qword ptr [rip + 0x5e947e]
0x001FE57A: mov ecx, 0x1bd69f49
0x001FE57F: mov qword ptr [rip + 0x5e94ea], rax
0x001FE586: call qword ptr [rip + 0x5e946c]
0x001FE58C: mov ecx, 0xc16c7e2c
0x001FE591: mov qword ptr [rip + 0x5e94e0], rax
0x001FE598: call qword ptr [rip + 0x5e945a]
0x001FE59E: mov ecx, 0x465f9bcf
0x001FE5A3: mov qword ptr [rip + 0x5e94d6], rax
0x001FE5AA: call qword ptr [rip + 0x5e9448]
0x001FE5B0: mov ecx, 0x927da4f6
0x001FE5B5: mov qword ptr [rip + 0x5e94cc], rax
0x001FE5BC: call qword ptr [rip + 0x5e9436]
0x001FE5C2: mov ecx, 0x6ff81213
0x001FE5C7: mov qword ptr [rip + 0x5e94c2], rax
0x001FE5CE: call qword ptr [rip + 0x5e9424]
0x001FE5D4: mov ecx, 0xf4dae6b
0x001FE5D9: mov qword ptr [rip + 0x5e94b8], rax
0x001FE5E0: call qword ptr [rip + 0x5e9412]
0x001FE5E6: mov ecx, 0x843c0256
0x001FE5EB: mov qword ptr [rip + 0x5e94ae], rax
0x001FE5F2: call qword ptr [rip + 0x5e9400]
0x001FE5F8: mov ecx, 0xedcf624e
0x001FE5FD: mov qword ptr [rip + 0x5e94a4], rax
0x001FE604: call qword ptr [rip + 0x5e93ee]
```

## call `0x001E5CA8` function slot `0x007E7AA0`

```asm
0x001E5C8A: mov eax, dword ptr [r10 + 0x30]
0x001E5C8E: mov dword ptr [rbp + 0x2414], eax
0x001E5C94: mov dword ptr [rbp + 0x23f8], ebx
0x001E5C9A: lea rdx, [rbp + 0x23d0]
0x001E5CA1: mov rcx, qword ptr [rsi + 0xd0]
0x001E5CA8: call qword ptr [rip + 0x601df2]
0x001E5CAE: mov dword ptr [rsp + 0x20], eax
0x001E5CB2: cmp eax, -1
0x001E5CB5: jne 0x1401e5da0
```

### refs to global slot `0x007E7AA0`: `5`

#### ref `0x001E1199`

```asm
0x001E1136: movups xmmword ptr [rcx + 0x10], xmm1
0x001E113A: movups xmm0, xmmword ptr [r8 + 0x20]
0x001E113F: movups xmmword ptr [rcx + 0x20], xmm0
0x001E1143: movups xmm1, xmmword ptr [r8 + 0x30]
0x001E1148: movups xmmword ptr [rcx + 0x30], xmm1
0x001E114C: mov rax, qword ptr [r8 + 0x40]
0x001E1150: mov qword ptr [rcx + 0x40], rax
0x001E1154: movups xmm0, xmmword ptr [r9 + 8]
0x001E1159: movups xmmword ptr [rbp + 0x21ec], xmm0
0x001E1160: movups xmm1, xmmword ptr [r9 + 0x18]
0x001E1165: movups xmmword ptr [rbp + 0x21fc], xmm1
0x001E116C: movsd xmm0, qword ptr [r9 + 0x28]
0x001E1172: movsd qword ptr [rbp + 0x220c], xmm0
0x001E117A: mov eax, dword ptr [r9 + 0x30]
0x001E117E: mov dword ptr [rbp + 0x2214], eax
0x001E1184: mov dword ptr [rbp + 0x21f8], r14d
0x001E118B: lea rdx, [rbp + 0x21d0]
0x001E1192: mov rcx, qword ptr [rsi + 0xd0]
0x001E1199: call qword ptr [rip + 0x606901]
0x001E119F: mov dword ptr [rsp + 0x20], eax
0x001E11A3: cmp eax, -1
0x001E11A6: jne 0x1401e128f
0x001E11AC: lea rdx, [rbp + 0x4d0]
0x001E11B3: mov rcx, qword ptr [rsi + 0xd0]
0x001E11BA: call qword ptr [rip + 0x6068d8]
0x001E11C0: test eax, eax
```

#### ref `0x001E2249`

```asm
0x001E21E6: movups xmmword ptr [rcx + 0x10], xmm1
0x001E21EA: movups xmm0, xmmword ptr [r8 + 0x20]
0x001E21EF: movups xmmword ptr [rcx + 0x20], xmm0
0x001E21F3: movups xmm1, xmmword ptr [r8 + 0x30]
0x001E21F8: movups xmmword ptr [rcx + 0x30], xmm1
0x001E21FC: mov rax, qword ptr [r8 + 0x40]
0x001E2200: mov qword ptr [rcx + 0x40], rax
0x001E2204: movups xmm0, xmmword ptr [r9 + 8]
0x001E2209: movups xmmword ptr [rbp + 0x21fc], xmm0
0x001E2210: movups xmm1, xmmword ptr [r9 + 0x18]
0x001E2215: movups xmmword ptr [rbp + 0x220c], xmm1
0x001E221C: movsd xmm0, qword ptr [r9 + 0x28]
0x001E2222: movsd qword ptr [rbp + 0x221c], xmm0
0x001E222A: mov eax, dword ptr [r9 + 0x30]
0x001E222E: mov dword ptr [rbp + 0x2224], eax
0x001E2234: mov dword ptr [rbp + 0x2208], r14d
0x001E223B: lea rdx, [rbp + 0x21e0]
0x001E2242: mov rcx, qword ptr [rsi + 0xd0]
0x001E2249: call qword ptr [rip + 0x605851]
0x001E224F: mov dword ptr [rsp + 0x20], eax
0x001E2253: cmp eax, -1
0x001E2256: jne 0x1401e2340
0x001E225C: lea rdx, [rbp + 0x4e0]
0x001E2263: mov rcx, qword ptr [rsi + 0xd0]
0x001E226A: call qword ptr [rip + 0x605828]
0x001E2270: test eax, eax
```

#### ref `0x001E5CA8`

```asm
0x001E5C46: movups xmmword ptr [rcx + 0x10], xmm1
0x001E5C4A: movups xmm0, xmmword ptr [r9 + 0x20]
0x001E5C4F: movups xmmword ptr [rcx + 0x20], xmm0
0x001E5C53: movups xmm1, xmmword ptr [r9 + 0x30]
0x001E5C58: movups xmmword ptr [rcx + 0x30], xmm1
0x001E5C5C: mov rax, qword ptr [r9 + 0x40]
0x001E5C60: mov qword ptr [rcx + 0x40], rax
0x001E5C64: movups xmm0, xmmword ptr [r10 + 8]
0x001E5C69: movups xmmword ptr [rbp + 0x23ec], xmm0
0x001E5C70: movups xmm1, xmmword ptr [r10 + 0x18]
0x001E5C75: movups xmmword ptr [rbp + 0x23fc], xmm1
0x001E5C7C: movsd xmm0, qword ptr [r10 + 0x28]
0x001E5C82: movsd qword ptr [rbp + 0x240c], xmm0
0x001E5C8A: mov eax, dword ptr [r10 + 0x30]
0x001E5C8E: mov dword ptr [rbp + 0x2414], eax
0x001E5C94: mov dword ptr [rbp + 0x23f8], ebx
0x001E5C9A: lea rdx, [rbp + 0x23d0]
0x001E5CA1: mov rcx, qword ptr [rsi + 0xd0]
0x001E5CA8: call qword ptr [rip + 0x601df2]
0x001E5CAE: mov dword ptr [rsp + 0x20], eax
0x001E5CB2: cmp eax, -1
0x001E5CB5: jne 0x1401e5da0
0x001E5CBB: lea rdx, [rbp + 0x6d0]
0x001E5CC2: mov rcx, qword ptr [rsi + 0xd0]
0x001E5CC9: call qword ptr [rip + 0x601dc9]
0x001E5CCF: test eax, eax
```

#### ref `0x001E7A88`

```asm
0x001E7A26: movups xmmword ptr [rcx + 0x10], xmm1
0x001E7A2A: movups xmm0, xmmword ptr [r9 + 0x20]
0x001E7A2F: movups xmmword ptr [rcx + 0x20], xmm0
0x001E7A33: movups xmm1, xmmword ptr [r9 + 0x30]
0x001E7A38: movups xmmword ptr [rcx + 0x30], xmm1
0x001E7A3C: mov rax, qword ptr [r9 + 0x40]
0x001E7A40: mov qword ptr [rcx + 0x40], rax
0x001E7A44: movups xmm0, xmmword ptr [r10 + 8]
0x001E7A49: movups xmmword ptr [rbp + 0x23fc], xmm0
0x001E7A50: movups xmm1, xmmword ptr [r10 + 0x18]
0x001E7A55: movups xmmword ptr [rbp + 0x240c], xmm1
0x001E7A5C: movsd xmm0, qword ptr [r10 + 0x28]
0x001E7A62: movsd qword ptr [rbp + 0x241c], xmm0
0x001E7A6A: mov eax, dword ptr [r10 + 0x30]
0x001E7A6E: mov dword ptr [rbp + 0x2424], eax
0x001E7A74: mov dword ptr [rbp + 0x2408], ebx
0x001E7A7A: lea rdx, [rbp + 0x23e0]
0x001E7A81: mov rcx, qword ptr [rsi + 0xd0]
0x001E7A88: call qword ptr [rip + 0x600012]
0x001E7A8E: mov dword ptr [rsp + 0x20], eax
0x001E7A92: cmp eax, -1
0x001E7A95: jne 0x1401e7b81
0x001E7A9B: lea rdx, [rbp + 0x6e0]
0x001E7AA2: mov rcx, qword ptr [rsi + 0xd0]
0x001E7AA9: call qword ptr [rip + 0x5fffe9]
0x001E7AAF: test eax, eax
```

#### ref `0x001FE5EB`

```asm
0x001FE57F: mov qword ptr [rip + 0x5e94ea], rax
0x001FE586: call qword ptr [rip + 0x5e946c]
0x001FE58C: mov ecx, 0xc16c7e2c
0x001FE591: mov qword ptr [rip + 0x5e94e0], rax
0x001FE598: call qword ptr [rip + 0x5e945a]
0x001FE59E: mov ecx, 0x465f9bcf
0x001FE5A3: mov qword ptr [rip + 0x5e94d6], rax
0x001FE5AA: call qword ptr [rip + 0x5e9448]
0x001FE5B0: mov ecx, 0x927da4f6
0x001FE5B5: mov qword ptr [rip + 0x5e94cc], rax
0x001FE5BC: call qword ptr [rip + 0x5e9436]
0x001FE5C2: mov ecx, 0x6ff81213
0x001FE5C7: mov qword ptr [rip + 0x5e94c2], rax
0x001FE5CE: call qword ptr [rip + 0x5e9424]
0x001FE5D4: mov ecx, 0xf4dae6b
0x001FE5D9: mov qword ptr [rip + 0x5e94b8], rax
0x001FE5E0: call qword ptr [rip + 0x5e9412]
0x001FE5E6: mov ecx, 0x843c0256
0x001FE5EB: mov qword ptr [rip + 0x5e94ae], rax
0x001FE5F2: call qword ptr [rip + 0x5e9400]
0x001FE5F8: mov ecx, 0xedcf624e
0x001FE5FD: mov qword ptr [rip + 0x5e94a4], rax
0x001FE604: call qword ptr [rip + 0x5e93ee]
0x001FE60A: mov ecx, 0x34206d86
0x001FE60F: mov qword ptr [rip + 0x5e949a], rax
0x001FE616: call qword ptr [rip + 0x5e93dc]
```

## call `0x001E5CC9` function slot `0x007E7A98`

```asm
0x001E5CAE: mov dword ptr [rsp + 0x20], eax
0x001E5CB2: cmp eax, -1
0x001E5CB5: jne 0x1401e5da0
0x001E5CBB: lea rdx, [rbp + 0x6d0]
0x001E5CC2: mov rcx, qword ptr [rsi + 0xd0]
0x001E5CC9: call qword ptr [rip + 0x601dc9]
0x001E5CCF: test eax, eax
0x001E5CD1: jne 0x1401e602b
0x001E5CD7: mov r8d, r15d
```

### refs to global slot `0x007E7A98`: `9`

#### ref `0x001E0F3F`

```asm
0x001E0ED7: sub rsp, rax
0x001E0EDA: mov qword ptr [rsp + 0x70], 0xfffffffffffffffe
0x001E0EE3: mov qword ptr [rsp + 0x4058], rbx
0x001E0EEB: mov qword ptr [rsp + 0x4060], rsi
0x001E0EF3: mov rax, qword ptr [rip + 0x5f59f6]
0x001E0EFA: xor rax, rsp
0x001E0EFD: mov qword ptr [rbp + 0x3f20], rax
0x001E0F04: mov rsi, rcx
0x001E0F07: mov rbx, qword ptr [rcx + 0xd0]
0x001E0F0E: test rbx, rbx
0x001E0F11: je 0x1401e1f3e
0x001E0F17: xor edx, edx
0x001E0F19: mov r8d, 0x1cf8
0x001E0F1F: lea rcx, [rbp + 0x4d0]
0x001E0F26: call 0x1403d3050
0x001E0F2B: mov dword ptr [rbp + 0x4d0], 0x31cf8
0x001E0F35: lea rdx, [rbp + 0x4d0]
0x001E0F3C: mov rcx, rbx
0x001E0F3F: call qword ptr [rip + 0x606b53]
0x001E0F45: mov dword ptr [rsp + 0x20], eax
0x001E0F49: test eax, eax
0x001E0F4B: jne 0x1401e1f3e
0x001E0F51: xor r14d, r14d
0x001E0F54: mov ebx, r14d
0x001E0F57: mov r8d, dword ptr [rbp + 0x4d8]
0x001E0F5E: test r8d, r8d
```

#### ref `0x001E11BA`

```asm
0x001E1150: mov qword ptr [rcx + 0x40], rax
0x001E1154: movups xmm0, xmmword ptr [r9 + 8]
0x001E1159: movups xmmword ptr [rbp + 0x21ec], xmm0
0x001E1160: movups xmm1, xmmword ptr [r9 + 0x18]
0x001E1165: movups xmmword ptr [rbp + 0x21fc], xmm1
0x001E116C: movsd xmm0, qword ptr [r9 + 0x28]
0x001E1172: movsd qword ptr [rbp + 0x220c], xmm0
0x001E117A: mov eax, dword ptr [r9 + 0x30]
0x001E117E: mov dword ptr [rbp + 0x2214], eax
0x001E1184: mov dword ptr [rbp + 0x21f8], r14d
0x001E118B: lea rdx, [rbp + 0x21d0]
0x001E1192: mov rcx, qword ptr [rsi + 0xd0]
0x001E1199: call qword ptr [rip + 0x606901]
0x001E119F: mov dword ptr [rsp + 0x20], eax
0x001E11A3: cmp eax, -1
0x001E11A6: jne 0x1401e128f
0x001E11AC: lea rdx, [rbp + 0x4d0]
0x001E11B3: mov rcx, qword ptr [rsi + 0xd0]
0x001E11BA: call qword ptr [rip + 0x6068d8]
0x001E11C0: test eax, eax
0x001E11C2: jne 0x1401e1515
0x001E11C8: mov edx, r14d
0x001E11CB: mov r10d, dword ptr [rbp + 0x4d8]
0x001E11D2: test r10d, r10d
0x001E11D5: je 0x1401e1515
0x001E11DB: nop dword ptr [rax + rax]
```

#### ref `0x001E1FEF`

```asm
0x001E1F87: sub rsp, rax
0x001E1F8A: mov qword ptr [rsp + 0x70], 0xfffffffffffffffe
0x001E1F93: mov qword ptr [rsp + 0x4068], rbx
0x001E1F9B: mov qword ptr [rsp + 0x4070], rsi
0x001E1FA3: mov rax, qword ptr [rip + 0x5f4946]
0x001E1FAA: xor rax, rsp
0x001E1FAD: mov qword ptr [rbp + 0x3f30], rax
0x001E1FB4: mov rsi, rcx
0x001E1FB7: mov rbx, qword ptr [rcx + 0xd0]
0x001E1FBE: test rbx, rbx
0x001E1FC1: je 0x1401e2fb2
0x001E1FC7: xor edx, edx
0x001E1FC9: mov r8d, 0x1cf8
0x001E1FCF: lea rcx, [rbp + 0x4e0]
0x001E1FD6: call 0x1403d3050
0x001E1FDB: mov dword ptr [rbp + 0x4e0], 0x31cf8
0x001E1FE5: lea rdx, [rbp + 0x4e0]
0x001E1FEC: mov rcx, rbx
0x001E1FEF: call qword ptr [rip + 0x605aa3]
0x001E1FF5: mov dword ptr [rsp + 0x20], eax
0x001E1FF9: test eax, eax
0x001E1FFB: jne 0x1401e2fb2
0x001E2001: xor r14d, r14d
0x001E2004: mov ebx, r14d
0x001E2007: mov r8d, dword ptr [rbp + 0x4e8]
0x001E200E: test r8d, r8d
```

#### ref `0x001E226A`

```asm
0x001E2200: mov qword ptr [rcx + 0x40], rax
0x001E2204: movups xmm0, xmmword ptr [r9 + 8]
0x001E2209: movups xmmword ptr [rbp + 0x21fc], xmm0
0x001E2210: movups xmm1, xmmword ptr [r9 + 0x18]
0x001E2215: movups xmmword ptr [rbp + 0x220c], xmm1
0x001E221C: movsd xmm0, qword ptr [r9 + 0x28]
0x001E2222: movsd qword ptr [rbp + 0x221c], xmm0
0x001E222A: mov eax, dword ptr [r9 + 0x30]
0x001E222E: mov dword ptr [rbp + 0x2224], eax
0x001E2234: mov dword ptr [rbp + 0x2208], r14d
0x001E223B: lea rdx, [rbp + 0x21e0]
0x001E2242: mov rcx, qword ptr [rsi + 0xd0]
0x001E2249: call qword ptr [rip + 0x605851]
0x001E224F: mov dword ptr [rsp + 0x20], eax
0x001E2253: cmp eax, -1
0x001E2256: jne 0x1401e2340
0x001E225C: lea rdx, [rbp + 0x4e0]
0x001E2263: mov rcx, qword ptr [rsi + 0xd0]
0x001E226A: call qword ptr [rip + 0x605828]
0x001E2270: test eax, eax
0x001E2272: jne 0x1401e2770
0x001E2278: mov edx, r14d
0x001E227B: mov r10d, dword ptr [rbp + 0x4e8]
0x001E2282: test r10d, r10d
0x001E2285: je 0x1401e2770
0x001E228B: nop dword ptr [rax + rax]
```

#### ref `0x001E59FD`

```asm
0x001E59AC: cmp rcx, 8
0x001E59B0: jae 0x1401e59b8
0x001E59B2: call 0x1403db020
0x001E59B7: int3
0x001E59B8: cmp rcx, 0x27
0x001E59BC: jbe 0x1401e59c4
0x001E59BE: call 0x1403db020
0x001E59C3: int3
0x001E59C4: mov rcx, rax
0x001E59C7: call 0x1403b20d4
0x001E59CC: jmp 0x1401e6c57
0x001E59D1: xor edx, edx
0x001E59D3: mov r8d, 0x1cf8
0x001E59D9: lea rcx, [rbp + 0x6d0]
0x001E59E0: call 0x1403d3050
0x001E59E5: mov dword ptr [rbp + 0x6d0], 0x31cf8
0x001E59EF: lea rdx, [rbp + 0x6d0]
0x001E59F6: mov rcx, qword ptr [rsi + 0xd0]
0x001E59FD: call qword ptr [rip + 0x602095]
0x001E5A03: mov dword ptr [rsp + 0x20], eax
0x001E5A07: test eax, eax
0x001E5A09: jne 0x1401e6c57
0x001E5A0F: mov ebx, r15d
0x001E5A12: mov r8d, dword ptr [rbp + 0x6d8]
0x001E5A19: test r8d, r8d
0x001E5A1C: je 0x1401e6627
```

#### ref `0x001E5CC9`

```asm
0x001E5C60: mov qword ptr [rcx + 0x40], rax
0x001E5C64: movups xmm0, xmmword ptr [r10 + 8]
0x001E5C69: movups xmmword ptr [rbp + 0x23ec], xmm0
0x001E5C70: movups xmm1, xmmword ptr [r10 + 0x18]
0x001E5C75: movups xmmword ptr [rbp + 0x23fc], xmm1
0x001E5C7C: movsd xmm0, qword ptr [r10 + 0x28]
0x001E5C82: movsd qword ptr [rbp + 0x240c], xmm0
0x001E5C8A: mov eax, dword ptr [r10 + 0x30]
0x001E5C8E: mov dword ptr [rbp + 0x2414], eax
0x001E5C94: mov dword ptr [rbp + 0x23f8], ebx
0x001E5C9A: lea rdx, [rbp + 0x23d0]
0x001E5CA1: mov rcx, qword ptr [rsi + 0xd0]
0x001E5CA8: call qword ptr [rip + 0x601df2]
0x001E5CAE: mov dword ptr [rsp + 0x20], eax
0x001E5CB2: cmp eax, -1
0x001E5CB5: jne 0x1401e5da0
0x001E5CBB: lea rdx, [rbp + 0x6d0]
0x001E5CC2: mov rcx, qword ptr [rsi + 0xd0]
0x001E5CC9: call qword ptr [rip + 0x601dc9]
0x001E5CCF: test eax, eax
0x001E5CD1: jne 0x1401e602b
0x001E5CD7: mov r8d, r15d
0x001E5CDA: mov r10d, dword ptr [rbp + 0x6d8]
0x001E5CE1: test r10d, r10d
0x001E5CE4: je 0x1401e602b
0x001E5CEA: nop word ptr [rax + rax]
```

#### ref `0x001E77DE`

```asm
0x001E7786: call 0x1403db020
0x001E778B: int3
0x001E778C: cmp rcx, 0x27
0x001E7790: jbe 0x1401e7798
0x001E7792: call 0x1403db020
0x001E7797: int3
0x001E7798: mov rcx, rax
0x001E779B: call 0x1403b20d4
0x001E77A0: jmp 0x1401e89e4
0x001E77A5: cmp byte ptr [rbp + 0x4190], r15b
0x001E77AC: jne 0x1401e89e4
0x001E77B2: xor edx, edx
0x001E77B4: mov r8d, 0x1cf8
0x001E77BA: lea rcx, [rbp + 0x6e0]
0x001E77C1: call 0x1403d3050
0x001E77C6: mov dword ptr [rbp + 0x6e0], 0x31cf8
0x001E77D0: lea rdx, [rbp + 0x6e0]
0x001E77D7: mov rcx, qword ptr [rsi + 0xd0]
0x001E77DE: call qword ptr [rip + 0x6002b4]
0x001E77E4: mov dword ptr [rsp + 0x20], eax
0x001E77E8: test eax, eax
0x001E77EA: jne 0x1401e89e4
0x001E77F0: mov ebx, r15d
0x001E77F3: mov r8d, dword ptr [rbp + 0x6e8]
0x001E77FA: test r8d, r8d
0x001E77FD: je 0x1401e83b4
```

#### ref `0x001E7AA9`

```asm
0x001E7A40: mov qword ptr [rcx + 0x40], rax
0x001E7A44: movups xmm0, xmmword ptr [r10 + 8]
0x001E7A49: movups xmmword ptr [rbp + 0x23fc], xmm0
0x001E7A50: movups xmm1, xmmword ptr [r10 + 0x18]
0x001E7A55: movups xmmword ptr [rbp + 0x240c], xmm1
0x001E7A5C: movsd xmm0, qword ptr [r10 + 0x28]
0x001E7A62: movsd qword ptr [rbp + 0x241c], xmm0
0x001E7A6A: mov eax, dword ptr [r10 + 0x30]
0x001E7A6E: mov dword ptr [rbp + 0x2424], eax
0x001E7A74: mov dword ptr [rbp + 0x2408], ebx
0x001E7A7A: lea rdx, [rbp + 0x23e0]
0x001E7A81: mov rcx, qword ptr [rsi + 0xd0]
0x001E7A88: call qword ptr [rip + 0x600012]
0x001E7A8E: mov dword ptr [rsp + 0x20], eax
0x001E7A92: cmp eax, -1
0x001E7A95: jne 0x1401e7b81
0x001E7A9B: lea rdx, [rbp + 0x6e0]
0x001E7AA2: mov rcx, qword ptr [rsi + 0xd0]
0x001E7AA9: call qword ptr [rip + 0x5fffe9]
0x001E7AAF: test eax, eax
0x001E7AB1: jne 0x1401e7fac
0x001E7AB7: mov r8d, r15d
0x001E7ABA: mov r10d, dword ptr [rbp + 0x6e8]
0x001E7AC1: test r10d, r10d
0x001E7AC4: je 0x1401e7fac
0x001E7ACA: nop word ptr [rax + rax]
```

#### ref `0x001FE5D9`

```asm
0x001FE56F: mov ecx, 0xdcb616c3
0x001FE574: call qword ptr [rip + 0x5e947e]
0x001FE57A: mov ecx, 0x1bd69f49
0x001FE57F: mov qword ptr [rip + 0x5e94ea], rax
0x001FE586: call qword ptr [rip + 0x5e946c]
0x001FE58C: mov ecx, 0xc16c7e2c
0x001FE591: mov qword ptr [rip + 0x5e94e0], rax
0x001FE598: call qword ptr [rip + 0x5e945a]
0x001FE59E: mov ecx, 0x465f9bcf
0x001FE5A3: mov qword ptr [rip + 0x5e94d6], rax
0x001FE5AA: call qword ptr [rip + 0x5e9448]
0x001FE5B0: mov ecx, 0x927da4f6
0x001FE5B5: mov qword ptr [rip + 0x5e94cc], rax
0x001FE5BC: call qword ptr [rip + 0x5e9436]
0x001FE5C2: mov ecx, 0x6ff81213
0x001FE5C7: mov qword ptr [rip + 0x5e94c2], rax
0x001FE5CE: call qword ptr [rip + 0x5e9424]
0x001FE5D4: mov ecx, 0xf4dae6b
0x001FE5D9: mov qword ptr [rip + 0x5e94b8], rax
0x001FE5E0: call qword ptr [rip + 0x5e9412]
0x001FE5E6: mov ecx, 0x843c0256
0x001FE5EB: mov qword ptr [rip + 0x5e94ae], rax
0x001FE5F2: call qword ptr [rip + 0x5e9400]
0x001FE5F8: mov ecx, 0xedcf624e
0x001FE5FD: mov qword ptr [rip + 0x5e94a4], rax
0x001FE604: call qword ptr [rip + 0x5e93ee]
```

## call `0x001E77DE` function slot `0x007E7A98`

```asm
0x001E77BA: lea rcx, [rbp + 0x6e0]
0x001E77C1: call 0x1403d3050
0x001E77C6: mov dword ptr [rbp + 0x6e0], 0x31cf8
0x001E77D0: lea rdx, [rbp + 0x6e0]
0x001E77D7: mov rcx, qword ptr [rsi + 0xd0]
0x001E77DE: call qword ptr [rip + 0x6002b4]
0x001E77E4: mov dword ptr [rsp + 0x20], eax
0x001E77E8: test eax, eax
0x001E77EA: jne 0x1401e89e4
```

### refs to global slot `0x007E7A98`: `9`

#### ref `0x001E0F3F`

```asm
0x001E0ED7: sub rsp, rax
0x001E0EDA: mov qword ptr [rsp + 0x70], 0xfffffffffffffffe
0x001E0EE3: mov qword ptr [rsp + 0x4058], rbx
0x001E0EEB: mov qword ptr [rsp + 0x4060], rsi
0x001E0EF3: mov rax, qword ptr [rip + 0x5f59f6]
0x001E0EFA: xor rax, rsp
0x001E0EFD: mov qword ptr [rbp + 0x3f20], rax
0x001E0F04: mov rsi, rcx
0x001E0F07: mov rbx, qword ptr [rcx + 0xd0]
0x001E0F0E: test rbx, rbx
0x001E0F11: je 0x1401e1f3e
0x001E0F17: xor edx, edx
0x001E0F19: mov r8d, 0x1cf8
0x001E0F1F: lea rcx, [rbp + 0x4d0]
0x001E0F26: call 0x1403d3050
0x001E0F2B: mov dword ptr [rbp + 0x4d0], 0x31cf8
0x001E0F35: lea rdx, [rbp + 0x4d0]
0x001E0F3C: mov rcx, rbx
0x001E0F3F: call qword ptr [rip + 0x606b53]
0x001E0F45: mov dword ptr [rsp + 0x20], eax
0x001E0F49: test eax, eax
0x001E0F4B: jne 0x1401e1f3e
0x001E0F51: xor r14d, r14d
0x001E0F54: mov ebx, r14d
0x001E0F57: mov r8d, dword ptr [rbp + 0x4d8]
0x001E0F5E: test r8d, r8d
```

#### ref `0x001E11BA`

```asm
0x001E1150: mov qword ptr [rcx + 0x40], rax
0x001E1154: movups xmm0, xmmword ptr [r9 + 8]
0x001E1159: movups xmmword ptr [rbp + 0x21ec], xmm0
0x001E1160: movups xmm1, xmmword ptr [r9 + 0x18]
0x001E1165: movups xmmword ptr [rbp + 0x21fc], xmm1
0x001E116C: movsd xmm0, qword ptr [r9 + 0x28]
0x001E1172: movsd qword ptr [rbp + 0x220c], xmm0
0x001E117A: mov eax, dword ptr [r9 + 0x30]
0x001E117E: mov dword ptr [rbp + 0x2214], eax
0x001E1184: mov dword ptr [rbp + 0x21f8], r14d
0x001E118B: lea rdx, [rbp + 0x21d0]
0x001E1192: mov rcx, qword ptr [rsi + 0xd0]
0x001E1199: call qword ptr [rip + 0x606901]
0x001E119F: mov dword ptr [rsp + 0x20], eax
0x001E11A3: cmp eax, -1
0x001E11A6: jne 0x1401e128f
0x001E11AC: lea rdx, [rbp + 0x4d0]
0x001E11B3: mov rcx, qword ptr [rsi + 0xd0]
0x001E11BA: call qword ptr [rip + 0x6068d8]
0x001E11C0: test eax, eax
0x001E11C2: jne 0x1401e1515
0x001E11C8: mov edx, r14d
0x001E11CB: mov r10d, dword ptr [rbp + 0x4d8]
0x001E11D2: test r10d, r10d
0x001E11D5: je 0x1401e1515
0x001E11DB: nop dword ptr [rax + rax]
```

#### ref `0x001E1FEF`

```asm
0x001E1F87: sub rsp, rax
0x001E1F8A: mov qword ptr [rsp + 0x70], 0xfffffffffffffffe
0x001E1F93: mov qword ptr [rsp + 0x4068], rbx
0x001E1F9B: mov qword ptr [rsp + 0x4070], rsi
0x001E1FA3: mov rax, qword ptr [rip + 0x5f4946]
0x001E1FAA: xor rax, rsp
0x001E1FAD: mov qword ptr [rbp + 0x3f30], rax
0x001E1FB4: mov rsi, rcx
0x001E1FB7: mov rbx, qword ptr [rcx + 0xd0]
0x001E1FBE: test rbx, rbx
0x001E1FC1: je 0x1401e2fb2
0x001E1FC7: xor edx, edx
0x001E1FC9: mov r8d, 0x1cf8
0x001E1FCF: lea rcx, [rbp + 0x4e0]
0x001E1FD6: call 0x1403d3050
0x001E1FDB: mov dword ptr [rbp + 0x4e0], 0x31cf8
0x001E1FE5: lea rdx, [rbp + 0x4e0]
0x001E1FEC: mov rcx, rbx
0x001E1FEF: call qword ptr [rip + 0x605aa3]
0x001E1FF5: mov dword ptr [rsp + 0x20], eax
0x001E1FF9: test eax, eax
0x001E1FFB: jne 0x1401e2fb2
0x001E2001: xor r14d, r14d
0x001E2004: mov ebx, r14d
0x001E2007: mov r8d, dword ptr [rbp + 0x4e8]
0x001E200E: test r8d, r8d
```

#### ref `0x001E226A`

```asm
0x001E2200: mov qword ptr [rcx + 0x40], rax
0x001E2204: movups xmm0, xmmword ptr [r9 + 8]
0x001E2209: movups xmmword ptr [rbp + 0x21fc], xmm0
0x001E2210: movups xmm1, xmmword ptr [r9 + 0x18]
0x001E2215: movups xmmword ptr [rbp + 0x220c], xmm1
0x001E221C: movsd xmm0, qword ptr [r9 + 0x28]
0x001E2222: movsd qword ptr [rbp + 0x221c], xmm0
0x001E222A: mov eax, dword ptr [r9 + 0x30]
0x001E222E: mov dword ptr [rbp + 0x2224], eax
0x001E2234: mov dword ptr [rbp + 0x2208], r14d
0x001E223B: lea rdx, [rbp + 0x21e0]
0x001E2242: mov rcx, qword ptr [rsi + 0xd0]
0x001E2249: call qword ptr [rip + 0x605851]
0x001E224F: mov dword ptr [rsp + 0x20], eax
0x001E2253: cmp eax, -1
0x001E2256: jne 0x1401e2340
0x001E225C: lea rdx, [rbp + 0x4e0]
0x001E2263: mov rcx, qword ptr [rsi + 0xd0]
0x001E226A: call qword ptr [rip + 0x605828]
0x001E2270: test eax, eax
0x001E2272: jne 0x1401e2770
0x001E2278: mov edx, r14d
0x001E227B: mov r10d, dword ptr [rbp + 0x4e8]
0x001E2282: test r10d, r10d
0x001E2285: je 0x1401e2770
0x001E228B: nop dword ptr [rax + rax]
```

#### ref `0x001E59FD`

```asm
0x001E59AC: cmp rcx, 8
0x001E59B0: jae 0x1401e59b8
0x001E59B2: call 0x1403db020
0x001E59B7: int3
0x001E59B8: cmp rcx, 0x27
0x001E59BC: jbe 0x1401e59c4
0x001E59BE: call 0x1403db020
0x001E59C3: int3
0x001E59C4: mov rcx, rax
0x001E59C7: call 0x1403b20d4
0x001E59CC: jmp 0x1401e6c57
0x001E59D1: xor edx, edx
0x001E59D3: mov r8d, 0x1cf8
0x001E59D9: lea rcx, [rbp + 0x6d0]
0x001E59E0: call 0x1403d3050
0x001E59E5: mov dword ptr [rbp + 0x6d0], 0x31cf8
0x001E59EF: lea rdx, [rbp + 0x6d0]
0x001E59F6: mov rcx, qword ptr [rsi + 0xd0]
0x001E59FD: call qword ptr [rip + 0x602095]
0x001E5A03: mov dword ptr [rsp + 0x20], eax
0x001E5A07: test eax, eax
0x001E5A09: jne 0x1401e6c57
0x001E5A0F: mov ebx, r15d
0x001E5A12: mov r8d, dword ptr [rbp + 0x6d8]
0x001E5A19: test r8d, r8d
0x001E5A1C: je 0x1401e6627
```

#### ref `0x001E5CC9`

```asm
0x001E5C60: mov qword ptr [rcx + 0x40], rax
0x001E5C64: movups xmm0, xmmword ptr [r10 + 8]
0x001E5C69: movups xmmword ptr [rbp + 0x23ec], xmm0
0x001E5C70: movups xmm1, xmmword ptr [r10 + 0x18]
0x001E5C75: movups xmmword ptr [rbp + 0x23fc], xmm1
0x001E5C7C: movsd xmm0, qword ptr [r10 + 0x28]
0x001E5C82: movsd qword ptr [rbp + 0x240c], xmm0
0x001E5C8A: mov eax, dword ptr [r10 + 0x30]
0x001E5C8E: mov dword ptr [rbp + 0x2414], eax
0x001E5C94: mov dword ptr [rbp + 0x23f8], ebx
0x001E5C9A: lea rdx, [rbp + 0x23d0]
0x001E5CA1: mov rcx, qword ptr [rsi + 0xd0]
0x001E5CA8: call qword ptr [rip + 0x601df2]
0x001E5CAE: mov dword ptr [rsp + 0x20], eax
0x001E5CB2: cmp eax, -1
0x001E5CB5: jne 0x1401e5da0
0x001E5CBB: lea rdx, [rbp + 0x6d0]
0x001E5CC2: mov rcx, qword ptr [rsi + 0xd0]
0x001E5CC9: call qword ptr [rip + 0x601dc9]
0x001E5CCF: test eax, eax
0x001E5CD1: jne 0x1401e602b
0x001E5CD7: mov r8d, r15d
0x001E5CDA: mov r10d, dword ptr [rbp + 0x6d8]
0x001E5CE1: test r10d, r10d
0x001E5CE4: je 0x1401e602b
0x001E5CEA: nop word ptr [rax + rax]
```

#### ref `0x001E77DE`

```asm
0x001E7786: call 0x1403db020
0x001E778B: int3
0x001E778C: cmp rcx, 0x27
0x001E7790: jbe 0x1401e7798
0x001E7792: call 0x1403db020
0x001E7797: int3
0x001E7798: mov rcx, rax
0x001E779B: call 0x1403b20d4
0x001E77A0: jmp 0x1401e89e4
0x001E77A5: cmp byte ptr [rbp + 0x4190], r15b
0x001E77AC: jne 0x1401e89e4
0x001E77B2: xor edx, edx
0x001E77B4: mov r8d, 0x1cf8
0x001E77BA: lea rcx, [rbp + 0x6e0]
0x001E77C1: call 0x1403d3050
0x001E77C6: mov dword ptr [rbp + 0x6e0], 0x31cf8
0x001E77D0: lea rdx, [rbp + 0x6e0]
0x001E77D7: mov rcx, qword ptr [rsi + 0xd0]
0x001E77DE: call qword ptr [rip + 0x6002b4]
0x001E77E4: mov dword ptr [rsp + 0x20], eax
0x001E77E8: test eax, eax
0x001E77EA: jne 0x1401e89e4
0x001E77F0: mov ebx, r15d
0x001E77F3: mov r8d, dword ptr [rbp + 0x6e8]
0x001E77FA: test r8d, r8d
0x001E77FD: je 0x1401e83b4
```

#### ref `0x001E7AA9`

```asm
0x001E7A40: mov qword ptr [rcx + 0x40], rax
0x001E7A44: movups xmm0, xmmword ptr [r10 + 8]
0x001E7A49: movups xmmword ptr [rbp + 0x23fc], xmm0
0x001E7A50: movups xmm1, xmmword ptr [r10 + 0x18]
0x001E7A55: movups xmmword ptr [rbp + 0x240c], xmm1
0x001E7A5C: movsd xmm0, qword ptr [r10 + 0x28]
0x001E7A62: movsd qword ptr [rbp + 0x241c], xmm0
0x001E7A6A: mov eax, dword ptr [r10 + 0x30]
0x001E7A6E: mov dword ptr [rbp + 0x2424], eax
0x001E7A74: mov dword ptr [rbp + 0x2408], ebx
0x001E7A7A: lea rdx, [rbp + 0x23e0]
0x001E7A81: mov rcx, qword ptr [rsi + 0xd0]
0x001E7A88: call qword ptr [rip + 0x600012]
0x001E7A8E: mov dword ptr [rsp + 0x20], eax
0x001E7A92: cmp eax, -1
0x001E7A95: jne 0x1401e7b81
0x001E7A9B: lea rdx, [rbp + 0x6e0]
0x001E7AA2: mov rcx, qword ptr [rsi + 0xd0]
0x001E7AA9: call qword ptr [rip + 0x5fffe9]
0x001E7AAF: test eax, eax
0x001E7AB1: jne 0x1401e7fac
0x001E7AB7: mov r8d, r15d
0x001E7ABA: mov r10d, dword ptr [rbp + 0x6e8]
0x001E7AC1: test r10d, r10d
0x001E7AC4: je 0x1401e7fac
0x001E7ACA: nop word ptr [rax + rax]
```

#### ref `0x001FE5D9`

```asm
0x001FE56F: mov ecx, 0xdcb616c3
0x001FE574: call qword ptr [rip + 0x5e947e]
0x001FE57A: mov ecx, 0x1bd69f49
0x001FE57F: mov qword ptr [rip + 0x5e94ea], rax
0x001FE586: call qword ptr [rip + 0x5e946c]
0x001FE58C: mov ecx, 0xc16c7e2c
0x001FE591: mov qword ptr [rip + 0x5e94e0], rax
0x001FE598: call qword ptr [rip + 0x5e945a]
0x001FE59E: mov ecx, 0x465f9bcf
0x001FE5A3: mov qword ptr [rip + 0x5e94d6], rax
0x001FE5AA: call qword ptr [rip + 0x5e9448]
0x001FE5B0: mov ecx, 0x927da4f6
0x001FE5B5: mov qword ptr [rip + 0x5e94cc], rax
0x001FE5BC: call qword ptr [rip + 0x5e9436]
0x001FE5C2: mov ecx, 0x6ff81213
0x001FE5C7: mov qword ptr [rip + 0x5e94c2], rax
0x001FE5CE: call qword ptr [rip + 0x5e9424]
0x001FE5D4: mov ecx, 0xf4dae6b
0x001FE5D9: mov qword ptr [rip + 0x5e94b8], rax
0x001FE5E0: call qword ptr [rip + 0x5e9412]
0x001FE5E6: mov ecx, 0x843c0256
0x001FE5EB: mov qword ptr [rip + 0x5e94ae], rax
0x001FE5F2: call qword ptr [rip + 0x5e9400]
0x001FE5F8: mov ecx, 0xedcf624e
0x001FE5FD: mov qword ptr [rip + 0x5e94a4], rax
0x001FE604: call qword ptr [rip + 0x5e93ee]
```

## call `0x001E7A88` function slot `0x007E7AA0`

```asm
0x001E7A6A: mov eax, dword ptr [r10 + 0x30]
0x001E7A6E: mov dword ptr [rbp + 0x2424], eax
0x001E7A74: mov dword ptr [rbp + 0x2408], ebx
0x001E7A7A: lea rdx, [rbp + 0x23e0]
0x001E7A81: mov rcx, qword ptr [rsi + 0xd0]
0x001E7A88: call qword ptr [rip + 0x600012]
0x001E7A8E: mov dword ptr [rsp + 0x20], eax
0x001E7A92: cmp eax, -1
0x001E7A95: jne 0x1401e7b81
```

### refs to global slot `0x007E7AA0`: `5`

#### ref `0x001E1199`

```asm
0x001E1136: movups xmmword ptr [rcx + 0x10], xmm1
0x001E113A: movups xmm0, xmmword ptr [r8 + 0x20]
0x001E113F: movups xmmword ptr [rcx + 0x20], xmm0
0x001E1143: movups xmm1, xmmword ptr [r8 + 0x30]
0x001E1148: movups xmmword ptr [rcx + 0x30], xmm1
0x001E114C: mov rax, qword ptr [r8 + 0x40]
0x001E1150: mov qword ptr [rcx + 0x40], rax
0x001E1154: movups xmm0, xmmword ptr [r9 + 8]
0x001E1159: movups xmmword ptr [rbp + 0x21ec], xmm0
0x001E1160: movups xmm1, xmmword ptr [r9 + 0x18]
0x001E1165: movups xmmword ptr [rbp + 0x21fc], xmm1
0x001E116C: movsd xmm0, qword ptr [r9 + 0x28]
0x001E1172: movsd qword ptr [rbp + 0x220c], xmm0
0x001E117A: mov eax, dword ptr [r9 + 0x30]
0x001E117E: mov dword ptr [rbp + 0x2214], eax
0x001E1184: mov dword ptr [rbp + 0x21f8], r14d
0x001E118B: lea rdx, [rbp + 0x21d0]
0x001E1192: mov rcx, qword ptr [rsi + 0xd0]
0x001E1199: call qword ptr [rip + 0x606901]
0x001E119F: mov dword ptr [rsp + 0x20], eax
0x001E11A3: cmp eax, -1
0x001E11A6: jne 0x1401e128f
0x001E11AC: lea rdx, [rbp + 0x4d0]
0x001E11B3: mov rcx, qword ptr [rsi + 0xd0]
0x001E11BA: call qword ptr [rip + 0x6068d8]
0x001E11C0: test eax, eax
```

#### ref `0x001E2249`

```asm
0x001E21E6: movups xmmword ptr [rcx + 0x10], xmm1
0x001E21EA: movups xmm0, xmmword ptr [r8 + 0x20]
0x001E21EF: movups xmmword ptr [rcx + 0x20], xmm0
0x001E21F3: movups xmm1, xmmword ptr [r8 + 0x30]
0x001E21F8: movups xmmword ptr [rcx + 0x30], xmm1
0x001E21FC: mov rax, qword ptr [r8 + 0x40]
0x001E2200: mov qword ptr [rcx + 0x40], rax
0x001E2204: movups xmm0, xmmword ptr [r9 + 8]
0x001E2209: movups xmmword ptr [rbp + 0x21fc], xmm0
0x001E2210: movups xmm1, xmmword ptr [r9 + 0x18]
0x001E2215: movups xmmword ptr [rbp + 0x220c], xmm1
0x001E221C: movsd xmm0, qword ptr [r9 + 0x28]
0x001E2222: movsd qword ptr [rbp + 0x221c], xmm0
0x001E222A: mov eax, dword ptr [r9 + 0x30]
0x001E222E: mov dword ptr [rbp + 0x2224], eax
0x001E2234: mov dword ptr [rbp + 0x2208], r14d
0x001E223B: lea rdx, [rbp + 0x21e0]
0x001E2242: mov rcx, qword ptr [rsi + 0xd0]
0x001E2249: call qword ptr [rip + 0x605851]
0x001E224F: mov dword ptr [rsp + 0x20], eax
0x001E2253: cmp eax, -1
0x001E2256: jne 0x1401e2340
0x001E225C: lea rdx, [rbp + 0x4e0]
0x001E2263: mov rcx, qword ptr [rsi + 0xd0]
0x001E226A: call qword ptr [rip + 0x605828]
0x001E2270: test eax, eax
```

#### ref `0x001E5CA8`

```asm
0x001E5C46: movups xmmword ptr [rcx + 0x10], xmm1
0x001E5C4A: movups xmm0, xmmword ptr [r9 + 0x20]
0x001E5C4F: movups xmmword ptr [rcx + 0x20], xmm0
0x001E5C53: movups xmm1, xmmword ptr [r9 + 0x30]
0x001E5C58: movups xmmword ptr [rcx + 0x30], xmm1
0x001E5C5C: mov rax, qword ptr [r9 + 0x40]
0x001E5C60: mov qword ptr [rcx + 0x40], rax
0x001E5C64: movups xmm0, xmmword ptr [r10 + 8]
0x001E5C69: movups xmmword ptr [rbp + 0x23ec], xmm0
0x001E5C70: movups xmm1, xmmword ptr [r10 + 0x18]
0x001E5C75: movups xmmword ptr [rbp + 0x23fc], xmm1
0x001E5C7C: movsd xmm0, qword ptr [r10 + 0x28]
0x001E5C82: movsd qword ptr [rbp + 0x240c], xmm0
0x001E5C8A: mov eax, dword ptr [r10 + 0x30]
0x001E5C8E: mov dword ptr [rbp + 0x2414], eax
0x001E5C94: mov dword ptr [rbp + 0x23f8], ebx
0x001E5C9A: lea rdx, [rbp + 0x23d0]
0x001E5CA1: mov rcx, qword ptr [rsi + 0xd0]
0x001E5CA8: call qword ptr [rip + 0x601df2]
0x001E5CAE: mov dword ptr [rsp + 0x20], eax
0x001E5CB2: cmp eax, -1
0x001E5CB5: jne 0x1401e5da0
0x001E5CBB: lea rdx, [rbp + 0x6d0]
0x001E5CC2: mov rcx, qword ptr [rsi + 0xd0]
0x001E5CC9: call qword ptr [rip + 0x601dc9]
0x001E5CCF: test eax, eax
```

#### ref `0x001E7A88`

```asm
0x001E7A26: movups xmmword ptr [rcx + 0x10], xmm1
0x001E7A2A: movups xmm0, xmmword ptr [r9 + 0x20]
0x001E7A2F: movups xmmword ptr [rcx + 0x20], xmm0
0x001E7A33: movups xmm1, xmmword ptr [r9 + 0x30]
0x001E7A38: movups xmmword ptr [rcx + 0x30], xmm1
0x001E7A3C: mov rax, qword ptr [r9 + 0x40]
0x001E7A40: mov qword ptr [rcx + 0x40], rax
0x001E7A44: movups xmm0, xmmword ptr [r10 + 8]
0x001E7A49: movups xmmword ptr [rbp + 0x23fc], xmm0
0x001E7A50: movups xmm1, xmmword ptr [r10 + 0x18]
0x001E7A55: movups xmmword ptr [rbp + 0x240c], xmm1
0x001E7A5C: movsd xmm0, qword ptr [r10 + 0x28]
0x001E7A62: movsd qword ptr [rbp + 0x241c], xmm0
0x001E7A6A: mov eax, dword ptr [r10 + 0x30]
0x001E7A6E: mov dword ptr [rbp + 0x2424], eax
0x001E7A74: mov dword ptr [rbp + 0x2408], ebx
0x001E7A7A: lea rdx, [rbp + 0x23e0]
0x001E7A81: mov rcx, qword ptr [rsi + 0xd0]
0x001E7A88: call qword ptr [rip + 0x600012]
0x001E7A8E: mov dword ptr [rsp + 0x20], eax
0x001E7A92: cmp eax, -1
0x001E7A95: jne 0x1401e7b81
0x001E7A9B: lea rdx, [rbp + 0x6e0]
0x001E7AA2: mov rcx, qword ptr [rsi + 0xd0]
0x001E7AA9: call qword ptr [rip + 0x5fffe9]
0x001E7AAF: test eax, eax
```

#### ref `0x001FE5EB`

```asm
0x001FE57F: mov qword ptr [rip + 0x5e94ea], rax
0x001FE586: call qword ptr [rip + 0x5e946c]
0x001FE58C: mov ecx, 0xc16c7e2c
0x001FE591: mov qword ptr [rip + 0x5e94e0], rax
0x001FE598: call qword ptr [rip + 0x5e945a]
0x001FE59E: mov ecx, 0x465f9bcf
0x001FE5A3: mov qword ptr [rip + 0x5e94d6], rax
0x001FE5AA: call qword ptr [rip + 0x5e9448]
0x001FE5B0: mov ecx, 0x927da4f6
0x001FE5B5: mov qword ptr [rip + 0x5e94cc], rax
0x001FE5BC: call qword ptr [rip + 0x5e9436]
0x001FE5C2: mov ecx, 0x6ff81213
0x001FE5C7: mov qword ptr [rip + 0x5e94c2], rax
0x001FE5CE: call qword ptr [rip + 0x5e9424]
0x001FE5D4: mov ecx, 0xf4dae6b
0x001FE5D9: mov qword ptr [rip + 0x5e94b8], rax
0x001FE5E0: call qword ptr [rip + 0x5e9412]
0x001FE5E6: mov ecx, 0x843c0256
0x001FE5EB: mov qword ptr [rip + 0x5e94ae], rax
0x001FE5F2: call qword ptr [rip + 0x5e9400]
0x001FE5F8: mov ecx, 0xedcf624e
0x001FE5FD: mov qword ptr [rip + 0x5e94a4], rax
0x001FE604: call qword ptr [rip + 0x5e93ee]
0x001FE60A: mov ecx, 0x34206d86
0x001FE60F: mov qword ptr [rip + 0x5e949a], rax
0x001FE616: call qword ptr [rip + 0x5e93dc]
```

## call `0x001E7AA9` function slot `0x007E7A98`

```asm
0x001E7A8E: mov dword ptr [rsp + 0x20], eax
0x001E7A92: cmp eax, -1
0x001E7A95: jne 0x1401e7b81
0x001E7A9B: lea rdx, [rbp + 0x6e0]
0x001E7AA2: mov rcx, qword ptr [rsi + 0xd0]
0x001E7AA9: call qword ptr [rip + 0x5fffe9]
0x001E7AAF: test eax, eax
0x001E7AB1: jne 0x1401e7fac
0x001E7AB7: mov r8d, r15d
```

### refs to global slot `0x007E7A98`: `9`

#### ref `0x001E0F3F`

```asm
0x001E0ED7: sub rsp, rax
0x001E0EDA: mov qword ptr [rsp + 0x70], 0xfffffffffffffffe
0x001E0EE3: mov qword ptr [rsp + 0x4058], rbx
0x001E0EEB: mov qword ptr [rsp + 0x4060], rsi
0x001E0EF3: mov rax, qword ptr [rip + 0x5f59f6]
0x001E0EFA: xor rax, rsp
0x001E0EFD: mov qword ptr [rbp + 0x3f20], rax
0x001E0F04: mov rsi, rcx
0x001E0F07: mov rbx, qword ptr [rcx + 0xd0]
0x001E0F0E: test rbx, rbx
0x001E0F11: je 0x1401e1f3e
0x001E0F17: xor edx, edx
0x001E0F19: mov r8d, 0x1cf8
0x001E0F1F: lea rcx, [rbp + 0x4d0]
0x001E0F26: call 0x1403d3050
0x001E0F2B: mov dword ptr [rbp + 0x4d0], 0x31cf8
0x001E0F35: lea rdx, [rbp + 0x4d0]
0x001E0F3C: mov rcx, rbx
0x001E0F3F: call qword ptr [rip + 0x606b53]
0x001E0F45: mov dword ptr [rsp + 0x20], eax
0x001E0F49: test eax, eax
0x001E0F4B: jne 0x1401e1f3e
0x001E0F51: xor r14d, r14d
0x001E0F54: mov ebx, r14d
0x001E0F57: mov r8d, dword ptr [rbp + 0x4d8]
0x001E0F5E: test r8d, r8d
```

#### ref `0x001E11BA`

```asm
0x001E1150: mov qword ptr [rcx + 0x40], rax
0x001E1154: movups xmm0, xmmword ptr [r9 + 8]
0x001E1159: movups xmmword ptr [rbp + 0x21ec], xmm0
0x001E1160: movups xmm1, xmmword ptr [r9 + 0x18]
0x001E1165: movups xmmword ptr [rbp + 0x21fc], xmm1
0x001E116C: movsd xmm0, qword ptr [r9 + 0x28]
0x001E1172: movsd qword ptr [rbp + 0x220c], xmm0
0x001E117A: mov eax, dword ptr [r9 + 0x30]
0x001E117E: mov dword ptr [rbp + 0x2214], eax
0x001E1184: mov dword ptr [rbp + 0x21f8], r14d
0x001E118B: lea rdx, [rbp + 0x21d0]
0x001E1192: mov rcx, qword ptr [rsi + 0xd0]
0x001E1199: call qword ptr [rip + 0x606901]
0x001E119F: mov dword ptr [rsp + 0x20], eax
0x001E11A3: cmp eax, -1
0x001E11A6: jne 0x1401e128f
0x001E11AC: lea rdx, [rbp + 0x4d0]
0x001E11B3: mov rcx, qword ptr [rsi + 0xd0]
0x001E11BA: call qword ptr [rip + 0x6068d8]
0x001E11C0: test eax, eax
0x001E11C2: jne 0x1401e1515
0x001E11C8: mov edx, r14d
0x001E11CB: mov r10d, dword ptr [rbp + 0x4d8]
0x001E11D2: test r10d, r10d
0x001E11D5: je 0x1401e1515
0x001E11DB: nop dword ptr [rax + rax]
```

#### ref `0x001E1FEF`

```asm
0x001E1F87: sub rsp, rax
0x001E1F8A: mov qword ptr [rsp + 0x70], 0xfffffffffffffffe
0x001E1F93: mov qword ptr [rsp + 0x4068], rbx
0x001E1F9B: mov qword ptr [rsp + 0x4070], rsi
0x001E1FA3: mov rax, qword ptr [rip + 0x5f4946]
0x001E1FAA: xor rax, rsp
0x001E1FAD: mov qword ptr [rbp + 0x3f30], rax
0x001E1FB4: mov rsi, rcx
0x001E1FB7: mov rbx, qword ptr [rcx + 0xd0]
0x001E1FBE: test rbx, rbx
0x001E1FC1: je 0x1401e2fb2
0x001E1FC7: xor edx, edx
0x001E1FC9: mov r8d, 0x1cf8
0x001E1FCF: lea rcx, [rbp + 0x4e0]
0x001E1FD6: call 0x1403d3050
0x001E1FDB: mov dword ptr [rbp + 0x4e0], 0x31cf8
0x001E1FE5: lea rdx, [rbp + 0x4e0]
0x001E1FEC: mov rcx, rbx
0x001E1FEF: call qword ptr [rip + 0x605aa3]
0x001E1FF5: mov dword ptr [rsp + 0x20], eax
0x001E1FF9: test eax, eax
0x001E1FFB: jne 0x1401e2fb2
0x001E2001: xor r14d, r14d
0x001E2004: mov ebx, r14d
0x001E2007: mov r8d, dword ptr [rbp + 0x4e8]
0x001E200E: test r8d, r8d
```

#### ref `0x001E226A`

```asm
0x001E2200: mov qword ptr [rcx + 0x40], rax
0x001E2204: movups xmm0, xmmword ptr [r9 + 8]
0x001E2209: movups xmmword ptr [rbp + 0x21fc], xmm0
0x001E2210: movups xmm1, xmmword ptr [r9 + 0x18]
0x001E2215: movups xmmword ptr [rbp + 0x220c], xmm1
0x001E221C: movsd xmm0, qword ptr [r9 + 0x28]
0x001E2222: movsd qword ptr [rbp + 0x221c], xmm0
0x001E222A: mov eax, dword ptr [r9 + 0x30]
0x001E222E: mov dword ptr [rbp + 0x2224], eax
0x001E2234: mov dword ptr [rbp + 0x2208], r14d
0x001E223B: lea rdx, [rbp + 0x21e0]
0x001E2242: mov rcx, qword ptr [rsi + 0xd0]
0x001E2249: call qword ptr [rip + 0x605851]
0x001E224F: mov dword ptr [rsp + 0x20], eax
0x001E2253: cmp eax, -1
0x001E2256: jne 0x1401e2340
0x001E225C: lea rdx, [rbp + 0x4e0]
0x001E2263: mov rcx, qword ptr [rsi + 0xd0]
0x001E226A: call qword ptr [rip + 0x605828]
0x001E2270: test eax, eax
0x001E2272: jne 0x1401e2770
0x001E2278: mov edx, r14d
0x001E227B: mov r10d, dword ptr [rbp + 0x4e8]
0x001E2282: test r10d, r10d
0x001E2285: je 0x1401e2770
0x001E228B: nop dword ptr [rax + rax]
```

#### ref `0x001E59FD`

```asm
0x001E59AC: cmp rcx, 8
0x001E59B0: jae 0x1401e59b8
0x001E59B2: call 0x1403db020
0x001E59B7: int3
0x001E59B8: cmp rcx, 0x27
0x001E59BC: jbe 0x1401e59c4
0x001E59BE: call 0x1403db020
0x001E59C3: int3
0x001E59C4: mov rcx, rax
0x001E59C7: call 0x1403b20d4
0x001E59CC: jmp 0x1401e6c57
0x001E59D1: xor edx, edx
0x001E59D3: mov r8d, 0x1cf8
0x001E59D9: lea rcx, [rbp + 0x6d0]
0x001E59E0: call 0x1403d3050
0x001E59E5: mov dword ptr [rbp + 0x6d0], 0x31cf8
0x001E59EF: lea rdx, [rbp + 0x6d0]
0x001E59F6: mov rcx, qword ptr [rsi + 0xd0]
0x001E59FD: call qword ptr [rip + 0x602095]
0x001E5A03: mov dword ptr [rsp + 0x20], eax
0x001E5A07: test eax, eax
0x001E5A09: jne 0x1401e6c57
0x001E5A0F: mov ebx, r15d
0x001E5A12: mov r8d, dword ptr [rbp + 0x6d8]
0x001E5A19: test r8d, r8d
0x001E5A1C: je 0x1401e6627
```

#### ref `0x001E5CC9`

```asm
0x001E5C60: mov qword ptr [rcx + 0x40], rax
0x001E5C64: movups xmm0, xmmword ptr [r10 + 8]
0x001E5C69: movups xmmword ptr [rbp + 0x23ec], xmm0
0x001E5C70: movups xmm1, xmmword ptr [r10 + 0x18]
0x001E5C75: movups xmmword ptr [rbp + 0x23fc], xmm1
0x001E5C7C: movsd xmm0, qword ptr [r10 + 0x28]
0x001E5C82: movsd qword ptr [rbp + 0x240c], xmm0
0x001E5C8A: mov eax, dword ptr [r10 + 0x30]
0x001E5C8E: mov dword ptr [rbp + 0x2414], eax
0x001E5C94: mov dword ptr [rbp + 0x23f8], ebx
0x001E5C9A: lea rdx, [rbp + 0x23d0]
0x001E5CA1: mov rcx, qword ptr [rsi + 0xd0]
0x001E5CA8: call qword ptr [rip + 0x601df2]
0x001E5CAE: mov dword ptr [rsp + 0x20], eax
0x001E5CB2: cmp eax, -1
0x001E5CB5: jne 0x1401e5da0
0x001E5CBB: lea rdx, [rbp + 0x6d0]
0x001E5CC2: mov rcx, qword ptr [rsi + 0xd0]
0x001E5CC9: call qword ptr [rip + 0x601dc9]
0x001E5CCF: test eax, eax
0x001E5CD1: jne 0x1401e602b
0x001E5CD7: mov r8d, r15d
0x001E5CDA: mov r10d, dword ptr [rbp + 0x6d8]
0x001E5CE1: test r10d, r10d
0x001E5CE4: je 0x1401e602b
0x001E5CEA: nop word ptr [rax + rax]
```

#### ref `0x001E77DE`

```asm
0x001E7786: call 0x1403db020
0x001E778B: int3
0x001E778C: cmp rcx, 0x27
0x001E7790: jbe 0x1401e7798
0x001E7792: call 0x1403db020
0x001E7797: int3
0x001E7798: mov rcx, rax
0x001E779B: call 0x1403b20d4
0x001E77A0: jmp 0x1401e89e4
0x001E77A5: cmp byte ptr [rbp + 0x4190], r15b
0x001E77AC: jne 0x1401e89e4
0x001E77B2: xor edx, edx
0x001E77B4: mov r8d, 0x1cf8
0x001E77BA: lea rcx, [rbp + 0x6e0]
0x001E77C1: call 0x1403d3050
0x001E77C6: mov dword ptr [rbp + 0x6e0], 0x31cf8
0x001E77D0: lea rdx, [rbp + 0x6e0]
0x001E77D7: mov rcx, qword ptr [rsi + 0xd0]
0x001E77DE: call qword ptr [rip + 0x6002b4]
0x001E77E4: mov dword ptr [rsp + 0x20], eax
0x001E77E8: test eax, eax
0x001E77EA: jne 0x1401e89e4
0x001E77F0: mov ebx, r15d
0x001E77F3: mov r8d, dword ptr [rbp + 0x6e8]
0x001E77FA: test r8d, r8d
0x001E77FD: je 0x1401e83b4
```

#### ref `0x001E7AA9`

```asm
0x001E7A40: mov qword ptr [rcx + 0x40], rax
0x001E7A44: movups xmm0, xmmword ptr [r10 + 8]
0x001E7A49: movups xmmword ptr [rbp + 0x23fc], xmm0
0x001E7A50: movups xmm1, xmmword ptr [r10 + 0x18]
0x001E7A55: movups xmmword ptr [rbp + 0x240c], xmm1
0x001E7A5C: movsd xmm0, qword ptr [r10 + 0x28]
0x001E7A62: movsd qword ptr [rbp + 0x241c], xmm0
0x001E7A6A: mov eax, dword ptr [r10 + 0x30]
0x001E7A6E: mov dword ptr [rbp + 0x2424], eax
0x001E7A74: mov dword ptr [rbp + 0x2408], ebx
0x001E7A7A: lea rdx, [rbp + 0x23e0]
0x001E7A81: mov rcx, qword ptr [rsi + 0xd0]
0x001E7A88: call qword ptr [rip + 0x600012]
0x001E7A8E: mov dword ptr [rsp + 0x20], eax
0x001E7A92: cmp eax, -1
0x001E7A95: jne 0x1401e7b81
0x001E7A9B: lea rdx, [rbp + 0x6e0]
0x001E7AA2: mov rcx, qword ptr [rsi + 0xd0]
0x001E7AA9: call qword ptr [rip + 0x5fffe9]
0x001E7AAF: test eax, eax
0x001E7AB1: jne 0x1401e7fac
0x001E7AB7: mov r8d, r15d
0x001E7ABA: mov r10d, dword ptr [rbp + 0x6e8]
0x001E7AC1: test r10d, r10d
0x001E7AC4: je 0x1401e7fac
0x001E7ACA: nop word ptr [rax + rax]
```

#### ref `0x001FE5D9`

```asm
0x001FE56F: mov ecx, 0xdcb616c3
0x001FE574: call qword ptr [rip + 0x5e947e]
0x001FE57A: mov ecx, 0x1bd69f49
0x001FE57F: mov qword ptr [rip + 0x5e94ea], rax
0x001FE586: call qword ptr [rip + 0x5e946c]
0x001FE58C: mov ecx, 0xc16c7e2c
0x001FE591: mov qword ptr [rip + 0x5e94e0], rax
0x001FE598: call qword ptr [rip + 0x5e945a]
0x001FE59E: mov ecx, 0x465f9bcf
0x001FE5A3: mov qword ptr [rip + 0x5e94d6], rax
0x001FE5AA: call qword ptr [rip + 0x5e9448]
0x001FE5B0: mov ecx, 0x927da4f6
0x001FE5B5: mov qword ptr [rip + 0x5e94cc], rax
0x001FE5BC: call qword ptr [rip + 0x5e9436]
0x001FE5C2: mov ecx, 0x6ff81213
0x001FE5C7: mov qword ptr [rip + 0x5e94c2], rax
0x001FE5CE: call qword ptr [rip + 0x5e9424]
0x001FE5D4: mov ecx, 0xf4dae6b
0x001FE5D9: mov qword ptr [rip + 0x5e94b8], rax
0x001FE5E0: call qword ptr [rip + 0x5e9412]
0x001FE5E6: mov ecx, 0x843c0256
0x001FE5EB: mov qword ptr [rip + 0x5e94ae], rax
0x001FE5F2: call qword ptr [rip + 0x5e9400]
0x001FE5F8: mov ecx, 0xedcf624e
0x001FE5FD: mov qword ptr [rip + 0x5e94a4], rax
0x001FE604: call qword ptr [rip + 0x5e93ee]
```

## call `0x001E8B20` function slot `0x007E7AC0`

```asm
0x001E8B01: mov qword ptr [rbp + 0xa4], rax
0x001E8B08: mov qword ptr [rbp + 0xac], rax
0x001E8B0F: mov dword ptr [rbp + 0xb4], eax
0x001E8B15: lea rdx, [rbp + 0x70]
0x001E8B19: mov rcx, qword ptr [rdi + 0xd0]
0x001E8B20: call qword ptr [rip + 0x5fef9a]
0x001E8B26: mov dword ptr [rsp + 0x28], eax
0x001E8B2A: test eax, eax
0x001E8B2C: je 0x1401e8d55
```

### refs to global slot `0x007E7AC0`: `5`

#### ref `0x001E3029`

```asm
0x001E2FDC: int3
0x001E2FDD: int3
0x001E2FDE: int3
0x001E2FDF: int3
0x001E2FE0: mov rax, rsp
0x001E2FE3: push rbp
0x001E2FE4: lea rbp, [rax - 0x168]
0x001E2FEB: sub rsp, 0x260
0x001E2FF2: mov qword ptr [rsp + 0x40], 0xfffffffffffffffe
0x001E2FFB: mov qword ptr [rax + 0x10], rbx
0x001E2FFF: mov qword ptr [rax + 0x18], rsi
0x001E3003: mov qword ptr [rax + 0x20], rdi
0x001E3007: mov rax, qword ptr [rip + 0x5f38e2]
0x001E300E: xor rax, rsp
0x001E3011: mov qword ptr [rbp + 0x150], rax
0x001E3018: mov rbx, rcx
0x001E301B: cmp qword ptr [rcx + 0xd0], 0
0x001E3023: je 0x1401e3e0c
0x001E3029: cmp qword ptr [rip + 0x604a8f], 0
0x001E3031: je 0x1401e3e04
0x001E3037: cmp qword ptr [rip + 0x604a89], 0
0x001E303F: je 0x1401e3e04
0x001E3045: cmp qword ptr [rip + 0x604a6b], 0
0x001E304D: je 0x1401e3e04
0x001E3053: xor esi, esi
0x001E3055: mov edi, esi
```

#### ref `0x001E30B8`

```asm
0x001E304D: je 0x1401e3e04
0x001E3053: xor esi, esi
0x001E3055: mov edi, esi
0x001E3057: mov dword ptr [rsp + 0x20], esi
0x001E305B: call 0x1401ed0b0
0x001E3060: mov dword ptr [rbp + 0xa0], 0x10048
0x001E306A: xor eax, eax
0x001E306C: mov qword ptr [rbp + 0xa4], rax
0x001E3073: mov qword ptr [rbp + 0xac], rax
0x001E307A: mov qword ptr [rbp + 0xb4], rax
0x001E3081: mov qword ptr [rbp + 0xbc], rax
0x001E3088: mov qword ptr [rbp + 0xc4], rax
0x001E308F: mov qword ptr [rbp + 0xcc], rax
0x001E3096: mov qword ptr [rbp + 0xd4], rax
0x001E309D: mov qword ptr [rbp + 0xdc], rax
0x001E30A4: mov dword ptr [rbp + 0xe4], eax
0x001E30AA: lea rdx, [rbp + 0xa0]
0x001E30B1: mov rcx, qword ptr [rbx + 0xd0]
0x001E30B8: call qword ptr [rip + 0x604a02]
0x001E30BE: mov dword ptr [rsp + 0x24], eax
0x001E30C2: test eax, eax
0x001E30C4: je 0x1401e3363
0x001E30CA: mov dword ptr [rsp + 0x28], 0x5e6
0x001E30D2: mov dword ptr [rbp + 0x20], 0x1d
0x001E30D9: mov eax, dword ptr [rbp + 0x20]
0x001E30DC: xor eax, 0x4e
```

#### ref `0x001E8A62`

```asm
0x001E8A13: push rsi
0x001E8A14: push rdi
0x001E8A15: push r14
0x001E8A17: lea rbp, [rsp - 0x150]
0x001E8A1F: sub rsp, 0x250
0x001E8A26: mov qword ptr [rsp + 0x40], 0xfffffffffffffffe
0x001E8A2F: mov rax, qword ptr [rip + 0x5edeba]
0x001E8A36: xor rax, rsp
0x001E8A39: mov qword ptr [rbp + 0x140], rax
0x001E8A40: mov esi, r8d
0x001E8A43: mov rdi, rcx
0x001E8A46: cmp qword ptr [rcx + 0xd0], 0
0x001E8A4E: jne 0x1401e8a62
0x001E8A50: xor eax, eax
0x001E8A52: mov ecx, 2
0x001E8A57: test r8d, r8d
0x001E8A5A: cmovg eax, ecx
0x001E8A5D: jmp 0x1401e9913
0x001E8A62: cmp qword ptr [rip + 0x5ff056], 0
0x001E8A6A: je 0x1401e98f8
0x001E8A70: cmp qword ptr [rip + 0x5ff050], 0
0x001E8A78: je 0x1401e98f8
0x001E8A7E: cmp qword ptr [rip + 0x5ff032], 0
0x001E8A86: je 0x1401e98f8
0x001E8A8C: xor eax, eax
0x001E8A8E: mov dword ptr [rsp + 0x24], eax
```

#### ref `0x001E8B20`

```asm
0x001E8AC3: lea rcx, [rsp + 0x20]
0x001E8AC8: cmp edx, dword ptr [rax]
0x001E8ACA: cmovl rcx, rax
0x001E8ACE: mov ebx, dword ptr [rcx]
0x001E8AD0: mov dword ptr [rsp + 0x20], ebx
0x001E8AD4: mov dword ptr [rbp + 0x70], 0x10048
0x001E8ADB: xor eax, eax
0x001E8ADD: mov qword ptr [rbp + 0x74], rax
0x001E8AE1: mov qword ptr [rbp + 0x7c], rax
0x001E8AE5: mov qword ptr [rbp + 0x84], rax
0x001E8AEC: mov qword ptr [rbp + 0x8c], rax
0x001E8AF3: mov qword ptr [rbp + 0x94], rax
0x001E8AFA: mov qword ptr [rbp + 0x9c], rax
0x001E8B01: mov qword ptr [rbp + 0xa4], rax
0x001E8B08: mov qword ptr [rbp + 0xac], rax
0x001E8B0F: mov dword ptr [rbp + 0xb4], eax
0x001E8B15: lea rdx, [rbp + 0x70]
0x001E8B19: mov rcx, qword ptr [rdi + 0xd0]
0x001E8B20: call qword ptr [rip + 0x5fef9a]
0x001E8B26: mov dword ptr [rsp + 0x28], eax
0x001E8B2A: test eax, eax
0x001E8B2C: je 0x1401e8d55
0x001E8B32: mov dword ptr [rsp + 0x2c], 0x5b5
0x001E8B3A: mov dword ptr [rbp + 0x40], 0x18
0x001E8B41: mov dword ptr [rbp + 0x44], 0x38
0x001E8B48: mov eax, dword ptr [rbp + 0x44]
```

#### ref `0x001FE633`

```asm
0x001FE5C7: mov qword ptr [rip + 0x5e94c2], rax
0x001FE5CE: call qword ptr [rip + 0x5e9424]
0x001FE5D4: mov ecx, 0xf4dae6b
0x001FE5D9: mov qword ptr [rip + 0x5e94b8], rax
0x001FE5E0: call qword ptr [rip + 0x5e9412]
0x001FE5E6: mov ecx, 0x843c0256
0x001FE5EB: mov qword ptr [rip + 0x5e94ae], rax
0x001FE5F2: call qword ptr [rip + 0x5e9400]
0x001FE5F8: mov ecx, 0xedcf624e
0x001FE5FD: mov qword ptr [rip + 0x5e94a4], rax
0x001FE604: call qword ptr [rip + 0x5e93ee]
0x001FE60A: mov ecx, 0x34206d86
0x001FE60F: mov qword ptr [rip + 0x5e949a], rax
0x001FE616: call qword ptr [rip + 0x5e93dc]
0x001FE61C: mov ecx, 0x70916171
0x001FE621: mov qword ptr [rip + 0x5e9490], rax
0x001FE628: call qword ptr [rip + 0x5e93ca]
0x001FE62E: mov ecx, 0xad95f5ed
0x001FE633: mov qword ptr [rip + 0x5e9486], rax
0x001FE63A: call qword ptr [rip + 0x5e93b8]
0x001FE640: mov ecx, 0xfb85b01e
0x001FE645: mov qword ptr [rip + 0x5e947c], rax
0x001FE64C: call qword ptr [rip + 0x5e93a6]
0x001FE652: mov ecx, 0x35aed5e8
0x001FE657: mov qword ptr [rip + 0x5e9472], rax
0x001FE65E: call qword ptr [rip + 0x5e9394]
```

## call `0x001E8D8C` function slot `0x007E7AC8`

```asm
0x001E8D70: cmp eax, 0x3e8
0x001E8D75: jl 0x1401e98f8
0x001E8D7B: mov dword ptr [rbp + 0x80], ebx
0x001E8D81: lea rdx, [rbp + 0x70]
0x001E8D85: mov rcx, qword ptr [rdi + 0xd0]
0x001E8D8C: call qword ptr [rip + 0x5fed36]
0x001E8D92: mov dword ptr [rsp + 0x24], eax
0x001E8D96: test eax, eax
0x001E8D98: jne 0x1401e8f4c
```

### refs to global slot `0x007E7AC8`: `5`

#### ref `0x001E3037`

```asm
0x001E2FDE: int3
0x001E2FDF: int3
0x001E2FE0: mov rax, rsp
0x001E2FE3: push rbp
0x001E2FE4: lea rbp, [rax - 0x168]
0x001E2FEB: sub rsp, 0x260
0x001E2FF2: mov qword ptr [rsp + 0x40], 0xfffffffffffffffe
0x001E2FFB: mov qword ptr [rax + 0x10], rbx
0x001E2FFF: mov qword ptr [rax + 0x18], rsi
0x001E3003: mov qword ptr [rax + 0x20], rdi
0x001E3007: mov rax, qword ptr [rip + 0x5f38e2]
0x001E300E: xor rax, rsp
0x001E3011: mov qword ptr [rbp + 0x150], rax
0x001E3018: mov rbx, rcx
0x001E301B: cmp qword ptr [rcx + 0xd0], 0
0x001E3023: je 0x1401e3e0c
0x001E3029: cmp qword ptr [rip + 0x604a8f], 0
0x001E3031: je 0x1401e3e04
0x001E3037: cmp qword ptr [rip + 0x604a89], 0
0x001E303F: je 0x1401e3e04
0x001E3045: cmp qword ptr [rip + 0x604a6b], 0
0x001E304D: je 0x1401e3e04
0x001E3053: xor esi, esi
0x001E3055: mov edi, esi
0x001E3057: mov dword ptr [rsp + 0x20], esi
0x001E305B: call 0x1401ed0b0
```

#### ref `0x001E3393`

```asm
0x001E3337: call 0x1403db020
0x001E333C: int3
0x001E333D: mov rcx, rax
0x001E3340: call 0x1403b20d4
0x001E3345: mov qword ptr [rbp + 0x90], 0xf
0x001E3350: mov qword ptr [rbp + 0x88], rsi
0x001E3357: mov byte ptr [rbp + 0x78], 0
0x001E335B: mov edi, dword ptr [rsp + 0x24]
0x001E335F: mov dword ptr [rsp + 0x20], edi
0x001E3363: test edi, edi
0x001E3365: jne 0x1401e351f
0x001E336B: cmp dword ptr [rbp + 0xa4], edi
0x001E3371: jbe 0x1401e33a7
0x001E3373: mov esi, dword ptr [rbp + 0xb0]
0x001E3379: mov eax, dword ptr [rbx + 0x140]
0x001E337F: mov dword ptr [rbp + 0xb0], eax
0x001E3385: lea rdx, [rbp + 0xa0]
0x001E338C: mov rcx, qword ptr [rbx + 0xd0]
0x001E3393: call qword ptr [rip + 0x60472f]
0x001E3399: mov edi, eax
0x001E339B: mov dword ptr [rsp + 0x20], eax
0x001E339F: test eax, eax
0x001E33A1: jne 0x1401e351f
0x001E33A7: mov eax, 0x10624dd3
0x001E33AC: imul dword ptr [rbx + 0x140]
0x001E33B2: sar edx, 6
```

#### ref `0x001E8A70`

```asm
0x001E8A15: push r14
0x001E8A17: lea rbp, [rsp - 0x150]
0x001E8A1F: sub rsp, 0x250
0x001E8A26: mov qword ptr [rsp + 0x40], 0xfffffffffffffffe
0x001E8A2F: mov rax, qword ptr [rip + 0x5edeba]
0x001E8A36: xor rax, rsp
0x001E8A39: mov qword ptr [rbp + 0x140], rax
0x001E8A40: mov esi, r8d
0x001E8A43: mov rdi, rcx
0x001E8A46: cmp qword ptr [rcx + 0xd0], 0
0x001E8A4E: jne 0x1401e8a62
0x001E8A50: xor eax, eax
0x001E8A52: mov ecx, 2
0x001E8A57: test r8d, r8d
0x001E8A5A: cmovg eax, ecx
0x001E8A5D: jmp 0x1401e9913
0x001E8A62: cmp qword ptr [rip + 0x5ff056], 0
0x001E8A6A: je 0x1401e98f8
0x001E8A70: cmp qword ptr [rip + 0x5ff050], 0
0x001E8A78: je 0x1401e98f8
0x001E8A7E: cmp qword ptr [rip + 0x5ff032], 0
0x001E8A86: je 0x1401e98f8
0x001E8A8C: xor eax, eax
0x001E8A8E: mov dword ptr [rsp + 0x24], eax
0x001E8A92: lea eax, [rdx + 0x64]
0x001E8A95: imul ebx, eax, 0x3e8
```

#### ref `0x001E8D8C`

```asm
0x001E8D42: call 0x1403db020
0x001E8D47: int3
0x001E8D48: mov rcx, rax
0x001E8D4B: call 0x1403b20d4
0x001E8D50: jmp 0x1401e98f8
0x001E8D55: cmp dword ptr [rbp + 0x74], 0
0x001E8D59: jbe 0x1401e98f8
0x001E8D5F: mov eax, ebx
0x001E8D61: mov r14d, dword ptr [rbp + 0x80]
0x001E8D68: sub eax, r14d
0x001E8D6B: cdq
0x001E8D6C: xor eax, edx
0x001E8D6E: sub eax, edx
0x001E8D70: cmp eax, 0x3e8
0x001E8D75: jl 0x1401e98f8
0x001E8D7B: mov dword ptr [rbp + 0x80], ebx
0x001E8D81: lea rdx, [rbp + 0x70]
0x001E8D85: mov rcx, qword ptr [rdi + 0xd0]
0x001E8D8C: call qword ptr [rip + 0x5fed36]
0x001E8D92: mov dword ptr [rsp + 0x24], eax
0x001E8D96: test eax, eax
0x001E8D98: jne 0x1401e8f4c
0x001E8D9E: mov eax, 0x10624dd3
0x001E8DA3: imul ebx
0x001E8DA5: sar edx, 6
0x001E8DA8: mov eax, edx
```

#### ref `0x001FE645`

```asm
0x001FE5D9: mov qword ptr [rip + 0x5e94b8], rax
0x001FE5E0: call qword ptr [rip + 0x5e9412]
0x001FE5E6: mov ecx, 0x843c0256
0x001FE5EB: mov qword ptr [rip + 0x5e94ae], rax
0x001FE5F2: call qword ptr [rip + 0x5e9400]
0x001FE5F8: mov ecx, 0xedcf624e
0x001FE5FD: mov qword ptr [rip + 0x5e94a4], rax
0x001FE604: call qword ptr [rip + 0x5e93ee]
0x001FE60A: mov ecx, 0x34206d86
0x001FE60F: mov qword ptr [rip + 0x5e949a], rax
0x001FE616: call qword ptr [rip + 0x5e93dc]
0x001FE61C: mov ecx, 0x70916171
0x001FE621: mov qword ptr [rip + 0x5e9490], rax
0x001FE628: call qword ptr [rip + 0x5e93ca]
0x001FE62E: mov ecx, 0xad95f5ed
0x001FE633: mov qword ptr [rip + 0x5e9486], rax
0x001FE63A: call qword ptr [rip + 0x5e93b8]
0x001FE640: mov ecx, 0xfb85b01e
0x001FE645: mov qword ptr [rip + 0x5e947c], rax
0x001FE64C: call qword ptr [rip + 0x5e93a6]
0x001FE652: mov ecx, 0x35aed5e8
0x001FE657: mov qword ptr [rip + 0x5e9472], rax
0x001FE65E: call qword ptr [rip + 0x5e9394]
0x001FE664: mov ecx, 0x814b209f
0x001FE669: mov qword ptr [rip + 0x5e9468], rax
0x001FE670: call qword ptr [rip + 0x5e9382]
```

## call `0x001E99B4` function slot `0x007E7A50`

```asm
0x001E9990: lea rcx, [rbp + 0x130]
0x001E9997: call 0x1403d3050
0x001E999C: mov dword ptr [rbp + 0x130], 0x20068
0x001E99A6: lea rdx, [rbp + 0x130]
0x001E99AD: mov rcx, qword ptr [rdi + 0xd0]
0x001E99B4: call qword ptr [rip + 0x5fe096]
0x001E99BA: mov dword ptr [rsp + 0x24], eax
0x001E99BE: test eax, eax
0x001E99C0: je 0x1401e9c27
```

### refs to global slot `0x007E7A50`: `3`

#### ref `0x001E3EC8`

```asm
0x001E3E67: mov rax, qword ptr [rip + 0x5f2a82]
0x001E3E6E: xor rax, rsp
0x001E3E71: mov qword ptr [rbp + 0x210], rax
0x001E3E78: mov rdi, rcx
0x001E3E7B: cmp byte ptr [rcx + 0xe4], 0
0x001E3E82: je 0x1401e512e
0x001E3E88: cmp qword ptr [rcx + 0xd0], 0
0x001E3E90: je 0x1401e512e
0x001E3E96: xor ebx, ebx
0x001E3E98: mov esi, ebx
0x001E3E9A: mov dword ptr [rsp + 0x20], ebx
0x001E3E9E: xor edx, edx
0x001E3EA0: lea r8d, [rbx + 0x68]
0x001E3EA4: lea rcx, [rbp + 0x1a0]
0x001E3EAB: call 0x1403d3050
0x001E3EB0: mov dword ptr [rbp + 0x1a0], 0x20068
0x001E3EBA: lea rdx, [rbp + 0x1a0]
0x001E3EC1: mov rcx, qword ptr [rdi + 0xd0]
0x001E3EC8: call qword ptr [rip + 0x603b82]
0x001E3ECE: mov dword ptr [rsp + 0x2c], eax
0x001E3ED2: test eax, eax
0x001E3ED4: je 0x1401e41b1
0x001E3EDA: mov dword ptr [rsp + 0x34], 0x55a
0x001E3EE2: mov dword ptr [rbp + 0x60], 0x7f
0x001E3EE9: mov eax, dword ptr [rbp + 0x60]
0x001E3EEC: xor eax, 0x4e
```

#### ref `0x001E99B4`

```asm
0x001E9960: mov qword ptr [rbp + 0x200], rax
0x001E9967: mov ebx, edx
0x001E9969: mov rdi, rcx
0x001E996C: mov dword ptr [rsp + 0x28], edx
0x001E9970: xor r14b, r14b
0x001E9973: cmp qword ptr [rcx + 0xd0], 0
0x001E997B: jne 0x1401e9984
0x001E997D: xor al, al
0x001E997F: jmp 0x1401eae3d
0x001E9984: xor esi, esi
0x001E9986: mov dword ptr [rsp + 0x20], esi
0x001E998A: xor edx, edx
0x001E998C: lea r8d, [rsi + 0x68]
0x001E9990: lea rcx, [rbp + 0x130]
0x001E9997: call 0x1403d3050
0x001E999C: mov dword ptr [rbp + 0x130], 0x20068
0x001E99A6: lea rdx, [rbp + 0x130]
0x001E99AD: mov rcx, qword ptr [rdi + 0xd0]
0x001E99B4: call qword ptr [rip + 0x5fe096]
0x001E99BA: mov dword ptr [rsp + 0x24], eax
0x001E99BE: test eax, eax
0x001E99C0: je 0x1401e9c27
0x001E99C6: mov dword ptr [rsp + 0x3c], 0x518
0x001E99CE: mov dword ptr [rbp + 0x58], 0x25
0x001E99D5: mov dword ptr [rbp + 0x5c], 0x46
0x001E99DC: mov eax, dword ptr [rbp + 0x5c]
```

#### ref `0x001FE50E`

```asm
0x001FE4AB: mov qword ptr [rip + 0x5e957e], rax
0x001FE4B2: test rax, rax
0x001FE4B5: je 0x1401fe296
0x001FE4BB: mov ecx, 0xda141340
0x001FE4C0: call qword ptr [rip + 0x5e9532]
0x001FE4C6: mov qword ptr [rip + 0x5e956b], rax
0x001FE4CD: test rax, rax
0x001FE4D0: je 0x1401fe296
0x001FE4D6: mov ecx, 0x891fa0ae
0x001FE4DB: call qword ptr [rip + 0x5e9517]
0x001FE4E1: mov qword ptr [rip + 0x5e9558], rax
0x001FE4E8: test rax, rax
0x001FE4EB: je 0x1401fe296
0x001FE4F1: mov ecx, 0x8f6ed0fb
0x001FE4F6: call qword ptr [rip + 0x5e94fc]
0x001FE4FC: mov ecx, 0xd258bb5
0x001FE501: mov qword ptr [rip + 0x5e9540], rax
0x001FE508: call qword ptr [rip + 0x5e94ea]
0x001FE50E: mov qword ptr [rip + 0x5e953b], rax
0x001FE515: test rax, rax
0x001FE518: je 0x1401fe296
0x001FE51E: mov ecx, 0xe9c425a1
0x001FE523: call qword ptr [rip + 0x5e94cf]
0x001FE529: mov qword ptr [rip + 0x5e9528], rax
0x001FE530: test rax, rax
0x001FE533: je 0x1401fe296
```

## call `0x001E9CD3` function slot `0x007E7A58`

```asm
0x001E9CAD: mov qword ptr [rbp + 0xe0], rax
0x001E9CB4: mov qword ptr [rbp + 0xe8], rax
0x001E9CBB: mov dword ptr [rbp + 0xb8], 0x20038
0x001E9CC5: lea rdx, [rbp + 0xb8]
0x001E9CCC: mov rcx, qword ptr [rdi + 0xd0]
0x001E9CD3: call qword ptr [rip + 0x5fdd7f]
0x001E9CD9: mov dword ptr [rsp + 0x44], eax
0x001E9CDD: test eax, eax
0x001E9CDF: je 0x1401e9ff5
```

### refs to global slot `0x007E7A58`: `3`

#### ref `0x001E425E`

```asm
0x001E41FA: cmp eax, 0x37
0x001E41FD: cmovle rcx, rdx
0x001E4201: lea rax, [rsp + 0x38]
0x001E4206: cmp dword ptr [rcx], 0x5a
0x001E4209: cmovl rax, rcx
0x001E420D: mov ebx, dword ptr [rax]
0x001E420F: mov dword ptr [rsp + 0x24], ebx
0x001E4213: xor eax, eax
0x001E4215: mov qword ptr [rbp + 0xc0], rax
0x001E421C: mov qword ptr [rbp + 0xc8], rax
0x001E4223: mov qword ptr [rbp + 0xd0], rax
0x001E422A: mov qword ptr [rbp + 0xd8], rax
0x001E4231: mov qword ptr [rbp + 0xe0], rax
0x001E4238: mov qword ptr [rbp + 0xe8], rax
0x001E423F: mov qword ptr [rbp + 0xf0], rax
0x001E4246: mov dword ptr [rbp + 0xc0], 0x20038
0x001E4250: lea rdx, [rbp + 0xc0]
0x001E4257: mov rcx, qword ptr [rdi + 0xd0]
0x001E425E: call qword ptr [rip + 0x6037f4]
0x001E4264: mov dword ptr [rsp + 0x3c], eax
0x001E4268: test eax, eax
0x001E426A: je 0x1401e45e4
0x001E4270: mov dword ptr [rsp + 0x40], 0x568
0x001E4278: mov dword ptr [rbp + 0x90], 8
0x001E4282: mov eax, dword ptr [rbp + 0x90]
0x001E4288: xor eax, 0x4e
```

#### ref `0x001E9CD3`

```asm
0x001E9C71: cmp eax, ebx
0x001E9C73: cmovge rcx, r8
0x001E9C77: lea rax, [rsp + 0x40]
0x001E9C7C: cmp dword ptr [rcx], edx
0x001E9C7E: cmovl rax, rcx
0x001E9C82: mov ebx, dword ptr [rax]
0x001E9C84: mov dword ptr [rsp + 0x34], ebx
0x001E9C88: xor eax, eax
0x001E9C8A: mov qword ptr [rbp + 0xb8], rax
0x001E9C91: mov qword ptr [rbp + 0xc0], rax
0x001E9C98: mov qword ptr [rbp + 0xc8], rax
0x001E9C9F: mov qword ptr [rbp + 0xd0], rax
0x001E9CA6: mov qword ptr [rbp + 0xd8], rax
0x001E9CAD: mov qword ptr [rbp + 0xe0], rax
0x001E9CB4: mov qword ptr [rbp + 0xe8], rax
0x001E9CBB: mov dword ptr [rbp + 0xb8], 0x20038
0x001E9CC5: lea rdx, [rbp + 0xb8]
0x001E9CCC: mov rcx, qword ptr [rdi + 0xd0]
0x001E9CD3: call qword ptr [rip + 0x5fdd7f]
0x001E9CD9: mov dword ptr [rsp + 0x44], eax
0x001E9CDD: test eax, eax
0x001E9CDF: je 0x1401e9ff5
0x001E9CE5: mov dword ptr [rsp + 0x48], 0x528
0x001E9CED: mov dword ptr [rbp + 0x88], 0x1c
0x001E9CF7: mov dword ptr [rbp + 0x8c], 0x63
0x001E9D01: mov eax, dword ptr [rbp + 0x8c]
```

#### ref `0x001FE529`

```asm
0x001FE4C6: mov qword ptr [rip + 0x5e956b], rax
0x001FE4CD: test rax, rax
0x001FE4D0: je 0x1401fe296
0x001FE4D6: mov ecx, 0x891fa0ae
0x001FE4DB: call qword ptr [rip + 0x5e9517]
0x001FE4E1: mov qword ptr [rip + 0x5e9558], rax
0x001FE4E8: test rax, rax
0x001FE4EB: je 0x1401fe296
0x001FE4F1: mov ecx, 0x8f6ed0fb
0x001FE4F6: call qword ptr [rip + 0x5e94fc]
0x001FE4FC: mov ecx, 0xd258bb5
0x001FE501: mov qword ptr [rip + 0x5e9540], rax
0x001FE508: call qword ptr [rip + 0x5e94ea]
0x001FE50E: mov qword ptr [rip + 0x5e953b], rax
0x001FE515: test rax, rax
0x001FE518: je 0x1401fe296
0x001FE51E: mov ecx, 0xe9c425a1
0x001FE523: call qword ptr [rip + 0x5e94cf]
0x001FE529: mov qword ptr [rip + 0x5e9528], rax
0x001FE530: test rax, rax
0x001FE533: je 0x1401fe296
0x001FE539: mov ecx, 0x34c0b13d
0x001FE53E: call qword ptr [rip + 0x5e94b4]
0x001FE544: mov qword ptr [rip + 0x5e9515], rax
0x001FE54B: test rax, rax
0x001FE54E: je 0x1401fe296
```

## call `0x001EA039` function slot `0x007E7A60`

```asm
0x001EA01C: mov dword ptr [rbp + 0xc4], ebx
0x001EA022: or ecx, 1
0x001EA025: mov dword ptr [rbp + 0xc8], ecx
0x001EA02B: lea rdx, [rbp + 0xb8]
0x001EA032: mov rcx, qword ptr [rdi + 0xd0]
0x001EA039: call qword ptr [rip + 0x5fda21]
0x001EA03F: mov dword ptr [rsp + 0x20], eax
0x001EA043: test eax, eax
0x001EA045: jne 0x1401ea20e
```

### refs to global slot `0x007E7A60`: `3`

#### ref `0x001E4624`

```asm
0x001E45D6: int3
0x001E45D7: mov rcx, rax
0x001E45DA: call 0x1403b20d4
0x001E45DF: jmp 0x1401e512e
0x001E45E4: mov eax, dword ptr [rbp + 0xcc]
0x001E45EA: shr eax, 8
0x001E45ED: mov dword ptr [rsp + 0x30], eax
0x001E45F1: mov ecx, dword ptr [rbp + 0xd0]
0x001E45F7: cmp eax, ebx
0x001E45F9: jne 0x1401e4604
0x001E45FB: test cl, 1
0x001E45FE: jne 0x1401e512e
0x001E4604: shl ebx, 8
0x001E4607: mov dword ptr [rbp + 0xcc], ebx
0x001E460D: or ecx, 1
0x001E4610: mov dword ptr [rbp + 0xd0], ecx
0x001E4616: lea rdx, [rbp + 0xc0]
0x001E461D: mov rcx, qword ptr [rdi + 0xd0]
0x001E4624: call qword ptr [rip + 0x603436]
0x001E462A: mov dword ptr [rsp + 0x20], eax
0x001E462E: test eax, eax
0x001E4630: jne 0x1401e47f1
0x001E4636: mov dword ptr [rbp - 0x10], 0x3e
0x001E463D: mov eax, dword ptr [rbp - 0x10]
0x001E4640: xor eax, 0x7b
0x001E4643: inc eax
```

#### ref `0x001EA039`

```asm
0x001E9FEB: call 0x1403b20d4
0x001E9FF0: jmp 0x1401eae32
0x001E9FF5: mov eax, dword ptr [rbp + 0xc4]
0x001E9FFB: shr eax, 8
0x001E9FFE: mov dword ptr [rsp + 0x30], eax
0x001EA002: mov ecx, dword ptr [rbp + 0xc8]
0x001EA008: cmp eax, ebx
0x001EA00A: jne 0x1401ea019
0x001EA00C: test cl, 1
0x001EA00F: je 0x1401ea019
0x001EA011: mov r14b, 1
0x001EA014: jmp 0x1401eae32
0x001EA019: shl ebx, 8
0x001EA01C: mov dword ptr [rbp + 0xc4], ebx
0x001EA022: or ecx, 1
0x001EA025: mov dword ptr [rbp + 0xc8], ecx
0x001EA02B: lea rdx, [rbp + 0xb8]
0x001EA032: mov rcx, qword ptr [rdi + 0xd0]
0x001EA039: call qword ptr [rip + 0x5fda21]
0x001EA03F: mov dword ptr [rsp + 0x20], eax
0x001EA043: test eax, eax
0x001EA045: jne 0x1401ea20e
0x001EA04B: mov r14b, 1
0x001EA04E: mov dword ptr [rbp + 0x30], 0xffffff83
0x001EA055: mov eax, dword ptr [rbp + 0x30]
0x001EA058: xor eax, 0x7b
```

#### ref `0x001FE544`

```asm
0x001FE4E1: mov qword ptr [rip + 0x5e9558], rax
0x001FE4E8: test rax, rax
0x001FE4EB: je 0x1401fe296
0x001FE4F1: mov ecx, 0x8f6ed0fb
0x001FE4F6: call qword ptr [rip + 0x5e94fc]
0x001FE4FC: mov ecx, 0xd258bb5
0x001FE501: mov qword ptr [rip + 0x5e9540], rax
0x001FE508: call qword ptr [rip + 0x5e94ea]
0x001FE50E: mov qword ptr [rip + 0x5e953b], rax
0x001FE515: test rax, rax
0x001FE518: je 0x1401fe296
0x001FE51E: mov ecx, 0xe9c425a1
0x001FE523: call qword ptr [rip + 0x5e94cf]
0x001FE529: mov qword ptr [rip + 0x5e9528], rax
0x001FE530: test rax, rax
0x001FE533: je 0x1401fe296
0x001FE539: mov ecx, 0x34c0b13d
0x001FE53E: call qword ptr [rip + 0x5e94b4]
0x001FE544: mov qword ptr [rip + 0x5e9515], rax
0x001FE54B: test rax, rax
0x001FE54E: je 0x1401fe296
0x001FE554: mov ecx, 0xe3640a56
0x001FE559: call qword ptr [rip + 0x5e9499]
0x001FE55F: mov qword ptr [rip + 0x5e9502], rax
0x001FE566: test rax, rax
0x001FE569: je 0x1401fe296
```

## call `0x001ECCB6` function slot `0x007E7B08`

```asm
0x001ECCA1: shl esi, 0x10
0x001ECCA4: mov eax, esi
0x001ECCA6: mov qword ptr [rbp - 0x78], rax
0x001ECCAA: lea rdx, [rsp + 0x70]
0x001ECCAF: mov rcx, qword ptr [rbx + 0xd0]
0x001ECCB6: call qword ptr [rip + 0x5fae4c]
0x001ECCBC: test eax, eax
0x001ECCBE: je 0x1401eccc5
0x001ECCC0: xor dil, dil
```

### refs to global slot `0x007E7B08`: `7`

#### ref `0x001E0CCE`

```asm
0x001E0C96: add rsp, 0x20
0x001E0C9A: pop rdi
0x001E0C9B: ret
0x001E0C9C: int3
0x001E0C9D: int3
0x001E0C9E: int3
0x001E0C9F: int3
0x001E0CA0: mov qword ptr [rsp + 0x18], rbx
0x001E0CA5: push rbp
0x001E0CA6: push rsi
0x001E0CA7: push rdi
0x001E0CA8: lea rbp, [rsp - 0x1740]
0x001E0CB0: mov eax, 0x1840
0x001E0CB5: call 0x1403b2500
0x001E0CBA: sub rsp, rax
0x001E0CBD: mov rax, qword ptr [rip + 0x5f5c2c]
0x001E0CC4: xor rax, rsp
0x001E0CC7: mov qword ptr [rbp + 0x1730], rax
0x001E0CCE: mov rdi, qword ptr [rip + 0x606e33]
0x001E0CD5: mov rbx, rdx
0x001E0CD8: mov rsi, rcx
0x001E0CDB: test rdi, rdi
0x001E0CDE: jne 0x1401e0ce7
0x001E0CE0: xor al, al
0x001E0CE2: jmp 0x1401e0e9e
0x001E0CE7: xor edx, edx
```

#### ref `0x001ECC46`

```asm
0x001ECC07: jne 0x1401ecc43
0x001ECC09: cmp dword ptr [rbx + 0x25c], 0
0x001ECC10: jne 0x1401ecc43
0x001ECC12: xor eax, eax
0x001ECC14: mov byte ptr [rsp + 0x20], al
0x001ECC18: lea rcx, [rbx + 0x26c]
0x001ECC1F: lea rax, [rbx + 0x260]
0x001ECC26: cmp rax, rcx
0x001ECC29: je 0x1401ecc3e
0x001ECC2B: nop dword ptr [rax + rax]
0x001ECC30: cmp dword ptr [rax], 0
0x001ECC33: jne 0x1401ecc43
0x001ECC35: add rax, 4
0x001ECC39: cmp rax, rcx
0x001ECC3C: jne 0x1401ecc30
0x001ECC3E: mov r13b, 1
0x001ECC41: jmp 0x1401ecc46
0x001ECC43: xor r13b, r13b
0x001ECC46: cmp qword ptr [rip + 0x5faeba], 0
0x001ECC4E: jne 0x1401ecc57
0x001ECC50: xor al, al
0x001ECC52: jmp 0x1401ed081
0x001ECC57: mov esi, dword ptr [r14 + 0x2c]
0x001ECC5B: test esi, esi
0x001ECC5D: je 0x1401eccc8
0x001ECC5F: cmp esi, dword ptr [r15 + 0x2c]
```

#### ref `0x001ECCB6`

```asm
0x001ECC5D: je 0x1401eccc8
0x001ECC5F: cmp esi, dword ptr [r15 + 0x2c]
0x001ECC63: je 0x1401eccc8
0x001ECC65: xor edx, edx
0x001ECC67: mov r8d, 0x1808
0x001ECC6D: lea rcx, [rsp + 0x70]
0x001ECC72: call 0x1403d3050
0x001ECC77: mov dword ptr [rsp + 0x70], 0x11808
0x001ECC7F: mov dword ptr [rsp + 0x74], 1
0x001ECC87: mov eax, 0x16
0x001ECC8C: mov word ptr [rsp + 0x78], ax
0x001ECC91: mov dword ptr [rsp + 0x7c], 0x9a0298
0x001ECC99: mov qword ptr [rbp - 0x80], 0x7f0000
0x001ECCA1: shl esi, 0x10
0x001ECCA4: mov eax, esi
0x001ECCA6: mov qword ptr [rbp - 0x78], rax
0x001ECCAA: lea rdx, [rsp + 0x70]
0x001ECCAF: mov rcx, qword ptr [rbx + 0xd0]
0x001ECCB6: call qword ptr [rip + 0x5fae4c]
0x001ECCBC: test eax, eax
0x001ECCBE: je 0x1401eccc5
0x001ECCC0: xor dil, dil
0x001ECCC3: jmp 0x1401eccc8
0x001ECCC5: mov r12b, 1
0x001ECCC8: mov esi, dword ptr [r14 + 0x38]
0x001ECCCC: test esi, esi
```

#### ref `0x001ECD39`

```asm
0x001ECCCE: je 0x1401ecd4b
0x001ECCD0: cmp esi, dword ptr [r15 + 0x38]
0x001ECCD4: je 0x1401ecd4b
0x001ECCD6: xor edx, edx
0x001ECCD8: mov r8d, 0x1808
0x001ECCDE: lea rcx, [rbp + 0x1780]
0x001ECCE5: call 0x1403d3050
0x001ECCEA: mov dword ptr [rbp + 0x1780], 0x11808
0x001ECCF4: mov dword ptr [rbp + 0x1784], 1
0x001ECCFE: mov eax, 0x16
0x001ECD03: mov word ptr [rbp + 0x1788], ax
0x001ECD0A: mov dword ptr [rbp + 0x178c], 0x9a029c
0x001ECD14: mov qword ptr [rbp + 0x1790], 0x1fe00
0x001ECD1F: shl esi, 9
0x001ECD22: mov eax, esi
0x001ECD24: mov qword ptr [rbp + 0x1798], rax
0x001ECD2B: lea rdx, [rbp + 0x1780]
0x001ECD32: mov rcx, qword ptr [rbx + 0xd0]
0x001ECD39: call qword ptr [rip + 0x5fadc9]
0x001ECD3F: test eax, eax
0x001ECD41: je 0x1401ecd48
0x001ECD43: xor dil, dil
0x001ECD46: jmp 0x1401ecd4b
0x001ECD48: mov r12b, 1
0x001ECD4B: mov esi, dword ptr [r14 + 0x44]
0x001ECD4F: test esi, esi
```

#### ref `0x001ECDBC`

```asm
0x001ECD51: je 0x1401ecdce
0x001ECD53: cmp esi, dword ptr [r15 + 0x44]
0x001ECD57: je 0x1401ecdce
0x001ECD59: xor edx, edx
0x001ECD5B: mov r8d, 0x1808
0x001ECD61: lea rcx, [rbp + 0x2f90]
0x001ECD68: call 0x1403d3050
0x001ECD6D: mov dword ptr [rbp + 0x2f90], 0x11808
0x001ECD77: mov dword ptr [rbp + 0x2f94], 1
0x001ECD81: mov eax, 0x16
0x001ECD86: mov word ptr [rbp + 0x2f98], ax
0x001ECD8D: mov dword ptr [rbp + 0x2f9c], 0x9a02a0
0x001ECD97: mov qword ptr [rbp + 0x2fa0], 0x1f8000
0x001ECDA2: shl esi, 0xf
0x001ECDA5: mov eax, esi
0x001ECDA7: mov qword ptr [rbp + 0x2fa8], rax
0x001ECDAE: lea rdx, [rbp + 0x2f90]
0x001ECDB5: mov rcx, qword ptr [rbx + 0xd0]
0x001ECDBC: call qword ptr [rip + 0x5fad46]
0x001ECDC2: test eax, eax
0x001ECDC4: je 0x1401ecdcb
0x001ECDC6: xor dil, dil
0x001ECDC9: jmp 0x1401ecdce
0x001ECDCB: mov r12b, 1
0x001ECDCE: mov esi, dword ptr [r14 + 8]
0x001ECDD2: test esi, esi
```

#### ref `0x001ECE3F`

```asm
0x001ECDD4: je 0x1401ece4c
0x001ECDD6: cmp esi, dword ptr [r15 + 8]
0x001ECDDA: je 0x1401ece4c
0x001ECDDC: xor edx, edx
0x001ECDDE: mov r8d, 0x1808
0x001ECDE4: lea rcx, [rbp + 0x47a0]
0x001ECDEB: call 0x1403d3050
0x001ECDF0: mov dword ptr [rbp + 0x47a0], 0x11808
0x001ECDFA: mov dword ptr [rbp + 0x47a4], 1
0x001ECE04: mov eax, 0x16
0x001ECE09: mov word ptr [rbp + 0x47a8], ax
0x001ECE10: mov dword ptr [rbp + 0x47ac], 0x9a0290
0x001ECE1A: mov qword ptr [rbp + 0x47b0], 0x1ff00
0x001ECE25: shl esi, 8
0x001ECE28: mov eax, esi
0x001ECE2A: mov qword ptr [rbp + 0x47b8], rax
0x001ECE31: lea rdx, [rbp + 0x47a0]
0x001ECE38: mov rcx, qword ptr [rbx + 0xd0]
0x001ECE3F: call qword ptr [rip + 0x5facc3]
0x001ECE45: test eax, eax
0x001ECE47: je 0x1401ece55
0x001ECE49: xor dil, dil
0x001ECE4C: test r12b, r12b
0x001ECE4F: je 0x1401ed07d
0x001ECE55: movsxd rax, dword ptr [rsp + 0x24]
0x001ECE5A: mov byte ptr [rax + rbx + 0x280], 1
```

#### ref `0x001FE6D5`

```asm
0x001FE669: mov qword ptr [rip + 0x5e9468], rax
0x001FE670: call qword ptr [rip + 0x5e9382]
0x001FE676: mov ecx, 0xa58971a5
0x001FE67B: mov qword ptr [rip + 0x5e945e], rax
0x001FE682: call qword ptr [rip + 0x5e9370]
0x001FE688: mov ecx, 0x57f7caac
0x001FE68D: mov qword ptr [rip + 0x5e9454], rax
0x001FE694: call qword ptr [rip + 0x5e935e]
0x001FE69A: mov ecx, 0x42aea16a
0x001FE69F: mov qword ptr [rip + 0x5e944a], rax
0x001FE6A6: call qword ptr [rip + 0x5e934c]
0x001FE6AC: mov ecx, 0x2ddfb66e
0x001FE6B1: mov qword ptr [rip + 0x5e9440], rax
0x001FE6B8: call qword ptr [rip + 0x5e933a]
0x001FE6BE: mov ecx, 0x2eb3c140
0x001FE6C3: mov qword ptr [rip + 0x5e9436], rax
0x001FE6CA: call qword ptr [rip + 0x5e9328]
0x001FE6D0: mov ecx, 0x65fe3aad
0x001FE6D5: mov qword ptr [rip + 0x5e942c], rax
0x001FE6DC: call qword ptr [rip + 0x5e9316]
0x001FE6E2: mov qword ptr [rip + 0x5e9427], rax
0x001FE6E9: mov al, 1
0x001FE6EB: mov rcx, qword ptr [rbp + 0x4f]
0x001FE6EF: xor rcx, rsp
0x001FE6F2: call 0x1403b24c0
0x001FE6F7: add rsp, 0xa0
```

## call `0x001ECCE5` function slot `unknown`

```asm
0x001ECCA1: shl esi, 0x10
0x001ECCA4: mov eax, esi
0x001ECCA6: mov qword ptr [rbp - 0x78], rax
0x001ECCAA: lea rdx, [rsp + 0x70]
0x001ECCAF: mov rcx, qword ptr [rbx + 0xd0]
0x001ECCB6: call qword ptr [rip + 0x5fae4c]
0x001ECCBC: test eax, eax
0x001ECCBE: je 0x1401eccc5
0x001ECCC0: xor dil, dil
0x001ECCC3: jmp 0x1401eccc8
0x001ECCC5: mov r12b, 1
0x001ECCC8: mov esi, dword ptr [r14 + 0x38]
0x001ECCCC: test esi, esi
0x001ECCCE: je 0x1401ecd4b
0x001ECCD0: cmp esi, dword ptr [r15 + 0x38]
0x001ECCD4: je 0x1401ecd4b
0x001ECCD6: xor edx, edx
0x001ECCD8: mov r8d, 0x1808
0x001ECCDE: lea rcx, [rbp + 0x1780]
0x001ECCE5: call 0x1403d3050
0x001ECCEA: mov dword ptr [rbp + 0x1780], 0x11808
0x001ECCF4: mov dword ptr [rbp + 0x1784], 1
0x001ECCFE: mov eax, 0x16
```

## call `0x001ECD39` function slot `0x007E7B08`

```asm
0x001ECD1F: shl esi, 9
0x001ECD22: mov eax, esi
0x001ECD24: mov qword ptr [rbp + 0x1798], rax
0x001ECD2B: lea rdx, [rbp + 0x1780]
0x001ECD32: mov rcx, qword ptr [rbx + 0xd0]
0x001ECD39: call qword ptr [rip + 0x5fadc9]
0x001ECD3F: test eax, eax
0x001ECD41: je 0x1401ecd48
0x001ECD43: xor dil, dil
```

### refs to global slot `0x007E7B08`: `7`

#### ref `0x001E0CCE`

```asm
0x001E0C96: add rsp, 0x20
0x001E0C9A: pop rdi
0x001E0C9B: ret
0x001E0C9C: int3
0x001E0C9D: int3
0x001E0C9E: int3
0x001E0C9F: int3
0x001E0CA0: mov qword ptr [rsp + 0x18], rbx
0x001E0CA5: push rbp
0x001E0CA6: push rsi
0x001E0CA7: push rdi
0x001E0CA8: lea rbp, [rsp - 0x1740]
0x001E0CB0: mov eax, 0x1840
0x001E0CB5: call 0x1403b2500
0x001E0CBA: sub rsp, rax
0x001E0CBD: mov rax, qword ptr [rip + 0x5f5c2c]
0x001E0CC4: xor rax, rsp
0x001E0CC7: mov qword ptr [rbp + 0x1730], rax
0x001E0CCE: mov rdi, qword ptr [rip + 0x606e33]
0x001E0CD5: mov rbx, rdx
0x001E0CD8: mov rsi, rcx
0x001E0CDB: test rdi, rdi
0x001E0CDE: jne 0x1401e0ce7
0x001E0CE0: xor al, al
0x001E0CE2: jmp 0x1401e0e9e
0x001E0CE7: xor edx, edx
```

#### ref `0x001ECC46`

```asm
0x001ECC07: jne 0x1401ecc43
0x001ECC09: cmp dword ptr [rbx + 0x25c], 0
0x001ECC10: jne 0x1401ecc43
0x001ECC12: xor eax, eax
0x001ECC14: mov byte ptr [rsp + 0x20], al
0x001ECC18: lea rcx, [rbx + 0x26c]
0x001ECC1F: lea rax, [rbx + 0x260]
0x001ECC26: cmp rax, rcx
0x001ECC29: je 0x1401ecc3e
0x001ECC2B: nop dword ptr [rax + rax]
0x001ECC30: cmp dword ptr [rax], 0
0x001ECC33: jne 0x1401ecc43
0x001ECC35: add rax, 4
0x001ECC39: cmp rax, rcx
0x001ECC3C: jne 0x1401ecc30
0x001ECC3E: mov r13b, 1
0x001ECC41: jmp 0x1401ecc46
0x001ECC43: xor r13b, r13b
0x001ECC46: cmp qword ptr [rip + 0x5faeba], 0
0x001ECC4E: jne 0x1401ecc57
0x001ECC50: xor al, al
0x001ECC52: jmp 0x1401ed081
0x001ECC57: mov esi, dword ptr [r14 + 0x2c]
0x001ECC5B: test esi, esi
0x001ECC5D: je 0x1401eccc8
0x001ECC5F: cmp esi, dword ptr [r15 + 0x2c]
```

#### ref `0x001ECCB6`

```asm
0x001ECC5D: je 0x1401eccc8
0x001ECC5F: cmp esi, dword ptr [r15 + 0x2c]
0x001ECC63: je 0x1401eccc8
0x001ECC65: xor edx, edx
0x001ECC67: mov r8d, 0x1808
0x001ECC6D: lea rcx, [rsp + 0x70]
0x001ECC72: call 0x1403d3050
0x001ECC77: mov dword ptr [rsp + 0x70], 0x11808
0x001ECC7F: mov dword ptr [rsp + 0x74], 1
0x001ECC87: mov eax, 0x16
0x001ECC8C: mov word ptr [rsp + 0x78], ax
0x001ECC91: mov dword ptr [rsp + 0x7c], 0x9a0298
0x001ECC99: mov qword ptr [rbp - 0x80], 0x7f0000
0x001ECCA1: shl esi, 0x10
0x001ECCA4: mov eax, esi
0x001ECCA6: mov qword ptr [rbp - 0x78], rax
0x001ECCAA: lea rdx, [rsp + 0x70]
0x001ECCAF: mov rcx, qword ptr [rbx + 0xd0]
0x001ECCB6: call qword ptr [rip + 0x5fae4c]
0x001ECCBC: test eax, eax
0x001ECCBE: je 0x1401eccc5
0x001ECCC0: xor dil, dil
0x001ECCC3: jmp 0x1401eccc8
0x001ECCC5: mov r12b, 1
0x001ECCC8: mov esi, dword ptr [r14 + 0x38]
0x001ECCCC: test esi, esi
```

#### ref `0x001ECD39`

```asm
0x001ECCCE: je 0x1401ecd4b
0x001ECCD0: cmp esi, dword ptr [r15 + 0x38]
0x001ECCD4: je 0x1401ecd4b
0x001ECCD6: xor edx, edx
0x001ECCD8: mov r8d, 0x1808
0x001ECCDE: lea rcx, [rbp + 0x1780]
0x001ECCE5: call 0x1403d3050
0x001ECCEA: mov dword ptr [rbp + 0x1780], 0x11808
0x001ECCF4: mov dword ptr [rbp + 0x1784], 1
0x001ECCFE: mov eax, 0x16
0x001ECD03: mov word ptr [rbp + 0x1788], ax
0x001ECD0A: mov dword ptr [rbp + 0x178c], 0x9a029c
0x001ECD14: mov qword ptr [rbp + 0x1790], 0x1fe00
0x001ECD1F: shl esi, 9
0x001ECD22: mov eax, esi
0x001ECD24: mov qword ptr [rbp + 0x1798], rax
0x001ECD2B: lea rdx, [rbp + 0x1780]
0x001ECD32: mov rcx, qword ptr [rbx + 0xd0]
0x001ECD39: call qword ptr [rip + 0x5fadc9]
0x001ECD3F: test eax, eax
0x001ECD41: je 0x1401ecd48
0x001ECD43: xor dil, dil
0x001ECD46: jmp 0x1401ecd4b
0x001ECD48: mov r12b, 1
0x001ECD4B: mov esi, dword ptr [r14 + 0x44]
0x001ECD4F: test esi, esi
```

#### ref `0x001ECDBC`

```asm
0x001ECD51: je 0x1401ecdce
0x001ECD53: cmp esi, dword ptr [r15 + 0x44]
0x001ECD57: je 0x1401ecdce
0x001ECD59: xor edx, edx
0x001ECD5B: mov r8d, 0x1808
0x001ECD61: lea rcx, [rbp + 0x2f90]
0x001ECD68: call 0x1403d3050
0x001ECD6D: mov dword ptr [rbp + 0x2f90], 0x11808
0x001ECD77: mov dword ptr [rbp + 0x2f94], 1
0x001ECD81: mov eax, 0x16
0x001ECD86: mov word ptr [rbp + 0x2f98], ax
0x001ECD8D: mov dword ptr [rbp + 0x2f9c], 0x9a02a0
0x001ECD97: mov qword ptr [rbp + 0x2fa0], 0x1f8000
0x001ECDA2: shl esi, 0xf
0x001ECDA5: mov eax, esi
0x001ECDA7: mov qword ptr [rbp + 0x2fa8], rax
0x001ECDAE: lea rdx, [rbp + 0x2f90]
0x001ECDB5: mov rcx, qword ptr [rbx + 0xd0]
0x001ECDBC: call qword ptr [rip + 0x5fad46]
0x001ECDC2: test eax, eax
0x001ECDC4: je 0x1401ecdcb
0x001ECDC6: xor dil, dil
0x001ECDC9: jmp 0x1401ecdce
0x001ECDCB: mov r12b, 1
0x001ECDCE: mov esi, dword ptr [r14 + 8]
0x001ECDD2: test esi, esi
```

#### ref `0x001ECE3F`

```asm
0x001ECDD4: je 0x1401ece4c
0x001ECDD6: cmp esi, dword ptr [r15 + 8]
0x001ECDDA: je 0x1401ece4c
0x001ECDDC: xor edx, edx
0x001ECDDE: mov r8d, 0x1808
0x001ECDE4: lea rcx, [rbp + 0x47a0]
0x001ECDEB: call 0x1403d3050
0x001ECDF0: mov dword ptr [rbp + 0x47a0], 0x11808
0x001ECDFA: mov dword ptr [rbp + 0x47a4], 1
0x001ECE04: mov eax, 0x16
0x001ECE09: mov word ptr [rbp + 0x47a8], ax
0x001ECE10: mov dword ptr [rbp + 0x47ac], 0x9a0290
0x001ECE1A: mov qword ptr [rbp + 0x47b0], 0x1ff00
0x001ECE25: shl esi, 8
0x001ECE28: mov eax, esi
0x001ECE2A: mov qword ptr [rbp + 0x47b8], rax
0x001ECE31: lea rdx, [rbp + 0x47a0]
0x001ECE38: mov rcx, qword ptr [rbx + 0xd0]
0x001ECE3F: call qword ptr [rip + 0x5facc3]
0x001ECE45: test eax, eax
0x001ECE47: je 0x1401ece55
0x001ECE49: xor dil, dil
0x001ECE4C: test r12b, r12b
0x001ECE4F: je 0x1401ed07d
0x001ECE55: movsxd rax, dword ptr [rsp + 0x24]
0x001ECE5A: mov byte ptr [rax + rbx + 0x280], 1
```

#### ref `0x001FE6D5`

```asm
0x001FE669: mov qword ptr [rip + 0x5e9468], rax
0x001FE670: call qword ptr [rip + 0x5e9382]
0x001FE676: mov ecx, 0xa58971a5
0x001FE67B: mov qword ptr [rip + 0x5e945e], rax
0x001FE682: call qword ptr [rip + 0x5e9370]
0x001FE688: mov ecx, 0x57f7caac
0x001FE68D: mov qword ptr [rip + 0x5e9454], rax
0x001FE694: call qword ptr [rip + 0x5e935e]
0x001FE69A: mov ecx, 0x42aea16a
0x001FE69F: mov qword ptr [rip + 0x5e944a], rax
0x001FE6A6: call qword ptr [rip + 0x5e934c]
0x001FE6AC: mov ecx, 0x2ddfb66e
0x001FE6B1: mov qword ptr [rip + 0x5e9440], rax
0x001FE6B8: call qword ptr [rip + 0x5e933a]
0x001FE6BE: mov ecx, 0x2eb3c140
0x001FE6C3: mov qword ptr [rip + 0x5e9436], rax
0x001FE6CA: call qword ptr [rip + 0x5e9328]
0x001FE6D0: mov ecx, 0x65fe3aad
0x001FE6D5: mov qword ptr [rip + 0x5e942c], rax
0x001FE6DC: call qword ptr [rip + 0x5e9316]
0x001FE6E2: mov qword ptr [rip + 0x5e9427], rax
0x001FE6E9: mov al, 1
0x001FE6EB: mov rcx, qword ptr [rbp + 0x4f]
0x001FE6EF: xor rcx, rsp
0x001FE6F2: call 0x1403b24c0
0x001FE6F7: add rsp, 0xa0
```

## call `0x001ECD68` function slot `unknown`

```asm
0x001ECD1F: shl esi, 9
0x001ECD22: mov eax, esi
0x001ECD24: mov qword ptr [rbp + 0x1798], rax
0x001ECD2B: lea rdx, [rbp + 0x1780]
0x001ECD32: mov rcx, qword ptr [rbx + 0xd0]
0x001ECD39: call qword ptr [rip + 0x5fadc9]
0x001ECD3F: test eax, eax
0x001ECD41: je 0x1401ecd48
0x001ECD43: xor dil, dil
0x001ECD46: jmp 0x1401ecd4b
0x001ECD48: mov r12b, 1
0x001ECD4B: mov esi, dword ptr [r14 + 0x44]
0x001ECD4F: test esi, esi
0x001ECD51: je 0x1401ecdce
0x001ECD53: cmp esi, dword ptr [r15 + 0x44]
0x001ECD57: je 0x1401ecdce
0x001ECD59: xor edx, edx
0x001ECD5B: mov r8d, 0x1808
0x001ECD61: lea rcx, [rbp + 0x2f90]
0x001ECD68: call 0x1403d3050
0x001ECD6D: mov dword ptr [rbp + 0x2f90], 0x11808
0x001ECD77: mov dword ptr [rbp + 0x2f94], 1
0x001ECD81: mov eax, 0x16
```

## call `0x001ECDBC` function slot `0x007E7B08`

```asm
0x001ECDA2: shl esi, 0xf
0x001ECDA5: mov eax, esi
0x001ECDA7: mov qword ptr [rbp + 0x2fa8], rax
0x001ECDAE: lea rdx, [rbp + 0x2f90]
0x001ECDB5: mov rcx, qword ptr [rbx + 0xd0]
0x001ECDBC: call qword ptr [rip + 0x5fad46]
0x001ECDC2: test eax, eax
0x001ECDC4: je 0x1401ecdcb
0x001ECDC6: xor dil, dil
```

### refs to global slot `0x007E7B08`: `7`

#### ref `0x001E0CCE`

```asm
0x001E0C96: add rsp, 0x20
0x001E0C9A: pop rdi
0x001E0C9B: ret
0x001E0C9C: int3
0x001E0C9D: int3
0x001E0C9E: int3
0x001E0C9F: int3
0x001E0CA0: mov qword ptr [rsp + 0x18], rbx
0x001E0CA5: push rbp
0x001E0CA6: push rsi
0x001E0CA7: push rdi
0x001E0CA8: lea rbp, [rsp - 0x1740]
0x001E0CB0: mov eax, 0x1840
0x001E0CB5: call 0x1403b2500
0x001E0CBA: sub rsp, rax
0x001E0CBD: mov rax, qword ptr [rip + 0x5f5c2c]
0x001E0CC4: xor rax, rsp
0x001E0CC7: mov qword ptr [rbp + 0x1730], rax
0x001E0CCE: mov rdi, qword ptr [rip + 0x606e33]
0x001E0CD5: mov rbx, rdx
0x001E0CD8: mov rsi, rcx
0x001E0CDB: test rdi, rdi
0x001E0CDE: jne 0x1401e0ce7
0x001E0CE0: xor al, al
0x001E0CE2: jmp 0x1401e0e9e
0x001E0CE7: xor edx, edx
```

#### ref `0x001ECC46`

```asm
0x001ECC07: jne 0x1401ecc43
0x001ECC09: cmp dword ptr [rbx + 0x25c], 0
0x001ECC10: jne 0x1401ecc43
0x001ECC12: xor eax, eax
0x001ECC14: mov byte ptr [rsp + 0x20], al
0x001ECC18: lea rcx, [rbx + 0x26c]
0x001ECC1F: lea rax, [rbx + 0x260]
0x001ECC26: cmp rax, rcx
0x001ECC29: je 0x1401ecc3e
0x001ECC2B: nop dword ptr [rax + rax]
0x001ECC30: cmp dword ptr [rax], 0
0x001ECC33: jne 0x1401ecc43
0x001ECC35: add rax, 4
0x001ECC39: cmp rax, rcx
0x001ECC3C: jne 0x1401ecc30
0x001ECC3E: mov r13b, 1
0x001ECC41: jmp 0x1401ecc46
0x001ECC43: xor r13b, r13b
0x001ECC46: cmp qword ptr [rip + 0x5faeba], 0
0x001ECC4E: jne 0x1401ecc57
0x001ECC50: xor al, al
0x001ECC52: jmp 0x1401ed081
0x001ECC57: mov esi, dword ptr [r14 + 0x2c]
0x001ECC5B: test esi, esi
0x001ECC5D: je 0x1401eccc8
0x001ECC5F: cmp esi, dword ptr [r15 + 0x2c]
```

#### ref `0x001ECCB6`

```asm
0x001ECC5D: je 0x1401eccc8
0x001ECC5F: cmp esi, dword ptr [r15 + 0x2c]
0x001ECC63: je 0x1401eccc8
0x001ECC65: xor edx, edx
0x001ECC67: mov r8d, 0x1808
0x001ECC6D: lea rcx, [rsp + 0x70]
0x001ECC72: call 0x1403d3050
0x001ECC77: mov dword ptr [rsp + 0x70], 0x11808
0x001ECC7F: mov dword ptr [rsp + 0x74], 1
0x001ECC87: mov eax, 0x16
0x001ECC8C: mov word ptr [rsp + 0x78], ax
0x001ECC91: mov dword ptr [rsp + 0x7c], 0x9a0298
0x001ECC99: mov qword ptr [rbp - 0x80], 0x7f0000
0x001ECCA1: shl esi, 0x10
0x001ECCA4: mov eax, esi
0x001ECCA6: mov qword ptr [rbp - 0x78], rax
0x001ECCAA: lea rdx, [rsp + 0x70]
0x001ECCAF: mov rcx, qword ptr [rbx + 0xd0]
0x001ECCB6: call qword ptr [rip + 0x5fae4c]
0x001ECCBC: test eax, eax
0x001ECCBE: je 0x1401eccc5
0x001ECCC0: xor dil, dil
0x001ECCC3: jmp 0x1401eccc8
0x001ECCC5: mov r12b, 1
0x001ECCC8: mov esi, dword ptr [r14 + 0x38]
0x001ECCCC: test esi, esi
```

#### ref `0x001ECD39`

```asm
0x001ECCCE: je 0x1401ecd4b
0x001ECCD0: cmp esi, dword ptr [r15 + 0x38]
0x001ECCD4: je 0x1401ecd4b
0x001ECCD6: xor edx, edx
0x001ECCD8: mov r8d, 0x1808
0x001ECCDE: lea rcx, [rbp + 0x1780]
0x001ECCE5: call 0x1403d3050
0x001ECCEA: mov dword ptr [rbp + 0x1780], 0x11808
0x001ECCF4: mov dword ptr [rbp + 0x1784], 1
0x001ECCFE: mov eax, 0x16
0x001ECD03: mov word ptr [rbp + 0x1788], ax
0x001ECD0A: mov dword ptr [rbp + 0x178c], 0x9a029c
0x001ECD14: mov qword ptr [rbp + 0x1790], 0x1fe00
0x001ECD1F: shl esi, 9
0x001ECD22: mov eax, esi
0x001ECD24: mov qword ptr [rbp + 0x1798], rax
0x001ECD2B: lea rdx, [rbp + 0x1780]
0x001ECD32: mov rcx, qword ptr [rbx + 0xd0]
0x001ECD39: call qword ptr [rip + 0x5fadc9]
0x001ECD3F: test eax, eax
0x001ECD41: je 0x1401ecd48
0x001ECD43: xor dil, dil
0x001ECD46: jmp 0x1401ecd4b
0x001ECD48: mov r12b, 1
0x001ECD4B: mov esi, dword ptr [r14 + 0x44]
0x001ECD4F: test esi, esi
```

#### ref `0x001ECDBC`

```asm
0x001ECD51: je 0x1401ecdce
0x001ECD53: cmp esi, dword ptr [r15 + 0x44]
0x001ECD57: je 0x1401ecdce
0x001ECD59: xor edx, edx
0x001ECD5B: mov r8d, 0x1808
0x001ECD61: lea rcx, [rbp + 0x2f90]
0x001ECD68: call 0x1403d3050
0x001ECD6D: mov dword ptr [rbp + 0x2f90], 0x11808
0x001ECD77: mov dword ptr [rbp + 0x2f94], 1
0x001ECD81: mov eax, 0x16
0x001ECD86: mov word ptr [rbp + 0x2f98], ax
0x001ECD8D: mov dword ptr [rbp + 0x2f9c], 0x9a02a0
0x001ECD97: mov qword ptr [rbp + 0x2fa0], 0x1f8000
0x001ECDA2: shl esi, 0xf
0x001ECDA5: mov eax, esi
0x001ECDA7: mov qword ptr [rbp + 0x2fa8], rax
0x001ECDAE: lea rdx, [rbp + 0x2f90]
0x001ECDB5: mov rcx, qword ptr [rbx + 0xd0]
0x001ECDBC: call qword ptr [rip + 0x5fad46]
0x001ECDC2: test eax, eax
0x001ECDC4: je 0x1401ecdcb
0x001ECDC6: xor dil, dil
0x001ECDC9: jmp 0x1401ecdce
0x001ECDCB: mov r12b, 1
0x001ECDCE: mov esi, dword ptr [r14 + 8]
0x001ECDD2: test esi, esi
```

#### ref `0x001ECE3F`

```asm
0x001ECDD4: je 0x1401ece4c
0x001ECDD6: cmp esi, dword ptr [r15 + 8]
0x001ECDDA: je 0x1401ece4c
0x001ECDDC: xor edx, edx
0x001ECDDE: mov r8d, 0x1808
0x001ECDE4: lea rcx, [rbp + 0x47a0]
0x001ECDEB: call 0x1403d3050
0x001ECDF0: mov dword ptr [rbp + 0x47a0], 0x11808
0x001ECDFA: mov dword ptr [rbp + 0x47a4], 1
0x001ECE04: mov eax, 0x16
0x001ECE09: mov word ptr [rbp + 0x47a8], ax
0x001ECE10: mov dword ptr [rbp + 0x47ac], 0x9a0290
0x001ECE1A: mov qword ptr [rbp + 0x47b0], 0x1ff00
0x001ECE25: shl esi, 8
0x001ECE28: mov eax, esi
0x001ECE2A: mov qword ptr [rbp + 0x47b8], rax
0x001ECE31: lea rdx, [rbp + 0x47a0]
0x001ECE38: mov rcx, qword ptr [rbx + 0xd0]
0x001ECE3F: call qword ptr [rip + 0x5facc3]
0x001ECE45: test eax, eax
0x001ECE47: je 0x1401ece55
0x001ECE49: xor dil, dil
0x001ECE4C: test r12b, r12b
0x001ECE4F: je 0x1401ed07d
0x001ECE55: movsxd rax, dword ptr [rsp + 0x24]
0x001ECE5A: mov byte ptr [rax + rbx + 0x280], 1
```

#### ref `0x001FE6D5`

```asm
0x001FE669: mov qword ptr [rip + 0x5e9468], rax
0x001FE670: call qword ptr [rip + 0x5e9382]
0x001FE676: mov ecx, 0xa58971a5
0x001FE67B: mov qword ptr [rip + 0x5e945e], rax
0x001FE682: call qword ptr [rip + 0x5e9370]
0x001FE688: mov ecx, 0x57f7caac
0x001FE68D: mov qword ptr [rip + 0x5e9454], rax
0x001FE694: call qword ptr [rip + 0x5e935e]
0x001FE69A: mov ecx, 0x42aea16a
0x001FE69F: mov qword ptr [rip + 0x5e944a], rax
0x001FE6A6: call qword ptr [rip + 0x5e934c]
0x001FE6AC: mov ecx, 0x2ddfb66e
0x001FE6B1: mov qword ptr [rip + 0x5e9440], rax
0x001FE6B8: call qword ptr [rip + 0x5e933a]
0x001FE6BE: mov ecx, 0x2eb3c140
0x001FE6C3: mov qword ptr [rip + 0x5e9436], rax
0x001FE6CA: call qword ptr [rip + 0x5e9328]
0x001FE6D0: mov ecx, 0x65fe3aad
0x001FE6D5: mov qword ptr [rip + 0x5e942c], rax
0x001FE6DC: call qword ptr [rip + 0x5e9316]
0x001FE6E2: mov qword ptr [rip + 0x5e9427], rax
0x001FE6E9: mov al, 1
0x001FE6EB: mov rcx, qword ptr [rbp + 0x4f]
0x001FE6EF: xor rcx, rsp
0x001FE6F2: call 0x1403b24c0
0x001FE6F7: add rsp, 0xa0
```

## call `0x001ECDEB` function slot `unknown`

```asm
0x001ECDA2: shl esi, 0xf
0x001ECDA5: mov eax, esi
0x001ECDA7: mov qword ptr [rbp + 0x2fa8], rax
0x001ECDAE: lea rdx, [rbp + 0x2f90]
0x001ECDB5: mov rcx, qword ptr [rbx + 0xd0]
0x001ECDBC: call qword ptr [rip + 0x5fad46]
0x001ECDC2: test eax, eax
0x001ECDC4: je 0x1401ecdcb
0x001ECDC6: xor dil, dil
0x001ECDC9: jmp 0x1401ecdce
0x001ECDCB: mov r12b, 1
0x001ECDCE: mov esi, dword ptr [r14 + 8]
0x001ECDD2: test esi, esi
0x001ECDD4: je 0x1401ece4c
0x001ECDD6: cmp esi, dword ptr [r15 + 8]
0x001ECDDA: je 0x1401ece4c
0x001ECDDC: xor edx, edx
0x001ECDDE: mov r8d, 0x1808
0x001ECDE4: lea rcx, [rbp + 0x47a0]
0x001ECDEB: call 0x1403d3050
0x001ECDF0: mov dword ptr [rbp + 0x47a0], 0x11808
0x001ECDFA: mov dword ptr [rbp + 0x47a4], 1
0x001ECE04: mov eax, 0x16
```

## call `0x001ECE3F` function slot `0x007E7B08`

```asm
0x001ECE25: shl esi, 8
0x001ECE28: mov eax, esi
0x001ECE2A: mov qword ptr [rbp + 0x47b8], rax
0x001ECE31: lea rdx, [rbp + 0x47a0]
0x001ECE38: mov rcx, qword ptr [rbx + 0xd0]
0x001ECE3F: call qword ptr [rip + 0x5facc3]
0x001ECE45: test eax, eax
0x001ECE47: je 0x1401ece55
0x001ECE49: xor dil, dil
```

### refs to global slot `0x007E7B08`: `7`

#### ref `0x001E0CCE`

```asm
0x001E0C96: add rsp, 0x20
0x001E0C9A: pop rdi
0x001E0C9B: ret
0x001E0C9C: int3
0x001E0C9D: int3
0x001E0C9E: int3
0x001E0C9F: int3
0x001E0CA0: mov qword ptr [rsp + 0x18], rbx
0x001E0CA5: push rbp
0x001E0CA6: push rsi
0x001E0CA7: push rdi
0x001E0CA8: lea rbp, [rsp - 0x1740]
0x001E0CB0: mov eax, 0x1840
0x001E0CB5: call 0x1403b2500
0x001E0CBA: sub rsp, rax
0x001E0CBD: mov rax, qword ptr [rip + 0x5f5c2c]
0x001E0CC4: xor rax, rsp
0x001E0CC7: mov qword ptr [rbp + 0x1730], rax
0x001E0CCE: mov rdi, qword ptr [rip + 0x606e33]
0x001E0CD5: mov rbx, rdx
0x001E0CD8: mov rsi, rcx
0x001E0CDB: test rdi, rdi
0x001E0CDE: jne 0x1401e0ce7
0x001E0CE0: xor al, al
0x001E0CE2: jmp 0x1401e0e9e
0x001E0CE7: xor edx, edx
```

#### ref `0x001ECC46`

```asm
0x001ECC07: jne 0x1401ecc43
0x001ECC09: cmp dword ptr [rbx + 0x25c], 0
0x001ECC10: jne 0x1401ecc43
0x001ECC12: xor eax, eax
0x001ECC14: mov byte ptr [rsp + 0x20], al
0x001ECC18: lea rcx, [rbx + 0x26c]
0x001ECC1F: lea rax, [rbx + 0x260]
0x001ECC26: cmp rax, rcx
0x001ECC29: je 0x1401ecc3e
0x001ECC2B: nop dword ptr [rax + rax]
0x001ECC30: cmp dword ptr [rax], 0
0x001ECC33: jne 0x1401ecc43
0x001ECC35: add rax, 4
0x001ECC39: cmp rax, rcx
0x001ECC3C: jne 0x1401ecc30
0x001ECC3E: mov r13b, 1
0x001ECC41: jmp 0x1401ecc46
0x001ECC43: xor r13b, r13b
0x001ECC46: cmp qword ptr [rip + 0x5faeba], 0
0x001ECC4E: jne 0x1401ecc57
0x001ECC50: xor al, al
0x001ECC52: jmp 0x1401ed081
0x001ECC57: mov esi, dword ptr [r14 + 0x2c]
0x001ECC5B: test esi, esi
0x001ECC5D: je 0x1401eccc8
0x001ECC5F: cmp esi, dword ptr [r15 + 0x2c]
```

#### ref `0x001ECCB6`

```asm
0x001ECC5D: je 0x1401eccc8
0x001ECC5F: cmp esi, dword ptr [r15 + 0x2c]
0x001ECC63: je 0x1401eccc8
0x001ECC65: xor edx, edx
0x001ECC67: mov r8d, 0x1808
0x001ECC6D: lea rcx, [rsp + 0x70]
0x001ECC72: call 0x1403d3050
0x001ECC77: mov dword ptr [rsp + 0x70], 0x11808
0x001ECC7F: mov dword ptr [rsp + 0x74], 1
0x001ECC87: mov eax, 0x16
0x001ECC8C: mov word ptr [rsp + 0x78], ax
0x001ECC91: mov dword ptr [rsp + 0x7c], 0x9a0298
0x001ECC99: mov qword ptr [rbp - 0x80], 0x7f0000
0x001ECCA1: shl esi, 0x10
0x001ECCA4: mov eax, esi
0x001ECCA6: mov qword ptr [rbp - 0x78], rax
0x001ECCAA: lea rdx, [rsp + 0x70]
0x001ECCAF: mov rcx, qword ptr [rbx + 0xd0]
0x001ECCB6: call qword ptr [rip + 0x5fae4c]
0x001ECCBC: test eax, eax
0x001ECCBE: je 0x1401eccc5
0x001ECCC0: xor dil, dil
0x001ECCC3: jmp 0x1401eccc8
0x001ECCC5: mov r12b, 1
0x001ECCC8: mov esi, dword ptr [r14 + 0x38]
0x001ECCCC: test esi, esi
```

#### ref `0x001ECD39`

```asm
0x001ECCCE: je 0x1401ecd4b
0x001ECCD0: cmp esi, dword ptr [r15 + 0x38]
0x001ECCD4: je 0x1401ecd4b
0x001ECCD6: xor edx, edx
0x001ECCD8: mov r8d, 0x1808
0x001ECCDE: lea rcx, [rbp + 0x1780]
0x001ECCE5: call 0x1403d3050
0x001ECCEA: mov dword ptr [rbp + 0x1780], 0x11808
0x001ECCF4: mov dword ptr [rbp + 0x1784], 1
0x001ECCFE: mov eax, 0x16
0x001ECD03: mov word ptr [rbp + 0x1788], ax
0x001ECD0A: mov dword ptr [rbp + 0x178c], 0x9a029c
0x001ECD14: mov qword ptr [rbp + 0x1790], 0x1fe00
0x001ECD1F: shl esi, 9
0x001ECD22: mov eax, esi
0x001ECD24: mov qword ptr [rbp + 0x1798], rax
0x001ECD2B: lea rdx, [rbp + 0x1780]
0x001ECD32: mov rcx, qword ptr [rbx + 0xd0]
0x001ECD39: call qword ptr [rip + 0x5fadc9]
0x001ECD3F: test eax, eax
0x001ECD41: je 0x1401ecd48
0x001ECD43: xor dil, dil
0x001ECD46: jmp 0x1401ecd4b
0x001ECD48: mov r12b, 1
0x001ECD4B: mov esi, dword ptr [r14 + 0x44]
0x001ECD4F: test esi, esi
```

#### ref `0x001ECDBC`

```asm
0x001ECD51: je 0x1401ecdce
0x001ECD53: cmp esi, dword ptr [r15 + 0x44]
0x001ECD57: je 0x1401ecdce
0x001ECD59: xor edx, edx
0x001ECD5B: mov r8d, 0x1808
0x001ECD61: lea rcx, [rbp + 0x2f90]
0x001ECD68: call 0x1403d3050
0x001ECD6D: mov dword ptr [rbp + 0x2f90], 0x11808
0x001ECD77: mov dword ptr [rbp + 0x2f94], 1
0x001ECD81: mov eax, 0x16
0x001ECD86: mov word ptr [rbp + 0x2f98], ax
0x001ECD8D: mov dword ptr [rbp + 0x2f9c], 0x9a02a0
0x001ECD97: mov qword ptr [rbp + 0x2fa0], 0x1f8000
0x001ECDA2: shl esi, 0xf
0x001ECDA5: mov eax, esi
0x001ECDA7: mov qword ptr [rbp + 0x2fa8], rax
0x001ECDAE: lea rdx, [rbp + 0x2f90]
0x001ECDB5: mov rcx, qword ptr [rbx + 0xd0]
0x001ECDBC: call qword ptr [rip + 0x5fad46]
0x001ECDC2: test eax, eax
0x001ECDC4: je 0x1401ecdcb
0x001ECDC6: xor dil, dil
0x001ECDC9: jmp 0x1401ecdce
0x001ECDCB: mov r12b, 1
0x001ECDCE: mov esi, dword ptr [r14 + 8]
0x001ECDD2: test esi, esi
```

#### ref `0x001ECE3F`

```asm
0x001ECDD4: je 0x1401ece4c
0x001ECDD6: cmp esi, dword ptr [r15 + 8]
0x001ECDDA: je 0x1401ece4c
0x001ECDDC: xor edx, edx
0x001ECDDE: mov r8d, 0x1808
0x001ECDE4: lea rcx, [rbp + 0x47a0]
0x001ECDEB: call 0x1403d3050
0x001ECDF0: mov dword ptr [rbp + 0x47a0], 0x11808
0x001ECDFA: mov dword ptr [rbp + 0x47a4], 1
0x001ECE04: mov eax, 0x16
0x001ECE09: mov word ptr [rbp + 0x47a8], ax
0x001ECE10: mov dword ptr [rbp + 0x47ac], 0x9a0290
0x001ECE1A: mov qword ptr [rbp + 0x47b0], 0x1ff00
0x001ECE25: shl esi, 8
0x001ECE28: mov eax, esi
0x001ECE2A: mov qword ptr [rbp + 0x47b8], rax
0x001ECE31: lea rdx, [rbp + 0x47a0]
0x001ECE38: mov rcx, qword ptr [rbx + 0xd0]
0x001ECE3F: call qword ptr [rip + 0x5facc3]
0x001ECE45: test eax, eax
0x001ECE47: je 0x1401ece55
0x001ECE49: xor dil, dil
0x001ECE4C: test r12b, r12b
0x001ECE4F: je 0x1401ed07d
0x001ECE55: movsxd rax, dword ptr [rsp + 0x24]
0x001ECE5A: mov byte ptr [rax + rbx + 0x280], 1
```

#### ref `0x001FE6D5`

```asm
0x001FE669: mov qword ptr [rip + 0x5e9468], rax
0x001FE670: call qword ptr [rip + 0x5e9382]
0x001FE676: mov ecx, 0xa58971a5
0x001FE67B: mov qword ptr [rip + 0x5e945e], rax
0x001FE682: call qword ptr [rip + 0x5e9370]
0x001FE688: mov ecx, 0x57f7caac
0x001FE68D: mov qword ptr [rip + 0x5e9454], rax
0x001FE694: call qword ptr [rip + 0x5e935e]
0x001FE69A: mov ecx, 0x42aea16a
0x001FE69F: mov qword ptr [rip + 0x5e944a], rax
0x001FE6A6: call qword ptr [rip + 0x5e934c]
0x001FE6AC: mov ecx, 0x2ddfb66e
0x001FE6B1: mov qword ptr [rip + 0x5e9440], rax
0x001FE6B8: call qword ptr [rip + 0x5e933a]
0x001FE6BE: mov ecx, 0x2eb3c140
0x001FE6C3: mov qword ptr [rip + 0x5e9436], rax
0x001FE6CA: call qword ptr [rip + 0x5e9328]
0x001FE6D0: mov ecx, 0x65fe3aad
0x001FE6D5: mov qword ptr [rip + 0x5e942c], rax
0x001FE6DC: call qword ptr [rip + 0x5e9316]
0x001FE6E2: mov qword ptr [rip + 0x5e9427], rax
0x001FE6E9: mov al, 1
0x001FE6EB: mov rcx, qword ptr [rbp + 0x4f]
0x001FE6EF: xor rcx, rsp
0x001FE6F2: call 0x1403b24c0
0x001FE6F7: add rsp, 0xa0
```

## call `0x001ED12F` function slot `0x007E7AB8`

```asm
0x001ED115: mov r8d, 0xb4
0x001ED11B: lea rcx, [rbp - 0x7c]
0x001ED11F: call 0x1403d3050
0x001ED124: lea rdx, [rbp - 0x80]
0x001ED128: mov rcx, qword ptr [rbx + 0xd0]
0x001ED12F: call rdi
0x001ED131: mov dword ptr [rsp + 0x20], eax
0x001ED135: test eax, eax
0x001ED137: je 0x1401ed39f
```

### refs to global slot `0x007E7AB8`: `4`

#### ref `0x001E3045`

```asm
0x001E2FE0: mov rax, rsp
0x001E2FE3: push rbp
0x001E2FE4: lea rbp, [rax - 0x168]
0x001E2FEB: sub rsp, 0x260
0x001E2FF2: mov qword ptr [rsp + 0x40], 0xfffffffffffffffe
0x001E2FFB: mov qword ptr [rax + 0x10], rbx
0x001E2FFF: mov qword ptr [rax + 0x18], rsi
0x001E3003: mov qword ptr [rax + 0x20], rdi
0x001E3007: mov rax, qword ptr [rip + 0x5f38e2]
0x001E300E: xor rax, rsp
0x001E3011: mov qword ptr [rbp + 0x150], rax
0x001E3018: mov rbx, rcx
0x001E301B: cmp qword ptr [rcx + 0xd0], 0
0x001E3023: je 0x1401e3e0c
0x001E3029: cmp qword ptr [rip + 0x604a8f], 0
0x001E3031: je 0x1401e3e04
0x001E3037: cmp qword ptr [rip + 0x604a89], 0
0x001E303F: je 0x1401e3e04
0x001E3045: cmp qword ptr [rip + 0x604a6b], 0
0x001E304D: je 0x1401e3e04
0x001E3053: xor esi, esi
0x001E3055: mov edi, esi
0x001E3057: mov dword ptr [rsp + 0x20], esi
0x001E305B: call 0x1401ed0b0
0x001E3060: mov dword ptr [rbp + 0xa0], 0x10048
0x001E306A: xor eax, eax
```

#### ref `0x001E8A7E`

```asm
0x001E8A1F: sub rsp, 0x250
0x001E8A26: mov qword ptr [rsp + 0x40], 0xfffffffffffffffe
0x001E8A2F: mov rax, qword ptr [rip + 0x5edeba]
0x001E8A36: xor rax, rsp
0x001E8A39: mov qword ptr [rbp + 0x140], rax
0x001E8A40: mov esi, r8d
0x001E8A43: mov rdi, rcx
0x001E8A46: cmp qword ptr [rcx + 0xd0], 0
0x001E8A4E: jne 0x1401e8a62
0x001E8A50: xor eax, eax
0x001E8A52: mov ecx, 2
0x001E8A57: test r8d, r8d
0x001E8A5A: cmovg eax, ecx
0x001E8A5D: jmp 0x1401e9913
0x001E8A62: cmp qword ptr [rip + 0x5ff056], 0
0x001E8A6A: je 0x1401e98f8
0x001E8A70: cmp qword ptr [rip + 0x5ff050], 0
0x001E8A78: je 0x1401e98f8
0x001E8A7E: cmp qword ptr [rip + 0x5ff032], 0
0x001E8A86: je 0x1401e98f8
0x001E8A8C: xor eax, eax
0x001E8A8E: mov dword ptr [rsp + 0x24], eax
0x001E8A92: lea eax, [rdx + 0x64]
0x001E8A95: imul ebx, eax, 0x3e8
0x001E8A9B: mov dword ptr [rsp + 0x20], ebx
0x001E8A9F: call 0x1401ed0b0
```

#### ref `0x001ED0FC`

```asm
0x001ED0AD: int3
0x001ED0AE: int3
0x001ED0AF: int3
0x001ED0B0: mov rax, rsp
0x001ED0B3: push rbp
0x001ED0B4: lea rbp, [rax - 0x58]
0x001ED0B8: sub rsp, 0x150
0x001ED0BF: mov qword ptr [rsp + 0x28], 0xfffffffffffffffe
0x001ED0C8: mov qword ptr [rax + 0x10], rbx
0x001ED0CC: mov qword ptr [rax + 0x18], rdi
0x001ED0D0: mov rax, qword ptr [rip + 0x5e9819]
0x001ED0D7: xor rax, rsp
0x001ED0DA: mov qword ptr [rbp + 0x40], rax
0x001ED0DE: mov rbx, rcx
0x001ED0E1: cmp qword ptr [rcx + 0xd0], 0
0x001ED0E9: je 0x1401ed3e0
0x001ED0EF: cmp dword ptr [rcx + 0x138], 0
0x001ED0F6: jge 0x1401ed3e0
0x001ED0FC: mov rdi, qword ptr [rip + 0x5fa9b5]
0x001ED103: test rdi, rdi
0x001ED106: je 0x1401ed3e0
0x001ED10C: mov dword ptr [rbp - 0x80], 0x100b8
0x001ED113: xor edx, edx
0x001ED115: mov r8d, 0xb4
0x001ED11B: lea rcx, [rbp - 0x7c]
0x001ED11F: call 0x1403d3050
```

#### ref `0x001FE621`

```asm
0x001FE5B5: mov qword ptr [rip + 0x5e94cc], rax
0x001FE5BC: call qword ptr [rip + 0x5e9436]
0x001FE5C2: mov ecx, 0x6ff81213
0x001FE5C7: mov qword ptr [rip + 0x5e94c2], rax
0x001FE5CE: call qword ptr [rip + 0x5e9424]
0x001FE5D4: mov ecx, 0xf4dae6b
0x001FE5D9: mov qword ptr [rip + 0x5e94b8], rax
0x001FE5E0: call qword ptr [rip + 0x5e9412]
0x001FE5E6: mov ecx, 0x843c0256
0x001FE5EB: mov qword ptr [rip + 0x5e94ae], rax
0x001FE5F2: call qword ptr [rip + 0x5e9400]
0x001FE5F8: mov ecx, 0xedcf624e
0x001FE5FD: mov qword ptr [rip + 0x5e94a4], rax
0x001FE604: call qword ptr [rip + 0x5e93ee]
0x001FE60A: mov ecx, 0x34206d86
0x001FE60F: mov qword ptr [rip + 0x5e949a], rax
0x001FE616: call qword ptr [rip + 0x5e93dc]
0x001FE61C: mov ecx, 0x70916171
0x001FE621: mov qword ptr [rip + 0x5e9490], rax
0x001FE628: call qword ptr [rip + 0x5e93ca]
0x001FE62E: mov ecx, 0xad95f5ed
0x001FE633: mov qword ptr [rip + 0x5e9486], rax
0x001FE63A: call qword ptr [rip + 0x5e93b8]
0x001FE640: mov ecx, 0xfb85b01e
0x001FE645: mov qword ptr [rip + 0x5e947c], rax
0x001FE64C: call qword ptr [rip + 0x5e93a6]
```