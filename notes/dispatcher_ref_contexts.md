# Dispatcher 0x584A0 reference contexts

## ref `0x00080066` PDATA `0x0007F0F0..0x000831BB`

```asm
0x0007FF85: add al, 0xf
0x0007FF87: xor eax, ecx
0x0007FF89: xor eax, 0x6e
0x0007FF8C: mov byte ptr [rsp + 0x58f], al
0x0007FF93: movsx ecx, byte ptr [rsp + 0x58f]
0x0007FF9B: mov eax, dword ptr [rsp + 0x578]
0x0007FFA2: add al, 0x10
0x0007FFA4: xor eax, ecx
0x0007FFA6: xor eax, 0x69
0x0007FFA9: mov byte ptr [rsp + 0x590], al
0x0007FFB0: movsx ecx, byte ptr [rsp + 0x590]
0x0007FFB8: mov eax, dword ptr [rsp + 0x578]
0x0007FFBF: add al, 0x11
0x0007FFC1: xor eax, ecx
0x0007FFC3: xor eax, 0x6e
0x0007FFC6: mov byte ptr [rsp + 0x591], al
0x0007FFCD: movsx ecx, byte ptr [rsp + 0x591]
0x0007FFD5: mov eax, dword ptr [rsp + 0x578]
0x0007FFDC: add al, 0x12
0x0007FFDE: xor eax, ecx
0x0007FFE0: xor eax, 0x67
0x0007FFE3: mov byte ptr [rsp + 0x592], al
0x0007FFEA: xor eax, eax
0x0007FFEC: mov byte ptr [rsp + 0x593], al
0x0007FFF3: movzx eax, byte ptr [rsp + 0x580]
0x0007FFFB: lea rdx, [rsp + 0x710]
0x00080003: lea rcx, [rsp + 0x578]
0x0008000B: call 0x140056320
0x00080010: nop
0x00080011: cmp qword ptr [rax + 0x18], 0x10
0x00080016: jb 0x14008001b
0x00080018: mov rax, qword ptr [rax]
0x0008001B: mov rcx, rax
0x0008001E: call 0x140063150
0x00080023: nop
0x00080024: mov r8, qword ptr [rsp + 0x728]
0x0008002C: cmp r8, 0x10
0x00080030: jb 0x14008004a
0x00080032: inc r8
0x00080035: mov rdx, qword ptr [rsp + 0x710]
0x0008003D: lea rcx, [rsp + 0x710]
0x00080045: call 0x140046ab0
0x0008004A: mov qword ptr [rsp + 0x728], 0xf
0x00080056: mov qword ptr [rsp + 0x720], r15
0x0008005E: mov byte ptr [rsp + 0x710], 0
0x00080066: lea rcx, [rip - 0x27bcd]
0x0008006D: mov qword ptr [rsp + 0x180], rcx
0x00080075: mov qword ptr [rsp + 0x470], r15
0x0008007D: test rcx, rcx
0x00080080: je 0x1400800a9
0x00080082: lea rax, [rip + 0x3b84d7]
0x00080089: mov qword ptr [rsp + 0x438], rax
0x00080091: mov qword ptr [rsp + 0x440], rcx
0x00080099: lea rax, [rsp + 0x438]
0x000800A1: mov qword ptr [rsp + 0x470], rax
0x000800A9: lea r12, [rsi + 0x300]
0x000800B0: lea r8, [rsp + 0x438]
0x000800B8: mov rdx, rdi
0x000800BB: mov rcx, r12
0x000800BE: call 0x14013c190
0x000800C3: mov ecx, 0x198
0x000800C8: call 0x1403b2098
0x000800CD: mov qword ptr [rsp + 0x70], rax
0x000800D2: test rax, rax
0x000800D5: je 0x1400800fe
0x000800D7: movzx ecx, byte ptr [rsi + 0xfe]
0x000800DE: mov byte ptr [rsp + 0x20], cl
0x000800E2: movzx r9d, byte ptr [rsi + 0xfd]
0x000800EA: mov r8d, dword ptr [rsi + 0x1cc]
0x000800F1: mov rdx, r12
0x000800F4: mov rcx, rax
0x000800F7: call 0x140059030
0x000800FC: jmp 0x140080101
0x000800FE: mov rax, r15
0x00080101: mov rbx, qword ptr [rsi + 0x15a0]
0x00080108: mov qword ptr [rsi + 0x15a0], rax
0x0008010F: test rbx, rbx
0x00080112: je 0x140080129
0x00080114: mov rcx, rbx
0x00080117: call 0x140059280
0x0008011C: mov edx, 0x198
0x00080121: mov rcx, rbx
0x00080124: call 0x1403b20dc
0x00080129: movzx edx, byte ptr [rsi + 0xfc]
0x00080130: mov rcx, qword ptr [rsi + 0x15a0]
0x00080137: call 0x14005c510
0x0008013C: mov rcx, r12
0x0008013F: call 0x1401406d0
0x00080144: call 0x140391550
0x00080149: mov rbx, rax
0x0008014C: call 0x140391534
0x00080151: cqo
0x00080153: idiv rbx
0x00080156: imul rcx, rax, 0x3b9aca00
0x0008015D: imul rax, rdx, 0x3b9aca00
0x00080164: cqo
0x00080166: idiv rbx
0x00080169: add rax, rcx
0x0008016C: mov qword ptr [rsp + 0x188], rax
0x00080174: mov qword ptr [rsi + 0x12b0], rax
```

## ref `0x000A2F31` PDATA `0x000A2870..0x000A459E`

```asm
0x000A2E57: mov rcx, r15
0x000A2E5A: call 0x1400b20d0
0x000A2E5F: movzx eax, byte ptr [rsp + 0x42]
0x000A2E64: mov byte ptr [rsp + 0x70], al
0x000A2E68: mov dword ptr [rbp + 0x98], 0
0x000A2E72: mov dword ptr [rbp - 0x7c], 0
0x000A2E79: mov eax, dword ptr [rbp - 0x7c]
0x000A2E7C: mov dword ptr [rbp - 0x10], eax
0x000A2E7F: mov qword ptr [rbp - 8], rdi
0x000A2E83: mov qword ptr [rbp], rdi
0x000A2E87: xor r8d, r8d
0x000A2E8A: xor edx, edx
0x000A2E8C: lea rcx, [rbp - 8]
0x000A2E90: call 0x140068860
0x000A2E95: mov qword ptr [rbp - 8], rax
0x000A2E99: mov qword ptr [rbp + 8], rdi
0x000A2E9D: xorps xmm0, xmm0
0x000A2EA0: movdqa xmmword ptr [rbp + 0x10], xmm0
0x000A2EA5: movss xmm0, dword ptr [rip + 0x399e93]
0x000A2EAD: movss dword ptr [rbp - 0x10], xmm0
0x000A2EB2: mov edx, 0x10
0x000A2EB7: lea rcx, [rbp + 8]
0x000A2EBB: call 0x140069ef0
0x000A2EC0: mov rax, qword ptr [rbp - 8]
0x000A2EC4: mov qword ptr [rbp - 0x28], rax
0x000A2EC8: mov r8, qword ptr [rbp + 8]
0x000A2ECC: mov qword ptr [rbp + 0x10], r8
0x000A2ED0: mov qword ptr [rbp + 0xf8], r8
0x000A2ED7: lea rax, [rbp - 0x28]
0x000A2EDB: mov qword ptr [rsp + 0x20], rax
0x000A2EE0: mov r9d, 0x10
0x000A2EE6: lea rdx, [rbp + 0x100]
0x000A2EED: lea rcx, [rbp + 8]
0x000A2EF1: call 0x140069640
0x000A2EF6: mov qword ptr [rbp + 0x20], 7
0x000A2EFE: mov qword ptr [rbp + 0x28], 8
0x000A2F06: mov edx, 2
0x000A2F0B: lea rcx, [rbp + 0xb20]
0x000A2F12: call 0x140391a94
0x000A2F17: nop
0x000A2F18: xor r9d, r9d
0x000A2F1B: xor r8d, r8d
0x000A2F1E: lea rdx, [rbp + 0x490]
0x000A2F25: lea rcx, [rbp + 0xb70]
0x000A2F2C: call 0x14013fcc0
0x000A2F31: lea rcx, [rip - 0x4aa98]
0x000A2F38: mov qword ptr [rbp + 0x120], rcx
0x000A2F3F: mov qword ptr [rbp + 0x1e0], rdi
0x000A2F46: test rcx, rcx
0x000A2F49: je 0x1400a2f6e
0x000A2F4B: lea rax, [rip + 0x39560e]
0x000A2F52: mov qword ptr [rbp + 0x1a8], rax
0x000A2F59: mov qword ptr [rbp + 0x1b0], rcx
0x000A2F60: lea rax, [rbp + 0x1a8]
0x000A2F67: mov qword ptr [rbp + 0x1e0], rax
0x000A2F6E: lea r8, [rbp + 0x1a8]
0x000A2F75: lea rdx, [r15 + 0x2c0]
0x000A2F7C: lea rcx, [rbp + 0xb70]
0x000A2F83: call 0x14013c190
0x000A2F88: xor eax, eax
0x000A2F8A: mov byte ptr [rsp + 0x78], al
0x000A2F8E: mov byte ptr [rsp + 0x79], al
0x000A2F92: mov byte ptr [rsp + 0x7f], al
0x000A2F96: xor edx, edx
0x000A2F98: lea r8d, [rax + 0x60]
0x000A2F9C: lea rcx, [rbp + 0x560]
0x000A2FA3: call 0x1403d3050
0x000A2FA8: mov qword ptr [rbp + 0x5c0], rdi
0x000A2FAF: mov dword ptr [rbp + 0x5c8], 0xffffffff
0x000A2FB9: mov qword ptr [rbp + 0x5d0], rdi
0x000A2FC0: mov dword ptr [rbp + 0x5d8], edi
0x000A2FC6: mov qword ptr [rbp + 0x5e8], rdi
0x000A2FCD: xorps xmm0, xmm0
0x000A2FD0: movdqa xmmword ptr [rbp + 0x5f0], xmm0
0x000A2FD8: mov qword ptr [rbp + 0x608], rdi
0x000A2FDF: xorps xmm1, xmm1
0x000A2FE2: movdqa xmmword ptr [rbp + 0x610], xmm1
0x000A2FEA: xor eax, eax
0x000A2FEC: mov byte ptr [rsp + 0x7b], al
0x000A2FF0: mov qword ptr [rbp + 0x620], rax
0x000A2FF7: mov byte ptr [rsp + 0x7c], al
0x000A2FFB: mov byte ptr [rsp + 0x7d], al
0x000A2FFF: mov dword ptr [rbp + 0x628], eax
0x000A3005: mov dword ptr [rbp + 0x5e0], edi
0x000A300B: mov dword ptr [rbp + 0x600], edi
0x000A3011: lea rax, [rbp + 0x560]
0x000A3018: mov qword ptr [rsp + 0x20], rax
0x000A301D: lea r9, [rbp + 0x490]
0x000A3024: lea r8, [rbp + 0x820]
0x000A302B: movabs rdx, 0x8000000000000000
0x000A3035: mov rcx, r15
0x000A3038: call 0x1400b15a0
0x000A303D: mov dword ptr [r15 + 0x4f0], eax
0x000A3044: test eax, eax
0x000A3046: je 0x1400a3069
0x000A3048: mov dword ptr [rsp + 0x20], eax
0x000A304C: mov r9, r15
0x000A304F: lea r8, [rip + 0x83ea]
0x000A3056: lea rdx, [rbp + 0x560]
0x000A305D: lea rcx, [rbp + 0xb70]
```

## ref `0x000A4DCC` PDATA `0x000A45A0..0x000A71B9`

```asm
0x000A4D05: xor eax, eax
0x000A4D07: mov byte ptr [rbp - 0x75], al
0x000A4D0A: mov qword ptr [rbp + 0x4f0], rax
0x000A4D11: mov qword ptr [rbp + 0x4f8], rax
0x000A4D18: mov qword ptr [rbp + 0x500], rax
0x000A4D1F: mov qword ptr [rbp + 0x508], rax
0x000A4D26: mov rcx, qword ptr [rbp + 0xd8]
0x000A4D2D: test rcx, rcx
0x000A4D30: je 0x1400a4d93
0x000A4D32: mov rax, qword ptr [rbp + 0xe8]
0x000A4D39: sub rax, rcx
0x000A4D3C: cmp rax, 0x1000
0x000A4D42: jb 0x1400a4d7c
0x000A4D44: test cl, 0x1f
0x000A4D47: je 0x1400a4d4f
0x000A4D49: call 0x1403db020
0x000A4D4E: int3
0x000A4D4F: mov rax, qword ptr [rcx - 8]
0x000A4D53: cmp rax, rcx
0x000A4D56: jb 0x1400a4d5e
0x000A4D58: call 0x1403db020
0x000A4D5D: int3
0x000A4D5E: sub rcx, rax
0x000A4D61: cmp rcx, 8
0x000A4D65: jae 0x1400a4d6d
0x000A4D67: call 0x1403db020
0x000A4D6C: int3
0x000A4D6D: cmp rcx, 0x27
0x000A4D71: jbe 0x1400a4d79
0x000A4D73: call 0x1403db020
0x000A4D78: int3
0x000A4D79: mov rcx, rax
0x000A4D7C: call 0x1403b20d4
0x000A4D81: xorps xmm0, xmm0
0x000A4D84: movdqu xmmword ptr [rbp + 0xd8], xmm0
0x000A4D8C: mov qword ptr [rbp + 0xe8], r14
0x000A4D93: movups xmm0, xmmword ptr [rbp + 0x4f0]
0x000A4D9A: movaps xmmword ptr [rbp + 0x590], xmm0
0x000A4DA1: movups xmm1, xmmword ptr [rbp + 0x500]
0x000A4DA8: movaps xmmword ptr [rbp + 0x5a0], xmm1
0x000A4DAF: mov r9, r15
0x000A4DB2: lea r8, [rip + 0x7f67]
0x000A4DB9: lea rdx, [rbp + 0x570]
0x000A4DC0: lea rcx, [rbp + 0xbf0]
0x000A4DC7: call 0x14013fcc0
0x000A4DCC: lea rcx, [rip - 0x4c933]
0x000A4DD3: mov qword ptr [rbp + 0x120], rcx
0x000A4DDA: mov qword ptr [rbp + 0x180], r14
0x000A4DE1: test rcx, rcx
0x000A4DE4: je 0x1400a4e09
0x000A4DE6: lea rax, [rip + 0x393773]
0x000A4DED: mov qword ptr [rbp + 0x148], rax
0x000A4DF4: mov qword ptr [rbp + 0x150], rcx
0x000A4DFB: lea rax, [rbp + 0x148]
0x000A4E02: mov qword ptr [rbp + 0x180], rax
0x000A4E09: lea r8, [rbp + 0x148]
0x000A4E10: lea rdx, [r15 + 0x2c0]
0x000A4E17: lea rcx, [rbp + 0xbf0]
0x000A4E1E: call 0x14013c190
0x000A4E23: movabs rax, 0x3ffffffffffffff
0x000A4E2D: cmp rdi, rax
0x000A4E30: jbe 0x1400a4e3a
0x000A4E32: shl rdi, 6
0x000A4E36: mov qword ptr [rbp - 0x20], rdi
0x000A4E3A: xor eax, eax
0x000A4E3C: mov byte ptr [rbp - 0x74], al
0x000A4E3F: mov byte ptr [rbp - 0x73], al
0x000A4E42: mov byte ptr [rbp - 0x72], al
0x000A4E45: xor edx, edx
0x000A4E47: lea r8d, [rax + 0x60]
0x000A4E4B: lea rcx, [rbp + 0x640]
0x000A4E52: call 0x1403d3050
0x000A4E57: mov qword ptr [rbp + 0x6a0], r14
0x000A4E5E: mov dword ptr [rbp + 0x6a8], 0xffffffff
0x000A4E68: mov qword ptr [rbp + 0x6b0], r14
0x000A4E6F: mov dword ptr [rbp + 0x6b8], r14d
0x000A4E76: mov qword ptr [rbp + 0x6c8], r14
0x000A4E7D: xorps xmm0, xmm0
0x000A4E80: movdqa xmmword ptr [rbp + 0x6d0], xmm0
0x000A4E88: mov qword ptr [rbp + 0x6e8], r14
0x000A4E8F: xorps xmm1, xmm1
0x000A4E92: movdqa xmmword ptr [rbp + 0x6f0], xmm1
0x000A4E9A: xor eax, eax
0x000A4E9C: mov byte ptr [rbp - 0x71], al
0x000A4E9F: mov qword ptr [rbp + 0x700], rax
0x000A4EA6: mov byte ptr [rbp - 0x6a], al
0x000A4EA9: mov byte ptr [rsp + 0x50], al
0x000A4EAD: mov dword ptr [rbp + 0x708], eax
0x000A4EB3: mov dword ptr [rbp + 0x6c0], r14d
0x000A4EBA: mov dword ptr [rbp + 0x6e0], r14d
0x000A4EC1: lea rax, [rbp + 0x640]
0x000A4EC8: mov qword ptr [rsp + 0x20], rax
0x000A4ECD: lea r9, [rbp + 0x570]
0x000A4ED4: lea r8, [rbp + 0x8f0]
0x000A4EDB: mov rdx, rdi
0x000A4EDE: mov rcx, r15
0x000A4EE1: call 0x1400b15a0
0x000A4EE6: mov dword ptr [r15 + 0x4f0], eax
0x000A4EED: test eax, eax
0x000A4EEF: je 0x1400a4f12
```

## .rdata neighborhood `0x00734A70`

| RVA | u32 | interpreted RVA | u64 | interpreted VA |
|---|---|---|---|---|
| `0x007349F0` | `0x00007004` | `0x00007004` | `0x003B242800007004` | `` |
| `0x007349F4` | `0x003B2428` | `0x003B2428` | `0x004357B8003B2428` | `` |
| `0x007349F8` | `0x004357B8` | `0x004357B8` | `0x000000DA004357B8` | `` |
| `0x007349FC` | `0x000000DA` | `` | `0xFFFFFFFF000000DA` | `` |
| `0x00734A00` | `0xFFFFFFFF` | `` | `0x0040A3D0FFFFFFFF` | `` |
| `0x00734A04` | `0x0040A3D0` | `0x0040A3D0` | `0x000000000040A3D0` | `` |
| `0x00734A08` | `0x00000000` | `` | `0x0040A3DC00000000` | `` |
| `0x00734A0C` | `0x0040A3DC` | `0x0040A3DC` | `0x000000010040A3DC` | `` |
| `0x00734A10` | `0x00000001` | `` | `0x0040A3E800000001` | `` |
| `0x00734A14` | `0x0040A3E8` | `0x0040A3E8` | `0x00046FA00040A3E8` | `` |
| `0x00734A18` | `0x00046FA0` | `0x00046FA0` | `0xFFFFFFFF00046FA0` | `` |
| `0x00734A1C` | `0xFFFFFFFF` | `` | `0x00046FE0FFFFFFFF` | `` |
| `0x00734A20` | `0x00046FE0` | `0x00046FE0` | `0x0000000000046FE0` | `` |
| `0x00734A24` | `0x00000000` | `` | `0x0004702300000000` | `` |
| `0x00734A28` | `0x00047023` | `0x00047023` | `0x0000000100047023` | `` |
| `0x00734A2C` | `0x00000001` | `` | `0x0004705B00000001` | `` |
| `0x00734A30` | `0x0004705B` | `0x0004705B` | `0x000000020004705B` | `` |
| `0x00734A34` | `0x00000002` | `` | `0x0004706E00000002` | `` |
| `0x00734A38` | `0x0004706E` | `0x0004706E` | `0x000000000004706E` | `` |
| `0x00734A3C` | `0x00000000` | `` | `0x000470B000000000` | `` |
| `0x00734A40` | `0x000470B0` | `0x000470B0` | `0xFFFFFFFF000470B0` | `` |
| `0x00734A44` | `0xFFFFFFFF` | `` | `0x00031501FFFFFFFF` | `` |
| `0x00734A48` | `0x00031501` | `0x00031501` | `0x7011621500031501` | `` |
| `0x00734A4C` | `0x70116215` | `` | `0x0000301070116215` | `` |
| `0x00734A50` | `0x00003010` | `0x00003010` | `0x00041E1100003010` | `` |
| `0x00734A54` | `0x00041E11` | `0x00041E11` | `0x7012921600041E11` | `` |
| `0x00734A58` | `0x70129216` | `` | `0x3010601170129216` | `` |
| `0x00734A5C` | `0x30106011` | `` | `0x003D2ED430106011` | `` |
| `0x00734A60` | `0x003D2ED4` | `0x003D2ED4` | `0x00435EA0003D2ED4` | `` |
| `0x00734A64` | `0x00435EA0` | `0x00435EA0` | `0xFFFFFFFF00435EA0` | `` |
| `0x00734A68` | `0xFFFFFFFF` | `` | `0x0040B3F0FFFFFFFF` | `` |
| `0x00734A6C` | `0x0040B3F0` | `0x0040B3F0` | `0x000584A00040B3F0` | `` |
| `0x00734A70` **TARGET** | `0x000584A0` | `0x000584A0` | `0xFFFFFFFF000584A0` | `` |
| `0x00734A74` | `0xFFFFFFFF` | `` | `0x000584C1FFFFFFFF` | `` |
| `0x00734A78` | `0x000584C1` | `0x000584C1` | `0x00000000000584C1` | `` |
| `0x00734A7C` | `0x00000000` | `` | `0x0008211100000000` | `` |
| `0x00734A80` | `0x00082111` | `0x00082111` | `0x000E642100082111` | `` |
| `0x00734A84` | `0x000E6421` | `0x000E6421` | `0x000D341C000E6421` | `` |
| `0x00734A88` | `0x000D341C` | `0x000D341C` | `0xF00A720E000D341C` | `` |
| `0x00734A8C` | `0xF00A720E` | `` | `0x7006E008F00A720E` | `` |
| `0x00734A90` | `0x7006E008` | `` | `0x003D2ED47006E008` | `` |
| `0x00734A94` | `0x003D2ED4` | `0x003D2ED4` | `0x00435EC8003D2ED4` | `` |
| `0x00734A98` | `0x00435EC8` | `0x00435EC8` | `0xFFFFFFFF00435EC8` | `` |
| `0x00734A9C` | `0xFFFFFFFF` | `` | `0x0040B350FFFFFFFF` | `` |
| `0x00734AA0` | `0x0040B350` | `0x0040B350` | `0x000000000040B350` | `` |
| `0x00734AA4` | `0x00000000` | `` | `0x0040B36D00000000` | `` |
| `0x00734AA8` | `0x0040B36D` | `0x0040B36D` | `0x000000010040B36D` | `` |
| `0x00734AAC` | `0x00000001` | `` | `0x0040B37900000001` | `` |
| `0x00734AB0` | `0x0040B379` | `0x0040B379` | `0x000000000040B379` | `` |
| `0x00734AB4` | `0x00000000` | `` | `0x0005821000000000` | `` |
| `0x00734AB8` | `0x00058210` | `0x00058210` | `0xFFFFFFFF00058210` | `` |
| `0x00734ABC` | `0xFFFFFFFF` | `` | `0x00058257FFFFFFFF` | `` |
| `0x00734AC0` | `0x00058257` | `0x00058257` | `0x0000000000058257` | `` |
| `0x00734AC4` | `0x00000000` | `` | `0x0005826A00000000` | `` |
| `0x00734AC8` | `0x0005826A` | `0x0005826A` | `0x000000010005826A` | `` |
| `0x00734ACC` | `0x00000001` | `` | `0x0005827D00000001` | `` |
| `0x00734AD0` | `0x0005827D` | `0x0005827D` | `0x000000020005827D` | `` |
| `0x00734AD4` | `0x00000002` | `` | `0x0005829100000002` | `` |
| `0x00734AD8` | `0x00058291` | `0x00058291` | `0x0000000000058291` | `` |
| `0x00734ADC` | `0x00000000` | `` | `0x0005829500000000` | `` |
| `0x00734AE0` | `0x00058295` | `0x00058295` | `0xFFFFFFFF00058295` | `` |
| `0x00734AE4` | `0xFFFFFFFF` | `` | `0x00081401FFFFFFFF` | `` |
| `0x00734AE8` | `0x00081401` | `0x00081401` | `0x0009641400081401` | `` |