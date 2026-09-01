# NVIDIA custom timing mode trace

Candidate child fields `+0x258/+0x25C` gate strap/custom-profile application.

| RVA | kind | field | base | instruction |
|---|---|---|---|---|
| `0x001D4B34` | write | `mode_258` | `rbx` | `mov qword ptr [rbx + 0x258], rdi` |
| `0x001D7B43` | read | `mode_258` | `rbx` | `mov r8d, dword ptr [rbx + 0x258]` |
| `0x001D7E01` | read | `mode_258` | `rbx` | `lea r8, [rbx + 0x258]` |
| `0x001D837B` | read | `mode_258` | `rbx` | `mov eax, dword ptr [rbx + 0x258]` |
| `0x001D8B1F` | read | `mode_25c` | `rbx` | `mov edx, dword ptr [rbx + 0x25c]` |
| `0x001D8F06` | read | `mode_25c` | `rbx` | `lea r8, [rbx + 0x25c]` |
| `0x001DA80A` | write | `mode_258` | `rbx` | `mov qword ptr [rbx + 0x258], rdi` |
| `0x001DBAAD` | read | `mode_258` | `rbx` | `cmp dword ptr [rbx + 0x258], edx` |
| `0x001DBAB5` | read | `mode_25c` | `rbx` | `cmp dword ptr [rbx + 0x25c], r8d` |
| `0x001DBADC` | write | `mode_258` | `rbx` | `mov dword ptr [rbx + 0x258], edx` |
| `0x001DBAE2` | write | `mode_25c` | `rbx` | `mov dword ptr [rbx + 0x25c], r8d` |
| `0x001DBB09` | write | `mode_258` | `rbx` | `mov dword ptr [rbx + 0x258], edx` |
| `0x001DF206` | read | `mode_258` | `rbx` | `cmp dword ptr [rbx + 0x258], 0` |
| `0x001DF213` | read | `mode_25c` | `rbx` | `cmp dword ptr [rbx + 0x25c], 0` |
| `0x001E1EE2` | read | `mode_258` | `rbp` | `mov rax, qword ptr [rbp + 0x258]` |
| `0x001E567A` | write | `mode_258` | `rbp` | `mov byte ptr [rbp + 0x258], cl` |
| `0x001E5680` | read | `mode_258` | `rbp` | `movsx ecx, byte ptr [rbp + 0x258]` |
| `0x001E56BA` | write | `mode_25c` | `rbp` | `mov byte ptr [rbp + 0x25c], cl` |
| `0x001E56C0` | read | `mode_25c` | `rbp` | `movsx ecx, byte ptr [rbp + 0x25c]` |
| `0x001E7C9D` | write | `mode_258` | `rbp` | `mov byte ptr [rbp + 0x258], al` |
| `0x001E7CA3` | read | `mode_258` | `rbp` | `movsx ecx, byte ptr [rbp + 0x258]` |
| `0x001E7D05` | write | `mode_25c` | `rbp` | `mov byte ptr [rbp + 0x25c], al` |
| `0x001E7D0B` | read | `mode_25c` | `rbp` | `movsx ecx, byte ptr [rbp + 0x25c]` |
| `0x001ECC00` | read | `mode_258` | `rbx` | `cmp dword ptr [rbx + 0x258], 0` |
| `0x001ECC09` | read | `mode_25c` | `rbx` | `cmp dword ptr [rbx + 0x25c], 0` |

## Access contexts

### write mode_258 at `0x001D4B34`

```asm
0x001D4AE9: lea r15, [rbx + 0xc8]
0x001D4AF0: mov qword ptr [r15], rdi
0x001D4AF3: mov qword ptr [rbx + 0xd0], rdi
0x001D4AFA: mov byte ptr [rbx + 0xd8], dil
0x001D4B01: mov qword ptr [rbx + 0xdc], rdi
0x001D4B08: mov byte ptr [rbx + 0xe4], dil
0x001D4B0F: lea rcx, [rbx + 0xe8]
0x001D4B16: mov rdx, r13
0x001D4B19: call 0x140408a20
0x001D4B1E: nop
0x001D4B1F: mov qword ptr [rbx + 0x138], 0xffffffffffffffff
0x001D4B2A: mov dword ptr [rbx + 0x140], 0xffffffff
0x001D4B34: mov qword ptr [rbx + 0x258], rdi
0x001D4B3B: mov dword ptr [rbx + 0x260], edi
0x001D4B41: xor eax, eax
0x001D4B43: mov qword ptr [rbx + 0x264], rax
0x001D4B4A: mov byte ptr [rbx + 0x26c], al
0x001D4B50: mov qword ptr [rbx + 0x270], 0xffffffffffffffff
0x001D4B5B: mov qword ptr [rbx + 0x278], rdi
0x001D4B62: mov byte ptr [rbx + 0x280], al
0x001D4B68: mov word ptr [rbx + 0x281], ax
0x001D4B6F: mov byte ptr [rbx + 0x398], al
0x001D4B75: mov word ptr [rbx + 0x399], ax
0x001D4B7C: mov dword ptr [rbx + 0x39c], edi
0x001D4B82: mov qword ptr [rbx + 0x3a0], 0xffffffffffffffff
0x001D4B8D: lea rcx, [rbx + 0x144]
```

### read mode_258 at `0x001D7B43`

```asm
0x001D7B10: cmp esi, eax
0x001D7B12: jb 0x1401d8ff0
0x001D7B18: cmp r14d, r8d
0x001D7B1B: jb 0x1401d8ff0
0x001D7B21: cmp r15d, edx
0x001D7B24: jb 0x1401d8ff0
0x001D7B2A: cmp r12d, ecx
0x001D7B2D: jb 0x1401d8ff0
0x001D7B33: xor edx, edx
0x001D7B35: lea r8d, [rdx + 0x5c]
0x001D7B39: lea rcx, [rsp + 0x70]
0x001D7B3E: call 0x1403d3050
0x001D7B43: mov r8d, dword ptr [rbx + 0x258]
0x001D7B4A: test r8d, r8d
0x001D7B4D: jle 0x1401d84f8
0x001D7B53: lea rdx, [rsp + 0x70]
0x001D7B58: mov rcx, rbx
0x001D7B5B: call 0x1401d78b0
0x001D7B60: test al, al
0x001D7B62: jne 0x1401d7e1d
0x001D7B68: mov dword ptr [rbp + 0x3f0], 0x5f
0x001D7B72: mov eax, dword ptr [rbp + 0x3f0]
0x001D7B78: xor eax, 0x7b
0x001D7B7B: add eax, 2
0x001D7B7E: mov byte ptr [rbp + 0x3f4], al
0x001D7B84: movsx ecx, byte ptr [rbp + 0x3f4]
```

### read mode_258 at `0x001D7E01`

```asm
0x001D7DC8: add ecx, 2
0x001D7DCB: mov byte ptr [rbp + 0x413], cl
0x001D7DD1: mov byte ptr [rbp + 0x414], 0
0x001D7DD8: movzx eax, byte ptr [rbp + 0x3f4]
0x001D7DDF: lea rdx, [rbp + 0x460]
0x001D7DE6: lea rcx, [rbp + 0x3f0]
0x001D7DED: call 0x140206e40
0x001D7DF2: nop
0x001D7DF3: cmp qword ptr [rax + 0x18], 0x10
0x001D7DF8: jb 0x1401d7dfd
0x001D7DFA: mov rax, qword ptr [rax]
0x001D7DFD: lea rdx, [rbx + 8]
0x001D7E01: lea r8, [rbx + 0x258]
0x001D7E08: mov rcx, rax
0x001D7E0B: call 0x14012ee60
0x001D7E10: nop
0x001D7E11: lea rcx, [rbp + 0x460]
0x001D7E18: jmp 0x1401d944a
0x001D7E1D: mov ecx, dword ptr [rsp + 0x78]
0x001D7E21: test ecx, ecx
0x001D7E23: je 0x1401d7e54
0x001D7E25: cmp ecx, esi
0x001D7E27: jae 0x1401d7e54
0x001D7E29: mov eax, esi
0x001D7E2B: sub eax, ecx
0x001D7E2D: imul ecx, eax, 0x64
```

### read mode_258 at `0x001D837B`

```asm
0x001D8343: jb 0x1401d834b
0x001D8345: mov rcx, qword ptr [rbx + 8]
0x001D8349: jmp 0x1401d834f
0x001D834B: lea rcx, [rbx + 8]
0x001D834F: mov qword ptr [rbp + 0x90], rcx
0x001D8356: mov rax, qword ptr [rbx + 0x18]
0x001D835A: mov qword ptr [rbp + 0x98], rax
0x001D8361: mov qword ptr [rbp - 0x30], rcx
0x001D8365: mov qword ptr [rbp - 0x28], rax
0x001D8369: movups xmm0, xmmword ptr [rbp - 0x30]
0x001D836D: movups xmmword ptr [rbp + 0x100], xmm0
0x001D8374: movups xmmword ptr [rbp + 0x750], xmm0
0x001D837B: mov eax, dword ptr [rbx + 0x258]
0x001D8381: mov dword ptr [rbp - 0x30], eax
0x001D8384: movups xmm0, xmmword ptr [rbp - 0x30]
0x001D8388: movups xmmword ptr [rbp - 0x30], xmm0
0x001D838C: movups xmmword ptr [rbp + 0x760], xmm0
0x001D8393: mov dword ptr [rsp + 0x50], esi
0x001D8397: movups xmm0, xmmword ptr [rsp + 0x50]
0x001D839C: movaps xmmword ptr [rbp + 0x770], xmm0
0x001D83A3: mov dword ptr [rsp + 0x50], r15d
0x001D83A8: movups xmm0, xmmword ptr [rsp + 0x50]
0x001D83AD: movaps xmmword ptr [rbp + 0x780], xmm0
0x001D83B4: mov dword ptr [rsp + 0x50], r12d
0x001D83B9: movups xmm0, xmmword ptr [rsp + 0x50]
0x001D83BE: movaps xmmword ptr [rbp + 0x790], xmm0
```

### read mode_25c at `0x001D8B1F`

```asm
0x001D8AE8: mov qword ptr [rsp + 0x20], rsi
0x001D8AED: lea r9, [rbx + 0x264]
0x001D8AF4: lea r8, [rbx + 0x260]
0x001D8AFB: mov rcx, rax
0x001D8AFE: call 0x1401d42c0
0x001D8B03: nop
0x001D8B04: lea rcx, [rbp + 0x4a0]
0x001D8B0B: call 0x140032ef0
0x001D8B10: mov esi, dword ptr [rbp + 0x28]
0x001D8B13: mov ecx, dword ptr [rbp + 0xa8]
0x001D8B19: jmp 0x1401d8b1f
0x001D8B1B: mov ecx, dword ptr [rsp + 0x40]
0x001D8B1F: mov edx, dword ptr [rbx + 0x25c]
0x001D8B25: test edx, edx
0x001D8B27: jle 0x1401d8f22
0x001D8B2D: mov eax, esi
0x001D8B2F: xorps xmm2, xmm2
0x001D8B32: cvtsi2sd xmm2, rax
0x001D8B37: sub esi, ecx
0x001D8B39: mov eax, esi
0x001D8B3B: xorps xmm1, xmm1
0x001D8B3E: cvtsi2sd xmm1, rax
0x001D8B43: movd xmm0, edx
0x001D8B47: cvtdq2pd xmm0, xmm0
0x001D8B4B: divsd xmm0, xmm6
0x001D8B4F: mulsd xmm1, xmm0
```

### read mode_25c at `0x001D8F06`

```asm
0x001D8ECF: mov byte ptr [rbp + 0x398], al
0x001D8ED5: xor eax, eax
0x001D8ED7: mov byte ptr [rbp + 0x399], al
0x001D8EDD: movzx eax, byte ptr [rbp + 0x378]
0x001D8EE4: lea rdx, [rbp + 0x4c0]
0x001D8EEB: lea rcx, [rbp + 0x370]
0x001D8EF2: call 0x1401eb3d0
0x001D8EF7: nop
0x001D8EF8: cmp qword ptr [rax + 0x18], 0x10
0x001D8EFD: jb 0x1401d8f02
0x001D8EFF: mov rax, qword ptr [rax]
0x001D8F02: lea rdx, [rbx + 8]
0x001D8F06: lea r8, [rbx + 0x25c]
0x001D8F0D: mov rcx, rax
0x001D8F10: call 0x14017b170
0x001D8F15: nop
0x001D8F16: lea rcx, [rbp + 0x4c0]
0x001D8F1D: call 0x140032ef0
0x001D8F22: cmp dword ptr [rdi + rbx + 0x144], 0
0x001D8F2A: je 0x1401d8f6e
0x001D8F2C: cmp dword ptr [rbp - 0x4c], 0
0x001D8F30: jne 0x1401d8f3c
0x001D8F32: mov eax, dword ptr [rdi + rbx + 0x188]
0x001D8F39: mov dword ptr [rbp - 0x4c], eax
0x001D8F3C: cmp dword ptr [rbp - 0x58], 0
0x001D8F40: jne 0x1401d8f4c
```

### write mode_258 at `0x001DA80A`

```asm
0x001DA7DE: cmp rax, rdx
0x001DA7E1: jne 0x1401da7d6
0x001DA7E3: or eax, 0xffffffff
0x001DA7E6: jmp 0x1401da7eb
0x001DA7E8: mov eax, dword ptr [rax + 4]
0x001DA7EB: mov dword ptr [rbx + 0x3a0], eax
0x001DA7F1: cmp dword ptr [rbx + 0x3a0], 0
0x001DA7F8: jl 0x1401da869
0x001DA7FA: xor eax, eax
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
```

### read mode_258 at `0x001DBAAD`

```asm
0x001DBA7F: lea r10, [rip + 0x2e1c4a]
0x001DBA86: cmp dword ptr [rax], ecx
0x001DBA88: je 0x1401dba98
0x001DBA8A: add rax, 8
0x001DBA8E: cmp rax, r10
0x001DBA91: jne 0x1401dba86
0x001DBA93: or eax, 0xffffffff
0x001DBA96: jmp 0x1401dba9b
0x001DBA98: mov eax, dword ptr [rax + 4]
0x001DBA9B: mov dword ptr [rbx + 0x3a0], eax
0x001DBAA1: cmp dword ptr [rbx + 0x3a0], esi
0x001DBAA7: jl 0x1401dbb5a
0x001DBAAD: cmp dword ptr [rbx + 0x258], edx
0x001DBAB3: jne 0x1401dbada
0x001DBAB5: cmp dword ptr [rbx + 0x25c], r8d
0x001DBABC: jne 0x1401dbada
0x001DBABE: mov rax, qword ptr [rbx + 0x260]
0x001DBAC5: cmp rax, qword ptr [r9]
0x001DBAC8: jne 0x1401dbada
0x001DBACA: mov eax, dword ptr [rbx + 0x268]
0x001DBAD0: cmp eax, dword ptr [r9 + 8]
0x001DBAD4: jne 0x1401dbada
0x001DBAD6: xor cl, cl
0x001DBAD8: jmp 0x1401dbadc
0x001DBADA: mov cl, 1
0x001DBADC: mov dword ptr [rbx + 0x258], edx
```

### read mode_25c at `0x001DBAB5`

```asm
0x001DBA88: je 0x1401dba98
0x001DBA8A: add rax, 8
0x001DBA8E: cmp rax, r10
0x001DBA91: jne 0x1401dba86
0x001DBA93: or eax, 0xffffffff
0x001DBA96: jmp 0x1401dba9b
0x001DBA98: mov eax, dword ptr [rax + 4]
0x001DBA9B: mov dword ptr [rbx + 0x3a0], eax
0x001DBAA1: cmp dword ptr [rbx + 0x3a0], esi
0x001DBAA7: jl 0x1401dbb5a
0x001DBAAD: cmp dword ptr [rbx + 0x258], edx
0x001DBAB3: jne 0x1401dbada
0x001DBAB5: cmp dword ptr [rbx + 0x25c], r8d
0x001DBABC: jne 0x1401dbada
0x001DBABE: mov rax, qword ptr [rbx + 0x260]
0x001DBAC5: cmp rax, qword ptr [r9]
0x001DBAC8: jne 0x1401dbada
0x001DBACA: mov eax, dword ptr [rbx + 0x268]
0x001DBAD0: cmp eax, dword ptr [r9 + 8]
0x001DBAD4: jne 0x1401dbada
0x001DBAD6: xor cl, cl
0x001DBAD8: jmp 0x1401dbadc
0x001DBADA: mov cl, 1
0x001DBADC: mov dword ptr [rbx + 0x258], edx
0x001DBAE2: mov dword ptr [rbx + 0x25c], r8d
0x001DBAE9: movsd xmm0, qword ptr [r9]
```

### write mode_258 at `0x001DBADC`

```asm
0x001DBAB3: jne 0x1401dbada
0x001DBAB5: cmp dword ptr [rbx + 0x25c], r8d
0x001DBABC: jne 0x1401dbada
0x001DBABE: mov rax, qword ptr [rbx + 0x260]
0x001DBAC5: cmp rax, qword ptr [r9]
0x001DBAC8: jne 0x1401dbada
0x001DBACA: mov eax, dword ptr [rbx + 0x268]
0x001DBAD0: cmp eax, dword ptr [r9 + 8]
0x001DBAD4: jne 0x1401dbada
0x001DBAD6: xor cl, cl
0x001DBAD8: jmp 0x1401dbadc
0x001DBADA: mov cl, 1
0x001DBADC: mov dword ptr [rbx + 0x258], edx
0x001DBAE2: mov dword ptr [rbx + 0x25c], r8d
0x001DBAE9: movsd xmm0, qword ptr [r9]
0x001DBAEE: movsd qword ptr [rbx + 0x260], xmm0
0x001DBAF6: mov eax, dword ptr [r9 + 8]
0x001DBAFA: mov dword ptr [rbx + 0x268], eax
0x001DBB00: lea eax, [rdx - 8]
0x001DBB03: cmp eax, 1
0x001DBB06: cmovbe edx, esi
0x001DBB09: mov dword ptr [rbx + 0x258], edx
0x001DBB0F: test cl, cl
0x001DBB11: je 0x1401dbb50
0x001DBB13: lea rax, [rbx + 0x398]
0x001DBB1A: lea rcx, [rax + 3]
```

### write mode_25c at `0x001DBAE2`

```asm
0x001DBAB5: cmp dword ptr [rbx + 0x25c], r8d
0x001DBABC: jne 0x1401dbada
0x001DBABE: mov rax, qword ptr [rbx + 0x260]
0x001DBAC5: cmp rax, qword ptr [r9]
0x001DBAC8: jne 0x1401dbada
0x001DBACA: mov eax, dword ptr [rbx + 0x268]
0x001DBAD0: cmp eax, dword ptr [r9 + 8]
0x001DBAD4: jne 0x1401dbada
0x001DBAD6: xor cl, cl
0x001DBAD8: jmp 0x1401dbadc
0x001DBADA: mov cl, 1
0x001DBADC: mov dword ptr [rbx + 0x258], edx
0x001DBAE2: mov dword ptr [rbx + 0x25c], r8d
0x001DBAE9: movsd xmm0, qword ptr [r9]
0x001DBAEE: movsd qword ptr [rbx + 0x260], xmm0
0x001DBAF6: mov eax, dword ptr [r9 + 8]
0x001DBAFA: mov dword ptr [rbx + 0x268], eax
0x001DBB00: lea eax, [rdx - 8]
0x001DBB03: cmp eax, 1
0x001DBB06: cmovbe edx, esi
0x001DBB09: mov dword ptr [rbx + 0x258], edx
0x001DBB0F: test cl, cl
0x001DBB11: je 0x1401dbb50
0x001DBB13: lea rax, [rbx + 0x398]
0x001DBB1A: lea rcx, [rax + 3]
0x001DBB1E: mov edx, 3
```

### write mode_258 at `0x001DBB09`

```asm
0x001DBAD6: xor cl, cl
0x001DBAD8: jmp 0x1401dbadc
0x001DBADA: mov cl, 1
0x001DBADC: mov dword ptr [rbx + 0x258], edx
0x001DBAE2: mov dword ptr [rbx + 0x25c], r8d
0x001DBAE9: movsd xmm0, qword ptr [r9]
0x001DBAEE: movsd qword ptr [rbx + 0x260], xmm0
0x001DBAF6: mov eax, dword ptr [r9 + 8]
0x001DBAFA: mov dword ptr [rbx + 0x268], eax
0x001DBB00: lea eax, [rdx - 8]
0x001DBB03: cmp eax, 1
0x001DBB06: cmovbe edx, esi
0x001DBB09: mov dword ptr [rbx + 0x258], edx
0x001DBB0F: test cl, cl
0x001DBB11: je 0x1401dbb50
0x001DBB13: lea rax, [rbx + 0x398]
0x001DBB1A: lea rcx, [rax + 3]
0x001DBB1E: mov edx, 3
0x001DBB23: cmp rax, rcx
0x001DBB26: cmova rdx, rsi
0x001DBB2A: ja 0x1401dbb50
0x001DBB2C: mov r8, rax
0x001DBB2F: neg r8
0x001DBB32: nop dword ptr [rax]
0x001DBB36: nop word ptr [rax + rax]
0x001DBB40: mov byte ptr [rax], sil
```

### read mode_258 at `0x001DF206`

```asm
0x001DF1D6: movaps xmm1, xmmword ptr [rbp + 0x10]
0x001DF1DA: movups xmmword ptr [rsi + 0x10], xmm1
0x001DF1DE: movaps xmm0, xmmword ptr [rbp + 0x20]
0x001DF1E2: movups xmmword ptr [rsi + 0x20], xmm0
0x001DF1E6: movaps xmm1, xmmword ptr [rbp + 0x30]
0x001DF1EA: movups xmmword ptr [rsi + 0x30], xmm1
0x001DF1EE: movaps xmm0, xmmword ptr [rbp + 0x40]
0x001DF1F2: movups xmmword ptr [rsi + 0x40], xmm0
0x001DF1F6: movsd xmm1, qword ptr [rbp + 0x50]
0x001DF1FB: movsd qword ptr [rsi + 0x50], xmm1
0x001DF200: mov eax, dword ptr [rbp + 0x58]
0x001DF203: mov dword ptr [rsi + 0x58], eax
0x001DF206: cmp dword ptr [rbx + 0x258], 0
0x001DF20D: jne 0x1401df413
0x001DF213: cmp dword ptr [rbx + 0x25c], 0
0x001DF21A: jne 0x1401df413
0x001DF220: mov rcx, rbx
0x001DF223: call 0x1401d97e0
0x001DF228: test al, al
0x001DF22A: jne 0x1401df413
0x001DF230: cmp dword ptr [rsi], 0
0x001DF233: je 0x1401df608
0x001DF239: mov r9d, edi
0x001DF23C: mov r8, rsi
0x001DF23F: lea rdx, [rbp]
0x001DF243: mov rcx, rbx
```

### read mode_25c at `0x001DF213`

```asm
0x001DF1DE: movaps xmm0, xmmword ptr [rbp + 0x20]
0x001DF1E2: movups xmmword ptr [rsi + 0x20], xmm0
0x001DF1E6: movaps xmm1, xmmword ptr [rbp + 0x30]
0x001DF1EA: movups xmmword ptr [rsi + 0x30], xmm1
0x001DF1EE: movaps xmm0, xmmword ptr [rbp + 0x40]
0x001DF1F2: movups xmmword ptr [rsi + 0x40], xmm0
0x001DF1F6: movsd xmm1, qword ptr [rbp + 0x50]
0x001DF1FB: movsd qword ptr [rsi + 0x50], xmm1
0x001DF200: mov eax, dword ptr [rbp + 0x58]
0x001DF203: mov dword ptr [rsi + 0x58], eax
0x001DF206: cmp dword ptr [rbx + 0x258], 0
0x001DF20D: jne 0x1401df413
0x001DF213: cmp dword ptr [rbx + 0x25c], 0
0x001DF21A: jne 0x1401df413
0x001DF220: mov rcx, rbx
0x001DF223: call 0x1401d97e0
0x001DF228: test al, al
0x001DF22A: jne 0x1401df413
0x001DF230: cmp dword ptr [rsi], 0
0x001DF233: je 0x1401df608
0x001DF239: mov r9d, edi
0x001DF23C: mov r8, rsi
0x001DF23F: lea rdx, [rbp]
0x001DF243: mov rcx, rbx
0x001DF246: call 0x1401ecb90
0x001DF24B: test al, al
```

### read mode_258 at `0x001E1EE2`

```asm
0x001E1EAD: lea rax, [rbp - 0x78]
0x001E1EB1: mov qword ptr [rbp - 0x80], rax
0x001E1EB5: mov qword ptr [rsp + 0x78], rsi
0x001E1EBA: lea rdx, [rbp + 0x2b0]
0x001E1EC1: lea rcx, [rbp - 0x78]
0x001E1EC5: call 0x1400328e0
0x001E1ECA: lea rcx, [rsp + 0x78]
0x001E1ECF: call 0x14004b060
0x001E1ED4: nop
0x001E1ED5: lea rcx, [rbp + 0x2b0]
0x001E1EDC: call 0x140032dc0
0x001E1EE1: nop
0x001E1EE2: mov rax, qword ptr [rbp + 0x258]
0x001E1EE9: cmp rax, 0x10
0x001E1EED: jb 0x1401e1f3e
0x001E1EEF: inc rax
0x001E1EF2: mov rcx, qword ptr [rbp + 0x240]
0x001E1EF9: cmp rax, 0x1000
0x001E1EFF: jb 0x1401e1f39
0x001E1F01: test cl, 0x1f
0x001E1F04: je 0x1401e1f0c
0x001E1F06: call 0x1403db020
0x001E1F0B: int3
0x001E1F0C: mov rax, qword ptr [rcx - 8]
0x001E1F10: cmp rax, rcx
0x001E1F13: jb 0x1401e1f1b
```

### write mode_258 at `0x001E567A`

```asm
0x001E563A: mov byte ptr [rbp + 0x254], cl
0x001E5640: movsx ecx, byte ptr [rbp + 0x254]
0x001E5647: xor ecx, 0x41
0x001E564A: mov byte ptr [rbp + 0x255], cl
0x001E5650: movsx ecx, byte ptr [rbp + 0x255]
0x001E5657: xor ecx, 5
0x001E565A: mov byte ptr [rbp + 0x256], cl
0x001E5660: movsx ecx, byte ptr [rbp + 0x256]
0x001E5667: xor ecx, 4
0x001E566A: mov byte ptr [rbp + 0x257], cl
0x001E5670: movsx ecx, byte ptr [rbp + 0x257]
0x001E5677: xor ecx, 0x15
0x001E567A: mov byte ptr [rbp + 0x258], cl
0x001E5680: movsx ecx, byte ptr [rbp + 0x258]
0x001E5687: xor ecx, 4
0x001E568A: mov byte ptr [rbp + 0x259], cl
0x001E5690: movsx ecx, byte ptr [rbp + 0x259]
0x001E5697: xor ecx, 0x13
0x001E569A: mov byte ptr [rbp + 0x25a], cl
0x001E56A0: movsx ecx, byte ptr [rbp + 0x25a]
0x001E56A7: xor ecx, 0xc
0x001E56AA: mov byte ptr [rbp + 0x25b], cl
0x001E56B0: movsx ecx, byte ptr [rbp + 0x25b]
0x001E56B7: xor ecx, 8
0x001E56BA: mov byte ptr [rbp + 0x25c], cl
0x001E56C0: movsx ecx, byte ptr [rbp + 0x25c]
```

### read mode_258 at `0x001E5680`

```asm
0x001E5640: movsx ecx, byte ptr [rbp + 0x254]
0x001E5647: xor ecx, 0x41
0x001E564A: mov byte ptr [rbp + 0x255], cl
0x001E5650: movsx ecx, byte ptr [rbp + 0x255]
0x001E5657: xor ecx, 5
0x001E565A: mov byte ptr [rbp + 0x256], cl
0x001E5660: movsx ecx, byte ptr [rbp + 0x256]
0x001E5667: xor ecx, 4
0x001E566A: mov byte ptr [rbp + 0x257], cl
0x001E5670: movsx ecx, byte ptr [rbp + 0x257]
0x001E5677: xor ecx, 0x15
0x001E567A: mov byte ptr [rbp + 0x258], cl
0x001E5680: movsx ecx, byte ptr [rbp + 0x258]
0x001E5687: xor ecx, 4
0x001E568A: mov byte ptr [rbp + 0x259], cl
0x001E5690: movsx ecx, byte ptr [rbp + 0x259]
0x001E5697: xor ecx, 0x13
0x001E569A: mov byte ptr [rbp + 0x25a], cl
0x001E56A0: movsx ecx, byte ptr [rbp + 0x25a]
0x001E56A7: xor ecx, 0xc
0x001E56AA: mov byte ptr [rbp + 0x25b], cl
0x001E56B0: movsx ecx, byte ptr [rbp + 0x25b]
0x001E56B7: xor ecx, 8
0x001E56BA: mov byte ptr [rbp + 0x25c], cl
0x001E56C0: movsx ecx, byte ptr [rbp + 0x25c]
0x001E56C7: xor ecx, 0xf
```

### write mode_25c at `0x001E56BA`

```asm
0x001E567A: mov byte ptr [rbp + 0x258], cl
0x001E5680: movsx ecx, byte ptr [rbp + 0x258]
0x001E5687: xor ecx, 4
0x001E568A: mov byte ptr [rbp + 0x259], cl
0x001E5690: movsx ecx, byte ptr [rbp + 0x259]
0x001E5697: xor ecx, 0x13
0x001E569A: mov byte ptr [rbp + 0x25a], cl
0x001E56A0: movsx ecx, byte ptr [rbp + 0x25a]
0x001E56A7: xor ecx, 0xc
0x001E56AA: mov byte ptr [rbp + 0x25b], cl
0x001E56B0: movsx ecx, byte ptr [rbp + 0x25b]
0x001E56B7: xor ecx, 8
0x001E56BA: mov byte ptr [rbp + 0x25c], cl
0x001E56C0: movsx ecx, byte ptr [rbp + 0x25c]
0x001E56C7: xor ecx, 0xf
0x001E56CA: mov byte ptr [rbp + 0x25d], cl
0x001E56D0: movsx ecx, byte ptr [rbp + 0x25d]
0x001E56D7: xor ecx, 4
0x001E56DA: mov byte ptr [rbp + 0x25e], cl
0x001E56E0: movsx ecx, byte ptr [rbp + 0x25e]
0x001E56E7: xor ecx, 0x41
0x001E56EA: mov byte ptr [rbp + 0x25f], cl
0x001E56F0: movsx ecx, byte ptr [rbp + 0x25f]
0x001E56F7: xor ecx, 0x15
0x001E56FA: mov byte ptr [rbp + 0x260], cl
0x001E5700: movsx ecx, byte ptr [rbp + 0x260]
```

### read mode_25c at `0x001E56C0`

```asm
0x001E5680: movsx ecx, byte ptr [rbp + 0x258]
0x001E5687: xor ecx, 4
0x001E568A: mov byte ptr [rbp + 0x259], cl
0x001E5690: movsx ecx, byte ptr [rbp + 0x259]
0x001E5697: xor ecx, 0x13
0x001E569A: mov byte ptr [rbp + 0x25a], cl
0x001E56A0: movsx ecx, byte ptr [rbp + 0x25a]
0x001E56A7: xor ecx, 0xc
0x001E56AA: mov byte ptr [rbp + 0x25b], cl
0x001E56B0: movsx ecx, byte ptr [rbp + 0x25b]
0x001E56B7: xor ecx, 8
0x001E56BA: mov byte ptr [rbp + 0x25c], cl
0x001E56C0: movsx ecx, byte ptr [rbp + 0x25c]
0x001E56C7: xor ecx, 0xf
0x001E56CA: mov byte ptr [rbp + 0x25d], cl
0x001E56D0: movsx ecx, byte ptr [rbp + 0x25d]
0x001E56D7: xor ecx, 4
0x001E56DA: mov byte ptr [rbp + 0x25e], cl
0x001E56E0: movsx ecx, byte ptr [rbp + 0x25e]
0x001E56E7: xor ecx, 0x41
0x001E56EA: mov byte ptr [rbp + 0x25f], cl
0x001E56F0: movsx ecx, byte ptr [rbp + 0x25f]
0x001E56F7: xor ecx, 0x15
0x001E56FA: mov byte ptr [rbp + 0x260], cl
0x001E5700: movsx ecx, byte ptr [rbp + 0x260]
0x001E5707: xor ecx, 9
```

### write mode_258 at `0x001E7C9D`

```asm
0x001E7C69: mov byte ptr [rbp + 0x256], al
0x001E7C6F: movsx ecx, byte ptr [rbp + 0x256]
0x001E7C76: mov eax, dword ptr [rbp + 0x248]
0x001E7C7C: add al, 7
0x001E7C7E: xor eax, ecx
0x001E7C80: xor eax, 0x20
0x001E7C83: mov byte ptr [rbp + 0x257], al
0x001E7C89: movsx ecx, byte ptr [rbp + 0x257]
0x001E7C90: mov eax, dword ptr [rbp + 0x248]
0x001E7C96: add al, 8
0x001E7C98: xor eax, ecx
0x001E7C9A: xor eax, 0x6d
0x001E7C9D: mov byte ptr [rbp + 0x258], al
0x001E7CA3: movsx ecx, byte ptr [rbp + 0x258]
0x001E7CAA: mov eax, dword ptr [rbp + 0x248]
0x001E7CB0: add al, 9
0x001E7CB2: xor eax, ecx
0x001E7CB4: xor eax, 0x65
0x001E7CB7: mov byte ptr [rbp + 0x259], al
0x001E7CBD: movsx ecx, byte ptr [rbp + 0x259]
0x001E7CC4: mov eax, dword ptr [rbp + 0x248]
0x001E7CCA: add al, 0xa
0x001E7CCC: xor eax, ecx
0x001E7CCE: xor eax, 0x6d
0x001E7CD1: mov byte ptr [rbp + 0x25a], al
0x001E7CD7: movsx ecx, byte ptr [rbp + 0x25a]
```

### read mode_258 at `0x001E7CA3`

```asm
0x001E7C6F: movsx ecx, byte ptr [rbp + 0x256]
0x001E7C76: mov eax, dword ptr [rbp + 0x248]
0x001E7C7C: add al, 7
0x001E7C7E: xor eax, ecx
0x001E7C80: xor eax, 0x20
0x001E7C83: mov byte ptr [rbp + 0x257], al
0x001E7C89: movsx ecx, byte ptr [rbp + 0x257]
0x001E7C90: mov eax, dword ptr [rbp + 0x248]
0x001E7C96: add al, 8
0x001E7C98: xor eax, ecx
0x001E7C9A: xor eax, 0x6d
0x001E7C9D: mov byte ptr [rbp + 0x258], al
0x001E7CA3: movsx ecx, byte ptr [rbp + 0x258]
0x001E7CAA: mov eax, dword ptr [rbp + 0x248]
0x001E7CB0: add al, 9
0x001E7CB2: xor eax, ecx
0x001E7CB4: xor eax, 0x65
0x001E7CB7: mov byte ptr [rbp + 0x259], al
0x001E7CBD: movsx ecx, byte ptr [rbp + 0x259]
0x001E7CC4: mov eax, dword ptr [rbp + 0x248]
0x001E7CCA: add al, 0xa
0x001E7CCC: xor eax, ecx
0x001E7CCE: xor eax, 0x6d
0x001E7CD1: mov byte ptr [rbp + 0x25a], al
0x001E7CD7: movsx ecx, byte ptr [rbp + 0x25a]
0x001E7CDE: mov eax, dword ptr [rbp + 0x248]
```

### write mode_25c at `0x001E7D05`

```asm
0x001E7CD1: mov byte ptr [rbp + 0x25a], al
0x001E7CD7: movsx ecx, byte ptr [rbp + 0x25a]
0x001E7CDE: mov eax, dword ptr [rbp + 0x248]
0x001E7CE4: add al, 0xb
0x001E7CE6: xor eax, ecx
0x001E7CE8: xor eax, 0x6f
0x001E7CEB: mov byte ptr [rbp + 0x25b], al
0x001E7CF1: movsx ecx, byte ptr [rbp + 0x25b]
0x001E7CF8: mov eax, dword ptr [rbp + 0x248]
0x001E7CFE: add al, 0xc
0x001E7D00: xor eax, ecx
0x001E7D02: xor eax, 0x72
0x001E7D05: mov byte ptr [rbp + 0x25c], al
0x001E7D0B: movsx ecx, byte ptr [rbp + 0x25c]
0x001E7D12: mov eax, dword ptr [rbp + 0x248]
0x001E7D18: add al, 0xd
0x001E7D1A: xor eax, ecx
0x001E7D1C: xor eax, 0x79
0x001E7D1F: mov byte ptr [rbp + 0x25d], al
0x001E7D25: movsx ecx, byte ptr [rbp + 0x25d]
0x001E7D2C: mov eax, dword ptr [rbp + 0x248]
0x001E7D32: add al, 0xe
0x001E7D34: xor eax, ecx
0x001E7D36: xor eax, 0x20
0x001E7D39: mov byte ptr [rbp + 0x25e], al
0x001E7D3F: movsx ecx, byte ptr [rbp + 0x25e]
```

### read mode_25c at `0x001E7D0B`

```asm
0x001E7CD7: movsx ecx, byte ptr [rbp + 0x25a]
0x001E7CDE: mov eax, dword ptr [rbp + 0x248]
0x001E7CE4: add al, 0xb
0x001E7CE6: xor eax, ecx
0x001E7CE8: xor eax, 0x6f
0x001E7CEB: mov byte ptr [rbp + 0x25b], al
0x001E7CF1: movsx ecx, byte ptr [rbp + 0x25b]
0x001E7CF8: mov eax, dword ptr [rbp + 0x248]
0x001E7CFE: add al, 0xc
0x001E7D00: xor eax, ecx
0x001E7D02: xor eax, 0x72
0x001E7D05: mov byte ptr [rbp + 0x25c], al
0x001E7D0B: movsx ecx, byte ptr [rbp + 0x25c]
0x001E7D12: mov eax, dword ptr [rbp + 0x248]
0x001E7D18: add al, 0xd
0x001E7D1A: xor eax, ecx
0x001E7D1C: xor eax, 0x79
0x001E7D1F: mov byte ptr [rbp + 0x25d], al
0x001E7D25: movsx ecx, byte ptr [rbp + 0x25d]
0x001E7D2C: mov eax, dword ptr [rbp + 0x248]
0x001E7D32: add al, 0xe
0x001E7D34: xor eax, ecx
0x001E7D36: xor eax, 0x20
0x001E7D39: mov byte ptr [rbp + 0x25e], al
0x001E7D3F: movsx ecx, byte ptr [rbp + 0x25e]
0x001E7D46: mov eax, dword ptr [rbp + 0x248]
```

### read mode_258 at `0x001ECC00`

```asm
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
```

### read mode_25c at `0x001ECC09`

```asm
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
```


## Profile-builder custom branch 0x1D8AE0..0x1D8F40

```asm
0x001D8AE0: add ecx, dword ptr [rax - 0x75]
0x001D8AE3: add byte ptr [rax - 0x73], cl
0x001D8AE6: push rbx
0x001D8AE7: or byte ptr [rax - 0x77], cl
0x001D8AEA: je 0x1401d8b10
0x001D8AEC: and byte ptr [rbp + rcx*4 - 0x75], cl
0x001D8AF0: add al, byte ptr fs:[rax]
0x001D8AF3: add byte ptr [rbp + rcx*4 - 0x7d], cl
0x001D8AF7: .byte 0x60
0x001D8AF8: add al, byte ptr [rax]
0x001D8AFA: add byte ptr [rax - 0x75], cl
0x001D8AFD: enter -0x4218, -0x49
0x001D8B01: .byte 0xff
0x001D8B02: call qword ptr [rax - 0x5f7272b8]
0x001D8B08: add al, 0
0x001D8B0A: add al, ch
0x001D8B0C: loopne 0x1401d8ab1
0x001D8B0E: in eax, 0xff
0x001D8B10: mov esi, dword ptr [rbp + 0x28]
0x001D8B13: mov ecx, dword ptr [rbp + 0xa8]
0x001D8B19: jmp 0x1401d8b1f
0x001D8B1B: mov ecx, dword ptr [rsp + 0x40]
0x001D8B1F: mov edx, dword ptr [rbx + 0x25c]
0x001D8B25: test edx, edx
0x001D8B27: jle 0x1401d8f22
0x001D8B2D: mov eax, esi
0x001D8B2F: xorps xmm2, xmm2
0x001D8B32: cvtsi2sd xmm2, rax
0x001D8B37: sub esi, ecx
0x001D8B39: mov eax, esi
0x001D8B3B: xorps xmm1, xmm1
0x001D8B3E: cvtsi2sd xmm1, rax
0x001D8B43: movd xmm0, edx
0x001D8B47: cvtdq2pd xmm0, xmm0
0x001D8B4B: divsd xmm0, xmm6
0x001D8B4F: mulsd xmm1, xmm0
0x001D8B53: subsd xmm2, xmm1
0x001D8B57: cvttsd2si rax, xmm2
0x001D8B5C: mov dword ptr [rsp + 0x78], eax
0x001D8B60: mov dword ptr [rbp + 0x370], 0x50
0x001D8B6A: mov eax, dword ptr [rbp + 0x370]
0x001D8B70: add al, 0x50
0x001D8B72: movsx ecx, al
0x001D8B75: xor ecx, 0x46
0x001D8B78: mov dword ptr [rbp + 0x374], ecx
0x001D8B7E: mov eax, dword ptr [rbp + 0x374]
0x001D8B84: mov ecx, dword ptr [rbp + 0x370]
0x001D8B8A: xor ecx, eax
0x001D8B8C: xor ecx, 0x7b
0x001D8B8F: mov byte ptr [rbp + 0x378], cl
0x001D8B95: movsx ecx, byte ptr [rbp + 0x378]
0x001D8B9C: mov eax, dword ptr [rbp + 0x370]
0x001D8BA2: inc al
0x001D8BA4: xor eax, ecx
0x001D8BA6: xor eax, 0x7d
0x001D8BA9: mov byte ptr [rbp + 0x379], al
0x001D8BAF: movsx ecx, byte ptr [rbp + 0x379]
0x001D8BB6: mov eax, dword ptr [rbp + 0x370]
0x001D8BBC: add al, 2
0x001D8BBE: xor eax, ecx
0x001D8BC0: xor eax, 0x3a
0x001D8BC3: mov byte ptr [rbp + 0x37a], al
0x001D8BC9: movsx ecx, byte ptr [rbp + 0x37a]
0x001D8BD0: mov eax, dword ptr [rbp + 0x370]
0x001D8BD6: add al, 3
0x001D8BD8: xor eax, ecx
0x001D8BDA: xor eax, 0x20
0x001D8BDD: mov byte ptr [rbp + 0x37b], al
0x001D8BE3: movsx ecx, byte ptr [rbp + 0x37b]
0x001D8BEA: mov eax, dword ptr [rbp + 0x370]
0x001D8BF0: add al, 4
0x001D8BF2: xor eax, ecx
0x001D8BF4: xor eax, 0x73
0x001D8BF7: mov byte ptr [rbp + 0x37c], al
0x001D8BFD: movsx ecx, byte ptr [rbp + 0x37c]
0x001D8C04: mov eax, dword ptr [rbp + 0x370]
0x001D8C0A: add al, 5
0x001D8C0C: xor eax, ecx
0x001D8C0E: xor eax, 0x65
0x001D8C11: mov byte ptr [rbp + 0x37d], al
0x001D8C17: movsx ecx, byte ptr [rbp + 0x37d]
0x001D8C1E: mov eax, dword ptr [rbp + 0x370]
0x001D8C24: add al, 6
0x001D8C26: xor eax, ecx
0x001D8C28: xor eax, 0x74
0x001D8C2B: mov byte ptr [rbp + 0x37e], al
0x001D8C31: movsx ecx, byte ptr [rbp + 0x37e]
0x001D8C38: mov eax, dword ptr [rbp + 0x370]
0x001D8C3E: add al, 7
0x001D8C40: xor eax, ecx
0x001D8C42: xor eax, 0x20
0x001D8C45: mov byte ptr [rbp + 0x37f], al
0x001D8C4B: movsx ecx, byte ptr [rbp + 0x37f]
0x001D8C52: mov eax, dword ptr [rbp + 0x370]
0x001D8C58: add al, 8
0x001D8C5A: xor eax, ecx
0x001D8C5C: xor eax, 0x56
0x001D8C5F: mov byte ptr [rbp + 0x380], al
0x001D8C65: movsx ecx, byte ptr [rbp + 0x380]
0x001D8C6C: mov eax, dword ptr [rbp + 0x370]
0x001D8C72: add al, 9
0x001D8C74: xor eax, ecx
0x001D8C76: xor eax, 0x52
0x001D8C79: mov byte ptr [rbp + 0x381], al
0x001D8C7F: movsx ecx, byte ptr [rbp + 0x381]
0x001D8C86: mov eax, dword ptr [rbp + 0x370]
0x001D8C8C: add al, 0xa
0x001D8C8E: xor eax, ecx
0x001D8C90: xor eax, 0x41
0x001D8C93: mov byte ptr [rbp + 0x382], al
0x001D8C99: movsx ecx, byte ptr [rbp + 0x382]
0x001D8CA0: mov eax, dword ptr [rbp + 0x370]
0x001D8CA6: add al, 0xb
0x001D8CA8: xor eax, ecx
0x001D8CAA: xor eax, 0x4d
0x001D8CAD: mov byte ptr [rbp + 0x383], al
0x001D8CB3: movsx ecx, byte ptr [rbp + 0x383]
0x001D8CBA: mov eax, dword ptr [rbp + 0x370]
0x001D8CC0: add al, 0xc
0x001D8CC2: xor eax, ecx
0x001D8CC4: xor eax, 0x20
0x001D8CC7: mov byte ptr [rbp + 0x384], al
0x001D8CCD: movsx ecx, byte ptr [rbp + 0x384]
0x001D8CD4: mov eax, dword ptr [rbp + 0x370]
0x001D8CDA: add al, 0xd
0x001D8CDC: xor eax, ecx
0x001D8CDE: xor eax, 0x72
0x001D8CE1: mov byte ptr [rbp + 0x385], al
0x001D8CE7: movsx ecx, byte ptr [rbp + 0x385]
0x001D8CEE: mov eax, dword ptr [rbp + 0x370]
0x001D8CF4: add al, 0xe
0x001D8CF6: xor eax, ecx
0x001D8CF8: xor eax, 0x65
0x001D8CFB: mov byte ptr [rbp + 0x386], al
0x001D8D01: movsx ecx, byte ptr [rbp + 0x386]
0x001D8D08: mov eax, dword ptr [rbp + 0x370]
0x001D8D0E: add al, 0xf
0x001D8D10: xor eax, ecx
0x001D8D12: xor eax, 0x66
0x001D8D15: mov byte ptr [rbp + 0x387], al
0x001D8D1B: movsx ecx, byte ptr [rbp + 0x387]
0x001D8D22: mov eax, dword ptr [rbp + 0x370]
0x001D8D28: add al, 0x10
0x001D8D2A: xor eax, ecx
0x001D8D2C: xor eax, 0x72
0x001D8D2F: mov byte ptr [rbp + 0x388], al
0x001D8D35: movsx ecx, byte ptr [rbp + 0x388]
0x001D8D3C: mov eax, dword ptr [rbp + 0x370]
0x001D8D42: add al, 0x11
0x001D8D44: xor eax, ecx
0x001D8D46: xor eax, 0x65
0x001D8D49: mov byte ptr [rbp + 0x389], al
0x001D8D4F: movsx ecx, byte ptr [rbp + 0x389]
0x001D8D56: mov eax, dword ptr [rbp + 0x370]
0x001D8D5C: add al, 0x12
0x001D8D5E: xor eax, ecx
0x001D8D60: xor eax, 0x73
0x001D8D63: mov byte ptr [rbp + 0x38a], al
0x001D8D69: movsx ecx, byte ptr [rbp + 0x38a]
0x001D8D70: mov eax, dword ptr [rbp + 0x370]
0x001D8D76: add al, 0x13
0x001D8D78: xor eax, ecx
0x001D8D7A: xor eax, 0x68
0x001D8D7D: mov byte ptr [rbp + 0x38b], al
0x001D8D83: movsx ecx, byte ptr [rbp + 0x38b]
0x001D8D8A: mov eax, dword ptr [rbp + 0x370]
0x001D8D90: add al, 0x14
0x001D8D92: xor eax, ecx
0x001D8D94: xor eax, 0x20
0x001D8D97: mov byte ptr [rbp + 0x38c], al
0x001D8D9D: movsx ecx, byte ptr [rbp + 0x38c]
0x001D8DA4: mov eax, dword ptr [rbp + 0x370]
0x001D8DAA: add al, 0x15
0x001D8DAC: xor eax, ecx
0x001D8DAE: xor eax, 0x72
0x001D8DB1: mov byte ptr [rbp + 0x38d], al
0x001D8DB7: movsx ecx, byte ptr [rbp + 0x38d]
0x001D8DBE: mov eax, dword ptr [rbp + 0x370]
0x001D8DC4: add al, 0x16
0x001D8DC6: xor eax, ecx
0x001D8DC8: xor eax, 0x61
0x001D8DCB: mov byte ptr [rbp + 0x38e], al
0x001D8DD1: movsx ecx, byte ptr [rbp + 0x38e]
0x001D8DD8: mov eax, dword ptr [rbp + 0x370]
0x001D8DDE: add al, 0x17
0x001D8DE0: xor eax, ecx
0x001D8DE2: xor eax, 0x74
0x001D8DE5: mov byte ptr [rbp + 0x38f], al
0x001D8DEB: movsx ecx, byte ptr [rbp + 0x38f]
0x001D8DF2: mov eax, dword ptr [rbp + 0x370]
0x001D8DF8: add al, 0x18
0x001D8DFA: xor eax, ecx
0x001D8DFC: xor eax, 0x65
0x001D8DFF: mov byte ptr [rbp + 0x390], al
0x001D8E05: movsx ecx, byte ptr [rbp + 0x390]
0x001D8E0C: mov eax, dword ptr [rbp + 0x370]
0x001D8E12: add al, 0x19
0x001D8E14: xor eax, ecx
0x001D8E16: xor eax, 0x20
0x001D8E19: mov byte ptr [rbp + 0x391], al
0x001D8E1F: movsx ecx, byte ptr [rbp + 0x391]
0x001D8E26: mov eax, dword ptr [rbp + 0x370]
0x001D8E2C: add al, 0x1a
0x001D8E2E: xor eax, ecx
0x001D8E30: xor eax, 0x2d
0x001D8E33: mov byte ptr [rbp + 0x392], al
0x001D8E39: movsx ecx, byte ptr [rbp + 0x392]
0x001D8E40: mov eax, dword ptr [rbp + 0x370]
0x001D8E46: add al, 0x1b
0x001D8E48: xor eax, ecx
0x001D8E4A: xor eax, 0x76
0x001D8E4D: mov byte ptr [rbp + 0x393], al
0x001D8E53: movsx ecx, byte ptr [rbp + 0x393]
0x001D8E5A: mov eax, dword ptr [rbp + 0x370]
0x001D8E60: add al, 0x1c
0x001D8E62: xor eax, ecx
0x001D8E64: xor eax, 0x6d
0x001D8E67: mov byte ptr [rbp + 0x394], al
0x001D8E6D: movsx ecx, byte ptr [rbp + 0x394]
0x001D8E74: mov eax, dword ptr [rbp + 0x370]
0x001D8E7A: add al, 0x1d
0x001D8E7C: xor eax, ecx
0x001D8E7E: xor eax, 0x72
0x001D8E81: mov byte ptr [rbp + 0x395], al
0x001D8E87: movsx ecx, byte ptr [rbp + 0x395]
0x001D8E8E: mov eax, dword ptr [rbp + 0x370]
0x001D8E94: add al, 0x1e
0x001D8E96: xor eax, ecx
0x001D8E98: xor eax, 0x20
0x001D8E9B: mov byte ptr [rbp + 0x396], al
0x001D8EA1: movsx ecx, byte ptr [rbp + 0x396]
0x001D8EA8: mov eax, dword ptr [rbp + 0x370]
0x001D8EAE: add al, 0x1f
0x001D8EB0: xor eax, ecx
0x001D8EB2: xor eax, 0x7b
0x001D8EB5: mov byte ptr [rbp + 0x397], al
0x001D8EBB: movsx ecx, byte ptr [rbp + 0x397]
0x001D8EC2: mov eax, dword ptr [rbp + 0x370]
0x001D8EC8: add al, 0x20
0x001D8ECA: xor eax, ecx
0x001D8ECC: xor eax, 0x7d
0x001D8ECF: mov byte ptr [rbp + 0x398], al
0x001D8ED5: xor eax, eax
0x001D8ED7: mov byte ptr [rbp + 0x399], al
0x001D8EDD: movzx eax, byte ptr [rbp + 0x378]
0x001D8EE4: lea rdx, [rbp + 0x4c0]
0x001D8EEB: lea rcx, [rbp + 0x370]
0x001D8EF2: call 0x1401eb3d0
0x001D8EF7: nop
0x001D8EF8: cmp qword ptr [rax + 0x18], 0x10
0x001D8EFD: jb 0x1401d8f02
0x001D8EFF: mov rax, qword ptr [rax]
0x001D8F02: lea rdx, [rbx + 8]
0x001D8F06: lea r8, [rbx + 0x25c]
0x001D8F0D: mov rcx, rax
0x001D8F10: call 0x14017b170
0x001D8F15: nop
0x001D8F16: lea rcx, [rbp + 0x4c0]
0x001D8F1D: call 0x140032ef0
0x001D8F22: cmp dword ptr [rdi + rbx + 0x144], 0
0x001D8F2A: je 0x1401d8f6e
0x001D8F2C: cmp dword ptr [rbp - 0x4c], 0
0x001D8F30: jne 0x1401d8f3c
0x001D8F32: mov eax, dword ptr [rdi + rbx + 0x188]
0x001D8F39: mov dword ptr [rbp - 0x4c], eax
0x001D8F3C: cmp dword ptr [rbp - 0x58], 0
```