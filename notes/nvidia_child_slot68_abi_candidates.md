# Child slot +0x68 callsites filtered by mode-setter ABI

Confirmed setter ABI: `RCX=child`, `EDX=preset`, `R8D=VMR`, `R9=&aux`.

candidates score>=2: `15`

## `0x001F94A5` score `3/3` in `0x001F7F40..0x001FB9C1`

Recent ABI defs:

- `r9` <- `0x001F9475: mov r9, r12`
- `r8d` <- `0x001F9478: lea r8d, [rcx + 4]`
- `rdx` <- `0x001F947C: mov rdx, qword ptr [rdi + rbx*8 + 0x1c8]`
- `rdx` <- `0x001F949F: mov rdx, r12`

```asm
0x001F943C: xor ecx, ecx
0x001F943E: mov qword ptr [rsp + 0x68], rcx
0x001F9443: mov dword ptr [rsp + 0x70], ecx
0x001F9447: movsxd rbx, r13d
0x001F944A: cmp r13d, r14d
0x001F944D: jne 0x1401f945a
0x001F944F: test r15b, r15b
0x001F9452: jne 0x1401fa42e
0x001F9458: jmp 0x1401f945f
0x001F945A: test r15b, r15b
0x001F945D: jne 0x1401f94a8
0x001F945F: cmp byte ptr [rsp + 0x52], 0
0x001F9464: je 0x1401f94a8
0x001F9466: mov rax, qword ptr [rbp + 0xb0]
0x001F946D: xor ecx, ecx
0x001F946F: mov dword ptr [rax], ecx
0x001F9471: mov r12, qword ptr [rbp + 0x70]
0x001F9475: mov r9, r12
0x001F9478: lea r8d, [rcx + 4]
0x001F947C: mov rdx, qword ptr [rdi + rbx*8 + 0x1c8]
0x001F9484: mov rcx, qword ptr [rdi + rbx*8 + 0x1b8]
0x001F948C: call 0x1402917f8
0x001F9491: mov dword ptr [rbp - 0x40], eax
0x001F9494: test eax, eax
0x001F9496: jne 0x1401fa7d5
0x001F949C: mov rax, qword ptr [rdi]
0x001F949F: mov rdx, r12
0x001F94A2: mov rcx, rdi
0x001F94A5: call qword ptr [rax + 0x68]
0x001F94A8: mov ecx, dword ptr [rsp + 0x64]
0x001F94AC: mov rdx, qword ptr [rbp + 0x1290]
0x001F94B3: mov r13d, r14d
0x001F94B6: mov dword ptr [rsp + 0x58], r14d
0x001F94BB: test r15b, r15b
0x001F94BE: jne 0x1401f94d6
0x001F94C0: inc r14d
0x001F94C3: and r14d, 0x80000001
0x001F94CA: jge 0x1401f94d6
0x001F94CC: dec r14d
0x001F94CF: or r14d, 0xfffffffe
0x001F94D3: inc r14d
0x001F94D6: lea ecx, [rcx + rcx*2]
```

## `0x002B1450` score `3/3` in `0x002B13E0..0x002B14B5`

Recent ABI defs:

- `r9d` <- `0x002B1430: mov r9d, esi`
- `r8` <- `0x002B1433: mov r8, rbp`
- `edx` <- `0x002B143A: mov edx, 0x17`

```asm
0x002B13DE: int3
0x002B13DF: int3
0x002B13E0: mov qword ptr [rsp + 8], rbx
0x002B13E5: mov qword ptr [rsp + 0x10], rbp
0x002B13EA: mov qword ptr [rsp + 0x18], rsi
0x002B13EF: push rdi
0x002B13F0: mov eax, 0x30
0x002B13F5: call 0x1403b2500
0x002B13FA: sub rsp, rax
0x002B13FD: mov rbx, rcx
0x002B1400: mov edi, r9d
0x002B1403: xor ecx, ecx
0x002B1405: mov esi, r8d
0x002B1408: mov rbp, rdx
0x002B140B: call qword ptr [rip + 0x17edef]
0x002B1411: mov rax, qword ptr [rbx + 0x80]
0x002B1418: cmp dword ptr [rax + 0x1dc], 0
0x002B141F: je 0x1402b1429
0x002B1421: mov rcx, rbx
0x002B1424: call 0x1402b14f0
0x002B1429: mov rax, qword ptr [rbx + 0x80]
0x002B1430: mov r9d, esi
0x002B1433: mov r8, rbp
0x002B1436: mov dword ptr [rsp + 0x20], edi
0x002B143A: mov edx, 0x17
0x002B143F: mov rcx, rbx
0x002B1442: mov dword ptr [rax + 0x1e8], 1
0x002B144C: mov rax, qword ptr [rbx + 8]
0x002B1450: call qword ptr [rax + 0x68]
0x002B1453: mov r8d, eax
0x002B1456: cmp eax, -1
0x002B1459: jne 0x1402b148c
0x002B145B: mov rcx, qword ptr [rbx + 0x80]
0x002B1462: cmp dword ptr [rcx + 0x1e8], 2
0x002B1469: jne 0x1402b148c
0x002B146B: mov rax, qword ptr [rbx + 8]
0x002B146F: mov r9d, esi
0x002B1472: inc dword ptr [rbx + 0x2c]
0x002B1475: mov r8, rbp
0x002B1478: mov edx, 0x17
0x002B147D: mov dword ptr [rsp + 0x20], edi
0x002B1481: mov rcx, rbx
```

## `0x002B1484` score `3/3` in `0x002B13E0..0x002B14B5`

Recent ABI defs:

- `r9d` <- `0x002B1430: mov r9d, esi`
- `r8` <- `0x002B1433: mov r8, rbp`
- `edx` <- `0x002B143A: mov edx, 0x17`
- `r8d` <- `0x002B1453: mov r8d, eax`
- `r9d` <- `0x002B146F: mov r9d, esi`
- `r8` <- `0x002B1475: mov r8, rbp`
- `edx` <- `0x002B1478: mov edx, 0x17`

```asm
0x002B140B: call qword ptr [rip + 0x17edef]
0x002B1411: mov rax, qword ptr [rbx + 0x80]
0x002B1418: cmp dword ptr [rax + 0x1dc], 0
0x002B141F: je 0x1402b1429
0x002B1421: mov rcx, rbx
0x002B1424: call 0x1402b14f0
0x002B1429: mov rax, qword ptr [rbx + 0x80]
0x002B1430: mov r9d, esi
0x002B1433: mov r8, rbp
0x002B1436: mov dword ptr [rsp + 0x20], edi
0x002B143A: mov edx, 0x17
0x002B143F: mov rcx, rbx
0x002B1442: mov dword ptr [rax + 0x1e8], 1
0x002B144C: mov rax, qword ptr [rbx + 8]
0x002B1450: call qword ptr [rax + 0x68]
0x002B1453: mov r8d, eax
0x002B1456: cmp eax, -1
0x002B1459: jne 0x1402b148c
0x002B145B: mov rcx, qword ptr [rbx + 0x80]
0x002B1462: cmp dword ptr [rcx + 0x1e8], 2
0x002B1469: jne 0x1402b148c
0x002B146B: mov rax, qword ptr [rbx + 8]
0x002B146F: mov r9d, esi
0x002B1472: inc dword ptr [rbx + 0x2c]
0x002B1475: mov r8, rbp
0x002B1478: mov edx, 0x17
0x002B147D: mov dword ptr [rsp + 0x20], edi
0x002B1481: mov rcx, rbx
0x002B1484: call qword ptr [rax + 0x68]
0x002B1487: dec dword ptr [rbx + 0x2c]
0x002B148A: jmp 0x1402b14a0
0x002B148C: mov rax, qword ptr [rbx + 0x80]
0x002B1493: mov dword ptr [rax + 0x1e8], 0
0x002B149D: mov eax, r8d
0x002B14A0: mov rbx, qword ptr [rsp + 0x40]
0x002B14A5: mov rbp, qword ptr [rsp + 0x48]
0x002B14AA: mov rsi, qword ptr [rsp + 0x50]
0x002B14AF: add rsp, 0x30
0x002B14B3: pop rdi
0x002B14B4: ret
0x002B14B5: int3
0x002B14B6: int3
```

## `0x002B16D1` score `3/3` in `0x002B1630..0x002B170A`

Recent ABI defs:

- `r9d` <- `0x002B16BE: xor r9d, r9d`
- `r8d` <- `0x002B16C1: xor r8d, r8d`
- `edx` <- `0x002B16CC: xor edx, edx`

```asm
0x002B1670: call 0x1402a8db0
0x002B1675: mov rax, qword ptr [rbx + 0x80]
0x002B167C: cmp dword ptr [rax + 0x1d4], 0
0x002B1683: je 0x1402b16da
0x002B1685: or eax, 0xffffffff
0x002B1688: add rsp, 0x30
0x002B168C: pop rbx
0x002B168D: ret
0x002B168E: mov rax, qword ptr [rbx + 0x80]
0x002B1695: cmp dword ptr [rax + 0x1d4], 0
0x002B169C: je 0x1402b16b5
0x002B169E: mov rax, qword ptr [rbx + 8]
0x002B16A2: mov rcx, rbx
0x002B16A5: call qword ptr [rax + 0x78]
0x002B16A8: cmp eax, -1
0x002B16AB: jne 0x1402b16da
0x002B16AD: or eax, eax
0x002B16AF: add rsp, 0x30
0x002B16B3: pop rbx
0x002B16B4: ret
0x002B16B5: test cl, 2
0x002B16B8: jne 0x1402b16da
0x002B16BA: mov rax, qword ptr [rbx + 8]
0x002B16BE: xor r9d, r9d
0x002B16C1: xor r8d, r8d
0x002B16C4: mov dword ptr [rsp + 0x20], 0
0x002B16CC: xor edx, edx
0x002B16CE: mov rcx, rbx
0x002B16D1: call qword ptr [rax + 0x68]
0x002B16D4: test byte ptr [rbx + 0x44], 2
0x002B16D8: je 0x1402b1685
0x002B16DA: cmp dword ptr [rbx + 0x44], 3
0x002B16DE: jne 0x1402b16f0
0x002B16E0: mov rcx, qword ptr [rbx + 0x80]
0x002B16E7: cmp dword ptr [rcx + 0x1d4], 0
0x002B16EE: je 0x1402b16ff
0x002B16F0: xor eax, eax
0x002B16F2: add rsp, 0x30
0x002B16F6: pop rbx
0x002B16F7: ret
0x002B16F8: mov dword ptr [rcx + 0x44], 3
0x002B16FF: mov eax, 1
```

## `0x002B1DA1` score `3/3` in `0x002B1CB0..0x002B2005`

Recent ABI defs:

- `r9d` <- `0x002B1D84: mov r9d, 4`
- `r9d` <- `0x002B1D8E: sub r9d, eax`
- `edx` <- `0x002B1D91: mov edx, 0x16`
- `r8` <- `0x002B1D9D: lea r8, [rdi + rax]`

```asm
0x002B1D20: jmp 0x1402b1e8e
0x002B1D25: mov rax, qword ptr [rsp + 0x78]
0x002B1D2A: mov dword ptr [rax], 1
0x002B1D30: mov rax, qword ptr [rcx + 0x50]
0x002B1D34: mov dword ptr [rcx + 0x48], r14d
0x002B1D38: mov rcx, qword ptr [rax + 8]
0x002B1D3C: mov rax, qword ptr [rbx + 0x80]
0x002B1D43: add rcx, 4
0x002B1D47: mov qword ptr [rbx + 0x58], rcx
0x002B1D4B: mov eax, dword ptr [rax + 0x398]
0x002B1D51: mov dword ptr [rbx + 0x60], eax
0x002B1D54: jmp 0x1402b1fea
0x002B1D59: mov rax, qword ptr [rcx + 0x50]
0x002B1D5D: mov rdi, qword ptr [rax + 8]
0x002B1D61: cmp dword ptr [rcx + 0x48], edx
0x002B1D64: jne 0x1402b1f21
0x002B1D6A: nop word ptr [rax + rax]
0x002B1D70: cmp dword ptr [rbx + 0x60], 4
0x002B1D74: jge 0x1402b1db4
0x002B1D76: nop word ptr [rax + rax]
0x002B1D80: movsxd rax, dword ptr [rbx + 0x60]
0x002B1D84: mov r9d, 4
0x002B1D8A: mov r10, qword ptr [rbx + 8]
0x002B1D8E: sub r9d, eax
0x002B1D91: mov edx, 0x16
0x002B1D96: mov dword ptr [rsp + 0x20], esi
0x002B1D9A: mov rcx, rbx
0x002B1D9D: lea r8, [rdi + rax]
0x002B1DA1: call qword ptr [r10 + 0x68]
0x002B1DA5: mov ecx, eax
0x002B1DA7: test eax, eax
0x002B1DA9: jle 0x1402b1e0e
0x002B1DAB: add dword ptr [rbx + 0x60], eax
0x002B1DAE: cmp dword ptr [rbx + 0x60], 4
0x002B1DB2: jl 0x1402b1d80
0x002B1DB4: cmp dword ptr [rbx + 0x38], esi
0x002B1DB7: jne 0x1402b1e23
0x002B1DB9: cmp byte ptr [rdi], sil
0x002B1DBC: jne 0x1402b1e23
0x002B1DBE: cmp byte ptr [rdi + 1], sil
0x002B1DC2: jne 0x1402b1e23
0x002B1DC4: cmp byte ptr [rdi + 2], sil
```

## `0x002B1F5A` score `3/3` in `0x002B1CB0..0x002B2005`

Recent ABI defs:

- `r8` <- `0x002B1F40: movsxd r8, dword ptr [rbx + 0x60]`
- `r9d` <- `0x002B1F44: mov r9d, edi`
- `r8` <- `0x002B1F4B: add r8, rbp`
- `edx` <- `0x002B1F4E: mov edx, 0x16`

```asm
0x002B1EE5: lea r8d, [rax + 7]
0x002B1EE9: call 0x1402c3c30
0x002B1EEE: mov rax, qword ptr [rsp + 0x78]
0x002B1EF3: mov dword ptr [rax], esi
0x002B1EF5: or eax, 0xffffffff
0x002B1EF8: jmp 0x1402b1fea
0x002B1EFD: mov rax, qword ptr [rbx + 0x80]
0x002B1F04: mov dword ptr [rax + 0x398], ebp
0x002B1F0A: mov rax, qword ptr [rbx + 0x50]
0x002B1F0E: mov dword ptr [rbx + 0x48], r14d
0x002B1F12: mov rcx, qword ptr [rax + 8]
0x002B1F16: add rcx, 4
0x002B1F1A: mov dword ptr [rbx + 0x60], esi
0x002B1F1D: mov qword ptr [rbx + 0x58], rcx
0x002B1F21: mov rax, qword ptr [rbx + 0x80]
0x002B1F28: mov rbp, qword ptr [rbx + 0x58]
0x002B1F2C: mov edi, dword ptr [rax + 0x398]
0x002B1F32: sub edi, dword ptr [rbx + 0x60]
0x002B1F35: test edi, edi
0x002B1F37: jle 0x1402b1f70
0x002B1F39: nop dword ptr [rax]
0x002B1F40: movsxd r8, dword ptr [rbx + 0x60]
0x002B1F44: mov r9d, edi
0x002B1F47: mov rax, qword ptr [rbx + 8]
0x002B1F4B: add r8, rbp
0x002B1F4E: mov edx, 0x16
0x002B1F53: mov dword ptr [rsp + 0x20], esi
0x002B1F57: mov rcx, rbx
0x002B1F5A: call qword ptr [rax + 0x68]
0x002B1F5D: mov ecx, eax
0x002B1F5F: test eax, eax
0x002B1F61: jle 0x1402b1e0e
0x002B1F67: add dword ptr [rbx + 0x60], eax
0x002B1F6A: sub edi, eax
0x002B1F6C: test edi, edi
0x002B1F6E: jg 0x1402b1f40
0x002B1F70: mov rax, qword ptr [rbx + 0x50]
0x002B1F74: mov rcx, qword ptr [rax + 8]
0x002B1F78: cmp byte ptr [rcx], 0x14
0x002B1F7B: jne 0x1402b1f85
0x002B1F7D: mov rcx, rbx
0x002B1F80: call 0x1402b25a0
```

## `0x002BCA96` score `3/3` in `0x002BCA20..0x002BCD6F`

Recent ABI defs:

- `r8` <- `0x002BCA57: mov r8, rsi`
- `edx` <- `0x002BCA5A: mov edx, r9d`
- `r8` <- `0x002BCA80: lea r8, [rbp - 1]`
- `r9d` <- `0x002BCA84: mov r9d, 0xc`
- `edx` <- `0x002BCA92: lea edx, [r9 + 0xa]`

```asm
0x002BCA2A: push r13
0x002BCA2C: push r14
0x002BCA2E: push r15
0x002BCA30: lea rbp, [rsp - 0x1f]
0x002BCA35: mov eax, 0xa0
0x002BCA3A: call 0x1403b2500
0x002BCA3F: sub rsp, rax
0x002BCA42: mov rax, qword ptr [rip + 0x519ea7]
0x002BCA49: xor rax, rsp
0x002BCA4C: mov qword ptr [rbp + 0xf], rax
0x002BCA50: mov rsi, qword ptr [rbp + 0x7f]
0x002BCA54: mov r12d, r8d
0x002BCA57: mov r8, rsi
0x002BCA5A: mov edx, r9d
0x002BCA5D: mov r14d, r9d
0x002BCA60: mov rbx, rcx
0x002BCA63: call 0x1402bdf00
0x002BCA68: test eax, eax
0x002BCA6A: jne 0x1402bcc15
0x002BCA70: xor r13d, r13d
0x002BCA73: cmp dword ptr [rsi], r13d
0x002BCA76: jne 0x1402bcc1a
0x002BCA7C: mov rax, qword ptr [rbx + 8]
0x002BCA80: lea r8, [rbp - 1]
0x002BCA84: mov r9d, 0xc
0x002BCA8A: mov dword ptr [rsp + 0x20], r13d
0x002BCA8F: mov rcx, rbx
0x002BCA92: lea edx, [r9 + 0xa]
0x002BCA96: call qword ptr [rax + 0x68]
0x002BCA99: test eax, eax
0x002BCA9B: jle 0x1402bccc5
0x002BCAA1: cmp eax, 0xc
0x002BCAA4: jne 0x1402bcd26
0x002BCAAA: movzx r8d, byte ptr [rbp]
0x002BCAAF: xor eax, eax
0x002BCAB1: mov r9, qword ptr [rbp + 1]
0x002BCAB5: mov edx, r8d
0x002BCAB8: movzx ecx, byte ptr [rbp + 3]
0x002BCABC: movzx r15d, byte ptr [rbp + 5]
0x002BCAC1: movzx edi, byte ptr [rbp + 8]
0x002BCAC5: movzx r10d, byte ptr [rbp + 2]
0x002BCACA: movzx r11d, byte ptr [rbp - 1]
```

## `0x002BCCBD` score `3/3` in `0x002BCA20..0x002BCD6F`

Recent ABI defs:

- `r9` <- `0x002BCC6E: lea r9, [rip + 0x4e1983]`
- `r8d` <- `0x002BCC7A: mov r8d, r14d`
- `rdx` <- `0x002BCC7D: lea rdx, [rbp - 0x41]`
- `edx` <- `0x002BCC9C: lea edx, [r14 + 0x16]`
- `r9d` <- `0x002BCCA4: mov r9d, edi`
- `r8d` <- `0x002BCCA7: mov r8d, r15d`
- `r8` <- `0x002BCCBA: add r8, rax`

```asm
0x002BCC53: jmp 0x1402bcc1d
0x002BCC55: mov r8, rsi
0x002BCC58: lea rdx, [rbp - 0x41]
0x002BCC5C: mov rcx, rbx
0x002BCC5F: call 0x1402bd8a0
0x002BCC64: jmp 0x1402bcc1d
0x002BCC66: mov dword ptr [rsp + 0x20], 0x3cb
0x002BCC6E: lea r9, [rip + 0x4e1983]
0x002BCC75: jmp 0x1402bcd35
0x002BCC7A: mov r8d, r14d
0x002BCC7D: lea rdx, [rbp - 0x41]
0x002BCC81: mov rcx, rbx
0x002BCC84: call 0x1402bd100
0x002BCC89: mov r14d, eax
0x002BCC8C: test eax, eax
0x002BCC8E: jne 0x1402bcd50
0x002BCC94: test edi, edi
0x002BCC96: je 0x1402bccd4
0x002BCC98: mov rax, qword ptr [rbx + 0x50]
0x002BCC9C: lea edx, [r14 + 0x16]
0x002BCCA0: mov r10, qword ptr [rbx + 8]
0x002BCCA4: mov r9d, edi
0x002BCCA7: mov r8d, r15d
0x002BCCAA: mov rcx, rbx
0x002BCCAD: mov dword ptr [rsp + 0x20], r13d
0x002BCCB2: mov rax, qword ptr [rax + 8]
0x002BCCB6: add rax, 0xc
0x002BCCBA: add r8, rax
0x002BCCBD: call qword ptr [r10 + 0x68]
0x002BCCC1: test eax, eax
0x002BCCC3: jg 0x1402bccd7
0x002BCCC5: mov dword ptr [rbx + 0x28], 3
0x002BCCCC: mov dword ptr [rsi], r13d
0x002BCCCF: jmp 0x1402bcc1d
0x002BCCD4: mov eax, r13d
0x002BCCD7: cmp eax, edi
0x002BCCD9: je 0x1402bccf5
0x002BCCDB: mov r14d, 0x2f
0x002BCCE1: mov dword ptr [rsp + 0x20], 0x3ec
0x002BCCE9: mov r8d, r14d
0x002BCCEC: lea r9, [rip + 0x4e1915]
0x002BCCF3: jmp 0x1402bcd41
```

## `0x002BD595` score `3/3` in `0x002BD450..0x002BD673`

Recent ABI defs:

- `edx` <- `0x002BD54A: xor edx, edx`
- `r9d` <- `0x002BD581: mov r9d, ebx`
- `r8` <- `0x002BD584: mov r8, qword ptr [r14 + 0x40]`
- `edx` <- `0x002BD588: mov edx, 0x16`

```asm
0x002BD536: mov eax, dword ptr [rbp + 0x1a4]
0x002BD53C: mov ecx, 0x454c
0x002BD541: cmp eax, ecx
0x002BD543: cmova ecx, eax
0x002BD546: cmp ebx, ecx
0x002BD548: ja 0x1402bd5a9
0x002BD54A: xor edx, edx
0x002BD54C: mov ecx, ebx
0x002BD54E: call 0x1402bd010
0x002BD553: mov r14, rax
0x002BD556: test rax, rax
0x002BD559: je 0x1402bd5a9
0x002BD55B: movups xmm0, xmmword ptr [rsi]
0x002BD55E: movups xmmword ptr [rax], xmm0
0x002BD561: movups xmm1, xmmword ptr [rsi + 0x10]
0x002BD565: movups xmmword ptr [rax + 0x10], xmm1
0x002BD569: movups xmm0, xmmword ptr [rsi + 0x20]
0x002BD56D: movups xmmword ptr [rax + 0x20], xmm0
0x002BD571: movups xmm1, xmmword ptr [rsi + 0x30]
0x002BD575: movups xmmword ptr [rax + 0x30], xmm1
0x002BD579: test ebx, ebx
0x002BD57B: je 0x1402bd5d4
0x002BD57D: mov rax, qword ptr [rbp + 8]
0x002BD581: mov r9d, ebx
0x002BD584: mov r8, qword ptr [r14 + 0x40]
0x002BD588: mov edx, 0x16
0x002BD58D: mov rcx, rbp
0x002BD590: mov dword ptr [rsp + 0x20], r12d
0x002BD595: call qword ptr [rax + 0x68]
0x002BD598: mov edi, eax
0x002BD59A: cmp eax, ebx
0x002BD59C: je 0x1402bd5d0
0x002BD59E: or edi, 0xffffffff
0x002BD5A1: mov rcx, r14
0x002BD5A4: call 0x1402bcfb0
0x002BD5A9: mov dword ptr [r15], r12d
0x002BD5AC: mov eax, edi
0x002BD5AE: mov rcx, qword ptr [rsp + 0x140]
0x002BD5B6: xor rcx, rsp
0x002BD5B9: call 0x1403b24c0
0x002BD5BE: add rsp, 0x150
0x002BD5C5: pop r15
```

## `0x002BD658` score `3/3` in `0x002BD450..0x002BD673`

Recent ABI defs:

- `r8` <- `0x002BD601: lea r8, [rip + 0x4e0fb0]`
- `edx` <- `0x002BD608: mov edx, 0x36f`
- `r8` <- `0x002BD643: lea r8, [rsp + 0x40]`
- `r9d` <- `0x002BD648: mov r9d, ecx`
- `edx` <- `0x002BD650: mov edx, 0x16`

```asm
0x002BD5E1: test rax, rax
0x002BD5E4: je 0x1402bd5a1
0x002BD5E6: mov rcx, qword ptr [rbp + 0x88]
0x002BD5ED: mov rdx, rax
0x002BD5F0: mov rcx, qword ptr [rcx + 0x258]
0x002BD5F7: call 0x1402ee3d0
0x002BD5FC: test rax, rax
0x002BD5FF: jne 0x1402bd669
0x002BD601: lea r8, [rip + 0x4e0fb0]
0x002BD608: mov edx, 0x36f
0x002BD60D: lea rcx, [rip + 0x4e0fb4]
0x002BD614: call 0x1402c2530
0x002BD619: mov eax, 0xfffffffd
0x002BD61E: jmp 0x1402bd5ae
0x002BD620: test ebx, ebx
0x002BD622: je 0x1402bd669
0x002BD624: nop dword ptr [rax]
0x002BD628: nop dword ptr [rax + rax]
0x002BD630: mov ecx, 0x100
0x002BD635: cmp ebx, 0x100
0x002BD63B: ja 0x1402bd63f
0x002BD63D: mov ecx, ebx
0x002BD63F: mov rax, qword ptr [rbp + 8]
0x002BD643: lea r8, [rsp + 0x40]
0x002BD648: mov r9d, ecx
0x002BD64B: mov dword ptr [rsp + 0x20], r12d
0x002BD650: mov edx, 0x16
0x002BD655: mov rcx, rbp
0x002BD658: call qword ptr [rax + 0x68]
0x002BD65B: mov edi, eax
0x002BD65D: test eax, eax
0x002BD65F: jle 0x1402bd5a9
0x002BD665: sub ebx, eax
0x002BD667: jne 0x1402bd630
0x002BD669: mov eax, 0xfffffffd
0x002BD66E: jmp 0x1402bd5ae
0x002BD673: int3
0x002BD674: int3
0x002BD675: int3
0x002BD676: int3
0x002BD677: int3
0x002BD678: int3
```

## `0x002BD9C8` score `3/3` in `0x002BD8A0..0x002BDBE1`

Recent ABI defs:

- `r8` <- `0x002BD9B3: lea r8, [rsp + 0x40]`
- `r9d` <- `0x002BD9B8: mov r9d, ecx`
- `edx` <- `0x002BD9C0: mov edx, 0x16`

```asm
0x002BD963: movups xmmword ptr [rax], xmm0
0x002BD966: movups xmm1, xmmword ptr [rsi + 0x10]
0x002BD96A: movups xmmword ptr [rax + 0x10], xmm1
0x002BD96E: movups xmm0, xmmword ptr [rsi + 0x20]
0x002BD972: movups xmmword ptr [rax + 0x20], xmm0
0x002BD976: movups xmm1, xmmword ptr [rsi + 0x30]
0x002BD97A: movups xmmword ptr [rax + 0x30], xmm1
0x002BD97E: mov eax, dword ptr [rax + 4]
0x002BD981: mov dword ptr [rbp + 0x10], eax
0x002BD984: mov dword ptr [rbp + 0xc], r13d
0x002BD988: jmp 0x1402bd996
0x002BD98A: mov rbp, qword ptr [rax + 8]
0x002BD98E: mov eax, dword ptr [rsi + 4]
0x002BD991: cmp dword ptr [rbp + 4], eax
0x002BD994: jne 0x1402bda11
0x002BD996: cmp qword ptr [rbp + 0x48], r13
0x002BD99A: jne 0x1402bd9dc
0x002BD99C: nop dword ptr [rax]
0x002BD9A0: mov ecx, 0x100
0x002BD9A5: cmp ebx, 0x100
0x002BD9AB: ja 0x1402bd9af
0x002BD9AD: mov ecx, ebx
0x002BD9AF: mov rax, qword ptr [r14 + 8]
0x002BD9B3: lea r8, [rsp + 0x40]
0x002BD9B8: mov r9d, ecx
0x002BD9BB: mov dword ptr [rsp + 0x20], r13d
0x002BD9C0: mov edx, 0x16
0x002BD9C5: mov rcx, r14
0x002BD9C8: call qword ptr [rax + 0x68]
0x002BD9CB: mov edi, eax
0x002BD9CD: test eax, eax
0x002BD9CF: jle 0x1402bda04
0x002BD9D1: sub ebx, eax
0x002BD9D3: jne 0x1402bd9a0
0x002BD9D5: mov eax, 0xfffffffd
0x002BD9DA: jmp 0x1402bda17
0x002BD9DC: mov r8d, dword ptr [rsi + 0xc]
0x002BD9E0: mov r9d, ebx
0x002BD9E3: mov rax, qword ptr [r14 + 8]
0x002BD9E7: mov edx, 0x16
0x002BD9EC: add r8, qword ptr [rbp + 0x40]
0x002BD9F0: mov rcx, r14
```

## `0x002BD9F8` score `3/3` in `0x002BD8A0..0x002BDBE1`

Recent ABI defs:

- `r8` <- `0x002BD9B3: lea r8, [rsp + 0x40]`
- `r9d` <- `0x002BD9B8: mov r9d, ecx`
- `edx` <- `0x002BD9C0: mov edx, 0x16`
- `r8d` <- `0x002BD9DC: mov r8d, dword ptr [rsi + 0xc]`
- `r9d` <- `0x002BD9E0: mov r9d, ebx`
- `edx` <- `0x002BD9E7: mov edx, 0x16`
- `r8` <- `0x002BD9EC: add r8, qword ptr [rbp + 0x40]`

```asm
0x002BD996: cmp qword ptr [rbp + 0x48], r13
0x002BD99A: jne 0x1402bd9dc
0x002BD99C: nop dword ptr [rax]
0x002BD9A0: mov ecx, 0x100
0x002BD9A5: cmp ebx, 0x100
0x002BD9AB: ja 0x1402bd9af
0x002BD9AD: mov ecx, ebx
0x002BD9AF: mov rax, qword ptr [r14 + 8]
0x002BD9B3: lea r8, [rsp + 0x40]
0x002BD9B8: mov r9d, ecx
0x002BD9BB: mov dword ptr [rsp + 0x20], r13d
0x002BD9C0: mov edx, 0x16
0x002BD9C5: mov rcx, r14
0x002BD9C8: call qword ptr [rax + 0x68]
0x002BD9CB: mov edi, eax
0x002BD9CD: test eax, eax
0x002BD9CF: jle 0x1402bda04
0x002BD9D1: sub ebx, eax
0x002BD9D3: jne 0x1402bd9a0
0x002BD9D5: mov eax, 0xfffffffd
0x002BD9DA: jmp 0x1402bda17
0x002BD9DC: mov r8d, dword ptr [rsi + 0xc]
0x002BD9E0: mov r9d, ebx
0x002BD9E3: mov rax, qword ptr [r14 + 8]
0x002BD9E7: mov edx, 0x16
0x002BD9EC: add r8, qword ptr [rbp + 0x40]
0x002BD9F0: mov rcx, r14
0x002BD9F3: mov dword ptr [rsp + 0x20], r13d
0x002BD9F8: call qword ptr [rax + 0x68]
0x002BD9FB: mov edi, eax
0x002BD9FD: cmp eax, ebx
0x002BD9FF: je 0x1402bda42
0x002BDA01: or edi, 0xffffffff
0x002BDA04: test r15, r15
0x002BDA07: jne 0x1402bda11
0x002BDA09: mov rcx, rbp
0x002BDA0C: call 0x1402bcfb0
0x002BDA11: mov dword ptr [r12], r13d
0x002BDA15: mov eax, edi
0x002BDA17: mov rcx, qword ptr [rsp + 0x140]
0x002BDA1F: xor rcx, rsp
0x002BDA22: call 0x1403b24c0
```

## `0x002CAE09` score `3/3` in `0x002CAD4B..0x002CAEF7`

Recent ABI defs:

- `r9` <- `0x002CADC0: mov r9, qword ptr [rbx + 0x60]`
- `rdx` <- `0x002CADC4: lea rdx, [rsp + 0x60]`
- `r9` <- `0x002CADD3: test r9, r9`
- `r8` <- `0x002CADD8: mov r8, rbp`
- `r9` <- `0x002CADDB: call r9`
- `r9` <- `0x002CADE0: mov r9, rbp`
- `r8` <- `0x002CADE3: lea r8, [rsp + 0x68]`
- `rdx` <- `0x002CADFA: mov rdx, qword ptr [rsp + 0x60]`

```asm
0x002CAD87: mov qword ptr [rsp + 0x60], r13
0x002CAD8C: mov qword ptr [rsp + 0x68], r13
0x002CAD91: call 0x1402c7510
0x002CAD96: mov qword ptr [rbx + 0xc0], rax
0x002CAD9D: mov rbp, rax
0x002CADA0: mov qword ptr [rbx + 0xc8], r13
0x002CADA7: mov qword ptr [rbx + 0xd8], r13
0x002CADAE: test dword ptr [rax + 0x40], 0x400
0x002CADB5: jne 0x1402caebd
0x002CADBB: nop dword ptr [rax + rax]
0x002CADC0: mov r9, qword ptr [rbx + 0x60]
0x002CADC4: lea rdx, [rsp + 0x60]
0x002CADC9: mov r14d, dword ptr [rbx + 0xdc]
0x002CADD0: mov rcx, rbx
0x002CADD3: test r9, r9
0x002CADD6: je 0x1402cade0
0x002CADD8: mov r8, rbp
0x002CADDB: call r9
0x002CADDE: jmp 0x1402cadf2
0x002CADE0: mov r9, rbp
0x002CADE3: lea r8, [rsp + 0x68]
0x002CADE8: call 0x1402cb510
0x002CADED: mov rsi, qword ptr [rsp + 0x68]
0x002CADF2: test eax, eax
0x002CADF4: je 0x1402cae8c
0x002CADFA: mov rdx, qword ptr [rsp + 0x60]
0x002CADFF: mov rcx, rbx
0x002CAE02: mov qword ptr [rbx + 0xd0], rdx
0x002CAE09: call qword ptr [rbx + 0x68]
0x002CAE0C: mov edi, eax
0x002CAE0E: test eax, eax
0x002CAE10: je 0x1402caea0
0x002CAE16: test rsi, rsi
0x002CAE19: je 0x1402cae41
0x002CAE1B: mov rdx, rsi
0x002CAE1E: mov rcx, rbx
0x002CAE21: call qword ptr [rbx + 0x68]
0x002CAE24: mov edi, eax
0x002CAE26: test eax, eax
0x002CAE28: je 0x1402caea0
0x002CAE2A: mov r8, rbp
0x002CAE2D: mov rdx, rsi
```

## `0x002CAE21` score `3/3` in `0x002CAD4B..0x002CAEF7`

Recent ABI defs:

- `r9` <- `0x002CADD3: test r9, r9`
- `r8` <- `0x002CADD8: mov r8, rbp`
- `r9` <- `0x002CADDB: call r9`
- `r9` <- `0x002CADE0: mov r9, rbp`
- `r8` <- `0x002CADE3: lea r8, [rsp + 0x68]`
- `rdx` <- `0x002CADFA: mov rdx, qword ptr [rsp + 0x60]`
- `rdx` <- `0x002CAE1B: mov rdx, rsi`

```asm
0x002CADB5: jne 0x1402caebd
0x002CADBB: nop dword ptr [rax + rax]
0x002CADC0: mov r9, qword ptr [rbx + 0x60]
0x002CADC4: lea rdx, [rsp + 0x60]
0x002CADC9: mov r14d, dword ptr [rbx + 0xdc]
0x002CADD0: mov rcx, rbx
0x002CADD3: test r9, r9
0x002CADD6: je 0x1402cade0
0x002CADD8: mov r8, rbp
0x002CADDB: call r9
0x002CADDE: jmp 0x1402cadf2
0x002CADE0: mov r9, rbp
0x002CADE3: lea r8, [rsp + 0x68]
0x002CADE8: call 0x1402cb510
0x002CADED: mov rsi, qword ptr [rsp + 0x68]
0x002CADF2: test eax, eax
0x002CADF4: je 0x1402cae8c
0x002CADFA: mov rdx, qword ptr [rsp + 0x60]
0x002CADFF: mov rcx, rbx
0x002CAE02: mov qword ptr [rbx + 0xd0], rdx
0x002CAE09: call qword ptr [rbx + 0x68]
0x002CAE0C: mov edi, eax
0x002CAE0E: test eax, eax
0x002CAE10: je 0x1402caea0
0x002CAE16: test rsi, rsi
0x002CAE19: je 0x1402cae41
0x002CAE1B: mov rdx, rsi
0x002CAE1E: mov rcx, rbx
0x002CAE21: call qword ptr [rbx + 0x68]
0x002CAE24: mov edi, eax
0x002CAE26: test eax, eax
0x002CAE28: je 0x1402caea0
0x002CAE2A: mov r8, rbp
0x002CAE2D: mov rdx, rsi
0x002CAE30: mov rcx, rbx
0x002CAE33: call qword ptr [rbx + 0x70]
0x002CAE36: mov edi, eax
0x002CAE38: test eax, eax
0x002CAE3A: je 0x1402caea0
0x002CAE3C: cmp eax, 2
0x002CAE3F: je 0x1402cae55
0x002CAE41: mov rdx, qword ptr [rsp + 0x60]
```

## `0x0037FFE4` score `3/3` in `0x0037F860..0x00380004`

Recent ABI defs:

- `rdx` <- `0x0037FF7F: lea rdx, [rip + 0x381bba]`
- `r8` <- `0x0037FF9F: mov r8, rax`
- `rdx` <- `0x0037FFA2: lea rdx, [rip + 0x381baf]`
- `r9` <- `0x0037FFC7: lea r9, [rbp + 0x40]`
- `r8` <- `0x0037FFCF: lea r8, [rbp - 8]`
- `rdx` <- `0x0037FFDA: mov rdx, rdi`

```asm
0x0037FF69: call 0x140377200
0x0037FF6E: mov byte ptr [rdi + 0x3b1], 1
0x0037FF75: jmp 0x14037f99e
0x0037FF7A: cmp eax, 4
0x0037FF7D: jne 0x14037ff98
0x0037FF7F: lea rdx, [rip + 0x381bba]
0x0037FF86: mov rcx, rsi
0x0037FF89: call 0x140377140
0x0037FF8E: mov eax, 0x17
0x0037FF93: jmp 0x14037f9a0
0x0037FF98: mov ecx, eax
0x0037FF9A: call 0x14038a9f0
0x0037FF9F: mov r8, rax
0x0037FFA2: lea rdx, [rip + 0x381baf]
0x0037FFA9: mov rcx, rsi
0x0037FFAC: call 0x140377140
0x0037FFB1: mov eax, 0x38
0x0037FFB6: jmp 0x14037f9a0
0x0037FFBB: mov eax, r15d
0x0037FFBE: jmp 0x14037f9a0
0x0037FFC3: mov rax, qword ptr [rbp - 8]
0x0037FFC7: lea r9, [rbp + 0x40]
0x0037FFCB: add qword ptr [rbx + 0x68], rax
0x0037FFCF: lea r8, [rbp - 8]
0x0037FFD3: mov rax, qword ptr [rdi + 0x3e0]
0x0037FFDA: mov rdx, rdi
0x0037FFDD: mov rcx, rsi
0x0037FFE0: mov qword ptr [rbp - 8], r13
0x0037FFE4: call qword ptr [rax + 0x68]
0x0037FFE7: test eax, eax
0x0037FFE9: jne 0x14037f9a0
0x0037FFEF: cmp byte ptr [rbp + 0x40], al
0x0037FFF2: je 0x14037f973
0x0037FFF8: or dword ptr [rbx + 0x138], 1
0x0037FFFF: jmp 0x14037f973
0x00380004: int3
0x00380005: int3
0x00380006: int3
0x00380007: int3
0x00380008: int3
0x00380009: int3
0x0038000A: int3
```
