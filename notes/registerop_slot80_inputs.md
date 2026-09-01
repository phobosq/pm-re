# NVIDIA child slot +0x80 RegisterOp input provenance

PDATA `0x001DE8B0..0x001DF630`

Known downstream: calls `0x001ECB90(this, current*, desired*, gpu_index)` at 0x1DF246 and 0x1DF43E.

## Calls

| RVA | target/form |
|---|---|
| `0x001DE90E` | `rax` |
| `0x001DE943` | `rax` |
| `0x001DE9C7` | `RVA 0x001E0CA0` |
| `0x001DF189` | `RVA 0x001EB4A0` |
| `0x001DF1A0` | `RVA 0x00040530` |
| `0x001DF223` | `RVA 0x001D97E0` |
| `0x001DF246` | `RVA 0x001ECB90` |
| `0x001DF3EA` | `RVA 0x000DCDD0` |
| `0x001DF401` | `RVA 0x00040530` |
| `0x001DF420` | `RVA 0x001D7930` |
| `0x001DF43E` | `RVA 0x001ECB90` |
| `0x001DF5DF` | `RVA 0x000DCDD0` |
| `0x001DF5F6` | `RVA 0x00040530` |
| `0x001DF603` | `RVA 0x00032EF0` |
| `0x001DF612` | `RVA 0x003B24C0` |

## Local candidate-struct accesses

Tracks RBP-relative offsets near current/desired structures (`0..0x180`).

| RVA | disp | instruction |
|---|---:|---|
| `0x001DE8E1` | `0x120` | `mov qword ptr [rbp + 0x120], rax` |
| `0x001DE9C0` | `0x0` | `lea rdx, [rbp]` |
| `0x001DF180` | `0x60` | `lea rdx, [rbp + 0x60]` |
| `0x001DF1A6` | `0x60` | `lea rcx, [rbp + 0x60]` |
| `0x001DF1CF` | `0x0` | `movaps xmm0, xmmword ptr [rbp]` |
| `0x001DF1D6` | `0x10` | `movaps xmm1, xmmword ptr [rbp + 0x10]` |
| `0x001DF1DE` | `0x20` | `movaps xmm0, xmmword ptr [rbp + 0x20]` |
| `0x001DF1E6` | `0x30` | `movaps xmm1, xmmword ptr [rbp + 0x30]` |
| `0x001DF1EE` | `0x40` | `movaps xmm0, xmmword ptr [rbp + 0x40]` |
| `0x001DF1F6` | `0x50` | `movsd xmm1, qword ptr [rbp + 0x50]` |
| `0x001DF200` | `0x58` | `mov eax, dword ptr [rbp + 0x58]` |
| `0x001DF23F` | `0x0` | `lea rdx, [rbp]` |
| `0x001DF3DF` | `0x80` | `lea rdx, [rbp + 0x80]` |
| `0x001DF407` | `0x80` | `lea rcx, [rbp + 0x80]` |
| `0x001DF416` | `0xC0` | `lea rdx, [rbp + 0xc0]` |
| `0x001DF430` | `0xC0` | `lea r8, [rbp + 0xc0]` |
| `0x001DF437` | `0x0` | `lea rdx, [rbp]` |
| `0x001DF5D4` | `0xA0` | `lea rdx, [rbp + 0xa0]` |
| `0x001DF5FC` | `0xA0` | `lea rcx, [rbp + 0xa0]` |
| `0x001DF608` | `0x120` | `mov rcx, qword ptr [rbp + 0x120]` |

## this-like accesses

Candidate `this` registers are inferred from prolog and callsite use; list non-stack mem displacements >=0x200.

| RVA | base | disp | instruction |
|---|---|---:|---|
| `0x001DE95A` | `rbx` | `0x274` | `mov eax, dword ptr [rbx + 0x274]` |
| `0x001DE968` | `rbx` | `0x274` | `mov dword ptr [rbx + 0x274], edi` |
| `0x001DE96E` | `rbx` | `0x270` | `movsxd rax, dword ptr [rbx + 0x270]` |
| `0x001DE980` | `rax` | `0x280` | `mov byte ptr [rax + rbx + 0x280], cl` |
| `0x001DE987` | `rbx` | `0x278` | `mov dword ptr [rbx + 0x278], ecx` |
| `0x001DE98D` | `rbx` | `0x270` | `mov dword ptr [rbx + 0x270], edi` |
| `0x001DE998` | `rbx` | `0x27C` | `mov dword ptr [rbx + 0x27c], ecx` |
| `0x001DE9A8` | `rbx` | `0x27C` | `mov ecx, dword ptr [rbx + 0x27c]` |
| `0x001DE9B1` | `rbx` | `0x27C` | `mov dword ptr [rbx + 0x27c], eax` |
| `0x001DE9D4` | `rbx` | `0x278` | `mov ecx, dword ptr [rbx + 0x278]` |
| `0x001DE9DD` | `rbx` | `0x278` | `mov dword ptr [rbx + 0x278], eax` |
| `0x001DF1C5` | `rcx` | `0x280` | `cmp byte ptr [rcx + rbx + 0x280], 0` |
| `0x001DF206` | `rbx` | `0x258` | `cmp dword ptr [rbx + 0x258], 0` |
| `0x001DF213` | `rbx` | `0x25C` | `cmp dword ptr [rbx + 0x25c], 0` |
| `0x001DF253` | `rbx` | `0x278` | `mov ecx, dword ptr [rbx + 0x278]` |
| `0x001DF25C` | `rbx` | `0x278` | `mov dword ptr [rbx + 0x278], eax` |
| `0x001DF44B` | `rbx` | `0x278` | `mov ecx, dword ptr [rbx + 0x278]` |
| `0x001DF454` | `rbx` | `0x278` | `mov dword ptr [rbx + 0x278], eax` |

## RegisterOp helper call context `0x001DF246`

```asm
0x001DF0AA: xor eax, 0x6f
0x001DF0AD: mov byte ptr [rbp - 0x72], al
0x001DF0B0: movsx ecx, byte ptr [rbp - 0x72]
0x001DF0B4: mov eax, dword ptr [rsp + 0x30]
0x001DF0B8: add al, 0x57
0x001DF0BA: xor eax, ecx
0x001DF0BC: xor eax, 0x20
0x001DF0BF: mov byte ptr [rbp - 0x71], al
0x001DF0C2: movsx ecx, byte ptr [rbp - 0x71]
0x001DF0C6: mov eax, dword ptr [rsp + 0x30]
0x001DF0CA: add al, 0x58
0x001DF0CC: xor eax, ecx
0x001DF0CE: xor eax, 0x73
0x001DF0D1: mov byte ptr [rbp - 0x70], al
0x001DF0D4: movsx ecx, byte ptr [rbp - 0x70]
0x001DF0D8: mov eax, dword ptr [rsp + 0x30]
0x001DF0DC: add al, 0x59
0x001DF0DE: xor eax, ecx
0x001DF0E0: xor eax, 0x65
0x001DF0E3: mov byte ptr [rbp - 0x6f], al
0x001DF0E6: movsx ecx, byte ptr [rbp - 0x6f]
0x001DF0EA: mov eax, dword ptr [rsp + 0x30]
0x001DF0EE: add al, 0x5a
0x001DF0F0: xor eax, ecx
0x001DF0F2: xor eax, 0x74
0x001DF0F5: mov byte ptr [rbp - 0x6e], al
0x001DF0F8: movsx ecx, byte ptr [rbp - 0x6e]
0x001DF0FC: mov eax, dword ptr [rsp + 0x30]
0x001DF100: add al, 0x5b
0x001DF102: xor eax, ecx
0x001DF104: xor eax, 0x20
0x001DF107: mov byte ptr [rbp - 0x6d], al
0x001DF10A: movsx ecx, byte ptr [rbp - 0x6d]
0x001DF10E: mov eax, dword ptr [rsp + 0x30]
0x001DF112: add al, 0x5c
0x001DF114: xor eax, ecx
0x001DF116: xor eax, 0x73
0x001DF119: mov byte ptr [rbp - 0x6c], al
0x001DF11C: movsx ecx, byte ptr [rbp - 0x6c]
0x001DF120: mov eax, dword ptr [rsp + 0x30]
0x001DF124: add al, 0x5d
0x001DF126: xor eax, ecx
0x001DF128: xor eax, 0x74
0x001DF12B: mov byte ptr [rbp - 0x6b], al
0x001DF12E: movsx ecx, byte ptr [rbp - 0x6b]
0x001DF132: mov eax, dword ptr [rsp + 0x30]
0x001DF136: add al, 0x5e
0x001DF138: xor eax, ecx
0x001DF13A: xor eax, 0x72
0x001DF13D: mov byte ptr [rbp - 0x6a], al
0x001DF140: movsx ecx, byte ptr [rbp - 0x6a]
0x001DF144: mov eax, dword ptr [rsp + 0x30]
0x001DF148: add al, 0x5f
0x001DF14A: xor eax, ecx
0x001DF14C: xor eax, 0x61
0x001DF14F: mov byte ptr [rbp - 0x69], al
0x001DF152: movsx ecx, byte ptr [rbp - 0x69]
0x001DF156: mov eax, dword ptr [rsp + 0x30]
0x001DF15A: add al, 0x60
0x001DF15C: xor eax, ecx
0x001DF15E: xor eax, 0x70
0x001DF161: mov byte ptr [rbp - 0x68], al
0x001DF164: movsx ecx, byte ptr [rbp - 0x68]
0x001DF168: mov eax, dword ptr [rsp + 0x30]
0x001DF16C: add al, 0x61
0x001DF16E: xor eax, ecx
0x001DF170: xor eax, 0x73
0x001DF173: mov byte ptr [rbp - 0x67], al
0x001DF176: xor eax, eax
0x001DF178: mov byte ptr [rbp - 0x66], al
0x001DF17B: movzx eax, byte ptr [rsp + 0x38]
0x001DF180: lea rdx, [rbp + 0x60]
0x001DF184: lea rcx, [rsp + 0x30]
0x001DF189: call 0x1401eb4a0
0x001DF18E: nop
0x001DF18F: cmp qword ptr [rax + 0x18], 0x10
0x001DF194: jb 0x1401df199
0x001DF196: mov rax, qword ptr [rax]
0x001DF199: lea rdx, [rbx + 8]
0x001DF19D: mov rcx, rax
0x001DF1A0: call 0x140040530
0x001DF1A5: nop
0x001DF1A6: lea rcx, [rbp + 0x60]
0x001DF1AA: jmp 0x1401df603
0x001DF1AF: movsxd rcx, edi
0x001DF1B2: imul rax, rcx, 0x5c
0x001DF1B6: lea rsi, [rbx + 0x144]
0x001DF1BD: add rsi, rax
0x001DF1C0: cmp dword ptr [rsi], 0
0x001DF1C3: jne 0x1401df206
0x001DF1C5: cmp byte ptr [rcx + rbx + 0x280], 0
0x001DF1CD: jne 0x1401df206
0x001DF1CF: movaps xmm0, xmmword ptr [rbp]
0x001DF1D3: movups xmmword ptr [rsi], xmm0
0x001DF1D6: movaps xmm1, xmmword ptr [rbp + 0x10]
0x001DF1DA: movups xmmword ptr [rsi + 0x10], xmm1
0x001DF1DE: movaps xmm0, xmmword ptr [rbp + 0x20]
0x001DF1E2: movups xmmword ptr [rsi + 0x20], xmm0
0x001DF1E6: movaps xmm1, xmmword ptr [rbp + 0x30]
0x001DF1EA: movups xmmword ptr [rsi + 0x30], xmm1
0x001DF1EE: movaps xmm0, xmmword ptr [rbp + 0x40]
0x001DF1F2: movups xmmword ptr [rsi + 0x40], xmm0
0x001DF1F6: movsd xmm1, qword ptr [rbp + 0x50]
0x001DF1FB: movsd qword ptr [rsi + 0x50], xmm1
0x001DF200: mov eax, dword ptr [rbp + 0x58]
0x001DF203: mov dword ptr [rsi + 0x58], eax
0x001DF206: cmp dword ptr [rbx + 0x258], 0
0x001DF20D: jne 0x1401df413
0x001DF213: cmp dword ptr [rbx + 0x25c], 0
0x001DF21A: jne 0x1401df413
0x001DF220: mov rcx, rbx
0x001DF223: call 0x1401d97e0
0x001DF228: test al, al
0x001DF22A: jne 0x1401df413
0x001DF230: cmp dword ptr [rsi], 0
0x001DF233: je 0x1401df608
0x001DF239: mov r9d, edi
0x001DF23C: mov r8, rsi
0x001DF23F: lea rdx, [rbp]
0x001DF243: mov rcx, rbx
0x001DF246: call 0x1401ecb90
0x001DF24B: test al, al
0x001DF24D: jne 0x1401df608
0x001DF253: mov ecx, dword ptr [rbx + 0x278]
0x001DF259: lea eax, [rcx + 1]
0x001DF25C: mov dword ptr [rbx + 0x278], eax
0x001DF262: cmp ecx, 4
0x001DF265: jge 0x1401df608
0x001DF26B: mov dword ptr [rbp - 0x60], 0x21
0x001DF272: mov dword ptr [rbp - 0x5c], 0x7c
0x001DF279: mov eax, dword ptr [rbp - 0x5c]
0x001DF27C: xor eax, 0x5a
0x001DF27F: mov byte ptr [rbp - 0x58], al
0x001DF282: movsx ecx, byte ptr [rbp - 0x58]
0x001DF286: xor ecx, 0x5c
0x001DF289: mov byte ptr [rbp - 0x57], cl
0x001DF28C: movsx ecx, byte ptr [rbp - 0x57]
0x001DF290: xor ecx, 0x1b
0x001DF293: mov byte ptr [rbp - 0x56], cl
0x001DF296: movsx ecx, byte ptr [rbp - 0x56]
0x001DF29A: xor ecx, 1
0x001DF29D: mov byte ptr [rbp - 0x55], cl
0x001DF2A0: movsx ecx, byte ptr [rbp - 0x55]
0x001DF2A4: xor ecx, 0x54
0x001DF2A7: mov byte ptr [rbp - 0x54], cl
0x001DF2AA: movsx ecx, byte ptr [rbp - 0x54]
0x001DF2AE: xor ecx, 0x4f
0x001DF2B1: mov byte ptr [rbp - 0x53], cl
0x001DF2B4: movsx ecx, byte ptr [rbp - 0x53]
0x001DF2B8: xor ecx, 0x40
0x001DF2BB: mov byte ptr [rbp - 0x52], cl
0x001DF2BE: movsx ecx, byte ptr [rbp - 0x52]
0x001DF2C2: xor ecx, 0x43
0x001DF2C5: mov byte ptr [rbp - 0x51], cl
0x001DF2C8: movsx ecx, byte ptr [rbp - 0x51]
0x001DF2CC: xor ecx, 0x4d
0x001DF2CF: mov byte ptr [rbp - 0x50], cl
0x001DF2D2: movsx ecx, byte ptr [rbp - 0x50]
0x001DF2D6: xor ecx, 0x44
0x001DF2D9: mov byte ptr [rbp - 0x4f], cl
```


## RegisterOp helper call context `0x001DF43E`

```asm
0x001DF29D: mov byte ptr [rbp - 0x55], cl
0x001DF2A0: movsx ecx, byte ptr [rbp - 0x55]
0x001DF2A4: xor ecx, 0x54
0x001DF2A7: mov byte ptr [rbp - 0x54], cl
0x001DF2AA: movsx ecx, byte ptr [rbp - 0x54]
0x001DF2AE: xor ecx, 0x4f
0x001DF2B1: mov byte ptr [rbp - 0x53], cl
0x001DF2B4: movsx ecx, byte ptr [rbp - 0x53]
0x001DF2B8: xor ecx, 0x40
0x001DF2BB: mov byte ptr [rbp - 0x52], cl
0x001DF2BE: movsx ecx, byte ptr [rbp - 0x52]
0x001DF2C2: xor ecx, 0x43
0x001DF2C5: mov byte ptr [rbp - 0x51], cl
0x001DF2C8: movsx ecx, byte ptr [rbp - 0x51]
0x001DF2CC: xor ecx, 0x4d
0x001DF2CF: mov byte ptr [rbp - 0x50], cl
0x001DF2D2: movsx ecx, byte ptr [rbp - 0x50]
0x001DF2D6: xor ecx, 0x44
0x001DF2D9: mov byte ptr [rbp - 0x4f], cl
0x001DF2DC: movsx ecx, byte ptr [rbp - 0x4f]
0x001DF2E0: xor ecx, 1
0x001DF2E3: mov byte ptr [rbp - 0x4e], cl
0x001DF2E6: movsx ecx, byte ptr [rbp - 0x4e]
0x001DF2EA: xor ecx, 0x55
0x001DF2ED: mov byte ptr [rbp - 0x4d], cl
0x001DF2F0: movsx ecx, byte ptr [rbp - 0x4d]
0x001DF2F4: xor ecx, 0x4e
0x001DF2F7: mov byte ptr [rbp - 0x4c], cl
0x001DF2FA: movsx ecx, byte ptr [rbp - 0x4c]
0x001DF2FE: xor ecx, 1
0x001DF301: mov byte ptr [rbp - 0x4b], cl
0x001DF304: movsx ecx, byte ptr [rbp - 0x4b]
0x001DF308: xor ecx, 0x52
0x001DF30B: mov byte ptr [rbp - 0x4a], cl
0x001DF30E: movsx ecx, byte ptr [rbp - 0x4a]
0x001DF312: xor ecx, 0x44
0x001DF315: mov byte ptr [rbp - 0x49], cl
0x001DF318: movsx ecx, byte ptr [rbp - 0x49]
0x001DF31C: xor ecx, 0x55
0x001DF31F: mov byte ptr [rbp - 0x48], cl
0x001DF322: movsx ecx, byte ptr [rbp - 0x48]
0x001DF326: xor ecx, 1
0x001DF329: mov byte ptr [rbp - 0x47], cl
0x001DF32C: movsx ecx, byte ptr [rbp - 0x47]
0x001DF330: xor ecx, 0x52
0x001DF333: mov byte ptr [rbp - 0x46], cl
0x001DF336: movsx ecx, byte ptr [rbp - 0x46]
0x001DF33A: xor ecx, 0x55
0x001DF33D: mov byte ptr [rbp - 0x45], cl
0x001DF340: movsx ecx, byte ptr [rbp - 0x45]
0x001DF344: xor ecx, 0x53
0x001DF347: mov byte ptr [rbp - 0x44], cl
0x001DF34A: movsx ecx, byte ptr [rbp - 0x44]
0x001DF34E: xor ecx, 0x40
0x001DF351: mov byte ptr [rbp - 0x43], cl
0x001DF354: movsx ecx, byte ptr [rbp - 0x43]
0x001DF358: xor ecx, 0x51
0x001DF35B: mov byte ptr [rbp - 0x42], cl
0x001DF35E: movsx ecx, byte ptr [rbp - 0x42]
0x001DF362: xor ecx, 0x52
0x001DF365: mov byte ptr [rbp - 0x41], cl
0x001DF368: movsx ecx, byte ptr [rbp - 0x41]
0x001DF36C: xor ecx, 0x1b
0x001DF36F: mov byte ptr [rbp - 0x40], cl
0x001DF372: movsx ecx, byte ptr [rbp - 0x40]
0x001DF376: xor ecx, 1
0x001DF379: mov byte ptr [rbp - 0x3f], cl
0x001DF37C: movsx ecx, byte ptr [rbp - 0x3f]
0x001DF380: xor ecx, 1
0x001DF383: mov byte ptr [rbp - 0x3e], cl
0x001DF386: movsx ecx, byte ptr [rbp - 0x3e]
0x001DF38A: xor ecx, 0x44
0x001DF38D: mov byte ptr [rbp - 0x3d], cl
0x001DF390: movsx ecx, byte ptr [rbp - 0x3d]
0x001DF394: xor ecx, 0x53
0x001DF397: mov byte ptr [rbp - 0x3c], cl
0x001DF39A: movsx ecx, byte ptr [rbp - 0x3c]
0x001DF39E: xor ecx, 0x53
0x001DF3A1: mov byte ptr [rbp - 0x3b], cl
0x001DF3A4: movsx ecx, byte ptr [rbp - 0x3b]
0x001DF3A8: xor ecx, 0x4e
0x001DF3AB: mov byte ptr [rbp - 0x3a], cl
0x001DF3AE: movsx ecx, byte ptr [rbp - 0x3a]
0x001DF3B2: xor ecx, 0x53
0x001DF3B5: mov byte ptr [rbp - 0x39], cl
0x001DF3B8: movsx ecx, byte ptr [rbp - 0x39]
0x001DF3BC: xor ecx, 1
0x001DF3BF: mov byte ptr [rbp - 0x38], cl
0x001DF3C2: movsx ecx, byte ptr [rbp - 0x38]
0x001DF3C6: xor ecx, 0x10
0x001DF3C9: mov byte ptr [rbp - 0x37], cl
0x001DF3CC: movsx ecx, byte ptr [rbp - 0x37]
0x001DF3D0: xor ecx, 0x13
0x001DF3D3: mov byte ptr [rbp - 0x36], cl
0x001DF3D6: xor eax, eax
0x001DF3D8: mov byte ptr [rbp - 0x35], al
0x001DF3DB: movzx eax, byte ptr [rbp - 0x58]
0x001DF3DF: lea rdx, [rbp + 0x80]
0x001DF3E6: lea rcx, [rbp - 0x60]
0x001DF3EA: call 0x1400dcdd0
0x001DF3EF: nop
0x001DF3F0: cmp qword ptr [rax + 0x18], 0x10
0x001DF3F5: jb 0x1401df3fa
0x001DF3F7: mov rax, qword ptr [rax]
0x001DF3FA: lea rdx, [rbx + 8]
0x001DF3FE: mov rcx, rax
0x001DF401: call 0x140040530
0x001DF406: nop
0x001DF407: lea rcx, [rbp + 0x80]
0x001DF40E: jmp 0x1401df603
0x001DF413: mov r8d, edi
0x001DF416: lea rdx, [rbp + 0xc0]
0x001DF41D: mov rcx, rbx
0x001DF420: call 0x1401d7930
0x001DF425: test al, al
0x001DF427: je 0x1401df608
0x001DF42D: mov r9d, edi
0x001DF430: lea r8, [rbp + 0xc0]
0x001DF437: lea rdx, [rbp]
0x001DF43B: mov rcx, rbx
0x001DF43E: call 0x1401ecb90
0x001DF443: test al, al
0x001DF445: jne 0x1401df608
0x001DF44B: mov ecx, dword ptr [rbx + 0x278]
0x001DF451: lea eax, [rcx + 1]
0x001DF454: mov dword ptr [rbx + 0x278], eax
0x001DF45A: cmp ecx, 4
0x001DF45D: jge 0x1401df608
0x001DF463: mov dword ptr [rbp - 0x30], 0x6c
0x001DF46A: mov dword ptr [rbp - 0x2c], 0x1f
0x001DF471: mov eax, dword ptr [rbp - 0x2c]
0x001DF474: xor eax, 0x17
0x001DF477: mov byte ptr [rbp - 0x28], al
0x001DF47A: movsx ecx, byte ptr [rbp - 0x28]
0x001DF47E: xor ecx, 0x11
0x001DF481: mov byte ptr [rbp - 0x27], cl
0x001DF484: movsx ecx, byte ptr [rbp - 0x27]
0x001DF488: xor ecx, 0x56
0x001DF48B: mov byte ptr [rbp - 0x26], cl
0x001DF48E: movsx ecx, byte ptr [rbp - 0x26]
0x001DF492: xor ecx, 0x4c
0x001DF495: mov byte ptr [rbp - 0x25], cl
0x001DF498: movsx ecx, byte ptr [rbp - 0x25]
0x001DF49C: xor ecx, 0x19
0x001DF49F: mov byte ptr [rbp - 0x24], cl
0x001DF4A2: movsx ecx, byte ptr [rbp - 0x24]
0x001DF4A6: xor ecx, 2
0x001DF4A9: mov byte ptr [rbp - 0x23], cl
0x001DF4AC: movsx ecx, byte ptr [rbp - 0x23]
0x001DF4B0: xor ecx, 0xd
0x001DF4B3: mov byte ptr [rbp - 0x22], cl
0x001DF4B6: movsx ecx, byte ptr [rbp - 0x22]
0x001DF4BA: xor ecx, 0xe
0x001DF4BD: mov byte ptr [rbp - 0x21], cl
0x001DF4C0: movsx eax, byte ptr [rbp - 0x21]
0x001DF4C4: mov byte ptr [rbp - 0x20], al
0x001DF4C7: movsx ecx, byte ptr [rbp - 0x20]
0x001DF4CB: xor ecx, 9
0x001DF4CE: mov byte ptr [rbp - 0x1f], cl
0x001DF4D1: movsx ecx, byte ptr [rbp - 0x1f]
```
