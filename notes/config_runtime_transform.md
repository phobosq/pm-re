# Config -> runtime transform decode

## target `0x0013C190` PDATA `0x0013C190..0x0013C4D8`

### Calls / interesting accesses

| RVA | kind | instruction |
|---|---|---|
| `0x0013C1C6` | call | `direct 0x00391AC4` |
| `0x0013C1D1` | call | `direct 0x0039219C` |
| `0x0013C1E4` | call | `direct 0x00391B24` |
| `0x0013C1EF` | call | `direct 0x0039219C` |
| `0x0013C20B` | call | `indirect qword ptr [rax + 0x20]` |
| `0x0013C21F` | call | `direct 0x00139D60` |
| `0x0013C232` | call | `direct 0x00391550` |
| `0x0013C23A` | call | `direct 0x00391534` |
| `0x0013C2A8` | call | `direct 0x0013A0D0` |
| `0x0013C2C3` | call | `direct 0x0008B600` |
| `0x0013C2D5` | context | `mov dword ptr [rsp + 0x90], esi` |
| `0x0013C315` | call | `direct 0x00139F00` |
| `0x0013C34E` | call | `direct 0x0013A180` |
| `0x0013C383` | call | `direct 0x0013A180` |
| `0x0013C3AC` | call | `direct 0x00058410` |
| `0x0013C3BE` | mt | `mov edx, dword ptr [rax + 0x98]` |
| `0x0013C3CB` | call | `direct 0x0014ABF0` |
| `0x0013C3D4` | context | `lea rcx, [rsp + 0x90]` |
| `0x0013C3E4` | context | `lea rdx, [rsp + 0x90]` |
| `0x0013C3F1` | context | `lea rbx, [rsp + 0x90]` |
| `0x0013C40E` | call | `direct 0x0008B8B0` |
| `0x0013C434` | call | `direct 0x0008B8B0` |
| `0x0013C466` | call | `indirect qword ptr [rax]` |
| `0x0013C47B` | call | `indirect qword ptr [rax + 8]` |
| `0x0013C494` | call | `direct 0x00391B24` |
| `0x0013C49F` | call | `direct 0x0039219C` |
| `0x0013C4B7` | call | `indirect qword ptr [rax + 0x20]` |
| `0x0013C4C0` | mt | `mov rbx, qword ptr [rsp + 0x98]` |

### Full disassembly
```asm
0x0013C190: mov rax, rsp
0x0013C193: mov qword ptr [rax + 0x18], r8
0x0013C197: push rbp
0x0013C198: push rsi
0x0013C199: push rdi
0x0013C19A: push r12
0x0013C19C: push r13
0x0013C19E: push r14
0x0013C1A0: push r15
0x0013C1A2: sub rsp, 0x50
0x0013C1A6: mov qword ptr [rax - 0x58], 0xfffffffffffffffe
0x0013C1AE: mov qword ptr [rax + 0x10], rbx
0x0013C1B2: mov r15, r8
0x0013C1B5: mov rsi, rdx
0x0013C1B8: mov r13, rcx
0x0013C1BB: lea rbx, [rcx + 0x10]
0x0013C1BF: mov qword ptr [rax + 0x20], rbx
0x0013C1C3: mov rcx, rbx
0x0013C1C6: call 0x140391ac4
0x0013C1CB: test eax, eax
0x0013C1CD: je 0x14013c1d7
0x0013C1CF: mov ecx, eax
0x0013C1D1: call 0x14039219c
0x0013C1D6: nop
0x0013C1D7: mov rax, qword ptr [r13 + 0x68]
0x0013C1DB: cmp qword ptr [r13 + 0x60], rax
0x0013C1DF: je 0x14013c215
0x0013C1E1: mov rcx, rbx
0x0013C1E4: call 0x140391b24
0x0013C1E9: test eax, eax
0x0013C1EB: je 0x14013c1f5
0x0013C1ED: mov ecx, eax
0x0013C1EF: call 0x14039219c
0x0013C1F4: nop
0x0013C1F5: mov rcx, qword ptr [r15 + 0x38]
0x0013C1F9: test rcx, rcx
0x0013C1FC: je 0x14013c4be
0x0013C202: mov rax, qword ptr [rcx]
0x0013C205: cmp rcx, r15
0x0013C208: setne dl
0x0013C20B: call qword ptr [rax + 0x20]
0x0013C20E: xor esi, esi
0x0013C210: jmp 0x14013c4ba
0x0013C215: lea rcx, [r13 + 0x458]
0x0013C21C: mov rdx, rsi
0x0013C21F: call 0x140139d60
0x0013C224: lea r14, [r13 + 0x158]
0x0013C22B: mov rax, qword ptr [r14]
0x0013C22E: mov qword ptr [r14 + 8], rax
0x0013C232: call 0x140391550
0x0013C237: mov rsi, rax
0x0013C23A: call 0x140391534
0x0013C23F: cqo
0x0013C241: idiv rsi
0x0013C244: imul rcx, rax, 0x3b9aca00
0x0013C24B: imul rax, rdx, 0x3b9aca00
0x0013C252: cqo
0x0013C254: idiv rsi
0x0013C257: add rcx, rax
0x0013C25A: mov qword ptr [r13 + 0x470], rcx
0x0013C261: mov rcx, qword ptr [rip + 0x6aa1a8]
0x0013C268: sub rcx, qword ptr [rip + 0x6aa199]
0x0013C26F: movabs rax, 0xc30c30c30c30c30d
0x0013C279: imul rcx
0x0013C27C: lea r12, [rcx + rdx]
0x0013C280: sar r12, 7
0x0013C284: mov rax, r12
0x0013C287: shr rax, 0x3f
0x0013C28B: add r12, rax
0x0013C28E: mov esi, r12d
0x0013C291: mov rax, qword ptr [r13 + 0x70]
0x0013C295: sub rax, qword ptr [r13 + 0x60]
0x0013C299: sar rax, 4
0x0013C29D: cmp rax, rsi
0x0013C2A0: jae 0x14013c2ad
0x0013C2A2: mov edx, esi
0x0013C2A4: lea rcx, [r13 + 0x60]
0x0013C2A8: call 0x14013a0d0
0x0013C2AD: mov rax, qword ptr [r14 + 0x10]
0x0013C2B1: sub rax, qword ptr [r14]
0x0013C2B4: sar rax, 2
0x0013C2B8: cmp rax, rsi
0x0013C2BB: jae 0x14013c2c8
0x0013C2BD: mov rdx, rsi
0x0013C2C0: mov rcx, r14
0x0013C2C3: call 0x14008b600
0x0013C2C8: xor esi, esi
0x0013C2CA: mov ebp, esi
0x0013C2CC: test r12d, r12d
0x0013C2CF: je 0x14013c491
0x0013C2D5: mov dword ptr [rsp + 0x90], esi
0x0013C2DC: nop dword ptr [rax]
0x0013C2E0: mov eax, ebp
0x0013C2E2: imul rcx, rax, 0xd8
0x0013C2E9: add rcx, qword ptr [r13 + 0x458]
0x0013C2F0: movsxd rax, ebp
0x0013C2F3: imul r8, rax, 0xa8
0x0013C2FA: add r8, qword ptr [rip + 0x6aa107]
0x0013C301: mov qword ptr [rsp + 0x28], rcx
0x0013C306: mov dword ptr [rsp + 0x20], ebp
0x0013C30A: mov r9, r13
0x0013C30D: lea rdx, [rsp + 0x38]
0x0013C312: mov rcx, r15
0x0013C315: call 0x140139f00
0x0013C31A: nop
0x0013C31B: mov rax, qword ptr [r13 + 0x68]
0x0013C31F: lea rcx, [rsp + 0x38]
0x0013C324: cmp rcx, rax
0x0013C327: jae 0x14013c374
0x0013C329: mov rcx, qword ptr [r13 + 0x60]
0x0013C32D: lea rdx, [rsp + 0x38]
0x0013C332: cmp rcx, rdx
0x0013C335: ja 0x14013c374
0x0013C337: lea rbx, [rsp + 0x38]
0x0013C33C: sub rbx, rcx
0x0013C33F: cmp rax, qword ptr [r13 + 0x70]
0x0013C343: jne 0x14013c353
0x0013C345: mov edx, 1
0x0013C34A: lea rcx, [r13 + 0x60]
0x0013C34E: call 0x14013a180
0x0013C353: mov rcx, qword ptr [r13 + 0x68]
0x0013C357: and rbx, 0xfffffffffffffff0
0x0013C35B: add rbx, qword ptr [r13 + 0x60]
0x0013C35F: test rcx, rcx
0x0013C362: je 0x14013c3b1
0x0013C364: mov qword ptr [rcx], rsi
0x0013C367: mov qword ptr [rcx + 8], rsi
0x0013C36B: mov r8, qword ptr [rbx + 8]
0x0013C36F: mov rdx, qword ptr [rbx]
0x0013C372: jmp 0x14013c3a2
0x0013C374: cmp rax, qword ptr [r13 + 0x70]
0x0013C378: jne 0x14013c388
0x0013C37A: mov edx, 1
0x0013C37F: lea rcx, [r13 + 0x60]
0x0013C383: call 0x14013a180
0x0013C388: mov rcx, qword ptr [r13 + 0x68]
0x0013C38C: test rcx, rcx
0x0013C38F: je 0x14013c3b1
0x0013C391: mov qword ptr [rcx], rsi
0x0013C394: mov qword ptr [rcx + 8], rsi
0x0013C398: mov r8, qword ptr [rsp + 0x40]
0x0013C39D: mov rdx, qword ptr [rsp + 0x38]
0x0013C3A2: test r8, r8
0x0013C3A5: je 0x14013c3ac
0x0013C3A7: lock inc dword ptr [r8 + 8]
0x0013C3AC: call 0x140058410
0x0013C3B1: add qword ptr [r13 + 0x68], 0x10
0x0013C3B6: mov rax, qword ptr [rsp + 0x38]
0x0013C3BB: xor r8d, r8d
0x0013C3BE: mov edx, dword ptr [rax + 0x98]
0x0013C3C4: lea rcx, [r13 + 0x340]
0x0013C3CB: call 0x14014abf0
0x0013C3D0: mov rax, qword ptr [r14 + 8]
0x0013C3D4: lea rcx, [rsp + 0x90]
0x0013C3DC: cmp rcx, rax
0x0013C3DF: jae 0x14013c426
0x0013C3E1: mov rcx, qword ptr [r14]
0x0013C3E4: lea rdx, [rsp + 0x90]
0x0013C3EC: cmp rcx, rdx
0x0013C3EF: ja 0x14013c426
0x0013C3F1: lea rbx, [rsp + 0x90]
0x0013C3F9: sub rbx, rcx
0x0013C3FC: sar rbx, 2
0x0013C400: cmp rax, qword ptr [r14 + 0x10]
0x0013C404: jne 0x14013c413
0x0013C406: mov edx, 1
0x0013C40B: mov rcx, r14
0x0013C40E: call 0x14008b8b0
0x0013C413: mov rax, qword ptr [r14]
0x0013C416: mov rcx, qword ptr [r14 + 8]
0x0013C41A: test rcx, rcx
0x0013C41D: je 0x14013c444
0x0013C41F: mov eax, dword ptr [rax + rbx*4]
0x0013C422: mov dword ptr [rcx], eax
0x0013C424: jmp 0x14013c444
0x0013C426: cmp rax, qword ptr [r14 + 0x10]
0x0013C42A: jne 0x14013c439
0x0013C42C: mov edx, 1
0x0013C431: mov rcx, r14
0x0013C434: call 0x14008b8b0
0x0013C439: mov rax, qword ptr [r14 + 8]
0x0013C43D: test rax, rax
0x0013C440: je 0x14013c444
0x0013C442: mov dword ptr [rax], esi
0x0013C444: add qword ptr [r14 + 8], 4
0x0013C449: mov rbx, qword ptr [rsp + 0x40]
0x0013C44E: test rbx, rbx
0x0013C451: je 0x14013c47e
0x0013C453: or eax, 0xffffffff
0x0013C456: lock xadd dword ptr [rbx + 8], eax
0x0013C45B: cmp eax, 1
0x0013C45E: jne 0x14013c47e
0x0013C460: mov rax, qword ptr [rbx]
0x0013C463: mov rcx, rbx
0x0013C466: call qword ptr [rax]
0x0013C468: or eax, 0xffffffff
0x0013C46B: lock xadd dword ptr [rbx + 0xc], eax
0x0013C470: cmp eax, 1
0x0013C473: jne 0x14013c47e
0x0013C475: mov rax, qword ptr [rbx]
0x0013C478: mov rcx, rbx
0x0013C47B: call qword ptr [rax + 8]
0x0013C47E: inc ebp
0x0013C480: cmp ebp, r12d
0x0013C483: jb 0x14013c2e0
0x0013C489: mov rbx, qword ptr [rsp + 0xa8]
0x0013C491: mov rcx, rbx
0x0013C494: call 0x140391b24
0x0013C499: test eax, eax
0x0013C49B: je 0x14013c4a5
0x0013C49D: mov ecx, eax
0x0013C49F: call 0x14039219c
0x0013C4A4: nop
0x0013C4A5: mov rcx, qword ptr [r15 + 0x38]
0x0013C4A9: test rcx, rcx
0x0013C4AC: je 0x14013c4be
0x0013C4AE: mov rax, qword ptr [rcx]
0x0013C4B1: cmp rcx, r15
0x0013C4B4: setne dl
0x0013C4B7: call qword ptr [rax + 0x20]
0x0013C4BA: mov qword ptr [r15 + 0x38], rsi
0x0013C4BE: mov al, 1
0x0013C4C0: mov rbx, qword ptr [rsp + 0x98]
0x0013C4C8: add rsp, 0x50
0x0013C4CC: pop r15
0x0013C4CE: pop r14
0x0013C4D0: pop r13
0x0013C4D2: pop r12
0x0013C4D4: pop rdi
0x0013C4D5: pop rsi
0x0013C4D6: pop rbp
0x0013C4D7: ret
```

## target `0x000584A0` PDATA `0x000584A0..0x00058581`

### Calls / interesting accesses

| RVA | kind | instruction |
|---|---|---|
| `0x000584E9` | context | `mov r9, qword ptr [rsp + 0x90]` |
| `0x000584FD` | call | `direct 0x000582D0` |
| `0x00058508` | call | `direct 0x00145010` |
| `0x00058514` | context | `mov r9, qword ptr [rsp + 0x90]` |
| `0x00058531` | call | `direct 0x00058210` |
| `0x0005853C` | call | `direct 0x00145010` |
| `0x00058560` | call | `indirect qword ptr [rax]` |
| `0x00058572` | call | `indirect qword ptr [rax + 8]` |

### Full disassembly
```asm
0x000584A0: mov r11, rsp
0x000584A3: mov dword ptr [r11 + 0x20], r9d
0x000584A7: mov qword ptr [r11 + 0x18], r8
0x000584AB: mov qword ptr [r11 + 8], rcx
0x000584AF: push rbx
0x000584B0: push rsi
0x000584B1: push rdi
0x000584B2: sub rsp, 0x50
0x000584B6: mov qword ptr [r11 - 0x40], 0xfffffffffffffffe
0x000584BE: mov rsi, rcx
0x000584C1: xor eax, eax
0x000584C3: mov dword ptr [rsp + 0x20], eax
0x000584C7: mov qword ptr [rcx], rax
0x000584CA: mov qword ptr [rcx + 8], rax
0x000584CE: mov dword ptr [rsp + 0x20], 1
0x000584D6: mov r8d, dword ptr [rdx]
0x000584D9: sub r8d, 1
0x000584DD: je 0x140058514
0x000584DF: cmp r8d, 1
0x000584E3: jne 0x140058575
0x000584E9: mov r9, qword ptr [rsp + 0x90]
0x000584F1: lea r8, [r11 + 0x20]
0x000584F5: lea rdx, [r11 + 0x18]
0x000584F9: lea rcx, [r11 - 0x38]
0x000584FD: call 0x1400582d0
0x00058502: mov rdx, rax
0x00058505: mov rcx, rsi
0x00058508: call 0x140145010
0x0005850D: mov rdi, qword ptr [rsp + 0x38]
0x00058512: jmp 0x140058546
0x00058514: mov r9, qword ptr [rsp + 0x90]
0x0005851C: lea r8, [rsp + 0x88]
0x00058524: lea rdx, [rsp + 0x80]
0x0005852C: lea rcx, [rsp + 0x40]
0x00058531: call 0x140058210
0x00058536: mov rdx, rax
0x00058539: mov rcx, rsi
0x0005853C: call 0x140145010
0x00058541: mov rdi, qword ptr [rsp + 0x48]
0x00058546: test rdi, rdi
0x00058549: je 0x140058575
0x0005854B: or ebx, 0xffffffff
0x0005854E: mov eax, ebx
0x00058550: lock xadd dword ptr [rdi + 8], eax
0x00058555: cmp eax, 1
0x00058558: jne 0x140058575
0x0005855A: mov rax, qword ptr [rdi]
0x0005855D: mov rcx, rdi
0x00058560: call qword ptr [rax]
0x00058562: lock xadd dword ptr [rdi + 0xc], ebx
0x00058567: cmp ebx, 1
0x0005856A: jne 0x140058575
0x0005856C: mov rax, qword ptr [rdi]
0x0005856F: mov rcx, rdi
0x00058572: call qword ptr [rax + 8]
0x00058575: mov rax, rsi
0x00058578: add rsp, 0x50
0x0005857C: pop rdi
0x0005857D: pop rsi
0x0005857E: pop rbx
0x0005857F: ret
0x00058580: int3
```

## target `0x00058410` PDATA `0x00058410..0x00058436`

### Calls / interesting accesses

| RVA | kind | instruction |
|---|---|---|

### Full disassembly
```asm
0x00058410: mov qword ptr [rsp + 0x10], rbx
0x00058415: mov qword ptr [rsp + 0x18], rbp
0x0005841A: mov qword ptr [rsp + 0x20], rsi
0x0005841F: push rdi
0x00058420: sub rsp, 0x20
0x00058424: mov rdi, qword ptr [rcx + 8]
0x00058428: mov rsi, r8
0x0005842B: mov rbp, rdx
0x0005842E: mov rbx, rcx
0x00058431: test rdi, rdi
0x00058434: je 0x140058493
```

## target `0x00145010` PDATA `0x00145010..0x00145048`

### Calls / interesting accesses

| RVA | kind | instruction |
|---|---|---|

### Full disassembly
```asm
0x00145010: push rdi
0x00145012: sub rsp, 0x30
0x00145016: mov r8, qword ptr [rdx]
0x00145019: mov rdi, rcx
0x0014501C: mov rax, qword ptr [rdx + 8]
0x00145020: xor ecx, ecx
0x00145022: mov qword ptr [rdx], rcx
0x00145025: mov qword ptr [rdx + 8], rcx
0x00145029: mov rcx, qword ptr [rdi + 8]
0x0014502D: mov qword ptr [rdi + 8], rax
0x00145031: mov qword ptr [rsp + 0x20], r8
0x00145036: mov qword ptr [rsp + 0x40], rax
0x0014503B: mov qword ptr [rsp + 0x28], rcx
0x00145040: mov qword ptr [rdi], r8
0x00145043: test rcx, rcx
0x00145046: je 0x140145096
```
