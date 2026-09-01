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


## Profile-builder custom branch 0x1D84C0..0x1D88C0

```asm
0x001D84C0: inc dword ptr [rbx + rcx*4 + 0x75]
0x001D84C4: mov r15d, dword ptr fs:[rbp + 0x58]
0x001D84C9: mov r12d, dword ptr [rbp + 0x4c]
0x001D84CD: mov esi, dword ptr [rbp + 0x28]
0x001D84D0: mov eax, dword ptr [rbp + 0xe4]
0x001D84D6: mov dword ptr [rsp + 0x30], eax
0x001D84DA: mov eax, dword ptr [rbp + 0xd8]
0x001D84E0: mov dword ptr [rsp + 0x34], eax
0x001D84E4: mov eax, dword ptr [rbp + 0xcc]
0x001D84EA: mov dword ptr [rsp + 0x38], eax
0x001D84EE: mov eax, dword ptr [rbp + 0xa8]
0x001D84F4: mov dword ptr [rsp + 0x40], eax
0x001D84F8: mov rcx, rbx
0x001D84FB: call 0x1401d97b0
0x001D8500: movsd xmm6, qword ptr [rip + 0x2601b0]
0x001D8508: test al, al
0x001D850A: je 0x1401d8b1b
0x001D8510: mov ecx, dword ptr [rbx + 0x260]
0x001D8516: test ecx, ecx
0x001D8518: jle 0x1401d8551
0x001D851A: mov eax, r14d
0x001D851D: xorps xmm2, xmm2
0x001D8520: cvtsi2sd xmm2, rax
0x001D8525: sub r14d, dword ptr [rsp + 0x30]
0x001D852A: mov eax, r14d
0x001D852D: xorps xmm1, xmm1
0x001D8530: cvtsi2sd xmm1, rax
0x001D8535: movd xmm0, ecx
0x001D8539: cvtdq2pd xmm0, xmm0
0x001D853D: divsd xmm0, xmm6
0x001D8541: mulsd xmm1, xmm0
0x001D8545: subsd xmm2, xmm1
0x001D8549: cvttsd2si rax, xmm2
0x001D854E: mov dword ptr [rbp - 0x4c], eax
0x001D8551: mov ecx, dword ptr [rbx + 0x264]
0x001D8557: test ecx, ecx
0x001D8559: jle 0x1401d8592
0x001D855B: mov eax, r15d
0x001D855E: xorps xmm2, xmm2
0x001D8561: cvtsi2sd xmm2, rax
0x001D8566: sub r15d, dword ptr [rsp + 0x34]
0x001D856B: mov eax, r15d
0x001D856E: xorps xmm1, xmm1
0x001D8571: cvtsi2sd xmm1, rax
0x001D8576: movd xmm0, ecx
0x001D857A: cvtdq2pd xmm0, xmm0
0x001D857E: divsd xmm0, xmm6
0x001D8582: mulsd xmm1, xmm0
0x001D8586: subsd xmm2, xmm1
0x001D858A: cvttsd2si rax, xmm2
0x001D858F: mov dword ptr [rbp - 0x58], eax
0x001D8592: lea rsi, [rbx + 0x268]
0x001D8599: mov ecx, dword ptr [rsi]
0x001D859B: test ecx, ecx
0x001D859D: jle 0x1401d85d6
0x001D859F: mov eax, r12d
0x001D85A2: xorps xmm2, xmm2
0x001D85A5: cvtsi2sd xmm2, rax
0x001D85AA: sub r12d, dword ptr [rsp + 0x38]
0x001D85AF: mov eax, r12d
0x001D85B2: xorps xmm1, xmm1
0x001D85B5: cvtsi2sd xmm1, rax
0x001D85BA: movd xmm0, ecx
0x001D85BE: cvtdq2pd xmm0, xmm0
0x001D85C2: divsd xmm0, xmm6
0x001D85C6: mulsd xmm1, xmm0
0x001D85CA: subsd xmm2, xmm1
0x001D85CE: cvttsd2si rax, xmm2
0x001D85D3: mov dword ptr [rbp - 0x64], eax
0x001D85D6: mov dword ptr [rbp + 0x338], 0x5d
0x001D85E0: mov eax, dword ptr [rbp + 0x338]
0x001D85E6: add al, 0x5d
0x001D85E8: movsx ecx, al
0x001D85EB: xor ecx, 0x72
0x001D85EE: mov dword ptr [rbp + 0x33c], ecx
0x001D85F4: mov eax, dword ptr [rbp + 0x33c]
0x001D85FA: mov ecx, dword ptr [rbp + 0x338]
0x001D8600: xor ecx, eax
0x001D8602: xor ecx, 0x7b
0x001D8605: mov byte ptr [rbp + 0x340], cl
0x001D860B: movsx ecx, byte ptr [rbp + 0x340]
0x001D8612: mov eax, dword ptr [rbp + 0x338]
0x001D8618: inc al
0x001D861A: xor eax, ecx
0x001D861C: xor eax, 0x7d
0x001D861F: mov byte ptr [rbp + 0x341], al
0x001D8625: movsx ecx, byte ptr [rbp + 0x341]
0x001D862C: mov eax, dword ptr [rbp + 0x338]
0x001D8632: add al, 2
0x001D8634: xor eax, ecx
0x001D8636: xor eax, 0x3a
0x001D8639: mov byte ptr [rbp + 0x342], al
0x001D863F: movsx ecx, byte ptr [rbp + 0x342]
0x001D8646: mov eax, dword ptr [rbp + 0x338]
0x001D864C: add al, 3
0x001D864E: xor eax, ecx
0x001D8650: xor eax, 0x20
0x001D8653: mov byte ptr [rbp + 0x343], al
0x001D8659: movsx ecx, byte ptr [rbp + 0x343]
0x001D8660: mov eax, dword ptr [rbp + 0x338]
0x001D8666: add al, 4
0x001D8668: xor eax, ecx
0x001D866A: xor eax, 0x73
0x001D866D: mov byte ptr [rbp + 0x344], al
0x001D8673: movsx ecx, byte ptr [rbp + 0x344]
0x001D867A: mov eax, dword ptr [rbp + 0x338]
0x001D8680: add al, 5
0x001D8682: xor eax, ecx
0x001D8684: xor eax, 0x65
0x001D8687: mov byte ptr [rbp + 0x345], al
0x001D868D: movsx ecx, byte ptr [rbp + 0x345]
0x001D8694: mov eax, dword ptr [rbp + 0x338]
0x001D869A: add al, 6
0x001D869C: xor eax, ecx
0x001D869E: xor eax, 0x74
0x001D86A1: mov byte ptr [rbp + 0x346], al
0x001D86A7: movsx ecx, byte ptr [rbp + 0x346]
0x001D86AE: mov eax, dword ptr [rbp + 0x338]
0x001D86B4: add al, 7
0x001D86B6: xor eax, ecx
0x001D86B8: xor eax, 0x20
0x001D86BB: mov byte ptr [rbp + 0x347], al
0x001D86C1: movsx ecx, byte ptr [rbp + 0x347]
0x001D86C8: mov eax, dword ptr [rbp + 0x338]
0x001D86CE: add al, 8
0x001D86D0: xor eax, ecx
0x001D86D2: xor eax, 0x56
0x001D86D5: mov byte ptr [rbp + 0x348], al
0x001D86DB: movsx ecx, byte ptr [rbp + 0x348]
0x001D86E2: mov eax, dword ptr [rbp + 0x338]
0x001D86E8: add al, 9
0x001D86EA: xor eax, ecx
0x001D86EC: xor eax, 0x52
0x001D86EF: mov byte ptr [rbp + 0x349], al
0x001D86F5: movsx ecx, byte ptr [rbp + 0x349]
0x001D86FC: mov eax, dword ptr [rbp + 0x338]
0x001D8702: add al, 0xa
0x001D8704: xor eax, ecx
0x001D8706: xor eax, 0x41
0x001D8709: mov byte ptr [rbp + 0x34a], al
0x001D870F: movsx ecx, byte ptr [rbp + 0x34a]
0x001D8716: mov eax, dword ptr [rbp + 0x338]
0x001D871C: add al, 0xb
0x001D871E: xor eax, ecx
0x001D8720: xor eax, 0x4d
0x001D8723: mov byte ptr [rbp + 0x34b], al
0x001D8729: movsx ecx, byte ptr [rbp + 0x34b]
0x001D8730: mov eax, dword ptr [rbp + 0x338]
0x001D8736: add al, 0xc
0x001D8738: xor eax, ecx
0x001D873A: xor eax, 0x20
0x001D873D: mov byte ptr [rbp + 0x34c], al
0x001D8743: movsx ecx, byte ptr [rbp + 0x34c]
0x001D874A: mov eax, dword ptr [rbp + 0x338]
0x001D8750: add al, 0xd
0x001D8752: xor eax, ecx
0x001D8754: xor eax, 0x74
0x001D8757: mov byte ptr [rbp + 0x34d], al
0x001D875D: movsx ecx, byte ptr [rbp + 0x34d]
0x001D8764: mov eax, dword ptr [rbp + 0x338]
0x001D876A: add al, 0xe
0x001D876C: xor eax, ecx
0x001D876E: xor eax, 0x69
0x001D8771: mov byte ptr [rbp + 0x34e], al
0x001D8777: movsx ecx, byte ptr [rbp + 0x34e]
0x001D877E: mov eax, dword ptr [rbp + 0x338]
0x001D8784: add al, 0xf
0x001D8786: xor eax, ecx
0x001D8788: xor eax, 0x6d
0x001D878B: mov byte ptr [rbp + 0x34f], al
0x001D8791: movsx ecx, byte ptr [rbp + 0x34f]
0x001D8798: mov eax, dword ptr [rbp + 0x338]
0x001D879E: add al, 0x10
0x001D87A0: xor eax, ecx
0x001D87A2: xor eax, 0x69
0x001D87A5: mov byte ptr [rbp + 0x350], al
0x001D87AB: movsx ecx, byte ptr [rbp + 0x350]
0x001D87B2: mov eax, dword ptr [rbp + 0x338]
0x001D87B8: add al, 0x11
0x001D87BA: xor eax, ecx
0x001D87BC: xor eax, 0x6e
0x001D87BF: mov byte ptr [rbp + 0x351], al
0x001D87C5: movsx ecx, byte ptr [rbp + 0x351]
0x001D87CC: mov eax, dword ptr [rbp + 0x338]
0x001D87D2: add al, 0x12
0x001D87D4: xor eax, ecx
0x001D87D6: xor eax, 0x67
0x001D87D9: mov byte ptr [rbp + 0x352], al
0x001D87DF: movsx ecx, byte ptr [rbp + 0x352]
0x001D87E6: mov eax, dword ptr [rbp + 0x338]
0x001D87EC: add al, 0x13
0x001D87EE: xor eax, ecx
0x001D87F0: xor eax, 0x73
0x001D87F3: mov byte ptr [rbp + 0x353], al
0x001D87F9: movsx ecx, byte ptr [rbp + 0x353]
0x001D8800: mov eax, dword ptr [rbp + 0x338]
0x001D8806: add al, 0x14
0x001D8808: xor eax, ecx
0x001D880A: xor eax, 0x20
0x001D880D: mov byte ptr [rbp + 0x354], al
0x001D8813: movsx ecx, byte ptr [rbp + 0x354]
0x001D881A: mov eax, dword ptr [rbp + 0x338]
0x001D8820: add al, 0x15
0x001D8822: xor eax, ecx
0x001D8824: xor eax, 0x2d
0x001D8827: mov byte ptr [rbp + 0x355], al
0x001D882D: movsx ecx, byte ptr [rbp + 0x355]
0x001D8834: mov eax, dword ptr [rbp + 0x338]
0x001D883A: add al, 0x16
0x001D883C: xor eax, ecx
0x001D883E: xor eax, 0x76
0x001D8841: mov byte ptr [rbp + 0x356], al
0x001D8847: movsx ecx, byte ptr [rbp + 0x356]
0x001D884E: mov eax, dword ptr [rbp + 0x338]
0x001D8854: add al, 0x17
0x001D8856: xor eax, ecx
0x001D8858: xor eax, 0x6d
0x001D885B: mov byte ptr [rbp + 0x357], al
0x001D8861: movsx ecx, byte ptr [rbp + 0x357]
0x001D8868: mov eax, dword ptr [rbp + 0x338]
0x001D886E: add al, 0x18
0x001D8870: xor eax, ecx
0x001D8872: xor eax, 0x74
0x001D8875: mov byte ptr [rbp + 0x358], al
0x001D887B: movsx ecx, byte ptr [rbp + 0x358]
0x001D8882: mov eax, dword ptr [rbp + 0x338]
0x001D8888: add al, 0x19
0x001D888A: xor eax, ecx
0x001D888C: xor eax, 0x31
0x001D888F: mov byte ptr [rbp + 0x359], al
0x001D8895: movsx ecx, byte ptr [rbp + 0x359]
0x001D889C: mov eax, dword ptr [rbp + 0x338]
0x001D88A2: add al, 0x1a
0x001D88A4: xor eax, ecx
0x001D88A6: xor eax, 0x20
0x001D88A9: mov byte ptr [rbp + 0x35a], al
0x001D88AF: movsx ecx, byte ptr [rbp + 0x35a]
0x001D88B6: mov eax, dword ptr [rbp + 0x338]
0x001D88BC: add al, 0x1b
0x001D88BE: xor eax, ecx
```