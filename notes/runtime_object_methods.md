# Runtime object snapshot methods

## target `0x00084A60` PDATA `0x00084A60..0x00084B48`

```asm
0x00084A60: push rdi
0x00084A62: sub rsp, 0x30
0x00084A66: mov qword ptr [rsp + 0x20], 0xfffffffffffffffe
0x00084A6F: mov qword ptr [rsp + 0x40], rbx
0x00084A74: mov qword ptr [rsp + 0x48], rsi
0x00084A79: mov rdi, rdx
0x00084A7C: mov rsi, rcx
0x00084A7F: add rcx, 0x318
0x00084A86: call 0x140391ac4
0x00084A8B: test eax, eax
0x00084A8D: je 0x140084a96
0x00084A8F: mov ecx, eax
0x00084A91: call 0x14039219c
0x00084A96: lea rax, [rsi + 0x368]
0x00084A9D: movups xmm0, xmmword ptr [rax]
0x00084AA0: movups xmmword ptr [rdi], xmm0
0x00084AA3: movups xmm1, xmmword ptr [rax + 0x10]
0x00084AA7: movups xmmword ptr [rdi + 0x10], xmm1
0x00084AAB: movups xmm0, xmmword ptr [rax + 0x20]
0x00084AAF: movups xmmword ptr [rdi + 0x20], xmm0
0x00084AB3: movups xmm1, xmmword ptr [rax + 0x30]
0x00084AB7: movups xmmword ptr [rdi + 0x30], xmm1
0x00084ABB: movups xmm0, xmmword ptr [rax + 0x40]
0x00084ABF: movups xmmword ptr [rdi + 0x40], xmm0
0x00084AC3: movups xmm1, xmmword ptr [rax + 0x50]
0x00084AC7: movups xmmword ptr [rdi + 0x50], xmm1
0x00084ACB: movups xmm0, xmmword ptr [rax + 0x60]
0x00084ACF: movups xmmword ptr [rdi + 0x60], xmm0
0x00084AD3: lea r8, [rdi + 0x80]
0x00084ADA: movups xmm0, xmmword ptr [rax + 0x70]
0x00084ADE: movups xmmword ptr [r8 - 0x10], xmm0
0x00084AE3: lea rax, [rax + 0x80]
0x00084AEA: movups xmm1, xmmword ptr [rax]
0x00084AED: movups xmmword ptr [r8], xmm1
0x00084AF1: movups xmm0, xmmword ptr [rax + 0x10]
0x00084AF5: movups xmmword ptr [r8 + 0x10], xmm0
0x00084AFA: movups xmm1, xmmword ptr [rax + 0x20]
0x00084AFE: movups xmmword ptr [r8 + 0x20], xmm1
0x00084B03: movups xmm0, xmmword ptr [rax + 0x30]
0x00084B07: movups xmmword ptr [r8 + 0x30], xmm0
0x00084B0C: movups xmm1, xmmword ptr [rax + 0x40]
0x00084B10: movups xmmword ptr [r8 + 0x40], xmm1
0x00084B15: mov rax, qword ptr [rax + 0x50]
0x00084B19: mov qword ptr [r8 + 0x50], rax
0x00084B1D: lea rcx, [rsi + 0x318]
0x00084B24: call 0x140391b24
0x00084B29: test eax, eax
0x00084B2B: je 0x140084b35
0x00084B2D: mov ecx, eax
0x00084B2F: call 0x14039219c
0x00084B34: nop
0x00084B35: mov rax, rdi
0x00084B38: mov rbx, qword ptr [rsp + 0x40]
0x00084B3D: mov rsi, qword ptr [rsp + 0x48]
0x00084B42: add rsp, 0x30
0x00084B46: pop rdi
0x00084B47: ret
```

### Direct callers

- `0x0006FA42` in `0x0006F940..0x000700E0`
- `0x0007011F` in `0x000700E0..0x00070187`
- `0x00134DBC` in `0x00134D80..0x00134FE0`
- `0x0013AE35` in `0x0013A9F0..0x0013AE7A`
- `0x0013C064` in `0x0013BFD0..0x0013C0F3`
- `0x0013ECA7` in `0x0013E6D0..0x0013EEA1`
- `0x0013F888` in `0x0013F7E0..0x0013FCC0`
- `0x001689B0` in `0x001688D0..0x001694C0`
- `0x001690C2` in `0x001688D0..0x001694C0`
- `0x00172C76` in `0x00172C10..0x00173AF2`
- `0x001B2954` in `0x001B22D0..0x001B5154`
- `0x001B31F4` in `0x001B22D0..0x001B5154`
- `0x001CF954` in `0x001CF8B0..0x001CFEC5`
- `0x001F27C5` in `0x001F21F0..0x001F2897`
- `0x0020324E` in `0x00201A80..0x0020424F`

## target `0x001362D0` PDATA `0x001362D0..0x00136447`

```asm
0x001362D0: push rdi
0x001362D2: sub rsp, 0x30
0x001362D6: mov qword ptr [rsp + 0x20], 0xfffffffffffffffe
0x001362DF: mov qword ptr [rsp + 0x40], rbx
0x001362E4: mov qword ptr [rsp + 0x48], rsi
0x001362E9: mov rsi, rdx
0x001362EC: mov rdi, rcx
0x001362EF: add rcx, 0x318
0x001362F6: call 0x140391ac4
0x001362FB: test eax, eax
0x001362FD: je 0x140136306
0x001362FF: mov ecx, eax
0x00136301: call 0x14039219c
0x00136306: lea r8, [rdi + 0x368]
0x0013630D: movups xmm0, xmmword ptr [rsi]
0x00136310: movups xmmword ptr [r8], xmm0
0x00136314: movups xmm1, xmmword ptr [rsi + 0x10]
0x00136318: movups xmmword ptr [r8 + 0x10], xmm1
0x0013631D: movups xmm0, xmmword ptr [rsi + 0x20]
0x00136321: movups xmmword ptr [r8 + 0x20], xmm0
0x00136326: movups xmm1, xmmword ptr [rsi + 0x30]
0x0013632A: movups xmmword ptr [r8 + 0x30], xmm1
0x0013632F: movups xmm0, xmmword ptr [rsi + 0x40]
0x00136333: movups xmmword ptr [r8 + 0x40], xmm0
0x00136338: movups xmm1, xmmword ptr [rsi + 0x50]
0x0013633C: movups xmmword ptr [r8 + 0x50], xmm1
0x00136341: movups xmm0, xmmword ptr [rsi + 0x60]
0x00136345: movups xmmword ptr [r8 + 0x60], xmm0
0x0013634A: lea r8, [r8 + 0x80]
0x00136351: movups xmm0, xmmword ptr [rsi + 0x70]
0x00136355: movups xmmword ptr [r8 - 0x10], xmm0
0x0013635A: lea rax, [rsi + 0x80]
0x00136361: movups xmm1, xmmword ptr [rax]
0x00136364: movups xmmword ptr [r8], xmm1
0x00136368: movups xmm0, xmmword ptr [rax + 0x10]
0x0013636C: movups xmmword ptr [r8 + 0x10], xmm0
0x00136371: movups xmm1, xmmword ptr [rax + 0x20]
0x00136375: movups xmmword ptr [r8 + 0x20], xmm1
0x0013637A: movups xmm0, xmmword ptr [rax + 0x30]
0x0013637E: movups xmmword ptr [r8 + 0x30], xmm0
0x00136383: movups xmm1, xmmword ptr [rax + 0x40]
0x00136387: movups xmmword ptr [r8 + 0x40], xmm1
0x0013638C: mov rax, qword ptr [rax + 0x50]
0x00136390: mov qword ptr [r8 + 0x50], rax
0x00136394: lea rcx, [rdi + 0x440]
0x0013639B: movups xmm0, xmmword ptr [rsi]
0x0013639E: movups xmmword ptr [rcx], xmm0
0x001363A1: movups xmm1, xmmword ptr [rsi + 0x10]
0x001363A5: movups xmmword ptr [rcx + 0x10], xmm1
0x001363A9: movups xmm0, xmmword ptr [rsi + 0x20]
0x001363AD: movups xmmword ptr [rcx + 0x20], xmm0
0x001363B1: movups xmm1, xmmword ptr [rsi + 0x30]
0x001363B5: movups xmmword ptr [rcx + 0x30], xmm1
0x001363B9: movups xmm0, xmmword ptr [rsi + 0x40]
0x001363BD: movups xmmword ptr [rcx + 0x40], xmm0
0x001363C1: movups xmm1, xmmword ptr [rsi + 0x50]
0x001363C5: movups xmmword ptr [rcx + 0x50], xmm1
0x001363C9: movups xmm0, xmmword ptr [rsi + 0x60]
0x001363CD: movups xmmword ptr [rcx + 0x60], xmm0
0x001363D1: lea rcx, [rcx + 0x80]
0x001363D8: movups xmm1, xmmword ptr [rsi + 0x70]
0x001363DC: movups xmmword ptr [rcx - 0x10], xmm1
0x001363E0: sub rsi, -0x80
0x001363E4: movups xmm0, xmmword ptr [rsi]
0x001363E7: movups xmmword ptr [rcx], xmm0
0x001363EA: movups xmm1, xmmword ptr [rsi + 0x10]
0x001363EE: movups xmmword ptr [rcx + 0x10], xmm1
0x001363F2: movups xmm0, xmmword ptr [rsi + 0x20]
0x001363F6: movups xmmword ptr [rcx + 0x20], xmm0
0x001363FA: movups xmm1, xmmword ptr [rsi + 0x30]
0x001363FE: movups xmmword ptr [rcx + 0x30], xmm1
0x00136402: movups xmm0, xmmword ptr [rsi + 0x40]
0x00136406: movups xmmword ptr [rcx + 0x40], xmm0
0x0013640A: mov rax, qword ptr [rsi + 0x50]
0x0013640E: mov qword ptr [rcx + 0x50], rax
0x00136412: lea rcx, [rdi + 0x318]
0x00136419: call 0x140391b24
0x0013641E: test eax, eax
0x00136420: je 0x14013642a
0x00136422: mov ecx, eax
0x00136424: call 0x14039219c
0x00136429: nop
0x0013642A: mov eax, 1
0x0013642F: lock xadd dword ptr [rdi + 0x538], eax
0x00136437: mov rbx, qword ptr [rsp + 0x40]
0x0013643C: mov rsi, qword ptr [rsp + 0x48]
0x00136441: add rsp, 0x30
0x00136445: pop rdi
0x00136446: ret
```

### Direct callers

- `0x0006FCC2` in `0x0006F940..0x000700E0`
- `0x0013F8A0` in `0x0013F7E0..0x0013FCC0`
- `0x001780F9` in `0x00177F40..0x0017857B`
- `0x00178131` in `0x00177F40..0x0017857B`
