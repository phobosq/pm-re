# Type2 dynamic API slots

Indirect RIP-call slots discovered in `0x001D4A80`.

| callsite | slot RVA |
|---|---|
| `0x001D4C4C` | `0x007E7848` |
| `0x001D4ECC` | `0x007E7840` |
| `0x001D4EE0` | `0x007E7858` |

## All code refs to slots

| slot | RVA | PDATA | access | instruction |
|---|---|---|---|---|
| `0x007E7840` | `0x001D1E37` | `0x001D123E..0x001D353C` | dst/write-ish | `mov qword ptr [rip + 0x615a02], rax` |
| `0x007E7848` | `0x001D20A3` | `0x001D123E..0x001D353C` | dst/write-ish | `mov qword ptr [rip + 0x61579e], rax` |
| `0x007E7858` | `0x001D24F1` | `0x001D123E..0x001D353C` | dst/write-ish | `mov qword ptr [rip + 0x615360], rax` |
| `0x007E7848` | `0x001D4C4C` | `0x001D4A80..0x001D5DC9` | indirect-call | `call qword ptr [rip + 0x612bf6]` |
| `0x007E7840` | `0x001D4ECC` | `0x001D4A80..0x001D5DC9` | indirect-call | `call qword ptr [rip + 0x61296e]` |
| `0x007E7858` | `0x001D4EE0` | `0x001D4A80..0x001D5DC9` | indirect-call | `call qword ptr [rip + 0x612972]` |
| `0x007E7848` | `0x001D6EDC` | `0x001D6E40..0x001D6F2A` | indirect-call | `call qword ptr [rip + 0x610966]` |
| `0x007E7840` | `0x001D6F06` | `0x001D6E40..0x001D6F2A` | indirect-call | `call qword ptr [rip + 0x610934]` |
| `0x007E7858` | `0x001D7123` | `0x001D6F30..0x001D748E` | indirect-call | `call qword ptr [rip + 0x61072f]` |
| `0x007E7858` | `0x001D94EF` | `0x001D9490..0x001D97A5` | indirect-call | `call qword ptr [rip + 0x60e363]` |
| `0x007E7858` | `0x001DC35D` | `0x001DC0C0..0x001DE7D3` | indirect-call | `call qword ptr [rip + 0x60b4f5]` |
| `0x007E7858` | `0x001DC81E` | `0x001DC0C0..0x001DE7D3` | indirect-call | `call qword ptr [rip + 0x60b034]` |
| `0x007E7858` | `0x001DF68C` | `0x001DF630..0x001E0B3C` | indirect-call | `call qword ptr [rip + 0x6081c6]` |
| `0x007E7840` | `0x001DFDD3` | `0x001DF630..0x001E0B3C` | indirect-call | `call qword ptr [rip + 0x607a67]` |
| `0x007E7858` | `0x001DFDE5` | `0x001DF630..0x001E0B3C` | indirect-call | `call qword ptr [rip + 0x607a6d]` |
| `0x007E7858` | `0x001E053B` | `0x001DF630..0x001E0B3C` | indirect-call | `call qword ptr [rip + 0x607317]` |

## Ref contexts

### slot `0x007E7840` in `0x001D123E..0x001D353C`

```asm
0x001D1DEA: xor ecx, 0x5f
0x001D1DED: add ecx, 9
0x001D1DF0: mov byte ptr [rbp + 0x36], cl
0x001D1DF3: movsx ecx, byte ptr [rbp + 0x36]
0x001D1DF7: xor ecx, 0x76
0x001D1DFA: add ecx, 9
0x001D1DFD: mov byte ptr [rbp + 0x37], cl
0x001D1E00: movsx ecx, byte ptr [rbp + 0x37]
0x001D1E04: xor ecx, 0x32
0x001D1E07: add ecx, 9
0x001D1E0A: mov byte ptr [rbp + 0x38], cl
0x001D1E0D: lea rcx, [rbp + 0x18]
0x001D1E11: mov byte ptr [rbp + 0x39], sil
0x001D1E15: movzx eax, byte ptr [rbp + 0x1c]
0x001D1E19: call 0x1401d35c0
0x001D1E1E: cmp qword ptr [rax + 0x18], 0x10
0x001D1E23: jb 0x1401d1e28
0x001D1E25: mov rax, qword ptr [rax]
0x001D1E28: mov rdx, rax
0x001D1E2B: mov rcx, rdi
0x001D1E2E: call qword ptr [rip + 0x25e3b4]
0x001D1E34: test rax, rax
0x001D1E37: mov qword ptr [rip + 0x615a02], rax
0x001D1E3E: lea rcx, [rbp + 0x3d0]
0x001D1E45: sete bl
0x001D1E48: call 0x140032ef0
0x001D1E4D: test bl, bl
0x001D1E4F: jne 0x1401d350a
0x001D1E55: mov dword ptr [rbp + 0x110], 0x5d
0x001D1E5F: mov dword ptr [rbp + 0x114], 0x54
0x001D1E69: mov eax, dword ptr [rbp + 0x114]
0x001D1E6F: xor eax, 0x33
0x001D1E72: mov byte ptr [rbp + 0x118], al
0x001D1E78: movsx ecx, byte ptr [rbp + 0x118]
0x001D1E7F: xor ecx, 0x2b
0x001D1E82: mov byte ptr [rbp + 0x119], cl
0x001D1E88: movsx ecx, byte ptr [rbp + 0x119]
0x001D1E8F: xor ecx, 0x30
0x001D1E92: mov byte ptr [rbp + 0x11a], cl
0x001D1E98: movsx ecx, byte ptr [rbp + 0x11a]
0x001D1E9F: xor ecx, 0x31
0x001D1EA2: mov byte ptr [rbp + 0x11b], cl
0x001D1EA8: movsx ecx, byte ptr [rbp + 0x11b]
0x001D1EAF: xor ecx, 0x19
0x001D1EB2: mov byte ptr [rbp + 0x11c], cl
0x001D1EB8: movsx ecx, byte ptr [rbp + 0x11c]
0x001D1EBF: xor ecx, 0x38
0x001D1EC2: mov byte ptr [rbp + 0x11d], cl
0x001D1EC8: movsx ecx, byte ptr [rbp + 0x11d]
0x001D1ECF: xor ecx, 0x2b
0x001D1ED2: mov byte ptr [rbp + 0x11e], cl
0x001D1ED8: movsx ecx, byte ptr [rbp + 0x11e]
```

Nearby imports / literal refs:

- `0x001D1E2E` -> `KERNEL32.dll!GetProcAddress`

### slot `0x007E7848` in `0x001D123E..0x001D353C`

```asm
0x001D2038: xor ecx, 0x39
0x001D203B: mov byte ptr [rbp + 0x134], cl
0x001D2041: movsx ecx, byte ptr [rbp + 0x134]
0x001D2048: xor ecx, 2
0x001D204B: mov byte ptr [rbp + 0x135], cl
0x001D2051: movsx ecx, byte ptr [rbp + 0x135]
0x001D2058: xor ecx, 0x2b
0x001D205B: mov byte ptr [rbp + 0x136], cl
0x001D2061: movsx ecx, byte ptr [rbp + 0x136]
0x001D2068: xor ecx, 0x6f
0x001D206B: mov byte ptr [rbp + 0x138], al
0x001D2071: mov byte ptr [rbp + 0x137], cl
0x001D2077: lea rcx, [rbp + 0x110]
0x001D207E: movzx eax, byte ptr [rbp + 0x118]
0x001D2085: call 0x1401a5430
0x001D208A: cmp qword ptr [rax + 0x18], 0x10
0x001D208F: jb 0x1401d2094
0x001D2091: mov rax, qword ptr [rax]
0x001D2094: mov rdx, rax
0x001D2097: mov rcx, rdi
0x001D209A: call qword ptr [rip + 0x25e148]
0x001D20A0: test rax, rax
0x001D20A3: mov qword ptr [rip + 0x61579e], rax
0x001D20AA: lea rcx, [rbp + 0x3f0]
0x001D20B1: sete bl
0x001D20B4: call 0x140032ef0
0x001D20B9: test bl, bl
0x001D20BB: jne 0x1401d350a
0x001D20C1: mov dword ptr [rbp - 0x80], 0xe
0x001D20C8: mov eax, dword ptr [rbp - 0x80]
0x001D20CB: xor eax, 0x6e
0x001D20CE: add eax, 3
0x001D20D1: mov byte ptr [rbp - 0x7c], al
0x001D20D4: movsx ecx, byte ptr [rbp - 0x7c]
0x001D20D8: xor ecx, 0x76
0x001D20DB: add ecx, 3
0x001D20DE: mov byte ptr [rbp - 0x7b], cl
0x001D20E1: movsx ecx, byte ptr [rbp - 0x7b]
0x001D20E5: xor ecx, 0x6d
0x001D20E8: add ecx, 3
0x001D20EB: mov byte ptr [rbp - 0x7a], cl
0x001D20EE: movsx ecx, byte ptr [rbp - 0x7a]
0x001D20F2: xor ecx, 0x6c
0x001D20F5: add ecx, 3
0x001D20F8: mov byte ptr [rbp - 0x79], cl
0x001D20FB: movsx ecx, byte ptr [rbp - 0x79]
0x001D20FF: xor ecx, 0x44
0x001D2102: add ecx, 3
0x001D2105: mov byte ptr [rbp - 0x78], cl
0x001D2108: movsx ecx, byte ptr [rbp - 0x78]
0x001D210C: xor ecx, 0x65
0x001D210F: add ecx, 3
```

Nearby imports / literal refs:

- `0x001D209A` -> `KERNEL32.dll!GetProcAddress`

### slot `0x007E7858` in `0x001D123E..0x001D353C`

```asm
0x001D2486: xor ecx, 5
0x001D2489: mov byte ptr [rbp + 0x17b], cl
0x001D248F: movsx ecx, byte ptr [rbp + 0x17b]
0x001D2496: xor ecx, 0x1e
0x001D2499: mov byte ptr [rbp + 0x17c], cl
0x001D249F: movsx ecx, byte ptr [rbp + 0x17c]
0x001D24A6: xor ecx, 0x19
0x001D24A9: mov byte ptr [rbp + 0x17d], cl
0x001D24AF: movsx ecx, byte ptr [rbp + 0x17d]
0x001D24B6: xor ecx, 0x10
0x001D24B9: mov byte ptr [rbp + 0x17f], al
0x001D24BF: mov byte ptr [rbp + 0x17e], cl
0x001D24C5: lea rcx, [rbp + 0x168]
0x001D24CC: movzx eax, byte ptr [rbp + 0x170]
0x001D24D3: call 0x140178f80
0x001D24D8: cmp qword ptr [rax + 0x18], 0x10
0x001D24DD: jb 0x1401d24e2
0x001D24DF: mov rax, qword ptr [rax]
0x001D24E2: mov rdx, rax
0x001D24E5: mov rcx, rdi
0x001D24E8: call qword ptr [rip + 0x25dcfa]
0x001D24EE: test rax, rax
0x001D24F1: mov qword ptr [rip + 0x615360], rax
0x001D24F8: lea rcx, [rbp + 0x270]
0x001D24FF: sete bl
0x001D2502: call 0x140032ef0
0x001D2507: test bl, bl
0x001D2509: jne 0x1401d350a
0x001D250F: mov dword ptr [rbp + 0xb0], 0x6d
0x001D2519: mov eax, dword ptr [rbp + 0xb0]
0x001D251F: xor eax, 0x6e
0x001D2522: add eax, 5
0x001D2525: mov byte ptr [rbp + 0xb4], al
0x001D252B: movsx ecx, byte ptr [rbp + 0xb4]
0x001D2532: xor ecx, 0x76
0x001D2535: add ecx, 5
0x001D2538: mov byte ptr [rbp + 0xb5], cl
0x001D253E: movsx ecx, byte ptr [rbp + 0xb5]
0x001D2545: xor ecx, 0x6d
0x001D2548: add ecx, 5
0x001D254B: mov byte ptr [rbp + 0xb6], cl
0x001D2551: movsx ecx, byte ptr [rbp + 0xb6]
0x001D2558: xor ecx, 0x6c
0x001D255B: add ecx, 5
0x001D255E: mov byte ptr [rbp + 0xb7], cl
0x001D2564: movsx ecx, byte ptr [rbp + 0xb7]
0x001D256B: xor ecx, 0x44
0x001D256E: add ecx, 5
0x001D2571: mov byte ptr [rbp + 0xb8], cl
0x001D2577: movsx ecx, byte ptr [rbp + 0xb8]
0x001D257E: xor ecx, 0x65
0x001D2581: add ecx, 5
```

Nearby imports / literal refs:

- `0x001D24E8` -> `KERNEL32.dll!GetProcAddress`

### slot `0x007E7848` in `0x001D4A80..0x001D5DC9`

```asm
0x001D4BFE: imul rcx
0x001D4C01: sar rdx, 4
0x001D4C05: mov rax, rdx
0x001D4C08: shr rax, 0x3f
0x001D4C0C: add rdx, rax
0x001D4C0F: je 0x1401d4eaa
0x001D4C15: mov rax, rdi
0x001D4C18: nop dword ptr [rax + rax]
0x001D4C20: lea rax, [rax + rax*4]
0x001D4C24: lea r14, [r8 + rax*8]
0x001D4C28: cmp qword ptr [r14], r9
0x001D4C2B: je 0x1401d4c3b
0x001D4C2D: inc esi
0x001D4C2F: mov eax, esi
0x001D4C31: cmp rax, rdx
0x001D4C34: jb 0x1401d4c20
0x001D4C36: jmp 0x1401d4ea3
0x001D4C3B: lea rcx, [r14 + 8]
0x001D4C3F: cmp qword ptr [rcx + 0x18], 0x10
0x001D4C44: jb 0x1401d4c49
0x001D4C46: mov rcx, qword ptr [rcx]
0x001D4C49: mov rdx, r15
0x001D4C4C: call qword ptr [rip + 0x612bf6]
0x001D4C52: mov dword ptr [rsp + 0x30], eax
0x001D4C56: test eax, eax
0x001D4C58: je 0x1401d4e97
0x001D4C5E: mov dword ptr [rbp + 0x10], 0x5a
0x001D4C65: mov dword ptr [rbp + 0x14], 0x75
0x001D4C6C: mov eax, dword ptr [rbp + 0x14]
0x001D4C6F: xor eax, 0x21
0x001D4C72: mov byte ptr [rbp + 0x18], al
0x001D4C75: movsx ecx, byte ptr [rbp + 0x18]
0x001D4C79: xor ecx, 0x27
0x001D4C7C: mov byte ptr [rbp + 0x19], cl
0x001D4C7F: movsx ecx, byte ptr [rbp + 0x19]
0x001D4C83: xor ecx, 0x60
0x001D4C86: mov byte ptr [rbp + 0x1a], cl
0x001D4C89: movsx ecx, byte ptr [rbp + 0x1a]
0x001D4C8D: xor ecx, 0x7a
0x001D4C90: mov byte ptr [rbp + 0x1b], cl
0x001D4C93: movsx ecx, byte ptr [rbp + 0x1b]
0x001D4C97: xor ecx, 0x2f
0x001D4C9A: mov byte ptr [rbp + 0x1c], cl
0x001D4C9D: movsx ecx, byte ptr [rbp + 0x1c]
0x001D4CA1: xor ecx, 0x34
0x001D4CA4: mov byte ptr [rbp + 0x1d], cl
0x001D4CA7: movsx ecx, byte ptr [rbp + 0x1d]
0x001D4CAB: xor ecx, 0x3b
0x001D4CAE: mov byte ptr [rbp + 0x1e], cl
0x001D4CB1: movsx ecx, byte ptr [rbp + 0x1e]
0x001D4CB5: xor ecx, 0x38
0x001D4CB8: mov byte ptr [rbp + 0x1f], cl
```

Nearby imports / literal refs:


### slot `0x007E7840` in `0x001D4A80..0x001D5DC9`

```asm
0x001D4E64: cmp rcx, 0x27
0x001D4E68: jbe 0x1401d4e70
0x001D4E6A: call 0x1403db020
0x001D4E6F: int3
0x001D4E70: mov rcx, rax
0x001D4E73: call 0x1403b20d4
0x001D4E78: mov qword ptr [rbp + 0xb8], 0xf
0x001D4E83: mov qword ptr [rbp + 0xb0], rdi
0x001D4E8A: mov byte ptr [rbp + 0xa0], 0
0x001D4E91: mov qword ptr [r15], rdi
0x001D4E94: mov r12d, esi
0x001D4E97: mov qword ptr [r14], 0xffffffffffffffff
0x001D4E9E: mov r10, qword ptr [rsp + 0x60]
0x001D4EA3: lea r14, [rbx + 0xc0]
0x001D4EAA: cmp qword ptr [r15], 0
0x001D4EAE: jne 0x1401d5165
0x001D4EB4: cmp r12d, -1
0x001D4EB8: jne 0x1401d4ec6
0x001D4EBA: mov rax, qword ptr [rip + 0x611547]
0x001D4EC1: mov r12d, dword ptr [r10 + rax + 0x10]
0x001D4EC6: mov rdx, r15
0x001D4EC9: mov ecx, r12d
0x001D4ECC: call qword ptr [rip + 0x61296e]
0x001D4ED2: mov dword ptr [rsp + 0x34], eax
0x001D4ED6: test eax, eax
0x001D4ED8: je 0x1401d5165
0x001D4EDE: mov ecx, eax
0x001D4EE0: call qword ptr [rip + 0x612972]
0x001D4EE6: mov qword ptr [rsp + 0x68], rax
0x001D4EEB: mov dword ptr [rbp + 0x40], 0x39
0x001D4EF2: mov dword ptr [rbp + 0x44], 0x54
0x001D4EF9: mov eax, dword ptr [rbp + 0x44]
0x001D4EFC: xor eax, 3
0x001D4EFF: mov byte ptr [rbp + 0x48], al
0x001D4F02: movsx ecx, byte ptr [rbp + 0x48]
0x001D4F06: xor ecx, 0x19
0x001D4F09: mov byte ptr [rbp + 0x49], cl
0x001D4F0C: movsx ecx, byte ptr [rbp + 0x49]
0x001D4F10: xor ecx, 0x4c
0x001D4F13: mov byte ptr [rbp + 0x4a], cl
0x001D4F16: movsx ecx, byte ptr [rbp + 0x4a]
0x001D4F1A: xor ecx, 0x57
0x001D4F1D: mov byte ptr [rbp + 0x4b], cl
0x001D4F20: movsx ecx, byte ptr [rbp + 0x4b]
0x001D4F24: xor ecx, 0x58
0x001D4F27: mov byte ptr [rbp + 0x4c], cl
0x001D4F2A: movsx ecx, byte ptr [rbp + 0x4c]
0x001D4F2E: xor ecx, 0x5b
0x001D4F31: mov byte ptr [rbp + 0x4d], cl
0x001D4F34: movsx ecx, byte ptr [rbp + 0x4d]
0x001D4F38: xor ecx, 0x55
0x001D4F3B: mov byte ptr [rbp + 0x4e], cl
```

Nearby imports / literal refs:


### slot `0x007E7858` in `0x001D4A80..0x001D5DC9`

```asm
0x001D4E73: call 0x1403b20d4
0x001D4E78: mov qword ptr [rbp + 0xb8], 0xf
0x001D4E83: mov qword ptr [rbp + 0xb0], rdi
0x001D4E8A: mov byte ptr [rbp + 0xa0], 0
0x001D4E91: mov qword ptr [r15], rdi
0x001D4E94: mov r12d, esi
0x001D4E97: mov qword ptr [r14], 0xffffffffffffffff
0x001D4E9E: mov r10, qword ptr [rsp + 0x60]
0x001D4EA3: lea r14, [rbx + 0xc0]
0x001D4EAA: cmp qword ptr [r15], 0
0x001D4EAE: jne 0x1401d5165
0x001D4EB4: cmp r12d, -1
0x001D4EB8: jne 0x1401d4ec6
0x001D4EBA: mov rax, qword ptr [rip + 0x611547]
0x001D4EC1: mov r12d, dword ptr [r10 + rax + 0x10]
0x001D4EC6: mov rdx, r15
0x001D4EC9: mov ecx, r12d
0x001D4ECC: call qword ptr [rip + 0x61296e]
0x001D4ED2: mov dword ptr [rsp + 0x34], eax
0x001D4ED6: test eax, eax
0x001D4ED8: je 0x1401d5165
0x001D4EDE: mov ecx, eax
0x001D4EE0: call qword ptr [rip + 0x612972]
0x001D4EE6: mov qword ptr [rsp + 0x68], rax
0x001D4EEB: mov dword ptr [rbp + 0x40], 0x39
0x001D4EF2: mov dword ptr [rbp + 0x44], 0x54
0x001D4EF9: mov eax, dword ptr [rbp + 0x44]
0x001D4EFC: xor eax, 3
0x001D4EFF: mov byte ptr [rbp + 0x48], al
0x001D4F02: movsx ecx, byte ptr [rbp + 0x48]
0x001D4F06: xor ecx, 0x19
0x001D4F09: mov byte ptr [rbp + 0x49], cl
0x001D4F0C: movsx ecx, byte ptr [rbp + 0x49]
0x001D4F10: xor ecx, 0x4c
0x001D4F13: mov byte ptr [rbp + 0x4a], cl
0x001D4F16: movsx ecx, byte ptr [rbp + 0x4a]
0x001D4F1A: xor ecx, 0x57
0x001D4F1D: mov byte ptr [rbp + 0x4b], cl
0x001D4F20: movsx ecx, byte ptr [rbp + 0x4b]
0x001D4F24: xor ecx, 0x58
0x001D4F27: mov byte ptr [rbp + 0x4c], cl
0x001D4F2A: movsx ecx, byte ptr [rbp + 0x4c]
0x001D4F2E: xor ecx, 0x5b
0x001D4F31: mov byte ptr [rbp + 0x4d], cl
0x001D4F34: movsx ecx, byte ptr [rbp + 0x4d]
0x001D4F38: xor ecx, 0x55
0x001D4F3B: mov byte ptr [rbp + 0x4e], cl
0x001D4F3E: movsx ecx, byte ptr [rbp + 0x4e]
0x001D4F42: xor ecx, 0x5c
0x001D4F45: mov byte ptr [rbp + 0x4f], cl
0x001D4F48: movsx ecx, byte ptr [rbp + 0x4f]
0x001D4F4C: xor ecx, 0x19
```

Nearby imports / literal refs:


### slot `0x007E7848` in `0x001D6E40..0x001D6F2A`

```asm
0x001D6E8F: sar rdx, 4
0x001D6E93: mov rax, rdx
0x001D6E96: shr rax, 0x3f
0x001D6E9A: add rdx, rax
0x001D6E9D: je 0x1401d6efc
0x001D6E9F: mov r8, qword ptr [rdi + 0x80]
0x001D6EA6: mov rax, rsi
0x001D6EA9: nop dword ptr [rax]
0x001D6EB0: lea rax, [rax + rax*4]
0x001D6EB4: cmp qword ptr [r9 + rax*8], r8
0x001D6EB8: lea rcx, [r9 + rax*8]
0x001D6EBC: je 0x1401d6ec9
0x001D6EBE: inc ebx
0x001D6EC0: mov eax, ebx
0x001D6EC2: cmp rax, rdx
0x001D6EC5: jb 0x1401d6eb0
0x001D6EC7: jmp 0x1401d6efc
0x001D6EC9: add rcx, 8
0x001D6ECD: cmp qword ptr [rcx + 0x18], 0x10
0x001D6ED2: jb 0x1401d6ed7
0x001D6ED4: mov rcx, qword ptr [rcx]
0x001D6ED7: lea rdx, [rsp + 0x38]
0x001D6EDC: call qword ptr [rip + 0x610966]
0x001D6EE2: test eax, eax
0x001D6EE4: je 0x1401d6ef2
0x001D6EE6: mov qword ptr [rsp + 0x38], rsi
0x001D6EEB: cmp ebx, -1
0x001D6EEE: jne 0x1401d6eff
0x001D6EF0: jmp 0x1401d6efc
0x001D6EF2: mov rcx, qword ptr [rsp + 0x38]
0x001D6EF7: test rcx, rcx
0x001D6EFA: jne 0x1401d6f17
0x001D6EFC: mov ebx, dword ptr [rdi + 0x10]
0x001D6EFF: lea rdx, [rsp + 0x38]
0x001D6F04: mov ecx, ebx
0x001D6F06: call qword ptr [rip + 0x610934]
0x001D6F0C: mov rcx, qword ptr [rsp + 0x38]
0x001D6F11: test eax, eax
0x001D6F13: cmovne rcx, rsi
0x001D6F17: mov rbx, qword ptr [rsp + 0x30]
0x001D6F1C: mov rax, rcx
0x001D6F1F: mov rsi, qword ptr [rsp + 0x40]
0x001D6F24: add rsp, 0x20
0x001D6F28: pop rdi
0x001D6F29: ret
0x001D6F2A: int3
0x001D6F2B: int3
0x001D6F2C: int3
0x001D6F2D: int3
0x001D6F2E: int3
0x001D6F2F: int3
0x001D6F30: mov rax, rsp
```

Nearby imports / literal refs:


### slot `0x007E7840` in `0x001D6E40..0x001D6F2A`

```asm
0x001D6EC0: mov eax, ebx
0x001D6EC2: cmp rax, rdx
0x001D6EC5: jb 0x1401d6eb0
0x001D6EC7: jmp 0x1401d6efc
0x001D6EC9: add rcx, 8
0x001D6ECD: cmp qword ptr [rcx + 0x18], 0x10
0x001D6ED2: jb 0x1401d6ed7
0x001D6ED4: mov rcx, qword ptr [rcx]
0x001D6ED7: lea rdx, [rsp + 0x38]
0x001D6EDC: call qword ptr [rip + 0x610966]
0x001D6EE2: test eax, eax
0x001D6EE4: je 0x1401d6ef2
0x001D6EE6: mov qword ptr [rsp + 0x38], rsi
0x001D6EEB: cmp ebx, -1
0x001D6EEE: jne 0x1401d6eff
0x001D6EF0: jmp 0x1401d6efc
0x001D6EF2: mov rcx, qword ptr [rsp + 0x38]
0x001D6EF7: test rcx, rcx
0x001D6EFA: jne 0x1401d6f17
0x001D6EFC: mov ebx, dword ptr [rdi + 0x10]
0x001D6EFF: lea rdx, [rsp + 0x38]
0x001D6F04: mov ecx, ebx
0x001D6F06: call qword ptr [rip + 0x610934]
0x001D6F0C: mov rcx, qword ptr [rsp + 0x38]
0x001D6F11: test eax, eax
0x001D6F13: cmovne rcx, rsi
0x001D6F17: mov rbx, qword ptr [rsp + 0x30]
0x001D6F1C: mov rax, rcx
0x001D6F1F: mov rsi, qword ptr [rsp + 0x40]
0x001D6F24: add rsp, 0x20
0x001D6F28: pop rdi
0x001D6F29: ret
0x001D6F2A: int3
0x001D6F2B: int3
0x001D6F2C: int3
0x001D6F2D: int3
0x001D6F2E: int3
0x001D6F2F: int3
0x001D6F30: mov rax, rsp
0x001D6F33: push rbp
0x001D6F34: lea rbp, [rax - 0x678]
0x001D6F3B: sub rsp, 0x770
0x001D6F42: mov qword ptr [rsp + 0x30], 0xfffffffffffffffe
0x001D6F4B: mov qword ptr [rax + 0x10], rbx
0x001D6F4F: mov qword ptr [rax + 0x18], rdi
0x001D6F53: mov rax, qword ptr [rip + 0x5ff996]
0x001D6F5A: xor rax, rsp
0x001D6F5D: mov qword ptr [rbp + 0x660], rax
0x001D6F64: mov rdi, rcx
0x001D6F67: cmp byte ptr [rcx + 0xd8], 0
0x001D6F6E: je 0x1401d70e9
0x001D6F74: mov rbx, qword ptr [rcx + 0xd0]
```

Nearby imports / literal refs:


### slot `0x007E7858` in `0x001D6F30..0x001D748E`

```asm
0x001D70CB: mov eax, ebx
0x001D70CD: sub eax, r11d
0x001D70D0: add r8d, dword ptr [rdx]
0x001D70D3: lea rdx, [rdx + 0x34]
0x001D70D7: sub rax, 1
0x001D70DB: jne 0x1401d70d0
0x001D70DD: xor edx, edx
0x001D70DF: mov eax, r8d
0x001D70E2: div ebx
0x001D70E4: jmp 0x1401d746a
0x001D70E9: mov rcx, qword ptr [rdi + 0xc8]
0x001D70F0: test rcx, rcx
0x001D70F3: je 0x1401d7467
0x001D70F9: mov dword ptr [rsp + 0x20], 0xffffffff
0x001D7101: lea rdx, [rsp + 0x20]
0x001D7106: call qword ptr [rip + 0x61075c]
0x001D710C: mov dword ptr [rsp + 0x24], eax
0x001D7110: test eax, eax
0x001D7112: je 0x1401d745e
0x001D7118: cmp eax, 3
0x001D711B: je 0x1401d7467
0x001D7121: mov ecx, eax
0x001D7123: call qword ptr [rip + 0x61072f]
0x001D7129: mov qword ptr [rsp + 0x28], rax
0x001D712E: mov dword ptr [rsp + 0x38], 0x3c
0x001D7136: mov eax, dword ptr [rsp + 0x38]
0x001D713A: add al, 0x3c
0x001D713C: movsx ecx, al
0x001D713F: xor ecx, 0x6c
0x001D7142: mov dword ptr [rsp + 0x3c], ecx
0x001D7146: mov eax, dword ptr [rsp + 0x3c]
0x001D714A: mov ecx, dword ptr [rsp + 0x38]
0x001D714E: xor ecx, eax
0x001D7150: xor ecx, 0x3a
0x001D7153: mov byte ptr [rsp + 0x40], cl
0x001D7157: movsx ecx, byte ptr [rsp + 0x40]
0x001D715C: mov eax, dword ptr [rsp + 0x38]
0x001D7160: inc al
0x001D7162: xor eax, ecx
0x001D7164: xor eax, 0x20
0x001D7167: mov byte ptr [rsp + 0x41], al
0x001D716B: movsx ecx, byte ptr [rsp + 0x41]
0x001D7170: mov eax, dword ptr [rsp + 0x38]
0x001D7174: add al, 2
0x001D7176: xor eax, ecx
0x001D7178: xor eax, 0x75
0x001D717B: mov byte ptr [rsp + 0x42], al
0x001D717F: movsx ecx, byte ptr [rsp + 0x42]
0x001D7184: mov eax, dword ptr [rsp + 0x38]
0x001D7188: add al, 3
0x001D718A: xor eax, ecx
0x001D718C: xor eax, 0x6e
```

Nearby imports / literal refs:


### slot `0x007E7858` in `0x001D9490..0x001D97A5`

```asm
0x001D948E: int3
0x001D948F: int3
0x001D9490: push rbp
0x001D9492: lea rbp, [rsp - 0x57]
0x001D9497: sub rsp, 0xb0
0x001D949E: mov qword ptr [rbp - 0x29], 0xfffffffffffffffe
0x001D94A6: mov qword ptr [rsp + 0xc8], rbx
0x001D94AE: mov rax, qword ptr [rip + 0x5fd43b]
0x001D94B5: xor rax, rsp
0x001D94B8: mov qword ptr [rbp + 0x4f], rax
0x001D94BC: mov rbx, rcx
0x001D94BF: mov rcx, qword ptr [rcx + 0xc8]
0x001D94C6: test rcx, rcx
0x001D94C9: je 0x1401d9785
0x001D94CF: mov dword ptr [rbp - 0x39], 0xffffffff
0x001D94D6: lea r8, [rbp - 0x39]
0x001D94DA: xor edx, edx
0x001D94DC: call qword ptr [rip + 0x60e37e]
0x001D94E2: mov dword ptr [rbp - 0x35], eax
0x001D94E5: test eax, eax
0x001D94E7: je 0x1401d977d
0x001D94ED: mov ecx, eax
0x001D94EF: call qword ptr [rip + 0x60e363]
0x001D94F5: mov qword ptr [rbp - 0x31], rax
0x001D94F9: mov dword ptr [rbp - 0x21], 0x23
0x001D9500: mov dword ptr [rbp - 0x1d], 0x52
0x001D9507: mov eax, dword ptr [rbp - 0x1d]
0x001D950A: xor eax, 0x19
0x001D950D: mov byte ptr [rbp - 0x19], al
0x001D9510: movsx ecx, byte ptr [rbp - 0x19]
0x001D9514: xor ecx, 3
0x001D9517: mov byte ptr [rbp - 0x18], cl
0x001D951A: movsx ecx, byte ptr [rbp - 0x18]
0x001D951E: xor ecx, 0x56
0x001D9521: mov byte ptr [rbp - 0x17], cl
0x001D9524: movsx ecx, byte ptr [rbp - 0x17]
0x001D9528: xor ecx, 0x4d
0x001D952B: mov byte ptr [rbp - 0x16], cl
0x001D952E: movsx ecx, byte ptr [rbp - 0x16]
0x001D9532: xor ecx, 0x42
0x001D9535: mov byte ptr [rbp - 0x15], cl
0x001D9538: movsx ecx, byte ptr [rbp - 0x15]
0x001D953C: xor ecx, 0x41
0x001D953F: mov byte ptr [rbp - 0x14], cl
0x001D9542: movsx ecx, byte ptr [rbp - 0x14]
0x001D9546: xor ecx, 0x4f
0x001D9549: mov byte ptr [rbp - 0x13], cl
0x001D954C: movsx ecx, byte ptr [rbp - 0x13]
0x001D9550: xor ecx, 0x46
0x001D9553: mov byte ptr [rbp - 0x12], cl
0x001D9556: movsx ecx, byte ptr [rbp - 0x12]
0x001D955A: xor ecx, 3
```

Nearby imports / literal refs:


### slot `0x007E7858` in `0x001DC0C0..0x001DE7D3`

```asm
0x001DC2FD: call 0x1403db020
0x001DC302: int3
0x001DC303: cmp rcx, 0x27
0x001DC307: jbe 0x1401dc30f
0x001DC309: call 0x1403db020
0x001DC30E: int3
0x001DC30F: mov rcx, rax
0x001DC312: call 0x1403b20d4
0x001DC317: mov qword ptr [rbp + 0x690], 0xf
0x001DC322: mov qword ptr [rbp + 0x688], rbx
0x001DC329: mov byte ptr [rbp + 0x678], 0
0x001DC330: cmp byte ptr [rip + 0x60a4b9], 0
0x001DC337: jne 0x1401dc80c
0x001DC33D: mov rax, qword ptr [rip + 0x60b4e4]
0x001DC344: test rax, rax
0x001DC347: je 0x1401dc80c
0x001DC34D: xor ecx, ecx
0x001DC34F: call rax
0x001DC351: mov esi, eax
0x001DC353: test eax, eax
0x001DC355: je 0x1401dcdf6
0x001DC35B: mov ecx, eax
0x001DC35D: call qword ptr [rip + 0x60b4f5]
0x001DC363: mov r14, rax
0x001DC366: mov dword ptr [rbp + 0x590], 0x55
0x001DC370: mov dword ptr [rbp + 0x594], 0x5c
0x001DC37A: mov ecx, dword ptr [rbp + 0x594]
0x001DC380: xor ecx, 0x1b
0x001DC383: mov byte ptr [rbp + 0x598], cl
0x001DC389: movsx edx, byte ptr [rbp + 0x598]
0x001DC390: xor edx, 3
0x001DC393: mov byte ptr [rbp + 0x599], dl
0x001DC399: movsx edx, byte ptr [rbp + 0x599]
0x001DC3A0: xor edx, 0x18
0x001DC3A3: mov byte ptr [rbp + 0x59a], dl
0x001DC3A9: movsx ecx, byte ptr [rbp + 0x59a]
0x001DC3B0: xor ecx, 0x19
0x001DC3B3: mov byte ptr [rbp + 0x59b], cl
0x001DC3B9: movsx ecx, byte ptr [rbp + 0x59b]
0x001DC3C0: xor ecx, 0x75
0x001DC3C3: mov byte ptr [rbp + 0x59c], cl
0x001DC3C9: movsx ecx, byte ptr [rbp + 0x59c]
0x001DC3D0: xor ecx, 0x30
0x001DC3D3: mov byte ptr [rbp + 0x59d], cl
0x001DC3D9: movsx ecx, byte ptr [rbp + 0x59d]
0x001DC3E0: xor ecx, 0x27
0x001DC3E3: mov byte ptr [rbp + 0x59e], cl
0x001DC3E9: movsx ecx, byte ptr [rbp + 0x59e]
0x001DC3F0: xor ecx, 0x27
0x001DC3F3: mov byte ptr [rbp + 0x59f], cl
0x001DC3F9: movsx ecx, byte ptr [rbp + 0x59f]
0x001DC400: xor ecx, 0x3a
```

Nearby imports / literal refs:


### slot `0x007E7858` in `0x001DF630..0x001E0B3C`

```asm
0x001DF62F: ret
0x001DF630: mov rax, rsp
0x001DF633: push r13
0x001DF635: push r14
0x001DF637: push r15
0x001DF639: sub rsp, 0xc00
0x001DF640: mov qword ptr [rax - 0xb30], 0xfffffffffffffffe
0x001DF64B: mov qword ptr [rax + 8], rbx
0x001DF64F: mov qword ptr [rax + 0x10], rsi
0x001DF653: mov qword ptr [rax + 0x18], rdi
0x001DF657: mov qword ptr [rax + 0x20], r12
0x001DF65B: mov rax, qword ptr [rip + 0x5f728e]
0x001DF662: xor rax, rsp
0x001DF665: mov qword ptr [rsp + 0xbf0], rax
0x001DF66D: xor r14d, r14d
0x001DF670: mov dword ptr [rsp + 0x24], r14d
0x001DF675: lea rcx, [rsp + 0x24]
0x001DF67A: call qword ptr [rip + 0x6081b8]
0x001DF680: mov ebx, eax
0x001DF682: test eax, eax
0x001DF684: je 0x1401dfd9d
0x001DF68A: mov ecx, eax
0x001DF68C: call qword ptr [rip + 0x6081c6]
0x001DF692: mov rdi, rax
0x001DF695: mov dword ptr [rsp + 0x5c8], 0x1c
0x001DF6A0: mov ecx, dword ptr [rsp + 0x5c8]
0x001DF6A7: xor ecx, 0x4e
0x001DF6AA: add ecx, 7
0x001DF6AD: mov byte ptr [rsp + 0x5cc], cl
0x001DF6B4: movsx edx, byte ptr [rsp + 0x5cc]
0x001DF6BC: xor edx, 0x56
0x001DF6BF: add edx, 7
0x001DF6C2: mov byte ptr [rsp + 0x5cd], dl
0x001DF6C9: movsx ecx, byte ptr [rsp + 0x5cd]
0x001DF6D1: xor ecx, 0x4d
0x001DF6D4: add ecx, 7
0x001DF6D7: mov byte ptr [rsp + 0x5ce], cl
0x001DF6DE: movsx ecx, byte ptr [rsp + 0x5ce]
0x001DF6E6: xor ecx, 0x4c
0x001DF6E9: add ecx, 7
0x001DF6EC: mov byte ptr [rsp + 0x5cf], cl
0x001DF6F3: movsx ecx, byte ptr [rsp + 0x5cf]
0x001DF6FB: xor ecx, 0x20
0x001DF6FE: add ecx, 7
0x001DF701: mov byte ptr [rsp + 0x5d0], cl
0x001DF708: movsx ecx, byte ptr [rsp + 0x5d0]
0x001DF710: xor ecx, 0x65
0x001DF713: add ecx, 7
0x001DF716: mov byte ptr [rsp + 0x5d1], cl
0x001DF71D: movsx ecx, byte ptr [rsp + 0x5d1]
0x001DF725: xor ecx, 0x72
0x001DF728: add ecx, 7
```

Nearby imports / literal refs:


### slot `0x007E7840` in `0x001DF630..0x001E0B3C`

```asm
0x001DFD60: call 0x1403db020
0x001DFD65: int3
0x001DFD66: cmp rcx, 0x27
0x001DFD6A: jbe 0x1401dfd72
0x001DFD6C: call 0x1403db020
0x001DFD71: int3
0x001DFD72: mov rcx, rax
0x001DFD75: call 0x1403b20d4
0x001DFD7A: mov qword ptr [rsp + 0x648], 0xf
0x001DFD86: mov qword ptr [rsp + 0x640], r14
0x001DFD8E: mov byte ptr [rsp + 0x630], 0
0x001DFD96: mov dword ptr [rsp + 0x24], r14d
0x001DFD9B: jmp 0x1401dfdbf
0x001DFD9D: lea rsi, [rip + 0x253f14]
0x001DFDA4: lea r15, [rip + 0x253e65]
0x001DFDAB: movabs r12, 0x6666666666666667
0x001DFDB5: movabs r13, 0x666666666666666
0x001DFDBF: mov edi, r14d
0x001DFDC2: cmp edi, dword ptr [rsp + 0x24]
0x001DFDC6: jae 0x1401e0b0a
0x001DFDCC: lea rdx, [rsp + 0x48]
0x001DFDD1: mov ecx, edi
0x001DFDD3: call qword ptr [rip + 0x607a67]
0x001DFDD9: mov ebx, eax
0x001DFDDB: test eax, eax
0x001DFDDD: je 0x1401e0513
0x001DFDE3: mov ecx, eax
0x001DFDE5: call qword ptr [rip + 0x607a6d]
0x001DFDEB: mov r14, rax
0x001DFDEE: mov dword ptr [rsp + 0x558], 0x66
0x001DFDF9: mov ecx, dword ptr [rsp + 0x558]
0x001DFE00: add cl, 0x66
0x001DFE03: movsx edx, cl
0x001DFE06: xor edx, 0x5c
0x001DFE09: mov dword ptr [rsp + 0x55c], edx
0x001DFE10: mov ecx, dword ptr [rsp + 0x55c]
0x001DFE17: mov edx, dword ptr [rsp + 0x558]
0x001DFE1E: xor edx, ecx
0x001DFE20: xor edx, 0x4e
0x001DFE23: mov byte ptr [rsp + 0x560], dl
0x001DFE2A: movsx ecx, byte ptr [rsp + 0x560]
0x001DFE32: mov eax, dword ptr [rsp + 0x558]
0x001DFE39: inc al
0x001DFE3B: xor eax, ecx
0x001DFE3D: xor eax, 0x56
0x001DFE40: mov byte ptr [rsp + 0x561], al
0x001DFE47: movsx ecx, byte ptr [rsp + 0x561]
0x001DFE4F: mov eax, dword ptr [rsp + 0x558]
0x001DFE56: add al, 2
0x001DFE58: xor eax, ecx
0x001DFE5A: xor eax, 0x4d
0x001DFE5D: mov byte ptr [rsp + 0x562], al
```

Nearby imports / literal refs:

