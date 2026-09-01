# Direct VMR +0xB0 read candidates

non-stack dword read candidates: 64

| score | RVA | PDATA | instruction |
|---:|---|---|---|
| 6 | `0x001F7591` | `0x001F74BB..0x001F770A` | `cmp ebx, dword ptr [rdi + 0xb0]` |
| 6 | `0x001F8EA8` | `0x001F7F40..0x001FB9C1` | `cmp r14d, dword ptr [rsi + 0xb0]` |
| 4 | `0x0009E00F` | `0x0009DFD0..0x0009E062` | `cmp dword ptr [rbx + 0xb0], edi` |
| 4 | `0x0009E036` | `0x0009DFD0..0x0009E062` | `cmp dword ptr [rbx + 0xb0], edi` |
| 4 | `0x000A1A82` | `0x000A1A50..0x000A1AC9` | `cmp dword ptr [rdi + 0xb0], esi` |
| 4 | `0x000B7B75` | `0x000B7B60..0x000B7B8F` | `mov eax, dword ptr [rbx + 0xb0]` |
| 4 | `0x000C6EA3` | `0x000C6E80..0x000C6EAE` | `mov eax, dword ptr [rsi + 0xb0]` |
| 4 | `0x000C6ECC` | `0x000C6EAE..0x000C6ED7` | `mov eax, dword ptr [rbx + 0xb0]` |
| 4 | `0x000D998B` | `0x000CAAD0..0x000D9A27` | `mov eax, dword ptr [rbx + 0xb0]` |
| 4 | `0x00274A6B` | `0x002749E0..0x00274C56` | `mov r8d, dword ptr [rdi + 0xb0]` |
| 4 | `0x00274BBD` | `0x002749E0..0x00274C56` | `mov r8d, dword ptr [rdi + 0xb0]` |
| 4 | `0x00274D53` | `0x00274C60..0x00274F45` | `mov r8d, dword ptr [rdi + 0xb0]` |
| 4 | `0x00274EA7` | `0x00274C60..0x00274F45` | `mov r8d, dword ptr [rdi + 0xb0]` |
| 4 | `0x00274FC5` | `0x00274F50..0x0027518D` | `mov r8d, dword ptr [rdi + 0xb0]` |
| 4 | `0x00275107` | `0x00274F50..0x0027518D` | `mov r8d, dword ptr [rdi + 0xb0]` |
| 4 | `0x002850BB` | `0x00283B10..0x0028560C` | `mov eax, dword ptr [rbx + 0xb0]` |
| 4 | `0x002850C1` | `0x00283B10..0x0028560C` | `cmp dword ptr [rcx + 0xb0], eax` |
| 4 | `0x002D871B` | `0x002D86C0..0x002D876F` | `cmp dword ptr [rbx + 0xb0], 0` |
| 4 | `0x002D884F` | `0x002D8840..0x002D8881` | `cmp dword ptr [rcx + 0xb0], 0` |
| 4 | `0x002E23BF` | `0x002E2350..0x002E24A0` | `cmp dword ptr [rbx + 0xb0], 0` |
| 4 | `0x00305A53` | `0x003053C0..0x00305BB6` | `mov ebx, dword ptr [rcx + 0xb0]` |
| 4 | `0x0032C723` | `0x0032C670..0x0032C7B7` | `cmp dword ptr [rbx + 0xb0], 0` |
| 4 | `0x0038B114` | `0x0038B100..0x0038B1D0` | `cmp dword ptr [rdx + 0xb0], 0` |
| 4 | `0x0038B1EF` | `0x0038B1D0..0x0038B2FD` | `cmp dword ptr [rdx + 0xb0], r12d` |
| 4 | `0x0038B2D2` | `0x0038B1D0..0x0038B2FD` | `mov ecx, dword ptr [rsi + 0xb0]` |
| 4 | `0x003B74DB` | `0x003B7494..0x003B7690` | `add edx, dword ptr [rbx + 0xb0]` |
| 4 | `0x003B7520` | `0x003B7494..0x003B7690` | `mov edx, dword ptr [rbx + 0xb0]` |
| 4 | `0x003B763A` | `0x003B7494..0x003B7690` | `mov eax, dword ptr [rbx + 0xb0]` |
| 4 | `0x003B765F` | `0x003B7494..0x003B7690` | `add r8d, dword ptr [rbx + 0xb0]` |
| 4 | `0x003B8CDF` | `0x003B8CA8..0x003B8D09` | `add edx, dword ptr [rcx + 0xb0]` |
| 4 | `0x003B9342` | `0x003B92B0..0x003B94CC` | `mov r8d, dword ptr [rbx + 0xb0]` |
| 4 | `0x003B93AB` | `0x003B92B0..0x003B94CC` | `mov esi, dword ptr [rbx + 0xb0]` |
| 4 | `0x003B9D50` | `0x003B9AEC..0x003B9ED5` | `add r11d, dword ptr [rdx + 0xb0]` |
| 4 | `0x003BA257` | `0x003BA210..0x003BA2B7` | `add ecx, dword ptr [rdi + 0xb0]` |
| 4 | `0x003BAAF0` | `0x003BA9E0..0x003BABA5` | `mov eax, dword ptr [rbx + 0xb0]` |
| 4 | `0x003BAC6B` | `0x003BABA8..0x003BACC1` | `add edx, dword ptr [rdi + 0xb0]` |
| 4 | `0x003BAD7F` | `0x003BACC4..0x003BADEA` | `mov eax, dword ptr [rsi + 0xb0]` |
| 4 | `0x003C0A23` | `0x003C0A04..0x003C0BE7` | `mov eax, dword ptr [rcx + 0xb0]` |
| 4 | `0x003C0A47` | `0x003C0A04..0x003C0BE7` | `mov eax, dword ptr [rbx + 0xb0]` |
| 4 | `0x003C10DE` | `0x003C10AC..0x003C116B` | `mov eax, dword ptr [rdi + 0xb0]` |
| 4 | `0x003C31E5` | `0x003C31D0..0x003C31FB` | `mov ecx, dword ptr [rcx + 0xb0]` |
| 4 | `0x003C3211` | `0x003C31FC..0x003C3236` | `mov ebx, dword ptr [rdx + 0xb0]` |
| 4 | `0x003C35C6` | `0x003C3574..0x003C36C4` | `add r8d, dword ptr [r9 + 0xb0]` |
| 4 | `0x003C3AE5` | `0x003C397C..0x003C3C19` | `mov r8d, dword ptr [rsi + 0xb0]` |
| 4 | `0x003C3FFE` | `none` | `add r10d, dword ptr [r8 + 0xb0]` |
| 4 | `0x003C43A3` | `0x003C4378..0x003C43CD` | `mov eax, dword ptr [rcx + 0xb0]` |
| 4 | `0x003C46BC` | `0x003C46B0..0x003C46DB` | `mov ecx, dword ptr [rax + 0xb0]` |
| 4 | `0x003C4BE3` | `0x003C4BB4..0x003C4C0D` | `mov eax, dword ptr [rcx + 0xb0]` |
| 4 | `0x003C4CD7` | `0x003C4CBC..0x003C4D9A` | `mov ecx, dword ptr [rax + 0xb0]` |
| 4 | `0x003CBA5A` | `0x003CB9B4..0x003CBAB1` | `mov eax, dword ptr [rdx + 0xb0]` |
| 4 | `0x003CBD6C` | `0x003CBD38..0x003CBD95` | `mov eax, dword ptr [rbx + 0xb0]` |
| 4 | `0x003CC102` | `0x003CC028..0x003CC3BE` | `mov eax, dword ptr [rdi + 0xb0]` |
| 4 | `0x003CC183` | `0x003CC028..0x003CC3BE` | `mov eax, dword ptr [rdi + 0xb0]` |
| 4 | `0x003CC240` | `0x003CC028..0x003CC3BE` | `mov eax, dword ptr [rdi + 0xb0]` |
| 4 | `0x003CC27D` | `0x003CC028..0x003CC3BE` | `mov eax, dword ptr [rdi + 0xb0]` |
| 4 | `0x003CC372` | `0x003CC028..0x003CC3BE` | `mov eax, dword ptr [rdx + 0xb0]` |
| 4 | `0x003CD9A8` | `0x003CD978..0x003CDA9E` | `mov eax, dword ptr [rcx + 0xb0]` |
| 4 | `0x003CE29D` | `0x003CE288..0x003CE330` | `mov ecx, dword ptr [rdx + 0xb0]` |
| 2 | `0x002D85F0` | `0x002D85D3..0x002D86B2` | `sub dword ptr [rdi + 0xb0], ebx` |
| 2 | `0x002D8743` | `0x002D86C0..0x002D876F` | `inc dword ptr [rbx + 0xb0]` |
| 2 | `0x002D878F` | `0x002D8770..0x002D8836` | `sub dword ptr [rcx + 0xb0], edi` |
| 2 | `0x002D8875` | `0x002D8840..0x002D8881` | `inc dword ptr [rbx + 0xb0]` |
| 2 | `0x003C04D7` | `0x003C04A0..0x003C04EE` | `lock dec dword ptr [rsi + 0xb0]` |
| 2 | `0x003C10A4` | `none` | `lock inc dword ptr [rcx + 0xb0]` |

## Top candidate contexts

### `0x001F7591` score 6 base `rdi`

```asm
0x001F755D: cmp r8, 0x7ad550
0x001F7564: jg 0x1401f765d
0x001F756A: test r9b, r9b
0x001F756D: jne 0x1401f765d
0x001F7573: test cl, cl
0x001F7575: jne 0x1401f765d
0x001F757B: cmp r8, 0x4dd1e0
0x001F7582: jle 0x1401f7700
0x001F7588: cmp r10d, r15d
0x001F758B: je 0x1401f7700
0x001F7591: cmp ebx, dword ptr [rdi + 0xb0]
0x001F7597: jne 0x1401f7700
0x001F759D: mov eax, dword ptr [rdi + 0x38]
0x001F75A0: xorps xmm1, xmm1
0x001F75A3: mov dword ptr [rdi + 0x40], eax
0x001F75A6: mov rax, qword ptr [rdi + 0x50]
0x001F75AA: mov dword ptr [rdi + 0x2c], r15d
0x001F75AE: mov dword ptr [rdi + 0x70], r8d
0x001F75B2: mov dword ptr [rdi + 0x74], r8d
0x001F75B6: mov dword ptr [rdi + 0x38], r14d
0x001F75BA: cvtsi2sd xmm1, rax
0x001F75BF: test rax, rax
0x001F75C2: jns 0x1401f75cc
0x001F75C4: addsd xmm1, qword ptr [rip + 0x23caa4]
```

### `0x001F8EA8` score 6 base `rsi`

```asm
0x001F8E7C: mov eax, r14d
0x001F8E7F: cmp byte ptr [rsp + 0x50], 0
0x001F8E84: mov ecx, 0
0x001F8E89: cmovne eax, ecx
0x001F8E8C: cdqe
0x001F8E8E: mov r13, qword ptr [rdi + rax*8 + 0x230]
0x001F8E96: cmp dword ptr [rsi], ecx
0x001F8E98: jle 0x1401f8f40
0x001F8E9E: cmp dword ptr [rsi + 0x2c], 1
0x001F8EA2: je 0x1401f8f40
0x001F8EA8: cmp r14d, dword ptr [rsi + 0xb0]
0x001F8EAF: je 0x1401f8f40
0x001F8EB5: mov eax, r11d
0x001F8EB8: imul eax, dword ptr [rdi + 0x1b0]
0x001F8EBF: xorps xmm0, xmm0
0x001F8EC2: cvtsi2sd xmm0, rax
0x001F8EC7: mulsd xmm0, qword ptr [rdi + 0x3e0]
0x001F8ECF: addsd xmm0, xmm14
0x001F8ED4: mulsd xmm0, xmm15
0x001F8ED9: cvttsd2si rbx, xmm0
0x001F8EDE: movsxd r12, r14d
0x001F8EE1: mov r10, qword ptr [rdi]
0x001F8EE4: mov dword ptr [rsp + 0x48], r14d
0x001F8EE9: mov eax, dword ptr [rsp + 0x5c]
```

### `0x0009E00F` score 4 base `rbx`

```asm
0x0009DFEB: mov rbx, rcx
0x0009DFEE: lea rsi, [rcx + 0x48]
0x0009DFF2: mov qword ptr [rsp + 0x28], rsi
0x0009DFF7: mov rcx, rsi
0x0009DFFA: call 0x140391ac4
0x0009DFFF: test eax, eax
0x0009E001: je 0x14009e00a
0x0009E003: mov ecx, eax
0x0009E005: call 0x14039219c
0x0009E00A: mov byte ptr [rsp + 0x30], 1
0x0009E00F: cmp dword ptr [rbx + 0xb0], edi
0x0009E015: jge 0x14009e03e
0x0009E017: nop word ptr [rax + rax]
0x0009E020: mov rdx, rsi
0x0009E023: mov rcx, rbx
0x0009E026: call 0x140391ec4
0x0009E02B: test eax, eax
0x0009E02D: je 0x14009e036
0x0009E02F: mov ecx, eax
0x0009E031: call 0x14039219c
0x0009E036: cmp dword ptr [rbx + 0xb0], edi
0x0009E03C: jl 0x14009e020
0x0009E03E: mov rcx, rsi
0x0009E041: call 0x140391b24
```

### `0x0009E036` score 4 base `rbx`

```asm
0x0009E00F: cmp dword ptr [rbx + 0xb0], edi
0x0009E015: jge 0x14009e03e
0x0009E017: nop word ptr [rax + rax]
0x0009E020: mov rdx, rsi
0x0009E023: mov rcx, rbx
0x0009E026: call 0x140391ec4
0x0009E02B: test eax, eax
0x0009E02D: je 0x14009e036
0x0009E02F: mov ecx, eax
0x0009E031: call 0x14039219c
0x0009E036: cmp dword ptr [rbx + 0xb0], edi
0x0009E03C: jl 0x14009e020
0x0009E03E: mov rcx, rsi
0x0009E041: call 0x140391b24
0x0009E046: test eax, eax
0x0009E048: je 0x14009e052
0x0009E04A: mov ecx, eax
0x0009E04C: call 0x14039219c
0x0009E051: nop
0x0009E052: mov rbx, qword ptr [rsp + 0x50]
0x0009E057: mov rsi, qword ptr [rsp + 0x58]
0x0009E05C: add rsp, 0x40
0x0009E060: pop rdi
0x0009E061: ret
```

### `0x000A1A82` score 4 base `rdi`

```asm
0x000A1A5F: mov qword ptr [rsp + 0x40], rbx
0x000A1A64: mov qword ptr [rsp + 0x48], rsi
0x000A1A69: mov esi, edx
0x000A1A6B: mov rdi, rcx
0x000A1A6E: add rcx, 0x48
0x000A1A72: call 0x140391ac4
0x000A1A77: test eax, eax
0x000A1A79: je 0x1400a1a82
0x000A1A7B: mov ecx, eax
0x000A1A7D: call 0x14039219c
0x000A1A82: cmp dword ptr [rdi + 0xb0], esi
0x000A1A88: jge 0x1400a1a90
0x000A1A8A: mov dword ptr [rdi + 0xb0], esi
0x000A1A90: mov rcx, rdi
0x000A1A93: call 0x140391dc0
0x000A1A98: test eax, eax
0x000A1A9A: je 0x1400a1aa4
0x000A1A9C: mov ecx, eax
0x000A1A9E: call 0x14039219c
0x000A1AA3: nop
0x000A1AA4: lea rcx, [rdi + 0x48]
0x000A1AA8: call 0x140391b24
0x000A1AAD: test eax, eax
0x000A1AAF: je 0x1400a1ab9
```

### `0x000B7B75` score 4 base `rbx`

```asm
0x000B7B5C: int3
0x000B7B5D: int3
0x000B7B5E: int3
0x000B7B5F: int3
0x000B7B60: mov qword ptr [rsp + 8], rbx
0x000B7B65: push rdi
0x000B7B66: sub rsp, 0x20
0x000B7B6A: mov rbx, rdx
0x000B7B6D: mov rdi, rcx
0x000B7B70: call 0x140066530
0x000B7B75: mov eax, dword ptr [rbx + 0xb0]
0x000B7B7B: mov rbx, qword ptr [rsp + 0x30]
0x000B7B80: mov dword ptr [rdi + 0xb0], eax
0x000B7B86: mov rax, rdi
0x000B7B89: add rsp, 0x20
0x000B7B8D: pop rdi
0x000B7B8E: ret
0x000B7B8F: int3
0x000B7B90: mov qword ptr [rcx + 0x18], 0xf
0x000B7B98: xor eax, eax
0x000B7B9A: mov qword ptr [rcx + 0x10], rax
0x000B7B9E: mov byte ptr [rcx], al
0x000B7BA0: mov qword ptr [rcx + 0x30], rax
0x000B7BA4: mov qword ptr [rcx + 0x38], 0xf
```

### `0x000C6EA3` score 4 base `rsi`

```asm
0x000C6E7F: int3
0x000C6E80: mov qword ptr [rsp + 0x10], rsi
0x000C6E85: push rdi
0x000C6E86: sub rsp, 0x30
0x000C6E8A: mov dword ptr [rsp + 0x20], 0
0x000C6E92: mov rsi, rdx
0x000C6E95: mov rdi, rcx
0x000C6E98: cmp r8d, 1
0x000C6E9C: jne 0x1400c6eab
0x000C6E9E: call 0x140066630
0x000C6EA3: mov eax, dword ptr [rsi + 0xb0]
0x000C6EA9: jmp 0x1400c6ed7
0x000C6EAB: mov eax, r9d
0x000C6EAE: mov qword ptr [rsp + 0x40], rbx
0x000C6EB3: cdq
0x000C6EB4: idiv r8d
0x000C6EB7: movsxd rax, edx
0x000C6EBA: imul rbx, rax, 0xb8
0x000C6EC1: add rbx, rsi
0x000C6EC4: mov rdx, rbx
0x000C6EC7: call 0x140066630
0x000C6ECC: mov eax, dword ptr [rbx + 0xb0]
0x000C6ED2: mov rbx, qword ptr [rsp + 0x40]
0x000C6ED7: mov rsi, qword ptr [rsp + 0x48]
```

### `0x000C6ECC` score 4 base `rbx`

```asm
0x000C6EA9: jmp 0x1400c6ed7
0x000C6EAB: mov eax, r9d
0x000C6EAE: mov qword ptr [rsp + 0x40], rbx
0x000C6EB3: cdq
0x000C6EB4: idiv r8d
0x000C6EB7: movsxd rax, edx
0x000C6EBA: imul rbx, rax, 0xb8
0x000C6EC1: add rbx, rsi
0x000C6EC4: mov rdx, rbx
0x000C6EC7: call 0x140066630
0x000C6ECC: mov eax, dword ptr [rbx + 0xb0]
0x000C6ED2: mov rbx, qword ptr [rsp + 0x40]
0x000C6ED7: mov rsi, qword ptr [rsp + 0x48]
0x000C6EDC: mov dword ptr [rdi + 0xb0], eax
0x000C6EE2: mov rax, rdi
0x000C6EE5: add rsp, 0x30
0x000C6EE9: pop rdi
0x000C6EEA: ret
0x000C6EEB: int3
0x000C6EEC: int3
0x000C6EED: int3
0x000C6EEE: int3
0x000C6EEF: int3
0x000C6EF0: push rbp
```

### `0x000D998B` score 4 base `rbx`

```asm
0x000D9963: lea rdx, [rbx + 0x30]
0x000D9967: cmp qword ptr [rdx + 0x10], 0
0x000D996C: je 0x1400d9977
0x000D996E: lea rcx, [r13 + 0x20]
0x000D9972: call 0x1400b81b0
0x000D9977: lea rdx, [rbx + 0x70]
0x000D997B: cmp qword ptr [rdx + 0x10], 0
0x000D9980: je 0x1400d998b
0x000D9982: lea rcx, [r13 + 0x60]
0x000D9986: call 0x1400b81b0
0x000D998B: mov eax, dword ptr [rbx + 0xb0]
0x000D9991: test eax, eax
0x000D9993: je 0x1400d999c
0x000D9995: mov dword ptr [r13 + 0xa0], eax
0x000D999C: lea rdx, [rbx + 0x90]
0x000D99A3: cmp qword ptr [rdx + 0x10], 0
0x000D99A8: je 0x1400d99b6
0x000D99AA: lea rcx, [r13 + 0x80]
0x000D99B1: call 0x1400b81b0
0x000D99B6: lea rdx, [rbx + 0x50]
0x000D99BA: lea rcx, [r13 + 0x40]
0x000D99BE: call 0x1400b81b0
0x000D99C3: mov bl, 1
0x000D99C5: jmp 0x1400d99c9
```

### `0x00274A6B` score 4 base `rdi`

```asm
0x00274A40: lea rax, [rbp + 0x77]
0x00274A44: mov qword ptr [rsp + 0x28], rax
0x00274A49: lea rdx, [rip - 0x2c070]
0x00274A50: mov rcx, rdi
0x00274A53: mov qword ptr [rsp + 0x20], r14
0x00274A58: call 0x1402537c0
0x00274A5D: cmp eax, -2
0x00274A60: je 0x140274aca
0x00274A62: cmp eax, -1
0x00274A65: jne 0x140274bb8
0x00274A6B: mov r8d, dword ptr [rdi + 0xb0]
0x00274A72: mov rdx, qword ptr [rdi + 0xa8]
0x00274A79: mov rcx, qword ptr [rdi + 8]
0x00274A7D: call 0x1402c7e90
0x00274A82: movsxd rcx, eax
0x00274A85: test eax, eax
0x00274A87: jg 0x140274a8c
0x00274A89: mov rcx, rsi
0x00274A8C: mov rax, qword ptr [rdi + 0xb0]
0x00274A93: lea rdx, [rbp + 0x17]
0x00274A97: cmp rax, rcx
0x00274A9A: mov r9, r14
0x00274A9D: movzx r8d, bl
0x00274AA1: cmovb rcx, rax
```

### `0x00274BBD` score 4 base `rdi`

```asm
0x00274B96: movups xmmword ptr [rdi + 0xe0], xmm0
0x00274B9D: cmp dword ptr [r14], esi
0x00274BA0: je 0x140274a20
0x00274BA6: mov rdx, r14
0x00274BA9: mov rcx, rdi
0x00274BAC: call 0x14024e8d0
0x00274BB1: xor eax, eax
0x00274BB3: jmp 0x140274c3a
0x00274BB8: cmp eax, 1
0x00274BBB: jne 0x140274c2b
0x00274BBD: mov r8d, dword ptr [rdi + 0xb0]
0x00274BC4: mov rdx, qword ptr [rdi + 0xa8]
0x00274BCB: mov rcx, qword ptr [rdi + 8]
0x00274BCF: call 0x1402c7e90
0x00274BD4: test eax, eax
0x00274BD6: jle 0x140274bdb
0x00274BD8: movsxd rsi, eax
0x00274BDB: mov rax, qword ptr [rdi + 0xb0]
0x00274BE2: lea rdx, [rbp + 0x17]
0x00274BE6: movzx r8d, byte ptr [rbp + 0x77]
0x00274BEB: cmp rax, rsi
0x00274BEE: mov r9, r14
0x00274BF1: mov rcx, r15
0x00274BF4: cmovb rsi, rax
```

### `0x00274D53` score 4 base `rdi`

```asm
0x00274D29: mov qword ptr [rsp + 0x28], rcx
0x00274D2E: lea rdx, [rip - 0x2c2a5]
0x00274D35: mov rcx, rdi
0x00274D38: mov qword ptr [rsp + 0x20], r15
0x00274D3D: mov r9, rax
0x00274D40: call 0x1402537c0
0x00274D45: cmp eax, -2
0x00274D48: je 0x140274db2
0x00274D4A: cmp eax, -1
0x00274D4D: jne 0x140274ea2
0x00274D53: mov r8d, dword ptr [rdi + 0xb0]
0x00274D5A: mov rdx, qword ptr [rdi + 0xa8]
0x00274D61: mov rcx, qword ptr [rdi + 8]
0x00274D65: call 0x1402c7e90
0x00274D6A: movsxd rcx, eax
0x00274D6D: test eax, eax
0x00274D6F: jg 0x140274d74
0x00274D71: mov rcx, rsi
0x00274D74: mov rax, qword ptr [rdi + 0xb0]
0x00274D7B: lea rdx, [rbp - 0x69]
0x00274D7F: cmp rax, rcx
0x00274D82: mov r9, r15
0x00274D85: movzx r8d, bl
0x00274D89: cmovb rcx, rax
```

### `0x00274EA7` score 4 base `rdi`

```asm
0x00274E80: movups xmmword ptr [rdi + 0xe0], xmm0
0x00274E87: cmp dword ptr [r15], esi
0x00274E8A: je 0x140274ca0
0x00274E90: mov rdx, r15
0x00274E93: mov rcx, rdi
0x00274E96: call 0x14024e8d0
0x00274E9B: xor eax, eax
0x00274E9D: jmp 0x140274f24
0x00274EA2: cmp eax, 1
0x00274EA5: jne 0x140274f15
0x00274EA7: mov r8d, dword ptr [rdi + 0xb0]
0x00274EAE: mov rdx, qword ptr [rdi + 0xa8]
0x00274EB5: mov rcx, qword ptr [rdi + 8]
0x00274EB9: call 0x1402c7e90
0x00274EBE: test eax, eax
0x00274EC0: jle 0x140274ec5
0x00274EC2: movsxd rsi, eax
0x00274EC5: mov rax, qword ptr [rdi + 0xb0]
0x00274ECC: lea rdx, [rbp - 0x69]
0x00274ED0: movzx r8d, byte ptr [rbp + 0x77]
0x00274ED5: cmp rax, rsi
0x00274ED8: mov r9, r15
0x00274EDB: mov rcx, r12
0x00274EDE: cmovb rsi, rax
```

### `0x00274FC5` score 4 base `rdi`

```asm
0x00274FA0: mov rcx, rdi
0x00274FA3: cmove rdx, r13
0x00274FA7: mov qword ptr [rsp + 0x20], r14
0x00274FAC: xor r9d, r9d
0x00274FAF: xor r8d, r8d
0x00274FB2: call 0x1402537c0
0x00274FB7: cmp eax, -2
0x00274FBA: je 0x140275024
0x00274FBC: cmp eax, -1
0x00274FBF: jne 0x140275102
0x00274FC5: mov r8d, dword ptr [rdi + 0xb0]
0x00274FCC: mov rdx, qword ptr [rdi + 0xa8]
0x00274FD3: mov rcx, qword ptr [rdi + 8]
0x00274FD7: call 0x1402c7e90
0x00274FDC: movsxd rcx, eax
0x00274FDF: test eax, eax
0x00274FE1: jg 0x140274fe6
0x00274FE3: mov rcx, rsi
0x00274FE6: mov rax, qword ptr [rdi + 0xb0]
0x00274FED: lea rdx, [rbp + 0x17]
0x00274FF1: cmp rax, rcx
0x00274FF4: mov r9, r14
0x00274FF7: movzx r8d, bl
0x00274FFB: cmovb rcx, rax
```

### `0x00275107` score 4 base `rdi`

```asm
0x002750E1: sub r8, rdx
0x002750E4: mov qword ptr [rbp - 0x19], rcx
0x002750E8: mov qword ptr [rbp - 0x11], r8
0x002750EC: movups xmm0, xmmword ptr [rbp - 0x19]
0x002750F0: movups xmmword ptr [rdi + 0xe0], xmm0
0x002750F7: cmp dword ptr [r14], esi
0x002750FA: je 0x140274f90
0x00275100: jmp 0x14027515f
0x00275102: cmp eax, 1
0x00275105: jne 0x14027515f
0x00275107: mov r8d, dword ptr [rdi + 0xb0]
0x0027510E: mov rdx, qword ptr [rdi + 0xa8]
0x00275115: mov rcx, qword ptr [rdi + 8]
0x00275119: call 0x1402c7e90
0x0027511E: test eax, eax
0x00275120: jle 0x140275125
0x00275122: movsxd rsi, eax
0x00275125: mov rax, qword ptr [rdi + 0xb0]
0x0027512C: lea rdx, [rbp + 0x17]
0x00275130: movzx r8d, byte ptr [rbp + 0x6f]
0x00275135: cmp rax, rsi
0x00275138: mov r9, r14
0x0027513B: mov rcx, r15
0x0027513E: cmovb rsi, rax
```

### `0x002850BB` score 4 base `rbx`

```asm
0x00285094: sub r8, rcx
0x00285097: mov edx, 0xaa
0x0028509C: call 0x1403d3050
0x002850A1: mov edx, esi
0x002850A3: mov rbx, rsi
0x002850A6: mov rcx, qword ptr [rip + 0x5635c3]
0x002850AD: test rcx, rcx
0x002850B0: je 0x1402855cd
0x002850B6: test rbx, rbx
0x002850B9: je 0x1402850c9
0x002850BB: mov eax, dword ptr [rbx + 0xb0]
0x002850C1: cmp dword ptr [rcx + 0xb0], eax
0x002850C7: jle 0x1402850cc
0x002850C9: mov rbx, rcx
0x002850CC: inc edx
0x002850CE: mov rcx, qword ptr [rcx + 0x9e0]
0x002850D5: test rcx, rcx
0x002850D8: jne 0x1402850b6
0x002850DA: cmp edx, 1
0x002850DD: jle 0x1402855cd
0x002850E3: test rbx, rbx
0x002850E6: je 0x1402855cd
0x002850EC: mov qword ptr [rip + 0x56357d], rbx
0x002850F3: mov qword ptr [rbx + 0x9e0], rsi
```

### `0x002850C1` score 4 base `rcx`

```asm
0x00285097: mov edx, 0xaa
0x0028509C: call 0x1403d3050
0x002850A1: mov edx, esi
0x002850A3: mov rbx, rsi
0x002850A6: mov rcx, qword ptr [rip + 0x5635c3]
0x002850AD: test rcx, rcx
0x002850B0: je 0x1402855cd
0x002850B6: test rbx, rbx
0x002850B9: je 0x1402850c9
0x002850BB: mov eax, dword ptr [rbx + 0xb0]
0x002850C1: cmp dword ptr [rcx + 0xb0], eax
0x002850C7: jle 0x1402850cc
0x002850C9: mov rbx, rcx
0x002850CC: inc edx
0x002850CE: mov rcx, qword ptr [rcx + 0x9e0]
0x002850D5: test rcx, rcx
0x002850D8: jne 0x1402850b6
0x002850DA: cmp edx, 1
0x002850DD: jle 0x1402855cd
0x002850E3: test rbx, rbx
0x002850E6: je 0x1402855cd
0x002850EC: mov qword ptr [rip + 0x56357d], rbx
0x002850F3: mov qword ptr [rbx + 0x9e0], rsi
0x002850FA: cmp qword ptr [rbx + 0xa0], rcx
```

### `0x002D871B` score 4 base `rbx`

```asm
0x002D86F5: xor eax, eax
0x002D86F7: add rsp, 0x30
0x002D86FB: pop rbx
0x002D86FC: ret
0x002D86FD: mov r9d, 0x86
0x002D8703: mov qword ptr [rsp + 0x40], rdi
0x002D8708: lea r8, [rip + 0x4d3c31]
0x002D870F: lea edx, [r9 - 0x68]
0x002D8713: lea ecx, [rdx - 0x15]
0x002D8716: call 0x1402c1f60
0x002D871B: cmp dword ptr [rbx + 0xb0], 0
0x002D8722: mov edi, 1
0x002D8727: jne 0x1402d873d
0x002D8729: mov rax, qword ptr [rbx + 0x70]
0x002D872D: test rax, rax
0x002D8730: je 0x1402d873d
0x002D8732: mov rcx, rbx
0x002D8735: call rax
0x002D8737: mov edi, eax
0x002D8739: test eax, eax
0x002D873B: je 0x1402d8749
0x002D873D: inc dword ptr [rbx + 0xac]
0x002D8743: inc dword ptr [rbx + 0xb0]
0x002D8749: mov r9d, 0x88
```

### `0x002D884F` score 4 base `rcx`

```asm
0x002D883A: int3
0x002D883B: int3
0x002D883C: int3
0x002D883D: int3
0x002D883E: int3
0x002D883F: int3
0x002D8840: push rbx
0x002D8842: mov eax, 0x20
0x002D8847: call 0x1403b2500
0x002D884C: sub rsp, rax
0x002D884F: cmp dword ptr [rcx + 0xb0], 0
0x002D8856: mov rbx, rcx
0x002D8859: mov eax, 1
0x002D885E: jne 0x1402d886f
0x002D8860: mov rdx, qword ptr [rcx + 0x70]
0x002D8864: test rdx, rdx
0x002D8867: je 0x1402d886f
0x002D8869: call rdx
0x002D886B: test eax, eax
0x002D886D: je 0x1402d887b
0x002D886F: inc dword ptr [rbx + 0xac]
0x002D8875: inc dword ptr [rbx + 0xb0]
0x002D887B: add rsp, 0x20
0x002D887F: pop rbx
```

### `0x002E23BF` score 4 base `rbx`

```asm
0x002E2392: lea ecx, [rax - 0x1a]
0x002E2395: lea r8d, [rax + 3]
0x002E2399: call 0x1402c3c30
0x002E239E: xor eax, eax
0x002E23A0: jmp 0x1402e248b
0x002E23A5: mov edx, 0x1e
0x002E23AA: lea r8, [rip + 0x4ccabf]
0x002E23B1: mov r9d, 0xab
0x002E23B7: lea ecx, [rdx - 0x15]
0x002E23BA: call 0x1402c1f60
0x002E23BF: cmp dword ptr [rbx + 0xb0], 0
0x002E23C6: mov edx, 0x1e
0x002E23CB: lea ecx, [rdx - 0x14]
0x002E23CE: jne 0x1402e240b
0x002E23D0: mov r9d, 0xad
0x002E23D6: lea r8, [rip + 0x4ccab3]
0x002E23DD: call 0x1402c1f60
0x002E23E2: mov edx, 0xc2
0x002E23E7: mov dword ptr [rsp + 0x20], 0xaf
0x002E23EF: lea r9, [rip + 0x4ccaba]
0x002E23F6: mov ecx, 0x26
0x002E23FB: lea r8d, [rdx - 0x4d]
0x002E23FF: call 0x1402c3c30
0x002E2404: xor eax, eax
```

### `0x00305A53` score 4 base `rcx`

```asm
0x00305A36: je 0x140305a4d
0x00305A38: mov eax, r9d
0x00305A3B: movzx r11d, r9w
0x00305A3F: shr eax, 0x10
0x00305A42: sub r11d, eax
0x00305A45: mov eax, r11d
0x00305A48: shr eax, 0x10
0x00305A4B: jmp 0x140305a53
0x00305A4D: mov r11d, edx
0x00305A50: sub r11d, ebx
0x00305A53: mov ebx, dword ptr [rcx + 0xb0]
0x00305A59: sub r11d, eax
0x00305A5C: add edi, dword ptr [rcx + 0xa8]
0x00305A62: mov r9d, ebx
0x00305A65: add r8d, dword ptr [rcx + 0xac]
0x00305A6C: movzx eax, r10w
0x00305A70: imul r9d, eax
0x00305A74: test r9d, r9d
0x00305A77: je 0x140305a8e
0x00305A79: mov eax, r9d
0x00305A7C: movzx r10d, r9w
0x00305A80: shr eax, 0x10
0x00305A83: sub r10d, eax
0x00305A86: mov eax, r10d
```

### `0x0032C723` score 4 base `rbx`

```asm
0x0032C701: jmp 0x14032c77e
0x0032C706: cmp dword ptr [rdi + 0x18], ebx
0x0032C709: jne 0x14032c6fd
0x0032C70B: mov rcx, qword ptr [rdi + 8]
0x0032C70F: xor edx, edx
0x0032C711: call 0x1402c7510
0x0032C716: mov rbx, rax
0x0032C719: mov esi, 1
0x0032C71E: test rax, rax
0x0032C721: je 0x14032c77e
0x0032C723: cmp dword ptr [rbx + 0xb0], 0
0x0032C72A: jg 0x14032c735
0x0032C72C: test byte ptr [rip + 0x4bf955], 1
0x0032C733: jne 0x14032c741
0x0032C735: mov rcx, rbx
0x0032C738: call 0x1402d8840
0x0032C73D: test eax, eax
0x0032C73F: jne 0x14032c758
0x0032C741: mov rcx, qword ptr [rdi + 8]
0x0032C745: mov edx, esi
0x0032C747: call 0x1402c7510
0x0032C74C: inc esi
0x0032C74E: mov rbx, rax
0x0032C751: test rax, rax
```

### `0x0038B114` score 4 base `rdx`

```asm
0x0038B0F8: add rsp, 0x20
0x0038B0FC: pop rbx
0x0038B0FD: ret
0x0038B0FE: int3
0x0038B0FF: int3
0x0038B100: mov qword ptr [rsp + 8], rbx
0x0038B105: mov qword ptr [rsp + 0x10], rbp
0x0038B10A: mov qword ptr [rsp + 0x18], rsi
0x0038B10F: push rdi
0x0038B110: sub rsp, 0x20
0x0038B114: cmp dword ptr [rdx + 0xb0], 0
0x0038B11B: lea rdi, [rdx + 0xb8]
0x0038B122: mov rbp, r8
0x0038B125: mov rbx, rdx
0x0038B128: mov rsi, rcx
0x0038B12B: jne 0x14038b1a6
0x0038B12D: xor edx, edx
0x0038B12F: mov rcx, rdi
0x0038B132: lea r8d, [rdx + 0x58]
0x0038B136: call 0x1403d3050
0x0038B13B: lea rax, [rip + 0x69e]
0x0038B142: mov r8d, 0x58
0x0038B148: mov qword ptr [rdi + 0x30], rax
0x0038B14C: lea rdx, [rip + 0x37b249]
```

### `0x0038B1EF` score 4 base `rdx`

```asm
0x0038B1D2: push rsi
0x0038B1D3: push rdi
0x0038B1D4: push r12
0x0038B1D6: push r14
0x0038B1D8: sub rsp, 0x20
0x0038B1DC: xor r12d, r12d
0x0038B1DF: lea rdi, [rdx + 0xb8]
0x0038B1E6: mov rbx, r8
0x0038B1E9: mov rsi, rdx
0x0038B1EC: mov r14, rcx
0x0038B1EF: cmp dword ptr [rdx + 0xb0], r12d
0x0038B1F6: jne 0x14038b2d2
0x0038B1FC: xor edx, edx
0x0038B1FE: lea r8d, [r12 + 0x58]
0x0038B203: mov rcx, rdi
0x0038B206: call 0x1403d3050
0x0038B20B: lea rax, [rip + 0x5ce]
0x0038B212: mov qword ptr [rdi + 0x30], rax
0x0038B216: lea rax, [rip - 0x20b2d]
0x0038B21D: mov qword ptr [rdi + 0x38], rax
0x0038B221: call 0x14038d440
0x0038B226: mov ecx, r12d
0x0038B229: lea r8, [rip + 0x37b178]
0x0038B230: movzx edx, byte ptr [rax + rcx]
```

### `0x0038B2D2` score 4 base `rsi`

```asm
0x0038B2AB: pop rsi
0x0038B2AC: pop rbx
0x0038B2AD: ret
0x0038B2AE: mov dword ptr [rsi + 0xb0], 4
0x0038B2B8: jmp 0x14038b2d2
0x0038B2BA: mov edx, 0xfffffff1
0x0038B2BF: call 0x14038ec70
0x0038B2C4: test eax, eax
0x0038B2C6: jne 0x14038b268
0x0038B2C8: mov dword ptr [rsi + 0xb0], 1
0x0038B2D2: mov ecx, dword ptr [rsi + 0xb0]
0x0038B2D8: cmp ecx, 4
0x0038B2DB: jne 0x14038b2fd
0x0038B2DD: mov rax, qword ptr [rsi + 0x68]
0x0038B2E1: mov rdx, rsi
0x0038B2E4: mov rcx, r14
0x0038B2E7: mov qword ptr [rdi], rax
0x0038B2EA: mov dword ptr [rdi + 8], ebx
0x0038B2ED: add rsp, 0x20
0x0038B2F1: pop r14
0x0038B2F3: pop r12
0x0038B2F5: pop rdi
0x0038B2F6: pop rsi
0x0038B2F7: pop rbx
```

### `0x003B74DB` score 4 base `rbx`

```asm
0x003B74AD: cmp qword ptr [rcx + 0x98], rdi
0x003B74B4: je 0x1403b7679
0x003B74BA: mov rbx, qword ptr [rcx + 0x98]
0x003B74C1: test rbx, rbx
0x003B74C4: je 0x1403b74cc
0x003B74C6: mov rbx, qword ptr [rbx + 0x30]
0x003B74CA: jmp 0x1403b74cf
0x003B74CC: mov rbx, rdi
0x003B74CF: mov ecx, dword ptr [rbx + 0xec]
0x003B74D5: mov edx, dword ptr [rbx + 0xe8]
0x003B74DB: add edx, dword ptr [rbx + 0xb0]
0x003B74E1: cmp ecx, edx
0x003B74E3: mov eax, edx
0x003B74E5: cmovb eax, ecx
0x003B74E8: cmp dword ptr [rbx + 0xd0], eax
0x003B74EE: jb 0x1403b74fc
0x003B74F0: cmp dword ptr [rbx + 0xd8], edi
0x003B74F6: jbe 0x1403b763a
0x003B74FC: cmp ecx, edx
0x003B74FE: cmovb edx, ecx
0x003B7501: mov rcx, rbx
0x003B7504: call 0x1403c3fa4
0x003B7509: mov ecx, dword ptr [rbx + 0xe8]
0x003B750F: mov r13d, eax
```

### `0x003B7520` score 4 base `rbx`

```asm
0x003B74F6: jbe 0x1403b763a
0x003B74FC: cmp ecx, edx
0x003B74FE: cmovb edx, ecx
0x003B7501: mov rcx, rbx
0x003B7504: call 0x1403c3fa4
0x003B7509: mov ecx, dword ptr [rbx + 0xe8]
0x003B750F: mov r13d, eax
0x003B7512: sub r13d, dword ptr [rbx + 0xd0]
0x003B7519: mov r15d, edi
0x003B751C: mov rax, qword ptr [rbx + 0x20]
0x003B7520: mov edx, dword ptr [rbx + 0xb0]
0x003B7526: mov r9d, dword ptr [r14 + 0x1c]
0x003B752A: add edx, ecx
0x003B752C: mov r12, qword ptr [rbx + 0x28]
0x003B7530: mov qword ptr [rsp + 0x68], rax
0x003B7535: mov eax, dword ptr [rbx + 0xec]
0x003B753B: cmp eax, edx
0x003B753D: cmovb edx, eax
0x003B7540: cmp edx, dword ptr [r14 + 0x20]
0x003B7544: setne cl
0x003B7547: test r9d, r9d
0x003B754A: je 0x1403b763a
0x003B7550: test r13d, r13d
0x003B7553: setne al
```

### `0x003B763A` score 4 base `rbx`

```asm
0x003B7617: mov rcx, rbx
0x003B761A: call 0x1403c5050
0x003B761F: inc ebp
0x003B7621: cmp ebp, dword ptr [rsi + 8]
0x003B7624: jb 0x1403b75d8
0x003B7626: mov r9d, dword ptr [r14 + 0x1c]
0x003B762A: inc r15d
0x003B762D: mov cl, byte ptr [rsp + 0x60]
0x003B7631: cmp r15d, r9d
0x003B7634: jb 0x1403b7550
0x003B763A: mov eax, dword ptr [rbx + 0xb0]
0x003B7640: cmp dword ptr [rbx + 0xb4], eax
0x003B7646: jne 0x1403b7652
0x003B7648: xor edx, edx
0x003B764A: mov rcx, r14
0x003B764D: call 0x1403ba9e0
0x003B7652: mov ecx, dword ptr [rbx + 0xec]
0x003B7658: mov r8d, dword ptr [rbx + 0xe8]
0x003B765F: add r8d, dword ptr [rbx + 0xb0]
0x003B7666: cmp ecx, r8d
0x003B7669: cmovb r8d, ecx
0x003B766D: cmp dword ptr [rbx + 0xd0], r8d
0x003B7674: sete al
0x003B7677: jmp 0x1403b767b
```

### `0x003B765F` score 4 base `rbx`

```asm
0x003B7631: cmp r15d, r9d
0x003B7634: jb 0x1403b7550
0x003B763A: mov eax, dword ptr [rbx + 0xb0]
0x003B7640: cmp dword ptr [rbx + 0xb4], eax
0x003B7646: jne 0x1403b7652
0x003B7648: xor edx, edx
0x003B764A: mov rcx, r14
0x003B764D: call 0x1403ba9e0
0x003B7652: mov ecx, dword ptr [rbx + 0xec]
0x003B7658: mov r8d, dword ptr [rbx + 0xe8]
0x003B765F: add r8d, dword ptr [rbx + 0xb0]
0x003B7666: cmp ecx, r8d
0x003B7669: cmovb r8d, ecx
0x003B766D: cmp dword ptr [rbx + 0xd0], r8d
0x003B7674: sete al
0x003B7677: jmp 0x1403b767b
0x003B7679: mov al, 1
0x003B767B: mov rbx, qword ptr [rsp + 0x70]
0x003B7680: add rsp, 0x20
0x003B7684: pop r15
0x003B7686: pop r14
0x003B7688: pop r13
0x003B768A: pop r12
0x003B768C: pop rdi
```

### `0x003B8CDF` score 4 base `rcx`

```asm
0x003B8CB9: mov rdi, rcx
0x003B8CBC: cmp dword ptr [rcx + 0xc], ebx
0x003B8CBF: jbe 0x1403b8cf9
0x003B8CC1: mov rax, qword ptr [rdi + 0x78]
0x003B8CC5: mov rsi, qword ptr [rax + rbx*8]
0x003B8CC9: cmp byte ptr [rsi + 0x21], 1
0x003B8CCD: jne 0x1403b8cf2
0x003B8CCF: mov rcx, qword ptr [rsi + 0x10]
0x003B8CD3: mov eax, dword ptr [rcx + 0xec]
0x003B8CD9: mov edx, dword ptr [rcx + 0xe8]
0x003B8CDF: add edx, dword ptr [rcx + 0xb0]
0x003B8CE5: cmp eax, edx
0x003B8CE7: cmovb edx, eax
0x003B8CEA: call 0x1403c3fa4
0x003B8CEF: mov dword ptr [rsi + 0x24], eax
0x003B8CF2: inc ebx
0x003B8CF4: cmp ebx, dword ptr [rdi + 0xc]
0x003B8CF7: jb 0x1403b8cc1
0x003B8CF9: mov rbx, qword ptr [rsp + 0x30]
0x003B8CFE: mov rsi, qword ptr [rsp + 0x38]
0x003B8D03: add rsp, 0x20
0x003B8D07: pop rdi
0x003B8D08: ret
0x003B8D09: int3
```

### `0x003B9342` score 4 base `rbx`

```asm
0x003B9327: add eax, r9d
0x003B932A: cmp esi, eax
0x003B932C: jae 0x1403b9333
0x003B932E: mov r15d, esi
0x003B9331: jmp 0x1403b9342
0x003B9333: cmp ecx, edx
0x003B9335: mov r15d, edx
0x003B9338: cmova r15d, ecx
0x003B933C: inc r15d
0x003B933F: add r15d, r9d
0x003B9342: mov r8d, dword ptr [rbx + 0xb0]
0x003B9349: add r8d, r9d
0x003B934C: cmp esi, r8d
0x003B934F: mov eax, r8d
0x003B9352: cmovb eax, esi
0x003B9355: inc eax
0x003B9357: cmp esi, eax
0x003B9359: jb 0x1403b9366
0x003B935B: cmp esi, r8d
0x003B935E: cmovb r8d, esi
0x003B9362: lea esi, [r8 + 1]
0x003B9366: test r12b, r12b
0x003B9369: je 0x1403b9375
0x003B936B: mov r9b, byte ptr [rsp + 0x88]
```

### `0x003B93AB` score 4 base `rbx`

```asm
0x003B9388: cmp eax, dword ptr [rbp + 0x20]
0x003B938B: setb sil
0x003B938F: xor r14d, r14d
0x003B9392: cmp r10d, r15d
0x003B9395: setb r14b
0x003B9399: jmp 0x1403b93c8
0x003B939B: mov edx, dword ptr [rbx + 0xe8]
0x003B93A1: sub ecx, edx
0x003B93A3: mov eax, dword ptr [rbx + 0xb4]
0x003B93A9: cmp ecx, eax
0x003B93AB: mov esi, dword ptr [rbx + 0xb0]
0x003B93B1: cmova eax, ecx
0x003B93B4: add esi, edx
0x003B93B6: lea r15d, [rdx + rax]
0x003B93BA: mov eax, dword ptr [rbx + 0xec]
0x003B93C0: cmp eax, esi
0x003B93C2: cmovb esi, eax
0x003B93C5: mov r14d, r15d
0x003B93C8: xor r13b, r13b
0x003B93CB: test esi, esi
0x003B93CD: je 0x1403b948c
0x003B93D3: mov r8b, r9b
0x003B93D6: mov rdx, rbx
0x003B93D9: mov rcx, rbp
```

### `0x003B9D50` score 4 base `rdx`

```asm
0x003B9D25: test r8b, r8b
0x003B9D28: jne 0x1403b9c78
0x003B9D2E: test edi, edi
0x003B9D30: je 0x1403b9e38
0x003B9D36: mov r9, rbx
0x003B9D39: mov r10, r15
0x003B9D3C: mov r14, qword ptr [r9]
0x003B9D3F: mov rdx, qword ptr [r14 + 0x10]
0x003B9D43: mov ecx, dword ptr [rdx + 0xec]
0x003B9D49: mov r11d, dword ptr [rdx + 0xe8]
0x003B9D50: add r11d, dword ptr [rdx + 0xb0]
0x003B9D57: cmp ecx, r11d
0x003B9D5A: mov eax, r11d
0x003B9D5D: cmovb eax, ecx
0x003B9D60: cmp dword ptr [r14 + 4], eax
0x003B9D64: jbe 0x1403b9daf
0x003B9D66: movsd xmm1, qword ptr [r14 + 0x20]
0x003B9D6C: xorps xmm0, xmm0
0x003B9D6F: xorps xmm2, xmm2
0x003B9D72: cmp ecx, r11d
0x003B9D75: mov r8b, 1
0x003B9D78: cmovb r11d, ecx
0x003B9D7C: mov eax, r11d
0x003B9D7F: cvtsi2sd xmm2, rax
```

### `0x003BA257` score 4 base `rdi`

```asm
0x003BA231: xor bpl, bpl
0x003BA234: lea rbx, [rcx + 0x30]
0x003BA238: mov qword ptr [rax + 8], rbx
0x003BA23C: mov rcx, rbx
0x003BA23F: call 0x1403b36c8
0x003BA244: nop
0x003BA245: mov rdi, qword ptr [rsi + 0x20]
0x003BA249: mov rcx, rsi
0x003BA24C: call 0x1403c2f94
0x003BA251: mov ecx, dword ptr [rdi + 0xe8]
0x003BA257: add ecx, dword ptr [rdi + 0xb0]
0x003BA25D: mov eax, dword ptr [rdi + 0xec]
0x003BA263: cmp eax, ecx
0x003BA265: cmovb ecx, eax
0x003BA268: cmp dword ptr [rdi + 0xd0], ecx
0x003BA26E: jae 0x1403ba28c
0x003BA270: mov edi, 1
0x003BA275: cmp dword ptr [r14 + 0xc], edi
0x003BA279: jne 0x1403ba28c
0x003BA27B: mov rcx, r14
0x003BA27E: call 0x1403b7494
0x003BA283: movzx ebp, bpl
0x003BA287: test al, al
0x003BA289: cmove ebp, edi
```

### `0x003BAAF0` score 4 base `rbx`

```asm
0x003BAAC5: jbe 0x1403bab81
0x003BAACB: mov rsi, qword ptr [rsp + 0x68]
0x003BAAD0: mov rbx, qword ptr [rdi + 0x98]
0x003BAAD7: lea rax, [r14 + r14*2]
0x003BAADB: shl rax, 4
0x003BAADF: add rax, qword ptr [rcx + 0x30]
0x003BAAE3: test rbx, rbx
0x003BAAE6: mov r13d, dword ptr [rax + 0x20]
0x003BAAEA: mov r15d, dword ptr [rax + 0x1c]
0x003BAAEE: jmp 0x1403bab5a
0x003BAAF0: mov eax, dword ptr [rbx + 0xb0]
0x003BAAF6: cmp dword ptr [rbx + 0xb4], eax
0x003BAAFC: jne 0x1403bab53
0x003BAAFE: mov rax, qword ptr [rbx + 0x20]
0x003BAB02: lea rcx, [r14 + r14*8]
0x003BAB06: mov rax, qword ptr [rax + rbp + 0x38]
0x003BAB0B: lea rdx, [rax + rcx*8]
0x003BAB0F: cmp dword ptr [rdx + 0x34], 0
0x003BAB13: jbe 0x1403bab53
0x003BAB15: cmp rbx, rsi
0x003BAB18: jne 0x1403bab28
0x003BAB1A: mov rcx, rbx
0x003BAB1D: cmp r15d, dword ptr [rdx + 0x2c]
0x003BAB21: jbe 0x1403bab4b
```

### `0x003BAC6B` score 4 base `rdi`

```asm
0x003BAC42: lea r8d, [rdx + 0x30]
0x003BAC46: call 0x1403d3050
0x003BAC4B: mov r9, rbx
0x003BAC4E: mov r8, rdi
0x003BAC51: mov edx, r14d
0x003BAC54: mov rcx, rsi
0x003BAC57: call 0x1403b94cc
0x003BAC5C: mov eax, dword ptr [rdi + 0xec]
0x003BAC62: xorps xmm0, xmm0
0x003BAC65: mov edx, dword ptr [rdi + 0xe8]
0x003BAC6B: add edx, dword ptr [rdi + 0xb0]
0x003BAC71: cmp eax, edx
0x003BAC73: mov ecx, r14d
0x003BAC76: cmovb edx, eax
0x003BAC79: inc r14d
0x003BAC7C: mov eax, edx
0x003BAC7E: cvtsi2sd xmm0, rax
0x003BAC83: movsd qword ptr [rbx + 0x20], xmm0
0x003BAC88: mov rax, qword ptr [rsi + 0x78]
0x003BAC8C: mov qword ptr [rax + rcx*8], rbx
0x003BAC90: cmp rdi, qword ptr [rsi + 0x98]
0x003BAC97: je 0x1403bac9f
0x003BAC99: mov rdi, qword ptr [rdi + 0x30]
0x003BAC9D: jmp 0x1403baca1
```

### `0x003BAD7F` score 4 base `rsi`

```asm
0x003BAD60: cmp dword ptr [r9 + rax*8], 4
0x003BAD65: jne 0x1403bad6f
0x003BAD67: mov rax, qword ptr [r9 + rax*8 + 0x20]
0x003BAD6C: add dword ptr [rax], r11d
0x003BAD6F: inc r8d
0x003BAD72: cmp r8d, dword ptr [rcx + 8]
0x003BAD76: jb 0x1403bad58
0x003BAD78: inc edx
0x003BAD7A: cmp edx, dword ptr [rdi + 0x1c]
0x003BAD7D: jb 0x1403bad40
0x003BAD7F: mov eax, dword ptr [rsi + 0xb0]
0x003BAD85: cmp dword ptr [rsi + 0xb4], eax
0x003BAD8B: jne 0x1403bad91
0x003BAD8D: add dword ptr [rdi + 0x14], r11d
0x003BAD91: add dword ptr [rdi + 0xc], r11d
0x003BAD95: cmp dword ptr [rdi + 0xc], 1
0x003BAD99: jne 0x1403bada5
0x003BAD9B: mov dword ptr [rdi + 0x2c], 0
0x003BADA2: mov bpl, 1
0x003BADA5: lea rcx, [rdi + 0x30]
0x003BADA9: call 0x1403b38d4
0x003BADAE: nop
0x003BADAF: test bpl, bpl
0x003BADB2: je 0x1403badbe
```

### `0x003C0A23` score 4 base `rcx`

```asm
0x003C0A07: mov qword ptr [r11 + 0x10], rbx
0x003C0A0B: mov qword ptr [r11 + 0x18], rsi
0x003C0A0F: mov qword ptr [r11 + 8], rcx
0x003C0A13: push rdi
0x003C0A14: push r12
0x003C0A16: push r13
0x003C0A18: push r14
0x003C0A1A: push r15
0x003C0A1C: sub rsp, 0x50
0x003C0A20: mov rbx, rcx
0x003C0A23: mov eax, dword ptr [rcx + 0xb0]
0x003C0A29: test eax, eax
0x003C0A2B: je 0x1403c0a51
0x003C0A2D: and dword ptr [rsp + 0x40], 0
0x003C0A32: lea rax, [rip - 0xa935]
0x003C0A39: mov qword ptr [r11 - 0x30], rax
0x003C0A3D: lea rcx, [rsp + 0x38]
0x003C0A42: call 0x1403b39ac
0x003C0A47: mov eax, dword ptr [rbx + 0xb0]
0x003C0A4D: test eax, eax
0x003C0A4F: jne 0x1403c0a3d
0x003C0A51: cmp dword ptr [rbx + 0xd4], 0
0x003C0A58: jle 0x1403c0a62
0x003C0A5A: mov rcx, rbx
```

### `0x003C0A47` score 4 base `rbx`

```asm
0x003C0A1C: sub rsp, 0x50
0x003C0A20: mov rbx, rcx
0x003C0A23: mov eax, dword ptr [rcx + 0xb0]
0x003C0A29: test eax, eax
0x003C0A2B: je 0x1403c0a51
0x003C0A2D: and dword ptr [rsp + 0x40], 0
0x003C0A32: lea rax, [rip - 0xa935]
0x003C0A39: mov qword ptr [r11 - 0x30], rax
0x003C0A3D: lea rcx, [rsp + 0x38]
0x003C0A42: call 0x1403b39ac
0x003C0A47: mov eax, dword ptr [rbx + 0xb0]
0x003C0A4D: test eax, eax
0x003C0A4F: jne 0x1403c0a3d
0x003C0A51: cmp dword ptr [rbx + 0xd4], 0
0x003C0A58: jle 0x1403c0a62
0x003C0A5A: mov rcx, rbx
0x003C0A5D: call 0x1403c0888
0x003C0A62: cmp qword ptr [rbx + 0x90], 0
0x003C0A6A: jne 0x1403c0a7d
0x003C0A6C: lea rcx, [rbx + 0x98]
0x003C0A73: call 0x1403b3868
0x003C0A78: jmp 0x1403c0bcd
0x003C0A7D: xor dil, dil
0x003C0A80: test dil, dil
```

### `0x003C10DE` score 4 base `rdi`

```asm
0x003C10B1: mov qword ptr [rsp + 0x10], rsi
0x003C10B6: push rdi
0x003C10B7: sub rsp, 0x20
0x003C10BB: mov rdi, qword ptr [rcx + 0x40]
0x003C10BF: mov rsi, rcx
0x003C10C2: test rdi, rdi
0x003C10C5: je 0x1403c1154
0x003C10CB: and qword ptr [rcx + 0x40], 0
0x003C10D0: lea rbx, [rdi + 0xe0]
0x003C10D7: mov r8d, dword ptr [rdi + 0xb4]
0x003C10DE: mov eax, dword ptr [rdi + 0xb0]
0x003C10E4: cmp r8d, eax
0x003C10E7: jle 0x1403c110f
0x003C10E9: mov rcx, rbx
0x003C10EC: call 0x1403b6028
0x003C10F1: and qword ptr [rdi + 0xa8], 0
0x003C10F9: mov rcx, rbx
0x003C10FC: call 0x1403b60b8
0x003C1101: mov rcx, qword ptr [rsi + 0x30]
0x003C1105: mov rdx, rdi
0x003C1108: call 0x1403cb314
0x003C110D: jmp 0x1403c1154
0x003C110F: mov eax, dword ptr [rbx]
0x003C1111: test eax, eax
```
