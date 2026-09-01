# NVIDIA big-slot dynamic-call profile

## function `0x001E8A10..0x001E9930`

| callsite | slot RVA | instruction |
|---|---|---|
| `0x001E8B20` | `0x007E7AC0` | `call qword ptr [rip + 0x5fef9a]` |
| `0x001E8D8C` | `0x007E7AC8` | `call qword ptr [rip + 0x5fed36]` |

## function `0x001E2FE0..0x001E3E34`

| callsite | slot RVA | instruction |
|---|---|---|
| `0x001E30B8` | `0x007E7AC0` | `call qword ptr [rip + 0x604a02]` |
| `0x001E3393` | `0x007E7AC8` | `call qword ptr [rip + 0x60472f]` |

## function `0x001E5160..0x001E6C7D`

| callsite | slot RVA | instruction |
|---|---|---|
| `0x001E5202` | `0x007E7A70` | `call qword ptr [rip + 0x602868]` |
| `0x001E59FD` | `0x007E7A98` | `call qword ptr [rip + 0x602095]` |
| `0x001E5CA8` | `0x007E7AA0` | `call qword ptr [rip + 0x601df2]` |
| `0x001E5CC9` | `0x007E7A98` | `call qword ptr [rip + 0x601dc9]` |

## slot `0x007E7A70`

used by: 0x001E5202

### references / candidate writers

```asm
0x001D7611: mov eax, r9d
0x001D7614: div r10d
0x001D7617: mov dword ptr [rbx + 0x14], eax
0x001D761A: cmp dword ptr [rip + 0x60f0f7], 1
0x001D7621: je 0x1401d7888
0x001D7627: mov qword ptr [rsp + 0x9b0], rsi
0x001D762F: mov rsi, qword ptr [rdi + 0xd0]
0x001D7636: test rsi, rsi
0x001D7639: je 0x1401d77f6
0x001D763F: mov qword ptr [rsp + 0x970], r14
0x001D7647: mov r14, qword ptr [rip + 0x610422]
0x001D764E: test r14, r14
0x001D7651: je 0x1401d76ae
0x001D7653: xor edx, edx
0x001D7655: lea rcx, [rsp + 0x50]
0x001D765A: mov r8d, 0x108
0x001D7660: call 0x1403d3050
0x001D7665: and dword ptr [rsp + 0x54], 0xfffffff0
0x001D766A: lea rdx, [rsp + 0x50]
0x001D766F: mov rcx, rsi
0x001D7672: mov dword ptr [rsp + 0x50], 0x20108
0x001D767A: call r14
```

```asm
0x001E51C8: mov r8d, 0x108
0x001E51CE: lea rcx, [rbp + 0x390]
0x001E51D5: call 0x1403d3050
0x001E51DA: mov dword ptr [rbp + 0x390], 0x20108
0x001E51E4: mov eax, dword ptr [rbp + 0x394]
0x001E51EA: and eax, 0xff000001
0x001E51EF: or eax, 1
0x001E51F2: mov dword ptr [rbp + 0x394], eax
0x001E51F8: lea rdx, [rbp + 0x390]
0x001E51FF: mov rcx, rdi
0x001E5202: call qword ptr [rip + 0x602868]
0x001E5208: mov dword ptr [rsp + 0x28], eax
0x001E520C: test eax, eax
0x001E520E: je 0x1401e553e
0x001E5214: mov dword ptr [rsp + 0x48], 0x671
0x001E521C: mov dword ptr [rbp + 0x290], 0x67
0x001E5226: mov dword ptr [rbp + 0x294], 4
0x001E5230: mov eax, dword ptr [rbp + 0x294]
0x001E5236: xor eax, 0x29
0x001E5239: mov byte ptr [rbp + 0x298], al
0x001E523F: movsx ecx, byte ptr [rbp + 0x298]
0x001E5246: xor ecx, 0x31
```

```asm
0x001E6CE8: mov r8d, 0x108
0x001E6CEE: lea rcx, [rbp + 0x3a0]
0x001E6CF5: call 0x1403d3050
0x001E6CFA: mov dword ptr [rbp + 0x3a0], 0x20108
0x001E6D04: mov eax, dword ptr [rbp + 0x3a4]
0x001E6D0A: and eax, 0xff000001
0x001E6D0F: or eax, 1
0x001E6D12: mov dword ptr [rbp + 0x3a4], eax
0x001E6D18: lea rdx, [rbp + 0x3a0]
0x001E6D1F: mov rcx, rdi
0x001E6D22: call qword ptr [rip + 0x600d48]
0x001E6D28: mov dword ptr [rsp + 0x28], eax
0x001E6D2C: test eax, eax
0x001E6D2E: je 0x1401e705e
0x001E6D34: mov dword ptr [rsp + 0x48], 0x743
0x001E6D3C: mov dword ptr [rbp + 0x2d0], 0x36
0x001E6D46: mov dword ptr [rbp + 0x2d4], 0x2c
0x001E6D50: mov eax, dword ptr [rbp + 0x2d4]
0x001E6D56: xor eax, 0x78
0x001E6D59: mov byte ptr [rbp + 0x2d8], al
0x001E6D5F: movsx ecx, byte ptr [rbp + 0x2d8]
0x001E6D66: xor ecx, 0x60
```

```asm
0x001FE54B: test rax, rax
0x001FE54E: je 0x1401fe296
0x001FE554: mov ecx, 0xe3640a56
0x001FE559: call qword ptr [rip + 0x5e9499]
0x001FE55F: mov qword ptr [rip + 0x5e9502], rax
0x001FE566: test rax, rax
0x001FE569: je 0x1401fe296
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
```

## slot `0x007E7A98`

used by: 0x001E59FD, 0x001E5CC9

### references / candidate writers

```asm
0x001E0F07: mov rbx, qword ptr [rcx + 0xd0]
0x001E0F0E: test rbx, rbx
0x001E0F11: je 0x1401e1f3e
0x001E0F17: xor edx, edx
0x001E0F19: mov r8d, 0x1cf8
0x001E0F1F: lea rcx, [rbp + 0x4d0]
0x001E0F26: call 0x1403d3050
0x001E0F2B: mov dword ptr [rbp + 0x4d0], 0x31cf8
0x001E0F35: lea rdx, [rbp + 0x4d0]
0x001E0F3C: mov rcx, rbx
0x001E0F3F: call qword ptr [rip + 0x606b53]
0x001E0F45: mov dword ptr [rsp + 0x20], eax
0x001E0F49: test eax, eax
0x001E0F4B: jne 0x1401e1f3e
0x001E0F51: xor r14d, r14d
0x001E0F54: mov ebx, r14d
0x001E0F57: mov r8d, dword ptr [rbp + 0x4d8]
0x001E0F5E: test r8d, r8d
0x001E0F61: je 0x1401e1a7a
0x001E0F67: nop word ptr [rax + rax]
0x001E0F70: mov eax, ebx
0x001E0F72: imul rcx, rax, 0x1c8
```

```asm
0x001E117E: mov dword ptr [rbp + 0x2214], eax
0x001E1184: mov dword ptr [rbp + 0x21f8], r14d
0x001E118B: lea rdx, [rbp + 0x21d0]
0x001E1192: mov rcx, qword ptr [rsi + 0xd0]
0x001E1199: call qword ptr [rip + 0x606901]
0x001E119F: mov dword ptr [rsp + 0x20], eax
0x001E11A3: cmp eax, -1
0x001E11A6: jne 0x1401e128f
0x001E11AC: lea rdx, [rbp + 0x4d0]
0x001E11B3: mov rcx, qword ptr [rsi + 0xd0]
0x001E11BA: call qword ptr [rip + 0x6068d8]
0x001E11C0: test eax, eax
0x001E11C2: jne 0x1401e1515
0x001E11C8: mov edx, r14d
0x001E11CB: mov r10d, dword ptr [rbp + 0x4d8]
0x001E11D2: test r10d, r10d
0x001E11D5: je 0x1401e1515
0x001E11DB: nop dword ptr [rax + rax]
0x001E11E0: mov eax, edx
0x001E11E2: imul rcx, rax, 0x1c8
0x001E11E9: lea r8, [rbp + 0x4e4]
0x001E11F0: add r8, rcx
```

```asm
0x001E1FB7: mov rbx, qword ptr [rcx + 0xd0]
0x001E1FBE: test rbx, rbx
0x001E1FC1: je 0x1401e2fb2
0x001E1FC7: xor edx, edx
0x001E1FC9: mov r8d, 0x1cf8
0x001E1FCF: lea rcx, [rbp + 0x4e0]
0x001E1FD6: call 0x1403d3050
0x001E1FDB: mov dword ptr [rbp + 0x4e0], 0x31cf8
0x001E1FE5: lea rdx, [rbp + 0x4e0]
0x001E1FEC: mov rcx, rbx
0x001E1FEF: call qword ptr [rip + 0x605aa3]
0x001E1FF5: mov dword ptr [rsp + 0x20], eax
0x001E1FF9: test eax, eax
0x001E1FFB: jne 0x1401e2fb2
0x001E2001: xor r14d, r14d
0x001E2004: mov ebx, r14d
0x001E2007: mov r8d, dword ptr [rbp + 0x4e8]
0x001E200E: test r8d, r8d
0x001E2011: je 0x1401e2ae3
0x001E2017: nop word ptr [rax + rax]
0x001E2020: mov eax, ebx
0x001E2022: imul rcx, rax, 0x1c8
```

```asm
0x001E222E: mov dword ptr [rbp + 0x2224], eax
0x001E2234: mov dword ptr [rbp + 0x2208], r14d
0x001E223B: lea rdx, [rbp + 0x21e0]
0x001E2242: mov rcx, qword ptr [rsi + 0xd0]
0x001E2249: call qword ptr [rip + 0x605851]
0x001E224F: mov dword ptr [rsp + 0x20], eax
0x001E2253: cmp eax, -1
0x001E2256: jne 0x1401e2340
0x001E225C: lea rdx, [rbp + 0x4e0]
0x001E2263: mov rcx, qword ptr [rsi + 0xd0]
0x001E226A: call qword ptr [rip + 0x605828]
0x001E2270: test eax, eax
0x001E2272: jne 0x1401e2770
0x001E2278: mov edx, r14d
0x001E227B: mov r10d, dword ptr [rbp + 0x4e8]
0x001E2282: test r10d, r10d
0x001E2285: je 0x1401e2770
0x001E228B: nop dword ptr [rax + rax]
0x001E2290: mov eax, edx
0x001E2292: imul rcx, rax, 0x1c8
0x001E2299: lea r8, [rbp + 0x4f4]
0x001E22A0: add r8, rcx
```

```asm
0x001E59C4: mov rcx, rax
0x001E59C7: call 0x1403b20d4
0x001E59CC: jmp 0x1401e6c57
0x001E59D1: xor edx, edx
0x001E59D3: mov r8d, 0x1cf8
0x001E59D9: lea rcx, [rbp + 0x6d0]
0x001E59E0: call 0x1403d3050
0x001E59E5: mov dword ptr [rbp + 0x6d0], 0x31cf8
0x001E59EF: lea rdx, [rbp + 0x6d0]
0x001E59F6: mov rcx, qword ptr [rsi + 0xd0]
0x001E59FD: call qword ptr [rip + 0x602095]
0x001E5A03: mov dword ptr [rsp + 0x20], eax
0x001E5A07: test eax, eax
0x001E5A09: jne 0x1401e6c57
0x001E5A0F: mov ebx, r15d
0x001E5A12: mov r8d, dword ptr [rbp + 0x6d8]
0x001E5A19: test r8d, r8d
0x001E5A1C: je 0x1401e6627
0x001E5A22: nop dword ptr [rax]
0x001E5A26: nop word ptr [rax + rax]
0x001E5A30: mov eax, ebx
0x001E5A32: imul rcx, rax, 0x1c8
```

```asm
0x001E5C8E: mov dword ptr [rbp + 0x2414], eax
0x001E5C94: mov dword ptr [rbp + 0x23f8], ebx
0x001E5C9A: lea rdx, [rbp + 0x23d0]
0x001E5CA1: mov rcx, qword ptr [rsi + 0xd0]
0x001E5CA8: call qword ptr [rip + 0x601df2]
0x001E5CAE: mov dword ptr [rsp + 0x20], eax
0x001E5CB2: cmp eax, -1
0x001E5CB5: jne 0x1401e5da0
0x001E5CBB: lea rdx, [rbp + 0x6d0]
0x001E5CC2: mov rcx, qword ptr [rsi + 0xd0]
0x001E5CC9: call qword ptr [rip + 0x601dc9]
0x001E5CCF: test eax, eax
0x001E5CD1: jne 0x1401e602b
0x001E5CD7: mov r8d, r15d
0x001E5CDA: mov r10d, dword ptr [rbp + 0x6d8]
0x001E5CE1: test r10d, r10d
0x001E5CE4: je 0x1401e602b
0x001E5CEA: nop word ptr [rax + rax]
0x001E5CF0: mov eax, r8d
0x001E5CF3: imul rcx, rax, 0x1c8
0x001E5CFA: lea r9, [rbp + 0x6e4]
0x001E5D01: add r9, rcx
```

```asm
0x001E77A0: jmp 0x1401e89e4
0x001E77A5: cmp byte ptr [rbp + 0x4190], r15b
0x001E77AC: jne 0x1401e89e4
0x001E77B2: xor edx, edx
0x001E77B4: mov r8d, 0x1cf8
0x001E77BA: lea rcx, [rbp + 0x6e0]
0x001E77C1: call 0x1403d3050
0x001E77C6: mov dword ptr [rbp + 0x6e0], 0x31cf8
0x001E77D0: lea rdx, [rbp + 0x6e0]
0x001E77D7: mov rcx, qword ptr [rsi + 0xd0]
0x001E77DE: call qword ptr [rip + 0x6002b4]
0x001E77E4: mov dword ptr [rsp + 0x20], eax
0x001E77E8: test eax, eax
0x001E77EA: jne 0x1401e89e4
0x001E77F0: mov ebx, r15d
0x001E77F3: mov r8d, dword ptr [rbp + 0x6e8]
0x001E77FA: test r8d, r8d
0x001E77FD: je 0x1401e83b4
0x001E7803: nop dword ptr [rax]
0x001E7807: nop word ptr [rax + rax]
0x001E7810: mov eax, ebx
0x001E7812: imul rcx, rax, 0x1c8
```

```asm
0x001E7A6E: mov dword ptr [rbp + 0x2424], eax
0x001E7A74: mov dword ptr [rbp + 0x2408], ebx
0x001E7A7A: lea rdx, [rbp + 0x23e0]
0x001E7A81: mov rcx, qword ptr [rsi + 0xd0]
0x001E7A88: call qword ptr [rip + 0x600012]
0x001E7A8E: mov dword ptr [rsp + 0x20], eax
0x001E7A92: cmp eax, -1
0x001E7A95: jne 0x1401e7b81
0x001E7A9B: lea rdx, [rbp + 0x6e0]
0x001E7AA2: mov rcx, qword ptr [rsi + 0xd0]
0x001E7AA9: call qword ptr [rip + 0x5fffe9]
0x001E7AAF: test eax, eax
0x001E7AB1: jne 0x1401e7fac
0x001E7AB7: mov r8d, r15d
0x001E7ABA: mov r10d, dword ptr [rbp + 0x6e8]
0x001E7AC1: test r10d, r10d
0x001E7AC4: je 0x1401e7fac
0x001E7ACA: nop word ptr [rax + rax]
0x001E7AD0: mov eax, r8d
0x001E7AD3: imul rcx, rax, 0x1c8
0x001E7ADA: lea r9, [rbp + 0x6f4]
0x001E7AE1: add r9, rcx
```

```asm
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
```

## slot `0x007E7AA0`

used by: 0x001E5CA8

### references / candidate writers

```asm
0x001E1159: movups xmmword ptr [rbp + 0x21ec], xmm0
0x001E1160: movups xmm1, xmmword ptr [r9 + 0x18]
0x001E1165: movups xmmword ptr [rbp + 0x21fc], xmm1
0x001E116C: movsd xmm0, qword ptr [r9 + 0x28]
0x001E1172: movsd qword ptr [rbp + 0x220c], xmm0
0x001E117A: mov eax, dword ptr [r9 + 0x30]
0x001E117E: mov dword ptr [rbp + 0x2214], eax
0x001E1184: mov dword ptr [rbp + 0x21f8], r14d
0x001E118B: lea rdx, [rbp + 0x21d0]
0x001E1192: mov rcx, qword ptr [rsi + 0xd0]
0x001E1199: call qword ptr [rip + 0x606901]
0x001E119F: mov dword ptr [rsp + 0x20], eax
0x001E11A3: cmp eax, -1
0x001E11A6: jne 0x1401e128f
0x001E11AC: lea rdx, [rbp + 0x4d0]
0x001E11B3: mov rcx, qword ptr [rsi + 0xd0]
0x001E11BA: call qword ptr [rip + 0x6068d8]
0x001E11C0: test eax, eax
0x001E11C2: jne 0x1401e1515
0x001E11C8: mov edx, r14d
0x001E11CB: mov r10d, dword ptr [rbp + 0x4d8]
0x001E11D2: test r10d, r10d
```

```asm
0x001E2209: movups xmmword ptr [rbp + 0x21fc], xmm0
0x001E2210: movups xmm1, xmmword ptr [r9 + 0x18]
0x001E2215: movups xmmword ptr [rbp + 0x220c], xmm1
0x001E221C: movsd xmm0, qword ptr [r9 + 0x28]
0x001E2222: movsd qword ptr [rbp + 0x221c], xmm0
0x001E222A: mov eax, dword ptr [r9 + 0x30]
0x001E222E: mov dword ptr [rbp + 0x2224], eax
0x001E2234: mov dword ptr [rbp + 0x2208], r14d
0x001E223B: lea rdx, [rbp + 0x21e0]
0x001E2242: mov rcx, qword ptr [rsi + 0xd0]
0x001E2249: call qword ptr [rip + 0x605851]
0x001E224F: mov dword ptr [rsp + 0x20], eax
0x001E2253: cmp eax, -1
0x001E2256: jne 0x1401e2340
0x001E225C: lea rdx, [rbp + 0x4e0]
0x001E2263: mov rcx, qword ptr [rsi + 0xd0]
0x001E226A: call qword ptr [rip + 0x605828]
0x001E2270: test eax, eax
0x001E2272: jne 0x1401e2770
0x001E2278: mov edx, r14d
0x001E227B: mov r10d, dword ptr [rbp + 0x4e8]
0x001E2282: test r10d, r10d
```

```asm
0x001E5C69: movups xmmword ptr [rbp + 0x23ec], xmm0
0x001E5C70: movups xmm1, xmmword ptr [r10 + 0x18]
0x001E5C75: movups xmmword ptr [rbp + 0x23fc], xmm1
0x001E5C7C: movsd xmm0, qword ptr [r10 + 0x28]
0x001E5C82: movsd qword ptr [rbp + 0x240c], xmm0
0x001E5C8A: mov eax, dword ptr [r10 + 0x30]
0x001E5C8E: mov dword ptr [rbp + 0x2414], eax
0x001E5C94: mov dword ptr [rbp + 0x23f8], ebx
0x001E5C9A: lea rdx, [rbp + 0x23d0]
0x001E5CA1: mov rcx, qword ptr [rsi + 0xd0]
0x001E5CA8: call qword ptr [rip + 0x601df2]
0x001E5CAE: mov dword ptr [rsp + 0x20], eax
0x001E5CB2: cmp eax, -1
0x001E5CB5: jne 0x1401e5da0
0x001E5CBB: lea rdx, [rbp + 0x6d0]
0x001E5CC2: mov rcx, qword ptr [rsi + 0xd0]
0x001E5CC9: call qword ptr [rip + 0x601dc9]
0x001E5CCF: test eax, eax
0x001E5CD1: jne 0x1401e602b
0x001E5CD7: mov r8d, r15d
0x001E5CDA: mov r10d, dword ptr [rbp + 0x6d8]
0x001E5CE1: test r10d, r10d
```

```asm
0x001E7A49: movups xmmword ptr [rbp + 0x23fc], xmm0
0x001E7A50: movups xmm1, xmmword ptr [r10 + 0x18]
0x001E7A55: movups xmmword ptr [rbp + 0x240c], xmm1
0x001E7A5C: movsd xmm0, qword ptr [r10 + 0x28]
0x001E7A62: movsd qword ptr [rbp + 0x241c], xmm0
0x001E7A6A: mov eax, dword ptr [r10 + 0x30]
0x001E7A6E: mov dword ptr [rbp + 0x2424], eax
0x001E7A74: mov dword ptr [rbp + 0x2408], ebx
0x001E7A7A: lea rdx, [rbp + 0x23e0]
0x001E7A81: mov rcx, qword ptr [rsi + 0xd0]
0x001E7A88: call qword ptr [rip + 0x600012]
0x001E7A8E: mov dword ptr [rsp + 0x20], eax
0x001E7A92: cmp eax, -1
0x001E7A95: jne 0x1401e7b81
0x001E7A9B: lea rdx, [rbp + 0x6e0]
0x001E7AA2: mov rcx, qword ptr [rsi + 0xd0]
0x001E7AA9: call qword ptr [rip + 0x5fffe9]
0x001E7AAF: test eax, eax
0x001E7AB1: jne 0x1401e7fac
0x001E7AB7: mov r8d, r15d
0x001E7ABA: mov r10d, dword ptr [rbp + 0x6e8]
0x001E7AC1: test r10d, r10d
```

```asm
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
```

## slot `0x007E7AC0`

used by: 0x001E8B20, 0x001E30B8

### references / candidate writers

```asm
0x001E2FF2: mov qword ptr [rsp + 0x40], 0xfffffffffffffffe
0x001E2FFB: mov qword ptr [rax + 0x10], rbx
0x001E2FFF: mov qword ptr [rax + 0x18], rsi
0x001E3003: mov qword ptr [rax + 0x20], rdi
0x001E3007: mov rax, qword ptr [rip + 0x5f38e2]
0x001E300E: xor rax, rsp
0x001E3011: mov qword ptr [rbp + 0x150], rax
0x001E3018: mov rbx, rcx
0x001E301B: cmp qword ptr [rcx + 0xd0], 0
0x001E3023: je 0x1401e3e0c
0x001E3029: cmp qword ptr [rip + 0x604a8f], 0
0x001E3031: je 0x1401e3e04
0x001E3037: cmp qword ptr [rip + 0x604a89], 0
0x001E303F: je 0x1401e3e04
0x001E3045: cmp qword ptr [rip + 0x604a6b], 0
0x001E304D: je 0x1401e3e04
0x001E3053: xor esi, esi
0x001E3055: mov edi, esi
0x001E3057: mov dword ptr [rsp + 0x20], esi
0x001E305B: call 0x1401ed0b0
0x001E3060: mov dword ptr [rbp + 0xa0], 0x10048
0x001E306A: xor eax, eax
```

```asm
0x001E3073: mov qword ptr [rbp + 0xac], rax
0x001E307A: mov qword ptr [rbp + 0xb4], rax
0x001E3081: mov qword ptr [rbp + 0xbc], rax
0x001E3088: mov qword ptr [rbp + 0xc4], rax
0x001E308F: mov qword ptr [rbp + 0xcc], rax
0x001E3096: mov qword ptr [rbp + 0xd4], rax
0x001E309D: mov qword ptr [rbp + 0xdc], rax
0x001E30A4: mov dword ptr [rbp + 0xe4], eax
0x001E30AA: lea rdx, [rbp + 0xa0]
0x001E30B1: mov rcx, qword ptr [rbx + 0xd0]
0x001E30B8: call qword ptr [rip + 0x604a02]
0x001E30BE: mov dword ptr [rsp + 0x24], eax
0x001E30C2: test eax, eax
0x001E30C4: je 0x1401e3363
0x001E30CA: mov dword ptr [rsp + 0x28], 0x5e6
0x001E30D2: mov dword ptr [rbp + 0x20], 0x1d
0x001E30D9: mov eax, dword ptr [rbp + 0x20]
0x001E30DC: xor eax, 0x4e
0x001E30DF: add eax, 0xb
0x001E30E2: mov byte ptr [rbp + 0x24], al
0x001E30E5: movsx ecx, byte ptr [rbp + 0x24]
0x001E30E9: xor ecx, 0x56
```

```asm
0x001E8A39: mov qword ptr [rbp + 0x140], rax
0x001E8A40: mov esi, r8d
0x001E8A43: mov rdi, rcx
0x001E8A46: cmp qword ptr [rcx + 0xd0], 0
0x001E8A4E: jne 0x1401e8a62
0x001E8A50: xor eax, eax
0x001E8A52: mov ecx, 2
0x001E8A57: test r8d, r8d
0x001E8A5A: cmovg eax, ecx
0x001E8A5D: jmp 0x1401e9913
0x001E8A62: cmp qword ptr [rip + 0x5ff056], 0
0x001E8A6A: je 0x1401e98f8
0x001E8A70: cmp qword ptr [rip + 0x5ff050], 0
0x001E8A78: je 0x1401e98f8
0x001E8A7E: cmp qword ptr [rip + 0x5ff032], 0
0x001E8A86: je 0x1401e98f8
0x001E8A8C: xor eax, eax
0x001E8A8E: mov dword ptr [rsp + 0x24], eax
0x001E8A92: lea eax, [rdx + 0x64]
0x001E8A95: imul ebx, eax, 0x3e8
0x001E8A9B: mov dword ptr [rsp + 0x20], ebx
0x001E8A9F: call 0x1401ed0b0
```

```asm
0x001E8AE1: mov qword ptr [rbp + 0x7c], rax
0x001E8AE5: mov qword ptr [rbp + 0x84], rax
0x001E8AEC: mov qword ptr [rbp + 0x8c], rax
0x001E8AF3: mov qword ptr [rbp + 0x94], rax
0x001E8AFA: mov qword ptr [rbp + 0x9c], rax
0x001E8B01: mov qword ptr [rbp + 0xa4], rax
0x001E8B08: mov qword ptr [rbp + 0xac], rax
0x001E8B0F: mov dword ptr [rbp + 0xb4], eax
0x001E8B15: lea rdx, [rbp + 0x70]
0x001E8B19: mov rcx, qword ptr [rdi + 0xd0]
0x001E8B20: call qword ptr [rip + 0x5fef9a]
0x001E8B26: mov dword ptr [rsp + 0x28], eax
0x001E8B2A: test eax, eax
0x001E8B2C: je 0x1401e8d55
0x001E8B32: mov dword ptr [rsp + 0x2c], 0x5b5
0x001E8B3A: mov dword ptr [rbp + 0x40], 0x18
0x001E8B41: mov dword ptr [rbp + 0x44], 0x38
0x001E8B48: mov eax, dword ptr [rbp + 0x44]
0x001E8B4B: xor eax, 0x56
0x001E8B4E: mov byte ptr [rbp + 0x48], al
0x001E8B51: movsx ecx, byte ptr [rbp + 0x48]
0x001E8B55: xor ecx, 0x4e
```

```asm
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
```

## slot `0x007E7AC8`

used by: 0x001E8D8C, 0x001E3393

### references / candidate writers

```asm
0x001E2FFF: mov qword ptr [rax + 0x18], rsi
0x001E3003: mov qword ptr [rax + 0x20], rdi
0x001E3007: mov rax, qword ptr [rip + 0x5f38e2]
0x001E300E: xor rax, rsp
0x001E3011: mov qword ptr [rbp + 0x150], rax
0x001E3018: mov rbx, rcx
0x001E301B: cmp qword ptr [rcx + 0xd0], 0
0x001E3023: je 0x1401e3e0c
0x001E3029: cmp qword ptr [rip + 0x604a8f], 0
0x001E3031: je 0x1401e3e04
0x001E3037: cmp qword ptr [rip + 0x604a89], 0
0x001E303F: je 0x1401e3e04
0x001E3045: cmp qword ptr [rip + 0x604a6b], 0
0x001E304D: je 0x1401e3e04
0x001E3053: xor esi, esi
0x001E3055: mov edi, esi
0x001E3057: mov dword ptr [rsp + 0x20], esi
0x001E305B: call 0x1401ed0b0
0x001E3060: mov dword ptr [rbp + 0xa0], 0x10048
0x001E306A: xor eax, eax
0x001E306C: mov qword ptr [rbp + 0xa4], rax
0x001E3073: mov qword ptr [rbp + 0xac], rax
```

```asm
0x001E335F: mov dword ptr [rsp + 0x20], edi
0x001E3363: test edi, edi
0x001E3365: jne 0x1401e351f
0x001E336B: cmp dword ptr [rbp + 0xa4], edi
0x001E3371: jbe 0x1401e33a7
0x001E3373: mov esi, dword ptr [rbp + 0xb0]
0x001E3379: mov eax, dword ptr [rbx + 0x140]
0x001E337F: mov dword ptr [rbp + 0xb0], eax
0x001E3385: lea rdx, [rbp + 0xa0]
0x001E338C: mov rcx, qword ptr [rbx + 0xd0]
0x001E3393: call qword ptr [rip + 0x60472f]
0x001E3399: mov edi, eax
0x001E339B: mov dword ptr [rsp + 0x20], eax
0x001E339F: test eax, eax
0x001E33A1: jne 0x1401e351f
0x001E33A7: mov eax, 0x10624dd3
0x001E33AC: imul dword ptr [rbx + 0x140]
0x001E33B2: sar edx, 6
0x001E33B5: mov eax, edx
0x001E33B7: shr eax, 0x1f
0x001E33BA: add edx, eax
0x001E33BC: mov dword ptr [rsp + 0x2c], edx
```

```asm
0x001E8A43: mov rdi, rcx
0x001E8A46: cmp qword ptr [rcx + 0xd0], 0
0x001E8A4E: jne 0x1401e8a62
0x001E8A50: xor eax, eax
0x001E8A52: mov ecx, 2
0x001E8A57: test r8d, r8d
0x001E8A5A: cmovg eax, ecx
0x001E8A5D: jmp 0x1401e9913
0x001E8A62: cmp qword ptr [rip + 0x5ff056], 0
0x001E8A6A: je 0x1401e98f8
0x001E8A70: cmp qword ptr [rip + 0x5ff050], 0
0x001E8A78: je 0x1401e98f8
0x001E8A7E: cmp qword ptr [rip + 0x5ff032], 0
0x001E8A86: je 0x1401e98f8
0x001E8A8C: xor eax, eax
0x001E8A8E: mov dword ptr [rsp + 0x24], eax
0x001E8A92: lea eax, [rdx + 0x64]
0x001E8A95: imul ebx, eax, 0x3e8
0x001E8A9B: mov dword ptr [rsp + 0x20], ebx
0x001E8A9F: call 0x1401ed0b0
0x001E8AA4: lea rax, [rdi + 0x13c]
0x001E8AAB: lea rcx, [rsp + 0x20]
```

```asm
0x001E8D61: mov r14d, dword ptr [rbp + 0x80]
0x001E8D68: sub eax, r14d
0x001E8D6B: cdq
0x001E8D6C: xor eax, edx
0x001E8D6E: sub eax, edx
0x001E8D70: cmp eax, 0x3e8
0x001E8D75: jl 0x1401e98f8
0x001E8D7B: mov dword ptr [rbp + 0x80], ebx
0x001E8D81: lea rdx, [rbp + 0x70]
0x001E8D85: mov rcx, qword ptr [rdi + 0xd0]
0x001E8D8C: call qword ptr [rip + 0x5fed36]
0x001E8D92: mov dword ptr [rsp + 0x24], eax
0x001E8D96: test eax, eax
0x001E8D98: jne 0x1401e8f4c
0x001E8D9E: mov eax, 0x10624dd3
0x001E8DA3: imul ebx
0x001E8DA5: sar edx, 6
0x001E8DA8: mov eax, edx
0x001E8DAA: shr eax, 0x1f
0x001E8DAD: add edx, eax
0x001E8DAF: mov dword ptr [rsp + 0x30], edx
0x001E8DB3: mov dword ptr [rbp + 0x20], 0x74
```

```asm
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
```
