# VMR profile +0x08 copyout confirmation

`0x1D7930`: R13 = caller output profile pointer. Local working profile is rooted at RSP+0x70; VMR interpolation writes RSP+0x78.

## References to R13 output pointer

| RVA | access | instruction |
|---|---|---|
| `0x001D8F73` | read | `movups xmmword ptr [r13], xmm6` |

```asm
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
0x001D8FA7: mov edx, dword ptr [rbp - 0x38]
0x001D8FAA: mov dword ptr [r13 + 0x58], edx
0x001D8FAE: movsxd rax, dword ptr [rsp + 0x3c]
```

| `0x001D8F7C` | read | `movups xmmword ptr [r13 + 0x10], xmm5` |

```asm
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
0x001D8FA7: mov edx, dword ptr [rbp - 0x38]
0x001D8FAA: mov dword ptr [r13 + 0x58], edx
0x001D8FAE: movsxd rax, dword ptr [rsp + 0x3c]
0x001D8FB3: mov r8, rax
0x001D8FB6: add rax, 7
```

| `0x001D8F85` | read | `movups xmmword ptr [r13 + 0x20], xmm4` |

```asm
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
0x001D8FA7: mov edx, dword ptr [rbp - 0x38]
0x001D8FAA: mov dword ptr [r13 + 0x58], edx
0x001D8FAE: movsxd rax, dword ptr [rsp + 0x3c]
0x001D8FB3: mov r8, rax
0x001D8FB6: add rax, 7
0x001D8FBA: imul rcx, rax, 0x5c
0x001D8FBE: movups xmmword ptr [rcx + rbx], xmm6
```

| `0x001D8F8E` | read | `movups xmmword ptr [r13 + 0x30], xmm3` |

```asm
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
0x001D8FA7: mov edx, dword ptr [rbp - 0x38]
0x001D8FAA: mov dword ptr [r13 + 0x58], edx
0x001D8FAE: movsxd rax, dword ptr [rsp + 0x3c]
0x001D8FB3: mov r8, rax
0x001D8FB6: add rax, 7
0x001D8FBA: imul rcx, rax, 0x5c
0x001D8FBE: movups xmmword ptr [rcx + rbx], xmm6
0x001D8FC2: movups xmmword ptr [rcx + rbx + 0x10], xmm5
0x001D8FC7: movups xmmword ptr [rcx + rbx + 0x20], xmm4
```

| `0x001D8F97` | read | `movups xmmword ptr [r13 + 0x40], xmm2` |

```asm
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
0x001D8FA7: mov edx, dword ptr [rbp - 0x38]
0x001D8FAA: mov dword ptr [r13 + 0x58], edx
0x001D8FAE: movsxd rax, dword ptr [rsp + 0x3c]
0x001D8FB3: mov r8, rax
0x001D8FB6: add rax, 7
0x001D8FBA: imul rcx, rax, 0x5c
0x001D8FBE: movups xmmword ptr [rcx + rbx], xmm6
0x001D8FC2: movups xmmword ptr [rcx + rbx + 0x10], xmm5
0x001D8FC7: movups xmmword ptr [rcx + rbx + 0x20], xmm4
0x001D8FCC: movups xmmword ptr [rcx + rbx + 0x30], xmm3
0x001D8FD1: movups xmmword ptr [rcx + rbx + 0x40], xmm2
```

| `0x001D8FA1` | write | `movsd qword ptr [r13 + 0x50], xmm1` |

```asm
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
0x001D8FA7: mov edx, dword ptr [rbp - 0x38]
0x001D8FAA: mov dword ptr [r13 + 0x58], edx
0x001D8FAE: movsxd rax, dword ptr [rsp + 0x3c]
0x001D8FB3: mov r8, rax
0x001D8FB6: add rax, 7
0x001D8FBA: imul rcx, rax, 0x5c
0x001D8FBE: movups xmmword ptr [rcx + rbx], xmm6
0x001D8FC2: movups xmmword ptr [rcx + rbx + 0x10], xmm5
0x001D8FC7: movups xmmword ptr [rcx + rbx + 0x20], xmm4
0x001D8FCC: movups xmmword ptr [rcx + rbx + 0x30], xmm3
0x001D8FD1: movups xmmword ptr [rcx + rbx + 0x40], xmm2
0x001D8FD6: movsd qword ptr [rcx + rbx + 0x50], xmm1
0x001D8FDC: mov dword ptr [rcx + rbx + 0x58], edx
```

| `0x001D8FAA` | write | `mov dword ptr [r13 + 0x58], edx` |

```asm
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
0x001D8FA7: mov edx, dword ptr [rbp - 0x38]
0x001D8FAA: mov dword ptr [r13 + 0x58], edx
0x001D8FAE: movsxd rax, dword ptr [rsp + 0x3c]
0x001D8FB3: mov r8, rax
0x001D8FB6: add rax, 7
0x001D8FBA: imul rcx, rax, 0x5c
0x001D8FBE: movups xmmword ptr [rcx + rbx], xmm6
0x001D8FC2: movups xmmword ptr [rcx + rbx + 0x10], xmm5
0x001D8FC7: movups xmmword ptr [rcx + rbx + 0x20], xmm4
0x001D8FCC: movups xmmword ptr [rcx + rbx + 0x30], xmm3
0x001D8FD1: movups xmmword ptr [rcx + rbx + 0x40], xmm2
0x001D8FD6: movsd qword ptr [rcx + rbx + 0x50], xmm1
0x001D8FDC: mov dword ptr [rcx + rbx + 0x58], edx
0x001D8FE0: mov byte ptr [rbx + r8 + 0x398], 1
0x001D8FE9: mov al, 1
```


## References to local VMR slot RSP+0x78

| RVA | access | instruction |
|---|---|---|
| `0x001D7E1D` | read | `mov ecx, dword ptr [rsp + 0x78]` |

```asm
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
0x001D7E30: xorps xmm1, xmm1
0x001D7E33: cvtsi2sd xmm1, rcx
0x001D7E38: sub esi, dword ptr [rsp + 0x40]
0x001D7E3C: mov eax, esi
0x001D7E3E: xorps xmm0, xmm0
0x001D7E41: cvtsi2sd xmm0, rax
```

| `0x001D8B5C` | write | `mov dword ptr [rsp + 0x78], eax` |

```asm
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
```

| `0x001D8F5C` | read | `cmp dword ptr [rsp + 0x78], 0` |

```asm
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
0x001D8F93: movaps xmm2, xmmword ptr [rbp - 0x50]
0x001D8F97: movups xmmword ptr [r13 + 0x40], xmm2
```

| `0x001D8F6A` | write | `mov dword ptr [rsp + 0x78], eax` |

```asm
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
0x001D8FA7: mov edx, dword ptr [rbp - 0x38]
```
