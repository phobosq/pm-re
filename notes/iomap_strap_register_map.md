# IOMap strap register map

Primitives: `0x1C1E40(ECX,DX)->EAX` read; `0x1C1ED0(ECX,EDX,R8W)->bool` write.

## Read/current-state builder `0x001C5120..0x001C52DA`

| call | arg setup window | post-call/store |
|---|---|---|
| `0x001C5186` | `je 0x1401c51b5; cmp ecx, 1; jne 0x1401c549f; xor ebp, ebp; mov ebx, 0x50200; nop word ptr [rax + rax]; movzx edx, word ptr [rsi + 0x38]; mov ecx, ebx` | `mov dword ptr [rdi + rbp*4], eax; add ebx, 4; inc rbp; cmp rbp, 0x19` |
| `0x001C51BE` | `cmp byte ptr [rdi + 4], 0xff; jne 0x1401c549f; cmp byte ptr [rdi + 5], 0xff; jne 0x1401c549f; xor al, al; jmp 0x1401c54ec; movzx edx, word ptr [rsi + 0x38]; mov ecx, 0x28ec` | `mov dword ptr [rdi + 0xc8], eax; mov ecx, 0x28f4; movzx edx, word ptr [rsi + 0x38]; call 0x1401c1e40` |
| `0x001C51D2` | `xor al, al; jmp 0x1401c54ec; movzx edx, word ptr [rsi + 0x38]; mov ecx, 0x28ec; call 0x1401c1e40; mov dword ptr [rdi + 0xc8], eax; mov ecx, 0x28f4; movzx edx, word ptr [rsi + 0x38]` | `mov dword ptr [rdi + 0xcc], eax; mov ecx, 0x28fc; movzx edx, word ptr [rsi + 0x38]; call 0x1401c1e40` |
| `0x001C51E6` | `call 0x1401c1e40; mov dword ptr [rdi + 0xc8], eax; mov ecx, 0x28f4; movzx edx, word ptr [rsi + 0x38]; call 0x1401c1e40; mov dword ptr [rdi + 0xcc], eax; mov ecx, 0x28fc; movzx edx, word ptr [rsi + 0x38]` | `mov dword ptr [rdi + 0x114], eax; mov ecx, 0x2904; movzx edx, word ptr [rsi + 0x38]; call 0x1401c1e40` |
| `0x001C51FA` | `call 0x1401c1e40; mov dword ptr [rdi + 0xcc], eax; mov ecx, 0x28fc; movzx edx, word ptr [rsi + 0x38]; call 0x1401c1e40; mov dword ptr [rdi + 0x114], eax; mov ecx, 0x2904; movzx edx, word ptr [rsi + 0x38]` | `mov dword ptr [rdi + 0x118], eax; mov ecx, 0x28c4; movzx edx, word ptr [rsi + 0x38]; call 0x1401c1e40` |
| `0x001C520E` | `call 0x1401c1e40; mov dword ptr [rdi + 0x114], eax; mov ecx, 0x2904; movzx edx, word ptr [rsi + 0x38]; call 0x1401c1e40; mov dword ptr [rdi + 0x118], eax; mov ecx, 0x28c4; movzx edx, word ptr [rsi + 0x38]` | `mov dword ptr [rdi + 0xd0], eax; mov ecx, 0x28a4; movzx edx, word ptr [rsi + 0x38]; call 0x1401c1e40` |
| `0x001C5222` | `call 0x1401c1e40; mov dword ptr [rdi + 0x118], eax; mov ecx, 0x28c4; movzx edx, word ptr [rsi + 0x38]; call 0x1401c1e40; mov dword ptr [rdi + 0xd0], eax; mov ecx, 0x28a4; movzx edx, word ptr [rsi + 0x38]` | `mov dword ptr [rdi + 0xd4], eax; mov ecx, 0x28ac; movzx edx, word ptr [rsi + 0x38]; call 0x1401c1e40` |
| `0x001C5236` | `call 0x1401c1e40; mov dword ptr [rdi + 0xd0], eax; mov ecx, 0x28a4; movzx edx, word ptr [rsi + 0x38]; call 0x1401c1e40; mov dword ptr [rdi + 0xd4], eax; mov ecx, 0x28ac; movzx edx, word ptr [rsi + 0x38]` | `mov dword ptr [rdi + 0xd8], eax; mov ecx, 0x28b4; movzx edx, word ptr [rsi + 0x38]; call 0x1401c1e40` |
| `0x001C524A` | `call 0x1401c1e40; mov dword ptr [rdi + 0xd4], eax; mov ecx, 0x28ac; movzx edx, word ptr [rsi + 0x38]; call 0x1401c1e40; mov dword ptr [rdi + 0xd8], eax; mov ecx, 0x28b4; movzx edx, word ptr [rsi + 0x38]` | `mov dword ptr [rdi + 0xdc], eax; mov ecx, 0x28bc; movzx edx, word ptr [rsi + 0x38]; call 0x1401c1e40` |
| `0x001C525E` | `call 0x1401c1e40; mov dword ptr [rdi + 0xd8], eax; mov ecx, 0x28b4; movzx edx, word ptr [rsi + 0x38]; call 0x1401c1e40; mov dword ptr [rdi + 0xdc], eax; mov ecx, 0x28bc; movzx edx, word ptr [rsi + 0x38]` | `mov dword ptr [rdi + 0xe0], eax; mov ecx, 0x29c8; movzx edx, word ptr [rsi + 0x38]; call 0x1401c1e40` |
| `0x001C5272` | `call 0x1401c1e40; mov dword ptr [rdi + 0xdc], eax; mov ecx, 0x28bc; movzx edx, word ptr [rsi + 0x38]; call 0x1401c1e40; mov dword ptr [rdi + 0xe0], eax; mov ecx, 0x29c8; movzx edx, word ptr [rsi + 0x38]` | `mov dword ptr [rdi + 0xe4], eax; mov ecx, 0x27b0; movzx edx, word ptr [rsi + 0x38]; call 0x1401c1e40` |
| `0x001C5286` | `call 0x1401c1e40; mov dword ptr [rdi + 0xe0], eax; mov ecx, 0x29c8; movzx edx, word ptr [rsi + 0x38]; call 0x1401c1e40; mov dword ptr [rdi + 0xe4], eax; mov ecx, 0x27b0; movzx edx, word ptr [rsi + 0x38]` | `mov dword ptr [rdi + 0x104], eax; mov ecx, 0x27b0; movzx edx, word ptr [rsi + 0x38]; call 0x1401c1e40` |
| `0x001C529A` | `call 0x1401c1e40; mov dword ptr [rdi + 0xe4], eax; mov ecx, 0x27b0; movzx edx, word ptr [rsi + 0x38]; call 0x1401c1e40; mov dword ptr [rdi + 0x104], eax; mov ecx, 0x27b0; movzx edx, word ptr [rsi + 0x38]` | `mov dword ptr [rdi + 0x10c], eax; mov ecx, 0x2acc; movzx edx, word ptr [rsi + 0x38]; call 0x1401c1e40` |
| `0x001C52AE` | `call 0x1401c1e40; mov dword ptr [rdi + 0x104], eax; mov ecx, 0x27b0; movzx edx, word ptr [rsi + 0x38]; call 0x1401c1e40; mov dword ptr [rdi + 0x10c], eax; mov ecx, 0x2acc; movzx edx, word ptr [rsi + 0x38]` | `cmp dword ptr [rdi + 0xd8], -1; mov dword ptr [rdi + 0x110], eax; jne 0x1401c549f; cmp dword ptr [rdi + 0xd4], -1` |

### Full body

```asm
0x001C5120: mov qword ptr [rsp + 0x20], rsi
0x001C5125: push rdi
0x001C5126: sub rsp, 0x20
0x001C512A: cmp dword ptr [rcx + 0x38], 0
0x001C512E: mov rdi, rdx
0x001C5131: mov rsi, rcx
0x001C5134: jge 0x1401c5143
0x001C5136: xor al, al
0x001C5138: mov rsi, qword ptr [rsp + 0x48]
0x001C513D: add rsp, 0x20
0x001C5141: pop rdi
0x001C5142: ret
0x001C5143: mov ecx, dword ptr [rcx + 0x3c]
0x001C5146: mov qword ptr [rsp + 0x30], rbx
0x001C514B: mov qword ptr [rsp + 0x38], rbp
0x001C5150: sub ecx, 1
0x001C5153: je 0x1401c5339
0x001C5159: sub ecx, 1
0x001C515C: je 0x1401c52da
0x001C5162: sub ecx, 1
0x001C5165: je 0x1401c51b5
0x001C5167: cmp ecx, 1
0x001C516A: jne 0x1401c549f
0x001C5170: xor ebp, ebp
0x001C5172: mov ebx, 0x50200
0x001C5177: nop word ptr [rax + rax]
0x001C5180: movzx edx, word ptr [rsi + 0x38]
0x001C5184: mov ecx, ebx
0x001C5186: call 0x1401c1e40
0x001C518B: mov dword ptr [rdi + rbp*4], eax
0x001C518E: add ebx, 4
0x001C5191: inc rbp
0x001C5194: cmp rbp, 0x19
0x001C5198: jl 0x1401c5180
0x001C519A: cmp byte ptr [rdi + 4], 0xff
0x001C519E: jne 0x1401c549f
0x001C51A4: cmp byte ptr [rdi + 5], 0xff
0x001C51A8: jne 0x1401c549f
0x001C51AE: xor al, al
0x001C51B0: jmp 0x1401c54ec
0x001C51B5: movzx edx, word ptr [rsi + 0x38]
0x001C51B9: mov ecx, 0x28ec
0x001C51BE: call 0x1401c1e40
0x001C51C3: mov dword ptr [rdi + 0xc8], eax
0x001C51C9: mov ecx, 0x28f4
0x001C51CE: movzx edx, word ptr [rsi + 0x38]
0x001C51D2: call 0x1401c1e40
0x001C51D7: mov dword ptr [rdi + 0xcc], eax
0x001C51DD: mov ecx, 0x28fc
0x001C51E2: movzx edx, word ptr [rsi + 0x38]
0x001C51E6: call 0x1401c1e40
0x001C51EB: mov dword ptr [rdi + 0x114], eax
0x001C51F1: mov ecx, 0x2904
0x001C51F6: movzx edx, word ptr [rsi + 0x38]
0x001C51FA: call 0x1401c1e40
0x001C51FF: mov dword ptr [rdi + 0x118], eax
0x001C5205: mov ecx, 0x28c4
0x001C520A: movzx edx, word ptr [rsi + 0x38]
0x001C520E: call 0x1401c1e40
0x001C5213: mov dword ptr [rdi + 0xd0], eax
0x001C5219: mov ecx, 0x28a4
0x001C521E: movzx edx, word ptr [rsi + 0x38]
0x001C5222: call 0x1401c1e40
0x001C5227: mov dword ptr [rdi + 0xd4], eax
0x001C522D: mov ecx, 0x28ac
0x001C5232: movzx edx, word ptr [rsi + 0x38]
0x001C5236: call 0x1401c1e40
0x001C523B: mov dword ptr [rdi + 0xd8], eax
0x001C5241: mov ecx, 0x28b4
0x001C5246: movzx edx, word ptr [rsi + 0x38]
0x001C524A: call 0x1401c1e40
0x001C524F: mov dword ptr [rdi + 0xdc], eax
0x001C5255: mov ecx, 0x28bc
0x001C525A: movzx edx, word ptr [rsi + 0x38]
0x001C525E: call 0x1401c1e40
0x001C5263: mov dword ptr [rdi + 0xe0], eax
0x001C5269: mov ecx, 0x29c8
0x001C526E: movzx edx, word ptr [rsi + 0x38]
0x001C5272: call 0x1401c1e40
0x001C5277: mov dword ptr [rdi + 0xe4], eax
0x001C527D: mov ecx, 0x27b0
0x001C5282: movzx edx, word ptr [rsi + 0x38]
0x001C5286: call 0x1401c1e40
0x001C528B: mov dword ptr [rdi + 0x104], eax
0x001C5291: mov ecx, 0x27b0
0x001C5296: movzx edx, word ptr [rsi + 0x38]
0x001C529A: call 0x1401c1e40
0x001C529F: mov dword ptr [rdi + 0x10c], eax
0x001C52A5: mov ecx, 0x2acc
0x001C52AA: movzx edx, word ptr [rsi + 0x38]
0x001C52AE: call 0x1401c1e40
0x001C52B3: cmp dword ptr [rdi + 0xd8], -1
0x001C52BA: mov dword ptr [rdi + 0x110], eax
0x001C52C0: jne 0x1401c549f
0x001C52C6: cmp dword ptr [rdi + 0xd4], -1
0x001C52CD: jne 0x1401c549f
0x001C52D3: xor al, al
0x001C52D5: jmp 0x1401c54ec
```

## Write/apply path `0x001C6CA0..0x001C7102`

| call | arg setup window | post-call/store |
|---|---|---|
| `0x001C6D7A` | `jne 0x1401c70d6; cmp dword ptr [rip + 0x61f6e7], 0; jg 0x1401c70d6; mov edx, dword ptr [rdi + 4]; cmp edx, dword ptr [r14 + 4]; je 0x1401c6dcd; movzx r8d, word ptr [rbx + 0x38]; mov ecx, 0x50204` | `test al, al; je 0x1401c6dca; movzx r8d, word ptr [rbx + 0x38]; mov edx, dword ptr [rdi + 4]` |
| `0x001C6D90` | `movzx r8d, word ptr [rbx + 0x38]; mov ecx, 0x50204; call 0x1401c1ed0; test al, al; je 0x1401c6dca; movzx r8d, word ptr [rbx + 0x38]; mov edx, dword ptr [rdi + 4]; mov ecx, 0x52204` | `test al, al; je 0x1401c6dca; movzx r8d, word ptr [rbx + 0x38]; mov edx, dword ptr [rdi + 4]` |
| `0x001C6DA6` | `mov edx, dword ptr [rdi + 4]; mov ecx, 0x52204; call 0x1401c1ed0; test al, al; je 0x1401c6dca; movzx r8d, word ptr [rbx + 0x38]; mov edx, dword ptr [rdi + 4]; mov ecx, 0x54204` | `test al, al; je 0x1401c6dca; movzx r8d, word ptr [rbx + 0x38]; mov edx, dword ptr [rdi + 4]` |
| `0x001C6DBC` | `mov edx, dword ptr [rdi + 4]; mov ecx, 0x54204; call 0x1401c1ed0; test al, al; je 0x1401c6dca; movzx r8d, word ptr [rbx + 0x38]; mov edx, dword ptr [rdi + 4]; mov ecx, 0x56204` | `test al, al; je 0x1401c6dca; mov r15b, 1; jmp 0x1401c6dcd` |
| `0x001C6DE0` | `mov r15b, 1; jmp 0x1401c6dcd; xor sil, sil; mov edx, dword ptr [rdi + 8]; cmp edx, dword ptr [r14 + 8]; je 0x1401c6e33; movzx r8d, word ptr [rbx + 0x38]; mov ecx, 0x50208` | `test al, al; je 0x1401c6e30; movzx r8d, word ptr [rbx + 0x38]; mov edx, dword ptr [rdi + 8]` |
| `0x001C6DF6` | `movzx r8d, word ptr [rbx + 0x38]; mov ecx, 0x50208; call 0x1401c1ed0; test al, al; je 0x1401c6e30; movzx r8d, word ptr [rbx + 0x38]; mov edx, dword ptr [rdi + 8]; mov ecx, 0x52208` | `test al, al; je 0x1401c6e30; movzx r8d, word ptr [rbx + 0x38]; mov edx, dword ptr [rdi + 8]` |
| `0x001C6E0C` | `mov edx, dword ptr [rdi + 8]; mov ecx, 0x52208; call 0x1401c1ed0; test al, al; je 0x1401c6e30; movzx r8d, word ptr [rbx + 0x38]; mov edx, dword ptr [rdi + 8]; mov ecx, 0x54208` | `test al, al; je 0x1401c6e30; movzx r8d, word ptr [rbx + 0x38]; mov edx, dword ptr [rdi + 8]` |
| `0x001C6E22` | `mov edx, dword ptr [rdi + 8]; mov ecx, 0x54208; call 0x1401c1ed0; test al, al; je 0x1401c6e30; movzx r8d, word ptr [rbx + 0x38]; mov edx, dword ptr [rdi + 8]; mov ecx, 0x56208` | `test al, al; je 0x1401c6e30; mov r15b, 1; jmp 0x1401c6e33` |
| `0x001C6E46` | `mov r15b, 1; jmp 0x1401c6e33; xor sil, sil; mov edx, dword ptr [rdi + 0xc]; cmp edx, dword ptr [r14 + 0xc]; je 0x1401c6e99; movzx r8d, word ptr [rbx + 0x38]; mov ecx, 0x5020c` | `test al, al; je 0x1401c6e96; movzx r8d, word ptr [rbx + 0x38]; mov edx, dword ptr [rdi + 0xc]` |
| `0x001C6E5C` | `movzx r8d, word ptr [rbx + 0x38]; mov ecx, 0x5020c; call 0x1401c1ed0; test al, al; je 0x1401c6e96; movzx r8d, word ptr [rbx + 0x38]; mov edx, dword ptr [rdi + 0xc]; mov ecx, 0x5220c` | `test al, al; je 0x1401c6e96; movzx r8d, word ptr [rbx + 0x38]; mov edx, dword ptr [rdi + 0xc]` |
| `0x001C6E72` | `mov edx, dword ptr [rdi + 0xc]; mov ecx, 0x5220c; call 0x1401c1ed0; test al, al; je 0x1401c6e96; movzx r8d, word ptr [rbx + 0x38]; mov edx, dword ptr [rdi + 0xc]; mov ecx, 0x5420c` | `test al, al; je 0x1401c6e96; movzx r8d, word ptr [rbx + 0x38]; mov edx, dword ptr [rdi + 0xc]` |
| `0x001C6E88` | `mov edx, dword ptr [rdi + 0xc]; mov ecx, 0x5420c; call 0x1401c1ed0; test al, al; je 0x1401c6e96; movzx r8d, word ptr [rbx + 0x38]; mov edx, dword ptr [rdi + 0xc]; mov ecx, 0x5620c` | `test al, al; je 0x1401c6e96; mov r15b, 1; jmp 0x1401c6e99` |
| `0x001C6EAC` | `mov r15b, 1; jmp 0x1401c6e99; xor sil, sil; mov edx, dword ptr [rdi + 0x10]; cmp edx, dword ptr [r14 + 0x10]; je 0x1401c6eff; movzx r8d, word ptr [rbx + 0x38]; mov ecx, 0x50210` | `test al, al; je 0x1401c6efc; movzx r8d, word ptr [rbx + 0x38]; mov edx, dword ptr [rdi + 0x10]` |
| `0x001C6EC2` | `movzx r8d, word ptr [rbx + 0x38]; mov ecx, 0x50210; call 0x1401c1ed0; test al, al; je 0x1401c6efc; movzx r8d, word ptr [rbx + 0x38]; mov edx, dword ptr [rdi + 0x10]; mov ecx, 0x52210` | `test al, al; je 0x1401c6efc; movzx r8d, word ptr [rbx + 0x38]; mov edx, dword ptr [rdi + 0x10]` |
| `0x001C6ED8` | `mov edx, dword ptr [rdi + 0x10]; mov ecx, 0x52210; call 0x1401c1ed0; test al, al; je 0x1401c6efc; movzx r8d, word ptr [rbx + 0x38]; mov edx, dword ptr [rdi + 0x10]; mov ecx, 0x54210` | `test al, al; je 0x1401c6efc; movzx r8d, word ptr [rbx + 0x38]; mov edx, dword ptr [rdi + 0x10]` |
| `0x001C6EEE` | `mov edx, dword ptr [rdi + 0x10]; mov ecx, 0x54210; call 0x1401c1ed0; test al, al; je 0x1401c6efc; movzx r8d, word ptr [rbx + 0x38]; mov edx, dword ptr [rdi + 0x10]; mov ecx, 0x56210` | `test al, al; je 0x1401c6efc; mov r15b, 1; jmp 0x1401c6eff` |
| `0x001C6F16` | `mov r15b, 1; jmp 0x1401c6eff; xor sil, sil; mov edx, dword ptr [rdi + 0x30]; cmp edx, dword ptr [r14 + 0x30]; je 0x1401c6f97; movzx r8d, word ptr [rbx + 0x38]; mov ecx, 0x50230` | `test al, al; je 0x1401c6f61; movzx r8d, word ptr [rbx + 0x38]; mov edx, dword ptr [rdi + 0x30]` |
| `0x001C6F2C` | `movzx r8d, word ptr [rbx + 0x38]; mov ecx, 0x50230; call 0x1401c1ed0; test al, al; je 0x1401c6f61; movzx r8d, word ptr [rbx + 0x38]; mov edx, dword ptr [rdi + 0x30]; mov ecx, 0x52230` | `test al, al; je 0x1401c6f61; movzx r8d, word ptr [rbx + 0x38]; mov edx, dword ptr [rdi + 0x30]` |
| `0x001C6F42` | `mov edx, dword ptr [rdi + 0x30]; mov ecx, 0x52230; call 0x1401c1ed0; test al, al; je 0x1401c6f61; movzx r8d, word ptr [rbx + 0x38]; mov edx, dword ptr [rdi + 0x30]; mov ecx, 0x54230` | `test al, al; je 0x1401c6f61; movzx r8d, word ptr [rbx + 0x38]; mov edx, dword ptr [rdi + 0x30]` |
| `0x001C6F58` | `mov edx, dword ptr [rdi + 0x30]; mov ecx, 0x54230; call 0x1401c1ed0; test al, al; je 0x1401c6f61; movzx r8d, word ptr [rbx + 0x38]; mov edx, dword ptr [rdi + 0x30]; mov ecx, 0x56230` | `test al, al; jne 0x1401c6fa0; xor sil, sil; jmp 0x1401c6f97` |
| `0x001C6F7F` | `jne 0x1401c6fa0; xor sil, sil; jmp 0x1401c6f97; mov edx, dword ptr [rdi + 0x104]; cmp edx, dword ptr [r14 + 0x104]; je 0x1401c6f90; movzx r8d, word ptr [rbx + 0x38]; mov ecx, 0x27b0` | `test al, al; jne 0x1401c6f8d; xor sil, sil; jmp 0x1401c6f90` |

### Full body

```asm
0x001C6CA0: mov rax, rsp
0x001C6CA3: push rbp
0x001C6CA4: push rdi
0x001C6CA5: push r12
0x001C6CA7: push r14
0x001C6CA9: push r15
0x001C6CAB: mov rbp, rsp
0x001C6CAE: sub rsp, 0x80
0x001C6CB5: mov qword ptr [rbp - 0x58], 0xfffffffffffffffe
0x001C6CBD: mov qword ptr [rax + 0x10], rbx
0x001C6CC1: mov qword ptr [rax + 0x20], rsi
0x001C6CC5: mov rax, qword ptr [rip + 0x60fc24]
0x001C6CCC: xor rax, rsp
0x001C6CCF: mov qword ptr [rbp - 0x10], rax
0x001C6CD3: mov rdi, r8
0x001C6CD6: mov r14, rdx
0x001C6CD9: mov rbx, rcx
0x001C6CDC: mov r8d, 0x11c
0x001C6CE2: mov rcx, rdi
0x001C6CE5: call 0x1403d2f70
0x001C6CEA: test eax, eax
0x001C6CEC: jne 0x1401c6cf5
0x001C6CEE: mov al, 1
0x001C6CF0: jmp 0x1401c70da
0x001C6CF5: mov sil, 1
0x001C6CF8: xor r15b, r15b
0x001C6CFB: cmp dword ptr [rbx + 0x78], 0
0x001C6CFF: jne 0x1401c6d33
0x001C6D01: cmp dword ptr [rbx + 0x7c], 0
0x001C6D05: jne 0x1401c6d33
0x001C6D07: xor eax, eax
0x001C6D09: mov byte ptr [rbp - 0x60], al
0x001C6D0C: lea rcx, [rbx + 0x8c]
0x001C6D13: lea rax, [rbx + 0x80]
0x001C6D1A: cmp rax, rcx
0x001C6D1D: je 0x1401c6d2e
0x001C6D1F: nop
0x001C6D20: cmp dword ptr [rax], 0
0x001C6D23: jne 0x1401c6d33
0x001C6D25: add rax, 4
0x001C6D29: cmp rax, rcx
0x001C6D2C: jne 0x1401c6d20
0x001C6D2E: mov r12b, 1
0x001C6D31: jmp 0x1401c6d36
0x001C6D33: xor r12b, r12b
0x001C6D36: mov ecx, dword ptr [rbx + 0x3c]
0x001C6D39: sub ecx, 1
0x001C6D3C: je 0x1401c6f66
0x001C6D42: cmp ecx, 3
0x001C6D45: jne 0x1401c70d6
0x001C6D4B: movzx eax, byte ptr [rip + 0x61f6fa]
0x001C6D52: test al, al
0x001C6D54: jne 0x1401c70d6
0x001C6D5A: cmp dword ptr [rip + 0x61f6e7], 0
0x001C6D61: jg 0x1401c70d6
0x001C6D67: mov edx, dword ptr [rdi + 4]
0x001C6D6A: cmp edx, dword ptr [r14 + 4]
0x001C6D6E: je 0x1401c6dcd
0x001C6D70: movzx r8d, word ptr [rbx + 0x38]
0x001C6D75: mov ecx, 0x50204
0x001C6D7A: call 0x1401c1ed0
0x001C6D7F: test al, al
0x001C6D81: je 0x1401c6dca
0x001C6D83: movzx r8d, word ptr [rbx + 0x38]
0x001C6D88: mov edx, dword ptr [rdi + 4]
0x001C6D8B: mov ecx, 0x52204
0x001C6D90: call 0x1401c1ed0
0x001C6D95: test al, al
0x001C6D97: je 0x1401c6dca
0x001C6D99: movzx r8d, word ptr [rbx + 0x38]
0x001C6D9E: mov edx, dword ptr [rdi + 4]
0x001C6DA1: mov ecx, 0x54204
0x001C6DA6: call 0x1401c1ed0
0x001C6DAB: test al, al
0x001C6DAD: je 0x1401c6dca
0x001C6DAF: movzx r8d, word ptr [rbx + 0x38]
0x001C6DB4: mov edx, dword ptr [rdi + 4]
0x001C6DB7: mov ecx, 0x56204
0x001C6DBC: call 0x1401c1ed0
0x001C6DC1: test al, al
0x001C6DC3: je 0x1401c6dca
0x001C6DC5: mov r15b, 1
0x001C6DC8: jmp 0x1401c6dcd
0x001C6DCA: xor sil, sil
0x001C6DCD: mov edx, dword ptr [rdi + 8]
0x001C6DD0: cmp edx, dword ptr [r14 + 8]
0x001C6DD4: je 0x1401c6e33
0x001C6DD6: movzx r8d, word ptr [rbx + 0x38]
0x001C6DDB: mov ecx, 0x50208
0x001C6DE0: call 0x1401c1ed0
0x001C6DE5: test al, al
0x001C6DE7: je 0x1401c6e30
0x001C6DE9: movzx r8d, word ptr [rbx + 0x38]
0x001C6DEE: mov edx, dword ptr [rdi + 8]
0x001C6DF1: mov ecx, 0x52208
0x001C6DF6: call 0x1401c1ed0
0x001C6DFB: test al, al
0x001C6DFD: je 0x1401c6e30
0x001C6DFF: movzx r8d, word ptr [rbx + 0x38]
0x001C6E04: mov edx, dword ptr [rdi + 8]
0x001C6E07: mov ecx, 0x54208
0x001C6E0C: call 0x1401c1ed0
0x001C6E11: test al, al
0x001C6E13: je 0x1401c6e30
0x001C6E15: movzx r8d, word ptr [rbx + 0x38]
0x001C6E1A: mov edx, dword ptr [rdi + 8]
0x001C6E1D: mov ecx, 0x56208
0x001C6E22: call 0x1401c1ed0
0x001C6E27: test al, al
0x001C6E29: je 0x1401c6e30
0x001C6E2B: mov r15b, 1
0x001C6E2E: jmp 0x1401c6e33
0x001C6E30: xor sil, sil
0x001C6E33: mov edx, dword ptr [rdi + 0xc]
0x001C6E36: cmp edx, dword ptr [r14 + 0xc]
0x001C6E3A: je 0x1401c6e99
0x001C6E3C: movzx r8d, word ptr [rbx + 0x38]
0x001C6E41: mov ecx, 0x5020c
0x001C6E46: call 0x1401c1ed0
0x001C6E4B: test al, al
0x001C6E4D: je 0x1401c6e96
0x001C6E4F: movzx r8d, word ptr [rbx + 0x38]
0x001C6E54: mov edx, dword ptr [rdi + 0xc]
0x001C6E57: mov ecx, 0x5220c
0x001C6E5C: call 0x1401c1ed0
0x001C6E61: test al, al
0x001C6E63: je 0x1401c6e96
0x001C6E65: movzx r8d, word ptr [rbx + 0x38]
0x001C6E6A: mov edx, dword ptr [rdi + 0xc]
0x001C6E6D: mov ecx, 0x5420c
0x001C6E72: call 0x1401c1ed0
0x001C6E77: test al, al
0x001C6E79: je 0x1401c6e96
0x001C6E7B: movzx r8d, word ptr [rbx + 0x38]
0x001C6E80: mov edx, dword ptr [rdi + 0xc]
0x001C6E83: mov ecx, 0x5620c
0x001C6E88: call 0x1401c1ed0
0x001C6E8D: test al, al
0x001C6E8F: je 0x1401c6e96
0x001C6E91: mov r15b, 1
0x001C6E94: jmp 0x1401c6e99
0x001C6E96: xor sil, sil
0x001C6E99: mov edx, dword ptr [rdi + 0x10]
0x001C6E9C: cmp edx, dword ptr [r14 + 0x10]
0x001C6EA0: je 0x1401c6eff
0x001C6EA2: movzx r8d, word ptr [rbx + 0x38]
0x001C6EA7: mov ecx, 0x50210
0x001C6EAC: call 0x1401c1ed0
0x001C6EB1: test al, al
0x001C6EB3: je 0x1401c6efc
0x001C6EB5: movzx r8d, word ptr [rbx + 0x38]
0x001C6EBA: mov edx, dword ptr [rdi + 0x10]
0x001C6EBD: mov ecx, 0x52210
0x001C6EC2: call 0x1401c1ed0
0x001C6EC7: test al, al
0x001C6EC9: je 0x1401c6efc
0x001C6ECB: movzx r8d, word ptr [rbx + 0x38]
0x001C6ED0: mov edx, dword ptr [rdi + 0x10]
0x001C6ED3: mov ecx, 0x54210
0x001C6ED8: call 0x1401c1ed0
0x001C6EDD: test al, al
0x001C6EDF: je 0x1401c6efc
0x001C6EE1: movzx r8d, word ptr [rbx + 0x38]
0x001C6EE6: mov edx, dword ptr [rdi + 0x10]
0x001C6EE9: mov ecx, 0x56210
0x001C6EEE: call 0x1401c1ed0
0x001C6EF3: test al, al
0x001C6EF5: je 0x1401c6efc
0x001C6EF7: mov r15b, 1
0x001C6EFA: jmp 0x1401c6eff
0x001C6EFC: xor sil, sil
0x001C6EFF: mov edx, dword ptr [rdi + 0x30]
0x001C6F02: cmp edx, dword ptr [r14 + 0x30]
0x001C6F06: je 0x1401c6f97
0x001C6F0C: movzx r8d, word ptr [rbx + 0x38]
0x001C6F11: mov ecx, 0x50230
0x001C6F16: call 0x1401c1ed0
0x001C6F1B: test al, al
0x001C6F1D: je 0x1401c6f61
0x001C6F1F: movzx r8d, word ptr [rbx + 0x38]
0x001C6F24: mov edx, dword ptr [rdi + 0x30]
0x001C6F27: mov ecx, 0x52230
0x001C6F2C: call 0x1401c1ed0
0x001C6F31: test al, al
0x001C6F33: je 0x1401c6f61
0x001C6F35: movzx r8d, word ptr [rbx + 0x38]
0x001C6F3A: mov edx, dword ptr [rdi + 0x30]
0x001C6F3D: mov ecx, 0x54230
0x001C6F42: call 0x1401c1ed0
0x001C6F47: test al, al
0x001C6F49: je 0x1401c6f61
0x001C6F4B: movzx r8d, word ptr [rbx + 0x38]
0x001C6F50: mov edx, dword ptr [rdi + 0x30]
0x001C6F53: mov ecx, 0x56230
0x001C6F58: call 0x1401c1ed0
0x001C6F5D: test al, al
0x001C6F5F: jne 0x1401c6fa0
0x001C6F61: xor sil, sil
0x001C6F64: jmp 0x1401c6f97
0x001C6F66: mov edx, dword ptr [rdi + 0x104]
0x001C6F6C: cmp edx, dword ptr [r14 + 0x104]
0x001C6F73: je 0x1401c6f90
0x001C6F75: movzx r8d, word ptr [rbx + 0x38]
0x001C6F7A: mov ecx, 0x27b0
0x001C6F7F: call 0x1401c1ed0
0x001C6F84: test al, al
0x001C6F86: jne 0x1401c6f8d
0x001C6F88: xor sil, sil
0x001C6F8B: jmp 0x1401c6f90
0x001C6F8D: mov r15b, 1
0x001C6F90: movzx eax, byte ptr [rip + 0x61f4b5]
0x001C6F97: test r15b, r15b
0x001C6F9A: je 0x1401c70d6
0x001C6FA0: mov byte ptr [rbx + 0x44], 1
0x001C6FA4: test sil, sil
0x001C6FA7: je 0x1401c70d6
0x001C6FAD: test r12b, r12b
0x001C6FB0: je 0x1401c70d6
0x001C6FB6: mov dword ptr [rbp - 0x50], 0x48
0x001C6FBD: mov dword ptr [rbp - 0x4c], 0x34
0x001C6FC4: mov eax, dword ptr [rbp - 0x4c]
0x001C6FC7: xor eax, 0x33
0x001C6FCA: mov byte ptr [rbp - 0x48], al
0x001C6FCD: movsx ecx, byte ptr [rbp - 0x48]
0x001C6FD1: xor ecx, 0x35
0x001C6FD4: mov byte ptr [rbp - 0x47], cl
0x001C6FD7: movsx ecx, byte ptr [rbp - 0x47]
0x001C6FDB: xor ecx, 0x72
0x001C6FDE: mov byte ptr [rbp - 0x46], cl
0x001C6FE1: movsx ecx, byte ptr [rbp - 0x46]
0x001C6FE5: xor ecx, 0x68
0x001C6FE8: mov byte ptr [rbp - 0x45], cl
0x001C6FEB: movsx ecx, byte ptr [rbp - 0x45]
0x001C6FEF: xor ecx, 0x3a
0x001C6FF2: mov byte ptr [rbp - 0x44], cl
0x001C6FF5: movsx ecx, byte ptr [rbp - 0x44]
0x001C6FF9: xor ecx, 0x2d
0x001C6FFC: mov byte ptr [rbp - 0x43], cl
0x001C6FFF: movsx ecx, byte ptr [rbp - 0x43]
0x001C7003: xor ecx, 0x3b
0x001C7006: mov byte ptr [rbp - 0x42], cl
0x001C7009: movsx ecx, byte ptr [rbp - 0x42]
0x001C700D: xor ecx, 0x2d
0x001C7010: mov byte ptr [rbp - 0x41], cl
0x001C7013: movsx ecx, byte ptr [rbp - 0x41]
0x001C7017: xor ecx, 0x3c
0x001C701A: mov byte ptr [rbp - 0x40], cl
0x001C701D: movsx ecx, byte ptr [rbp - 0x40]
0x001C7021: xor ecx, 0x68
0x001C7024: mov byte ptr [rbp - 0x3f], cl
0x001C7027: movsx ecx, byte ptr [rbp - 0x3f]
0x001C702B: xor ecx, 0x1e
0x001C702E: mov byte ptr [rbp - 0x3e], cl
0x001C7031: movsx ecx, byte ptr [rbp - 0x3e]
0x001C7035: xor ecx, 0x1a
0x001C7038: mov byte ptr [rbp - 0x3d], cl
0x001C703B: movsx ecx, byte ptr [rbp - 0x3d]
0x001C703F: xor ecx, 9
0x001C7042: mov byte ptr [rbp - 0x3c], cl
0x001C7045: movsx ecx, byte ptr [rbp - 0x3c]
0x001C7049: xor ecx, 5
0x001C704C: mov byte ptr [rbp - 0x3b], cl
0x001C704F: movsx ecx, byte ptr [rbp - 0x3b]
0x001C7053: xor ecx, 0x68
0x001C7056: mov byte ptr [rbp - 0x3a], cl
0x001C7059: movsx ecx, byte ptr [rbp - 0x3a]
0x001C705D: xor ecx, 0x3c
0x001C7060: mov byte ptr [rbp - 0x39], cl
0x001C7063: movsx ecx, byte ptr [rbp - 0x39]
0x001C7067: xor ecx, 0x21
0x001C706A: mov byte ptr [rbp - 0x38], cl
0x001C706D: movsx ecx, byte ptr [rbp - 0x38]
0x001C7071: xor ecx, 0x25
0x001C7074: mov byte ptr [rbp - 0x37], cl
0x001C7077: movsx ecx, byte ptr [rbp - 0x37]
0x001C707B: xor ecx, 0x21
0x001C707E: mov byte ptr [rbp - 0x36], cl
0x001C7081: movsx ecx, byte ptr [rbp - 0x36]
0x001C7085: xor ecx, 0x26
0x001C7088: mov byte ptr [rbp - 0x35], cl
0x001C708B: movsx ecx, byte ptr [rbp - 0x35]
0x001C708F: xor ecx, 0x2f
0x001C7092: mov byte ptr [rbp - 0x34], cl
0x001C7095: movsx ecx, byte ptr [rbp - 0x34]
0x001C7099: xor ecx, 0x3b
0x001C709C: mov byte ptr [rbp - 0x33], cl
0x001C709F: xor eax, eax
0x001C70A1: mov byte ptr [rbp - 0x32], al
0x001C70A4: movzx eax, byte ptr [rbp - 0x48]
0x001C70A8: lea rdx, [rbp - 0x30]
0x001C70AC: lea rcx, [rbp - 0x50]
0x001C70B0: call 0x14026ee50
0x001C70B5: nop
0x001C70B6: cmp qword ptr [rax + 0x18], 0x10
0x001C70BB: jb 0x1401c70c0
0x001C70BD: mov rax, qword ptr [rax]
0x001C70C0: lea rdx, [rbx + 0x10]
0x001C70C4: mov rcx, rax
0x001C70C7: call 0x140063980
0x001C70CC: nop
0x001C70CD: lea rcx, [rbp - 0x30]
0x001C70D1: call 0x140032ef0
0x001C70D6: movzx eax, sil
0x001C70DA: mov rcx, qword ptr [rbp - 0x10]
0x001C70DE: xor rcx, rsp
0x001C70E1: call 0x1403b24c0
0x001C70E6: lea r11, [rsp + 0x80]
0x001C70EE: mov rbx, qword ptr [r11 + 0x38]
0x001C70F2: mov rsi, qword ptr [r11 + 0x48]
0x001C70F6: mov rsp, r11
0x001C70F9: pop r15
0x001C70FB: pop r14
0x001C70FD: pop r12
0x001C70FF: pop rdi
0x001C7100: pop rbp
0x001C7101: ret
```
