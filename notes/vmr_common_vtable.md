# VMR common setter and descriptor vtable

## Common parser containing function `0x00090AB0..0x000914CB`

```asm
0x00090AB0: push rbp
0x00090AB2: push rbx
0x00090AB3: push rsi
0x00090AB4: push rdi
0x00090AB5: push r12
0x00090AB7: push r13
0x00090AB9: push r14
0x00090ABB: push r15
0x00090ABD: lea rbp, [rsp - 0x318]
0x00090AC5: sub rsp, 0x418
0x00090ACC: mov qword ptr [rbp - 0x78], 0xfffffffffffffffe
0x00090AD4: mov rax, qword ptr [rip + 0x745e15]
0x00090ADB: xor rax, rsp
0x00090ADE: mov qword ptr [rbp + 0x300], rax
0x00090AE5: mov r14, r9
0x00090AE8: mov rbx, r8
0x00090AEB: mov rdi, rdx
0x00090AEE: mov r13, rcx
0x00090AF1: mov qword ptr [rbp - 0x70], r9
0x00090AF5: xorps xmm0, xmm0
0x00090AF8: movdqu xmmword ptr [rsp + 0x40], xmm0
0x00090AFE: xor r15d, r15d
0x00090B01: mov qword ptr [rsp + 0x50], r15
0x00090B06: movsxd rdx, dword ptr [rdx]
0x00090B09: shl rdx, 5
0x00090B0D: add rdx, qword ptr [r8]
0x00090B10: mov qword ptr [rbp + 0xa0], 0xf
0x00090B1B: mov qword ptr [rbp + 0x98], r15
0x00090B22: mov byte ptr [rbp + 0x88], r15b
0x00090B29: or r9, 0xffffffffffffffff
0x00090B2D: xor r8d, r8d
0x00090B30: lea rcx, [rbp + 0x88]
0x00090B37: call 0x1400354b0
0x00090B3C: nop
0x00090B3D: mov rcx, qword ptr [rbx + 8]
0x00090B41: sub rcx, qword ptr [rbx]
0x00090B44: sar rcx, 5
0x00090B48: mov eax, dword ptr [rdi]
0x00090B4A: inc eax
0x00090B4C: cmp eax, ecx
0x00090B4E: jl 0x140090dd4
0x00090B54: mov dword ptr [rbp + 0x40], 0x7a
0x00090B5B: mov dword ptr [rbp + 0x44], 0x4b
0x00090B62: mov eax, dword ptr [rbp + 0x44]
0x00090B65: xor eax, 0x37
0x00090B68: mov byte ptr [rbp + 0x48], al
0x00090B6B: movsx ecx, byte ptr [rbp + 0x48]
0x00090B6F: xor ecx, 0x13
0x00090B72: mov byte ptr [rbp + 0x49], cl
0x00090B75: movsx ecx, byte ptr [rbp + 0x49]
0x00090B79: xor ecx, 9
0x00090B7C: mov byte ptr [rbp + 0x4a], cl
0x00090B7F: movsx ecx, byte ptr [rbp + 0x4a]
0x00090B83: xor ecx, 9
0x00090B86: mov byte ptr [rbp + 0x4b], cl
0x00090B89: movsx ecx, byte ptr [rbp + 0x4b]
0x00090B8D: xor ecx, 0x13
0x00090B90: mov byte ptr [rbp + 0x4c], cl
0x00090B93: movsx ecx, byte ptr [rbp + 0x4c]
0x00090B97: xor ecx, 0x14
0x00090B9A: mov byte ptr [rbp + 0x4d], cl
0x00090B9D: movsx ecx, byte ptr [rbp + 0x4d]
0x00090BA1: xor ecx, 0x1d
0x00090BA4: mov byte ptr [rbp + 0x4e], cl
0x00090BA7: movsx ecx, byte ptr [rbp + 0x4e]
0x00090BAB: xor ecx, 0x5a
0x00090BAE: mov byte ptr [rbp + 0x4f], cl
0x00090BB1: movsx ecx, byte ptr [rbp + 0x4f]
0x00090BB5: xor ecx, 0xc
0x00090BB8: mov byte ptr [rbp + 0x50], cl
0x00090BBB: movsx ecx, byte ptr [rbp + 0x50]
0x00090BBF: xor ecx, 0x1b
0x00090BC2: mov byte ptr [rbp + 0x51], cl
0x00090BC5: movsx ecx, byte ptr [rbp + 0x51]
0x00090BC9: xor ecx, 0x16
0x00090BCC: mov byte ptr [rbp + 0x52], cl
0x00090BCF: movsx ecx, byte ptr [rbp + 0x52]
0x00090BD3: xor ecx, 0xf
0x00090BD6: mov byte ptr [rbp + 0x53], cl
0x00090BD9: movsx ecx, byte ptr [rbp + 0x53]
0x00090BDD: xor ecx, 0x1f
0x00090BE0: mov byte ptr [rbp + 0x54], cl
0x00090BE3: movsx ecx, byte ptr [rbp + 0x54]
0x00090BE7: xor ecx, 0x52
0x00090BEA: mov byte ptr [rbp + 0x55], cl
0x00090BED: movsx ecx, byte ptr [rbp + 0x55]
0x00090BF1: xor ecx, 9
0x00090BF4: mov byte ptr [rbp + 0x56], cl
0x00090BF7: movsx ecx, byte ptr [rbp + 0x56]
0x00090BFB: xor ecx, 0x53
0x00090BFE: mov byte ptr [rbp + 0x57], cl
0x00090C01: movsx ecx, byte ptr [rbp + 0x57]
0x00090C05: xor ecx, 0x5a
0x00090C08: mov byte ptr [rbp + 0x58], cl
0x00090C0B: movsx ecx, byte ptr [rbp + 0x58]
0x00090C0F: xor ecx, 0x13
0x00090C12: mov byte ptr [rbp + 0x59], cl
0x00090C15: movsx ecx, byte ptr [rbp + 0x59]
0x00090C19: xor ecx, 0x14
0x00090C1C: mov byte ptr [rbp + 0x5a], cl
0x00090C1F: movsx ecx, byte ptr [rbp + 0x5a]
0x00090C23: xor ecx, 0x5a
0x00090C26: mov byte ptr [rbp + 0x5b], cl
0x00090C29: movsx ecx, byte ptr [rbp + 0x5b]
0x00090C2D: xor ecx, 1
0x00090C30: mov byte ptr [rbp + 0x5c], cl
0x00090C33: movsx ecx, byte ptr [rbp + 0x5c]
0x00090C37: xor ecx, 7
0x00090C3A: mov byte ptr [rbp + 0x5d], cl
0x00090C3D: movsx ecx, byte ptr [rbp + 0x5d]
0x00090C41: xor ecx, 0x5a
0x00090C44: mov byte ptr [rbp + 0x5e], cl
0x00090C47: movsx ecx, byte ptr [rbp + 0x5e]
0x00090C4B: xor ecx, 0x15
0x00090C4E: mov byte ptr [rbp + 0x5f], cl
0x00090C51: movsx ecx, byte ptr [rbp + 0x5f]
0x00090C55: xor ecx, 0xa
0x00090C58: mov byte ptr [rbp + 0x60], cl
0x00090C5B: movsx ecx, byte ptr [rbp + 0x60]
0x00090C5F: xor ecx, 0xe
0x00090C62: mov byte ptr [rbp + 0x61], cl
0x00090C65: movsx ecx, byte ptr [rbp + 0x61]
0x00090C69: xor ecx, 0x13
0x00090C6C: mov byte ptr [rbp + 0x62], cl
0x00090C6F: movsx ecx, byte ptr [rbp + 0x62]
0x00090C73: xor ecx, 0x15
0x00090C76: mov byte ptr [rbp + 0x63], cl
0x00090C79: movsx ecx, byte ptr [rbp + 0x63]
0x00090C7D: xor ecx, 0x14
0x00090C80: mov byte ptr [rbp + 0x64], cl
0x00090C83: xor eax, eax
0x00090C85: mov byte ptr [rbp + 0x65], al
0x00090C88: movzx eax, byte ptr [rbp + 0x48]
0x00090C8C: lea rdx, [rbp + 0x1d0]
0x00090C93: lea rcx, [rbp + 0x40]
0x00090C97: call 0x14003a9b0
0x00090C9C: nop
0x00090C9D: cmp qword ptr [rax + 0x18], 0x10
0x00090CA2: jb 0x140090ca7
0x00090CA4: mov rax, qword ptr [rax]
0x00090CA7: lea r8, [rbp + 0x88]
0x00090CAE: mov rdx, rax
0x00090CB1: lea rcx, [rbp + 0xa8]
0x00090CB8: call 0x14003f750
0x00090CBD: nop
0x00090CBE: mov rdx, rax
0x00090CC1: lea rcx, [rip + 0x75be88]
0x00090CC8: call 0x140058590
0x00090CCD: mov rcx, rax
0x00090CD0: call 0x140062570
0x00090CD5: nop
0x00090CD6: mov rax, qword ptr [rbp + 0xc0]
0x00090CDD: cmp rax, 0x10
0x00090CE1: jb 0x140090d32
0x00090CE3: inc rax
0x00090CE6: mov rcx, qword ptr [rbp + 0xa8]
0x00090CED: cmp rax, 0x1000
0x00090CF3: jb 0x140090d2d
0x00090CF5: test cl, 0x1f
0x00090CF8: je 0x140090d00
0x00090CFA: call 0x1403db020
0x00090CFF: int3
0x00090D00: mov rax, qword ptr [rcx - 8]
0x00090D04: cmp rax, rcx
0x00090D07: jb 0x140090d0f
0x00090D09: call 0x1403db020
0x00090D0E: int3
0x00090D0F: sub rcx, rax
0x00090D12: cmp rcx, 8
0x00090D16: jae 0x140090d1e
0x00090D18: call 0x1403db020
0x00090D1D: int3
0x00090D1E: cmp rcx, 0x27
0x00090D22: jbe 0x140090d2a
0x00090D24: call 0x1403db020
0x00090D29: int3
0x00090D2A: mov rcx, rax
0x00090D2D: call 0x1403b20d4
0x00090D32: mov qword ptr [rbp + 0xc0], 0xf
0x00090D3D: mov qword ptr [rbp + 0xb8], r15
0x00090D44: mov byte ptr [rbp + 0xa8], 0
0x00090D4B: mov rax, qword ptr [rbp + 0x1e8]
0x00090D52: cmp rax, 0x10
0x00090D56: jb 0x140090da7
0x00090D58: inc rax
0x00090D5B: mov rcx, qword ptr [rbp + 0x1d0]
0x00090D62: cmp rax, 0x1000
0x00090D68: jb 0x140090da2
0x00090D6A: test cl, 0x1f
0x00090D6D: je 0x140090d75
0x00090D6F: call 0x1403db020
0x00090D74: int3
0x00090D75: mov rax, qword ptr [rcx - 8]
0x00090D79: cmp rax, rcx
0x00090D7C: jb 0x140090d84
0x00090D7E: call 0x1403db020
0x00090D83: int3
0x00090D84: sub rcx, rax
0x00090D87: cmp rcx, 8
0x00090D8B: jae 0x140090d93
0x00090D8D: call 0x1403db020
0x00090D92: int3
0x00090D93: cmp rcx, 0x27
0x00090D97: jbe 0x140090d9f
0x00090D99: call 0x1403db020
0x00090D9E: int3
0x00090D9F: mov rcx, rax
0x00090DA2: call 0x1403b20d4
0x00090DA7: xor edx, edx
0x00090DA9: lea r8d, [rdx + 0x70]
0x00090DAD: lea rcx, [rbp + 0x290]
0x00090DB4: call 0x1403d3050
0x00090DB9: mov edx, 1
0x00090DBE: lea rcx, [rbp + 0x290]
0x00090DC5: call 0x14008a650
0x00090DCA: nop
0x00090DCB: mov rcx, rax
0x00090DCE: call 0x14008a330
0x00090DD3: nop
0x00090DD4: mov dword ptr [rdi], eax
0x00090DD6: movsxd rdx, eax
0x00090DD9: shl rdx, 5
0x00090DDD: add rdx, qword ptr [rbx]
0x00090DE0: mov qword ptr [rbp + 0x80], 0xf
0x00090DEB: mov qword ptr [rbp + 0x78], r15
0x00090DEF: mov byte ptr [rbp + 0x68], 0
0x00090DF3: or r9, 0xffffffffffffffff
0x00090DF7: xor r8d, r8d
0x00090DFA: lea rcx, [rbp + 0x68]
0x00090DFE: call 0x1400354b0
0x00090E03: nop
0x00090E04: mov rbx, qword ptr [rbp + 0x78]
0x00090E08: test rbx, rbx
0x00090E0B: je 0x140091019
0x00090E11: cmp rbx, 1
0x00090E15: jb 0x140090ef0
0x00090E1B: lea rdi, [rbp + 0x68]
0x00090E1F: cmp qword ptr [rbp + 0x80], 0x10
0x00090E27: cmovae rdi, qword ptr [rbp + 0x68]
0x00090E2C: nop dword ptr [rax]
0x00090E30: test rbx, rbx
0x00090E33: je 0x140090eec
0x00090E39: mov r8, rbx
0x00090E3C: mov edx, 0x3a
0x00090E41: mov rcx, rdi
0x00090E44: call 0x1403d31f0
0x00090E49: mov rcx, rax
0x00090E4C: test rax, rax
0x00090E4F: je 0x140090eec
0x00090E55: cmp byte ptr [rax], 0x3a
0x00090E58: je 0x140090e69
0x00090E5A: sub rdi, rax
0x00090E5D: dec rdi
0x00090E60: add rbx, rdi
0x00090E63: lea rdi, [rax + 1]
0x00090E67: jmp 0x140090e30
0x00090E69: lea rax, [rbp + 0x68]
0x00090E6D: cmp qword ptr [rbp + 0x80], 0x10
0x00090E75: cmovae rax, qword ptr [rbp + 0x68]
0x00090E7A: sub rcx, rax
0x00090E7D: cmp rcx, -1
0x00090E81: je 0x140090eec
0x00090E83: lea r9, [rip + 0x3a7848]
0x00090E8A: lea r8, [rip + 0x3a7840]
0x00090E91: mov rdx, r14
0x00090E94: lea rcx, [rbp - 8]
0x00090E98: call 0x1400889b0
0x00090E9D: mov rdx, rax
0x00090EA0: lea rcx, [rbp - 0x48]
0x00090EA4: call 0x140087840
0x00090EA9: mov byte ptr [rsp + 0x30], 0
0x00090EAE: mov qword ptr [rsp + 0x28], rax
0x00090EB3: mov eax, dword ptr [rbp + 0x388]
0x00090EB9: mov dword ptr [rsp + 0x20], eax
0x00090EBD: mov r9d, dword ptr [rbp + 0x380]
0x00090EC4: lea r8, [rbp + 0x68]
0x00090EC8: lea rdx, [rbp + 0x88]
0x00090ECF: mov rcx, r13
0x00090ED2: call 0x140091d10
0x00090ED7: test al, al
0x00090ED9: jne 0x14009144a
0x00090EDF: lea rcx, [rbp + 0x88]
0x00090EE6: call 0x140093610
0x00090EEB: int3
0x00090EEC: mov rbx, qword ptr [rbp + 0x78]
0x00090EF0: test rbx, rbx
0x00090EF3: je 0x140091019
0x00090EF9: cmp rbx, 1
0x00090EFD: jb 0x140091019
0x00090F03: lea rdi, [rbp + 0x68]
0x00090F07: cmp qword ptr [rbp + 0x80], 0x10
0x00090F0F: cmovae rdi, qword ptr [rbp + 0x68]
0x00090F14: test rbx, rbx
0x00090F17: je 0x140091015
0x00090F1D: mov r8, rbx
0x00090F20: mov edx, 0x2c
0x00090F25: mov rcx, rdi
0x00090F28: call 0x1403d31f0
0x00090F2D: mov rcx, rax
0x00090F30: test rax, rax
0x00090F33: je 0x140091015
0x00090F39: cmp byte ptr [rax], 0x2c
0x00090F3C: je 0x140090f4d
0x00090F3E: sub rdi, rax
0x00090F41: dec rdi
0x00090F44: add rbx, rdi
0x00090F47: lea rdi, [rax + 1]
0x00090F4B: jmp 0x140090f14
0x00090F4D: lea rax, [rbp + 0x68]
0x00090F51: mov r8, qword ptr [rbp + 0x68]
0x00090F55: mov r9, qword ptr [rbp + 0x80]
0x00090F5C: cmp r9, 0x10
0x00090F60: cmovae rax, r8
0x00090F64: sub rcx, rax
0x00090F67: cmp rcx, -1
0x00090F6B: je 0x140091015
0x00090F71: lea rcx, [rbp + 0x68]
0x00090F75: cmp r9, 0x10
0x00090F79: cmovae rcx, r8
0x00090F7D: mov rdx, qword ptr [rbp + 0x78]
0x00090F81: add rdx, rcx
0x00090F84: lea rcx, [rbp + 0x68]
0x00090F88: cmp r9, 0x10
0x00090F8C: cmovae rcx, r8
0x00090F90: mov r9b, 0x2c
0x00090F93: lea r8, [rsp + 0x40]
0x00090F98: call 0x1400909c0
0x00090F9D: test al, al
0x00090F9F: jne 0x140090fae
0x00090FA1: lea rcx, [rbp + 0x88]
0x00090FA8: call 0x140093610
0x00090FAD: int3
0x00090FAE: mov rsi, r15
0x00090FB1: mov rbx, qword ptr [rsp + 0x40]
0x00090FB6: mov rax, qword ptr [rsp + 0x48]
0x00090FBB: mov rdi, rax
0x00090FBE: sub rdi, rbx
0x00090FC1: add rdi, 3
0x00090FC5: shr rdi, 2
0x00090FC9: cmp rbx, rax
0x00090FCC: cmova rdi, r15
0x00090FD0: test rdi, rdi
0x00090FD3: je 0x14009125b
0x00090FD9: mov r15d, dword ptr [rbp + 0x388]
0x00090FE0: mov r12d, dword ptr [rbp + 0x380]
0x00090FE7: nop word ptr [rax + rax]
0x00090FF0: mov r9d, r15d
0x00090FF3: mov r8d, r12d
0x00090FF6: mov edx, dword ptr [rbx]
0x00090FF8: lea rcx, [rbp + 0x88]
0x00090FFF: call 0x14008bce0
0x00091004: lea rbx, [rbx + 4]
0x00091008: inc rsi
0x0009100B: cmp rsi, rdi
0x0009100E: jne 0x140090ff0
0x00091010: jmp 0x14009124e
0x00091015: mov rbx, qword ptr [rbp + 0x78]
0x00091019: mov r15d, dword ptr [rbp + 0x388]
0x00091020: mov r12d, dword ptr [rbp + 0x380]
0x00091027: test r12d, r12d
0x0009102A: js 0x1400911f9
0x00091030: cmp r15d, 0xa
0x00091034: jge 0x1400911f9
0x0009103A: xor esi, esi
0x0009103C: test rbx, rbx
0x0009103F: je 0x14009124e
0x00091045: xor ecx, ecx
0x00091047: nop word ptr [rax + rax]
0x00091050: mov r9d, 1
0x00091056: mov r8, rcx
0x00091059: lea rdx, [rbp - 0x68]
0x0009105D: lea rcx, [rbp + 0x68]
0x00091061: call 0x1400575c0
0x00091066: mov r9d, r15d
0x00091069: mov r8d, r12d
0x0009106C: mov rdx, rax
0x0009106F: lea rcx, [rbp + 0x88]
0x00091076: call 0x14008eb60
0x0009107B: mov edi, eax
0x0009107D: mov dword ptr [rsp + 0x58], eax
0x00091081: lea rcx, [rsp + 0x58]
0x00091086: mov rbx, qword ptr [rsp + 0x40]
0x0009108B: mov rax, qword ptr [rsp + 0x48]
0x00091090: cmp rcx, rax
0x00091093: jae 0x140091140
0x00091099: lea rcx, [rsp + 0x58]
0x0009109E: cmp rbx, rcx
0x000910A1: ja 0x140091140
0x000910A7: lea rdi, [rsp + 0x58]
0x000910AC: sub rdi, rbx
0x000910AF: sar rdi, 2
0x000910B3: mov r9, qword ptr [rsp + 0x50]
0x000910B8: cmp rax, r9
0x000910BB: jne 0x14009112d
0x000910BD: mov rcx, r9
0x000910C0: sub rcx, rax
0x000910C3: sar rcx, 2
0x000910C7: cmp rcx, 1
0x000910CB: jae 0x14009112d
0x000910CD: sub rax, rbx
0x000910D0: sar rax, 2
0x000910D4: movabs r8, 0x3fffffffffffffff
0x000910DE: mov rcx, r8
0x000910E1: sub rcx, rax
0x000910E4: cmp rcx, 1
0x000910E8: jb 0x1400911df
0x000910EE: lea rdx, [rax + 1]
0x000910F2: sub r9, rbx
0x000910F5: sar r9, 2
0x000910F9: mov rax, r9
0x000910FC: shr rax, 1
0x000910FF: mov rcx, r8
0x00091102: sub rcx, rax
0x00091105: add rax, r9
0x00091108: xor r8d, r8d
0x0009110B: cmp rcx, r9
0x0009110E: cmovae r8, rax
0x00091112: cmp r8, rdx
0x00091115: cmovae rdx, r8
0x00091119: lea rcx, [rsp + 0x40]
0x0009111E: call 0x14008b600
0x00091123: mov rax, qword ptr [rsp + 0x48]
0x00091128: mov rbx, qword ptr [rsp + 0x40]
0x0009112D: lea rcx, [rbx + rdi*4]
0x00091131: test rax, rax
0x00091134: je 0x1400911c7
0x0009113A: mov ecx, dword ptr [rcx]
0x0009113C: mov dword ptr [rax], ecx
0x0009113E: jmp 0x1400911bd
0x00091140: mov r9, qword ptr [rsp + 0x50]
0x00091145: cmp rax, r9
0x00091148: jne 0x1400911b6
0x0009114A: mov rcx, r9
0x0009114D: sub rcx, rax
0x00091150: sar rcx, 2
0x00091154: cmp rcx, 1
0x00091158: jae 0x1400911b6
0x0009115A: sub rax, rbx
0x0009115D: sar rax, 2
0x00091161: movabs r8, 0x3fffffffffffffff
0x0009116B: mov rcx, r8
0x0009116E: sub rcx, rax
0x00091171: cmp rcx, 1
0x00091175: jb 0x1400911ec
0x00091177: lea rdx, [rax + 1]
0x0009117B: sub r9, rbx
0x0009117E: sar r9, 2
0x00091182: mov rax, r9
0x00091185: shr rax, 1
0x00091188: mov rcx, r8
0x0009118B: sub rcx, rax
0x0009118E: add rax, r9
0x00091191: xor r8d, r8d
0x00091194: cmp rcx, r9
0x00091197: cmovae r8, rax
0x0009119B: cmp r8, rdx
0x0009119E: cmovae rdx, r8
0x000911A2: lea rcx, [rsp + 0x40]
0x000911A7: call 0x14008b600
0x000911AC: mov rax, qword ptr [rsp + 0x48]
0x000911B1: mov rbx, qword ptr [rsp + 0x40]
0x000911B6: test rax, rax
0x000911B9: je 0x1400911c7
0x000911BB: mov dword ptr [rax], edi
0x000911BD: mov rax, qword ptr [rsp + 0x48]
0x000911C2: mov rbx, qword ptr [rsp + 0x40]
0x000911C7: add rax, 4
0x000911CB: mov qword ptr [rsp + 0x48], rax
0x000911D0: inc esi
0x000911D2: mov ecx, esi
0x000911D4: cmp rcx, qword ptr [rbp + 0x78]
0x000911D8: jae 0x140091258
0x000911DA: jmp 0x140091050
0x000911DF: lea rcx, [rip + 0x3a1632]
0x000911E6: call 0x140390a98
0x000911EB: int3
0x000911EC: lea rcx, [rip + 0x3a1625]
0x000911F3: call 0x140390a98
0x000911F8: int3
0x000911F9: mov qword ptr [rbp - 0x80], 0xf
0x00091201: mov qword ptr [rsp + 0x78], 0
0x0009120A: mov byte ptr [rsp + 0x68], 0
0x0009120F: or r9, 0xffffffffffffffff
0x00091213: xor r8d, r8d
0x00091216: lea rdx, [rbp + 0x68]
0x0009121A: lea rcx, [rsp + 0x68]
0x0009121F: call 0x1400354b0
0x00091224: mov r9d, r15d
0x00091227: mov r8d, r12d
0x0009122A: lea rdx, [rsp + 0x68]
0x0009122F: lea rcx, [rbp + 0x88]
0x00091236: call 0x14008eb60
0x0009123B: mov dword ptr [rsp + 0x60], eax
0x0009123F: lea rdx, [rsp + 0x60]
0x00091244: lea rcx, [rsp + 0x40]
0x00091249: call 0x140092d50
0x0009124E: mov rax, qword ptr [rsp + 0x48]
0x00091253: mov rbx, qword ptr [rsp + 0x40]
0x00091258: xor r15d, r15d
0x0009125B: sub rax, rbx
0x0009125E: sar rax, 2
0x00091262: cmp rax, 1
0x00091266: jne 0x140091347
0x0009126C: mov byte ptr [rbp + 0xd8], 0
0x00091273: mov qword ptr [rbp + 0xf8], 0xf
0x0009127E: mov qword ptr [rbp + 0xf0], r15
0x00091285: mov byte ptr [rbp + 0xe0], 0
0x0009128C: mov qword ptr [rbp + 0x140], r15
0x00091293: mov dword ptr [rbp + 0xd0], r15d
0x0009129A: mov dword ptr [rbp + 0xd4], 0x63
0x000912A4: mov eax, dword ptr [rbx]
0x000912A6: mov dword ptr [rbp + 0x100], eax
0x000912AC: mov dword ptr [rbp + 0x104], r15d
0x000912B3: lea r9, [rip + 0x3a7418]
0x000912BA: lea r8, [rip + 0x3a7410]
0x000912C1: mov rdx, r14
0x000912C4: lea rcx, [rbp + 0x1f0]
0x000912CB: call 0x1400889b0
0x000912D0: nop
0x000912D1: mov rdx, rax
0x000912D4: lea rcx, [rbp + 0x108]
0x000912DB: call 0x140087cc0
0x000912E0: nop
0x000912E1: mov rcx, qword ptr [rbp + 0x228]
0x000912E8: test rcx, rcx
0x000912EB: je 0x140091300
0x000912ED: mov rax, qword ptr [rcx]
0x000912F0: lea rdx, [rbp + 0x1f0]
0x000912F7: cmp rcx, rdx
0x000912FA: setne dl
0x000912FD: call qword ptr [rax + 0x20]
0x00091300: lea rdx, [rbp + 0xd0]
0x00091307: mov rcx, r13
0x0009130A: call 0x140092e70
0x0009130F: nop
0x00091310: mov rcx, qword ptr [rbp + 0x140]
0x00091317: test rcx, rcx
0x0009131A: je 0x140091336
0x0009131C: mov rax, qword ptr [rcx]
0x0009131F: lea rdx, [rbp + 0x108]
0x00091326: cmp rcx, rdx
0x00091329: setne dl
0x0009132C: call qword ptr [rax + 0x20]
0x0009132F: mov qword ptr [rbp + 0x140], r15
0x00091336: lea rcx, [rbp + 0xe0]
0x0009133D: call 0x140032ef0
0x00091342: jmp 0x14009144a
0x00091347: mov edi, r15d
0x0009134A: test rax, rax
0x0009134D: je 0x14009144a
0x00091353: mov rsi, r15
0x00091356: mov byte ptr [rbp + 0x158], 0
0x0009135D: mov qword ptr [rbp + 0x178], 0xf
0x00091368: mov qword ptr [rbp + 0x170], r15
0x0009136F: mov byte ptr [rbp + 0x160], 0
0x00091376: mov qword ptr [rbp + 0x1c0], r15
0x0009137D: mov dword ptr [rbp + 0x150], edi
0x00091383: mov dword ptr [rbp + 0x154], edi
0x00091389: mov eax, dword ptr [rbx + rsi]
0x0009138C: mov dword ptr [rbp + 0x180], eax
0x00091392: mov dword ptr [rbp + 0x184], r15d
0x00091399: lea r9, [rip + 0x3a7332]
0x000913A0: lea r8, [rip + 0x3a732a]
0x000913A7: mov rdx, r14
0x000913AA: lea rcx, [rbp + 0x240]
0x000913B1: call 0x1400889b0
0x000913B6: nop
0x000913B7: mov rdx, rax
0x000913BA: lea rcx, [rbp + 0x188]
0x000913C1: call 0x140087cc0
0x000913C6: nop
0x000913C7: mov rcx, qword ptr [rbp + 0x278]
0x000913CE: test rcx, rcx
0x000913D1: je 0x1400913e6
0x000913D3: mov rax, qword ptr [rcx]
0x000913D6: lea rdx, [rbp + 0x240]
0x000913DD: cmp rcx, rdx
0x000913E0: setne dl
0x000913E3: call qword ptr [rax + 0x20]
0x000913E6: lea rdx, [rbp + 0x150]
0x000913ED: mov rcx, r13
0x000913F0: call 0x140092e70
0x000913F5: nop
0x000913F6: mov rcx, qword ptr [rbp + 0x1c0]
0x000913FD: test rcx, rcx
0x00091400: je 0x14009141c
0x00091402: mov rax, qword ptr [rcx]
0x00091405: lea rdx, [rbp + 0x188]
0x0009140C: cmp rcx, rdx
0x0009140F: setne dl
0x00091412: call qword ptr [rax + 0x20]
0x00091415: mov qword ptr [rbp + 0x1c0], r15
0x0009141C: lea rcx, [rbp + 0x160]
0x00091423: call 0x140032ef0
0x00091428: inc edi
0x0009142A: add rsi, 4
0x0009142E: mov rcx, qword ptr [rsp + 0x48]
0x00091433: mov rbx, qword ptr [rsp + 0x40]
0x00091438: sub rcx, rbx
0x0009143B: sar rcx, 2
0x0009143F: mov eax, edi
0x00091441: cmp rax, rcx
0x00091444: jb 0x140091356
0x0009144A: lea rcx, [rbp + 0x68]
0x0009144E: call 0x140032ef0
0x00091453: nop
0x00091454: lea rcx, [rbp + 0x88]
0x0009145B: call 0x140032ef0
0x00091460: nop
0x00091461: mov rdx, qword ptr [rsp + 0x40]
0x00091466: test rdx, rdx
0x00091469: je 0x14009148f
0x0009146B: mov r8, qword ptr [rsp + 0x50]
0x00091470: sub r8, rdx
0x00091473: sar r8, 2
0x00091477: lea rcx, [rsp + 0x40]
0x0009147C: call 0x14006f4d0
0x00091481: xorps xmm0, xmm0
0x00091484: movdqu xmmword ptr [rsp + 0x40], xmm0
0x0009148A: mov qword ptr [rsp + 0x50], r15
0x0009148F: mov rcx, qword ptr [r14 + 0x38]
0x00091493: test rcx, rcx
0x00091496: je 0x1400914a8
0x00091498: mov rax, qword ptr [rcx]
0x0009149B: cmp rcx, r14
0x0009149E: setne dl
0x000914A1: call qword ptr [rax + 0x20]
0x000914A4: mov qword ptr [r14 + 0x38], r15
0x000914A8: mov rcx, qword ptr [rbp + 0x300]
0x000914AF: xor rcx, rsp
0x000914B2: call 0x1403b24c0
0x000914B7: add rsp, 0x418
0x000914BE: pop r15
0x000914C0: pop r14
0x000914C2: pop r13
0x000914C4: pop r12
0x000914C6: pop rdi
0x000914C7: pop rsi
0x000914C8: pop rbx
0x000914C9: pop rbp
0x000914CA: ret
```

## VMR descriptor vtable neighborhood

VMR descriptor vtable base inferred from `0xDD570`: `0x0043F0E8`

| slot | address | qword VA | RVA |
|---:|---|---|---|
| `-0x30` | `0x0043F0B8` | `0x00000001400E1870` | `0x000E1870` |
| `-0x28` | `0x0043F0C0` | `0x00000001400E0F00` | `0x000E0F00` |
| `-0x20` | `0x0043F0C8` | `0x00000001400E1C40` | `0x000E1C40` |
| `-0x18` | `0x0043F0D0` | `0x00000001400E0E40` | `0x000E0E40` |
| `-0x10` | `0x0043F0D8` | `0x0000000140068CE0` | `0x00068CE0` |
| `-0x8` | `0x0043F0E0` | `0x0000000140725E08` | `0x00725E08` |
| `+0x0` | `0x0043F0E8` | `0x00000001400E0AC0` | `0x000E0AC0` |
| `+0x8` | `0x0043F0F0` | `0x00000001400E0AC0` | `0x000E0AC0` |
| `+0x10` | `0x0043F0F8` | `0x00000001400E10C0` | `0x000E10C0` |
| `+0x18` | `0x0043F100` | `0x00000001400E1CF0` | `0x000E1CF0` |
| `+0x20` | `0x0043F108` | `0x00000001400E0E40` | `0x000E0E40` |
| `+0x28` | `0x0043F110` | `0x0000000140068CE0` | `0x00068CE0` |
| `+0x30` | `0x0043F118` | `0x0000000140725E88` | `0x00725E88` |
| `+0x38` | `0x0043F120` | `0x00000001400E18F0` | `0x000E18F0` |
| `+0x40` | `0x0043F128` | `0x00000001400E18F0` | `0x000E18F0` |
| `+0x48` | `0x0043F130` | `0x00000001400E1180` | `0x000E1180` |
| `+0x50` | `0x0043F138` | `0x00000001400E1D40` | `0x000E1D40` |
| `+0x58` | `0x0043F140` | `0x00000001400E0E40` | `0x000E0E40` |
| `+0x60` | `0x0043F148` | `0x0000000140068CE0` | `0x00068CE0` |
| `+0x68` | `0x0043F150` | `0x0000000140725F08` | `0x00725F08` |
| `+0x70` | `0x0043F158` | `0x00000001400E0D20` | `0x000E0D20` |
| `+0x78` | `0x0043F160` | `0x00000001400E0D20` | `0x000E0D20` |
| `+0x80` | `0x0043F168` | `0x00000001400E1630` | `0x000E1630` |

## Candidate vtable code targets

### slot +0x0 -> `0x000E0AC0`

```asm
0x000E0AC0: test rdx, rdx
0x000E0AC3: je 0x1400e0ad7
0x000E0AC5: lea rax, [rip + 0x35e61c]
0x000E0ACC: mov qword ptr [rdx], rax
0x000E0ACF: mov rax, qword ptr [rcx + 8]
0x000E0AD3: mov qword ptr [rdx + 8], rax
0x000E0AD7: mov rax, rdx
0x000E0ADA: ret
0x000E0ADB: int3
0x000E0ADC: int3
0x000E0ADD: int3
0x000E0ADE: int3
0x000E0ADF: int3
0x000E0AE0: test rdx, rdx
0x000E0AE3: je 0x1400e0af7
0x000E0AE5: lea rax, [rip + 0x35e12c]
0x000E0AEC: mov qword ptr [rdx], rax
0x000E0AEF: mov rax, qword ptr [rcx + 8]
0x000E0AF3: mov qword ptr [rdx + 8], rax
0x000E0AF7: mov rax, rdx
0x000E0AFA: ret
0x000E0AFB: int3
0x000E0AFC: int3
0x000E0AFD: int3
0x000E0AFE: int3
0x000E0AFF: int3
0x000E0B00: test rdx, rdx
0x000E0B03: je 0x1400e0b17
0x000E0B05: lea rax, [rip + 0x35e454]
0x000E0B0C: mov qword ptr [rdx], rax
0x000E0B0F: mov rax, qword ptr [rcx + 8]
0x000E0B13: mov qword ptr [rdx + 8], rax
0x000E0B17: mov rax, rdx
0x000E0B1A: ret
0x000E0B1B: int3
0x000E0B1C: int3
0x000E0B1D: int3
0x000E0B1E: int3
0x000E0B1F: int3
0x000E0B20: test rdx, rdx
0x000E0B23: je 0x1400e0b37
0x000E0B25: lea rax, [rip + 0x35e7b4]
0x000E0B2C: mov qword ptr [rdx], rax
0x000E0B2F: mov rax, qword ptr [rcx + 8]
0x000E0B33: mov qword ptr [rdx + 8], rax
0x000E0B37: mov rax, rdx
0x000E0B3A: ret
0x000E0B3B: int3
0x000E0B3C: int3
0x000E0B3D: int3
0x000E0B3E: int3
0x000E0B3F: int3
0x000E0B40: test rdx, rdx
0x000E0B43: je 0x1400e0b57
0x000E0B45: lea rax, [rip + 0x35e1ac]
0x000E0B4C: mov qword ptr [rdx], rax
0x000E0B4F: mov rax, qword ptr [rcx + 8]
0x000E0B53: mov qword ptr [rdx + 8], rax
0x000E0B57: mov rax, rdx
0x000E0B5A: ret
0x000E0B5B: int3
0x000E0B5C: int3
0x000E0B5D: int3
0x000E0B5E: int3
0x000E0B5F: int3
0x000E0B60: test rdx, rdx
0x000E0B63: je 0x1400e0b77
0x000E0B65: lea rax, [rip + 0x35de44]
0x000E0B6C: mov qword ptr [rdx], rax
0x000E0B6F: mov rax, qword ptr [rcx + 8]
0x000E0B73: mov qword ptr [rdx + 8], rax
0x000E0B77: mov rax, rdx
0x000E0B7A: ret
0x000E0B7B: int3
0x000E0B7C: int3
0x000E0B7D: int3
0x000E0B7E: int3
0x000E0B7F: int3
0x000E0B80: test rdx, rdx
0x000E0B83: je 0x1400e0b97
0x000E0B85: lea rax, [rip + 0x35e364]
0x000E0B8C: mov qword ptr [rdx], rax
0x000E0B8F: mov rax, qword ptr [rcx + 8]
0x000E0B93: mov qword ptr [rdx + 8], rax
0x000E0B97: mov rax, rdx
0x000E0B9A: ret
0x000E0B9B: int3
0x000E0B9C: int3
0x000E0B9D: int3
0x000E0B9E: int3
0x000E0B9F: int3
0x000E0BA0: test rdx, rdx
0x000E0BA3: je 0x1400e0bb7
0x000E0BA5: lea rax, [rip + 0x35e5e4]
0x000E0BAC: mov qword ptr [rdx], rax
0x000E0BAF: mov rax, qword ptr [rcx + 8]
0x000E0BB3: mov qword ptr [rdx + 8], rax
0x000E0BB7: mov rax, rdx
0x000E0BBA: ret
0x000E0BBB: int3
0x000E0BBC: int3
0x000E0BBD: int3
0x000E0BBE: int3
0x000E0BBF: int3
```

### slot +0x10 -> `0x000E10C0`

```asm
0x000E10C0: movsxd rax, dword ptr [rdx]
0x000E10C3: imul rdx, rax, 0xd8
0x000E10CA: mov rax, qword ptr [rcx + 8]
0x000E10CE: mov rcx, qword ptr [rax + 0x2c0]
0x000E10D5: mov eax, dword ptr [r8]
0x000E10D8: mov dword ptr [rdx + rcx + 0xb0], eax
0x000E10DF: ret
0x000E10E0: movsxd rax, dword ptr [rdx]
0x000E10E3: imul rdx, rax, 0xd8
0x000E10EA: mov rax, qword ptr [rcx + 8]
0x000E10EE: mov rcx, qword ptr [rax + 0x2c0]
0x000E10F5: mov eax, dword ptr [r8]
0x000E10F8: mov dword ptr [rdx + rcx + 0x84], eax
0x000E10FF: ret
0x000E1100: movsxd rax, dword ptr [rdx]
0x000E1103: cmp dword ptr [r8], 0
0x000E1107: setne r8b
0x000E110B: imul rdx, rax, 0xd8
0x000E1112: mov rax, qword ptr [rcx + 8]
0x000E1116: mov rcx, qword ptr [rax + 0x2c0]
0x000E111D: mov byte ptr [rdx + rcx + 0x19], r8b
0x000E1122: ret
0x000E1123: int3
0x000E1124: int3
0x000E1125: int3
0x000E1126: int3
0x000E1127: int3
0x000E1128: int3
0x000E1129: int3
0x000E112A: int3
0x000E112B: int3
0x000E112C: int3
0x000E112D: int3
0x000E112E: int3
0x000E112F: int3
0x000E1130: mov r9d, dword ptr [r8]
0x000E1133: xor eax, eax
0x000E1135: cmp r9d, 0x64
0x000E1139: cmove r9d, eax
0x000E113D: movsxd rax, dword ptr [rdx]
0x000E1140: imul rdx, rax, 0xd8
0x000E1147: mov rax, qword ptr [rcx + 8]
0x000E114B: mov rcx, qword ptr [rax + 0x2c0]
0x000E1152: mov dword ptr [rdx + rcx + 4], r9d
0x000E1157: ret
0x000E1158: int3
0x000E1159: int3
0x000E115A: int3
0x000E115B: int3
0x000E115C: int3
0x000E115D: int3
0x000E115E: int3
0x000E115F: int3
0x000E1160: movsxd rax, dword ptr [rdx]
0x000E1163: imul rdx, rax, 0xd8
0x000E116A: mov rax, qword ptr [rcx + 8]
0x000E116E: mov rcx, qword ptr [rax + 0x2c0]
0x000E1175: mov eax, dword ptr [r8]
0x000E1178: mov dword ptr [rdx + rcx + 0x7c], eax
0x000E117C: ret
0x000E117D: int3
0x000E117E: int3
0x000E117F: int3
0x000E1180: movsxd rax, dword ptr [rdx]
0x000E1183: mov r9d, dword ptr [r8]
0x000E1186: imul rdx, rax, 0xd8
0x000E118D: mov rax, qword ptr [rcx + 8]
0x000E1191: neg r9d
0x000E1194: mov rcx, qword ptr [rax + 0x2c0]
0x000E119B: mov dword ptr [rdx + rcx + 0xb0], r9d
0x000E11A3: ret
0x000E11A4: int3
0x000E11A5: int3
0x000E11A6: int3
0x000E11A7: int3
0x000E11A8: int3
0x000E11A9: int3
0x000E11AA: int3
0x000E11AB: int3
0x000E11AC: int3
0x000E11AD: int3
0x000E11AE: int3
0x000E11AF: int3
0x000E11B0: mov r9d, dword ptr [r8]
0x000E11B3: mov r10, rcx
0x000E11B6: movsxd rax, dword ptr [rdx]
0x000E11B9: cmp r9d, 0x28
0x000E11BD: jl 0x1400e11d7
```

### slot +0x18 -> `0x000E1CF0`

```asm
0x000E1CF0: lea rax, [rip + 0x6fd6d9]
0x000E1CF7: ret
0x000E1CF8: int3
0x000E1CF9: int3
0x000E1CFA: int3
0x000E1CFB: int3
0x000E1CFC: int3
0x000E1CFD: int3
0x000E1CFE: int3
0x000E1CFF: int3
0x000E1D00: lea rax, [rip + 0x6fd7c9]
0x000E1D07: ret
0x000E1D08: int3
0x000E1D09: int3
0x000E1D0A: int3
0x000E1D0B: int3
0x000E1D0C: int3
0x000E1D0D: int3
0x000E1D0E: int3
0x000E1D0F: int3
0x000E1D10: lea rax, [rip + 0x6fdc39]
0x000E1D17: ret
0x000E1D18: int3
0x000E1D19: int3
0x000E1D1A: int3
0x000E1D1B: int3
0x000E1D1C: int3
0x000E1D1D: int3
0x000E1D1E: int3
0x000E1D1F: int3
0x000E1D20: lea rax, [rip + 0x6fd869]
0x000E1D27: ret
0x000E1D28: int3
0x000E1D29: int3
0x000E1D2A: int3
0x000E1D2B: int3
0x000E1D2C: int3
0x000E1D2D: int3
0x000E1D2E: int3
0x000E1D2F: int3
0x000E1D30: lea rax, [rip + 0x6fd459]
0x000E1D37: ret
0x000E1D38: int3
0x000E1D39: int3
0x000E1D3A: int3
0x000E1D3B: int3
0x000E1D3C: int3
0x000E1D3D: int3
0x000E1D3E: int3
0x000E1D3F: int3
0x000E1D40: lea rax, [rip + 0x6fd649]
0x000E1D47: ret
0x000E1D48: int3
0x000E1D49: int3
0x000E1D4A: int3
0x000E1D4B: int3
0x000E1D4C: int3
0x000E1D4D: int3
0x000E1D4E: int3
0x000E1D4F: int3
0x000E1D50: lea rax, [rip + 0x6fdaf9]
0x000E1D57: ret
0x000E1D58: int3
0x000E1D59: int3
0x000E1D5A: int3
0x000E1D5B: int3
0x000E1D5C: int3
0x000E1D5D: int3
0x000E1D5E: int3
0x000E1D5F: int3
0x000E1D60: lea rax, [rip + 0x6fdea9]
0x000E1D67: ret
0x000E1D68: int3
0x000E1D69: int3
0x000E1D6A: int3
0x000E1D6B: int3
0x000E1D6C: int3
0x000E1D6D: int3
0x000E1D6E: int3
0x000E1D6F: int3
0x000E1D70: lea rax, [rip + 0x6fd7d9]
0x000E1D77: ret
0x000E1D78: int3
0x000E1D79: int3
0x000E1D7A: int3
0x000E1D7B: int3
0x000E1D7C: int3
0x000E1D7D: int3
0x000E1D7E: int3
0x000E1D7F: int3
0x000E1D80: lea rax, [rip + 0x6fd889]
0x000E1D87: ret
0x000E1D88: int3
0x000E1D89: int3
0x000E1D8A: int3
0x000E1D8B: int3
0x000E1D8C: int3
0x000E1D8D: int3
0x000E1D8E: int3
0x000E1D8F: int3
0x000E1D90: lea rax, [rip + 0x6fdc39]
0x000E1D97: ret
0x000E1D98: int3
0x000E1D99: int3
0x000E1D9A: int3
0x000E1D9B: int3
0x000E1D9C: int3
0x000E1D9D: int3
0x000E1D9E: int3
0x000E1D9F: int3
0x000E1DA0: lea rax, [rip + 0x6fd569]
0x000E1DA7: ret
0x000E1DA8: int3
0x000E1DA9: int3
0x000E1DAA: int3
0x000E1DAB: int3
0x000E1DAC: int3
0x000E1DAD: int3
0x000E1DAE: int3
0x000E1DAF: int3
0x000E1DB0: lea rax, [rip + 0x6fdad9]
0x000E1DB7: ret
0x000E1DB8: int3
0x000E1DB9: int3
0x000E1DBA: int3
0x000E1DBB: int3
0x000E1DBC: int3
0x000E1DBD: int3
0x000E1DBE: int3
0x000E1DBF: int3
0x000E1DC0: lea rax, [rip + 0x6fdd49]
0x000E1DC7: ret
0x000E1DC8: int3
0x000E1DC9: int3
0x000E1DCA: int3
0x000E1DCB: int3
0x000E1DCC: int3
0x000E1DCD: int3
0x000E1DCE: int3
0x000E1DCF: int3
0x000E1DD0: lea rax, [rip + 0x6fd9f9]
0x000E1DD7: ret
0x000E1DD8: int3
0x000E1DD9: int3
0x000E1DDA: int3
0x000E1DDB: int3
0x000E1DDC: int3
0x000E1DDD: int3
0x000E1DDE: int3
0x000E1DDF: int3
0x000E1DE0: lea rax, [rip + 0x6fdb29]
0x000E1DE7: ret
0x000E1DE8: int3
0x000E1DE9: int3
0x000E1DEA: int3
0x000E1DEB: int3
0x000E1DEC: int3
0x000E1DED: int3
0x000E1DEE: int3
0x000E1DEF: int3
```

### slot +0x20 -> `0x000E0E40`

```asm
0x000E0E40: lea rax, [rip + 0x35da19]
0x000E0E47: mov qword ptr [rcx], rax
0x000E0E4A: test dl, dl
0x000E0E4C: jne 0x1403b20d4
0x000E0E52: ret
0x000E0E53: int3
0x000E0E54: int3
0x000E0E55: int3
0x000E0E56: int3
0x000E0E57: int3
0x000E0E58: int3
0x000E0E59: int3
0x000E0E5A: int3
0x000E0E5B: int3
0x000E0E5C: int3
0x000E0E5D: int3
0x000E0E5E: int3
0x000E0E5F: int3
0x000E0E60: lea rax, [rip + 0x35da31]
0x000E0E67: mov qword ptr [rcx], rax
0x000E0E6A: test dl, dl
0x000E0E6C: jne 0x1403b20d4
0x000E0E72: ret
0x000E0E73: int3
0x000E0E74: int3
0x000E0E75: int3
0x000E0E76: int3
0x000E0E77: int3
0x000E0E78: int3
0x000E0E79: int3
0x000E0E7A: int3
0x000E0E7B: int3
0x000E0E7C: int3
0x000E0E7D: int3
0x000E0E7E: int3
0x000E0E7F: int3
0x000E0E80: lea rax, [rip + 0x3585b1]
0x000E0E87: mov qword ptr [rcx], rax
0x000E0E8A: test dl, dl
0x000E0E8C: jne 0x1403b20d4
0x000E0E92: ret
0x000E0E93: int3
0x000E0E94: int3
0x000E0E95: int3
0x000E0E96: int3
0x000E0E97: int3
0x000E0E98: int3
0x000E0E99: int3
0x000E0E9A: int3
0x000E0E9B: int3
0x000E0E9C: int3
0x000E0E9D: int3
0x000E0E9E: int3
0x000E0E9F: int3
0x000E0EA0: cmp rcx, rdx
0x000E0EA3: je 0x1400e0ef0
0x000E0EA5: mov qword ptr [rsp + 0x10], rbx
0x000E0EAA: push rdi
0x000E0EAB: sub rsp, 0x20
0x000E0EAF: mov qword ptr [rsp + 0x30], rsi
0x000E0EB4: mov rdi, rdx
0x000E0EB7: xor esi, esi
0x000E0EB9: mov rbx, rcx
0x000E0EBC: nop dword ptr [rax]
0x000E0EC0: test rbx, rbx
0x000E0EC3: je 0x1400e0ee1
0x000E0EC5: lea rax, [rbx + 0x10]
0x000E0EC9: mov rcx, rbx
0x000E0ECC: mov rbx, qword ptr [rax]
0x000E0ECF: mov edx, 1
0x000E0ED4: mov qword ptr [rax], rsi
0x000E0ED7: mov rax, qword ptr [rcx]
0x000E0EDA: call qword ptr [rax]
0x000E0EDC: cmp rbx, rdi
0x000E0EDF: jne 0x1400e0ec0
0x000E0EE1: mov rsi, qword ptr [rsp + 0x30]
0x000E0EE6: mov rbx, qword ptr [rsp + 0x38]
0x000E0EEB: add rsp, 0x20
0x000E0EEF: pop rdi
0x000E0EF0: ret
0x000E0EF1: int3
0x000E0EF2: int3
0x000E0EF3: int3
0x000E0EF4: int3
0x000E0EF5: int3
0x000E0EF6: int3
0x000E0EF7: int3
0x000E0EF8: int3
0x000E0EF9: int3
0x000E0EFA: int3
0x000E0EFB: int3
0x000E0EFC: int3
0x000E0EFD: int3
0x000E0EFE: int3
0x000E0EFF: int3
0x000E0F00: movsxd rax, dword ptr [rdx]
0x000E0F03: imul rdx, rax, 0xd8
0x000E0F0A: mov rax, qword ptr [rcx + 8]
0x000E0F0E: mov rcx, qword ptr [rax + 0x2c0]
0x000E0F15: mov eax, dword ptr [r8]
0x000E0F18: mov dword ptr [rdx + rcx + 0xac], eax
0x000E0F1F: ret
0x000E0F20: movsxd rax, dword ptr [rdx]
0x000E0F23: cmp dword ptr [r8], 0
0x000E0F27: setne r8b
0x000E0F2B: imul rdx, rax, 0xd8
0x000E0F32: mov rax, qword ptr [rcx + 8]
0x000E0F36: mov rcx, qword ptr [rax + 0x2c0]
```

### slot +0x28 -> `0x00068CE0`

```asm
0x00068CE0: lea rax, [rcx + 8]
0x00068CE4: ret
0x00068CE5: int3
0x00068CE6: int3
0x00068CE7: int3
0x00068CE8: int3
0x00068CE9: int3
0x00068CEA: int3
0x00068CEB: int3
0x00068CEC: int3
0x00068CED: int3
0x00068CEE: int3
0x00068CEF: int3
0x00068CF0: mov qword ptr [rsp + 0x18], rbx
0x00068CF5: push rsi
0x00068CF6: push rdi
0x00068CF7: push r14
0x00068CF9: sub rsp, 0x30
0x00068CFD: mov rax, qword ptr [rcx + 0x28]
0x00068D01: lea rdi, [rdx + rdx]
0x00068D05: sub rax, qword ptr [rcx + 0x18]
0x00068D09: mov r14, rdx
0x00068D0C: sar rax, 3
0x00068D10: mov rsi, rcx
0x00068D13: cmp rax, rdi
0x00068D16: jae 0x140068d33
0x00068D18: movabs rax, 0x1fffffffffffffff
0x00068D22: cmp rdi, rax
0x00068D25: ja 0x140068d7d
0x00068D27: mov rdx, rdi
0x00068D2A: add rcx, 0x18
0x00068D2E: call 0x140069e40
0x00068D33: mov rax, qword ptr [rsi + 8]
0x00068D37: lea rdx, [rsp + 0x58]
0x00068D3C: mov qword ptr [rsp + 0x50], rax
0x00068D41: lea rcx, [rsi + 0x18]
0x00068D45: mov rax, qword ptr [rsi + 0x18]
0x00068D49: mov r9, rdi
0x00068D4C: mov qword ptr [rsi + 0x20], rax
0x00068D50: lea rax, [rsp + 0x50]
0x00068D55: mov r8, qword ptr [rsi + 0x18]
0x00068D59: mov qword ptr [rsp + 0x20], rax
0x00068D5E: call 0x140069300
0x00068D63: mov rbx, qword ptr [rsp + 0x60]
0x00068D68: lea rax, [r14 - 1]
0x00068D6C: mov qword ptr [rsi + 0x30], rax
0x00068D70: mov qword ptr [rsi + 0x38], r14
0x00068D74: add rsp, 0x30
0x00068D78: pop r14
0x00068D7A: pop rdi
0x00068D7B: pop rsi
0x00068D7C: ret
0x00068D7D: lea rcx, [rip + 0x3c9a94]
0x00068D84: call 0x140390a98
0x00068D89: int3
0x00068D8A: int3
0x00068D8B: int3
0x00068D8C: int3
0x00068D8D: int3
0x00068D8E: int3
0x00068D8F: int3
0x00068D90: mov qword ptr [rsp + 0x18], rbx
0x00068D95: push rsi
0x00068D96: push rdi
0x00068D97: push r14
0x00068D99: sub rsp, 0x30
0x00068D9D: mov rax, qword ptr [rcx + 0x28]
0x00068DA1: lea rdi, [rdx + rdx]
0x00068DA5: sub rax, qword ptr [rcx + 0x18]
0x00068DA9: mov r14, rdx
0x00068DAC: sar rax, 3
0x00068DB0: mov rsi, rcx
0x00068DB3: cmp rax, rdi
0x00068DB6: jae 0x140068dd3
0x00068DB8: movabs rax, 0x1fffffffffffffff
0x00068DC2: cmp rdi, rax
0x00068DC5: ja 0x140068e1d
0x00068DC7: mov rdx, rdi
0x00068DCA: add rcx, 0x18
0x00068DCE: call 0x140069ef0
0x00068DD3: mov rax, qword ptr [rsi + 8]
0x00068DD7: lea rdx, [rsp + 0x58]
```

### slot +0x30 -> `0x00725E88`

```asm
0x00725E88: add dword ptr [rax], eax
0x00725E8A: add byte ptr [rax], al
0x00725E8C: add byte ptr [rax], al
0x00725E8E: add byte ptr [rax], al
0x00725E90: add byte ptr [rax], al
0x00725E92: add byte ptr [rax], al
0x00725E94: ror byte ptr [rsi], 0x7e
0x00725E97: add byte ptr [rax - 0x77ff8da2], dh
0x00725E9D: pop rsi
0x00725E9E: jb 0x140725ea0
0x00725EA0: add byte ptr [rax], al
0x00725EA2: add byte ptr [rax], al
0x00725EA4: add byte ptr [rax], al
0x00725EA6: add byte ptr [rax], al
0x00725EA8: add byte ptr [rax], al
0x00725EAA: add byte ptr [rax], al
0x00725EAC: add byte ptr [rax], al
0x00725EAE: add byte ptr [rax], al
0x00725EB0: add byte ptr [rax], al
0x00725EB2: add byte ptr [rax], al
0x00725EB4: add byte ptr [rax], al
0x00725EB6: add byte ptr [rax], al
0x00725EB8: add al, byte ptr [rax]
0x00725EBA: add byte ptr [rax], al
0x00725EBC: enter 0x725e, 0
0x00725EC0: add byte ptr [rax], al
0x00725EC2: add byte ptr [rax], al
0x00725EC4: add byte ptr [rax], al
0x00725EC6: add byte ptr [rax], al
0x00725EC8: loopne 0x140725f28
0x00725ECA: jb 0x140725ecc
```

### slot +0x38 -> `0x000E18F0`

```asm
0x000E18F0: test rdx, rdx
0x000E18F3: je 0x1400e1907
0x000E18F5: lea rax, [rip + 0x35d824]
0x000E18FC: mov qword ptr [rdx], rax
0x000E18FF: mov rax, qword ptr [rcx + 8]
0x000E1903: mov qword ptr [rdx + 8], rax
0x000E1907: mov rax, rdx
0x000E190A: ret
0x000E190B: int3
0x000E190C: int3
0x000E190D: int3
0x000E190E: int3
0x000E190F: int3
0x000E1910: test rdx, rdx
0x000E1913: je 0x1400e1927
0x000E1915: lea rax, [rip + 0x35d67c]
0x000E191C: mov qword ptr [rdx], rax
0x000E191F: mov rax, qword ptr [rcx + 8]
0x000E1923: mov qword ptr [rdx + 8], rax
0x000E1927: mov rax, rdx
0x000E192A: ret
0x000E192B: int3
0x000E192C: int3
0x000E192D: int3
0x000E192E: int3
0x000E192F: int3
0x000E1930: test rdx, rdx
0x000E1933: je 0x1400e1947
0x000E1935: lea rax, [rip + 0x35d26c]
0x000E193C: mov qword ptr [rdx], rax
0x000E193F: mov rax, qword ptr [rcx + 8]
0x000E1943: mov qword ptr [rdx + 8], rax
0x000E1947: mov rax, rdx
0x000E194A: ret
0x000E194B: int3
0x000E194C: int3
0x000E194D: int3
0x000E194E: int3
0x000E194F: int3
0x000E1950: test rdx, rdx
0x000E1953: je 0x1400e1967
0x000E1955: lea rax, [rip + 0x35d134]
0x000E195C: mov qword ptr [rdx], rax
0x000E195F: mov rax, qword ptr [rcx + 8]
0x000E1963: mov qword ptr [rdx + 8], rax
0x000E1967: mov rax, rdx
0x000E196A: ret
0x000E196B: int3
0x000E196C: int3
0x000E196D: int3
0x000E196E: int3
0x000E196F: int3
0x000E1970: test rdx, rdx
0x000E1973: je 0x1400e1987
0x000E1975: lea rax, [rip + 0x35d3ec]
0x000E197C: mov qword ptr [rdx], rax
0x000E197F: mov rax, qword ptr [rcx + 8]
0x000E1983: mov qword ptr [rdx + 8], rax
0x000E1987: mov rax, rdx
0x000E198A: ret
0x000E198B: int3
0x000E198C: int3
0x000E198D: int3
0x000E198E: int3
0x000E198F: int3
0x000E1990: test rdx, rdx
0x000E1993: je 0x1400e19a7
0x000E1995: lea rax, [rip + 0x35d4ac]
0x000E199C: mov qword ptr [rdx], rax
0x000E199F: mov rax, qword ptr [rcx + 8]
0x000E19A3: mov qword ptr [rdx + 8], rax
0x000E19A7: mov rax, rdx
0x000E19AA: ret
0x000E19AB: int3
0x000E19AC: int3
0x000E19AD: int3
0x000E19AE: int3
0x000E19AF: int3
0x000E19B0: test rdx, rdx
0x000E19B3: je 0x1400e19c7
0x000E19B5: lea rax, [rip + 0x35d144]
0x000E19BC: mov qword ptr [rdx], rax
0x000E19BF: mov rax, qword ptr [rcx + 8]
0x000E19C3: mov qword ptr [rdx + 8], rax
0x000E19C7: mov rax, rdx
0x000E19CA: ret
0x000E19CB: int3
0x000E19CC: int3
0x000E19CD: int3
0x000E19CE: int3
0x000E19CF: int3
0x000E19D0: test rdx, rdx
0x000E19D3: je 0x1400e19e7
0x000E19D5: lea rax, [rip + 0x35d4a4]
0x000E19DC: mov qword ptr [rdx], rax
0x000E19DF: mov rax, qword ptr [rcx + 8]
0x000E19E3: mov qword ptr [rdx + 8], rax
0x000E19E7: mov rax, rdx
0x000E19EA: ret
0x000E19EB: int3
0x000E19EC: int3
0x000E19ED: int3
0x000E19EE: int3
0x000E19EF: int3
```
