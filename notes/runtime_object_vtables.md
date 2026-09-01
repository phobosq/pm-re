# Runtime object vtables

Confirmed ctor writes: `[this]=0x440528` then `[this]=0x440560`.

## ctor_base_vtable `RVA 0x00440528`

| slot | qword | method RVA | PDATA |
|---:|---|---|---|
| 0 (`+0x0`) | `0x000000014012FEA0` | `0x0012FEA0` | `0x0012FEA0..0x0012FED4` |
| 1 (`+0x8`) | `0x0000000140067840` | `0x00067840` | `none` |
| 2 (`+0x10`) | `0x0000000140067840` | `0x00067840` | `none` |
| 3 (`+0x18`) | `0x0000000140228240` | `0x00228240` | `0x00228240..0x00228303` |
| 4 (`+0x20`) | `0x0000000140067840` | `0x00067840` | `none` |
| 5 (`+0x28`) | `0x0000000140067840` | `0x00067840` | `none` |
| 6 (`+0x30`) | `0x0000000140726800` | `0x00726800` | non-text |
| 7 (`+0x38`) | `0x000000014012FE60` | `0x0012FE60` | `0x0012FE60..0x0012FE94` |
| 8 (`+0x40`) | `0x0000000140067840` | `0x00067840` | `none` |
| 9 (`+0x48`) | `0x0000000140067840` | `0x00067840` | `none` |
| 10 (`+0x50`) | `0x0000000140138970` | `0x00138970` | `0x00138970..0x00138B02` |
| 11 (`+0x58`) | `0x0000000140067840` | `0x00067840` | `none` |
| 12 (`+0x60`) | `0x0000000140132720` | `0x00132720` | `none` |
| 13 (`+0x68`) | `0x00000001403D0ADC` | `0x003D0ADC` | `0x003D0ADC..0x003D0B16` |
| 14 (`+0x70`) | `0x00000001403D0ADC` | `0x003D0ADC` | `0x003D0ADC..0x003D0B16` |
| 15 (`+0x78`) | `0x00000001403D0ADC` | `0x003D0ADC` | `0x003D0ADC..0x003D0B16` |
| 16 (`+0x80`) | `0x00000001403D0ADC` | `0x003D0ADC` | `0x003D0ADC..0x003D0B16` |
| 17 (`+0x88`) | `0x00000001403D0ADC` | `0x003D0ADC` | `0x003D0ADC..0x003D0B16` |
| 18 (`+0x90`) | `0x00000001403D0ADC` | `0x003D0ADC` | `0x003D0ADC..0x003D0B16` |
| 19 (`+0x98`) | `0x000000014036EFD0` | `0x0036EFD0` | `none` |
| 20 (`+0xA0`) | `0x00000001403D0ADC` | `0x003D0ADC` | `0x003D0ADC..0x003D0B16` |
| 21 (`+0xA8`) | `0x00000001403D0ADC` | `0x003D0ADC` | `0x003D0ADC..0x003D0B16` |
| 22 (`+0xB0`) | `0x00000001403D0ADC` | `0x003D0ADC` | `0x003D0ADC..0x003D0B16` |
| 23 (`+0xB8`) | `0x00000001403D0ADC` | `0x003D0ADC` | `0x003D0ADC..0x003D0B16` |
| 24 (`+0xC0`) | `0x00000001403D0ADC` | `0x003D0ADC` | `0x003D0ADC..0x003D0B16` |
| 25 (`+0xC8`) | `0x00000001403D0ADC` | `0x003D0ADC` | `0x003D0ADC..0x003D0B16` |
| 26 (`+0xD0`) | `0x74746573203A7D7B` | `-` | non-text |
| 27 (`+0xD8`) | `0x72686C2D20676E69` | `-` | non-text |
| 28 (`+0xE0`) | `0x28207D7B206F7420` | `-` | non-text |

### Code xrefs to vtable address


## derived_vtable `RVA 0x00440560`

| slot | qword | method RVA | PDATA |
|---:|---|---|---|
| 0 (`+0x0`) | `0x000000014012FE60` | `0x0012FE60` | `0x0012FE60..0x0012FE94` |
| 1 (`+0x8`) | `0x0000000140067840` | `0x00067840` | `none` |
| 2 (`+0x10`) | `0x0000000140067840` | `0x00067840` | `none` |
| 3 (`+0x18`) | `0x0000000140138970` | `0x00138970` | `0x00138970..0x00138B02` |
| 4 (`+0x20`) | `0x0000000140067840` | `0x00067840` | `none` |
| 5 (`+0x28`) | `0x0000000140132720` | `0x00132720` | `none` |
| 6 (`+0x30`) | `0x00000001403D0ADC` | `0x003D0ADC` | `0x003D0ADC..0x003D0B16` |
| 7 (`+0x38`) | `0x00000001403D0ADC` | `0x003D0ADC` | `0x003D0ADC..0x003D0B16` |
| 8 (`+0x40`) | `0x00000001403D0ADC` | `0x003D0ADC` | `0x003D0ADC..0x003D0B16` |
| 9 (`+0x48`) | `0x00000001403D0ADC` | `0x003D0ADC` | `0x003D0ADC..0x003D0B16` |
| 10 (`+0x50`) | `0x00000001403D0ADC` | `0x003D0ADC` | `0x003D0ADC..0x003D0B16` |
| 11 (`+0x58`) | `0x00000001403D0ADC` | `0x003D0ADC` | `0x003D0ADC..0x003D0B16` |
| 12 (`+0x60`) | `0x000000014036EFD0` | `0x0036EFD0` | `none` |
| 13 (`+0x68`) | `0x00000001403D0ADC` | `0x003D0ADC` | `0x003D0ADC..0x003D0B16` |
| 14 (`+0x70`) | `0x00000001403D0ADC` | `0x003D0ADC` | `0x003D0ADC..0x003D0B16` |
| 15 (`+0x78`) | `0x00000001403D0ADC` | `0x003D0ADC` | `0x003D0ADC..0x003D0B16` |
| 16 (`+0x80`) | `0x00000001403D0ADC` | `0x003D0ADC` | `0x003D0ADC..0x003D0B16` |
| 17 (`+0x88`) | `0x00000001403D0ADC` | `0x003D0ADC` | `0x003D0ADC..0x003D0B16` |
| 18 (`+0x90`) | `0x00000001403D0ADC` | `0x003D0ADC` | `0x003D0ADC..0x003D0B16` |
| 19 (`+0x98`) | `0x74746573203A7D7B` | `-` | non-text |
| 20 (`+0xA0`) | `0x72686C2D20676E69` | `-` | non-text |
| 21 (`+0xA8`) | `0x28207D7B206F7420` | `-` | non-text |

### Code xrefs to vtable address


## Virtual method details

### method `0x0012FEA0` PDATA `0x0012FEA0..0x0012FED4`

Vtable slots:
- ctor_base_vtable slot 0 (`+0x0`)

Calls:
- `0x0012FEAF` -> `0x00227C10`
- `0x0012FEC1` -> `0x003B20DC`

Body:
```asm
0x0012FEA0: mov qword ptr [rsp + 8], rbx
0x0012FEA5: push rdi
0x0012FEA6: sub rsp, 0x20
0x0012FEAA: mov ebx, edx
0x0012FEAC: mov rdi, rcx
0x0012FEAF: call 0x140227c10
0x0012FEB4: test bl, 1
0x0012FEB7: je 0x14012fec6
0x0012FEB9: mov edx, 0x90
0x0012FEBE: mov rcx, rdi
0x0012FEC1: call 0x1403b20dc
0x0012FEC6: mov rax, rdi
0x0012FEC9: mov rbx, qword ptr [rsp + 0x30]
0x0012FECE: add rsp, 0x20
0x0012FED2: pop rdi
0x0012FED3: ret
```

### method `0x00228240` PDATA `0x00228240..0x00228303`

Vtable slots:
- ctor_base_vtable slot 3 (`+0x18`)

Calls:
- `0x00228286` -> `0x00391638`
- `0x002282D1` -> `0x00391484`
- `0x002282DC` -> `qword ptr [rax + 0x10]`
- `0x002282EE` -> `0x003B24C0`

Body:
```asm
0x00228240: mov qword ptr [rsp + 0x18], rbx
0x00228245: mov qword ptr [rsp + 0x20], rbp
0x0022824A: push rsi
0x0022824B: sub rsp, 0x50
0x0022824F: mov rax, qword ptr [rip + 0x5ae69a]
0x00228256: xor rax, rsp
0x00228259: mov qword ptr [rsp + 0x40], rax
0x0022825E: mov rbx, rcx
0x00228261: mov qword ptr [rsp + 0x68], rdi
0x00228266: xor esi, esi
0x00228268: movabs rbp, 0x112e0be826d694b3
0x00228272: mov eax, dword ptr [rbx + 0x88]
0x00228278: cmp eax, 1
0x0022827B: jne 0x1402282e1
0x0022827D: mov eax, dword ptr [rbx + 0x28]
0x00228280: test eax, eax
0x00228282: je 0x1402282d6
0x00228284: mov edi, eax
0x00228286: call 0x140391638
0x0022828B: imul rcx, rax, 0x64
0x0022828F: imul r8, rdi, 0xf4240
0x00228296: mov rax, rbp
0x00228299: add r8, rcx
0x0022829C: lea rcx, [rsp + 0x30]
0x002282A1: imul r8
0x002282A4: sar rdx, 0x1a
0x002282A8: mov rax, rdx
0x002282AB: shr rax, 0x3f
0x002282AF: add rdx, rax
0x002282B2: imul rax, rdx, 0x3b9aca00
0x002282B9: mov qword ptr [rsp + 0x20], rdx
0x002282BE: sub r8d, eax
0x002282C1: mov dword ptr [rsp + 0x28], r8d
0x002282C6: movaps xmm0, xmmword ptr [rsp + 0x20]
0x002282CB: movdqa xmmword ptr [rsp + 0x30], xmm0
0x002282D1: call 0x140391484
0x002282D6: mov rax, qword ptr [rbx]
0x002282D9: mov rcx, rbx
0x002282DC: call qword ptr [rax + 0x10]
0x002282DF: jmp 0x140228272
0x002282E1: mov rdi, qword ptr [rsp + 0x68]
0x002282E6: mov rcx, qword ptr [rsp + 0x40]
0x002282EB: xor rcx, rsp
0x002282EE: call 0x1403b24c0
0x002282F3: mov rbx, qword ptr [rsp + 0x70]
0x002282F8: mov rbp, qword ptr [rsp + 0x78]
0x002282FD: add rsp, 0x50
0x00228301: pop rsi
0x00228302: ret
```

### method `0x0012FE60` PDATA `0x0012FE60..0x0012FE94`

Vtable slots:
- ctor_base_vtable slot 7 (`+0x38`)
- derived_vtable slot 0 (`+0x0`)

Calls:
- `0x0012FE6F` -> `0x0012F970`
- `0x0012FE81` -> `0x003B20DC`

Body:
```asm
0x0012FE60: mov qword ptr [rsp + 8], rbx
0x0012FE65: push rdi
0x0012FE66: sub rsp, 0x20
0x0012FE6A: mov ebx, edx
0x0012FE6C: mov rdi, rcx
0x0012FE6F: call 0x14012f970
0x0012FE74: test bl, 1
0x0012FE77: je 0x14012fe86
0x0012FE79: mov edx, 0x7c0
0x0012FE7E: mov rcx, rdi
0x0012FE81: call 0x1403b20dc
0x0012FE86: mov rax, rdi
0x0012FE89: mov rbx, qword ptr [rsp + 0x30]
0x0012FE8E: add rsp, 0x20
0x0012FE92: pop rdi
0x0012FE93: ret
```

### method `0x00138970` PDATA `0x00138970..0x00138B02`

Vtable slots:
- ctor_base_vtable slot 10 (`+0x50`)
- derived_vtable slot 3 (`+0x18`)

Calls:
- `0x001389AB` -> `0x00227F80`
- `0x001389CB` -> `0x003D3050`
- `0x00138A2F` -> `0x00134690`
- `0x00138A49` -> `0x00066CE0`
- `0x00138A6C` -> `0x001312E0`
- `0x00138A78` -> `0x00134690`
- `0x00138A90` -> `0x001354F0`
- `0x00138AB7` -> `0x0006F460`
- `0x00138AD5` -> `0x0006A240`
- `0x00138AE4` -> `0x003B24C0`

Body:
```asm
0x00138970: mov rax, rsp
0x00138973: push rbp
0x00138974: lea rbp, [rax - 0x108]
0x0013897B: sub rsp, 0x200
0x00138982: mov qword ptr [rsp + 0x20], 0xfffffffffffffffe
0x0013898B: mov qword ptr [rax + 0x10], rbx
0x0013898F: mov qword ptr [rax + 0x18], rsi
0x00138993: mov qword ptr [rax + 0x20], rdi
0x00138997: mov rax, qword ptr [rip + 0x69df52]
0x0013899E: xor rax, rsp
0x001389A1: mov qword ptr [rbp + 0xf0], rax
0x001389A8: mov rbx, rcx
0x001389AB: call 0x140227f80
0x001389B0: mov rcx, qword ptr [rbx + 0x90]
0x001389B7: mov eax, 1
0x001389BC: lock xadd dword ptr [rcx + 0xc], eax
0x001389C1: xor edx, edx
0x001389C3: lea r8d, [rdx + 0x60]
0x001389C7: lea rcx, [rbp + 0x10]
0x001389CB: call 0x1403d3050
0x001389D0: xor esi, esi
0x001389D2: mov qword ptr [rbp + 0x70], rsi
0x001389D6: or edi, 0xffffffff
0x001389D9: mov dword ptr [rbp + 0x78], edi
0x001389DC: mov qword ptr [rbp + 0x80], rsi
0x001389E3: mov dword ptr [rbp + 0x88], esi
0x001389E9: mov qword ptr [rbp + 0x98], rsi
0x001389F0: xorps xmm0, xmm0
0x001389F3: movdqa xmmword ptr [rbp + 0xa0], xmm0
0x001389FB: mov qword ptr [rbp + 0xb8], rsi
0x00138A02: xorps xmm1, xmm1
0x00138A05: movdqa xmmword ptr [rbp + 0xc0], xmm1
0x00138A0D: xor eax, eax
0x00138A0F: mov qword ptr [rbp + 0xd0], rax
0x00138A16: mov dword ptr [rbp + 0xd8], eax
0x00138A1C: mov dword ptr [rbp + 0x90], esi
0x00138A22: mov dword ptr [rbp + 0xb0], esi
0x00138A28: lea rdx, [rbp + 0x10]
0x00138A2C: mov rcx, rbx
0x00138A2F: call 0x140134690
0x00138A34: test al, al
0x00138A36: je 0x140138a81
0x00138A38: nop dword ptr [rax + rax]
0x00138A40: lea rdx, [rbp + 0x10]
0x00138A44: lea rcx, [rsp + 0x30]
0x00138A49: call 0x140066ce0
0x00138A4E: mov rax, qword ptr [rbp + 0xe0]
0x00138A55: mov qword ptr [rbp], rax
0x00138A59: mov rax, qword ptr [rbp + 0xe8]
0x00138A60: mov qword ptr [rbp + 8], rax
0x00138A64: lea rdx, [rsp + 0x30]
0x00138A69: mov rcx, rbx
0x00138A6C: call 0x1401312e0
0x00138A71: lea rdx, [rbp + 0x10]
0x00138A75: mov rcx, rbx
0x00138A78: call 0x140134690
0x00138A7D: test al, al
0x00138A7F: jne 0x140138a40
0x00138A81: mov rax, qword ptr [rbx + 0x90]
0x00138A88: lock xadd dword ptr [rax + 0xc], edi
0x00138A8D: mov rcx, rbx
0x00138A90: call 0x1401354f0
0x00138A95: nop
0x00138A96: mov rdx, qword ptr [rbp + 0xb8]
0x00138A9D: test rdx, rdx
0x00138AA0: je 0x140138ace
0x00138AA2: mov r8, qword ptr [rbp + 0xc8]
0x00138AA9: sub r8, rdx
0x00138AAC: sar r8, 5
0x00138AB0: lea rcx, [rbp + 0xb8]
0x00138AB7: call 0x14006f460
0x00138ABC: mov qword ptr [rbp + 0xb8], rsi
0x00138AC3: xorps xmm0, xmm0
0x00138AC6: movdqa xmmword ptr [rbp + 0xc0], xmm0
0x00138ACE: lea rcx, [rbp + 0x98]
0x00138AD5: call 0x14006a240
0x00138ADA: mov rcx, qword ptr [rbp + 0xf0]
0x00138AE1: xor rcx, rsp
0x00138AE4: call 0x1403b24c0
0x00138AE9: lea r11, [rsp + 0x200]
0x00138AF1: mov rbx, qword ptr [r11 + 0x18]
0x00138AF5: mov rsi, qword ptr [r11 + 0x20]
0x00138AF9: mov rdi, qword ptr [r11 + 0x28]
0x00138AFD: mov rsp, r11
0x00138B00: pop rbp
0x00138B01: ret
```

### method `0x003D0ADC` PDATA `0x003D0ADC..0x003D0B16`

Vtable slots:
- ctor_base_vtable slot 13 (`+0x68`)
- ctor_base_vtable slot 14 (`+0x70`)
- ctor_base_vtable slot 15 (`+0x78`)
- ctor_base_vtable slot 16 (`+0x80`)
- ctor_base_vtable slot 17 (`+0x88`)
- ctor_base_vtable slot 18 (`+0x90`)
- ctor_base_vtable slot 20 (`+0xA0`)
- ctor_base_vtable slot 21 (`+0xA8`)
- ctor_base_vtable slot 22 (`+0xB0`)
- ctor_base_vtable slot 23 (`+0xB8`)
- ctor_base_vtable slot 24 (`+0xC0`)
- ctor_base_vtable slot 25 (`+0xC8`)
- derived_vtable slot 6 (`+0x30`)
- derived_vtable slot 7 (`+0x38`)
- derived_vtable slot 8 (`+0x40`)
- derived_vtable slot 9 (`+0x48`)
- derived_vtable slot 10 (`+0x50`)
- derived_vtable slot 11 (`+0x58`)
- derived_vtable slot 13 (`+0x68`)
- derived_vtable slot 14 (`+0x70`)
- derived_vtable slot 15 (`+0x78`)
- derived_vtable slot 16 (`+0x80`)
- derived_vtable slot 17 (`+0x88`)
- derived_vtable slot 18 (`+0x90`)

Calls:
- `0x003D0B09` -> `0x003B2E14`
- `0x003D0B0E` -> `rbx`
- `0x003D0B10` -> `0x003E87D8`

Body:
```asm
0x003D0ADC: push rbx
0x003D0ADE: sub rsp, 0x20
0x003D0AE2: xor edx, edx
0x003D0AE4: xor eax, eax
0x003D0AE6: lock cmpxchg qword ptr [rip + 0x41ce99], rdx
0x003D0AEF: mov rbx, qword ptr [rip + 0x405dfa]
0x003D0AF6: mov ecx, ebx
0x003D0AF8: xor rbx, rax
0x003D0AFB: and ecx, 0x3f
0x003D0AFE: ror rbx, cl
0x003D0B01: test rbx, rbx
0x003D0B04: je 0x1403d0b10
0x003D0B06: mov rcx, rbx
0x003D0B09: call 0x1403b2e14
0x003D0B0E: call rbx
0x003D0B10: call 0x1403e87d8
0x003D0B15: int3
```
