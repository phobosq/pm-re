# Focused NVIDIA Type2 vtable profile

## slot `+0x48` method `0x001CF7C0` PDATA `0x001CF7C0..0x001CF87B`

### this-derived accesses

| RVA | base | disp | label | instruction |
|---|---|---:|---|---|
| `0x001CF7E7` | `rcx` | `0x7C0` | vendor_lock | `lea rbx, [rcx + 0x7c0]` |
| `0x001CF801` | `rdi` | `0x838` | vendor_obj | `cmp qword ptr [rdi + 0x838], 0` |
| `0x001CF80E` | `rdi` | `0x810` | vendor_state | `cmp qword ptr [rdi + 0x810], rax` |
| `0x001CF81B` | `rdi` | `0x818` |  | `cmp qword ptr [rdi + 0x818], rax` |
| `0x001CF828` | `rdi` | `0x820` |  | `cmp qword ptr [rdi + 0x820], rax` |
| `0x001CF835` | `rdi` | `0x828` |  | `cmp qword ptr [rdi + 0x828], rax` |
| `0x001CF83E` | `rdi` | `0x830` |  | `cmp ebp, dword ptr [rdi + 0x830]` |

### calls

| RVA | target/form |
|---|---|
| `0x001CF7F1` | `0x00391AC4` |
| `0x001CF7FC` | `0x0039219C` |
| `0x001CF851` | `0x00391B24` |
| `0x001CF85C` | `0x0039219C` |

### Full body
```asm
0x001CF7C0: push rdi
0x001CF7C2: sub rsp, 0x30
0x001CF7C6: mov qword ptr [rsp + 0x20], 0xfffffffffffffffe
0x001CF7CF: mov qword ptr [rsp + 0x40], rbx
0x001CF7D4: mov qword ptr [rsp + 0x48], rbp
0x001CF7D9: mov qword ptr [rsp + 0x50], rsi
0x001CF7DE: mov ebp, r8d
0x001CF7E1: mov rsi, rdx
0x001CF7E4: mov rdi, rcx
0x001CF7E7: lea rbx, [rcx + 0x7c0]
0x001CF7EE: mov rcx, rbx
0x001CF7F1: call 0x140391ac4
0x001CF7F6: test eax, eax
0x001CF7F8: je 0x1401cf801
0x001CF7FA: mov ecx, eax
0x001CF7FC: call 0x14039219c
0x001CF801: cmp qword ptr [rdi + 0x838], 0
0x001CF809: je 0x1401cf84b
0x001CF80B: mov rax, qword ptr [rsi]
0x001CF80E: cmp qword ptr [rdi + 0x810], rax
0x001CF815: jne 0x1401cf84b
0x001CF817: mov rax, qword ptr [rsi + 8]
0x001CF81B: cmp qword ptr [rdi + 0x818], rax
0x001CF822: jne 0x1401cf84b
0x001CF824: mov rax, qword ptr [rsi + 0x10]
0x001CF828: cmp qword ptr [rdi + 0x820], rax
0x001CF82F: jne 0x1401cf84b
0x001CF831: mov rax, qword ptr [rsi + 0x18]
0x001CF835: cmp qword ptr [rdi + 0x828], rax
0x001CF83C: jne 0x1401cf84b
0x001CF83E: cmp ebp, dword ptr [rdi + 0x830]
0x001CF844: jne 0x1401cf84b
0x001CF846: mov dil, 1
0x001CF849: jmp 0x1401cf84e
0x001CF84B: xor dil, dil
0x001CF84E: mov rcx, rbx
0x001CF851: call 0x140391b24
0x001CF856: test eax, eax
0x001CF858: je 0x1401cf862
0x001CF85A: mov ecx, eax
0x001CF85C: call 0x14039219c
0x001CF861: nop
0x001CF862: movzx eax, dil
0x001CF866: mov rbx, qword ptr [rsp + 0x40]
0x001CF86B: mov rbp, qword ptr [rsp + 0x48]
0x001CF870: mov rsi, qword ptr [rsp + 0x50]
0x001CF875: add rsp, 0x30
0x001CF879: pop rdi
0x001CF87A: ret
```

## slot `+0x58` method `0x001D0730` PDATA `0x001D0730..0x001D0AB5`

### this-derived accesses

| RVA | base | disp | label | instruction |
|---|---|---:|---|---|
| `0x001D075A` | `rcx` | `0x838` | vendor_obj | `cmp qword ptr [rcx + 0x838], 0` |
| `0x001D0A90` | `rcx` | `0x838` | vendor_obj | `mov rcx, qword ptr [rcx + 0x838]` |

### calls

| RVA | target/form |
|---|---|
| `0x001D0A18` | `0x0021C680` |
| `0x001D0A54` | `0x003D23C8` |
| `0x001D0A71` | `0x003D25D0` |
| `0x001D0A97` | `0x001F0120` |
| `0x001D0AA8` | `0x003B24C0` |

### Full body
```asm
0x001D0730: mov r11, rsp
0x001D0733: sub rsp, 0x118
0x001D073A: mov qword ptr [rsp + 0x68], 0xfffffffffffffffe
0x001D0743: mov rax, qword ptr [rip + 0x6061a6]
0x001D074A: xor rax, rsp
0x001D074D: mov qword ptr [rsp + 0x100], rax
0x001D0755: mov qword ptr [rsp + 0x30], rcx
0x001D075A: cmp qword ptr [rcx + 0x838], 0
0x001D0762: jne 0x1401d0a77
0x001D0768: mov dword ptr [rsp + 0x78], 0x38
0x001D0770: mov eax, dword ptr [rsp + 0x78]
0x001D0774: add al, 0x38
0x001D0776: movsx ecx, al
0x001D0779: xor ecx, 0x24
0x001D077C: mov dword ptr [rsp + 0x7c], ecx
0x001D0780: mov eax, dword ptr [rsp + 0x7c]
0x001D0784: mov ecx, dword ptr [rsp + 0x78]
0x001D0788: xor ecx, eax
0x001D078A: xor ecx, 0x45
0x001D078D: mov byte ptr [rsp + 0x80], cl
0x001D0794: movsx ecx, byte ptr [rsp + 0x80]
0x001D079C: mov eax, dword ptr [rsp + 0x78]
0x001D07A0: inc al
0x001D07A2: xor eax, ecx
0x001D07A4: xor eax, 0x74
0x001D07A7: mov byte ptr [rsp + 0x81], al
0x001D07AE: movsx ecx, byte ptr [rsp + 0x81]
0x001D07B6: mov eax, dword ptr [rsp + 0x78]
0x001D07BA: add al, 2
0x001D07BC: xor eax, ecx
0x001D07BE: xor eax, 0x68
0x001D07C1: mov byte ptr [rsp + 0x82], al
0x001D07C8: movsx ecx, byte ptr [rsp + 0x82]
0x001D07D0: mov eax, dword ptr [rsp + 0x78]
0x001D07D4: add al, 3
0x001D07D6: xor eax, ecx
0x001D07D8: xor eax, 0x61
0x001D07DB: mov byte ptr [rsp + 0x83], al
0x001D07E2: movsx ecx, byte ptr [rsp + 0x83]
0x001D07EA: mov eax, dword ptr [rsp + 0x78]
0x001D07EE: add al, 4
0x001D07F0: xor eax, ecx
0x001D07F2: xor eax, 0x73
0x001D07F5: mov byte ptr [rsp + 0x84], al
0x001D07FC: movsx ecx, byte ptr [rsp + 0x84]
0x001D0804: mov eax, dword ptr [rsp + 0x78]
0x001D0808: add al, 5
0x001D080A: xor eax, ecx
0x001D080C: xor eax, 0x68
0x001D080F: mov byte ptr [rsp + 0x85], al
0x001D0816: movsx ecx, byte ptr [rsp + 0x85]
0x001D081E: mov eax, dword ptr [rsp + 0x78]
0x001D0822: add al, 6
0x001D0824: xor eax, ecx
0x001D0826: xor eax, 0x20
0x001D0829: mov byte ptr [rsp + 0x86], al
0x001D0830: movsx ecx, byte ptr [rsp + 0x86]
0x001D0838: mov eax, dword ptr [rsp + 0x78]
0x001D083C: add al, 7
0x001D083E: xor eax, ecx
0x001D0840: xor eax, 0x43
0x001D0843: mov byte ptr [rsp + 0x87], al
0x001D084A: movsx ecx, byte ptr [rsp + 0x87]
0x001D0852: mov eax, dword ptr [rsp + 0x78]
0x001D0856: add al, 8
0x001D0858: xor eax, ecx
0x001D085A: xor eax, 0x55
0x001D085D: mov byte ptr [rsp + 0x88], al
0x001D0864: movsx ecx, byte ptr [rsp + 0x88]
0x001D086C: mov eax, dword ptr [rsp + 0x78]
0x001D0870: add al, 9
0x001D0872: xor eax, ecx
0x001D0874: xor eax, 0x44
0x001D0877: mov byte ptr [rsp + 0x89], al
0x001D087E: movsx ecx, byte ptr [rsp + 0x89]
0x001D0886: mov eax, dword ptr [rsp + 0x78]
0x001D088A: add al, 0xa
0x001D088C: xor eax, ecx
0x001D088E: xor eax, 0x41
0x001D0891: mov byte ptr [rsp + 0x8a], al
0x001D0898: movsx ecx, byte ptr [rsp + 0x8a]
0x001D08A0: mov eax, dword ptr [rsp + 0x78]
0x001D08A4: add al, 0xb
0x001D08A6: xor eax, ecx
0x001D08A8: xor eax, 0x20
0x001D08AB: mov byte ptr [rsp + 0x8b], al
0x001D08B2: movsx ecx, byte ptr [rsp + 0x8b]
0x001D08BA: mov eax, dword ptr [rsp + 0x78]
0x001D08BE: add al, 0xc
0x001D08C0: xor eax, ecx
0x001D08C2: xor eax, 0x6d
0x001D08C5: mov byte ptr [rsp + 0x8c], al
0x001D08CC: movsx ecx, byte ptr [rsp + 0x8c]
0x001D08D4: mov eax, dword ptr [rsp + 0x78]
0x001D08D8: add al, 0xd
0x001D08DA: xor eax, ecx
0x001D08DC: xor eax, 0x69
0x001D08DF: mov byte ptr [rsp + 0x8d], al
0x001D08E6: movsx ecx, byte ptr [rsp + 0x8d]
0x001D08EE: mov eax, dword ptr [rsp + 0x78]
0x001D08F2: add al, 0xe
0x001D08F4: xor eax, ecx
0x001D08F6: xor eax, 0x6e
0x001D08F9: mov byte ptr [rsp + 0x8e], al
0x001D0900: movsx ecx, byte ptr [rsp + 0x8e]
0x001D0908: mov eax, dword ptr [rsp + 0x78]
0x001D090C: add al, 0xf
0x001D090E: xor eax, ecx
0x001D0910: xor eax, 0x69
0x001D0913: mov byte ptr [rsp + 0x8f], al
0x001D091A: movsx ecx, byte ptr [rsp + 0x8f]
0x001D0922: mov eax, dword ptr [rsp + 0x78]
0x001D0926: add al, 0x10
0x001D0928: xor eax, ecx
0x001D092A: xor eax, 0x6e
0x001D092D: mov byte ptr [rsp + 0x90], al
0x001D0934: movsx ecx, byte ptr [rsp + 0x90]
0x001D093C: mov eax, dword ptr [rsp + 0x78]
0x001D0940: add al, 0x11
0x001D0942: xor eax, ecx
0x001D0944: xor eax, 0x67
0x001D0947: mov byte ptr [rsp + 0x91], al
0x001D094E: movsx ecx, byte ptr [rsp + 0x91]
0x001D0956: mov eax, dword ptr [rsp + 0x78]
0x001D095A: add al, 0x12
0x001D095C: xor eax, ecx
0x001D095E: xor eax, 0x20
0x001D0961: mov byte ptr [rsp + 0x92], al
0x001D0968: movsx ecx, byte ptr [rsp + 0x92]
0x001D0970: mov eax, dword ptr [rsp + 0x78]
0x001D0974: add al, 0x13
0x001D0976: xor eax, ecx
0x001D0978: xor eax, 0x66
0x001D097B: mov byte ptr [rsp + 0x93], al
0x001D0982: movsx ecx, byte ptr [rsp + 0x93]
0x001D098A: mov eax, dword ptr [rsp + 0x78]
0x001D098E: add al, 0x14
0x001D0990: xor eax, ecx
0x001D0992: xor eax, 0x61
0x001D0995: mov byte ptr [rsp + 0x94], al
0x001D099C: movsx ecx, byte ptr [rsp + 0x94]
0x001D09A4: mov eax, dword ptr [rsp + 0x78]
0x001D09A8: add al, 0x15
0x001D09AA: xor eax, ecx
0x001D09AC: xor eax, 0x69
0x001D09AF: mov byte ptr [rsp + 0x95], al
0x001D09B6: movsx ecx, byte ptr [rsp + 0x95]
0x001D09BE: mov eax, dword ptr [rsp + 0x78]
0x001D09C2: add al, 0x16
0x001D09C4: xor eax, ecx
0x001D09C6: xor eax, 0x6c
0x001D09C9: mov byte ptr [rsp + 0x96], al
0x001D09D0: movsx ecx, byte ptr [rsp + 0x96]
0x001D09D8: mov eax, dword ptr [rsp + 0x78]
0x001D09DC: add al, 0x17
0x001D09DE: xor eax, ecx
0x001D09E0: xor eax, 0x65
0x001D09E3: mov byte ptr [rsp + 0x97], al
0x001D09EA: movsx ecx, byte ptr [rsp + 0x97]
0x001D09F2: mov eax, dword ptr [rsp + 0x78]
0x001D09F6: add al, 0x18
0x001D09F8: xor eax, ecx
0x001D09FA: xor eax, 0x64
0x001D09FD: mov byte ptr [r11 - 0x80], al
0x001D0A01: xor eax, eax
0x001D0A03: mov byte ptr [r11 - 0x7f], al
0x001D0A07: movzx eax, byte ptr [rsp + 0x80]
0x001D0A0F: lea rdx, [r11 - 0x38]
0x001D0A13: lea rcx, [rsp + 0x78]
0x001D0A18: call 0x14021c680
0x001D0A1D: nop
0x001D0A1E: cmp qword ptr [rax + 0x18], 0x10
0x001D0A23: jb 0x1401d0a28
0x001D0A25: mov rax, qword ptr [rax]
0x001D0A28: lea rcx, [rip + 0x262f41]
0x001D0A2F: mov qword ptr [rsp + 0x40], rcx
0x001D0A34: xor ecx, ecx
0x001D0A36: mov qword ptr [rsp + 0x48], rcx
0x001D0A3B: mov qword ptr [rsp + 0x50], rcx
0x001D0A40: mov qword ptr [rsp + 0x58], rax
0x001D0A45: mov byte ptr [rsp + 0x60], 1
0x001D0A4A: lea rdx, [rsp + 0x48]
0x001D0A4F: lea rcx, [rsp + 0x58]
0x001D0A54: call 0x1403d23c8
0x001D0A59: lea rax, [rip + 0x262f28]
0x001D0A60: mov qword ptr [rsp + 0x40], rax
0x001D0A65: lea rdx, [rip + 0x5ba4f4]
0x001D0A6C: lea rcx, [rsp + 0x40]
0x001D0A71: call 0x1403d25d0
0x001D0A76: nop
0x001D0A77: mov rax, qword ptr [rsp + 0x148]
0x001D0A7F: mov qword ptr [rsp + 0x28], rax
0x001D0A84: movzx eax, byte ptr [rsp + 0x140]
0x001D0A8C: mov byte ptr [rsp + 0x20], al
0x001D0A90: mov rcx, qword ptr [rcx + 0x838]
0x001D0A97: call 0x1401f0120
0x001D0A9C: nop
0x001D0A9D: mov rcx, qword ptr [rsp + 0x100]
0x001D0AA5: xor rcx, rsp
0x001D0AA8: call 0x1403b24c0
0x001D0AAD: add rsp, 0x118
0x001D0AB4: ret
```

## slot `+0x70` method `0x001CDFD0` PDATA `0x001CDFD0..0x001CE053`

### this-derived accesses

| RVA | base | disp | label | instruction |
|---|---|---:|---|---|
| `0x001CDFEF` | `rcx` | `0x7C0` | vendor_lock | `lea rbx, [rcx + 0x7c0]` |
| `0x001CE00F` | `rdi` | `0x838` | vendor_obj | `mov rcx, qword ptr [rdi + 0x838]` |

### calls

| RVA | target/form |
|---|---|
| `0x001CDFFE` | `0x00391AC4` |
| `0x001CE009` | `0x0039219C` |
| `0x001CE023` | `0x001EED90` |
| `0x001CE02E` | `0x00391B24` |
| `0x001CE039` | `0x0039219C` |

### Full body
```asm
0x001CDFD0: push rdi
0x001CDFD2: sub rsp, 0x30
0x001CDFD6: mov qword ptr [rsp + 0x20], 0xfffffffffffffffe
0x001CDFDF: mov qword ptr [rsp + 0x48], rbx
0x001CDFE4: mov qword ptr [rsp + 0x50], rsi
0x001CDFE9: mov rsi, rdx
0x001CDFEC: mov rdi, rcx
0x001CDFEF: lea rbx, [rcx + 0x7c0]
0x001CDFF6: mov qword ptr [rsp + 0x40], rbx
0x001CDFFB: mov rcx, rbx
0x001CDFFE: call 0x140391ac4
0x001CE003: test eax, eax
0x001CE005: je 0x1401ce00f
0x001CE007: mov ecx, eax
0x001CE009: call 0x14039219c
0x001CE00E: nop
0x001CE00F: mov rcx, qword ptr [rdi + 0x838]
0x001CE016: test rcx, rcx
0x001CE019: jne 0x1401ce020
0x001CE01B: xor dil, dil
0x001CE01E: jmp 0x1401ce02b
0x001CE020: mov rdx, rsi
0x001CE023: call 0x1401eed90
0x001CE028: movzx edi, al
0x001CE02B: mov rcx, rbx
0x001CE02E: call 0x140391b24
0x001CE033: test eax, eax
0x001CE035: je 0x1401ce03f
0x001CE037: mov ecx, eax
0x001CE039: call 0x14039219c
0x001CE03E: nop
0x001CE03F: movzx eax, dil
0x001CE043: mov rbx, qword ptr [rsp + 0x48]
0x001CE048: mov rsi, qword ptr [rsp + 0x50]
0x001CE04D: add rsp, 0x30
0x001CE051: pop rdi
0x001CE052: ret
```

## slot `+0x78` method `0x001D0AD0` PDATA `0x001D0AD0..0x001D0B38`

### this-derived accesses

| RVA | base | disp | label | instruction |
|---|---|---:|---|---|
| `0x001D0AE7` | `rcx` | `0x7C0` | vendor_lock | `lea rbx, [rcx + 0x7c0]` |
| `0x001D0B07` | `rdi` | `0x838` | vendor_obj | `mov rcx, qword ptr [rdi + 0x838]` |

### calls

| RVA | target/form |
|---|---|
| `0x001D0AF6` | `0x00391AC4` |
| `0x001D0B01` | `0x0039219C` |
| `0x001D0B13` | `0x001F0960` |
| `0x001D0B1C` | `0x00391B24` |
| `0x001D0B27` | `0x0039219C` |

### Full body
```asm
0x001D0AD0: push rdi
0x001D0AD2: sub rsp, 0x30
0x001D0AD6: mov qword ptr [rsp + 0x20], 0xfffffffffffffffe
0x001D0ADF: mov qword ptr [rsp + 0x48], rbx
0x001D0AE4: mov rdi, rcx
0x001D0AE7: lea rbx, [rcx + 0x7c0]
0x001D0AEE: mov qword ptr [rsp + 0x40], rbx
0x001D0AF3: mov rcx, rbx
0x001D0AF6: call 0x140391ac4
0x001D0AFB: test eax, eax
0x001D0AFD: je 0x1401d0b07
0x001D0AFF: mov ecx, eax
0x001D0B01: call 0x14039219c
0x001D0B06: nop
0x001D0B07: mov rcx, qword ptr [rdi + 0x838]
0x001D0B0E: test rcx, rcx
0x001D0B11: je 0x1401d0b19
0x001D0B13: call 0x1401f0960
0x001D0B18: nop
0x001D0B19: mov rcx, rbx
0x001D0B1C: call 0x140391b24
0x001D0B21: test eax, eax
0x001D0B23: je 0x1401d0b2d
0x001D0B25: mov ecx, eax
0x001D0B27: call 0x14039219c
0x001D0B2C: nop
0x001D0B2D: mov rbx, qword ptr [rsp + 0x48]
0x001D0B32: add rsp, 0x30
0x001D0B36: pop rdi
0x001D0B37: ret
```

## slot `+0x80` method `0x001CE0B0` PDATA `0x001CE0B0..0x001CE141`

### this-derived accesses

| RVA | base | disp | label | instruction |
|---|---|---:|---|---|
| `0x001CE0E3` | `rdi` | `0x838` | vendor_obj | `mov rsi, qword ptr [rdi + 0x838]` |
| `0x001CE0EA` | `rdi` | `0x838` | vendor_obj | `mov qword ptr [rdi + 0x838], 0` |
| `0x001CE110` | `rdi` | `0x7C0` | vendor_lock | `lea rcx, [rdi + 0x7c0]` |

### calls

| RVA | target/form |
|---|---|
| `0x001CE0D3` | `0x00391AC4` |
| `0x001CE0DE` | `0x0039219C` |
| `0x001CE0FD` | `0x001ED8B0` |
| `0x001CE10A` | `0x003B20DC` |
| `0x001CE117` | `0x00391B24` |
| `0x001CE122` | `0x0039219C` |

### Full body
```asm
0x001CE0B0: push rdi
0x001CE0B2: sub rsp, 0x30
0x001CE0B6: mov qword ptr [rsp + 0x20], 0xfffffffffffffffe
0x001CE0BF: mov qword ptr [rsp + 0x40], rbx
0x001CE0C4: mov qword ptr [rsp + 0x48], rsi
0x001CE0C9: mov rdi, rcx
0x001CE0CC: add rcx, 0x7c0
0x001CE0D3: call 0x140391ac4
0x001CE0D8: test eax, eax
0x001CE0DA: je 0x1401ce0e3
0x001CE0DC: mov ecx, eax
0x001CE0DE: call 0x14039219c
0x001CE0E3: mov rsi, qword ptr [rdi + 0x838]
0x001CE0EA: mov qword ptr [rdi + 0x838], 0
0x001CE0F5: test rsi, rsi
0x001CE0F8: je 0x1401ce110
0x001CE0FA: mov rcx, rsi
0x001CE0FD: call 0x1401ed8b0
0x001CE102: mov edx, 0x38
0x001CE107: mov rcx, rsi
0x001CE10A: call 0x1403b20dc
0x001CE10F: nop
0x001CE110: lea rcx, [rdi + 0x7c0]
0x001CE117: call 0x140391b24
0x001CE11C: test eax, eax
0x001CE11E: je 0x1401ce128
0x001CE120: mov ecx, eax
0x001CE122: call 0x14039219c
0x001CE127: nop
0x001CE128: xor edx, edx
0x001CE12A: mov rcx, rdi
0x001CE12D: mov rbx, qword ptr [rsp + 0x40]
0x001CE132: mov rsi, qword ptr [rsp + 0x48]
0x001CE137: add rsp, 0x30
0x001CE13B: pop rdi
0x001CE13C: jmp 0x140135fa0
```

## slot `+0x88` method `0x001CFED0` PDATA `none`

No PDATA body.

## slot `+0x90` method `0x001CF880` PDATA `none`

No PDATA body.
