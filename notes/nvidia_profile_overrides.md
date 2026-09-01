# NVIDIA profile override fields

Offsets: `+0x14C/+0x170/+0x17C/+0x188` in NVIDIA child region.

| RVA | kind | base/index | field | instruction |
|---|---|---|---|---|
| `0x001D7AB1` | read | `rdi+rbx*1` | `ovr_188` | `mov r9d, dword ptr [rdi + rbx + 0x188]` |
| `0x001D7AC9` | read | `rdi+rbx*1` | `ovr_17c` | `mov r9d, dword ptr [rdi + rbx + 0x17c]` |
| `0x001D7AE1` | read | `rdi+rbx*1` | `ovr_170` | `mov r9d, dword ptr [rdi + rbx + 0x170]` |
| `0x001D7AF9` | read | `rdi+rbx*1` | `ovr_14c` | `mov r9d, dword ptr [rdi + rbx + 0x14c]` |
| `0x001D8F32` | read | `rdi+rbx*1` | `ovr_188` | `mov eax, dword ptr [rdi + rbx + 0x188]` |
| `0x001D8F42` | read | `rdi+rbx*1` | `ovr_17c` | `mov eax, dword ptr [rdi + rbx + 0x17c]` |
| `0x001D8F52` | read | `rdi+rbx*1` | `ovr_170` | `mov eax, dword ptr [rdi + rbx + 0x170]` |
| `0x001D8F63` | read | `rdi+rbx*1` | `ovr_14c` | `mov eax, dword ptr [rdi + rbx + 0x14c]` |

## Contexts

### `read` ovr_188 at `0x001D7AB1`

```asm
0x001D7A78: mov dword ptr [rbp + 0xcc], ecx
0x001D7A7E: mov edx, dword ptr [rdi + 0xc]
0x001D7A81: mov dword ptr [rsp + 0x34], edx
0x001D7A85: mov dword ptr [rbp + 0xd8], edx
0x001D7A8B: mov r8d, dword ptr [rdi + 8]
0x001D7A8F: mov dword ptr [rsp + 0x30], r8d
0x001D7A94: mov dword ptr [rbp + 0xe4], r8d
0x001D7A9B: mov eax, dword ptr [rdi + 0x14]
0x001D7A9E: mov dword ptr [rsp + 0x40], eax
0x001D7AA2: mov dword ptr [rbp + 0xa8], eax
0x001D7AA8: movsxd r10, dword ptr [rsp + 0x3c]
0x001D7AAD: imul rdi, r10, 0x5c
0x001D7AB1: mov r9d, dword ptr [rdi + rbx + 0x188]
0x001D7AB9: test r9d, r9d
0x001D7ABC: je 0x1401d7ac9
0x001D7ABE: cmp r9d, r14d
0x001D7AC1: cmovne r14d, r9d
0x001D7AC5: mov dword ptr [rbp + 0x64], r14d
0x001D7AC9: mov r9d, dword ptr [rdi + rbx + 0x17c]
0x001D7AD1: test r9d, r9d
0x001D7AD4: je 0x1401d7ae1
0x001D7AD6: cmp r9d, r15d
0x001D7AD9: cmovne r15d, r9d
0x001D7ADD: mov dword ptr [rbp + 0x58], r15d
0x001D7AE1: mov r9d, dword ptr [rdi + rbx + 0x170]
0x001D7AE9: test r9d, r9d
```

### `read` ovr_17c at `0x001D7AC9`

```asm
0x001D7A94: mov dword ptr [rbp + 0xe4], r8d
0x001D7A9B: mov eax, dword ptr [rdi + 0x14]
0x001D7A9E: mov dword ptr [rsp + 0x40], eax
0x001D7AA2: mov dword ptr [rbp + 0xa8], eax
0x001D7AA8: movsxd r10, dword ptr [rsp + 0x3c]
0x001D7AAD: imul rdi, r10, 0x5c
0x001D7AB1: mov r9d, dword ptr [rdi + rbx + 0x188]
0x001D7AB9: test r9d, r9d
0x001D7ABC: je 0x1401d7ac9
0x001D7ABE: cmp r9d, r14d
0x001D7AC1: cmovne r14d, r9d
0x001D7AC5: mov dword ptr [rbp + 0x64], r14d
0x001D7AC9: mov r9d, dword ptr [rdi + rbx + 0x17c]
0x001D7AD1: test r9d, r9d
0x001D7AD4: je 0x1401d7ae1
0x001D7AD6: cmp r9d, r15d
0x001D7AD9: cmovne r15d, r9d
0x001D7ADD: mov dword ptr [rbp + 0x58], r15d
0x001D7AE1: mov r9d, dword ptr [rdi + rbx + 0x170]
0x001D7AE9: test r9d, r9d
0x001D7AEC: je 0x1401d7af9
0x001D7AEE: cmp r9d, r12d
0x001D7AF1: cmovne r12d, r9d
0x001D7AF5: mov dword ptr [rbp + 0x4c], r12d
0x001D7AF9: mov r9d, dword ptr [rdi + rbx + 0x14c]
0x001D7B01: test r9d, r9d
```

### `read` ovr_170 at `0x001D7AE1`

```asm
0x001D7AB1: mov r9d, dword ptr [rdi + rbx + 0x188]
0x001D7AB9: test r9d, r9d
0x001D7ABC: je 0x1401d7ac9
0x001D7ABE: cmp r9d, r14d
0x001D7AC1: cmovne r14d, r9d
0x001D7AC5: mov dword ptr [rbp + 0x64], r14d
0x001D7AC9: mov r9d, dword ptr [rdi + rbx + 0x17c]
0x001D7AD1: test r9d, r9d
0x001D7AD4: je 0x1401d7ae1
0x001D7AD6: cmp r9d, r15d
0x001D7AD9: cmovne r15d, r9d
0x001D7ADD: mov dword ptr [rbp + 0x58], r15d
0x001D7AE1: mov r9d, dword ptr [rdi + rbx + 0x170]
0x001D7AE9: test r9d, r9d
0x001D7AEC: je 0x1401d7af9
0x001D7AEE: cmp r9d, r12d
0x001D7AF1: cmovne r12d, r9d
0x001D7AF5: mov dword ptr [rbp + 0x4c], r12d
0x001D7AF9: mov r9d, dword ptr [rdi + rbx + 0x14c]
0x001D7B01: test r9d, r9d
0x001D7B04: je 0x1401d7b10
0x001D7B06: cmp r9d, esi
0x001D7B09: cmovne esi, r9d
0x001D7B0D: mov dword ptr [rbp + 0x28], esi
0x001D7B10: cmp esi, eax
0x001D7B12: jb 0x1401d8ff0
```

### `read` ovr_14c at `0x001D7AF9`

```asm
0x001D7AC9: mov r9d, dword ptr [rdi + rbx + 0x17c]
0x001D7AD1: test r9d, r9d
0x001D7AD4: je 0x1401d7ae1
0x001D7AD6: cmp r9d, r15d
0x001D7AD9: cmovne r15d, r9d
0x001D7ADD: mov dword ptr [rbp + 0x58], r15d
0x001D7AE1: mov r9d, dword ptr [rdi + rbx + 0x170]
0x001D7AE9: test r9d, r9d
0x001D7AEC: je 0x1401d7af9
0x001D7AEE: cmp r9d, r12d
0x001D7AF1: cmovne r12d, r9d
0x001D7AF5: mov dword ptr [rbp + 0x4c], r12d
0x001D7AF9: mov r9d, dword ptr [rdi + rbx + 0x14c]
0x001D7B01: test r9d, r9d
0x001D7B04: je 0x1401d7b10
0x001D7B06: cmp r9d, esi
0x001D7B09: cmovne esi, r9d
0x001D7B0D: mov dword ptr [rbp + 0x28], esi
0x001D7B10: cmp esi, eax
0x001D7B12: jb 0x1401d8ff0
0x001D7B18: cmp r14d, r8d
0x001D7B1B: jb 0x1401d8ff0
0x001D7B21: cmp r15d, edx
0x001D7B24: jb 0x1401d8ff0
0x001D7B2A: cmp r12d, ecx
0x001D7B2D: jb 0x1401d8ff0
```

### `read` ovr_188 at `0x001D8F32`

```asm
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
0x001D8F42: mov eax, dword ptr [rdi + rbx + 0x17c]
0x001D8F49: mov dword ptr [rbp - 0x58], eax
0x001D8F4C: cmp dword ptr [rbp - 0x64], 0
0x001D8F50: jne 0x1401d8f5c
0x001D8F52: mov eax, dword ptr [rdi + rbx + 0x170]
0x001D8F59: mov dword ptr [rbp - 0x64], eax
0x001D8F5C: cmp dword ptr [rsp + 0x78], 0
0x001D8F61: jne 0x1401d8f6e
0x001D8F63: mov eax, dword ptr [rdi + rbx + 0x14c]
0x001D8F6A: mov dword ptr [rsp + 0x78], eax
```

### `read` ovr_17c at `0x001D8F42`

```asm
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
0x001D8F42: mov eax, dword ptr [rdi + rbx + 0x17c]
0x001D8F49: mov dword ptr [rbp - 0x58], eax
0x001D8F4C: cmp dword ptr [rbp - 0x64], 0
0x001D8F50: jne 0x1401d8f5c
0x001D8F52: mov eax, dword ptr [rdi + rbx + 0x170]
0x001D8F59: mov dword ptr [rbp - 0x64], eax
0x001D8F5C: cmp dword ptr [rsp + 0x78], 0
0x001D8F61: jne 0x1401d8f6e
0x001D8F63: mov eax, dword ptr [rdi + rbx + 0x14c]
0x001D8F6A: mov dword ptr [rsp + 0x78], eax
0x001D8F6E: movaps xmm6, xmmword ptr [rsp + 0x70]
0x001D8F73: movups xmmword ptr [r13], xmm6
0x001D8F78: movaps xmm5, xmmword ptr [rbp - 0x80]
0x001D8F7C: movups xmmword ptr [r13 + 0x10], xmm5
```

### `read` ovr_170 at `0x001D8F52`

```asm
0x001D8F22: cmp dword ptr [rdi + rbx + 0x144], 0
0x001D8F2A: je 0x1401d8f6e
0x001D8F2C: cmp dword ptr [rbp - 0x4c], 0
0x001D8F30: jne 0x1401d8f3c
0x001D8F32: mov eax, dword ptr [rdi + rbx + 0x188]
0x001D8F39: mov dword ptr [rbp - 0x4c], eax
0x001D8F3C: cmp dword ptr [rbp - 0x58], 0
0x001D8F40: jne 0x1401d8f4c
0x001D8F42: mov eax, dword ptr [rdi + rbx + 0x17c]
0x001D8F49: mov dword ptr [rbp - 0x58], eax
0x001D8F4C: cmp dword ptr [rbp - 0x64], 0
0x001D8F50: jne 0x1401d8f5c
0x001D8F52: mov eax, dword ptr [rdi + rbx + 0x170]
0x001D8F59: mov dword ptr [rbp - 0x64], eax
0x001D8F5C: cmp dword ptr [rsp + 0x78], 0
0x001D8F61: jne 0x1401d8f6e
0x001D8F63: mov eax, dword ptr [rdi + rbx + 0x14c]
0x001D8F6A: mov dword ptr [rsp + 0x78], eax
0x001D8F6E: movaps xmm6, xmmword ptr [rsp + 0x70]
0x001D8F73: movups xmmword ptr [r13], xmm6
0x001D8F78: movaps xmm5, xmmword ptr [rbp - 0x80]
0x001D8F7C: movups xmmword ptr [r13 + 0x10], xmm5
0x001D8F81: movaps xmm4, xmmword ptr [rbp - 0x70]
0x001D8F85: movups xmmword ptr [r13 + 0x20], xmm4
0x001D8F8A: movaps xmm3, xmmword ptr [rbp - 0x60]
0x001D8F8E: movups xmmword ptr [r13 + 0x30], xmm3
```

### `read` ovr_14c at `0x001D8F63`

```asm
0x001D8F32: mov eax, dword ptr [rdi + rbx + 0x188]
0x001D8F39: mov dword ptr [rbp - 0x4c], eax
0x001D8F3C: cmp dword ptr [rbp - 0x58], 0
0x001D8F40: jne 0x1401d8f4c
0x001D8F42: mov eax, dword ptr [rdi + rbx + 0x17c]
0x001D8F49: mov dword ptr [rbp - 0x58], eax
0x001D8F4C: cmp dword ptr [rbp - 0x64], 0
0x001D8F50: jne 0x1401d8f5c
0x001D8F52: mov eax, dword ptr [rdi + rbx + 0x170]
0x001D8F59: mov dword ptr [rbp - 0x64], eax
0x001D8F5C: cmp dword ptr [rsp + 0x78], 0
0x001D8F61: jne 0x1401d8f6e
0x001D8F63: mov eax, dword ptr [rdi + rbx + 0x14c]
0x001D8F6A: mov dword ptr [rsp + 0x78], eax
0x001D8F6E: movaps xmm6, xmmword ptr [rsp + 0x70]
0x001D8F73: movups xmmword ptr [r13], xmm6
0x001D8F78: movaps xmm5, xmmword ptr [rbp - 0x80]
0x001D8F7C: movups xmmword ptr [r13 + 0x10], xmm5
0x001D8F81: movaps xmm4, xmmword ptr [rbp - 0x70]
0x001D8F85: movups xmmword ptr [r13 + 0x20], xmm4
0x001D8F8A: movaps xmm3, xmmword ptr [rbp - 0x60]
0x001D8F8E: movups xmmword ptr [r13 + 0x30], xmm3
0x001D8F93: movaps xmm2, xmmword ptr [rbp - 0x50]
0x001D8F97: movups xmmword ptr [r13 + 0x40], xmm2
0x001D8F9C: movsd xmm1, qword ptr [rbp - 0x40]
0x001D8FA1: movsd qword ptr [r13 + 0x50], xmm1
```
