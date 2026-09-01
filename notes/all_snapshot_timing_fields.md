# All snapshot timing-field consumers

getter `0x00084A60`, calls `15`

| getter call | PDATA | output local | timing hits |
|---|---|---|---:|
| `0x0006FA42` | `0x0006F940..0x000700E0` | `rbp+0x90` | 3 |
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

## Detailed field accesses

### getter `0x0006FA42` in `0x0006F940..0x000700E0` output `rbp+0x90`

| RVA | snapshot off | label | instruction |
|---|---:|---|---|
| `0x0006FAD2` | `+0x0` |  | `mov eax, dword ptr [rbp + 0x90]` |
| `0x0006FAE2` | `+0x0` |  | `mov dword ptr [rbp + 0x90], eax` |
| `0x0006FAF1` | `+0x1C` |  | `mov dword ptr [rbp + 0xac], eax` |
| `0x0006FAFA` | `+0x28` |  | `mov dword ptr [rbp + 0xb8], eax` |
| `0x0006FB00` | `+0x8` |  | `mov eax, dword ptr [rbp + 0x98]` |
| `0x0006FB10` | `+0x8` |  | `mov dword ptr [rbp + 0x98], eax` |
| `0x0006FB1A` | `+0xC` |  | `mov eax, dword ptr [rbp + 0x9c]` |
| `0x0006FB25` | `+0xC` |  | `mov dword ptr [rbp + 0x9c], eax` |
| `0x0006FB2E` | `+0x90` |  | `mov dword ptr [rbp + 0x120], eax` |
| `0x0006FB34` | `+0x48` |  | `mov ecx, dword ptr [rbp + 0xd8]` |
| `0x0006FB42` | `+0x48` |  | `mov dword ptr [rbp + 0xd8], ecx` |
| `0x0006FB48` | `+0x3C` |  | `mov ecx, dword ptr [rbp + 0xcc]` |
| `0x0006FB56` | `+0x3C` |  | `mov dword ptr [rbp + 0xcc], ecx` |
| `0x0006FB5C` | `+0x40` |  | `mov ecx, dword ptr [rbp + 0xd0]` |
| `0x0006FB6A` | `+0x40` |  | `mov dword ptr [rbp + 0xd0], ecx` |
| `0x0006FB70` | `+0x44` |  | `mov ecx, dword ptr [rbp + 0xd4]` |
| `0x0006FB7E` | `+0x44` |  | `mov dword ptr [rbp + 0xd4], ecx` |
| `0x0006FB84` | `+0x4C` |  | `mov ecx, dword ptr [rbp + 0xdc]` |
| `0x0006FB92` | `+0x4C` |  | `mov dword ptr [rbp + 0xdc], ecx` |
| `0x0006FB98` | `+0x50` |  | `mov ecx, dword ptr [rbp + 0xe0]` |
| `0x0006FBA6` | `+0x50` |  | `mov dword ptr [rbp + 0xe0], ecx` |
| `0x0006FBAF` | `+0x68` |  | `mov dword ptr [rbp + 0xf8], eax` |
| `0x0006FBB5` | `+0x78` |  | `mov ecx, dword ptr [rbp + 0x108]` |
| `0x0006FBC3` | `+0x78` |  | `mov dword ptr [rbp + 0x108], ecx` |
| `0x0006FBC9` | `+0x58` |  | `mov ecx, dword ptr [rbp + 0xe8]` |
| `0x0006FBD7` | `+0x58` |  | `mov dword ptr [rbp + 0xe8], ecx` |
| `0x0006FBDD` | `+0x5C` |  | `mov ecx, dword ptr [rbp + 0xec]` |
| `0x0006FBEB` | `+0x5C` |  | `mov dword ptr [rbp + 0xec], ecx` |
| `0x0006FBF1` | `+0x6C` |  | `mov ecx, dword ptr [rbp + 0xfc]` |
| `0x0006FBFF` | `+0x6C` |  | `mov dword ptr [rbp + 0xfc], ecx` |
| `0x0006FC05` | `+0x60` |  | `mov ecx, dword ptr [rbp + 0xf0]` |
| `0x0006FC13` | `+0x60` |  | `mov dword ptr [rbp + 0xf0], ecx` |
| `0x0006FC19` | `+0x64` |  | `mov ecx, dword ptr [rbp + 0xf4]` |
| `0x0006FC27` | `+0x64` |  | `mov dword ptr [rbp + 0xf4], ecx` |
| `0x0006FC2D` | `+0x74` |  | `mov ecx, dword ptr [rbp + 0x104]` |
| `0x0006FC3B` | `+0x74` |  | `mov dword ptr [rbp + 0x104], ecx` |
| `0x0006FC44` | `+0xA0` |  | `mov dword ptr [rbp + 0x130], eax` |
| `0x0006FC4D` | `+0xAC` | straps | `mov dword ptr [rbp + 0x13c], eax` |
| `0x0006FC56` | `+0xB0` | vmr/rxboost | `mov dword ptr [rbp + 0x140], eax` |
| `0x0006FC61` | `+0xB4` |  | `movsd qword ptr [rbp + 0x144], xmm0` |
| `0x0006FC6C` | `+0xBC` | vmt3 | `mov dword ptr [rbp + 0x14c], eax` |
| `0x0006FC76` | `+0x4` |  | `mov dword ptr [rbp + 0x94], edx` |
| `0x0006FC7C` | `+0x7C` |  | `mov edx, dword ptr [rbp + 0x10c]` |
| `0x0006FC8A` | `+0x7C` |  | `mov dword ptr [rbp + 0x10c], edx` |
| `0x0006FC90` | `+0x80` |  | `mov edx, dword ptr [rbp + 0x110]` |
| `0x0006FC9E` | `+0x80` |  | `mov dword ptr [rbp + 0x110], edx` |
| `0x0006FCA4` | `+0x84` |  | `mov edx, dword ptr [rbp + 0x114]` |
| `0x0006FCB2` | `+0x84` |  | `mov dword ptr [rbp + 0x114], edx` |
| `0x0006FCB8` | `+0x0` |  | `lea rdx, [rbp + 0x90]` |

#### straps at `0x0006FC4D`

```asm
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
```

#### vmr/rxboost at `0x0006FC56`

```asm
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
```

#### vmt3 at `0x0006FC6C`

```asm
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
```
### getter `0x00134DBC` in `0x00134D80..0x00134FE0` output `rbp+0x20`

| RVA | snapshot off | label | instruction |
|---|---:|---|---|
| `0x00134E20` | `+0x4` |  | `mov r12d, dword ptr [rbp + 0x24]` |
| `0x00134F26` | `+0x0` |  | `cmove r14d, dword ptr [rbp + 0x20]` |
| `0x00134FA0` | `+0x4` |  | `cmp eax, dword ptr [rbp + 0x24]` |
### getter `0x0013C064` in `0x0013BFD0..0x0013C0F3` output `rsp+0x20`

| RVA | snapshot off | label | instruction |
|---|---:|---|---|
| `0x0013C074` | `+0xC` |  | `mov eax, dword ptr [rsp + 0x2c]` |
| `0x0013C0BA` | `+0x14` |  | `cmp dword ptr [rsp + 0x34], 0` |
| `0x0013C0C5` | `+0x8` |  | `mov eax, dword ptr [rsp + 0x28]` |
### getter `0x0013ECA7` in `0x0013E6D0..0x0013EEA1` output `rsp+0x40`

| RVA | snapshot off | label | instruction |
|---|---:|---|---|
| `0x0013ECC7` | `+0x14` |  | `cmp dword ptr [rsp + 0x54], 0` |
### getter `0x0013F888` in `0x0013F7E0..0x0013FCC0` output `rbp-0x40`

| RVA | snapshot off | label | instruction |
|---|---:|---|---|
| `0x0013F88D` | `+0x10` |  | `cmp dword ptr [rbp - 0x30], edi` |
| `0x0013F896` | `+0x10` |  | `mov dword ptr [rbp - 0x30], edi` |
| `0x0013F899` | `+0x0` |  | `lea rdx, [rbp - 0x40]` |
### getter `0x001689B0` in `0x001688D0..0x001694C0` output `rsp+0x1a0`

| RVA | snapshot off | label | instruction |
|---|---:|---|---|
| `0x00168A04` | `+0x14` |  | `mov r13d, dword ptr [rsp + 0x1b4]` |
| `0x00168A0C` | `+0x2C` |  | `cmp dword ptr [rsp + 0x1cc], 0` |
| `0x00168C11` | `+0x30` |  | `mov r10d, dword ptr [rsp + 0x1d0]` |
| `0x00168C19` | `+0x2C` |  | `cmp dword ptr [rsp + 0x1cc], 0` |
| `0x00168C3A` | `+0x19` |  | `movzx eax, byte ptr [rsp + 0x1b9]` |
| `0x001690C7` | `+0x0` |  | `lea rcx, [rsp + 0x1a0]` |
| `0x00169146` | `+0xA8` |  | `mov r9d, dword ptr [rsp + 0x248]` |
| `0x0016914E` | `+0x34` |  | `mov r8d, dword ptr [rsp + 0x1d4]` |
### getter `0x001CF954` in `0x001CF8B0..0x001CFEC5` output `rsp+0xb0`

| RVA | snapshot off | label | instruction |
|---|---:|---|---|
| `0x001CF99E` | `+0x2C` |  | `cmp dword ptr [rsp + 0xdc], 0` |
| `0x001CFAD4` | `+0x30` |  | `mov r9d, dword ptr [rsp + 0xe0]` |
| `0x001CFADC` | `+0x2C` |  | `cmp dword ptr [rsp + 0xdc], 0` |
| `0x001CFAFA` | `+0x25` |  | `movzx r9d, byte ptr [rsp + 0xd5]` |
| `0x001CFB03` | `+0x20` |  | `mov r8d, dword ptr [rsp + 0xd0]` |
| `0x001CFB1B` | `+0x34` |  | `mov r8d, dword ptr [rsp + 0xe4]` |