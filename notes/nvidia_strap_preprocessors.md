# NVIDIA strap preprocessors 0x1D97E0 / 0x1D7930

Exact-RVA leaf decoding. Called by NVIDIA child vtable slot +0x80 immediately before RegisterOp-backed apply.

## target `0x001D97E0`

### Calls

| RVA | target/form |
|---|---|

### Object/struct accesses

| RVA | base | disp | instruction |
|---|---|---:|---|
| `0x001D97E0` | `rcx` | `0x26C` | `lea rdx, [rcx + 0x26c]` |
| `0x001D97E7` | `rcx` | `0x260` | `lea rax, [rcx + 0x260]` |
| `0x001D97F3` | `rax` | `0x0` | `cmp dword ptr [rax], 0` |

### Full body

```asm
0x001D97E0: lea rdx, [rcx + 0x26c]
0x001D97E7: lea rax, [rcx + 0x260]
0x001D97EE: cmp rax, rdx
0x001D97F1: je 0x1401d9801
0x001D97F3: cmp dword ptr [rax], 0
0x001D97F6: jne 0x1401d9804
0x001D97F8: add rax, 4
0x001D97FC: cmp rax, rdx
0x001D97FF: jne 0x1401d97f3
0x001D9801: xor al, al
0x001D9803: ret
```

## target `0x001D7930`

### Calls

| RVA | target/form |
|---|---|
| `0x001D7A16` | `RVA 0x003D3050` |
| `0x001D7A6C` | `RVA 0x003D3050` |
| `0x001D7B3E` | `RVA 0x003D3050` |
| `0x001D7B5B` | `RVA 0x001D78B0` |
| `0x001D7DED` | `RVA 0x00206E40` |
| `0x001D7E0B` | `RVA 0x0012EE60` |

### Object/struct accesses

| RVA | base | disp | instruction |
|---|---|---:|---|
| `0x001D7957` | `rax` | `0x20` | `mov qword ptr [rax + 0x20], rbx` |
| `0x001D7986` | `rcx` | `0x398` | `cmp byte ptr [rcx + rax + 0x398], 0` |
| `0x001D7998` | `rcx` | `0x0` | `movups xmm0, xmmword ptr [rcx + rbx]` |
| `0x001D799C` | `rdx` | `0x0` | `movups xmmword ptr [rdx], xmm0` |
| `0x001D799F` | `rcx` | `0x10` | `movups xmm1, xmmword ptr [rcx + rbx + 0x10]` |
| `0x001D79A4` | `rdx` | `0x10` | `movups xmmword ptr [rdx + 0x10], xmm1` |
| `0x001D79A8` | `rcx` | `0x20` | `movups xmm0, xmmword ptr [rcx + rbx + 0x20]` |
| `0x001D79AD` | `rdx` | `0x20` | `movups xmmword ptr [rdx + 0x20], xmm0` |
| `0x001D79B1` | `rcx` | `0x30` | `movups xmm1, xmmword ptr [rcx + rbx + 0x30]` |
| `0x001D79B6` | `rdx` | `0x30` | `movups xmmword ptr [rdx + 0x30], xmm1` |
| `0x001D79BA` | `rcx` | `0x40` | `movups xmm0, xmmword ptr [rcx + rbx + 0x40]` |
| `0x001D79BF` | `rdx` | `0x40` | `movups xmmword ptr [rdx + 0x40], xmm0` |
| `0x001D79C3` | `rcx` | `0x50` | `movsd xmm1, qword ptr [rcx + rbx + 0x50]` |
| `0x001D79C9` | `rdx` | `0x50` | `movsd qword ptr [rdx + 0x50], xmm1` |
| `0x001D79CE` | `rcx` | `0x58` | `mov eax, dword ptr [rcx + rbx + 0x58]` |
| `0x001D79D2` | `rdx` | `0x58` | `mov dword ptr [rdx + 0x58], eax` |
| `0x001D79E6` | `rcx` | `0x3A0` | `mov eax, dword ptr [rcx + 0x3a0]` |
| `0x001D79F3` | `rsi` | `0x0` | `cmp dword ptr [rsi], eax` |
| `0x001D79F7` | `rsi` | `0x4` | `cmp dword ptr [rsi + 4], 8` |
| `0x001D7A0E` | `rdx` | `0x5C` | `lea r8d, [rdx + 0x5c]` |
| `0x001D7A1B` | `rsi` | `0x10` | `mov r12d, dword ptr [rsi + 0x10]` |
| `0x001D7A23` | `rsi` | `0xC` | `mov r15d, dword ptr [rsi + 0xc]` |
| `0x001D7A2B` | `rsi` | `0x8` | `mov r14d, dword ptr [rsi + 8]` |
| `0x001D7A33` | `rsi` | `0x14` | `mov esi, dword ptr [rsi + 0x14]` |
| `0x001D7A39` | `rbx` | `0x3A0` | `mov eax, dword ptr [rbx + 0x3a0]` |
| `0x001D7A46` | `rdi` | `0x0` | `cmp dword ptr [rdi], eax` |
| `0x001D7A4A` | `rdi` | `0x4` | `cmp dword ptr [rdi + 4], 9` |
| `0x001D7A61` | `rdx` | `0x5C` | `lea r8d, [rdx + 0x5c]` |
| `0x001D7A71` | `rdi` | `0x10` | `mov ecx, dword ptr [rdi + 0x10]` |
| `0x001D7A7E` | `rdi` | `0xC` | `mov edx, dword ptr [rdi + 0xc]` |
| `0x001D7A8B` | `rdi` | `0x8` | `mov r8d, dword ptr [rdi + 8]` |
| `0x001D7A9B` | `rdi` | `0x14` | `mov eax, dword ptr [rdi + 0x14]` |
| `0x001D7AB1` | `rdi` | `0x188` | `mov r9d, dword ptr [rdi + rbx + 0x188]` |
| `0x001D7AC9` | `rdi` | `0x17C` | `mov r9d, dword ptr [rdi + rbx + 0x17c]` |
| `0x001D7AE1` | `rdi` | `0x170` | `mov r9d, dword ptr [rdi + rbx + 0x170]` |
| `0x001D7AF9` | `rdi` | `0x14C` | `mov r9d, dword ptr [rdi + rbx + 0x14c]` |
| `0x001D7B35` | `rdx` | `0x5C` | `lea r8d, [rdx + 0x5c]` |
| `0x001D7B43` | `rbx` | `0x258` | `mov r8d, dword ptr [rbx + 0x258]` |
| `0x001D7DF3` | `rax` | `0x18` | `cmp qword ptr [rax + 0x18], 0x10` |
| `0x001D7DFA` | `rax` | `0x0` | `mov rax, qword ptr [rax]` |
| `0x001D7DFD` | `rbx` | `0x8` | `lea rdx, [rbx + 8]` |
| `0x001D7E01` | `rbx` | `0x258` | `lea r8, [rbx + 0x258]` |

### Full body

```asm
0x001D7930: mov rax, rsp
0x001D7933: push rbp
0x001D7934: push rsi
0x001D7935: push rdi
0x001D7936: push r12
0x001D7938: push r13
0x001D793A: push r14
0x001D793C: push r15
0x001D793E: lea rbp, [rax - 0x808]
0x001D7945: sub rsp, 0x8d0
0x001D794C: mov qword ptr [rbp + 0x80], 0xfffffffffffffffe
0x001D7957: mov qword ptr [rax + 0x20], rbx
0x001D795B: movaps xmmword ptr [rax - 0x48], xmm6
0x001D795F: mov rax, qword ptr [rip + 0x5fef8a]
0x001D7966: xor rax, rsp
0x001D7969: mov qword ptr [rbp + 0x7b0], rax
0x001D7970: movsxd rax, r8d
0x001D7973: mov dword ptr [rsp + 0x3c], eax
0x001D7977: mov r13, rdx
0x001D797A: mov rbx, rcx
0x001D797D: cmp eax, 2
0x001D7980: ja 0x1401d944f
0x001D7986: cmp byte ptr [rcx + rax + 0x398], 0
0x001D798E: je 0x1401d79dc
0x001D7990: add rax, 7
0x001D7994: imul rcx, rax, 0x5c
0x001D7998: movups xmm0, xmmword ptr [rcx + rbx]
0x001D799C: movups xmmword ptr [rdx], xmm0
0x001D799F: movups xmm1, xmmword ptr [rcx + rbx + 0x10]
0x001D79A4: movups xmmword ptr [rdx + 0x10], xmm1
0x001D79A8: movups xmm0, xmmword ptr [rcx + rbx + 0x20]
0x001D79AD: movups xmmword ptr [rdx + 0x20], xmm0
0x001D79B1: movups xmm1, xmmword ptr [rcx + rbx + 0x30]
0x001D79B6: movups xmmword ptr [rdx + 0x30], xmm1
0x001D79BA: movups xmm0, xmmword ptr [rcx + rbx + 0x40]
0x001D79BF: movups xmmword ptr [rdx + 0x40], xmm0
0x001D79C3: movsd xmm1, qword ptr [rcx + rbx + 0x50]
0x001D79C9: movsd qword ptr [rdx + 0x50], xmm1
0x001D79CE: mov eax, dword ptr [rcx + rbx + 0x58]
0x001D79D2: mov dword ptr [rdx + 0x58], eax
0x001D79D5: mov al, 1
0x001D79D7: jmp 0x1401d9451
0x001D79DC: lea rdi, [rip + 0x2e5ced]
0x001D79E3: mov rsi, rdi
0x001D79E6: mov eax, dword ptr [rcx + 0x3a0]
0x001D79EC: lea rcx, [rip + 0x2e5e5d]
0x001D79F3: cmp dword ptr [rsi], eax
0x001D79F5: jne 0x1401d79fd
0x001D79F7: cmp dword ptr [rsi + 4], 8
0x001D79FB: je 0x1401d7a0c
0x001D79FD: add rsi, 0x18
0x001D7A01: cmp rsi, rcx
0x001D7A04: je 0x1401d9206
0x001D7A0A: jmp 0x1401d79f3
0x001D7A0C: xor edx, edx
0x001D7A0E: lea r8d, [rdx + 0x5c]
0x001D7A12: lea rcx, [rbp + 0x20]
0x001D7A16: call 0x1403d3050
0x001D7A1B: mov r12d, dword ptr [rsi + 0x10]
0x001D7A1F: mov dword ptr [rbp + 0x4c], r12d
0x001D7A23: mov r15d, dword ptr [rsi + 0xc]
0x001D7A27: mov dword ptr [rbp + 0x58], r15d
0x001D7A2B: mov r14d, dword ptr [rsi + 8]
0x001D7A2F: mov dword ptr [rbp + 0x64], r14d
0x001D7A33: mov esi, dword ptr [rsi + 0x14]
0x001D7A36: mov dword ptr [rbp + 0x28], esi
0x001D7A39: mov eax, dword ptr [rbx + 0x3a0]
0x001D7A3F: lea rcx, [rip + 0x2e5e0a]
0x001D7A46: cmp dword ptr [rdi], eax
0x001D7A48: jne 0x1401d7a50
0x001D7A4A: cmp dword ptr [rdi + 4], 9
0x001D7A4E: je 0x1401d7a5f
0x001D7A50: add rdi, 0x18
0x001D7A54: cmp rdi, rcx
0x001D7A57: je 0x1401d9206
0x001D7A5D: jmp 0x1401d7a46
0x001D7A5F: xor edx, edx
0x001D7A61: lea r8d, [rdx + 0x5c]
0x001D7A65: lea rcx, [rbp + 0xa0]
0x001D7A6C: call 0x1403d3050
0x001D7A71: mov ecx, dword ptr [rdi + 0x10]
0x001D7A74: mov dword ptr [rsp + 0x38], ecx
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
0x001D7B8B: xor ecx, 0x7d
0x001D7B8E: add ecx, 2
0x001D7B91: mov byte ptr [rbp + 0x3f5], cl
0x001D7B97: movsx ecx, byte ptr [rbp + 0x3f5]
0x001D7B9E: xor ecx, 0x3a
0x001D7BA1: add ecx, 2
0x001D7BA4: mov byte ptr [rbp + 0x3f6], cl
0x001D7BAA: movsx ecx, byte ptr [rbp + 0x3f6]
0x001D7BB1: xor ecx, 0x20
0x001D7BB4: add ecx, 2
0x001D7BB7: mov byte ptr [rbp + 0x3f7], cl
0x001D7BBD: movsx ecx, byte ptr [rbp + 0x3f7]
0x001D7BC4: xor ecx, 0x75
0x001D7BC7: add ecx, 2
0x001D7BCA: mov byte ptr [rbp + 0x3f8], cl
0x001D7BD0: movsx ecx, byte ptr [rbp + 0x3f8]
0x001D7BD7: xor ecx, 0x6e
0x001D7BDA: add ecx, 2
0x001D7BDD: mov byte ptr [rbp + 0x3f9], cl
0x001D7BE3: movsx ecx, byte ptr [rbp + 0x3f9]
0x001D7BEA: xor ecx, 0x61
0x001D7BED: add ecx, 2
0x001D7BF0: mov byte ptr [rbp + 0x3fa], cl
0x001D7BF6: movsx ecx, byte ptr [rbp + 0x3fa]
0x001D7BFD: xor ecx, 0x62
0x001D7C00: add ecx, 2
0x001D7C03: mov byte ptr [rbp + 0x3fb], cl
0x001D7C09: movsx ecx, byte ptr [rbp + 0x3fb]
0x001D7C10: xor ecx, 0x6c
0x001D7C13: add ecx, 2
0x001D7C16: mov byte ptr [rbp + 0x3fc], cl
0x001D7C1C: movsx ecx, byte ptr [rbp + 0x3fc]
0x001D7C23: xor ecx, 0x65
0x001D7C26: add ecx, 2
0x001D7C29: mov byte ptr [rbp + 0x3fd], cl
0x001D7C2F: movsx ecx, byte ptr [rbp + 0x3fd]
0x001D7C36: xor ecx, 0x20
0x001D7C39: add ecx, 2
0x001D7C3C: mov byte ptr [rbp + 0x3fe], cl
0x001D7C42: movsx ecx, byte ptr [rbp + 0x3fe]
0x001D7C49: xor ecx, 0x74
0x001D7C4C: add ecx, 2
0x001D7C4F: mov byte ptr [rbp + 0x3ff], cl
0x001D7C55: movsx ecx, byte ptr [rbp + 0x3ff]
0x001D7C5C: xor ecx, 0x6f
0x001D7C5F: add ecx, 2
0x001D7C62: mov byte ptr [rbp + 0x400], cl
0x001D7C68: movsx ecx, byte ptr [rbp + 0x400]
0x001D7C6F: xor ecx, 0x20
0x001D7C72: add ecx, 2
0x001D7C75: mov byte ptr [rbp + 0x401], cl
0x001D7C7B: movsx ecx, byte ptr [rbp + 0x401]
0x001D7C82: xor ecx, 0x66
0x001D7C85: add ecx, 2
0x001D7C88: mov byte ptr [rbp + 0x402], cl
0x001D7C8E: movsx ecx, byte ptr [rbp + 0x402]
0x001D7C95: xor ecx, 0x69
0x001D7C98: add ecx, 2
0x001D7C9B: mov byte ptr [rbp + 0x403], cl
0x001D7CA1: movsx ecx, byte ptr [rbp + 0x403]
0x001D7CA8: xor ecx, 0x6e
0x001D7CAB: add ecx, 2
0x001D7CAE: mov byte ptr [rbp + 0x404], cl
0x001D7CB4: movsx ecx, byte ptr [rbp + 0x404]
0x001D7CBB: xor ecx, 0x64
0x001D7CBE: add ecx, 2
0x001D7CC1: mov byte ptr [rbp + 0x405], cl
0x001D7CC7: movsx ecx, byte ptr [rbp + 0x405]
0x001D7CCE: xor ecx, 0x20
0x001D7CD1: add ecx, 2
0x001D7CD4: mov byte ptr [rbp + 0x406], cl
0x001D7CDA: movsx ecx, byte ptr [rbp + 0x406]
0x001D7CE1: xor ecx, 0x73
0x001D7CE4: add ecx, 2
0x001D7CE7: mov byte ptr [rbp + 0x407], cl
0x001D7CED: movsx ecx, byte ptr [rbp + 0x407]
0x001D7CF4: xor ecx, 0x74
0x001D7CF7: add ecx, 2
0x001D7CFA: mov byte ptr [rbp + 0x408], cl
0x001D7D00: movsx ecx, byte ptr [rbp + 0x408]
0x001D7D07: xor ecx, 0x72
0x001D7D0A: add ecx, 2
0x001D7D0D: mov byte ptr [rbp + 0x409], cl
0x001D7D13: movsx ecx, byte ptr [rbp + 0x409]
0x001D7D1A: xor ecx, 0x61
0x001D7D1D: add ecx, 2
0x001D7D20: mov byte ptr [rbp + 0x40a], cl
0x001D7D26: movsx ecx, byte ptr [rbp + 0x40a]
0x001D7D2D: xor ecx, 0x70
0x001D7D30: add ecx, 2
0x001D7D33: mov byte ptr [rbp + 0x40b], cl
0x001D7D39: movsx ecx, byte ptr [rbp + 0x40b]
0x001D7D40: xor ecx, 0x20
0x001D7D43: add ecx, 2
0x001D7D46: mov byte ptr [rbp + 0x40c], cl
0x001D7D4C: movsx ecx, byte ptr [rbp + 0x40c]
0x001D7D53: xor ecx, 0x7b
0x001D7D56: add ecx, 2
0x001D7D59: mov byte ptr [rbp + 0x40d], cl
0x001D7D5F: movsx ecx, byte ptr [rbp + 0x40d]
0x001D7D66: xor ecx, 0x7d
0x001D7D69: add ecx, 2
0x001D7D6C: mov byte ptr [rbp + 0x40e], cl
0x001D7D72: movsx ecx, byte ptr [rbp + 0x40e]
0x001D7D79: xor ecx, 0x20
0x001D7D7C: add ecx, 2
0x001D7D7F: mov byte ptr [rbp + 0x40f], cl
0x001D7D85: movsx ecx, byte ptr [rbp + 0x40f]
0x001D7D8C: xor ecx, 0x69
0x001D7D8F: add ecx, 2
0x001D7D92: mov byte ptr [rbp + 0x410], cl
0x001D7D98: movsx ecx, byte ptr [rbp + 0x410]
0x001D7D9F: xor ecx, 0x6e
0x001D7DA2: add ecx, 2
0x001D7DA5: mov byte ptr [rbp + 0x411], cl
0x001D7DAB: movsx ecx, byte ptr [rbp + 0x411]
0x001D7DB2: xor ecx, 0x66
0x001D7DB5: add ecx, 2
0x001D7DB8: mov byte ptr [rbp + 0x412], cl
0x001D7DBE: movsx ecx, byte ptr [rbp + 0x412]
0x001D7DC5: xor ecx, 0x6f
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
