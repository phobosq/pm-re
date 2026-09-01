# NVIDIA child slot +0x80 entry/signature

Target `0x001DE8B0`; first 0x380 bytes.

## Entry disassembly

```asm
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
0x001DE912: jne 0x1401df608
0x001DE918: mov edi, dword ptr [rsp + 0x20]
0x001DE91C: jmp 0x1401de951
0x001DE91E: mov rcx, qword ptr [rcx + 0xc8]
0x001DE925: test rcx, rcx
0x001DE928: je 0x1401df608
0x001DE92E: mov rax, qword ptr [rip + 0x608f53]
0x001DE935: test rax, rax
0x001DE938: je 0x1401df608
0x001DE93E: lea rdx, [rsp + 0x24]
0x001DE943: call rax
0x001DE945: test eax, eax
0x001DE947: jne 0x1401df608
0x001DE94D: mov edi, dword ptr [rsp + 0x24]
0x001DE951: cmp edi, 0xf
0x001DE954: ja 0x1401df608
0x001DE95A: mov eax, dword ptr [rbx + 0x274]
0x001DE960: cmp edi, eax
0x001DE962: jl 0x1401de968
0x001DE964: test eax, eax
0x001DE966: jns 0x1401de96e
0x001DE968: mov dword ptr [rbx + 0x274], edi
0x001DE96E: movsxd rax, dword ptr [rbx + 0x270]
0x001DE975: xor ecx, ecx
0x001DE977: cmp edi, eax
0x001DE979: je 0x1401de993
0x001DE97B: cmp eax, 2
0x001DE97E: ja 0x1401de987
0x001DE980: mov byte ptr [rax + rbx + 0x280], cl
0x001DE987: mov dword ptr [rbx + 0x278], ecx
0x001DE98D: mov dword ptr [rbx + 0x270], edi
0x001DE993: cmp edi, 2
0x001DE996: jle 0x1401de9a3
0x001DE998: mov dword ptr [rbx + 0x27c], ecx
0x001DE99E: jmp 0x1401df608
0x001DE9A3: test sil, sil
0x001DE9A6: jne 0x1401de998
0x001DE9A8: mov ecx, dword ptr [rbx + 0x27c]
0x001DE9AE: lea eax, [rcx + 1]
0x001DE9B1: mov dword ptr [rbx + 0x27c], eax
0x001DE9B7: cmp ecx, 0x14
0x001DE9BA: jl 0x1401df608
0x001DE9C0: lea rdx, [rbp]
0x001DE9C4: mov rcx, rbx
0x001DE9C7: call 0x1401e0ca0
0x001DE9CC: test al, al
0x001DE9CE: jne 0x1401df1af
0x001DE9D4: mov ecx, dword ptr [rbx + 0x278]
0x001DE9DA: lea eax, [rcx + 1]
0x001DE9DD: mov dword ptr [rbx + 0x278], eax
0x001DE9E3: cmp ecx, 4
0x001DE9E6: jge 0x1401df608
0x001DE9EC: mov dword ptr [rsp + 0x30], 0x61
0x001DE9F4: mov eax, dword ptr [rsp + 0x30]
0x001DE9F8: add al, 0x61
0x001DE9FA: movsx ecx, al
0x001DE9FD: xor ecx, 0x76
0x001DEA00: mov dword ptr [rsp + 0x34], ecx
0x001DEA04: mov eax, dword ptr [rsp + 0x34]
0x001DEA08: mov ecx, dword ptr [rsp + 0x30]
0x001DEA0C: xor ecx, eax
0x001DEA0E: xor ecx, 0x7b
0x001DEA11: mov byte ptr [rsp + 0x38], cl
0x001DEA15: movsx ecx, byte ptr [rsp + 0x38]
0x001DEA1A: mov eax, dword ptr [rsp + 0x30]
0x001DEA1E: inc al
0x001DEA20: xor eax, ecx
0x001DEA22: xor eax, 0x7d
0x001DEA25: mov byte ptr [rsp + 0x39], al
0x001DEA29: movsx ecx, byte ptr [rsp + 0x39]
0x001DEA2E: mov eax, dword ptr [rsp + 0x30]
0x001DEA32: add al, 2
0x001DEA34: xor eax, ecx
0x001DEA36: xor eax, 0x3a
0x001DEA39: mov byte ptr [rsp + 0x3a], al
0x001DEA3D: movsx ecx, byte ptr [rsp + 0x3a]
0x001DEA42: mov eax, dword ptr [rsp + 0x30]
0x001DEA46: add al, 3
0x001DEA48: xor eax, ecx
0x001DEA4A: xor eax, 0x20
0x001DEA4D: mov byte ptr [rsp + 0x3b], al
0x001DEA51: movsx ecx, byte ptr [rsp + 0x3b]
0x001DEA56: mov eax, dword ptr [rsp + 0x30]
0x001DEA5A: add al, 4
0x001DEA5C: xor eax, ecx
0x001DEA5E: xor eax, 0x75
0x001DEA61: mov byte ptr [rsp + 0x3c], al
0x001DEA65: movsx ecx, byte ptr [rsp + 0x3c]
0x001DEA6A: mov eax, dword ptr [rsp + 0x30]
0x001DEA6E: add al, 5
0x001DEA70: xor eax, ecx
0x001DEA72: xor eax, 0x6e
0x001DEA75: mov byte ptr [rsp + 0x3d], al
0x001DEA79: movsx ecx, byte ptr [rsp + 0x3d]
0x001DEA7E: mov eax, dword ptr [rsp + 0x30]
0x001DEA82: add al, 6
0x001DEA84: xor eax, ecx
0x001DEA86: xor eax, 0x61
0x001DEA89: mov byte ptr [rsp + 0x3e], al
0x001DEA8D: movsx ecx, byte ptr [rsp + 0x3e]
0x001DEA92: mov eax, dword ptr [rsp + 0x30]
0x001DEA96: add al, 7
0x001DEA98: xor eax, ecx
0x001DEA9A: xor eax, 0x62
0x001DEA9D: mov byte ptr [rsp + 0x3f], al
0x001DEAA1: movsx ecx, byte ptr [rsp + 0x3f]
0x001DEAA6: mov eax, dword ptr [rsp + 0x30]
0x001DEAAA: add al, 8
0x001DEAAC: xor eax, ecx
0x001DEAAE: xor eax, 0x6c
0x001DEAB1: mov byte ptr [rsp + 0x40], al
0x001DEAB5: movsx ecx, byte ptr [rsp + 0x40]
0x001DEABA: mov eax, dword ptr [rsp + 0x30]
0x001DEABE: add al, 9
0x001DEAC0: xor eax, ecx
0x001DEAC2: xor eax, 0x65
0x001DEAC5: mov byte ptr [rsp + 0x41], al
0x001DEAC9: movsx ecx, byte ptr [rsp + 0x41]
0x001DEACE: mov eax, dword ptr [rsp + 0x30]
0x001DEAD2: add al, 0xa
0x001DEAD4: xor eax, ecx
0x001DEAD6: xor eax, 0x20
0x001DEAD9: mov byte ptr [rsp + 0x42], al
0x001DEADD: movsx ecx, byte ptr [rsp + 0x42]
0x001DEAE2: mov eax, dword ptr [rsp + 0x30]
0x001DEAE6: add al, 0xb
0x001DEAE8: xor eax, ecx
0x001DEAEA: xor eax, 0x74
0x001DEAED: mov byte ptr [rsp + 0x43], al
0x001DEAF1: movsx ecx, byte ptr [rsp + 0x43]
0x001DEAF6: mov eax, dword ptr [rsp + 0x30]
0x001DEAFA: add al, 0xc
0x001DEAFC: xor eax, ecx
0x001DEAFE: xor eax, 0x6f
0x001DEB01: mov byte ptr [rsp + 0x44], al
0x001DEB05: movsx ecx, byte ptr [rsp + 0x44]
0x001DEB0A: mov eax, dword ptr [rsp + 0x30]
0x001DEB0E: add al, 0xd
0x001DEB10: xor eax, ecx
0x001DEB12: xor eax, 0x20
0x001DEB15: mov byte ptr [rsp + 0x45], al
0x001DEB19: movsx ecx, byte ptr [rsp + 0x45]
0x001DEB1E: mov eax, dword ptr [rsp + 0x30]
0x001DEB22: add al, 0xe
0x001DEB24: xor eax, ecx
0x001DEB26: xor eax, 0x73
0x001DEB29: mov byte ptr [rsp + 0x46], al
0x001DEB2D: movsx ecx, byte ptr [rsp + 0x46]
0x001DEB32: mov eax, dword ptr [rsp + 0x30]
0x001DEB36: add al, 0xf
0x001DEB38: xor eax, ecx
0x001DEB3A: xor eax, 0x65
0x001DEB3D: mov byte ptr [rsp + 0x47], al
0x001DEB41: movsx ecx, byte ptr [rsp + 0x47]
0x001DEB46: mov eax, dword ptr [rsp + 0x30]
0x001DEB4A: add al, 0x10
0x001DEB4C: xor eax, ecx
0x001DEB4E: xor eax, 0x74
0x001DEB51: mov byte ptr [rsp + 0x48], al
0x001DEB55: movsx ecx, byte ptr [rsp + 0x48]
0x001DEB5A: mov eax, dword ptr [rsp + 0x30]
0x001DEB5E: add al, 0x11
0x001DEB60: xor eax, ecx
0x001DEB62: xor eax, 0x20
0x001DEB65: mov byte ptr [rsp + 0x49], al
0x001DEB69: movsx ecx, byte ptr [rsp + 0x49]
0x001DEB6E: mov eax, dword ptr [rsp + 0x30]
0x001DEB72: add al, 0x12
0x001DEB74: xor eax, ecx
0x001DEB76: xor eax, 0x73
0x001DEB79: mov byte ptr [rsp + 0x4a], al
0x001DEB7D: movsx ecx, byte ptr [rsp + 0x4a]
0x001DEB82: mov eax, dword ptr [rsp + 0x30]
0x001DEB86: add al, 0x13
0x001DEB88: xor eax, ecx
0x001DEB8A: xor eax, 0x74
0x001DEB8D: mov byte ptr [rsp + 0x4b], al
0x001DEB91: movsx ecx, byte ptr [rsp + 0x4b]
0x001DEB96: mov eax, dword ptr [rsp + 0x30]
0x001DEB9A: add al, 0x14
0x001DEB9C: xor eax, ecx
0x001DEB9E: xor eax, 0x72
0x001DEBA1: mov byte ptr [rsp + 0x4c], al
0x001DEBA5: movsx ecx, byte ptr [rsp + 0x4c]
0x001DEBAA: mov eax, dword ptr [rsp + 0x30]
0x001DEBAE: add al, 0x15
0x001DEBB0: xor eax, ecx
0x001DEBB2: xor eax, 0x61
0x001DEBB5: mov byte ptr [rsp + 0x4d], al
0x001DEBB9: movsx ecx, byte ptr [rsp + 0x4d]
0x001DEBBE: mov eax, dword ptr [rsp + 0x30]
0x001DEBC2: add al, 0x16
0x001DEBC4: xor eax, ecx
0x001DEBC6: xor eax, 0x70
0x001DEBC9: mov byte ptr [rsp + 0x4e], al
0x001DEBCD: movsx ecx, byte ptr [rsp + 0x4e]
0x001DEBD2: mov eax, dword ptr [rsp + 0x30]
0x001DEBD6: add al, 0x17
0x001DEBD8: xor eax, ecx
0x001DEBDA: xor eax, 0x73
0x001DEBDD: mov byte ptr [rsp + 0x4f], al
0x001DEBE1: movsx ecx, byte ptr [rsp + 0x4f]
0x001DEBE6: mov eax, dword ptr [rsp + 0x30]
0x001DEBEA: add al, 0x18
0x001DEBEC: xor eax, ecx
0x001DEBEE: xor eax, 0x3a
0x001DEBF1: mov byte ptr [rsp + 0x50], al
0x001DEBF5: movsx ecx, byte ptr [rsp + 0x50]
0x001DEBFA: mov eax, dword ptr [rsp + 0x30]
0x001DEBFE: add al, 0x19
0x001DEC00: xor eax, ecx
0x001DEC02: xor eax, 0x20
0x001DEC05: mov byte ptr [rsp + 0x51], al
0x001DEC09: movsx ecx, byte ptr [rsp + 0x51]
0x001DEC0E: mov eax, dword ptr [rsp + 0x30]
0x001DEC12: add al, 0x1a
0x001DEC14: xor eax, ecx
0x001DEC16: xor eax, 0x20
0x001DEC19: mov byte ptr [rsp + 0x52], al
0x001DEC1D: movsx ecx, byte ptr [rsp + 0x52]
0x001DEC22: mov eax, dword ptr [rsp + 0x30]
0x001DEC26: add al, 0x1b
0x001DEC28: xor eax, ecx
0x001DEC2A: xor eax, 0x65
```

## Entry-argument references

| RVA | arg register | instruction |
|---|---|---|
| `0x001DE8EB` | `rcx` | `mov rbx, rcx` |
| `0x001DE902` | `rdx` | `lea rdx, [rsp + 0x20]` |
| `0x001DE907` | `rcx` | `mov rcx, qword ptr [rcx + 0xd0]` |
| `0x001DE91E` | `rcx` | `mov rcx, qword ptr [rcx + 0xc8]` |
| `0x001DE925` | `rcx` | `test rcx, rcx` |
| `0x001DE93E` | `rdx` | `lea rdx, [rsp + 0x24]` |
| `0x001DE9AE` | `rcx` | `lea eax, [rcx + 1]` |
| `0x001DE9C0` | `rdx` | `lea rdx, [rbp]` |
| `0x001DE9C4` | `rcx` | `mov rcx, rbx` |
| `0x001DE9DA` | `rcx` | `lea eax, [rcx + 1]` |