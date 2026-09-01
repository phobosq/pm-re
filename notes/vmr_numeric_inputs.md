# VMR numeric input provenance

Interpolation anchor: `0x1D8B1F`; formula consumes ESI, ECX, child+0x25C and XMM6.

## Watched local accesses

- `0x001D7A36` write `vmr_base_rbp28`: `mov dword ptr [rbp + 0x28], esi`
- `0x001D7A9E` write `vmr_alt_rsp40`: `mov dword ptr [rsp + 0x40], eax`
- `0x001D7AA2` write `vmr_target_rbpA8`: `mov dword ptr [rbp + 0xa8], eax`
- `0x001D7B0D` write `vmr_base_rbp28`: `mov dword ptr [rbp + 0x28], esi`
- `0x001D7E38` read `vmr_alt_rsp40`: `sub esi, dword ptr [rsp + 0x40]`
- `0x001D7E4E` write `vmr_alt_rsp40`: `mov dword ptr [rsp + 0x40], eax`
- `0x001D7E54` write `vmr_alt_rsp40`: `mov dword ptr [rsp + 0x40], 0`
- `0x001D83C5` read `vmr_alt_rsp40`: `mov eax, dword ptr [rsp + 0x40]`
- `0x001D83D9` write `vmr_alt_rsp40`: `mov qword ptr [rsp + 0x40], 0x22222b`
- `0x001D83EE` read `vmr_alt_rsp40`: `movups xmm0, xmmword ptr [rsp + 0x40]`
- `0x001D84CD` read `vmr_base_rbp28`: `mov esi, dword ptr [rbp + 0x28]`
- `0x001D84EE` read `vmr_target_rbpA8`: `mov eax, dword ptr [rbp + 0xa8]`
- `0x001D84F4` write `vmr_alt_rsp40`: `mov dword ptr [rsp + 0x40], eax`
- `0x001D8B10` read `vmr_base_rbp28`: `mov esi, dword ptr [rbp + 0x28]`
- `0x001D8B13` read `vmr_target_rbpA8`: `mov ecx, dword ptr [rbp + 0xa8]`
- `0x001D8B1B` read `vmr_alt_rsp40`: `mov ecx, dword ptr [rsp + 0x40]`

## writer `vmr_base_rbp28` at `0x001D7A36`

```asm
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
```

## writer `vmr_alt_rsp40` at `0x001D7A9E`

```asm
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
```

## writer `vmr_target_rbpA8` at `0x001D7AA2`

```asm
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
```

## writer `vmr_base_rbp28` at `0x001D7B0D`

```asm
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
```

## writer `vmr_alt_rsp40` at `0x001D7E4E`

```asm
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
0x001D7E46: divsd xmm1, xmm0
0x001D7E4A: cvttsd2si eax, xmm1
0x001D7E4E: mov dword ptr [rsp + 0x40], eax
0x001D7E52: jmp 0x1401d7e5c
0x001D7E54: mov dword ptr [rsp + 0x40], 0
0x001D7E5C: mov ecx, dword ptr [rbp - 0x64]
0x001D7E5F: test ecx, ecx
0x001D7E61: je 0x1401d7e93
0x001D7E63: cmp ecx, r12d
0x001D7E66: jae 0x1401d7e93
0x001D7E68: mov eax, r12d
0x001D7E6B: sub eax, ecx
0x001D7E6D: imul ecx, eax, 0x64
0x001D7E70: xorps xmm1, xmm1
0x001D7E73: cvtsi2sd xmm1, rcx
0x001D7E78: sub r12d, dword ptr [rsp + 0x38]
0x001D7E7D: mov eax, r12d
0x001D7E80: xorps xmm0, xmm0
0x001D7E83: cvtsi2sd xmm0, rax
0x001D7E88: divsd xmm1, xmm0
```

## writer `vmr_alt_rsp40` at `0x001D7E54`

```asm
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
0x001D7E46: divsd xmm1, xmm0
0x001D7E4A: cvttsd2si eax, xmm1
0x001D7E4E: mov dword ptr [rsp + 0x40], eax
0x001D7E52: jmp 0x1401d7e5c
0x001D7E54: mov dword ptr [rsp + 0x40], 0
0x001D7E5C: mov ecx, dword ptr [rbp - 0x64]
0x001D7E5F: test ecx, ecx
0x001D7E61: je 0x1401d7e93
0x001D7E63: cmp ecx, r12d
0x001D7E66: jae 0x1401d7e93
0x001D7E68: mov eax, r12d
0x001D7E6B: sub eax, ecx
0x001D7E6D: imul ecx, eax, 0x64
0x001D7E70: xorps xmm1, xmm1
0x001D7E73: cvtsi2sd xmm1, rcx
0x001D7E78: sub r12d, dword ptr [rsp + 0x38]
0x001D7E7D: mov eax, r12d
0x001D7E80: xorps xmm0, xmm0
0x001D7E83: cvtsi2sd xmm0, rax
0x001D7E88: divsd xmm1, xmm0
0x001D7E8C: cvttsd2si r12d, xmm1
0x001D7E91: jmp 0x1401d7e96
```

## writer `vmr_alt_rsp40` at `0x001D83D9`

```asm
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
0x001D83C5: mov eax, dword ptr [rsp + 0x40]
0x001D83C9: mov dword ptr [rsp + 0x50], eax
0x001D83CD: movups xmm0, xmmword ptr [rsp + 0x50]
0x001D83D2: movaps xmmword ptr [rbp + 0x7a0], xmm0
0x001D83D9: mov qword ptr [rsp + 0x40], 0x22222b
0x001D83E2: lea rax, [rbp + 0x750]
0x001D83E9: mov qword ptr [rsp + 0x48], rax
0x001D83EE: movups xmm0, xmmword ptr [rsp + 0x40]
0x001D83F3: movups xmmword ptr [rbp - 0x18], xmm0
0x001D83F7: mov dword ptr [rbp - 8], r14d
0x001D83FB: lea rax, [rbp + 0x520]
0x001D8402: mov qword ptr [rbp], rax
0x001D8406: xorps xmm0, xmm0
0x001D8409: movdqu xmmword ptr [rbp + 8], xmm0
0x001D840E: mov qword ptr [rbp + 0x18], r14
0x001D8412: lea rcx, [rbp - 0x18]
0x001D8416: call 0x140036ad0
0x001D841B: nop
0x001D841C: mov r9, qword ptr [rbp + 8]
0x001D8420: test r9, r9
0x001D8423: je 0x1401d845f
0x001D8425: mov rcx, qword ptr [rbp + 0x18]
```

## writer `vmr_alt_rsp40` at `0x001D84F4`

```asm
0x001D8474: mov qword ptr [rbp + 0x110], rax
0x001D847B: lea rdx, [rbp + 0x530]
0x001D8482: lea rcx, [rbp + 0x120]
0x001D8489: call 0x1400328e0
0x001D848E: lea rcx, [rbp + 0x110]
0x001D8495: call 0x140073470
0x001D849A: nop
0x001D849B: lea rcx, [rbp + 0x530]
0x001D84A2: call 0x140032dc0
0x001D84A7: lea rax, [rip + 0x25b7fa]
0x001D84AE: mov qword ptr [rbp + 0x520], rax
0x001D84B5: lea rcx, [rbp + 0x480]
0x001D84BC: call 0x140032ef0
0x001D84C1: mov r14d, dword ptr [rbp + 0x64]
0x001D84C5: mov r15d, dword ptr [rbp + 0x58]
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
```

## XMM6 definitions before interpolation


### `0x001D8500: movsd xmm6, qword ptr [rip + 0x2601b0]`

```asm
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
```

## Aligned lead-in 0x1D89C0..0x1D8B60

```asm
0x001D89C0: add al, 0x25
0x001D89C2: xor eax, ecx
0x001D89C4: xor eax, 0x7d
0x001D89C7: mov byte ptr [rbp + 0x365], al
0x001D89CD: movsx ecx, byte ptr [rbp + 0x365]
0x001D89D4: mov eax, dword ptr [rbp + 0x338]
0x001D89DA: add al, 0x26
0x001D89DC: xor eax, ecx
0x001D89DE: xor eax, 0x20
0x001D89E1: mov byte ptr [rbp + 0x366], al
0x001D89E7: movsx ecx, byte ptr [rbp + 0x366]
0x001D89EE: mov eax, dword ptr [rbp + 0x338]
0x001D89F4: add al, 0x27
0x001D89F6: xor eax, ecx
0x001D89F8: xor eax, 0x2d
0x001D89FB: mov byte ptr [rbp + 0x367], al
0x001D8A01: movsx ecx, byte ptr [rbp + 0x367]
0x001D8A08: mov eax, dword ptr [rbp + 0x338]
0x001D8A0E: add al, 0x28
0x001D8A10: xor eax, ecx
0x001D8A12: xor eax, 0x76
0x001D8A15: mov byte ptr [rbp + 0x368], al
0x001D8A1B: movsx ecx, byte ptr [rbp + 0x368]
0x001D8A22: mov eax, dword ptr [rbp + 0x338]
0x001D8A28: add al, 0x29
0x001D8A2A: xor eax, ecx
0x001D8A2C: xor eax, 0x6d
0x001D8A2F: mov byte ptr [rbp + 0x369], al
0x001D8A35: movsx ecx, byte ptr [rbp + 0x369]
0x001D8A3C: mov eax, dword ptr [rbp + 0x338]
0x001D8A42: add al, 0x2a
0x001D8A44: xor eax, ecx
0x001D8A46: xor eax, 0x74
0x001D8A49: mov byte ptr [rbp + 0x36a], al
0x001D8A4F: movsx ecx, byte ptr [rbp + 0x36a]
0x001D8A56: mov eax, dword ptr [rbp + 0x338]
0x001D8A5C: add al, 0x2b
0x001D8A5E: xor eax, ecx
0x001D8A60: xor eax, 0x33
0x001D8A63: mov byte ptr [rbp + 0x36b], al
0x001D8A69: movsx ecx, byte ptr [rbp + 0x36b]
0x001D8A70: mov eax, dword ptr [rbp + 0x338]
0x001D8A76: add al, 0x2c
0x001D8A78: xor eax, ecx
0x001D8A7A: xor eax, 0x20
0x001D8A7D: mov byte ptr [rbp + 0x36c], al
0x001D8A83: movsx ecx, byte ptr [rbp + 0x36c]
0x001D8A8A: mov eax, dword ptr [rbp + 0x338]
0x001D8A90: add al, 0x2d
0x001D8A92: xor eax, ecx
0x001D8A94: xor eax, 0x7b
0x001D8A97: mov byte ptr [rbp + 0x36d], al
0x001D8A9D: movsx ecx, byte ptr [rbp + 0x36d]
0x001D8AA4: mov eax, dword ptr [rbp + 0x338]
0x001D8AAA: add al, 0x2e
0x001D8AAC: xor eax, ecx
0x001D8AAE: xor eax, 0x7d
0x001D8AB1: mov byte ptr [rbp + 0x36e], al
0x001D8AB7: xor eax, eax
0x001D8AB9: mov byte ptr [rbp + 0x36f], al
0x001D8ABF: movzx eax, byte ptr [rbp + 0x340]
0x001D8AC6: lea rdx, [rbp + 0x4a0]
0x001D8ACD: lea rcx, [rbp + 0x338]
0x001D8AD4: call 0x1401372a0
0x001D8AD9: nop
0x001D8ADA: cmp qword ptr [rax + 0x18], 0x10
0x001D8ADF: jb 0x1401d8ae4
0x001D8AE1: mov rax, qword ptr [rax]
0x001D8AE4: lea rdx, [rbx + 8]
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
0x001D8B53: subsd xmm2, xmm1
0x001D8B57: cvttsd2si rax, xmm2
0x001D8B5C: mov dword ptr [rsp + 0x78], eax
```