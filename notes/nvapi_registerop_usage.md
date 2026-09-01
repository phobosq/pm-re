# NvAPI_GPU_RegisterOp (0x2EB3C140) usage in PhoenixMiner 6.2c

Global function slot: `0x007E7B08`.

References found: `7`.

## hit 1: `0x001E0CCE` in `0x001E0CA0..0x001E0EC0`

Instruction: `mov rdi, qword ptr [rip + 0x606e33]`

### Direct callers of containing function

- `0x001DE9C7` from `0x001DE8B0..0x001DF630`

### Context

```asm
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
0x001E0D7E: mov rax, rcx
0x001E0D81: shr rax, 0x11
0x001E0D85: and eax, 0x7f
0x001E0D88: mov dword ptr [rbx], eax
0x001E0D8A: mov rax, rcx
0x001E0D8D: shr rax, 0x18
0x001E0D91: and eax, 0x7f
0x001E0D94: shr rcx, 8
0x001E0D98: mov dword ptr [rbx + 4], eax
0x001E0D9B: and ecx, 0x1ff
0x001E0DA1: movzx eax, byte ptr [rsp + 0x38]
0x001E0DA6: mov dword ptr [rbx + 0xc], eax
0x001E0DA9: mov eax, dword ptr [rsp + 0x50]
0x001E0DAD: and eax, 0x7f
0x001E0DB0: mov dword ptr [rbx + 8], ecx
0x001E0DB3: mov rcx, qword ptr [rsp + 0x50]
0x001E0DB8: mov dword ptr [rbx + 0x10], eax
0x001E0DBB: mov rax, rcx
0x001E0DBE: shr rax, 7
0x001E0DC2: and eax, 0x7f
0x001E0DC5: mov dword ptr [rbx + 0x14], eax
0x001E0DC8: mov rax, rcx
0x001E0DCB: shr rax, 0xe
0x001E0DCF: and eax, 0x3f
0x001E0DD2: shr rcx, 0x14
0x001E0DD6: mov dword ptr [rbx + 0x18], eax
0x001E0DD9: and ecx, 0x3f
0x001E0DDC: mov eax, dword ptr [rsp + 0x68]
0x001E0DE0: and eax, 0xf
0x001E0DE3: mov dword ptr [rbx + 0x1c], ecx
0x001E0DE6: mov rcx, qword ptr [rsp + 0x68]
0x001E0DEB: mov dword ptr [rbx + 0x20], eax
0x001E0DEE: mov rax, rcx
0x001E0DF1: shr rax, 4
0x001E0DF5: and eax, 0xf
0x001E0DF8: mov dword ptr [rbx + 0x24], eax
0x001E0DFB: mov rax, rcx
0x001E0DFE: shr rax, 8
0x001E0E02: and eax, 0x7f
0x001E0E05: mov dword ptr [rbx + 0x28], eax
0x001E0E08: mov rax, rcx
0x001E0E0B: shr rax, 0x10
0x001E0E0F: and eax, 0x7f
0x001E0E12: mov dword ptr [rbx + 0x2c], eax
0x001E0E15: mov rax, rcx
0x001E0E18: shr rax, 0x18
```

### Last argument-register writes before call/reference

- `rcx`: no local write in last 30 instructions
- `rdx`: no local write in last 30 instructions
- `r8`: no local write in last 30 instructions
- `r9`: no local write in last 30 instructions

## hit 2: `0x001ECC46` in `0x001ECB90..0x001ED0AB`

Instruction: `cmp qword ptr [rip + 0x5faeba], 0`

### Direct callers of containing function

- `0x001DF246` from `0x001DE8B0..0x001DF630`
- `0x001DF43E` from `0x001DE8B0..0x001DF630`

### Context

```asm
0x001ECB90: push rbp
0x001ECB92: push rsi
0x001ECB93: push rdi
0x001ECB94: push r12
0x001ECB96: push r13
0x001ECB98: push r14
0x001ECB9A: push r15
0x001ECB9C: lea rbp, [rsp - 0x5fc0]
0x001ECBA4: mov eax, 0x60c0
0x001ECBA9: call 0x1403b2500
0x001ECBAE: sub rsp, rax
0x001ECBB1: mov qword ptr [rsp + 0x28], 0xfffffffffffffffe
0x001ECBBA: mov qword ptr [rsp + 0x6108], rbx
0x001ECBC2: mov rax, qword ptr [rip + 0x5e9d27]
0x001ECBC9: xor rax, rsp
0x001ECBCC: mov qword ptr [rbp + 0x5fb0], rax
0x001ECBD3: mov dword ptr [rsp + 0x24], r9d
0x001ECBD8: mov r14, r8
0x001ECBDB: mov r15, rdx
0x001ECBDE: mov rbx, rcx
0x001ECBE1: mov r8d, 0x5c
0x001ECBE7: mov rcx, r14
0x001ECBEA: call 0x1403d2f70
0x001ECBEF: test eax, eax
0x001ECBF1: jne 0x1401ecbfa
0x001ECBF3: mov al, 1
0x001ECBF5: jmp 0x1401ed081
0x001ECBFA: mov dil, 1
0x001ECBFD: xor r12b, r12b
0x001ECC00: cmp dword ptr [rbx + 0x258], 0
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
```

### Last argument-register writes before call/reference

- `rcx`: `0x001ECC18: lea rcx, [rbx + 0x26c]`
- `rdx`: no local write in last 30 instructions
- `r8`: no local write in last 30 instructions
- `r9`: no local write in last 30 instructions

## hit 3: `0x001ECCB6` in `0x001ECB90..0x001ED0AB`

Instruction: `call qword ptr [rip + 0x5fae4c]`

### Direct callers of containing function

- `0x001DF246` from `0x001DE8B0..0x001DF630`
- `0x001DF43E` from `0x001DE8B0..0x001DF630`

### Context

```asm
0x001ECBBA: mov qword ptr [rsp + 0x6108], rbx
0x001ECBC2: mov rax, qword ptr [rip + 0x5e9d27]
0x001ECBC9: xor rax, rsp
0x001ECBCC: mov qword ptr [rbp + 0x5fb0], rax
0x001ECBD3: mov dword ptr [rsp + 0x24], r9d
0x001ECBD8: mov r14, r8
0x001ECBDB: mov r15, rdx
0x001ECBDE: mov rbx, rcx
0x001ECBE1: mov r8d, 0x5c
0x001ECBE7: mov rcx, r14
0x001ECBEA: call 0x1403d2f70
0x001ECBEF: test eax, eax
0x001ECBF1: jne 0x1401ecbfa
0x001ECBF3: mov al, 1
0x001ECBF5: jmp 0x1401ed081
0x001ECBFA: mov dil, 1
0x001ECBFD: xor r12b, r12b
0x001ECC00: cmp dword ptr [rbx + 0x258], 0
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
```

### Last argument-register writes before call/reference

- `rcx`: `0x001ECCAF: mov rcx, qword ptr [rbx + 0xd0]`
- `rdx`: `0x001ECCAA: lea rdx, [rsp + 0x70]`
- `r8`: no local write in last 30 instructions
- `r9`: no local write in last 30 instructions

## hit 4: `0x001ECD39` in `0x001ECB90..0x001ED0AB`

Instruction: `call qword ptr [rip + 0x5fadc9]`

### Direct callers of containing function

- `0x001DF246` from `0x001DE8B0..0x001DF630`
- `0x001DF43E` from `0x001DE8B0..0x001DF630`

### Context

```asm
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
0x001ECE62: test dil, dil
0x001ECE65: je 0x1401ed07d
0x001ECE6B: test r13b, r13b
0x001ECE6E: je 0x1401ed07d
0x001ECE74: mov dword ptr [rsp + 0x30], 0x22
0x001ECE7C: mov eax, dword ptr [rsp + 0x30]
0x001ECE80: add al, 0x22
0x001ECE82: movsx ecx, al
0x001ECE85: xor ecx, 0x71
0x001ECE88: mov dword ptr [rsp + 0x34], ecx
0x001ECE8C: mov eax, dword ptr [rsp + 0x34]
0x001ECE90: mov ecx, dword ptr [rsp + 0x30]
0x001ECE94: xor ecx, eax
0x001ECE96: xor ecx, 0x7b
0x001ECE99: mov byte ptr [rsp + 0x38], cl
0x001ECE9D: movsx ecx, byte ptr [rsp + 0x38]
0x001ECEA2: mov eax, dword ptr [rsp + 0x30]
0x001ECEA6: inc al
0x001ECEA8: xor eax, ecx
0x001ECEAA: xor eax, 0x7d
```

### Last argument-register writes before call/reference

- `rcx`: `0x001ECD32: mov rcx, qword ptr [rbx + 0xd0]`
- `rdx`: `0x001ECD2B: lea rdx, [rbp + 0x1780]`
- `r8`: no local write in last 30 instructions
- `r9`: no local write in last 30 instructions

## hit 5: `0x001ECDBC` in `0x001ECB90..0x001ED0AB`

Instruction: `call qword ptr [rip + 0x5fad46]`

### Direct callers of containing function

- `0x001DF246` from `0x001DE8B0..0x001DF630`
- `0x001DF43E` from `0x001DE8B0..0x001DF630`

### Context

```asm
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
0x001ECE62: test dil, dil
0x001ECE65: je 0x1401ed07d
0x001ECE6B: test r13b, r13b
0x001ECE6E: je 0x1401ed07d
0x001ECE74: mov dword ptr [rsp + 0x30], 0x22
0x001ECE7C: mov eax, dword ptr [rsp + 0x30]
0x001ECE80: add al, 0x22
0x001ECE82: movsx ecx, al
0x001ECE85: xor ecx, 0x71
0x001ECE88: mov dword ptr [rsp + 0x34], ecx
0x001ECE8C: mov eax, dword ptr [rsp + 0x34]
0x001ECE90: mov ecx, dword ptr [rsp + 0x30]
0x001ECE94: xor ecx, eax
0x001ECE96: xor ecx, 0x7b
0x001ECE99: mov byte ptr [rsp + 0x38], cl
0x001ECE9D: movsx ecx, byte ptr [rsp + 0x38]
0x001ECEA2: mov eax, dword ptr [rsp + 0x30]
0x001ECEA6: inc al
0x001ECEA8: xor eax, ecx
0x001ECEAA: xor eax, 0x7d
0x001ECEAD: mov byte ptr [rsp + 0x39], al
0x001ECEB1: movsx ecx, byte ptr [rsp + 0x39]
0x001ECEB6: mov eax, dword ptr [rsp + 0x30]
0x001ECEBA: add al, 2
0x001ECEBC: xor eax, ecx
0x001ECEBE: xor eax, 0x3a
0x001ECEC1: mov byte ptr [rsp + 0x3a], al
0x001ECEC5: movsx ecx, byte ptr [rsp + 0x3a]
0x001ECECA: mov eax, dword ptr [rsp + 0x30]
0x001ECECE: add al, 3
0x001ECED0: xor eax, ecx
0x001ECED2: xor eax, 0x20
0x001ECED5: mov byte ptr [rsp + 0x3b], al
0x001ECED9: movsx ecx, byte ptr [rsp + 0x3b]
0x001ECEDE: mov eax, dword ptr [rsp + 0x30]
0x001ECEE2: add al, 4
0x001ECEE4: xor eax, ecx
0x001ECEE6: xor eax, 0x72
0x001ECEE9: mov byte ptr [rsp + 0x3c], al
0x001ECEED: movsx ecx, byte ptr [rsp + 0x3c]
0x001ECEF2: mov eax, dword ptr [rsp + 0x30]
0x001ECEF6: add al, 5
0x001ECEF8: xor eax, ecx
0x001ECEFA: xor eax, 0x65
0x001ECEFD: mov byte ptr [rsp + 0x3d], al
0x001ECF01: movsx ecx, byte ptr [rsp + 0x3d]
```

### Last argument-register writes before call/reference

- `rcx`: `0x001ECDB5: mov rcx, qword ptr [rbx + 0xd0]`
- `rdx`: `0x001ECDAE: lea rdx, [rbp + 0x2f90]`
- `r8`: no local write in last 30 instructions
- `r9`: no local write in last 30 instructions

## hit 6: `0x001ECE3F` in `0x001ECB90..0x001ED0AB`

Instruction: `call qword ptr [rip + 0x5facc3]`

### Direct callers of containing function

- `0x001DF246` from `0x001DE8B0..0x001DF630`
- `0x001DF43E` from `0x001DE8B0..0x001DF630`

### Context

```asm
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
0x001ECE62: test dil, dil
0x001ECE65: je 0x1401ed07d
0x001ECE6B: test r13b, r13b
0x001ECE6E: je 0x1401ed07d
0x001ECE74: mov dword ptr [rsp + 0x30], 0x22
0x001ECE7C: mov eax, dword ptr [rsp + 0x30]
0x001ECE80: add al, 0x22
0x001ECE82: movsx ecx, al
0x001ECE85: xor ecx, 0x71
0x001ECE88: mov dword ptr [rsp + 0x34], ecx
0x001ECE8C: mov eax, dword ptr [rsp + 0x34]
0x001ECE90: mov ecx, dword ptr [rsp + 0x30]
0x001ECE94: xor ecx, eax
0x001ECE96: xor ecx, 0x7b
0x001ECE99: mov byte ptr [rsp + 0x38], cl
0x001ECE9D: movsx ecx, byte ptr [rsp + 0x38]
0x001ECEA2: mov eax, dword ptr [rsp + 0x30]
0x001ECEA6: inc al
0x001ECEA8: xor eax, ecx
0x001ECEAA: xor eax, 0x7d
0x001ECEAD: mov byte ptr [rsp + 0x39], al
0x001ECEB1: movsx ecx, byte ptr [rsp + 0x39]
0x001ECEB6: mov eax, dword ptr [rsp + 0x30]
0x001ECEBA: add al, 2
0x001ECEBC: xor eax, ecx
0x001ECEBE: xor eax, 0x3a
0x001ECEC1: mov byte ptr [rsp + 0x3a], al
0x001ECEC5: movsx ecx, byte ptr [rsp + 0x3a]
0x001ECECA: mov eax, dword ptr [rsp + 0x30]
0x001ECECE: add al, 3
0x001ECED0: xor eax, ecx
0x001ECED2: xor eax, 0x20
0x001ECED5: mov byte ptr [rsp + 0x3b], al
0x001ECED9: movsx ecx, byte ptr [rsp + 0x3b]
0x001ECEDE: mov eax, dword ptr [rsp + 0x30]
0x001ECEE2: add al, 4
0x001ECEE4: xor eax, ecx
0x001ECEE6: xor eax, 0x72
0x001ECEE9: mov byte ptr [rsp + 0x3c], al
0x001ECEED: movsx ecx, byte ptr [rsp + 0x3c]
0x001ECEF2: mov eax, dword ptr [rsp + 0x30]
0x001ECEF6: add al, 5
0x001ECEF8: xor eax, ecx
0x001ECEFA: xor eax, 0x65
0x001ECEFD: mov byte ptr [rsp + 0x3d], al
0x001ECF01: movsx ecx, byte ptr [rsp + 0x3d]
0x001ECF06: mov eax, dword ptr [rsp + 0x30]
0x001ECF0A: add al, 6
0x001ECF0C: xor eax, ecx
0x001ECF0E: xor eax, 0x73
0x001ECF11: mov byte ptr [rsp + 0x3e], al
0x001ECF15: movsx ecx, byte ptr [rsp + 0x3e]
0x001ECF1A: mov eax, dword ptr [rsp + 0x30]
0x001ECF1E: add al, 7
0x001ECF20: xor eax, ecx
0x001ECF22: xor eax, 0x65
0x001ECF25: mov byte ptr [rsp + 0x3f], al
0x001ECF29: movsx ecx, byte ptr [rsp + 0x3f]
0x001ECF2E: mov eax, dword ptr [rsp + 0x30]
0x001ECF32: add al, 8
0x001ECF34: xor eax, ecx
0x001ECF36: xor eax, 0x74
0x001ECF39: mov byte ptr [rsp + 0x40], al
0x001ECF3D: movsx ecx, byte ptr [rsp + 0x40]
0x001ECF42: mov eax, dword ptr [rsp + 0x30]
0x001ECF46: add al, 9
0x001ECF48: xor eax, ecx
0x001ECF4A: xor eax, 0x20
0x001ECF4D: mov byte ptr [rsp + 0x41], al
0x001ECF51: movsx ecx, byte ptr [rsp + 0x41]
0x001ECF56: mov eax, dword ptr [rsp + 0x30]
0x001ECF5A: add al, 0xa
```

### Last argument-register writes before call/reference

- `rcx`: `0x001ECE38: mov rcx, qword ptr [rbx + 0xd0]`
- `rdx`: `0x001ECE31: lea rdx, [rbp + 0x47a0]`
- `r8`: no local write in last 30 instructions
- `r9`: no local write in last 30 instructions

## hit 7: `0x001FE6D5` in `0x001FE160..0x001FE730`

Instruction: `mov qword ptr [rip + 0x5e942c], rax`

### Direct callers of containing function

- `0x001DD7AA` from `0x001DC0C0..0x001DE7D3`

### Context

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
0x001FE700: call 0x1403db020
0x001FE705: int3
0x001FE706: call 0x1403db020
0x001FE70B: int3
0x001FE70C: call 0x1403db020
0x001FE711: int3
0x001FE712: call 0x1403db020
0x001FE717: int3
0x001FE718: call 0x1403db020
0x001FE71D: int3
0x001FE71E: call 0x1403db020
0x001FE723: int3
0x001FE724: call 0x1403db020
0x001FE729: int3
0x001FE72A: call 0x1403db020
0x001FE72F: int3
```

### Last argument-register writes before call/reference

- `rcx`: no local write in last 30 instructions
- `rdx`: no local write in last 30 instructions
- `r8`: no local write in last 30 instructions
- `r9`: no local write in last 30 instructions
