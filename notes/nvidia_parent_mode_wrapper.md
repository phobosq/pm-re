# Parent mode wrapper 0x1688B0 reference trace

This function loads `[this+0x888]` and tail-jumps to `0x16E0B0`, preserving RDX/R8/R9.

## Absolute qword refs

- `.rdata` RVA `0x0044B410` mod8=0

## Direct CALL/JMP refs

count: `0`

## Candidate vtable `0x0044B3D8`, target slot `+0x38`

- `+0x00` -> `0x001618B0`
- `+0x08` -> `0x00067840`
- `+0x10` -> `0x00067840`
- `+0x18` -> `0x00138970`
- `+0x20` -> `0x00067840`
- `+0x28` -> `0x00132720`
- `+0x30` -> `0x00169AA0`
- `+0x38` -> `0x001688B0`
- `+0x40` -> `0x00161DB0`
- `+0x48` -> `0x00168780`
- `+0x50` -> `0x001688D0`
- `+0x58` -> `0x00169660`
- `+0x60` -> `0x0036EFD0`
- `+0x68` -> `0x001620D0`
- `+0x70` -> `0x001620F0`
- `+0x78` -> `0x00169F20`
- `+0x80` -> `0x00164350`
- `+0x88` -> `0x00169650`
- `+0x90` -> `0x001688A0`

### Same-slot indirect callsites

count: `70`

#### `call` `0x00047BE8`

```asm
0x00047BAB: jne 0x140047bb8
0x00047BAD: mov esi, 3
0x00047BB2: mov dword ptr [rsp + 0x24], esi
0x00047BB6: jmp 0x140047bef
0x00047BB8: mov rax, qword ptr [rbx]
0x00047BBB: movsxd rcx, dword ptr [rax + 4]
0x00047BBF: mov rcx, qword ptr [rcx + rbx + 0x48]
0x00047BC4: mov rax, qword ptr [rcx + 0x38]
0x00047BC8: cmp qword ptr [rax], 0
0x00047BCC: je 0x140047be5
0x00047BCE: mov rdx, qword ptr [rcx + 0x50]
0x00047BD2: mov eax, dword ptr [rdx]
0x00047BD4: test eax, eax
0x00047BD6: jle 0x140047be5
0x00047BD8: dec eax
0x00047BDA: mov dword ptr [rdx], eax
0x00047BDC: mov rax, qword ptr [rcx + 0x38]
0x00047BE0: inc qword ptr [rax]
0x00047BE3: jmp 0x140047beb
0x00047BE5: mov rax, qword ptr [rcx]
0x00047BE8: call qword ptr [rax + 0x38]
0x00047BEB: inc qword ptr [rbx + 8]
0x00047BEF: jmp 0x140047bfe
0x00047BF1: mov edi, dword ptr [rsp + 0x20]
0x00047BF5: mov esi, dword ptr [rsp + 0x24]
0x00047BF9: mov rbx, qword ptr [rsp + 0x28]
```

#### `call` `0x0004AA77`

```asm
0x0004AA21: mov rcx, qword ptr [rbp + 0x17]
0x0004AA25: mov r9, qword ptr [rbp + 0x2f]
0x0004AA29: nop dword ptr [rax]
0x0004AA30: lea rdx, [rbp + 0x17]
0x0004AA34: cmp r9, 0x10
0x0004AA38: cmovae rdx, rcx
0x0004AA3C: lea r8, [rbp + 0x17]
0x0004AA40: cmovae r8, rcx
0x0004AA44: mov rcx, qword ptr [rbx + 0x68]
0x0004AA48: mov r10, qword ptr [rcx]
0x0004AA4B: add rdx, qword ptr [rbp + 0x27]
0x0004AA4F: lea rax, [rbp - 1]
0x0004AA53: mov qword ptr [rsp + 0x38], rax
0x0004AA58: mov qword ptr [rsp + 0x30], rdx
0x0004AA5D: mov qword ptr [rsp + 0x28], r8
0x0004AA62: lea rax, [rbp + 7]
0x0004AA66: mov qword ptr [rsp + 0x20], rax
0x0004AA6B: lea r9, [rbp - 8]
0x0004AA6F: lea r8, [rbp - 9]
0x0004AA73: lea rdx, [rbx + 0x74]
0x0004AA77: call qword ptr [r10 + 0x38]
0x0004AA7B: test eax, eax
0x0004AA7D: js 0x14004ab36
0x0004AA83: cmp eax, 1
0x0004AA86: jg 0x14004ab0f
0x0004AA8C: lea rax, [rbp + 0x17]
```

#### `call` `0x000555F6`

```asm
0x000555C1: movzx eax, byte ptr [rcx]
0x000555C4: add rsp, 0x20
0x000555C8: pop rbx
0x000555C9: ret
0x000555CA: test rcx, rcx
0x000555CD: je 0x1400555f0
0x000555CF: mov rcx, qword ptr [rbx + 0x50]
0x000555D3: mov eax, dword ptr [rcx]
0x000555D5: test eax, eax
0x000555D7: jle 0x1400555f0
0x000555D9: dec eax
0x000555DB: mov dword ptr [rcx], eax
0x000555DD: mov rcx, qword ptr [rbx + 0x38]
0x000555E1: mov rdx, qword ptr [rcx]
0x000555E4: lea rax, [rdx + 1]
0x000555E8: mov qword ptr [rcx], rax
0x000555EB: movzx eax, byte ptr [rdx]
0x000555EE: jmp 0x1400555f9
0x000555F0: mov rax, qword ptr [rbx]
0x000555F3: mov rcx, rbx
0x000555F6: call qword ptr [rax + 0x38]
0x000555F9: cmp eax, -1
0x000555FC: jne 0x140055606
0x000555FE: or eax, eax
0x00055600: add rsp, 0x20
0x00055604: pop rbx
```

#### `call` `0x00057E78`

```asm
0x00057E3F: int3
0x00057E40: push rbx
0x00057E42: sub rsp, 0x20
0x00057E46: mov rax, qword ptr [rcx + 0x38]
0x00057E4A: mov rbx, rcx
0x00057E4D: mov rcx, qword ptr [rax]
0x00057E50: test rcx, rcx
0x00057E53: je 0x140057e6d
0x00057E55: mov rax, qword ptr [rbx + 0x50]
0x00057E59: movsxd rdx, dword ptr [rax]
0x00057E5C: add rdx, rcx
0x00057E5F: cmp rcx, rdx
0x00057E62: jae 0x140057e6d
0x00057E64: movzx eax, byte ptr [rcx]
0x00057E67: add rsp, 0x20
0x00057E6B: pop rbx
0x00057E6C: ret
0x00057E6D: mov rax, qword ptr [rbx]
0x00057E70: mov rcx, rbx
0x00057E73: mov qword ptr [rsp + 0x30], rdi
0x00057E78: call qword ptr [rax + 0x38]
0x00057E7B: mov edi, eax
0x00057E7D: cmp eax, -1
0x00057E80: jne 0x140057e8f
0x00057E82: or eax, eax
0x00057E84: mov rdi, qword ptr [rsp + 0x30]
```

#### `call` `0x0005810F`

```asm
0x000580D0: cmp rdi, rax
0x000580D3: cmovl rbx, rdi
0x000580D7: test rbx, rbx
0x000580DA: je 0x1400580ee
0x000580DC: mov rdx, qword ptr [r14 + 0x38]
0x000580E0: mov r8, rbx
0x000580E3: mov rcx, rsi
0x000580E6: mov rdx, qword ptr [rdx]
0x000580E9: call 0x1403d1f90
0x000580EE: mov rax, qword ptr [r14 + 0x50]
0x000580F2: add rsi, rbx
0x000580F5: add rbp, rbx
0x000580F8: sub rdi, rbx
0x000580FB: sub dword ptr [rax], ebx
0x000580FD: mov rcx, qword ptr [r14 + 0x38]
0x00058101: movsxd rax, ebx
0x00058104: add qword ptr [rcx], rax
0x00058107: jmp 0x140058122
0x00058109: mov rdx, qword ptr [r14]
0x0005810C: mov rcx, r14
0x0005810F: call qword ptr [rdx + 0x38]
0x00058112: cmp eax, -1
0x00058115: je 0x140058127
0x00058117: mov byte ptr [rsi], al
0x00058119: inc rbp
0x0005811C: inc rsi
```

#### `call` `0x0007819A`

```asm
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
0x00078183: mov rcx, rsi
0x00078186: call 0x14006a320
0x0007818B: test r15b, r15b
0x0007818E: je 0x1400784ac
0x00078194: mov rax, qword ptr [rsi]
0x00078197: mov rcx, rsi
0x0007819A: call qword ptr [rax + 0x38]
0x0007819D: test al, al
0x0007819F: je 0x1400781f1
0x000781A1: mov dword ptr [rsp + 0x8e0], 0x2a
0x000781AC: mov eax, dword ptr [rsp + 0x8e0]
0x000781B3: xor eax, 0x30
```

#### `call` `0x000784BB`

```asm
0x00078465: nop
0x00078466: or r9, 0xffffffffffffffff
0x0007846A: xor r8d, r8d
0x0007846D: mov rdx, rax
0x00078470: lea rcx, [rsp + 0x9e8]
0x00078478: call 0x140035230
0x0007847D: nop
0x0007847E: lea rcx, [rsp + 0xc88]
0x00078486: call 0x140032ef0
0x0007848B: nop
0x0007848C: lea rcx, [rsp + 0xca8]
0x00078494: call 0x140032ef0
0x00078499: nop
0x0007849A: lea rcx, [rsp + 0xaa8]
0x000784A2: call 0x140032ef0
0x000784A7: mov rsi, qword ptr [rsp + 0x70]
0x000784AC: test r13b, r13b
0x000784AF: je 0x1400787e3
0x000784B5: mov rax, qword ptr [rsi]
0x000784B8: mov rcx, rsi
0x000784BB: call qword ptr [rax + 0x38]
0x000784BE: test al, al
0x000784C0: je 0x14007851b
0x000784C2: mov dword ptr [rsp + 0x928], 0x50
0x000784CD: mov dword ptr [rsp + 0x92c], 0x7f
0x000784D8: mov eax, dword ptr [rsp + 0x92c]
```

#### `call` `0x00087702`

```asm
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
```

#### `call` `0x00088F7E`

```asm
0x00088F41: cmp eax, r15d
0x00088F44: jne 0x140088f83
0x00088F46: mov sil, 1
0x00088F49: mov byte ptr [rsp + 0x20], sil
0x00088F4E: mov rax, qword ptr [rdi]
0x00088F51: movsxd rcx, dword ptr [rax + 4]
0x00088F55: mov rcx, qword ptr [rcx + rdi + 0x48]
0x00088F5A: mov rax, qword ptr [rcx + 0x38]
0x00088F5E: cmp qword ptr [rax], 0
0x00088F62: je 0x140088f7b
0x00088F64: mov rdx, qword ptr [rcx + 0x50]
0x00088F68: mov eax, dword ptr [rdx]
0x00088F6A: test eax, eax
0x00088F6C: jle 0x140088f7b
0x00088F6E: dec eax
0x00088F70: mov dword ptr [rdx], eax
0x00088F72: mov rax, qword ptr [rcx + 0x38]
0x00088F76: inc qword ptr [rax]
0x00088F79: jmp 0x140088f93
0x00088F7B: mov rax, qword ptr [rcx]
0x00088F7E: call qword ptr [rax + 0x38]
0x00088F81: jmp 0x140088f93
0x00088F83: cmp qword ptr [r14 + 0x10], -2
0x00088F88: jb 0x140088f95
0x00088F8A: mov ebx, 2
0x00088F8F: mov dword ptr [rsp + 0x24], ebx
```

#### `call` `0x0009F18C`

```asm
0x0009F140: je 0x14009f14d
0x0009F142: mov rax, qword ptr [rax]
0x0009F145: mov edx, 1
0x0009F14A: call qword ptr [rax]
0x0009F14C: nop
0x0009F14D: mov qword ptr [rbp - 0x29], 0xf
0x0009F155: mov qword ptr [rbp - 0x31], 0
0x0009F15D: mov byte ptr [rbp - 0x41], 0
0x0009F161: xor r8d, r8d
0x0009F164: mov rdx, rdi
0x0009F167: lea rcx, [rbp - 0x41]
0x0009F16B: call 0x1400a2320
0x0009F170: nop
0x0009F171: lea r9, [rbp - 0x41]
0x0009F175: cmp qword ptr [rbp - 0x29], 0x10
0x0009F17A: cmovae r9, qword ptr [rbp - 0x41]
0x0009F17F: mov rax, qword ptr [r14]
0x0009F182: lea r8, [rdi + rbx]
0x0009F186: mov rdx, rbx
0x0009F189: mov rcx, r14
0x0009F18C: call qword ptr [rax + 0x38]
0x0009F18F: lea rdx, [rsp + 0x20]
0x0009F194: mov rcx, r13
0x0009F197: call 0x140047d30
0x0009F19C: nop
0x0009F19D: mov rcx, rax
```

#### `call` `0x000A03B6`

```asm
0x000A0368: mov r8, qword ptr [rax]
0x000A036B: mov edx, 1
0x000A0370: mov rcx, rax
0x000A0373: call qword ptr [r8]
0x000A0376: nop
0x000A0377: mov qword ptr [rbp - 0x29], 0xf
0x000A037F: mov qword ptr [rbp - 0x31], 0
0x000A0387: mov byte ptr [rbp - 0x41], 0
0x000A038B: xor r8d, r8d
0x000A038E: mov rdx, rdi
0x000A0391: lea rcx, [rbp - 0x41]
0x000A0395: call 0x1400a2320
0x000A039A: nop
0x000A039B: lea r9, [rbp - 0x41]
0x000A039F: cmp qword ptr [rbp - 0x29], 0x10
0x000A03A4: cmovae r9, qword ptr [rbp - 0x41]
0x000A03A9: mov rax, qword ptr [rsi]
0x000A03AC: lea r8, [rdi + rbx]
0x000A03B0: mov rdx, rbx
0x000A03B3: mov rcx, rsi
0x000A03B6: call qword ptr [rax + 0x38]
0x000A03B9: lea rdx, [rbp - 0x71]
0x000A03BD: mov rcx, r12
0x000A03C0: call 0x140047d30
0x000A03C5: nop
0x000A03C6: mov rcx, rax
```

#### `call` `0x000B4A14`

```asm
0x000B49D2: call 0x140064f60
0x000B49D7: nop
0x000B49D8: mov rcx, qword ptr [rbp + 0x27]
0x000B49DC: xor rcx, rsp
0x000B49DF: call 0x1403b24c0
0x000B49E4: lea r11, [rsp + 0xc0]
0x000B49EC: mov rbx, qword ptr [r11 + 0x40]
0x000B49F0: mov rsi, qword ptr [r11 + 0x48]
0x000B49F4: mov rsp, r11
0x000B49F7: pop r15
0x000B49F9: pop r14
0x000B49FB: pop r12
0x000B49FD: pop rdi
0x000B49FE: pop rbp
0x000B49FF: ret
0x000B4A00: push rbx
0x000B4A02: sub rsp, 0x30
0x000B4A06: mov rax, qword ptr [rcx]
0x000B4A09: mov rbx, rdx
0x000B4A0C: mov dword ptr [rsp + 0x20], 0
0x000B4A14: call qword ptr [rax + 0x38]
0x000B4A17: mov rax, rbx
0x000B4A1A: add rsp, 0x30
0x000B4A1E: pop rbx
0x000B4A1F: ret
0x000B4A20: mov r11, rsp
```

#### `call` `0x0013065F`

```asm
0x0013060F: mov rax, qword ptr [rip + 0x6a62da]
0x00130616: xor rax, rsp
0x00130619: mov qword ptr [rbp + 0x100], rax
0x00130620: mov rax, qword ptr [rcx]
0x00130623: mov esi, edx
0x00130625: mov rbx, rcx
0x00130628: call qword ptr [rax + 0x90]
0x0013062E: mov rdi, rax
0x00130631: test rax, rax
0x00130634: je 0x1401309b1
0x0013063A: lea rdx, [rbp + 0x20]
0x0013063E: mov rcx, rbx
0x00130641: call 0x14006a320
0x00130646: cmp esi, 1
0x00130649: ja 0x140130705
0x0013064F: mov edx, dword ptr [rbp + 0xb8]
0x00130655: test edx, edx
0x00130657: js 0x14013066c
0x00130659: mov r8, qword ptr [rdi]
0x0013065C: mov rcx, rdi
0x0013065F: call qword ptr [r8 + 0x38]
0x00130663: mov byte ptr [rbx + 0x544], 1
0x0013066A: jmp 0x140130687
0x0013066C: cmp byte ptr [rbx + 0x544], 0
0x00130673: je 0x140130687
0x00130675: mov rax, qword ptr [rdi]
```

#### `call` `0x0013067D`

```asm
0x00130631: test rax, rax
0x00130634: je 0x1401309b1
0x0013063A: lea rdx, [rbp + 0x20]
0x0013063E: mov rcx, rbx
0x00130641: call 0x14006a320
0x00130646: cmp esi, 1
0x00130649: ja 0x140130705
0x0013064F: mov edx, dword ptr [rbp + 0xb8]
0x00130655: test edx, edx
0x00130657: js 0x14013066c
0x00130659: mov r8, qword ptr [rdi]
0x0013065C: mov rcx, rdi
0x0013065F: call qword ptr [r8 + 0x38]
0x00130663: mov byte ptr [rbx + 0x544], 1
0x0013066A: jmp 0x140130687
0x0013066C: cmp byte ptr [rbx + 0x544], 0
0x00130673: je 0x140130687
0x00130675: mov rax, qword ptr [rdi]
0x00130678: xor edx, edx
0x0013067A: mov rcx, rdi
0x0013067D: call qword ptr [rax + 0x38]
0x00130680: mov byte ptr [rbx + 0x544], 0
0x00130687: mov edx, dword ptr [rbp + 0xcc]
0x0013068D: mov r8d, dword ptr [rbp + 0xd0]
0x00130694: test edx, edx
0x00130696: jg 0x1401306ef
```

#### `call` `0x00135A42`

```asm
0x001359FC: mov rcx, rdi
0x001359FF: call qword ptr [rax + 0x28]
0x00135A02: mov byte ptr [rbx + 0x542], 0
0x00135A09: test sil, sil
0x00135A0C: jne 0x140135a17
0x00135A0E: cmp byte ptr [rbx + 0x543], 0
0x00135A15: je 0x140135a2c
0x00135A17: mov rax, qword ptr [rdi]
0x00135A1A: mov rcx, rdi
0x00135A1D: call qword ptr [rax + 0x40]
0x00135A20: mov byte ptr [rbx + 0x543], 0
0x00135A27: test sil, sil
0x00135A2A: jne 0x140135a3a
0x00135A2C: cmp byte ptr [rbx + 0x544], 0
0x00135A33: je 0x140135a51
0x00135A35: test bpl, bpl
0x00135A38: je 0x140135a51
0x00135A3A: mov rax, qword ptr [rdi]
0x00135A3D: xor edx, edx
0x00135A3F: mov rcx, rdi
0x00135A42: call qword ptr [rax + 0x38]
0x00135A45: mov byte ptr [rbx + 0x544], 0
0x00135A4C: test sil, sil
0x00135A4F: jne 0x140135a5f
0x00135A51: cmp byte ptr [rbx + 0x545], 0
0x00135A58: je 0x140135a6e
```

#### `call` `0x0013E786`

```asm
0x0013E740: add rax, rax
0x0013E743: mov rcx, qword ptr [rdx + rax*8]
0x0013E747: cmp dword ptr [rcx + 0x98], edi
0x0013E74D: je 0x14013e76a
0x0013E74F: inc r8d
0x0013E752: mov rcx, qword ptr [r10 + 0x68]
0x0013E756: sub rcx, rdx
0x0013E759: sar rcx, 4
0x0013E75D: mov eax, r8d
0x0013E760: cmp rax, rcx
0x0013E763: jb 0x14013e740
0x0013E765: jmp 0x14013ee7d
0x0013E76A: mov eax, r8d
0x0013E76D: shl rax, 4
0x0013E771: add rax, rdx
0x0013E774: mov rbx, qword ptr [rax]
0x0013E777: test rbx, rbx
0x0013E77A: je 0x14013ee7d
0x0013E780: mov rax, qword ptr [rbx]
0x0013E783: mov rcx, rbx
0x0013E786: call qword ptr [rax + 0x38]
0x0013E789: test al, al
0x0013E78B: je 0x14013eac1
0x0013E791: call 0x140134560
0x0013E796: add eax, edi
0x0013E798: mov dword ptr [rsp + 0x28], eax
```

#### `call` `0x0016EDDA`

```asm
0x0016ED7C: sub rsp, 0x260
0x0016ED83: mov qword ptr [rsp + 0x78], 0xfffffffffffffffe
0x0016ED8C: mov rax, qword ptr [rip + 0x667b5d]
0x0016ED93: xor rax, rsp
0x0016ED96: mov qword ptr [rsp + 0x250], rax
0x0016ED9E: mov dword ptr [rsp + 0x38], r9d
0x0016EDA3: mov dword ptr [rsp + 0x48], r8d
0x0016EDA8: mov rbx, rdx
0x0016EDAB: mov qword ptr [rsp + 0x50], rdx
0x0016EDB0: mov rsi, rcx
0x0016EDB3: mov qword ptr [rsp + 0x68], rcx
0x0016EDB8: xor r13d, r13d
0x0016EDBB: mov edx, dword ptr [rdx + 0x18]
0x0016EDBE: mov rcx, qword ptr [rbx + 0x10]
0x0016EDC2: call 0x140159b40
0x0016EDC7: mov r14d, eax
0x0016EDCA: mov dword ptr [rsp + 0x34], eax
0x0016EDCE: mov rcx, qword ptr [rsi + 0x80]
0x0016EDD5: mov r8, qword ptr [rcx]
0x0016EDD8: mov edx, eax
0x0016EDDA: call qword ptr [r8 + 0x38]
0x0016EDDE: mov rcx, qword ptr [rsi + 0x80]
0x0016EDE5: mov rdx, qword ptr [rcx]
0x0016EDE8: call qword ptr [rdx + 0x78]
0x0016EDEB: movzx ecx, al
0x0016EDEE: mov r15d, r13d
```

#### `call` `0x001BDE10`

```asm
0x001BDDC7: call 0x1402813e0
0x001BDDCC: test eax, eax
0x001BDDCE: je 0x1401bde04
0x001BDDD0: xor ecx, ecx
0x001BDDD2: mov qword ptr [rbp - 0x50], rcx
0x001BDDD6: mov qword ptr [rbp - 0x48], rcx
0x001BDDDA: lea rcx, [rip + 0x28d697]
0x001BDDE1: mov qword ptr [rbp - 0x58], rcx
0x001BDDE5: mov dword ptr [rbp - 0x40], eax
0x001BDDE8: lea rax, [rip + 0x28dd91]
0x001BDDEF: mov qword ptr [rbp - 0x38], rax
0x001BDDF3: lea rdx, [rip + 0x5cdbb6]
0x001BDDFA: lea rcx, [rbp - 0x58]
0x001BDDFE: call 0x1403d25d0
0x001BDE03: int3
0x001BDE04: test edi, edi
0x001BDE06: js 0x1401bde13
0x001BDE08: mov rax, qword ptr [rbx]
0x001BDE0B: mov edx, edi
0x001BDE0D: mov rcx, rbx
0x001BDE10: call qword ptr [rax + 0x38]
0x001BDE13: mov rdx, qword ptr [rsi + 0x70]
0x001BDE17: mov rcx, rbx
0x001BDE1A: call 0x1401b9e60
0x001BDE1F: movzx r15d, al
0x001BDE23: mov rcx, qword ptr [rbx + 0x198]
```

#### `call` `0x002001AB`

```asm
0x00200155: push rdi
0x00200156: push r12
0x00200158: push r13
0x0020015A: push r14
0x0020015C: push r15
0x0020015E: lea rbp, [rax - 0x798]
0x00200165: sub rsp, 0x860
0x0020016C: mov qword ptr [rbp + 0x90], 0xfffffffffffffffe
0x00200177: mov qword ptr [rax + 0x18], rbx
0x0020017B: movaps xmmword ptr [rax - 0x48], xmm6
0x0020017F: mov rax, qword ptr [rip + 0x5d676a]
0x00200186: xor rax, rsp
0x00200189: mov qword ptr [rbp + 0x740], rax
0x00200190: mov rsi, r9
0x00200193: mov ebx, r8d
0x00200196: mov rdi, rcx
0x00200199: mov dword ptr [rbp - 0x68], edx
0x0020019C: cmp edx, 0x258
0x002001A2: jg 0x1402013b4
0x002001A8: mov rax, qword ptr [rcx]
0x002001AB: call qword ptr [rax + 0x38]
0x002001AE: mov rdx, rsi
0x002001B1: mov rcx, rdi
0x002001B4: call 0x1401fb9e0
0x002001B9: mov ecx, 0x40
0x002001BE: sub ebx, 1
```

#### `call` `0x0020D08B`

```asm
0x0020D035: push rdi
0x0020D036: push r12
0x0020D038: push r13
0x0020D03A: push r14
0x0020D03C: push r15
0x0020D03E: lea rbp, [rax - 0x798]
0x0020D045: sub rsp, 0x860
0x0020D04C: mov qword ptr [rbp + 0x90], 0xfffffffffffffffe
0x0020D057: mov qword ptr [rax + 0x18], rbx
0x0020D05B: movaps xmmword ptr [rax - 0x48], xmm6
0x0020D05F: mov rax, qword ptr [rip + 0x5c988a]
0x0020D066: xor rax, rsp
0x0020D069: mov qword ptr [rbp + 0x740], rax
0x0020D070: mov rsi, r9
0x0020D073: mov ebx, r8d
0x0020D076: mov rdi, rcx
0x0020D079: mov dword ptr [rbp - 0x68], edx
0x0020D07C: cmp edx, 0x258
0x0020D082: jg 0x14020e21e
0x0020D088: mov rax, qword ptr [rcx]
0x0020D08B: call qword ptr [rax + 0x38]
0x0020D08E: mov rdx, rsi
0x0020D091: mov rcx, rdi
0x0020D094: call 0x1401fb9e0
0x0020D099: mov ecx, 0x40
0x0020D09E: sub ebx, 1
```

#### `call` `0x0021113F`

```asm
0x002110EB: xor eax, eax
0x002110ED: mov qword ptr [rsp + 0x30], rax
0x002110F2: mov qword ptr [rsp + 0x38], rax
0x002110F7: mov rax, qword ptr [rsp + 0x20]
0x002110FC: mov qword ptr [rsp + 0x40], rax
0x00211101: mov byte ptr [rsp + 0x48], 1
0x00211106: lea rdx, [rsp + 0x30]
0x0021110B: lea rcx, [rsp + 0x40]
0x00211110: call 0x1403d23c8
0x00211115: lea rax, [rip + 0x22286c]
0x0021111C: mov qword ptr [rsp + 0x28], rax
0x00211121: lea rdx, [rip + 0x579e38]
0x00211128: lea rcx, [rsp + 0x28]
0x0021112D: call 0x1403d25d0
0x00211132: int3
0x00211133: test esi, esi
0x00211135: js 0x140211142
0x00211137: mov rax, qword ptr [rdi]
0x0021113A: mov edx, esi
0x0021113C: mov rcx, rdi
0x0021113F: call qword ptr [rax + 0x38]
0x00211142: mov rdx, qword ptr [r14 + 0x70]
0x00211146: mov rcx, rdi
0x00211149: call 0x14020c500
0x0021114E: movzx ebx, al
0x00211151: mov rcx, qword ptr [rdi + 0x240]
```

#### `call` `0x0023A2A5`

```asm
0x0023A255: mov rcx, qword ptr [rdi]
0x0023A258: call 0x14022e900
0x0023A25D: jmp 0x14023a347
0x0023A262: lea rdx, [rcx + 0x18]
0x0023A266: mov rcx, qword ptr [rcx + 0x10]
0x0023A26A: jmp 0x14023a33f
0x0023A26F: cmp eax, 1
0x0023A272: jne 0x14023a28d
0x0023A274: lea rcx, [rbp + 0x40]
0x0023A278: call 0x14024ed80
0x0023A27D: mov rdx, rax
0x0023A280: mov rcx, qword ptr [rdi + 8]
0x0023A284: add rcx, 0x50
0x0023A288: call 0x140248f20
0x0023A28D: lea rdx, [rdi + 0x20]
0x0023A291: mov rcx, qword ptr [rdi + 8]
0x0023A295: call 0x14024e8d0
0x0023A29A: mov r8, qword ptr [rdi + 0x48]
0x0023A29E: mov rdx, rax
0x0023A2A1: mov rcx, qword ptr [rdi + 0x40]
0x0023A2A5: call qword ptr [rdi + 0x38]
0x0023A2A8: jmp 0x14023a347
0x0023A2AD: mov rax, qword ptr [rdi + 8]
0x0023A2B1: mov rax, qword ptr [rax + 0xd0]
0x0023A2B8: mov qword ptr [rbp - 0x20], rax
0x0023A2BC: mov qword ptr [rbp - 0x18], r12
```

#### `call` `0x002748AB`

```asm
0x00274872: inc r15
0x00274875: mov rcx, qword ptr [rdi]
0x00274878: test rcx, rcx
0x0027487B: je 0x1402748b9
0x0027487D: mov rax, qword ptr [rcx + 0x38]
0x00274881: cmp qword ptr [rax], 0
0x00274885: je 0x1402748a8
0x00274887: mov rdx, qword ptr [rcx + 0x50]
0x0027488B: mov eax, dword ptr [rdx]
0x0027488D: test eax, eax
0x0027488F: jle 0x1402748a8
0x00274891: dec eax
0x00274893: mov dword ptr [rdx], eax
0x00274895: mov rcx, qword ptr [rcx + 0x38]
0x00274899: mov rdx, qword ptr [rcx]
0x0027489C: lea rax, [rdx + 1]
0x002748A0: mov qword ptr [rcx], rax
0x002748A3: movzx eax, byte ptr [rdx]
0x002748A6: jmp 0x1402748ae
0x002748A8: mov rax, qword ptr [rcx]
0x002748AB: call qword ptr [rax + 0x38]
0x002748AE: cmp eax, -1
0x002748B1: je 0x1402748b9
0x002748B3: mov byte ptr [rdi + 8], 0
0x002748B7: jmp 0x1402748c4
0x002748B9: mov qword ptr [rdi], 0
```

#### `call` `0x00276F5F`

```asm
0x00276F26: mov rbx, rcx
0x00276F29: mov rcx, qword ptr [rcx]
0x00276F2C: test rcx, rcx
0x00276F2F: je 0x140276f74
0x00276F31: mov rax, qword ptr [rcx + 0x38]
0x00276F35: cmp qword ptr [rax], 0
0x00276F39: je 0x140276f5c
0x00276F3B: mov rdx, qword ptr [rcx + 0x50]
0x00276F3F: mov eax, dword ptr [rdx]
0x00276F41: test eax, eax
0x00276F43: jle 0x140276f5c
0x00276F45: dec eax
0x00276F47: mov dword ptr [rdx], eax
0x00276F49: mov rcx, qword ptr [rcx + 0x38]
0x00276F4D: mov rdx, qword ptr [rcx]
0x00276F50: lea rax, [rdx + 1]
0x00276F54: mov qword ptr [rcx], rax
0x00276F57: movzx eax, byte ptr [rdx]
0x00276F5A: jmp 0x140276f62
0x00276F5C: mov rax, qword ptr [rcx]
0x00276F5F: call qword ptr [rax + 0x38]
0x00276F62: cmp eax, -1
0x00276F65: je 0x140276f74
0x00276F67: mov byte ptr [rbx + 8], 0
0x00276F6B: mov rax, rbx
0x00276F6E: add rsp, 0x20
```

#### `call` `0x00279B37`

```asm
0x00279AF1: mov rcx, rax
0x00279AF4: call 0x1400309f0
0x00279AF9: mov rdi, rax
0x00279AFC: mov rcx, qword ptr [rbp - 0x71]
0x00279B00: test rcx, rcx
0x00279B03: je 0x140279b1f
0x00279B05: mov rdx, qword ptr [rcx]
0x00279B08: call qword ptr [rdx + 0x10]
0x00279B0B: test rax, rax
0x00279B0E: je 0x140279b1f
0x00279B10: mov r8, qword ptr [rax]
0x00279B13: mov edx, 1
0x00279B18: mov rcx, rax
0x00279B1B: call qword ptr [r8]
0x00279B1E: nop
0x00279B1F: mov rax, qword ptr [rdi]
0x00279B22: lea r9, [rbp - 9]
0x00279B26: lea r8, [rip + 0x44d152]
0x00279B2D: lea rdx, [rip + 0x44d13c]
0x00279B34: mov rcx, rdi
0x00279B37: call qword ptr [rax + 0x38]
0x00279B3A: mov rdx, r14
0x00279B3D: mov rcx, rbx
0x00279B40: call 0x14027c9c0
0x00279B45: test al, al
0x00279B47: jne 0x140279b7b
```

#### `call` `0x0027A0DA`

```asm
0x0027A09F: mov byte ptr [rsp + 0x30], 1
0x0027A0A4: mov rcx, qword ptr [rbx]
0x0027A0A7: test rcx, rcx
0x0027A0AA: je 0x14027a0e8
0x0027A0AC: mov rax, qword ptr [rcx + 0x38]
0x0027A0B0: cmp qword ptr [rax], 0
0x0027A0B4: je 0x14027a0d7
0x0027A0B6: mov rdx, qword ptr [rcx + 0x50]
0x0027A0BA: mov eax, dword ptr [rdx]
0x0027A0BC: test eax, eax
0x0027A0BE: jle 0x14027a0d7
0x0027A0C0: dec eax
0x0027A0C2: mov dword ptr [rdx], eax
0x0027A0C4: mov rcx, qword ptr [rcx + 0x38]
0x0027A0C8: mov rdx, qword ptr [rcx]
0x0027A0CB: lea rax, [rdx + 1]
0x0027A0CF: mov qword ptr [rcx], rax
0x0027A0D2: movzx eax, byte ptr [rdx]
0x0027A0D5: jmp 0x14027a0dd
0x0027A0D7: mov rax, qword ptr [rcx]
0x0027A0DA: call qword ptr [rax + 0x38]
0x0027A0DD: cmp eax, -1
0x0027A0E0: je 0x14027a0e8
0x0027A0E2: mov byte ptr [rbx + 8], 0
0x0027A0E6: jmp 0x14027a0f3
0x0027A0E8: mov qword ptr [rbx], 0
```

#### `call` `0x0027A226`

```asm
0x0027A1EB: mov byte ptr [rsp + 0x30], r12b
0x0027A1F0: mov rcx, qword ptr [rbx]
0x0027A1F3: test rcx, rcx
0x0027A1F6: je 0x14027a234
0x0027A1F8: mov rax, qword ptr [rcx + 0x38]
0x0027A1FC: cmp qword ptr [rax], 0
0x0027A200: je 0x14027a223
0x0027A202: mov rdx, qword ptr [rcx + 0x50]
0x0027A206: mov eax, dword ptr [rdx]
0x0027A208: test eax, eax
0x0027A20A: jle 0x14027a223
0x0027A20C: dec eax
0x0027A20E: mov dword ptr [rdx], eax
0x0027A210: mov rcx, qword ptr [rcx + 0x38]
0x0027A214: mov rdx, qword ptr [rcx]
0x0027A217: lea rax, [rdx + 1]
0x0027A21B: mov qword ptr [rcx], rax
0x0027A21E: movzx eax, byte ptr [rdx]
0x0027A221: jmp 0x14027a229
0x0027A223: mov rax, qword ptr [rcx]
0x0027A226: call qword ptr [rax + 0x38]
0x0027A229: cmp eax, -1
0x0027A22C: je 0x14027a234
0x0027A22E: mov byte ptr [rbx + 8], 0
0x0027A232: jmp 0x14027a23f
0x0027A234: mov qword ptr [rbx], 0
```

#### `call` `0x0027A392`

```asm
0x0027A359: inc rsi
0x0027A35C: mov rcx, qword ptr [rbx]
0x0027A35F: test rcx, rcx
0x0027A362: je 0x14027a3a3
0x0027A364: mov rax, qword ptr [rcx + 0x38]
0x0027A368: cmp qword ptr [rax], 0
0x0027A36C: je 0x14027a38f
0x0027A36E: mov rdx, qword ptr [rcx + 0x50]
0x0027A372: mov eax, dword ptr [rdx]
0x0027A374: test eax, eax
0x0027A376: jle 0x14027a38f
0x0027A378: dec eax
0x0027A37A: mov dword ptr [rdx], eax
0x0027A37C: mov rcx, qword ptr [rcx + 0x38]
0x0027A380: mov rdx, qword ptr [rcx]
0x0027A383: lea rax, [rdx + 1]
0x0027A387: mov qword ptr [rcx], rax
0x0027A38A: movzx eax, byte ptr [rdx]
0x0027A38D: jmp 0x14027a395
0x0027A38F: mov rax, qword ptr [rcx]
0x0027A392: call qword ptr [rax + 0x38]
0x0027A395: cmp eax, -1
0x0027A398: je 0x14027a3a3
0x0027A39A: mov byte ptr [rbx + 8], 0
0x0027A39E: xor r13d, r13d
0x0027A3A1: jmp 0x14027a3ad
```

#### `call` `0x0027A496`

```asm
0x0027A45D: inc rsi
0x0027A460: mov rcx, qword ptr [rbx]
0x0027A463: test rcx, rcx
0x0027A466: je 0x14027a4a4
0x0027A468: mov rax, qword ptr [rcx + 0x38]
0x0027A46C: cmp qword ptr [rax], 0
0x0027A470: je 0x14027a493
0x0027A472: mov rdx, qword ptr [rcx + 0x50]
0x0027A476: mov eax, dword ptr [rdx]
0x0027A478: test eax, eax
0x0027A47A: jle 0x14027a493
0x0027A47C: dec eax
0x0027A47E: mov dword ptr [rdx], eax
0x0027A480: mov rcx, qword ptr [rcx + 0x38]
0x0027A484: mov rdx, qword ptr [rcx]
0x0027A487: lea rax, [rdx + 1]
0x0027A48B: mov qword ptr [rcx], rax
0x0027A48E: movzx eax, byte ptr [rdx]
0x0027A491: jmp 0x14027a499
0x0027A493: mov rax, qword ptr [rcx]
0x0027A496: call qword ptr [rax + 0x38]
0x0027A499: cmp eax, -1
0x0027A49C: je 0x14027a4a4
0x0027A49E: mov byte ptr [rbx + 8], 0
0x0027A4A2: jmp 0x14027a4ab
0x0027A4A4: mov byte ptr [rbx + 8], 1
```

#### `call` `0x0027A541`

```asm
0x0027A508: mov r14b, 1
0x0027A50B: mov rcx, qword ptr [rbx]
0x0027A50E: test rcx, rcx
0x0027A511: je 0x14027a54f
0x0027A513: mov rax, qword ptr [rcx + 0x38]
0x0027A517: cmp qword ptr [rax], 0
0x0027A51B: je 0x14027a53e
0x0027A51D: mov rdx, qword ptr [rcx + 0x50]
0x0027A521: mov eax, dword ptr [rdx]
0x0027A523: test eax, eax
0x0027A525: jle 0x14027a53e
0x0027A527: dec eax
0x0027A529: mov dword ptr [rdx], eax
0x0027A52B: mov rcx, qword ptr [rcx + 0x38]
0x0027A52F: mov rdx, qword ptr [rcx]
0x0027A532: lea rax, [rdx + 1]
0x0027A536: mov qword ptr [rcx], rax
0x0027A539: movzx eax, byte ptr [rdx]
0x0027A53C: jmp 0x14027a544
0x0027A53E: mov rax, qword ptr [rcx]
0x0027A541: call qword ptr [rax + 0x38]
0x0027A544: cmp eax, -1
0x0027A547: je 0x14027a54f
0x0027A549: mov byte ptr [rbx + 8], 0
0x0027A54D: jmp 0x14027a556
0x0027A54F: mov qword ptr [rbx], r13
```

#### `call` `0x0027A645`

```asm
0x0027A60C: mov r14b, 1
0x0027A60F: mov rcx, qword ptr [rbx]
0x0027A612: test rcx, rcx
0x0027A615: je 0x14027a653
0x0027A617: mov rax, qword ptr [rcx + 0x38]
0x0027A61B: cmp qword ptr [rax], 0
0x0027A61F: je 0x14027a642
0x0027A621: mov rdx, qword ptr [rcx + 0x50]
0x0027A625: mov eax, dword ptr [rdx]
0x0027A627: test eax, eax
0x0027A629: jle 0x14027a642
0x0027A62B: dec eax
0x0027A62D: mov dword ptr [rdx], eax
0x0027A62F: mov rcx, qword ptr [rcx + 0x38]
0x0027A633: mov rdx, qword ptr [rcx]
0x0027A636: lea rax, [rdx + 1]
0x0027A63A: mov qword ptr [rcx], rax
0x0027A63D: movzx eax, byte ptr [rdx]
0x0027A640: jmp 0x14027a648
0x0027A642: mov rax, qword ptr [rcx]
0x0027A645: call qword ptr [rax + 0x38]
0x0027A648: cmp eax, -1
0x0027A64B: je 0x14027a653
0x0027A64D: mov byte ptr [rbx + 8], 0
0x0027A651: jmp 0x14027a65a
0x0027A653: mov qword ptr [rbx], r13
```

#### `call` `0x0027A808`

```asm
0x0027A7C3: mov rcx, rax
0x0027A7C6: call 0x1400309f0
0x0027A7CB: mov rdi, rax
0x0027A7CE: mov rcx, qword ptr [rsp + 0x40]
0x0027A7D3: test rcx, rcx
0x0027A7D6: je 0x14027a7f0
0x0027A7D8: mov rdx, qword ptr [rcx]
0x0027A7DB: call qword ptr [rdx + 0x10]
0x0027A7DE: test rax, rax
0x0027A7E1: je 0x14027a7f0
0x0027A7E3: mov r8, qword ptr [rax]
0x0027A7E6: mov edx, r12d
0x0027A7E9: mov rcx, rax
0x0027A7EC: call qword ptr [r8]
0x0027A7EF: nop
0x0027A7F0: mov rax, qword ptr [rdi]
0x0027A7F3: lea r9, [rbp - 0x11]
0x0027A7F7: lea r8, [rip + 0x44c4bf]
0x0027A7FE: lea rdx, [rip + 0x44c49b]
0x0027A805: mov rcx, rdi
0x0027A808: call qword ptr [rax + 0x38]
0x0027A80B: mov rsi, r14
0x0027A80E: mov byte ptr [rsp + 0x21], 0
0x0027A813: mov rdx, r13
0x0027A816: mov rcx, rbx
0x0027A819: call 0x14027c9c0
```

#### `call` `0x0027ACFD`

```asm
0x0027ACC2: mov byte ptr [rsp + 0x20], r12b
0x0027ACC7: mov rcx, qword ptr [rbx]
0x0027ACCA: test rcx, rcx
0x0027ACCD: je 0x14027ad0b
0x0027ACCF: mov rax, qword ptr [rcx + 0x38]
0x0027ACD3: cmp qword ptr [rax], 0
0x0027ACD7: je 0x14027acfa
0x0027ACD9: mov rdx, qword ptr [rcx + 0x50]
0x0027ACDD: mov eax, dword ptr [rdx]
0x0027ACDF: test eax, eax
0x0027ACE1: jle 0x14027acfa
0x0027ACE3: dec eax
0x0027ACE5: mov dword ptr [rdx], eax
0x0027ACE7: mov rcx, qword ptr [rcx + 0x38]
0x0027ACEB: mov rdx, qword ptr [rcx]
0x0027ACEE: lea rax, [rdx + 1]
0x0027ACF2: mov qword ptr [rcx], rax
0x0027ACF5: movzx eax, byte ptr [rdx]
0x0027ACF8: jmp 0x14027ad00
0x0027ACFA: mov rax, qword ptr [rcx]
0x0027ACFD: call qword ptr [rax + 0x38]
0x0027AD00: cmp eax, -1
0x0027AD03: je 0x14027ad0b
0x0027AD05: mov byte ptr [rbx + 8], 0
0x0027AD09: jmp 0x14027ad16
0x0027AD0B: mov qword ptr [rbx], 0
```

#### `call` `0x0027AE02`

```asm
0x0027ADC9: inc rsi
0x0027ADCC: mov rcx, qword ptr [rbx]
0x0027ADCF: test rcx, rcx
0x0027ADD2: je 0x14027ae10
0x0027ADD4: mov rax, qword ptr [rcx + 0x38]
0x0027ADD8: cmp qword ptr [rax], 0
0x0027ADDC: je 0x14027adff
0x0027ADDE: mov rdx, qword ptr [rcx + 0x50]
0x0027ADE2: mov eax, dword ptr [rdx]
0x0027ADE4: test eax, eax
0x0027ADE6: jle 0x14027adff
0x0027ADE8: dec eax
0x0027ADEA: mov dword ptr [rdx], eax
0x0027ADEC: mov rcx, qword ptr [rcx + 0x38]
0x0027ADF0: mov rdx, qword ptr [rcx]
0x0027ADF3: lea rax, [rdx + 1]
0x0027ADF7: mov qword ptr [rcx], rax
0x0027ADFA: movzx eax, byte ptr [rdx]
0x0027ADFD: jmp 0x14027ae05
0x0027ADFF: mov rax, qword ptr [rcx]
0x0027AE02: call qword ptr [rax + 0x38]
0x0027AE05: cmp eax, -1
0x0027AE08: je 0x14027ae10
0x0027AE0A: mov byte ptr [rbx + 8], 0
0x0027AE0E: jmp 0x14027ae1b
0x0027AE10: xor edi, edi
```

#### `call` `0x0027AEC4`

```asm
0x0027AE8B: mov r12b, 1
0x0027AE8E: mov rcx, qword ptr [rbx]
0x0027AE91: test rcx, rcx
0x0027AE94: je 0x14027aed2
0x0027AE96: mov rax, qword ptr [rcx + 0x38]
0x0027AE9A: cmp qword ptr [rax], 0
0x0027AE9E: je 0x14027aec1
0x0027AEA0: mov rdx, qword ptr [rcx + 0x50]
0x0027AEA4: mov eax, dword ptr [rdx]
0x0027AEA6: test eax, eax
0x0027AEA8: jle 0x14027aec1
0x0027AEAA: dec eax
0x0027AEAC: mov dword ptr [rdx], eax
0x0027AEAE: mov rcx, qword ptr [rcx + 0x38]
0x0027AEB2: mov rdx, qword ptr [rcx]
0x0027AEB5: lea rax, [rdx + 1]
0x0027AEB9: mov qword ptr [rcx], rax
0x0027AEBC: movzx eax, byte ptr [rdx]
0x0027AEBF: jmp 0x14027aec7
0x0027AEC1: mov rax, qword ptr [rcx]
0x0027AEC4: call qword ptr [rax + 0x38]
0x0027AEC7: cmp eax, -1
0x0027AECA: je 0x14027aed2
0x0027AECC: mov byte ptr [rbx + 8], 0
0x0027AED0: jmp 0x14027aed9
0x0027AED2: mov qword ptr [rbx], rdi
```

#### `call` `0x0027AFF7`

```asm
0x0027AFBC: mov byte ptr [rsp + 0x20], r12b
0x0027AFC1: mov rcx, qword ptr [rbx]
0x0027AFC4: test rcx, rcx
0x0027AFC7: je 0x14027b005
0x0027AFC9: mov rax, qword ptr [rcx + 0x38]
0x0027AFCD: cmp qword ptr [rax], 0
0x0027AFD1: je 0x14027aff4
0x0027AFD3: mov rdx, qword ptr [rcx + 0x50]
0x0027AFD7: mov eax, dword ptr [rdx]
0x0027AFD9: test eax, eax
0x0027AFDB: jle 0x14027aff4
0x0027AFDD: dec eax
0x0027AFDF: mov dword ptr [rdx], eax
0x0027AFE1: mov rcx, qword ptr [rcx + 0x38]
0x0027AFE5: mov rdx, qword ptr [rcx]
0x0027AFE8: lea rax, [rdx + 1]
0x0027AFEC: mov qword ptr [rcx], rax
0x0027AFEF: movzx eax, byte ptr [rdx]
0x0027AFF2: jmp 0x14027affa
0x0027AFF4: mov rax, qword ptr [rcx]
0x0027AFF7: call qword ptr [rax + 0x38]
0x0027AFFA: cmp eax, -1
0x0027AFFD: je 0x14027b005
0x0027AFFF: mov byte ptr [rbx + 8], 0
0x0027B003: jmp 0x14027b00c
0x0027B005: mov qword ptr [rbx], rdi
```

#### `call` `0x0027B10C`

```asm
0x0027B0D3: inc rsi
0x0027B0D6: mov rcx, qword ptr [rbx]
0x0027B0D9: test rcx, rcx
0x0027B0DC: je 0x14027b11a
0x0027B0DE: mov rax, qword ptr [rcx + 0x38]
0x0027B0E2: cmp qword ptr [rax], 0
0x0027B0E6: je 0x14027b109
0x0027B0E8: mov rdx, qword ptr [rcx + 0x50]
0x0027B0EC: mov eax, dword ptr [rdx]
0x0027B0EE: test eax, eax
0x0027B0F0: jle 0x14027b109
0x0027B0F2: dec eax
0x0027B0F4: mov dword ptr [rdx], eax
0x0027B0F6: mov rcx, qword ptr [rcx + 0x38]
0x0027B0FA: mov rdx, qword ptr [rcx]
0x0027B0FD: lea rax, [rdx + 1]
0x0027B101: mov qword ptr [rcx], rax
0x0027B104: movzx eax, byte ptr [rdx]
0x0027B107: jmp 0x14027b10f
0x0027B109: mov rax, qword ptr [rcx]
0x0027B10C: call qword ptr [rax + 0x38]
0x0027B10F: cmp eax, -1
0x0027B112: je 0x14027b11a
0x0027B114: mov byte ptr [rbx + 8], 0
0x0027B118: jmp 0x14027b121
0x0027B11A: mov qword ptr [rbx], rdi
```

#### `call` `0x0027B1C3`

```asm
0x0027B18A: inc rsi
0x0027B18D: mov rcx, qword ptr [rbx]
0x0027B190: test rcx, rcx
0x0027B193: je 0x14027b1cf
0x0027B195: mov rax, qword ptr [rcx + 0x38]
0x0027B199: cmp qword ptr [rax], 0
0x0027B19D: je 0x14027b1c0
0x0027B19F: mov rdx, qword ptr [rcx + 0x50]
0x0027B1A3: mov eax, dword ptr [rdx]
0x0027B1A5: test eax, eax
0x0027B1A7: jle 0x14027b1c0
0x0027B1A9: dec eax
0x0027B1AB: mov dword ptr [rdx], eax
0x0027B1AD: mov rcx, qword ptr [rcx + 0x38]
0x0027B1B1: mov rdx, qword ptr [rcx]
0x0027B1B4: lea rax, [rdx + 1]
0x0027B1B8: mov qword ptr [rcx], rax
0x0027B1BB: movzx eax, byte ptr [rdx]
0x0027B1BE: jmp 0x14027b1c6
0x0027B1C0: mov rax, qword ptr [rcx]
0x0027B1C3: call qword ptr [rax + 0x38]
0x0027B1C6: cmp eax, -1
0x0027B1C9: jne 0x14027b272
0x0027B1CF: xor r12d, r12d
0x0027B1D2: mov qword ptr [rbx], r12
0x0027B1D5: mov byte ptr [rbx + 8], 1
```

#### `call` `0x0027B266`

```asm
0x0027B22D: inc rsi
0x0027B230: mov rcx, qword ptr [rbx]
0x0027B233: test rcx, rcx
0x0027B236: je 0x14027b1cf
0x0027B238: mov rax, qword ptr [rcx + 0x38]
0x0027B23C: cmp qword ptr [rax], 0
0x0027B240: je 0x14027b263
0x0027B242: mov rdx, qword ptr [rcx + 0x50]
0x0027B246: mov eax, dword ptr [rdx]
0x0027B248: test eax, eax
0x0027B24A: jle 0x14027b263
0x0027B24C: dec eax
0x0027B24E: mov dword ptr [rdx], eax
0x0027B250: mov rcx, qword ptr [rcx + 0x38]
0x0027B254: mov rdx, qword ptr [rcx]
0x0027B257: lea rax, [rdx + 1]
0x0027B25B: mov qword ptr [rcx], rax
0x0027B25E: movzx eax, byte ptr [rdx]
0x0027B261: jmp 0x14027b269
0x0027B263: mov rax, qword ptr [rcx]
0x0027B266: call qword ptr [rax + 0x38]
0x0027B269: cmp eax, -1
0x0027B26C: je 0x14027b1cf
0x0027B272: mov byte ptr [rbx + 8], 0
0x0027B276: xor r12d, r12d
0x0027B279: mov rdx, r13
```

#### `call` `0x0027B316`

```asm
0x0027B2DB: mov byte ptr [rsp + 0x20], r14b
0x0027B2E0: mov rcx, qword ptr [rbx]
0x0027B2E3: test rcx, rcx
0x0027B2E6: je 0x14027b324
0x0027B2E8: mov rax, qword ptr [rcx + 0x38]
0x0027B2EC: cmp qword ptr [rax], 0
0x0027B2F0: je 0x14027b313
0x0027B2F2: mov rdx, qword ptr [rcx + 0x50]
0x0027B2F6: mov eax, dword ptr [rdx]
0x0027B2F8: test eax, eax
0x0027B2FA: jle 0x14027b313
0x0027B2FC: dec eax
0x0027B2FE: mov dword ptr [rdx], eax
0x0027B300: mov rcx, qword ptr [rcx + 0x38]
0x0027B304: mov rdx, qword ptr [rcx]
0x0027B307: lea rax, [rdx + 1]
0x0027B30B: mov qword ptr [rcx], rax
0x0027B30E: movzx eax, byte ptr [rdx]
0x0027B311: jmp 0x14027b319
0x0027B313: mov rax, qword ptr [rcx]
0x0027B316: call qword ptr [rax + 0x38]
0x0027B319: cmp eax, -1
0x0027B31C: je 0x14027b324
0x0027B31E: mov byte ptr [rbx + 8], 0
0x0027B322: jmp 0x14027b32b
0x0027B324: mov qword ptr [rbx], r12
```

#### `call` `0x0027B41B`

```asm
0x0027B3E0: mov byte ptr [rsp + 0x20], 1
0x0027B3E5: mov rcx, qword ptr [rbx]
0x0027B3E8: test rcx, rcx
0x0027B3EB: je 0x14027b429
0x0027B3ED: mov rax, qword ptr [rcx + 0x38]
0x0027B3F1: cmp qword ptr [rax], 0
0x0027B3F5: je 0x14027b418
0x0027B3F7: mov rdx, qword ptr [rcx + 0x50]
0x0027B3FB: mov eax, dword ptr [rdx]
0x0027B3FD: test eax, eax
0x0027B3FF: jle 0x14027b418
0x0027B401: dec eax
0x0027B403: mov dword ptr [rdx], eax
0x0027B405: mov rcx, qword ptr [rcx + 0x38]
0x0027B409: mov rdx, qword ptr [rcx]
0x0027B40C: lea rax, [rdx + 1]
0x0027B410: mov qword ptr [rcx], rax
0x0027B413: movzx eax, byte ptr [rdx]
0x0027B416: jmp 0x14027b41e
0x0027B418: mov rax, qword ptr [rcx]
0x0027B41B: call qword ptr [rax + 0x38]
0x0027B41E: cmp eax, -1
0x0027B421: je 0x14027b429
0x0027B423: mov byte ptr [rbx + 8], 0
0x0027B427: jmp 0x14027b430
0x0027B429: mov qword ptr [rbx], r12
```

#### `call` `0x0027B58A`

```asm
0x0027B543: mov rdi, rax
0x0027B546: lea rdx, [rbp - 0x31]
0x0027B54A: mov rcx, rax
0x0027B54D: call 0x1400aa6c0
0x0027B552: nop
0x0027B553: cmp qword ptr [rbp - 0x21], 0
0x0027B558: jne 0x14027b55e
0x0027B55A: xor al, al
0x0027B55C: jmp 0x14027b567
0x0027B55E: mov rax, qword ptr [rdi]
0x0027B561: mov rcx, rdi
0x0027B564: call qword ptr [rax + 0x20]
0x0027B567: mov byte ptr [rbp - 0x77], al
0x0027B56A: mov rcx, rsi
0x0027B56D: call 0x1400309f0
0x0027B572: mov r10, qword ptr [rax]
0x0027B575: lea r9, [rbp - 0x11]
0x0027B579: lea r8, [rip + 0x44b71b]
0x0027B580: lea rdx, [rip + 0x44b6f9]
0x0027B587: mov rcx, rax
0x0027B58A: call qword ptr [r10 + 0x38]
0x0027B58E: mov r12, r15
0x0027B591: mov rdx, r14
0x0027B594: mov rcx, rbx
0x0027B597: call 0x14027c9c0
0x0027B59C: test al, al
```

#### `call` `0x0027B8C3`

```asm
0x0027B88A: inc rsi
0x0027B88D: mov rcx, qword ptr [rbx]
0x0027B890: test rcx, rcx
0x0027B893: je 0x14027b8d1
0x0027B895: mov rax, qword ptr [rcx + 0x38]
0x0027B899: cmp qword ptr [rax], 0
0x0027B89D: je 0x14027b8c0
0x0027B89F: mov rdx, qword ptr [rcx + 0x50]
0x0027B8A3: mov eax, dword ptr [rdx]
0x0027B8A5: test eax, eax
0x0027B8A7: jle 0x14027b8c0
0x0027B8A9: dec eax
0x0027B8AB: mov dword ptr [rdx], eax
0x0027B8AD: mov rcx, qword ptr [rcx + 0x38]
0x0027B8B1: mov rdx, qword ptr [rcx]
0x0027B8B4: lea rax, [rdx + 1]
0x0027B8B8: mov qword ptr [rcx], rax
0x0027B8BB: movzx eax, byte ptr [rdx]
0x0027B8BE: jmp 0x14027b8c6
0x0027B8C0: mov rax, qword ptr [rcx]
0x0027B8C3: call qword ptr [rax + 0x38]
0x0027B8C6: cmp eax, -1
0x0027B8C9: je 0x14027b8d1
0x0027B8CB: mov byte ptr [rbx + 8], 0
0x0027B8CF: jmp 0x14027b8dc
0x0027B8D1: mov qword ptr [rbx], 0
```

#### `call` `0x00287DEC`

```asm
0x00287D84: sub rsp, 0xd0
0x00287D8B: mov qword ptr [rsp + 0x60], 0xfffffffffffffffe
0x00287D94: mov rax, qword ptr [rip + 0x54eb55]
0x00287D9B: xor rax, rsp
0x00287D9E: mov qword ptr [rsp + 0xc0], rax
0x00287DA6: mov rsi, r8
0x00287DA9: mov r8, rcx
0x00287DAC: mov rbx, qword ptr [rsp + 0x110]
0x00287DB4: mov rcx, qword ptr [rsp + 0x118]
0x00287DBC: xor eax, eax
0x00287DBE: mov qword ptr [rsp + 0x40], rax
0x00287DC3: mov rax, qword ptr [rcx]
0x00287DC6: lea r10, [rsp + 0x48]
0x00287DCB: mov qword ptr [rsp + 0x38], r10
0x00287DD0: mov qword ptr [rsp + 0x30], r9
0x00287DD5: mov qword ptr [rsp + 0x28], rsi
0x00287DDA: lea r9, [rsp + 0x68]
0x00287DDF: mov qword ptr [rsp + 0x20], r9
0x00287DE4: mov r9, rdx
0x00287DE7: lea rdx, [rsp + 0x40]
0x00287DEC: call qword ptr [rax + 0x38]
0x00287DEF: mov edi, eax
0x00287DF1: test eax, eax
0x00287DF3: je 0x140287e89
0x00287DF9: call 0x14028d720
0x00287DFE: mov rbx, rax
```

#### `call` `0x0028E036`

```asm
0x0028DFDF: mov edi, r8d
0x0028DFE2: mov esi, edx
0x0028DFE4: mov rbx, rcx
0x0028DFE7: test rcx, rcx
0x0028DFEA: je 0x14028e0a6
0x0028DFF0: cmp r8d, 1
0x0028DFF4: ja 0x14028e0a6
0x0028DFFA: cmp edx, 4
0x0028DFFD: ja 0x14028e0a6
0x0028E003: cmp qword ptr [rcx + 0x38], 0
0x0028E008: jne 0x14028e015
0x0028E00A: lea rax, [rip + 0x14f]
0x0028E011: mov qword ptr [rcx + 0x38], rax
0x0028E015: cmp qword ptr [rcx + 0x40], 0
0x0028E01A: jne 0x14028e027
0x0028E01C: lea rax, [rip + 0x14d]
0x0028E023: mov qword ptr [rcx + 0x40], rax
0x0028E027: mov rcx, qword ptr [rcx + 0x48]
0x0028E02B: mov edx, 0xfa90
0x0028E030: mov r8d, 1
0x0028E036: call qword ptr [rbx + 0x38]
0x0028E039: test rax, rax
0x0028E03C: jne 0x14028e053
0x0028E03E: mov eax, 0xfffffffd
0x0028E043: mov rbx, qword ptr [rsp + 0x30]
0x0028E048: mov rsi, qword ptr [rsp + 0x38]
```

#### `call` `0x0028F1EF`

```asm
0x0028F1AA: inc dword ptr [rax + 0x10]
0x0028F1AD: cmp dword ptr [rbx + 0x24], 8
0x0028F1B1: jl 0x14028f170
0x0028F1B3: mov ecx, dword ptr [rbx + 0x24]
0x0028F1B6: mov eax, dword ptr [rbx + 0x20]
0x0028F1B9: add ecx, -8
0x0028F1BC: shr eax, cl
0x0028F1BE: movzx edx, al
0x0028F1C1: mov dword ptr [rbx + 0x24], ecx
0x0028F1C4: mov dword ptr [rbx + 0x28], edx
0x0028F1C7: lea eax, [rdx - 0x31]
0x0028F1CA: cmp eax, 8
0x0028F1CD: ja 0x14028f085
0x0028F1D3: add edx, -0x30
0x0028F1D6: mov r8d, 1
0x0028F1DC: mov dword ptr [rbx + 0x28], edx
0x0028F1DF: mov rcx, qword ptr [rdi + 0x48]
0x0028F1E3: cmp byte ptr [rbx + 0x2c], r14b
0x0028F1E7: je 0x14028f231
0x0028F1E9: imul edx, edx, 0x30d40
0x0028F1EF: call qword ptr [rdi + 0x38]
0x0028F1F2: imul edx, dword ptr [rbx + 0x28], 0x186a0
0x0028F1F9: mov r8d, 1
0x0028F1FF: mov qword ptr [rbx + 0xc58], rax
0x0028F206: mov rcx, qword ptr [rdi + 0x48]
0x0028F20A: inc edx
```

#### `call` `0x0028F20E`

```asm
0x0028F1BE: movzx edx, al
0x0028F1C1: mov dword ptr [rbx + 0x24], ecx
0x0028F1C4: mov dword ptr [rbx + 0x28], edx
0x0028F1C7: lea eax, [rdx - 0x31]
0x0028F1CA: cmp eax, 8
0x0028F1CD: ja 0x14028f085
0x0028F1D3: add edx, -0x30
0x0028F1D6: mov r8d, 1
0x0028F1DC: mov dword ptr [rbx + 0x28], edx
0x0028F1DF: mov rcx, qword ptr [rdi + 0x48]
0x0028F1E3: cmp byte ptr [rbx + 0x2c], r14b
0x0028F1E7: je 0x14028f231
0x0028F1E9: imul edx, edx, 0x30d40
0x0028F1EF: call qword ptr [rdi + 0x38]
0x0028F1F2: imul edx, dword ptr [rbx + 0x28], 0x186a0
0x0028F1F9: mov r8d, 1
0x0028F1FF: mov qword ptr [rbx + 0xc58], rax
0x0028F206: mov rcx, qword ptr [rdi + 0x48]
0x0028F20A: inc edx
0x0028F20C: sar edx, 1
0x0028F20E: call qword ptr [rdi + 0x38]
0x0028F211: mov qword ptr [rbx + 0xc60], rax
0x0028F218: cmp qword ptr [rbx + 0xc58], r14
0x0028F21F: je 0x14028f226
0x0028F221: test rax, rax
0x0028F224: jne 0x14028f24f
```

#### `call` `0x0028F237`

```asm
0x0028F1DF: mov rcx, qword ptr [rdi + 0x48]
0x0028F1E3: cmp byte ptr [rbx + 0x2c], r14b
0x0028F1E7: je 0x14028f231
0x0028F1E9: imul edx, edx, 0x30d40
0x0028F1EF: call qword ptr [rdi + 0x38]
0x0028F1F2: imul edx, dword ptr [rbx + 0x28], 0x186a0
0x0028F1F9: mov r8d, 1
0x0028F1FF: mov qword ptr [rbx + 0xc58], rax
0x0028F206: mov rcx, qword ptr [rdi + 0x48]
0x0028F20A: inc edx
0x0028F20C: sar edx, 1
0x0028F20E: call qword ptr [rdi + 0x38]
0x0028F211: mov qword ptr [rbx + 0xc60], rax
0x0028F218: cmp qword ptr [rbx + 0xc58], r14
0x0028F21F: je 0x14028f226
0x0028F221: test rax, rax
0x0028F224: jne 0x14028f24f
0x0028F226: mov r14d, 0xfffffffd
0x0028F22C: jmp 0x1402912f6
0x0028F231: imul edx, edx, 0x61a80
0x0028F237: call qword ptr [rdi + 0x38]
0x0028F23A: mov qword ptr [rbx + 0xc50], rax
0x0028F241: test rax, rax
0x0028F244: jne 0x14028f24f
0x0028F246: lea r14d, [rax - 3]
0x0028F24A: jmp 0x1402912f6
```

#### `jmp` `0x002942A1`

```asm
0x00294255: call 0x1403b2500
0x0029425A: sub rsp, rax
0x0029425D: cmp qword ptr [rcx + 0x30], 0
0x00294262: jne 0x14029428c
0x00294264: mov edx, 0x10e
0x00294269: mov dword ptr [rsp + 0x20], 0x409
0x00294271: lea r9, [rip + 0x4fd140]
0x00294278: lea ecx, [rax - 0x24]
0x0029427B: lea r8d, [rdx + 6]
0x0029427F: call 0x1402c3c30
0x00294284: or eax, 0xffffffff
0x00294287: add rsp, 0x38
0x0029428B: ret
0x0029428C: test byte ptr [rcx + 0x44], 2
0x00294290: je 0x140294299
0x00294292: xor eax, eax
0x00294294: add rsp, 0x38
0x00294298: ret
0x00294299: mov rax, qword ptr [rcx + 8]
0x0029429D: add rsp, 0x38
0x002942A1: jmp qword ptr [rax + 0x38]
0x002942A5: int3
0x002942A6: int3
0x002942A7: int3
0x002942A8: int3
0x002942A9: int3
```

#### `call` `0x00295CE1`

```asm
0x00295C8B: call 0x1402b5b30
0x00295C90: test eax, eax
0x00295C92: je 0x140296248
0x00295C98: mov r14, r13
0x00295C9B: nop dword ptr [rax + rax]
0x00295CA0: mov rdx, qword ptr [rsi + 0x80]
0x00295CA7: mov rax, qword ptr [rdx + 0x1c0]
0x00295CAE: mov rcx, qword ptr [r14 + rax]
0x00295CB2: test rcx, rcx
0x00295CB5: je 0x140295d0d
0x00295CB7: mov rax, qword ptr [rsi + 8]
0x00295CBB: movsxd rbx, ebp
0x00295CBE: add rbx, rdx
0x00295CC1: mov rdi, qword ptr [rax + 0xc8]
0x00295CC8: call 0x1402cc830
0x00295CCD: mov rcx, rax
0x00295CD0: call 0x1402d5ee0
0x00295CD5: mov edx, eax
0x00295CD7: lea r8, [rbx + 0x210]
0x00295CDE: mov rcx, rsi
0x00295CE1: call qword ptr [rdi + 0x38]
0x00295CE4: mov rax, qword ptr [rsi + 0x80]
0x00295CEB: mov rcx, qword ptr [rax + 0x1c0]
0x00295CF2: mov rcx, qword ptr [rcx + r14]
0x00295CF6: call 0x1402cc830
0x00295CFB: mov rcx, rax
```

#### `call` `0x0029FC71`

```asm
0x0029FC21: call 0x1402de9e0
0x0029FC26: test eax, eax
0x0029FC28: jle 0x14029ffcd
0x0029FC2E: call 0x1402c54e0
0x0029FC33: mov qword ptr [rsp + 0x28], rax
0x0029FC38: lea r9d, [rdi + 1]
0x0029FC3C: mov r8d, 0xf8
0x0029FC42: mov dword ptr [rsp + 0x20], edi
0x0029FC46: or edx, 0xffffffff
0x0029FC49: mov rcx, r15
0x0029FC4C: call 0x1402ddb80
0x0029FC51: test eax, eax
0x0029FC53: jle 0x14029fc77
0x0029FC55: mov rax, qword ptr [rsi + 8]
0x0029FC59: mov r9, qword ptr [rax + 0xc8]
0x0029FC60: test byte ptr [r9 + 0x70], 2
0x0029FC65: jne 0x14029fc7c
0x0029FC67: lea r8, [rbp - 0x39]
0x0029FC6B: mov rcx, rsi
0x0029FC6E: lea edx, [rdi + 0x40]
0x0029FC71: call qword ptr [r9 + 0x38]
0x0029FC75: jmp 0x14029fc7c
0x0029FC77: call 0x1402c3280
0x0029FC7C: mov rax, qword ptr [rsi + 8]
0x0029FC80: mov r9, qword ptr [rax + 0xc8]
0x0029FC87: test byte ptr [r9 + 0x70], 2
```

#### `call` `0x0029FD8F`

```asm
0x0029FD33: mov byte ptr [rbx + 3], al
0x0029FD36: mov ebx, dword ptr [rsp + 0x34]
0x0029FD3A: add ebx, 4
0x0029FD3D: call 0x1402b5b30
0x0029FD42: test eax, eax
0x0029FD44: je 0x14029fff1
0x0029FD4A: jmp 0x14029ff5f
0x0029FD4F: mov dword ptr [rsp + 0x20], 0xcdd
0x0029FD57: lea r9, [rip + 0x4f2832]
0x0029FD5E: mov r8d, 6
0x0029FD64: jmp 0x14029ffe2
0x0029FD69: mov dword ptr [rsp + 0x20], 0xcd2
0x0029FD71: lea r9, [rip + 0x4f2808]
0x0029FD78: jmp 0x14029ffdc
0x0029FD7D: mov eax, dword ptr [r14]
0x0029FD80: cmp eax, 6
0x0029FD83: jne 0x14029fdf5
0x0029FD85: lea r8, [rbp - 0x49]
0x0029FD89: mov rcx, rsi
0x0029FD8C: lea edx, [rax - 2]
0x0029FD8F: call qword ptr [r9 + 0x38]
0x0029FD93: mov rax, qword ptr [r14 + 0x20]
0x0029FD97: lea r9, [rbx + 2]
0x0029FD9B: mov qword ptr [rsp + 0x28], rax
0x0029FDA0: lea rdx, [rbp - 0x49]
0x0029FDA4: mov r8d, 0x24
```

#### `call` `0x0029FECE`

```asm
0x0029FE6A: mov r8d, 0x14
0x0029FE70: lea rax, [rsp + 0x30]
0x0029FE75: mov qword ptr [rsp + 0x20], rax
0x0029FE7A: call 0x1402e21f0
0x0029FE7F: test eax, eax
0x0029FE81: jne 0x14029fe40
0x0029FE83: mov dword ptr [rsp + 0x20], 0xd05
0x0029FE8B: lea r9, [rip + 0x4f274e]
0x0029FE92: lea r8d, [rax + 0x2a]
0x0029FE96: jmp 0x14029ffe2
0x0029FE9B: add eax, 0xfffffcd5
0x0029FEA0: cmp eax, 1
0x0029FEA3: jbe 0x14029feb9
0x0029FEA5: mov dword ptr [rsp + 0x20], 0xd1d
0x0029FEAD: lea r9, [rip + 0x4f276c]
0x0029FEB4: jmp 0x14029ffdc
0x0029FEB9: lea r8, [rbp - 0x49]
0x0029FEBD: mov qword ptr [rsp + 0x38], 0x40
0x0029FEC6: mov edx, 0x329
0x0029FECB: mov rcx, rsi
0x0029FECE: call qword ptr [r9 + 0x38]
0x0029FED2: mov r14d, 0x20
0x0029FED8: lea r9, [rbp - 0x49]
0x0029FEDC: lea r8, [rsp + 0x38]
0x0029FEE1: mov qword ptr [rsp + 0x20], r14
0x0029FEE6: lea rdx, [rbp - 0x19]
```

#### `call` `0x002B4833`

```asm
0x002B47CD: mov dword ptr [rbx + 0x60], r15d
0x002B47D1: je 0x1402b4816
0x002B47D3: mov rax, qword ptr [rbx + 0x130]
0x002B47DA: mov ecx, r15d
0x002B47DD: cmp qword ptr [rax + 0xb0], rcx
0x002B47E4: je 0x1402b4b4d
0x002B47EA: mov rax, qword ptr [rbx + 0x80]
0x002B47F1: cmp qword ptr [rax + 0x1b8], rcx
0x002B47F8: je 0x1402b4ca7
0x002B47FE: or dword ptr [rax], 0x20
0x002B4801: mov rcx, rbx
0x002B4804: call 0x1402b5b30
0x002B4809: test eax, eax
0x002B480B: je 0x1402b4cc9
0x002B4811: jmp 0x1402b4b4a
0x002B4816: mov rax, qword ptr [rcx + 0xc8]
0x002B481D: mov edx, 4
0x002B4822: mov r8, qword ptr [rbx + 0x80]
0x002B4829: mov rcx, rbx
0x002B482C: add r8, 0x210
0x002B4833: call qword ptr [rax + 0x38]
0x002B4836: mov rax, qword ptr [rbx + 8]
0x002B483A: mov edx, 0x40
0x002B483F: mov r8, qword ptr [rbx + 0x80]
0x002B4846: mov rcx, rbx
0x002B4849: add r8, 0x220
```

#### `call` `0x002B4857`

```asm
0x002B47F1: cmp qword ptr [rax + 0x1b8], rcx
0x002B47F8: je 0x1402b4ca7
0x002B47FE: or dword ptr [rax], 0x20
0x002B4801: mov rcx, rbx
0x002B4804: call 0x1402b5b30
0x002B4809: test eax, eax
0x002B480B: je 0x1402b4cc9
0x002B4811: jmp 0x1402b4b4a
0x002B4816: mov rax, qword ptr [rcx + 0xc8]
0x002B481D: mov edx, 4
0x002B4822: mov r8, qword ptr [rbx + 0x80]
0x002B4829: mov rcx, rbx
0x002B482C: add r8, 0x210
0x002B4833: call qword ptr [rax + 0x38]
0x002B4836: mov rax, qword ptr [rbx + 8]
0x002B483A: mov edx, 0x40
0x002B483F: mov r8, qword ptr [rbx + 0x80]
0x002B4846: mov rcx, rbx
0x002B4849: add r8, 0x220
0x002B4850: mov r9, qword ptr [rax + 0xc8]
0x002B4857: call qword ptr [r9 + 0x38]
0x002B485B: jmp 0x1402b4b4a
0x002B4860: mov rcx, rbx
0x002B4863: call 0x1402963f0
0x002B4868: mov edi, eax
0x002B486A: test eax, eax
```

#### `call` `0x002B8951`

```asm
0x002B88FC: jbe 0x1402b8d50
0x002B8902: mov rdx, qword ptr [rsp + 0x78]
0x002B8907: lea rcx, [rbp - 0x30]
0x002B890B: mov ebx, r14d
0x002B890E: sub ebx, esi
0x002B8910: call r13
0x002B8913: mov edx, esi
0x002B8915: lea rcx, [rbp + 0x180]
0x002B891C: add rdx, qword ptr [rsp + 0x78]
0x002B8921: mov r8d, ebx
0x002B8924: mov r13d, ebx
0x002B8927: call 0x1403d1f90
0x002B892C: mov rdx, qword ptr [rsp + 0x58]
0x002B8931: lea rcx, [rbp + 0x180]
0x002B8938: mov r8d, esi
0x002B893B: add rcx, r13
0x002B893E: sub r8d, ebx
0x002B8941: call 0x1403d1f90
0x002B8946: lea rdx, [rbp + 0x180]
0x002B894D: lea rcx, [rbp - 0x30]
0x002B8951: call qword ptr [rsp + 0x38]
0x002B8955: xor edx, edx
0x002B8957: mov eax, edi
0x002B8959: div esi
0x002B895B: dec eax
0x002B895D: cmp eax, 1
```

#### `call` `0x002B8BDB`

```asm
0x002B8B8F: cmp r10d, dword ptr [rsp + 0x68]
0x002B8B94: jb 0x1402b8bb6
0x002B8B96: mov ecx, r10d
0x002B8B99: movzx r8d, r15b
0x002B8B9D: sub ecx, esi
0x002B8B9F: add ecx, dword ptr [rsp + 0x24]
0x002B8BA3: movzx edx, byte ptr [rbp + rcx + 0xb0]
0x002B8BAB: and dl, r8b
0x002B8BAE: not r8b
0x002B8BB1: and al, r8b
0x002B8BB4: or al, dl
0x002B8BB6: mov r8d, dword ptr [rsp + 0x2c]
0x002B8BBB: inc r10d
0x002B8BBE: mov edx, dword ptr [rsp + 0x34]
0x002B8BC2: mov byte ptr [rbx], al
0x002B8BC4: inc rbx
0x002B8BC7: cmp r10d, esi
0x002B8BCA: jb 0x1402b8b00
0x002B8BD0: lea rdx, [rbp + 0x200]
0x002B8BD7: lea rcx, [rbp - 0x30]
0x002B8BDB: call qword ptr [rsp + 0x38]
0x002B8BDF: lea rdx, [rbp + 0x200]
0x002B8BE6: lea rcx, [rbp - 0x30]
0x002B8BEA: call qword ptr [rsp + 0x48]
0x002B8BEE: mov r13d, dword ptr [rsp + 0x28]
0x002B8BF3: xor r12d, r12d
```

#### `call` `0x002C384F`

```asm
0x002C37FC: int3
0x002C37FD: int3
0x002C37FE: int3
0x002C37FF: int3
0x002C3800: mov qword ptr [rsp + 8], rbx
0x002C3805: push rdi
0x002C3806: mov eax, 0x260
0x002C380B: call 0x1403b2500
0x002C3810: sub rsp, rax
0x002C3813: mov rax, qword ptr [rip + 0x5130d6]
0x002C381A: xor rax, rsp
0x002C381D: mov qword ptr [rsp + 0x250], rax
0x002C3825: call 0x1402c3fe0
0x002C382A: lea rcx, [rsp + 0x20]
0x002C382F: call 0x1402c1cd0
0x002C3834: lea rdx, [rsp + 0x20]
0x002C3839: lea rcx, [rsp + 0x30]
0x002C383E: call 0x1402c1cc0
0x002C3843: mov rax, qword ptr [rip + 0x526486]
0x002C384A: lea rcx, [rsp + 0x30]
0x002C384F: call qword ptr [rax + 0x38]
0x002C3852: mov rbx, rax
0x002C3855: test rax, rax
0x002C3858: jne 0x1402c3904
0x002C385E: mov r8d, 0x406
0x002C3864: lea rdx, [rip + 0x4dc805]
```

#### `call` `0x002C38DE`

```asm
0x002C3882: mov rcx, rax
0x002C3885: call 0x1402c1cc0
0x002C388A: xor r8d, r8d
0x002C388D: lea rax, [rbx + 0x110]
0x002C3894: mov qword ptr [rbx + 0x210], r8
0x002C389B: lea rcx, [rbx + 0x90]
0x002C38A2: lea edx, [r8 + 0x10]
0x002C38A6: nop word ptr [rax + rax]
0x002C38B0: mov qword ptr [rcx], r8
0x002C38B3: lea rcx, [rcx + 8]
0x002C38B7: mov dword ptr [rax], r8d
0x002C38BA: lea rax, [rax + 4]
0x002C38BE: sub rdx, 1
0x002C38C2: jne 0x1402c38b0
0x002C38C4: mov rax, qword ptr [rip + 0x526405]
0x002C38CB: mov rcx, rbx
0x002C38CE: call qword ptr [rax + 0x40]
0x002C38D1: mov rdx, qword ptr [rip + 0x5263f8]
0x002C38D8: mov rcx, rbx
0x002C38DB: mov rdi, rax
0x002C38DE: call qword ptr [rdx + 0x38]
0x002C38E1: cmp rax, rbx
0x002C38E4: je 0x1402c38f7
0x002C38E6: mov rcx, rbx
0x002C38E9: call 0x1402c3060
0x002C38EE: lea rax, [rip + 0x527cdb]
```

#### `call` `0x002EE12C`

```asm
0x002EE0E8: lea r9, [rip + 0x4c3d89]
0x002EE0EF: mov ecx, 6
0x002EE0F4: lea r8d, [rdx + 5]
0x002EE0F8: call 0x1402c3c30
0x002EE0FD: or eax, 0xffffffff
0x002EE100: mov rbx, qword ptr [rsp + 0x40]
0x002EE105: add rsp, 0x30
0x002EE109: pop rdi
0x002EE10A: ret
0x002EE10B: test rbx, rbx
0x002EE10E: je 0x1402ee0fd
0x002EE110: cmp qword ptr [rdx], 0
0x002EE114: jne 0x1402ee123
0x002EE116: call 0x1402d5f20
0x002EE11B: mov qword ptr [rbx], rax
0x002EE11E: test rax, rax
0x002EE121: je 0x1402ee0fd
0x002EE123: mov rax, qword ptr [rdi]
0x002EE126: mov rcx, rdi
0x002EE129: mov rdx, qword ptr [rbx]
0x002EE12C: call qword ptr [rax + 0x38]
0x002EE12F: mov edi, eax
0x002EE131: test eax, eax
0x002EE133: jg 0x1402ee144
0x002EE135: mov rcx, qword ptr [rbx]
0x002EE138: call 0x1402d5da0
```

#### `jmp` `0x002EE2F5`

```asm
0x002EE2C6: int3
0x002EE2C7: int3
0x002EE2C8: int3
0x002EE2C9: int3
0x002EE2CA: int3
0x002EE2CB: int3
0x002EE2CC: int3
0x002EE2CD: int3
0x002EE2CE: int3
0x002EE2CF: int3
0x002EE2D0: mov eax, 0x28
0x002EE2D5: call 0x1403b2500
0x002EE2DA: sub rsp, rax
0x002EE2DD: mov r9, qword ptr [r8 + 8]
0x002EE2E1: mov rax, qword ptr [r9 + 0x40]
0x002EE2E5: mov dword ptr [rax], ecx
0x002EE2E7: mov rcx, r9
0x002EE2EA: mov rax, qword ptr [r9 + 0x40]
0x002EE2EE: mov dword ptr [rax + 4], edx
0x002EE2F1: add rsp, 0x28
0x002EE2F5: jmp qword ptr [r9 + 0x38]
0x002EE2F9: int3
0x002EE2FA: int3
0x002EE2FB: int3
0x002EE2FC: int3
0x002EE2FD: int3
```

#### `call` `0x0035669F`

```asm
0x00356653: mov rdx, r12
0x00356656: mov qword ptr [rsp + 0x48], r12
0x0035665B: lea r9, [rsi + 0x68]
0x0035665F: mov rcx, rbx
0x00356662: call 0x140325b90
0x00356667: test eax, eax
0x00356669: je 0x140356916
0x0035666F: mov rdx, r12
0x00356672: lea r9, [rsi + 0x68]
0x00356676: mov r12, qword ptr [rsp + 0x30]
0x0035667B: mov r8, r14
0x0035667E: mov rcx, r12
0x00356681: call 0x140325ef0
0x00356686: test eax, eax
0x00356688: je 0x140356916
0x0035668E: mov r9, r12
0x00356691: mov qword ptr [rsp + 0x20], rdi
0x00356696: mov r8, rbx
0x00356699: mov rdx, r14
0x0035669C: mov rcx, rsi
0x0035669F: call qword ptr [rsp + 0x38]
0x003566A3: test eax, eax
0x003566A5: je 0x140356916
0x003566AB: lea r8, [rsi + 0x68]
0x003566AF: mov rdx, r14
0x003566B2: mov rcx, rbx
```

#### `call` `0x0035675C`

```asm
0x00356712: je 0x140356916
0x00356718: lea r8, [r15 + 0x38]
0x0035671C: mov r9, rdi
0x0035671F: mov rdx, r14
0x00356722: mov rcx, rsi
0x00356725: call r12
0x00356728: test eax, eax
0x0035672A: je 0x140356916
0x00356730: mov r9, rdi
0x00356733: mov r8, r14
0x00356736: mov rdx, r14
0x00356739: mov rcx, rsi
0x0035673C: call r12
0x0035673F: test eax, eax
0x00356741: je 0x140356916
0x00356747: lea r9, [rsi + 0x98]
0x0035674E: mov qword ptr [rsp + 0x20], rdi
0x00356753: mov r8, r14
0x00356756: mov rdx, r14
0x00356759: mov rcx, rsi
0x0035675C: call qword ptr [rsp + 0x38]
0x00356760: test eax, eax
0x00356762: je 0x140356916
0x00356768: mov r8, rbx
0x0035676B: mov rdx, r14
0x0035676E: lea r9, [rsi + 0x68]
```

#### `call` `0x003567AE`

```asm
0x00356768: mov r8, rbx
0x0035676B: mov rdx, r14
0x0035676E: lea r9, [rsi + 0x68]
0x00356772: mov rcx, r14
0x00356775: call 0x140325b90
0x0035677A: test eax, eax
0x0035677C: je 0x140356916
0x00356782: lea r12, [r15 + 0x20]
0x00356786: cmp dword ptr [r15 + 0x50], r13d
0x0035678A: je 0x14035679c
0x0035678C: mov rdx, r12
0x0035678F: mov rcx, rbx
0x00356792: call 0x1402d9350
0x00356797: test rax, rax
0x0035679A: jmp 0x1403567b4
0x0035679C: lea r9, [r15 + 0x38]
0x003567A0: mov qword ptr [rsp + 0x20], rdi
0x003567A5: mov r8, r12
0x003567A8: mov rdx, rbx
0x003567AB: mov rcx, rsi
0x003567AE: call qword ptr [rsp + 0x38]
0x003567B2: test eax, eax
0x003567B4: je 0x140356916
0x003567BA: mov r15, qword ptr [rsp + 0x98]
0x003567C2: lea r8, [rsi + 0x68]
0x003567C6: mov rdx, rbx
```

#### `call` `0x00356813`

```asm
0x003567C2: lea r8, [rsi + 0x68]
0x003567C6: mov rdx, rbx
0x003567C9: lea rcx, [r15 + 0x38]
0x003567CD: call 0x140325c00
0x003567D2: test eax, eax
0x003567D4: je 0x140356916
0x003567DA: mov rdx, qword ptr [rsp + 0x40]
0x003567DF: mov r8, r12
0x003567E2: mov r12, qword ptr [rsp + 0x50]
0x003567E7: mov r9, rdi
0x003567EA: mov rcx, rsi
0x003567ED: mov dword ptr [r15 + 0x50], r13d
0x003567F1: call r12
0x003567F4: test eax, eax
0x003567F6: je 0x140356916
0x003567FC: mov r9, qword ptr [rsp + 0x40]
0x00356801: mov rcx, rsi
0x00356804: mov r8, qword ptr [rsp + 0x48]
0x00356809: mov rdx, qword ptr [rsp + 0x30]
0x0035680E: mov qword ptr [rsp + 0x20], rdi
0x00356813: call qword ptr [rsp + 0x38]
0x00356817: test eax, eax
0x00356819: je 0x140356916
0x0035681F: mov rdx, qword ptr [rsp + 0x30]
0x00356824: lea r9, [rsi + 0x68]
0x00356828: mov rcx, rdx
```

#### `call` `0x003568E8`

```asm
0x003568A1: mov r12, qword ptr [rsp + 0x40]
0x003568A6: lea r9, [rsi + 0x68]
0x003568AA: mov rcx, r12
0x003568AD: mov r8d, 3
0x003568B3: mov rdx, rbx
0x003568B6: call 0x140325c70
0x003568BB: test eax, eax
0x003568BD: je 0x140356916
0x003568BF: mov rdx, qword ptr [rsp + 0x30]
0x003568C4: lea r9, [rsi + 0x68]
0x003568C8: mov r8, r15
0x003568CB: mov rcx, rbx
0x003568CE: call 0x140325ef0
0x003568D3: test eax, eax
0x003568D5: je 0x140356916
0x003568D7: mov r9, rbx
0x003568DA: mov qword ptr [rsp + 0x20], rdi
0x003568DF: mov r8, r14
0x003568E2: mov rdx, rbx
0x003568E5: mov rcx, rsi
0x003568E8: call qword ptr [rsp + 0x38]
0x003568EC: test eax, eax
0x003568EE: je 0x140356916
0x003568F0: mov rcx, qword ptr [rsp + 0x98]
0x003568F8: lea r9, [rsi + 0x68]
0x003568FC: add rcx, 0x20
```

#### `jmp` `0x00370C0D`

```asm
0x00370BDD: jmp qword ptr [rax + 0x30]
0x00370BE1: mov byte ptr [rdx], 1
0x00370BE4: xor eax, eax
0x00370BE6: ret
0x00370BE7: int3
0x00370BE8: int3
0x00370BE9: int3
0x00370BEA: int3
0x00370BEB: int3
0x00370BEC: int3
0x00370BED: int3
0x00370BEE: int3
0x00370BEF: int3
0x00370BF0: test rcx, rcx
0x00370BF3: je 0x140370c11
0x00370BF5: mov rax, qword ptr [rcx + 0x3e0]
0x00370BFC: cmp qword ptr [rax + 0x38], 0
0x00370C01: je 0x140370c11
0x00370C03: mov byte ptr [rdx], 0
0x00370C06: mov rax, qword ptr [rcx + 0x3e0]
0x00370C0D: jmp qword ptr [rax + 0x38]
0x00370C11: mov byte ptr [rdx], 1
0x00370C14: xor eax, eax
0x00370C16: ret
0x00370C17: int3
0x00370C18: int3
```

#### `call` `0x0038EC48`

```asm
0x0038EC0E: int3
0x0038EC0F: int3
0x0038EC10: push rbx
0x0038EC12: sub rsp, 0x20
0x0038EC16: mov rbx, rcx
0x0038EC19: test rcx, rcx
0x0038EC1C: je 0x14038ec5b
0x0038EC1E: mov rax, qword ptr [rcx + 0x28]
0x0038EC22: test rax, rax
0x0038EC25: je 0x14038ec5b
0x0038EC27: mov r8, qword ptr [rcx + 0x38]
0x0038EC2B: test r8, r8
0x0038EC2E: je 0x14038ec5b
0x0038EC30: mov rdx, qword ptr [rax + 0x38]
0x0038EC34: test rdx, rdx
0x0038EC37: je 0x14038ec40
0x0038EC39: mov rcx, qword ptr [rcx + 0x40]
0x0038EC3D: call r8
0x0038EC40: mov rdx, qword ptr [rbx + 0x28]
0x0038EC44: mov rcx, qword ptr [rbx + 0x40]
0x0038EC48: call qword ptr [rbx + 0x38]
0x0038EC4B: xor eax, eax
0x0038EC4D: mov qword ptr [rbx + 0x28], 0
0x0038EC55: add rsp, 0x20
0x0038EC59: pop rbx
0x0038EC5A: ret
```

#### `call` `0x0038ED36`

```asm
0x0038ECF7: mov rdi, rax
0x0038ECFA: test rax, rax
0x0038ECFD: jne 0x14038ed17
0x0038ECFF: lea eax, [rdi - 4]
0x0038ED02: mov rbp, qword ptr [rsp + 0x30]
0x0038ED07: mov rdi, qword ptr [rsp + 0x38]
0x0038ED0C: mov rbx, qword ptr [rsp + 0x40]
0x0038ED11: add rsp, 0x20
0x0038ED15: pop rsi
0x0038ED16: ret
0x0038ED17: mov qword ptr [rbx + 0x28], rdi
0x0038ED1B: mov edx, esi
0x0038ED1D: mov rcx, rbx
0x0038ED20: mov qword ptr [rax + 0x38], rbp
0x0038ED24: call 0x14038ed70
0x0038ED29: mov esi, eax
0x0038ED2B: test eax, eax
0x0038ED2D: je 0x14038ed3d
0x0038ED2F: mov rcx, qword ptr [rbx + 0x40]
0x0038ED33: mov rdx, rdi
0x0038ED36: call qword ptr [rbx + 0x38]
0x0038ED39: mov qword ptr [rbx + 0x28], rbp
0x0038ED3D: mov eax, esi
0x0038ED3F: jmp 0x14038ed02
0x0038ED41: mov eax, 0xfffffffa
0x0038ED46: mov rbx, qword ptr [rsp + 0x40]
```

#### `call` `0x0038EDDF`

```asm
0x0038EDAB: mov ebp, r14d
0x0038EDAE: neg ebx
0x0038EDB0: jmp 0x14038edc1
0x0038EDB2: mov ebp, ebx
0x0038EDB4: sar ebp, 4
0x0038EDB7: inc ebp
0x0038EDB9: cmp ebx, 0x30
0x0038EDBC: jge 0x14038edc1
0x0038EDBE: and ebx, 0xf
0x0038EDC1: test ebx, ebx
0x0038EDC3: je 0x14038edcd
0x0038EDC5: lea eax, [rbx - 8]
0x0038EDC8: cmp eax, 7
0x0038EDCB: ja 0x14038ee1f
0x0038EDCD: mov rdx, qword ptr [rsi + 0x38]
0x0038EDD1: test rdx, rdx
0x0038EDD4: je 0x14038ede6
0x0038EDD6: cmp dword ptr [rsi + 0x28], ebx
0x0038EDD9: je 0x14038ede6
0x0038EDDB: mov rcx, qword ptr [rcx + 0x40]
0x0038EDDF: call qword ptr [rdi + 0x38]
0x0038EDE2: mov qword ptr [rsi + 0x38], r14
0x0038EDE6: mov dword ptr [rsi + 8], ebp
0x0038EDE9: mov dword ptr [rsi + 0x28], ebx
0x0038EDEC: mov rax, qword ptr [rdi + 0x28]
0x0038EDF0: test rax, rax
```