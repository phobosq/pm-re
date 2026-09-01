# Runtime container consumers via 0x13C5A0

direct callers: 8

## call `0x000590CC` in `0x00059030..0x000590F4`

```asm
0x00059072: call 0x140391a94
0x00059077: nop
0x00059078: mov qword ptr [rdi + 0x68], rsi
0x0005907C: mov qword ptr [rdi + 0x70], rsi
0x00059080: mov qword ptr [rdi + 0x78], rsi
0x00059084: mov byte ptr [rdi + 0x80], sil
0x0005908B: mov qword ptr [rdi + 0x88], rsi
0x00059092: mov dword ptr [rdi + 0x90], esi
0x00059098: lea rcx, [rdi + 0x98]
0x0005909F: lea edx, [rsi + 2]
0x000590A2: call 0x140391a94
0x000590A7: nop
0x000590A8: lea rcx, [rdi + 0xe8]
0x000590AF: call 0x140391e84
0x000590B4: nop
0x000590B5: lea rcx, [rdi + 0x130]
0x000590BC: call 0x140391e84
0x000590C1: nop
0x000590C2: mov word ptr [rdi + 0x178], si
0x000590C9: mov rcx, rbx
0x000590CC: call 0x14013c5a0
0x000590D1: mov rdx, rax
0x000590D4: lea rcx, [rdi + 0x180]
0x000590DB: call 0x140058f70
0x000590E0: nop
0x000590E1: mov rax, rdi
0x000590E4: mov rbx, qword ptr [rsp + 0x48]
0x000590E9: mov rsi, qword ptr [rsp + 0x50]
0x000590EE: add rsp, 0x30
0x000590F2: pop rdi
0x000590F3: ret
```

### Interesting accesses/calls after accessor

| RVA | kind | instruction |
|---|---|---|
| `0x000590DB` | call | `direct 0x00058F70` |

## call `0x0006FA05` in `0x0006F940..0x000700E0`

```asm
0x0006F9A6: mov rcx, r13
0x0006F9A9: call 0x1400e32c0
0x0006F9AE: test al, al
0x0006F9B0: je 0x14007001e
0x0006F9B6: lea rcx, [rbp + 0x190]
0x0006F9BD: call 0x1400e00c0
0x0006F9C2: nop
0x0006F9C3: xorps xmm0, xmm0
0x0006F9C6: movdqu xmmword ptr [rsp + 0x28], xmm0
0x0006F9CC: mov qword ptr [rsp + 0x38], rsi
0x0006F9D1: lea r8, [rsp + 0x28]
0x0006F9D6: lea rdx, [rsp + 0x40]
0x0006F9DB: lea rcx, [rbp + 0x190]
0x0006F9E2: call 0x1400ef860
0x0006F9E7: test al, al
0x0006F9E9: je 0x14006ffc9
0x0006F9EF: lea rcx, [rbp + 0x190]
0x0006F9F6: call 0x1400e2100
0x0006F9FB: mov r14d, esi
0x0006F9FE: lea rcx, [r13 + 0x300]
0x0006FA05: call 0x14013c5a0
0x0006FA0A: mov rbx, qword ptr [rax]
0x0006FA0D: mov rdi, qword ptr [rax + 8]
0x0006FA11: cmp rbx, rdi
0x0006FA14: je 0x14006fd27
0x0006FA1A: nop word ptr [rax + rax]
0x0006FA20: mov rsi, qword ptr [rbx + 8]
0x0006FA24: mov r15, qword ptr [rbx]
0x0006FA27: test rsi, rsi
0x0006FA2A: je 0x14006fa30
0x0006FA2C: lock inc dword ptr [rsi + 8]
0x0006FA30: mov qword ptr [rbp + 0x50], rsi
0x0006FA34: mov qword ptr [rbp + 0x48], r15
0x0006FA38: lea rdx, [rbp + 0x90]
0x0006FA3F: mov rcx, r15
0x0006FA42: call 0x140084a60
0x0006FA47: mov edx, r14d
0x0006FA4A: lea rcx, [rbp + 0x190]
0x0006FA51: call 0x1400e3f60
0x0006FA56: lea rcx, [rsp + 0x60]
0x0006FA5B: movups xmm0, xmmword ptr [rax]
0x0006FA5E: movups xmmword ptr [rcx], xmm0
0x0006FA61: movups xmm1, xmmword ptr [rax + 0x10]
0x0006FA65: movups xmmword ptr [rcx + 0x10], xmm1
0x0006FA69: movups xmm0, xmmword ptr [rax + 0x20]
0x0006FA6D: movups xmmword ptr [rcx + 0x20], xmm0
0x0006FA71: movups xmm1, xmmword ptr [rax + 0x30]
0x0006FA75: movups xmmword ptr [rcx + 0x30], xmm1
0x0006FA79: movups xmm0, xmmword ptr [rax + 0x40]
0x0006FA7D: movups xmmword ptr [rcx + 0x40], xmm0
0x0006FA81: movups xmm1, xmmword ptr [rax + 0x50]
0x0006FA85: movups xmmword ptr [rcx + 0x50], xmm1
0x0006FA89: movups xmm0, xmmword ptr [rax + 0x60]
0x0006FA8D: movups xmmword ptr [rcx + 0x60], xmm0
0x0006FA91: lea rcx, [rcx + 0x80]
0x0006FA98: movups xmm1, xmmword ptr [rax + 0x70]
0x0006FA9C: movups xmmword ptr [rcx - 0x10], xmm1
0x0006FAA0: sub rax, -0x80
0x0006FAA4: movups xmm0, xmmword ptr [rax]
0x0006FAA7: movups xmmword ptr [rcx], xmm0
0x0006FAAA: movups xmm1, xmmword ptr [rax + 0x10]
0x0006FAAE: movups xmmword ptr [rcx + 0x10], xmm1
0x0006FAB2: movups xmm0, xmmword ptr [rax + 0x20]
0x0006FAB6: movups xmmword ptr [rcx + 0x20], xmm0
0x0006FABA: movups xmm1, xmmword ptr [rax + 0x30]
0x0006FABE: movups xmmword ptr [rcx + 0x30], xmm1
0x0006FAC2: movups xmm0, xmmword ptr [rax + 0x40]
0x0006FAC6: movups xmmword ptr [rcx + 0x40], xmm0
0x0006FACA: mov rax, qword ptr [rax + 0x50]
0x0006FACE: mov qword ptr [rcx + 0x50], rax
0x0006FAD2: mov eax, dword ptr [rbp + 0x90]
0x0006FAD8: mov rdx, qword ptr [rsp + 0x60]
0x0006FADD: test edx, edx
0x0006FADF: cmovns eax, edx
0x0006FAE2: mov dword ptr [rbp + 0x90], eax
0x0006FAE8: mov rax, qword ptr [rsp + 0x78]
0x0006FAED: shr rax, 0x20
0x0006FAF1: mov dword ptr [rbp + 0xac], eax
0x0006FAF7: mov eax, dword ptr [rbp - 0x78]
0x0006FAFA: mov dword ptr [rbp + 0xb8], eax
0x0006FB00: mov eax, dword ptr [rbp + 0x98]
0x0006FB06: mov rcx, qword ptr [rsp + 0x68]
0x0006FB0B: test ecx, ecx
0x0006FB0D: cmovne eax, ecx
0x0006FB10: mov dword ptr [rbp + 0x98], eax
0x0006FB16: shr rcx, 0x20
0x0006FB1A: mov eax, dword ptr [rbp + 0x9c]
0x0006FB20: test ecx, ecx
0x0006FB22: cmovg eax, ecx
0x0006FB25: mov dword ptr [rbp + 0x9c], eax
0x0006FB2B: mov eax, dword ptr [rbp - 0x10]
0x0006FB2E: mov dword ptr [rbp + 0x120], eax
0x0006FB34: mov ecx, dword ptr [rbp + 0xd8]
0x0006FB3A: mov eax, dword ptr [rbp - 0x58]
0x0006FB3D: test eax, eax
0x0006FB3F: cmovns ecx, eax
0x0006FB42: mov dword ptr [rbp + 0xd8], ecx
0x0006FB48: mov ecx, dword ptr [rbp + 0xcc]
0x0006FB4E: mov eax, dword ptr [rbp - 0x64]
0x0006FB51: test eax, eax
0x0006FB53: cmovg ecx, eax
0x0006FB56: mov dword ptr [rbp + 0xcc], ecx
0x0006FB5C: mov ecx, dword ptr [rbp + 0xd0]
0x0006FB62: mov eax, dword ptr [rbp - 0x60]
0x0006FB65: test eax, eax
0x0006FB67: cmovg ecx, eax
0x0006FB6A: mov dword ptr [rbp + 0xd0], ecx
0x0006FB70: mov ecx, dword ptr [rbp + 0xd4]
0x0006FB76: mov eax, dword ptr [rbp - 0x5c]
0x0006FB79: test eax, eax
0x0006FB7B: cmovg ecx, eax
0x0006FB7E: mov dword ptr [rbp + 0xd4], ecx
0x0006FB84: mov ecx, dword ptr [rbp + 0xdc]
0x0006FB8A: mov eax, dword ptr [rbp - 0x54]
0x0006FB8D: test eax, eax
0x0006FB8F: cmovns ecx, eax
0x0006FB92: mov dword ptr [rbp + 0xdc], ecx
0x0006FB98: mov ecx, dword ptr [rbp + 0xe0]
0x0006FB9E: mov eax, dword ptr [rbp - 0x50]
0x0006FBA1: test eax, eax
0x0006FBA3: cmovns ecx, eax
0x0006FBA6: mov dword ptr [rbp + 0xe0], ecx
0x0006FBAC: mov eax, dword ptr [rbp - 0x38]
0x0006FBAF: mov dword ptr [rbp + 0xf8], eax
0x0006FBB5: mov ecx, dword ptr [rbp + 0x108]
0x0006FBBB: mov eax, dword ptr [rbp - 0x28]
0x0006FBBE: test eax, eax
0x0006FBC0: cmovg ecx, eax
0x0006FBC3: mov dword ptr [rbp + 0x108], ecx
0x0006FBC9: mov ecx, dword ptr [rbp + 0xe8]
0x0006FBCF: mov eax, dword ptr [rbp - 0x48]
0x0006FBD2: test eax, eax
0x0006FBD4: cmovg ecx, eax
0x0006FBD7: mov dword ptr [rbp + 0xe8], ecx
0x0006FBDD: mov ecx, dword ptr [rbp + 0xec]
0x0006FBE3: mov eax, dword ptr [rbp - 0x44]
0x0006FBE6: test eax, eax
0x0006FBE8: cmovne ecx, eax
0x0006FBEB: mov dword ptr [rbp + 0xec], ecx
0x0006FBF1: mov ecx, dword ptr [rbp + 0xfc]
0x0006FBF7: mov eax, dword ptr [rbp - 0x34]
0x0006FBFA: test eax, eax
0x0006FBFC: cmovg ecx, eax
0x0006FBFF: mov dword ptr [rbp + 0xfc], ecx
0x0006FC05: mov ecx, dword ptr [rbp + 0xf0]
0x0006FC0B: mov eax, dword ptr [rbp - 0x40]
0x0006FC0E: test eax, eax
0x0006FC10: cmovg ecx, eax
0x0006FC13: mov dword ptr [rbp + 0xf0], ecx
0x0006FC19: mov ecx, dword ptr [rbp + 0xf4]
```

### Interesting accesses/calls after accessor

| RVA | kind | instruction |
|---|---|---|
| `0x0006FA38` | context | `lea rdx, [rbp + 0x90]` |
| `0x0006FA42` | call | `direct 0x00084A60` |
| `0x0006FA51` | call | `direct 0x000E3F60` |
| `0x0006FAD2` | context | `mov eax, dword ptr [rbp + 0x90]` |
| `0x0006FAE2` | context | `mov dword ptr [rbp + 0x90], eax` |

## call `0x00077536` in `0x00074AB0..0x00079CAC`

```asm
0x000774BF: lea rcx, [rsp + 0x6c0]
0x000774C7: call 0x1400dccf0
0x000774CC: nop
0x000774CD: cmp qword ptr [rax + 0x18], 0x10
0x000774D2: jb 0x1400774d7
0x000774D4: mov rax, qword ptr [rax]
0x000774D7: lea rdx, [r15 + 0x1648]
0x000774DE: mov rcx, rax
0x000774E1: call 0x140063420
0x000774E6: nop
0x000774E7: lea rcx, [rsp + 0x10a8]
0x000774EF: call 0x140032ef0
0x000774F4: mov qword ptr [rsp + 0x970], 0xf
0x00077500: mov qword ptr [rsp + 0x968], r14
0x00077508: mov byte ptr [rsp + 0x958], 0
0x00077510: mov qword ptr [rsp + 0x950], 0xf
0x0007751C: mov qword ptr [rsp + 0x948], r14
0x00077524: mov byte ptr [rsp + 0x938], 0
0x0007752C: lea r12, [r15 + 0x300]
0x00077533: mov rcx, r12
0x00077536: call 0x14013c5a0
0x0007753B: mov rbx, qword ptr [rax]
0x0007753E: mov rdi, qword ptr [rax + 8]
0x00077542: cmp rbx, rdi
0x00077545: je 0x140077dc5
0x0007754B: nop dword ptr [rax + rax]
0x00077550: xorps xmm0, xmm0
0x00077553: movdqu xmmword ptr [rsp + 0x58], xmm0
0x00077559: mov r8, qword ptr [rbx + 8]
0x0007755D: mov rdx, qword ptr [rbx]
0x00077560: test r8, r8
0x00077563: je 0x14007756a
0x00077565: lock inc dword ptr [r8 + 8]
0x0007756A: lea rcx, [rsp + 0x58]
0x0007756F: call 0x140058410
0x00077574: nop
0x00077575: mov rsi, qword ptr [rsp + 0x58]
0x0007757A: mov rcx, rsi
0x0007757D: call 0x1401348b0
0x00077582: test al, al
0x00077584: je 0x14007784a
0x0007758A: cmp qword ptr [rsp + 0x968], 0
0x00077593: jne 0x1400777a5
0x00077599: mov dword ptr [rsp + 0x7e8], 0x66
0x000775A4: mov dword ptr [rsp + 0x7ec], 0x77
0x000775AF: mov eax, dword ptr [rsp + 0x7ec]
0x000775B6: xor eax, 0x21
0x000775B9: mov byte ptr [rsp + 0x7f0], al
0x000775C0: movsx ecx, byte ptr [rsp + 0x7f0]
0x000775C8: xor ecx, 0x36
0x000775CB: mov byte ptr [rsp + 0x7f1], cl
0x000775D2: movsx ecx, byte ptr [rsp + 0x7f1]
0x000775DA: xor ecx, 0x33
0x000775DD: mov byte ptr [rsp + 0x7f2], cl
0x000775E4: movsx ecx, byte ptr [rsp + 0x7f2]
0x000775EC: xor ecx, 0x15
0x000775EF: mov byte ptr [rsp + 0x7f3], cl
0x000775F6: movsx ecx, byte ptr [rsp + 0x7f3]
0x000775FE: xor ecx, 0x46
0x00077601: mov byte ptr [rsp + 0x7f4], cl
0x00077608: movsx ecx, byte ptr [rsp + 0x7f4]
0x00077610: xor ecx, 0xf
0x00077613: mov byte ptr [rsp + 0x7f5], cl
0x0007761A: movsx ecx, byte ptr [rsp + 0x7f5]
0x00077622: xor ecx, 8
0x00077625: mov byte ptr [rsp + 0x7f6], cl
0x0007762C: movsx ecx, byte ptr [rsp + 0x7f6]
0x00077634: xor ecx, 0x46
0x00077637: mov byte ptr [rsp + 0x7f7], cl
0x0007763E: movsx ecx, byte ptr [rsp + 0x7f7]
0x00077646: xor ecx, 0x12
0x00077649: mov byte ptr [rsp + 0x7f8], cl
0x00077650: movsx ecx, byte ptr [rsp + 0x7f8]
0x00077658: xor ecx, 0xe
0x0007765B: mov byte ptr [rsp + 0x7f9], cl
0x00077662: movsx ecx, byte ptr [rsp + 0x7f9]
0x0007766A: xor ecx, 3
0x0007766D: mov byte ptr [rsp + 0x7fa], cl
0x00077674: movsx ecx, byte ptr [rsp + 0x7fa]
0x0007767C: xor ecx, 0x14
0x0007767F: mov byte ptr [rsp + 0x7fb], cl
0x00077686: movsx ecx, byte ptr [rsp + 0x7fb]
0x0007768E: xor ecx, 0xb
0x00077691: mov byte ptr [rsp + 0x7fc], cl
0x00077698: movsx ecx, byte ptr [rsp + 0x7fc]
0x000776A0: xor ecx, 7
0x000776A3: mov byte ptr [rsp + 0x7fd], cl
0x000776AA: movsx ecx, byte ptr [rsp + 0x7fd]
0x000776B2: xor ecx, 0xa
0x000776B5: mov byte ptr [rsp + 0x7fe], cl
0x000776BC: movsx ecx, byte ptr [rsp + 0x7fe]
0x000776C4: xor ecx, 0x46
0x000776C7: mov byte ptr [rsp + 0x7ff], cl
0x000776CE: movsx ecx, byte ptr [rsp + 0x7ff]
0x000776D6: xor ecx, 0x15
0x000776D9: mov byte ptr [rsp + 0x800], cl
0x000776E0: movsx ecx, byte ptr [rsp + 0x800]
0x000776E8: xor ecx, 0x12
0x000776EB: mov byte ptr [rsp + 0x801], cl
0x000776F2: movsx ecx, byte ptr [rsp + 0x801]
0x000776FA: xor ecx, 9
0x000776FD: mov byte ptr [rsp + 0x802], cl
0x00077704: movsx ecx, byte ptr [rsp + 0x802]
0x0007770C: xor ecx, 0x16
0x0007770F: mov byte ptr [rsp + 0x803], cl
0x00077716: movsx ecx, byte ptr [rsp + 0x803]
0x0007771E: xor ecx, 0x5c
0x00077721: mov byte ptr [rsp + 0x804], cl
0x00077728: movsx ecx, byte ptr [rsp + 0x804]
0x00077730: xor ecx, 0x46
0x00077733: mov byte ptr [rsp + 0x805], cl
0x0007773A: xor eax, eax
0x0007773C: mov byte ptr [rsp + 0x806], al
0x00077743: movzx eax, byte ptr [rsp + 0x7f0]
0x0007774B: lea rdx, [rsp + 0x1228]
0x00077753: lea rcx, [rsp + 0x7e8]
0x0007775B: call 0x14026ee50
0x00077760: nop
0x00077761: mov r8, qword ptr [rsp + 0x58]
0x00077766: add r8, 8
0x0007776A: mov rdx, rax
0x0007776D: lea rcx, [rsp + 0x1208]
0x00077775: call 0x14005cd90
0x0007777A: mov rdx, rax
0x0007777D: lea rcx, [rsp + 0x958]
0x00077785: call 0x140043f90
0x0007778A: lea rcx, [rsp + 0x1208]
0x00077792: call 0x140032ef0
0x00077797: nop
0x00077798: lea rcx, [rsp + 0x1228]
0x000777A0: jmp 0x140077d76
0x000777A5: mov dword ptr [rsp + 0x8a0], 0x5a
0x000777B0: mov eax, dword ptr [rsp + 0x8a0]
0x000777B7: xor eax, 0x2c
0x000777BA: inc eax
0x000777BC: mov byte ptr [rsp + 0x8a4], al
0x000777C3: movsx ecx, byte ptr [rsp + 0x8a4]
0x000777CB: xor ecx, 0x20
0x000777CE: inc ecx
0x000777D0: mov byte ptr [rsp + 0x8a5], cl
0x000777D7: mov byte ptr [rsp + 0x8a6], 0
0x000777DF: movzx eax, byte ptr [rsp + 0x8a4]
0x000777E7: lea rdx, [rsp + 0x1268]
0x000777EF: lea rcx, [rsp + 0x8a0]
0x000777F7: call 0x140085770
0x000777FC: nop
0x000777FD: mov r8, qword ptr [rsp + 0x58]
0x00077802: add r8, 8
0x00077806: mov rdx, rax
0x00077809: lea rcx, [rsp + 0x1248]
```

### Interesting accesses/calls after accessor

| RVA | kind | instruction |
|---|---|---|
| `0x0007756F` | call | `direct 0x00058410` |
| `0x0007757D` | call | `direct 0x001348B0` |
| `0x0007775B` | call | `direct 0x0026EE50` |
| `0x00077775` | call | `direct 0x0005CD90` |
| `0x00077785` | call | `direct 0x00043F90` |
| `0x00077792` | call | `direct 0x00032EF0` |
| `0x000777F7` | call | `direct 0x00085770` |
| `0x00077811` | call | `direct 0x0005CD90` |
| `0x00077829` | call | `direct 0x00035230` |
| `0x00077837` | call | `direct 0x00032EF0` |
| `0x0007784D` | call | `direct 0x00137960` |

## call `0x00077ED2` in `0x00074AB0..0x00079CAC`

```asm
0x00077E3D: jne 0x140078b67
0x00077E43: lea rcx, [rip + 0x76e5be]
0x00077E4A: call 0x140134a40
0x00077E4F: mov rcx, r15
0x00077E52: call 0x140079cb0
0x00077E57: mov qword ptr [rsp + 0x990], 0xf
0x00077E63: mov qword ptr [rsp + 0x988], r14
0x00077E6B: mov byte ptr [rsp + 0x978], 0
0x00077E73: mov qword ptr [rsp + 0xa00], 0xf
0x00077E7F: mov qword ptr [rsp + 0x9f8], r14
0x00077E87: mov byte ptr [rsp + 0x9e8], 0
0x00077E8F: mov qword ptr [rsp + 0x9e0], 0xf
0x00077E9B: mov qword ptr [rsp + 0x9d8], r14
0x00077EA3: mov byte ptr [rsp + 0x9c8], 0
0x00077EAB: mov qword ptr [rsp + 0x9c0], 0xf
0x00077EB7: mov qword ptr [rsp + 0x9b8], r14
0x00077EBF: mov byte ptr [rsp + 0x9a8], 0
0x00077EC7: xor sil, sil
0x00077ECA: mov byte ptr [rsp + 0x30], sil
0x00077ECF: mov rcx, r12
0x00077ED2: call 0x14013c5a0
0x00077ED7: mov rbx, qword ptr [rax]
0x00077EDA: mov rdi, qword ptr [rax + 8]
0x00077EDE: movzx r13d, byte ptr [rsp + 0x1678]
0x00077EE7: cmp rbx, rdi
0x00077EEA: je 0x140078a94
0x00077EF0: movzx r15d, byte ptr [rsp + 0x1670]
0x00077EF9: nop dword ptr [rax]
0x00077F00: xorps xmm0, xmm0
0x00077F03: movdqu xmmword ptr [rsp + 0x70], xmm0
0x00077F09: mov r8, qword ptr [rbx + 8]
0x00077F0D: mov rdx, qword ptr [rbx]
0x00077F10: test r8, r8
0x00077F13: je 0x140077f1a
0x00077F15: lock inc dword ptr [r8 + 8]
0x00077F1A: lea rcx, [rsp + 0x70]
0x00077F1F: call 0x140058410
0x00077F24: nop
0x00077F25: mov rsi, qword ptr [rsp + 0x70]
0x00077F2A: mov rcx, rsi
0x00077F2D: call 0x140134910
0x00077F32: test al, al
0x00077F34: jne 0x14007817b
0x00077F3A: cmp qword ptr [rsp + 0x988], 0
0x00077F43: jne 0x1400780ce
0x00077F49: mov dword ptr [rsp + 0x808], 0x57
0x00077F54: mov eax, dword ptr [rsp + 0x808]
0x00077F5B: xor eax, 0x50
0x00077F5E: add eax, 5
0x00077F61: mov byte ptr [rsp + 0x80c], al
0x00077F68: movsx ecx, byte ptr [rsp + 0x80c]
0x00077F70: xor ecx, 0x61
0x00077F73: add ecx, 5
0x00077F76: mov byte ptr [rsp + 0x80d], cl
0x00077F7D: movsx ecx, byte ptr [rsp + 0x80d]
0x00077F85: xor ecx, 0x75
0x00077F88: add ecx, 5
0x00077F8B: mov byte ptr [rsp + 0x80e], cl
0x00077F92: movsx ecx, byte ptr [rsp + 0x80e]
0x00077F9A: xor ecx, 0x73
0x00077F9D: add ecx, 5
0x00077FA0: mov byte ptr [rsp + 0x80f], cl
0x00077FA7: movsx ecx, byte ptr [rsp + 0x80f]
0x00077FAF: xor ecx, 0x65
0x00077FB2: add ecx, 5
0x00077FB5: mov byte ptr [rsp + 0x810], cl
0x00077FBC: movsx ecx, byte ptr [rsp + 0x810]
0x00077FC4: xor ecx, 0x64
0x00077FC7: add ecx, 5
0x00077FCA: mov byte ptr [rsp + 0x811], cl
0x00077FD1: movsx ecx, byte ptr [rsp + 0x811]
0x00077FD9: xor ecx, 0x20
0x00077FDC: add ecx, 5
0x00077FDF: mov byte ptr [rsp + 0x812], cl
0x00077FE6: movsx ecx, byte ptr [rsp + 0x812]
0x00077FEE: xor ecx, 0x47
0x00077FF1: add ecx, 5
0x00077FF4: mov byte ptr [rsp + 0x813], cl
0x00077FFB: movsx ecx, byte ptr [rsp + 0x813]
0x00078003: xor ecx, 0x50
0x00078006: add ecx, 5
0x00078009: mov byte ptr [rsp + 0x814], cl
0x00078010: movsx ecx, byte ptr [rsp + 0x814]
0x00078018: xor ecx, 0x55
0x0007801B: add ecx, 5
0x0007801E: mov byte ptr [rsp + 0x815], cl
0x00078025: movsx ecx, byte ptr [rsp + 0x815]
0x0007802D: xor ecx, 0x73
0x00078030: add ecx, 5
0x00078033: mov byte ptr [rsp + 0x816], cl
0x0007803A: movsx ecx, byte ptr [rsp + 0x816]
0x00078042: xor ecx, 0x3a
0x00078045: add ecx, 5
0x00078048: mov byte ptr [rsp + 0x817], cl
0x0007804F: movsx ecx, byte ptr [rsp + 0x817]
0x00078057: xor ecx, 0x20
0x0007805A: add ecx, 5
0x0007805D: mov byte ptr [rsp + 0x818], cl
0x00078064: mov byte ptr [rsp + 0x819], 0
0x0007806C: movzx eax, byte ptr [rsp + 0x80c]
0x00078074: lea rdx, [rsp + 0xba8]
0x0007807C: lea rcx, [rsp + 0x808]
0x00078084: call 0x1400dbc00
0x00078089: nop
0x0007808A: mov rsi, qword ptr [rsp + 0x70]
0x0007808F: lea r8, [rsi + 8]
0x00078093: mov rdx, rax
0x00078096: lea rcx, [rsp + 0xb88]
0x0007809E: call 0x14005cd90
0x000780A3: mov rdx, rax
0x000780A6: lea rcx, [rsp + 0x978]
0x000780AE: call 0x140043f90
0x000780B3: lea rcx, [rsp + 0xb88]
0x000780BB: call 0x140032ef0
0x000780C0: nop
0x000780C1: lea rcx, [rsp + 0xba8]
0x000780C9: jmp 0x140078176
0x000780CE: mov dword ptr [rsp + 0x8e8], 0x11
0x000780D9: mov dword ptr [rsp + 0x8ec], 0x26
0x000780E4: mov eax, dword ptr [rsp + 0x8ec]
0x000780EB: xor eax, 0x3d
0x000780EE: mov byte ptr [rsp + 0x8f0], al
0x000780F5: movsx ecx, byte ptr [rsp + 0x8f0]
0x000780FD: xor ecx, 0x31
0x00078100: mov byte ptr [rsp + 0x8f1], cl
0x00078107: xor eax, eax
0x00078109: mov byte ptr [rsp + 0x8f2], al
0x00078110: movzx eax, byte ptr [rsp + 0x8f0]
0x00078118: lea rdx, [rsp + 0xbe8]
0x00078120: lea rcx, [rsp + 0x8e8]
0x00078128: call 0x1401bfed0
0x0007812D: nop
0x0007812E: mov rsi, qword ptr [rsp + 0x70]
0x00078133: lea r8, [rsi + 8]
0x00078137: mov rdx, rax
0x0007813A: lea rcx, [rsp + 0xbc8]
0x00078142: call 0x14005cd90
0x00078147: nop
0x00078148: or r9, 0xffffffffffffffff
0x0007814C: xor r8d, r8d
0x0007814F: mov rdx, rax
0x00078152: lea rcx, [rsp + 0x978]
0x0007815A: call 0x140035230
0x0007815F: nop
0x00078160: lea rcx, [rsp + 0xbc8]
0x00078168: call 0x140032ef0
0x0007816D: nop
0x0007816E: lea rcx, [rsp + 0xbe8]
0x00078176: call 0x140032ef0
0x0007817B: lea rdx, [rsp + 0x1e0]
```

### Interesting accesses/calls after accessor

| RVA | kind | instruction |
|---|---|---|
| `0x00077F1F` | call | `direct 0x00058410` |
| `0x00077F2D` | call | `direct 0x00134910` |
| `0x00078084` | call | `direct 0x000DBC00` |
| `0x0007809E` | call | `direct 0x0005CD90` |
| `0x000780AE` | call | `direct 0x00043F90` |
| `0x000780BB` | call | `direct 0x00032EF0` |
| `0x00078128` | call | `direct 0x001BFED0` |
| `0x00078142` | call | `direct 0x0005CD90` |
| `0x0007815A` | call | `direct 0x00035230` |
| `0x00078168` | call | `direct 0x00032EF0` |
| `0x00078176` | call | `direct 0x00032EF0` |
| `0x00078186` | call | `direct 0x0006A320` |
| `0x0007819A` | call | `indirect qword ptr [rax + 0x38]` |
| `0x000781E0` | call | `direct 0x00068370` |
| `0x0007820A` | call | `direct 0x00086AD0` |

## call `0x0008477D` in `0x00084700..0x000847FB`

```asm
0x0008473C: mov ecx, eax
0x0008473E: call 0x14039219c
0x00084743: nop
0x00084744: test esi, esi
0x00084746: jns 0x1400847c0
0x00084748: test ebp, ebp
0x0008474A: jne 0x140084761
0x0008474C: cmp byte ptr [rdi + 0x13b8], bpl
0x00084753: jne 0x1400847bb
0x00084755: mov dl, 1
0x00084757: mov rcx, rdi
0x0008475A: call 0x140070190
0x0008475F: jmp 0x1400847bb
0x00084761: cmp byte ptr [rdi + 0x13b8], 0
0x00084768: je 0x140084774
0x0008476A: xor edx, edx
0x0008476C: mov rcx, rdi
0x0008476F: call 0x140070190
0x00084774: xor esi, esi
0x00084776: lea rcx, [rdi + 0x300]
0x0008477D: call 0x14013c5a0
0x00084782: mov rcx, qword ptr [rax + 8]
0x00084786: sub rcx, qword ptr [rax]
0x00084789: sar rcx, 4
0x0008478D: test ecx, ecx
0x0008478F: jle 0x1400847bb
0x00084791: mov r8d, ebp
0x00084794: mov edx, esi
0x00084796: mov rcx, rdi
0x00084799: call 0x1400700e0
0x0008479E: inc esi
0x000847A0: lea rcx, [rdi + 0x300]
0x000847A7: call 0x14013c5a0
0x000847AC: mov rcx, qword ptr [rax + 8]
0x000847B0: sub rcx, qword ptr [rax]
0x000847B3: sar rcx, 4
0x000847B7: cmp esi, ecx
0x000847B9: jl 0x140084791
0x000847BB: mov dil, 1
0x000847BE: jmp 0x1400847d0
0x000847C0: mov r8d, ebp
0x000847C3: mov edx, esi
0x000847C5: mov rcx, rdi
0x000847C8: call 0x1400700e0
0x000847CD: movzx edi, al
0x000847D0: mov rcx, rbx
0x000847D3: call 0x140391b24
0x000847D8: test eax, eax
0x000847DA: je 0x1400847e4
0x000847DC: mov ecx, eax
0x000847DE: call 0x14039219c
0x000847E3: nop
0x000847E4: movzx eax, dil
0x000847E8: mov rbx, qword ptr [rsp + 0x58]
0x000847ED: mov rbp, qword ptr [rsp + 0x60]
0x000847F2: add rsp, 0x30
0x000847F6: pop r14
0x000847F8: pop rdi
0x000847F9: pop rsi
0x000847FA: ret
```

### Interesting accesses/calls after accessor

| RVA | kind | instruction |
|---|---|---|
| `0x00084799` | call | `direct 0x000700E0` |
| `0x000847A7` | call | `direct 0x0013C5A0` |
| `0x000847C8` | call | `direct 0x000700E0` |
| `0x000847D3` | call | `direct 0x00391B24` |
| `0x000847DE` | call | `direct 0x0039219C` |

## call `0x000847A7` in `0x00084700..0x000847FB`

```asm
0x0008475F: jmp 0x1400847bb
0x00084761: cmp byte ptr [rdi + 0x13b8], 0
0x00084768: je 0x140084774
0x0008476A: xor edx, edx
0x0008476C: mov rcx, rdi
0x0008476F: call 0x140070190
0x00084774: xor esi, esi
0x00084776: lea rcx, [rdi + 0x300]
0x0008477D: call 0x14013c5a0
0x00084782: mov rcx, qword ptr [rax + 8]
0x00084786: sub rcx, qword ptr [rax]
0x00084789: sar rcx, 4
0x0008478D: test ecx, ecx
0x0008478F: jle 0x1400847bb
0x00084791: mov r8d, ebp
0x00084794: mov edx, esi
0x00084796: mov rcx, rdi
0x00084799: call 0x1400700e0
0x0008479E: inc esi
0x000847A0: lea rcx, [rdi + 0x300]
0x000847A7: call 0x14013c5a0
0x000847AC: mov rcx, qword ptr [rax + 8]
0x000847B0: sub rcx, qword ptr [rax]
0x000847B3: sar rcx, 4
0x000847B7: cmp esi, ecx
0x000847B9: jl 0x140084791
0x000847BB: mov dil, 1
0x000847BE: jmp 0x1400847d0
0x000847C0: mov r8d, ebp
0x000847C3: mov edx, esi
0x000847C5: mov rcx, rdi
0x000847C8: call 0x1400700e0
0x000847CD: movzx edi, al
0x000847D0: mov rcx, rbx
0x000847D3: call 0x140391b24
0x000847D8: test eax, eax
0x000847DA: je 0x1400847e4
0x000847DC: mov ecx, eax
0x000847DE: call 0x14039219c
0x000847E3: nop
0x000847E4: movzx eax, dil
0x000847E8: mov rbx, qword ptr [rsp + 0x58]
0x000847ED: mov rbp, qword ptr [rsp + 0x60]
0x000847F2: add rsp, 0x30
0x000847F6: pop r14
0x000847F8: pop rdi
0x000847F9: pop rsi
0x000847FA: ret
```

### Interesting accesses/calls after accessor

| RVA | kind | instruction |
|---|---|---|
| `0x000847C8` | call | `direct 0x000700E0` |
| `0x000847D3` | call | `direct 0x00391B24` |
| `0x000847DE` | call | `direct 0x0039219C` |

## call `0x00086CA9` in `0x00086C60..0x0008759D`

```asm
0x00086C60: mov rax, rsp
0x00086C63: push rbp
0x00086C64: push r12
0x00086C66: push r13
0x00086C68: push r14
0x00086C6A: push r15
0x00086C6C: lea rbp, [rax - 0x78]
0x00086C70: sub rsp, 0x150
0x00086C77: mov qword ptr [rsp + 0x38], 0xfffffffffffffffe
0x00086C80: mov qword ptr [rax + 0x10], rbx
0x00086C84: mov qword ptr [rax + 0x18], rsi
0x00086C88: mov qword ptr [rax + 0x20], rdi
0x00086C8C: mov rax, qword ptr [rip + 0x74fc5d]
0x00086C93: xor rax, rsp
0x00086C96: mov qword ptr [rbp + 0x40], rax
0x00086C9A: xor r12b, r12b
0x00086C9D: mov byte ptr [rsp + 0x30], r12b
0x00086CA2: add rcx, 0x300
0x00086CA9: call 0x14013c5a0
0x00086CAE: mov rbx, qword ptr [rax]
0x00086CB1: mov rdi, qword ptr [rax + 8]
0x00086CB5: cmp rbx, rdi
0x00086CB8: je 0x140086da5
0x00086CBE: xor r13d, r13d
0x00086CC1: or r15d, 0xffffffff
0x00086CC5: nop word ptr [rax + rax]
0x00086CD0: mov rsi, qword ptr [rbx + 8]
0x00086CD4: mov r14, qword ptr [rbx]
0x00086CD7: test rsi, rsi
0x00086CDA: je 0x140086ce0
0x00086CDC: lock inc dword ptr [rsi + 8]
0x00086CE0: mov qword ptr [rsp + 0x48], rsi
0x00086CE5: mov qword ptr [rsp + 0x40], r14
0x00086CEA: test r14, r14
0x00086CED: je 0x140086d38
0x00086CEF: mov rcx, r14
0x00086CF2: call 0x140134570
0x00086CF7: cmp dword ptr [rax + 0xc], 1
0x00086CFB: jne 0x140086d38
0x00086CFD: mov dword ptr [rsp + 0x20], r13d
0x00086D02: lea r9, [rip + 0x753307]
0x00086D09: lea r8, [rip + 0x7532d8]
0x00086D10: xor edx, edx
0x00086D12: mov rcx, r14
0x00086D15: call 0x1403d3750
0x00086D1A: test rax, rax
0x00086D1D: je 0x140086d38
0x00086D1F: lea r8, [rsp + 0x30]
0x00086D24: mov dl, 1
0x00086D26: mov rcx, rax
0x00086D29: call 0x140164410
0x00086D2E: or r12b, al
0x00086D31: cmp byte ptr [rsp + 0x30], 0
0x00086D36: jne 0x140086d76
0x00086D38: test rsi, rsi
0x00086D3B: je 0x140086d68
0x00086D3D: mov eax, r15d
0x00086D40: lock xadd dword ptr [rsi + 8], eax
0x00086D45: cmp eax, 1
0x00086D48: jne 0x140086d68
0x00086D4A: mov rax, qword ptr [rsi]
0x00086D4D: mov rcx, rsi
0x00086D50: call qword ptr [rax]
0x00086D52: mov eax, r15d
0x00086D55: lock xadd dword ptr [rsi + 0xc], eax
0x00086D5A: cmp eax, 1
0x00086D5D: jne 0x140086d68
0x00086D5F: mov rax, qword ptr [rsi]
0x00086D62: mov rcx, rsi
0x00086D65: call qword ptr [rax + 8]
0x00086D68: add rbx, 0x10
0x00086D6C: cmp rbx, rdi
0x00086D6F: je 0x140086da5
0x00086D71: jmp 0x140086cd0
0x00086D76: test rsi, rsi
0x00086D79: je 0x140086da5
0x00086D7B: mov eax, r15d
0x00086D7E: lock xadd dword ptr [rsi + 8], eax
0x00086D83: cmp eax, 1
0x00086D86: jne 0x140086da5
0x00086D88: mov rax, qword ptr [rsi]
0x00086D8B: mov rcx, rsi
0x00086D8E: call qword ptr [rax]
0x00086D90: lock xadd dword ptr [rsi + 0xc], r15d
0x00086D96: cmp r15d, 1
0x00086D9A: jne 0x140086da5
0x00086D9C: mov rax, qword ptr [rsi]
0x00086D9F: mov rcx, rsi
0x00086DA2: call qword ptr [rax + 8]
0x00086DA5: cmp byte ptr [rsp + 0x30], 0
0x00086DAA: je 0x140087231
0x00086DB0: mov dword ptr [rsp + 0x50], 0x6b
0x00086DB8: mov eax, dword ptr [rsp + 0x50]
0x00086DBC: xor eax, 0x55
0x00086DBF: inc eax
0x00086DC1: mov byte ptr [rsp + 0x54], al
0x00086DC5: movsx ecx, byte ptr [rsp + 0x54]
0x00086DCA: xor ecx, 0x6e
0x00086DCD: inc ecx
0x00086DCF: mov byte ptr [rsp + 0x55], cl
0x00086DD3: movsx ecx, byte ptr [rsp + 0x55]
0x00086DD8: xor ecx, 0x61
0x00086DDB: inc ecx
0x00086DDD: mov byte ptr [rsp + 0x56], cl
0x00086DE1: movsx ecx, byte ptr [rsp + 0x56]
0x00086DE6: xor ecx, 0x62
0x00086DE9: inc ecx
0x00086DEB: mov byte ptr [rsp + 0x57], cl
0x00086DEF: movsx ecx, byte ptr [rsp + 0x57]
0x00086DF4: xor ecx, 0x6c
0x00086DF7: inc ecx
0x00086DF9: mov byte ptr [rsp + 0x58], cl
0x00086DFD: movsx ecx, byte ptr [rsp + 0x58]
0x00086E02: xor ecx, 0x65
0x00086E05: inc ecx
0x00086E07: mov byte ptr [rsp + 0x59], cl
0x00086E0B: movsx ecx, byte ptr [rsp + 0x59]
0x00086E10: xor ecx, 0x20
0x00086E13: inc ecx
0x00086E15: mov byte ptr [rsp + 0x5a], cl
0x00086E19: movsx ecx, byte ptr [rsp + 0x5a]
0x00086E1E: xor ecx, 0x74
0x00086E21: inc ecx
0x00086E23: mov byte ptr [rsp + 0x5b], cl
0x00086E27: movsx ecx, byte ptr [rsp + 0x5b]
0x00086E2C: xor ecx, 0x6f
0x00086E2F: inc ecx
0x00086E31: mov byte ptr [rsp + 0x5c], cl
0x00086E35: movsx ecx, byte ptr [rsp + 0x5c]
0x00086E3A: xor ecx, 0x20
0x00086E3D: inc ecx
0x00086E3F: mov byte ptr [rsp + 0x5d], cl
0x00086E43: movsx ecx, byte ptr [rsp + 0x5d]
0x00086E48: xor ecx, 0x73
0x00086E4B: inc ecx
0x00086E4D: mov byte ptr [rsp + 0x5e], cl
0x00086E51: movsx ecx, byte ptr [rsp + 0x5e]
0x00086E56: xor ecx, 0x65
0x00086E59: inc ecx
0x00086E5B: mov byte ptr [rsp + 0x5f], cl
0x00086E5F: movsx ecx, byte ptr [rsp + 0x5f]
0x00086E64: xor ecx, 0x74
0x00086E67: inc ecx
0x00086E69: mov byte ptr [rsp + 0x60], cl
0x00086E6D: movsx ecx, byte ptr [rsp + 0x60]
0x00086E72: xor ecx, 0x20
0x00086E75: inc ecx
0x00086E77: mov byte ptr [rsp + 0x61], cl
```

### Interesting accesses/calls after accessor

| RVA | kind | instruction |
|---|---|---|
| `0x00086CF2` | call | `direct 0x00134570` |
| `0x00086D15` | call | `direct 0x003D3750` |
| `0x00086D29` | call | `direct 0x00164410` |
| `0x00086D50` | call | `indirect qword ptr [rax]` |
| `0x00086D65` | call | `indirect qword ptr [rax + 8]` |
| `0x00086D8E` | call | `indirect qword ptr [rax]` |
| `0x00086DA2` | call | `indirect qword ptr [rax + 8]` |

## call `0x000876CA` in `0x00087690..0x000877BA`

```asm
0x00087690: push r12
0x00087692: push r14
0x00087694: push r15
0x00087696: sub rsp, 0x40
0x0008769A: mov qword ptr [rsp + 0x20], 0xfffffffffffffffe
0x000876A3: mov qword ptr [rsp + 0x60], rbx
0x000876A8: mov qword ptr [rsp + 0x68], rbp
0x000876AD: mov qword ptr [rsp + 0x70], rsi
0x000876B2: mov qword ptr [rsp + 0x78], rdi
0x000876B7: mov r14, rcx
0x000876BA: mov r15d, dword ptr [rcx + 0x1648]
0x000876C1: xor ebp, ebp
0x000876C3: add rcx, 0x300
0x000876CA: call 0x14013c5a0
0x000876CF: mov rbx, qword ptr [rax]
0x000876D2: mov rdi, qword ptr [rax + 8]
0x000876D6: cmp rbx, rdi
0x000876D9: je 0x140087744
0x000876DB: nop dword ptr [rax + rax]
0x000876E0: mov rsi, qword ptr [rbx + 8]
0x000876E4: mov rcx, qword ptr [rbx]
0x000876E7: test rsi, rsi
0x000876EA: je 0x1400876f0
0x000876EC: lock inc dword ptr [rsi + 8]
0x000876F0: mov qword ptr [rsp + 0x30], rsi
0x000876F5: mov qword ptr [rsp + 0x28], rcx
0x000876FA: test rcx, rcx
0x000876FD: je 0x14008770b
0x000876FF: mov rax, qword ptr [rcx]
0x00087702: call qword ptr [rax + 0x38]
0x00087705: test al, al
0x00087707: je 0x14008770b
0x00087709: inc ebp
0x0008770B: test rsi, rsi
0x0008770E: je 0x14008773b
0x00087710: or eax, 0xffffffff
0x00087713: lock xadd dword ptr [rsi + 8], eax
0x00087718: cmp eax, 1
0x0008771B: jne 0x14008773b
0x0008771D: mov rax, qword ptr [rsi]
0x00087720: mov rcx, rsi
0x00087723: call qword ptr [rax]
0x00087725: or eax, 0xffffffff
0x00087728: lock xadd dword ptr [rsi + 0xc], eax
0x0008772D: cmp eax, 1
0x00087730: jne 0x14008773b
0x00087732: mov rax, qword ptr [rsi]
0x00087735: mov rcx, rsi
0x00087738: call qword ptr [rax + 8]
0x0008773B: add rbx, 0x10
0x0008773F: cmp rbx, rdi
0x00087742: jne 0x1400876e0
0x00087744: mov dword ptr [r14 + 0x1648], ebp
0x0008774B: test r15d, r15d
0x0008774E: jg 0x140087754
0x00087750: test ebp, ebp
0x00087752: jle 0x140087788
0x00087754: call 0x140391550
0x00087759: mov rbx, rax
0x0008775C: call 0x140391534
0x00087761: cqo
0x00087763: idiv rbx
0x00087766: mov r8, rax
0x00087769: imul rax, rdx, 0x3b9aca00
0x00087770: cqo
0x00087772: idiv rbx
0x00087775: imul rdx, r8, 0x3b9aca00
0x0008777C: add rax, rdx
0x0008777F: mov qword ptr [r14 + 0x13d0], rax
0x00087786: test ebp, ebp
0x00087788: jne 0x14008779b
0x0008778A: test r15d, r15d
0x0008778D: jle 0x14008779b
0x0008778F: lea rcx, [r14 + 0x300]
0x00087796: call 0x14013e250
0x0008779B: mov rbx, qword ptr [rsp + 0x60]
0x000877A0: mov rbp, qword ptr [rsp + 0x68]
0x000877A5: mov rsi, qword ptr [rsp + 0x70]
0x000877AA: mov rdi, qword ptr [rsp + 0x78]
0x000877AF: add rsp, 0x40
0x000877B3: pop r15
0x000877B5: pop r14
0x000877B7: pop r12
0x000877B9: ret
```

### Interesting accesses/calls after accessor

| RVA | kind | instruction |
|---|---|---|
| `0x00087702` | call | `indirect qword ptr [rax + 0x38]` |
| `0x00087723` | call | `indirect qword ptr [rax]` |
| `0x00087738` | call | `indirect qword ptr [rax + 8]` |
| `0x00087754` | call | `direct 0x00391550` |
| `0x0008775C` | call | `direct 0x00391534` |
| `0x00087796` | call | `direct 0x0013E250` |
