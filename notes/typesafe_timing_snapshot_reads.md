# Type-safe timing snapshot reads

getter callers: 15

| getter call | PDATA | snapshot base | timing hits | calls after |
|---|---|---|---:|---:|
| `0x0006FA42` | `0x0006F940..0x000700E0` | `rbp+144` | 3 | 25 |
| `0x0007011F` | `0x000700E0..0x00070187` | `rsp+32` | 0 | 3 |
| `0x00134DBC` | `0x00134D80..0x00134FE0` | `rbp+32` | 0 | 13 |
| `0x0013AE35` | `0x0013A9F0..0x0013AE7A` | `rsp+48` | 0 | 2 |
| `0x0013C064` | `0x0013BFD0..0x0013C0F3` | `rsp+32` | 0 | 2 |
| `0x0013ECA7` | `0x0013E6D0..0x0013EEA1` | `rsp+64` | 0 | 6 |
| `0x0013F888` | `0x0013F7E0..0x0013FCC0` | `rbp-64` | 0 | 7 |
| `0x001689B0` | `0x001688D0..0x001694C0` | `rsp+416` | 0 | 39 |
| `0x001690C2` | `0x001688D0..0x001694C0` | `rsp+640` | 0 | 13 |
| `0x00172C76` | `0x00172C10..0x00173AF2` | `rbp-112` | 0 | 38 |
| `0x001B2954` | `0x001B22D0..0x001B5154` | `rsp+1392` | 0 | 119 |
| `0x001B31F4` | `0x001B22D0..0x001B5154` | `rsp+1168` | 0 | 104 |
| `0x001CF954` | `0x001CF8B0..0x001CFEC5` | `rsp+176` | 0 | 26 |
| `0x001F27C5` | `0x001F21F0..0x001F2897` | `rbp+560` | 0 | 3 |
| `0x0020324E` | `0x00201A80..0x0020424F` | `rbp+1440` | 0 | 41 |

## Functions with timing hits

### getter `0x0006FA42` in `0x0006F940..0x000700E0` — snapshot `rbp+144`

Timing hits:
- straps `+0xAC`: `0x0006FC4D: mov dword ptr [rbp + 0x13c], eax`
- vmr_rxboost `+0xB0`: `0x0006FC56: mov dword ptr [rbp + 0x140], eax`
- vmt3 `+0xBC`: `0x0006FC6C: mov dword ptr [rbp + 0x14c], eax`

#### straps @ `0x0006FC4D`

```asm
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
```

#### vmr_rxboost @ `0x0006FC56`

```asm
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
```

#### vmt3 @ `0x0006FC6C`

```asm
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
```
