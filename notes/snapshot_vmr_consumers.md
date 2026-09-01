# Snapshot getter VMR consumers

getter: `0x00084A60`; calls: 15

| call | PDATA | output local | +0xB0 consumers |
|---|---|---|---:|
| `0x0006FA42` | `0x0006F940..0x000700E0` | `rbp+0x90` | 1 |
| `0x0007011F` | `0x000700E0..0x00070187` | `rsp+0x20` | 0 |
| `0x00134DBC` | `0x00134D80..0x00134FE0` | `rbp+0x20` | 0 |
| `0x0013AE35` | `0x0013A9F0..0x0013AE7A` | `rsp+0x30` | 0 |
| `0x0013C064` | `0x0013BFD0..0x0013C0F3` | `rsp+0x20` | 0 |
| `0x0013ECA7` | `0x0013E6D0..0x0013EEA1` | `rsp+0x40` | 0 |
| `0x0013F888` | `0x0013F7E0..0x0013FCC0` | `rbp-0x40` | 0 |
| `0x001689B0` | `0x001688D0..0x001694C0` | `rsp+0x1a0` | 0 |
| `0x001690C2` | `0x001688D0..0x001694C0` | `rsp+0x280` | 0 |
| `0x00172C76` | `0x00172C10..0x00173AF2` | `rbp-0x70` | 0 |
| `0x001B2954` | `0x001B22D0..0x001B5154` | `rsp+0x570` | 0 |
| `0x001B31F4` | `0x001B22D0..0x001B5154` | `rsp+0x490` | 0 |
| `0x001CF954` | `0x001CF8B0..0x001CFEC5` | `rsp+0xb0` | 0 |
| `0x001F27C5` | `0x001F21F0..0x001F2897` | `rbp+0x230` | 0 |
| `0x0020324E` | `0x00201A80..0x0020424F` | `rbp+0x5a0` | 0 |

## Calls with snapshot+0xB0 consumers

### getter call `0x0006FA42` in `0x0006F940..0x000700E0`

output setup: `0x0006FA38: lea rdx, [rbp + 0x90]`

Consumers:
- `0x0006FC56`: `mov dword ptr [rbp + 0x140], eax`

```asm
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
0x0006FC1F: mov eax, dword ptr [rbp - 0x3c]
0x0006FC22: test eax, eax
0x0006FC24: cmovne ecx, eax
0x0006FC27: mov dword ptr [rbp + 0xf4], ecx
0x0006FC2D: mov ecx, dword ptr [rbp + 0x104]
0x0006FC33: mov eax, dword ptr [rbp - 0x2c]
0x0006FC36: test eax, eax
0x0006FC38: cmovg ecx, eax
0x0006FC3B: mov dword ptr [rbp + 0x104], ecx
0x0006FC41: mov eax, dword ptr [rbp]
0x0006FC44: mov dword ptr [rbp + 0x130], eax
0x0006FC4A: mov eax, dword ptr [rbp + 0xc]
0x0006FC4D: mov dword ptr [rbp + 0x13c], eax
0x0006FC53: mov eax, dword ptr [rbp + 0x10]
0x0006FC56: mov dword ptr [rbp + 0x140], eax
0x0006FC5C: movsd xmm0, qword ptr [rbp + 0x14]
0x0006FC61: movsd qword ptr [rbp + 0x144], xmm0
0x0006FC69: mov eax, dword ptr [rbp + 0x1c]
0x0006FC6C: mov dword ptr [rbp + 0x14c], eax
0x0006FC72: shr rdx, 0x20
0x0006FC76: mov dword ptr [rbp + 0x94], edx
0x0006FC7C: mov edx, dword ptr [rbp + 0x10c]
0x0006FC82: mov eax, dword ptr [rbp - 0x24]
0x0006FC85: test eax, eax
0x0006FC87: cmovg edx, eax
0x0006FC8A: mov dword ptr [rbp + 0x10c], edx
0x0006FC90: mov edx, dword ptr [rbp + 0x110]
0x0006FC96: mov eax, dword ptr [rbp - 0x20]
0x0006FC99: test eax, eax
0x0006FC9B: cmovg edx, eax
0x0006FC9E: mov dword ptr [rbp + 0x110], edx
0x0006FCA4: mov edx, dword ptr [rbp + 0x114]
0x0006FCAA: mov eax, dword ptr [rbp - 0x1c]
0x0006FCAD: test eax, eax
0x0006FCAF: cmovg edx, eax
0x0006FCB2: mov dword ptr [rbp + 0x114], edx
0x0006FCB8: lea rdx, [rbp + 0x90]
0x0006FCBF: mov rcx, r15
0x0006FCC2: call 0x1401362d0
0x0006FCC7: cmp qword ptr [r13 + 0x12a8], 0
0x0006FCCF: je 0x14006fce5
0x0006FCD1: mov r8d, dword ptr [rsp + 0x70]
0x0006FCD6: mov edx, r14d
0x0006FCD9: lea rcx, [r13 + 0x300]
0x0006FCE0: call 0x14013f7e0
0x0006FCE5: inc r14d
0x0006FCE8: test rsi, rsi
0x0006FCEB: je 0x14006fd18
0x0006FCED: or eax, 0xffffffff
0x0006FCF0: lock xadd dword ptr [rsi + 8], eax
0x0006FCF5: cmp eax, 1
0x0006FCF8: jne 0x14006fd18
0x0006FCFA: mov rax, qword ptr [rsi]
0x0006FCFD: mov rcx, rsi
0x0006FD00: call qword ptr [rax]
0x0006FD02: or eax, 0xffffffff
0x0006FD05: lock xadd dword ptr [rsi + 0xc], eax
0x0006FD0A: cmp eax, 1
0x0006FD0D: jne 0x14006fd18
```
