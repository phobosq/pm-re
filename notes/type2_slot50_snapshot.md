# Type2 slot +0x50 snapshot flow

PDATA `0x001CF8B0..0x001CFEC5`

Known snapshot getter: `0x00084A60`.

## Calls

| RVA | target/form |
|---|---|
| `0x001CF903` | `RVA 0x00391AC4` |
| `0x001CF90E` | `RVA 0x0039219C` |
| `0x001CF938` | `RVA 0x00391B24` |
| `0x001CF943` | `RVA 0x0039219C` |
| `0x001CF954` | `RVA 0x00084A60` |
| `0x001CF9B4` | `RVA 0x00391AC4` |
| `0x001CF9BF` | `RVA 0x0039219C` |
| `0x001CF9DD` | `RVA 0x001ED8B0` |
| `0x001CF9E9` | `RVA 0x003B20DC` |
| `0x001CF9F2` | `RVA 0x00391B24` |
| `0x001CF9FD` | `RVA 0x0039219C` |
| `0x001CFA1F` | `RVA 0x00391AC4` |
| `0x001CFA2A` | `RVA 0x0039219C` |
| `0x001CFA4E` | `RVA 0x001CD970` |
| `0x001CFA6C` | `RVA 0x001ED8B0` |
| `0x001CFA79` | `RVA 0x003B20DC` |
| `0x001CFA8B` | `RVA 0x001ED8B0` |
| `0x001CFA98` | `RVA 0x003B20DC` |
| `0x001CFAA1` | `RVA 0x00391B24` |
| `0x001CFAAC` | `RVA 0x0039219C` |
| `0x001CFABA` | `RVA 0x00159B40` |
| `0x001CFB11` | `RVA 0x001EFF00` |
| `0x001CFB29` | `RVA 0x001F0140` |
| `0x001CFDEB` | `RVA 0x001D0E50` |
| `0x001CFE30` | `RVA 0x003D23C8` |
| `0x001CFE4D` | `RVA 0x003D25D0` |
| `0x001CFE56` | `RVA 0x00391AC4` |
| `0x001CFE61` | `RVA 0x0039219C` |
| `0x001CFE8C` | `RVA 0x00391B24` |
| `0x001CFE97` | `RVA 0x0039219C` |
| `0x001CFEA8` | `RVA 0x003B24C0` |

## Stack/local memory accesses around snapshot-sized regions

| RVA | instruction |
|---|---|
| `0x001CF8C0` | `mov qword ptr [rsp + 0x90], 0xfffffffffffffffe` |
| `0x001CF8CC` | `mov qword ptr [rsp + 0x258], rbx` |
| `0x001CF8DE` | `mov qword ptr [rsp + 0x218], rax` |
| `0x001CF8EC` | `mov qword ptr [rsp + 0x48], rdx` |
| `0x001CF8F4` | `mov qword ptr [rsp + 0x60], rcx` |
| `0x001CF915` | `mov byte ptr [rsp + 0x40], al` |
| `0x001CF949` | `lea rdx, [rsp + 0xb0]` |
| `0x001CF99E` | `cmp dword ptr [rsp + 0xdc], 0` |
| `0x001CFA14` | `mov qword ptr [rsp + 0x98], rbx` |
| `0x001CFA36` | `mov dword ptr [rsp + 0x44], eax` |
| `0x001CFA3A` | `mov qword ptr [rsp + 0x50], rdi` |
| `0x001CFA3F` | `lea r8, [rsp + 0x44]` |
| `0x001CFA44` | `lea rdx, [rsp + 0x50]` |
| `0x001CFA49` | `lea rcx, [rsp + 0x58]` |
| `0x001CFA7E` | `mov r12, qword ptr [rsp + 0x58]` |
| `0x001CFAD4` | `mov r9d, dword ptr [rsp + 0xe0]` |
| `0x001CFADC` | `cmp dword ptr [rsp + 0xdc], 0` |
| `0x001CFAEC` | `mov dword ptr [rsp + 0x30], r8d` |
| `0x001CFAF1` | `mov dword ptr [rsp + 0x28], r9d` |
| `0x001CFAF6` | `mov dword ptr [rsp + 0x20], eax` |
| `0x001CFAFA` | `movzx r9d, byte ptr [rsp + 0xd5]` |
| `0x001CFB03` | `mov r8d, dword ptr [rsp + 0xd0]` |
| `0x001CFB16` | `mov r12, qword ptr [rsp + 0x48]` |
| `0x001CFB1B` | `mov r8d, dword ptr [rsp + 0xe4]` |
| `0x001CFB36` | `mov dword ptr [rsp + 0x1b0], 0x1c` |
| `0x001CFB41` | `mov eax, dword ptr [rsp + 0x1b0]` |
| `0x001CFB4E` | `mov byte ptr [rsp + 0x1b4], al` |
| `0x001CFB55` | `movsx ecx, byte ptr [rsp + 0x1b4]` |
| `0x001CFB63` | `mov byte ptr [rsp + 0x1b5], cl` |
| `0x001CFB6A` | `movsx ecx, byte ptr [rsp + 0x1b5]` |
| `0x001CFB78` | `mov byte ptr [rsp + 0x1b6], cl` |
| `0x001CFB7F` | `movsx ecx, byte ptr [rsp + 0x1b6]` |
| `0x001CFB8D` | `mov byte ptr [rsp + 0x1b7], cl` |
| `0x001CFB94` | `movsx ecx, byte ptr [rsp + 0x1b7]` |
| `0x001CFBA2` | `mov byte ptr [rsp + 0x1b8], cl` |
| `0x001CFBA9` | `movsx ecx, byte ptr [rsp + 0x1b8]` |
| `0x001CFBB7` | `mov byte ptr [rsp + 0x1b9], cl` |
| `0x001CFBBE` | `movsx ecx, byte ptr [rsp + 0x1b9]` |
| `0x001CFBCC` | `mov byte ptr [rsp + 0x1ba], cl` |
| `0x001CFBD3` | `movsx ecx, byte ptr [rsp + 0x1ba]` |
| `0x001CFBE1` | `mov byte ptr [rsp + 0x1bb], cl` |
| `0x001CFBE8` | `movsx ecx, byte ptr [rsp + 0x1bb]` |
| `0x001CFBF6` | `mov byte ptr [rsp + 0x1bc], cl` |
| `0x001CFBFD` | `movsx ecx, byte ptr [rsp + 0x1bc]` |
| `0x001CFC0B` | `mov byte ptr [rsp + 0x1bd], cl` |
| `0x001CFC12` | `movsx ecx, byte ptr [rsp + 0x1bd]` |
| `0x001CFC20` | `mov byte ptr [rsp + 0x1be], cl` |
| `0x001CFC27` | `movsx ecx, byte ptr [rsp + 0x1be]` |
| `0x001CFC35` | `mov byte ptr [rsp + 0x1bf], cl` |
| `0x001CFC3C` | `movsx ecx, byte ptr [rsp + 0x1bf]` |
| `0x001CFC4A` | `mov byte ptr [rsp + 0x1c0], cl` |
| `0x001CFC51` | `movsx ecx, byte ptr [rsp + 0x1c0]` |
| `0x001CFC5F` | `mov byte ptr [rsp + 0x1c1], cl` |
| `0x001CFC66` | `movsx ecx, byte ptr [rsp + 0x1c1]` |
| `0x001CFC74` | `mov byte ptr [rsp + 0x1c2], cl` |
| `0x001CFC7B` | `movsx ecx, byte ptr [rsp + 0x1c2]` |
| `0x001CFC89` | `mov byte ptr [rsp + 0x1c3], cl` |
| `0x001CFC90` | `movsx ecx, byte ptr [rsp + 0x1c3]` |
| `0x001CFC9E` | `mov byte ptr [rsp + 0x1c4], cl` |
| `0x001CFCA5` | `movsx ecx, byte ptr [rsp + 0x1c4]` |
| `0x001CFCB3` | `mov byte ptr [rsp + 0x1c5], cl` |
| `0x001CFCBA` | `movsx ecx, byte ptr [rsp + 0x1c5]` |
| `0x001CFCC8` | `mov byte ptr [rsp + 0x1c6], cl` |
| `0x001CFCCF` | `movsx ecx, byte ptr [rsp + 0x1c6]` |
| `0x001CFCDD` | `mov byte ptr [rsp + 0x1c7], cl` |
| `0x001CFCE4` | `movsx ecx, byte ptr [rsp + 0x1c7]` |
| `0x001CFCF2` | `mov byte ptr [rsp + 0x1c8], cl` |
| `0x001CFCF9` | `movsx ecx, byte ptr [rsp + 0x1c8]` |
| `0x001CFD07` | `mov byte ptr [rsp + 0x1c9], cl` |
| `0x001CFD0E` | `movsx ecx, byte ptr [rsp + 0x1c9]` |
| `0x001CFD1C` | `mov byte ptr [rsp + 0x1ca], cl` |
| `0x001CFD23` | `movsx ecx, byte ptr [rsp + 0x1ca]` |
| `0x001CFD31` | `mov byte ptr [rsp + 0x1cb], cl` |
| `0x001CFD38` | `movsx ecx, byte ptr [rsp + 0x1cb]` |
| `0x001CFD46` | `mov byte ptr [rsp + 0x1cc], cl` |
| `0x001CFD4D` | `movsx ecx, byte ptr [rsp + 0x1cc]` |
| `0x001CFD5B` | `mov byte ptr [rsp + 0x1cd], cl` |
| `0x001CFD62` | `movsx ecx, byte ptr [rsp + 0x1cd]` |
| `0x001CFD70` | `mov byte ptr [rsp + 0x1ce], cl` |
| `0x001CFD77` | `movsx ecx, byte ptr [rsp + 0x1ce]` |
| `0x001CFD85` | `mov byte ptr [rsp + 0x1cf], cl` |
| `0x001CFD8C` | `movsx ecx, byte ptr [rsp + 0x1cf]` |
| `0x001CFD9A` | `mov byte ptr [rsp + 0x1d0], cl` |
| `0x001CFDA1` | `movsx ecx, byte ptr [rsp + 0x1d0]` |
| `0x001CFDAF` | `mov byte ptr [rsp + 0x1d1], cl` |
| `0x001CFDB6` | `movsx ecx, byte ptr [rsp + 0x1d1]` |
| `0x001CFDC4` | `mov byte ptr [rsp + 0x1d2], cl` |
| `0x001CFDCB` | `mov byte ptr [rsp + 0x1d3], 0` |
| `0x001CFDD3` | `movzx eax, byte ptr [rsp + 0x1b4]` |
| `0x001CFDDB` | `lea rdx, [rsp + 0x1f8]` |
| `0x001CFDE3` | `lea rcx, [rsp + 0x1b0]` |
| `0x001CFE02` | `mov qword ptr [rsp + 0x68], rcx` |
| `0x001CFE09` | `mov qword ptr [rsp + 0x70], rcx` |
| `0x001CFE0E` | `mov qword ptr [rsp + 0x78], rcx` |
| `0x001CFE13` | `mov qword ptr [rsp + 0x80], rax` |
| `0x001CFE1B` | `mov byte ptr [rsp + 0x88], 1` |
| `0x001CFE23` | `lea rdx, [rsp + 0x70]` |
| `0x001CFE28` | `lea rcx, [rsp + 0x80]` |
| `0x001CFE3C` | `mov qword ptr [rsp + 0x68], rax` |
| `0x001CFE48` | `lea rcx, [rsp + 0x68]` |
| `0x001CFE9D` | `mov rcx, qword ptr [rsp + 0x218]` |
| `0x001CFEAD` | `mov rbx, qword ptr [rsp + 0x258]` |

## Full body

```asm
0x001CF8B0: push rsi
0x001CF8B2: push rdi
0x001CF8B3: push r12
0x001CF8B5: push r14
0x001CF8B7: push r15
0x001CF8B9: sub rsp, 0x220
0x001CF8C0: mov qword ptr [rsp + 0x90], 0xfffffffffffffffe
0x001CF8CC: mov qword ptr [rsp + 0x258], rbx
0x001CF8D4: mov rax, qword ptr [rip + 0x607015]
0x001CF8DB: xor rax, rsp
0x001CF8DE: mov qword ptr [rsp + 0x218], rax
0x001CF8E6: mov r14, r8
0x001CF8E9: mov r12, rdx
0x001CF8EC: mov qword ptr [rsp + 0x48], rdx
0x001CF8F1: mov rdi, rcx
0x001CF8F4: mov qword ptr [rsp + 0x60], rcx
0x001CF8F9: lea rbx, [rcx + 0x7c0]
0x001CF900: mov rcx, rbx
0x001CF903: call 0x140391ac4
0x001CF908: test eax, eax
0x001CF90A: je 0x1401cf913
0x001CF90C: mov ecx, eax
0x001CF90E: call 0x14039219c
0x001CF913: xor eax, eax
0x001CF915: mov byte ptr [rsp + 0x40], al
0x001CF919: mov qword ptr [rdi + 0x810], rax
0x001CF920: mov qword ptr [rdi + 0x818], rax
0x001CF927: mov qword ptr [rdi + 0x820], rax
0x001CF92E: mov qword ptr [rdi + 0x828], rax
0x001CF935: mov rcx, rbx
0x001CF938: call 0x140391b24
0x001CF93D: test eax, eax
0x001CF93F: je 0x1401cf949
0x001CF941: mov ecx, eax
0x001CF943: call 0x14039219c
0x001CF948: nop
0x001CF949: lea rdx, [rsp + 0xb0]
0x001CF951: mov rcx, rdi
0x001CF954: call 0x140084a60
0x001CF959: xor cl, cl
0x001CF95B: mov eax, dword ptr [r14 + 0x18]
0x001CF95F: mov edx, dword ptr [rdi + 0x830]
0x001CF965: cmp eax, edx
0x001CF967: je 0x1401cf99e
0x001CF969: test eax, eax
0x001CF96B: js 0x1401cf98b
0x001CF96D: cmp eax, 1
0x001CF970: jle 0x1401cf983
0x001CF972: cmp eax, 3
0x001CF975: jle 0x1401cf98b
0x001CF977: cmp eax, 4
0x001CF97A: jne 0x1401cf98b
0x001CF97C: cmp edx, eax
0x001CF97E: setne al
0x001CF981: jmp 0x1401cf98d
0x001CF983: cmp edx, 1
0x001CF986: seta al
0x001CF989: jmp 0x1401cf98d
0x001CF98B: mov al, 1
0x001CF98D: movzx ecx, al
0x001CF990: mov eax, 1
0x001CF995: cmp edx, 0x3e8
0x001CF99B: cmove ecx, eax
0x001CF99E: cmp dword ptr [rsp + 0xdc], 0
0x001CF9A6: jg 0x1401cf9b1
0x001CF9A8: test cl, cl
0x001CF9AA: jne 0x1401cf9b1
0x001CF9AC: xor r15d, r15d
0x001CF9AF: jmp 0x1401cfa03
0x001CF9B1: mov rcx, rbx
0x001CF9B4: call 0x140391ac4
0x001CF9B9: test eax, eax
0x001CF9BB: je 0x1401cf9c4
0x001CF9BD: mov ecx, eax
0x001CF9BF: call 0x14039219c
0x001CF9C4: mov rsi, qword ptr [rdi + 0x838]
0x001CF9CB: xor r15d, r15d
0x001CF9CE: mov qword ptr [rdi + 0x838], r15
0x001CF9D5: test rsi, rsi
0x001CF9D8: je 0x1401cf9ef
0x001CF9DA: mov rcx, rsi
0x001CF9DD: call 0x1401ed8b0
0x001CF9E2: lea edx, [r15 + 0x38]
0x001CF9E6: mov rcx, rsi
0x001CF9E9: call 0x1403b20dc
0x001CF9EE: nop
0x001CF9EF: mov rcx, rbx
0x001CF9F2: call 0x140391b24
0x001CF9F7: test eax, eax
0x001CF9F9: je 0x1401cfa03
0x001CF9FB: mov ecx, eax
0x001CF9FD: call 0x14039219c
0x001CFA02: nop
0x001CFA03: lea rsi, [rdi + 0x838]
0x001CFA0A: cmp qword ptr [rsi], 0
0x001CFA0E: jne 0x1401cfb1b
0x001CFA14: mov qword ptr [rsp + 0x98], rbx
0x001CFA1C: mov rcx, rbx
0x001CFA1F: call 0x140391ac4
0x001CFA24: test eax, eax
0x001CFA26: je 0x1401cfa30
0x001CFA28: mov ecx, eax
0x001CFA2A: call 0x14039219c
0x001CFA2F: nop
0x001CFA30: mov eax, dword ptr [rdi + 0x98]
0x001CFA36: mov dword ptr [rsp + 0x44], eax
0x001CFA3A: mov qword ptr [rsp + 0x50], rdi
0x001CFA3F: lea r8, [rsp + 0x44]
0x001CFA44: lea rdx, [rsp + 0x50]
0x001CFA49: lea rcx, [rsp + 0x58]
0x001CFA4E: call 0x1401cd970
0x001CFA53: cmp rsi, rax
0x001CFA56: je 0x1401cfa7e
0x001CFA58: mov rdx, qword ptr [rax]
0x001CFA5B: mov qword ptr [rax], r15
0x001CFA5E: mov r12, qword ptr [rsi]
0x001CFA61: mov qword ptr [rsi], rdx
0x001CFA64: test r12, r12
0x001CFA67: je 0x1401cfa7e
0x001CFA69: mov rcx, r12
0x001CFA6C: call 0x1401ed8b0
0x001CFA71: mov edx, 0x38
0x001CFA76: mov rcx, r12
0x001CFA79: call 0x1403b20dc
0x001CFA7E: mov r12, qword ptr [rsp + 0x58]
0x001CFA83: test r12, r12
0x001CFA86: je 0x1401cfa9e
0x001CFA88: mov rcx, r12
0x001CFA8B: call 0x1401ed8b0
0x001CFA90: mov edx, 0x38
0x001CFA95: mov rcx, r12
0x001CFA98: call 0x1403b20dc
0x001CFA9D: nop
0x001CFA9E: mov rcx, rbx
0x001CFAA1: call 0x140391b24
0x001CFAA6: test eax, eax
0x001CFAA8: je 0x1401cfab2
0x001CFAAA: mov ecx, eax
0x001CFAAC: call 0x14039219c
0x001CFAB1: nop
0x001CFAB2: mov edx, dword ptr [r14 + 0x18]
0x001CFAB6: mov rcx, qword ptr [r14 + 0x10]
0x001CFABA: call 0x140159b40
0x001CFABF: movsxd rcx, dword ptr [rdi + 0x98]
0x001CFAC6: imul rdx, rcx, 0xa8
0x001CFACD: add rdx, qword ptr [rip + 0x616934]
0x001CFAD4: mov r9d, dword ptr [rsp + 0xe0]
0x001CFADC: cmp dword ptr [rsp + 0xdc], 0
0x001CFAE4: cmovg r9d, r15d
0x001CFAE8: mov r8d, dword ptr [r14 + 0x18]
0x001CFAEC: mov dword ptr [rsp + 0x30], r8d
0x001CFAF1: mov dword ptr [rsp + 0x28], r9d
0x001CFAF6: mov dword ptr [rsp + 0x20], eax
0x001CFAFA: movzx r9d, byte ptr [rsp + 0xd5]
0x001CFB03: mov r8d, dword ptr [rsp + 0xd0]
0x001CFB0B: mov edx, dword ptr [rdx + 0x10]
0x001CFB0E: mov rcx, qword ptr [rsi]
0x001CFB11: call 0x1401eff00
0x001CFB16: mov r12, qword ptr [rsp + 0x48]
0x001CFB1B: mov r8d, dword ptr [rsp + 0xe4]
0x001CFB23: mov rdx, r14
0x001CFB26: mov rcx, qword ptr [rsi]
0x001CFB29: call 0x1401f0140
0x001CFB2E: test al, al
0x001CFB30: jne 0x1401cfe53
0x001CFB36: mov dword ptr [rsp + 0x1b0], 0x1c
0x001CFB41: mov eax, dword ptr [rsp + 0x1b0]
0x001CFB48: xor eax, 0x55
0x001CFB4B: add eax, 7
0x001CFB4E: mov byte ptr [rsp + 0x1b4], al
0x001CFB55: movsx ecx, byte ptr [rsp + 0x1b4]
0x001CFB5D: xor ecx, 0x6e
0x001CFB60: add ecx, 7
0x001CFB63: mov byte ptr [rsp + 0x1b5], cl
0x001CFB6A: movsx ecx, byte ptr [rsp + 0x1b5]
0x001CFB72: xor ecx, 0x61
0x001CFB75: add ecx, 7
0x001CFB78: mov byte ptr [rsp + 0x1b6], cl
0x001CFB7F: movsx ecx, byte ptr [rsp + 0x1b6]
0x001CFB87: xor ecx, 0x62
0x001CFB8A: add ecx, 7
0x001CFB8D: mov byte ptr [rsp + 0x1b7], cl
0x001CFB94: movsx ecx, byte ptr [rsp + 0x1b7]
0x001CFB9C: xor ecx, 0x6c
0x001CFB9F: add ecx, 7
0x001CFBA2: mov byte ptr [rsp + 0x1b8], cl
0x001CFBA9: movsx ecx, byte ptr [rsp + 0x1b8]
0x001CFBB1: xor ecx, 0x65
0x001CFBB4: add ecx, 7
0x001CFBB7: mov byte ptr [rsp + 0x1b9], cl
0x001CFBBE: movsx ecx, byte ptr [rsp + 0x1b9]
0x001CFBC6: xor ecx, 0x20
0x001CFBC9: add ecx, 7
0x001CFBCC: mov byte ptr [rsp + 0x1ba], cl
0x001CFBD3: movsx ecx, byte ptr [rsp + 0x1ba]
0x001CFBDB: xor ecx, 0x74
0x001CFBDE: add ecx, 7
0x001CFBE1: mov byte ptr [rsp + 0x1bb], cl
0x001CFBE8: movsx ecx, byte ptr [rsp + 0x1bb]
0x001CFBF0: xor ecx, 0x6f
0x001CFBF3: add ecx, 7
0x001CFBF6: mov byte ptr [rsp + 0x1bc], cl
0x001CFBFD: movsx ecx, byte ptr [rsp + 0x1bc]
0x001CFC05: xor ecx, 0x20
0x001CFC08: add ecx, 7
0x001CFC0B: mov byte ptr [rsp + 0x1bd], cl
0x001CFC12: movsx ecx, byte ptr [rsp + 0x1bd]
0x001CFC1A: xor ecx, 0x69
0x001CFC1D: add ecx, 7
0x001CFC20: mov byte ptr [rsp + 0x1be], cl
0x001CFC27: movsx ecx, byte ptr [rsp + 0x1be]
0x001CFC2F: xor ecx, 0x6e
0x001CFC32: add ecx, 7
0x001CFC35: mov byte ptr [rsp + 0x1bf], cl
0x001CFC3C: movsx ecx, byte ptr [rsp + 0x1bf]
0x001CFC44: xor ecx, 0x69
0x001CFC47: add ecx, 7
0x001CFC4A: mov byte ptr [rsp + 0x1c0], cl
0x001CFC51: movsx ecx, byte ptr [rsp + 0x1c0]
0x001CFC59: xor ecx, 0x74
0x001CFC5C: add ecx, 7
0x001CFC5F: mov byte ptr [rsp + 0x1c1], cl
0x001CFC66: movsx ecx, byte ptr [rsp + 0x1c1]
0x001CFC6E: xor ecx, 0x69
0x001CFC71: add ecx, 7
0x001CFC74: mov byte ptr [rsp + 0x1c2], cl
0x001CFC7B: movsx ecx, byte ptr [rsp + 0x1c2]
0x001CFC83: xor ecx, 0x61
0x001CFC86: add ecx, 7
0x001CFC89: mov byte ptr [rsp + 0x1c3], cl
0x001CFC90: movsx ecx, byte ptr [rsp + 0x1c3]
0x001CFC98: xor ecx, 0x6c
0x001CFC9B: add ecx, 7
0x001CFC9E: mov byte ptr [rsp + 0x1c4], cl
0x001CFCA5: movsx ecx, byte ptr [rsp + 0x1c4]
0x001CFCAD: xor ecx, 0x69
0x001CFCB0: add ecx, 7
0x001CFCB3: mov byte ptr [rsp + 0x1c5], cl
0x001CFCBA: movsx ecx, byte ptr [rsp + 0x1c5]
0x001CFCC2: xor ecx, 0x7a
0x001CFCC5: add ecx, 7
0x001CFCC8: mov byte ptr [rsp + 0x1c6], cl
0x001CFCCF: movsx ecx, byte ptr [rsp + 0x1c6]
0x001CFCD7: xor ecx, 0x65
0x001CFCDA: add ecx, 7
0x001CFCDD: mov byte ptr [rsp + 0x1c7], cl
0x001CFCE4: movsx ecx, byte ptr [rsp + 0x1c7]
0x001CFCEC: xor ecx, 0x20
0x001CFCEF: add ecx, 7
0x001CFCF2: mov byte ptr [rsp + 0x1c8], cl
0x001CFCF9: movsx ecx, byte ptr [rsp + 0x1c8]
0x001CFD01: xor ecx, 0x43
0x001CFD04: add ecx, 7
0x001CFD07: mov byte ptr [rsp + 0x1c9], cl
0x001CFD0E: movsx ecx, byte ptr [rsp + 0x1c9]
0x001CFD16: xor ecx, 0x55
0x001CFD19: add ecx, 7
0x001CFD1C: mov byte ptr [rsp + 0x1ca], cl
0x001CFD23: movsx ecx, byte ptr [rsp + 0x1ca]
0x001CFD2B: xor ecx, 0x44
0x001CFD2E: add ecx, 7
0x001CFD31: mov byte ptr [rsp + 0x1cb], cl
0x001CFD38: movsx ecx, byte ptr [rsp + 0x1cb]
0x001CFD40: xor ecx, 0x41
0x001CFD43: add ecx, 7
0x001CFD46: mov byte ptr [rsp + 0x1cc], cl
0x001CFD4D: movsx ecx, byte ptr [rsp + 0x1cc]
0x001CFD55: xor ecx, 0x20
0x001CFD58: add ecx, 7
0x001CFD5B: mov byte ptr [rsp + 0x1cd], cl
0x001CFD62: movsx ecx, byte ptr [rsp + 0x1cd]
0x001CFD6A: xor ecx, 0x6d
0x001CFD6D: add ecx, 7
0x001CFD70: mov byte ptr [rsp + 0x1ce], cl
0x001CFD77: movsx ecx, byte ptr [rsp + 0x1ce]
0x001CFD7F: xor ecx, 0x69
0x001CFD82: add ecx, 7
0x001CFD85: mov byte ptr [rsp + 0x1cf], cl
0x001CFD8C: movsx ecx, byte ptr [rsp + 0x1cf]
0x001CFD94: xor ecx, 0x6e
0x001CFD97: add ecx, 7
0x001CFD9A: mov byte ptr [rsp + 0x1d0], cl
0x001CFDA1: movsx ecx, byte ptr [rsp + 0x1d0]
0x001CFDA9: xor ecx, 0x65
0x001CFDAC: add ecx, 7
0x001CFDAF: mov byte ptr [rsp + 0x1d1], cl
0x001CFDB6: movsx ecx, byte ptr [rsp + 0x1d1]
0x001CFDBE: xor ecx, 0x72
0x001CFDC1: add ecx, 7
0x001CFDC4: mov byte ptr [rsp + 0x1d2], cl
0x001CFDCB: mov byte ptr [rsp + 0x1d3], 0
0x001CFDD3: movzx eax, byte ptr [rsp + 0x1b4]
0x001CFDDB: lea rdx, [rsp + 0x1f8]
0x001CFDE3: lea rcx, [rsp + 0x1b0]
0x001CFDEB: call 0x1401d0e50
0x001CFDF0: nop
0x001CFDF1: cmp qword ptr [rax + 0x18], 0x10
0x001CFDF6: jb 0x1401cfdfb
0x001CFDF8: mov rax, qword ptr [rax]
0x001CFDFB: lea rcx, [rip + 0x263b6e]
0x001CFE02: mov qword ptr [rsp + 0x68], rcx
0x001CFE07: xor ecx, ecx
0x001CFE09: mov qword ptr [rsp + 0x70], rcx
0x001CFE0E: mov qword ptr [rsp + 0x78], rcx
0x001CFE13: mov qword ptr [rsp + 0x80], rax
0x001CFE1B: mov byte ptr [rsp + 0x88], 1
0x001CFE23: lea rdx, [rsp + 0x70]
0x001CFE28: lea rcx, [rsp + 0x80]
0x001CFE30: call 0x1403d23c8
0x001CFE35: lea rax, [rip + 0x263b4c]
0x001CFE3C: mov qword ptr [rsp + 0x68], rax
0x001CFE41: lea rdx, [rip + 0x5bb118]
0x001CFE48: lea rcx, [rsp + 0x68]
0x001CFE4D: call 0x1403d25d0
0x001CFE52: nop
0x001CFE53: mov rcx, rbx
0x001CFE56: call 0x140391ac4
0x001CFE5B: test eax, eax
0x001CFE5D: je 0x1401cfe66
0x001CFE5F: mov ecx, eax
0x001CFE61: call 0x14039219c
0x001CFE66: movups xmm0, xmmword ptr [r12]
0x001CFE6B: movups xmmword ptr [rdi + 0x810], xmm0
0x001CFE72: movups xmm1, xmmword ptr [r12 + 0x10]
0x001CFE78: movups xmmword ptr [rdi + 0x820], xmm1
0x001CFE7F: mov eax, dword ptr [r14 + 0x18]
0x001CFE83: mov dword ptr [rdi + 0x830], eax
0x001CFE89: mov rcx, rbx
0x001CFE8C: call 0x140391b24
0x001CFE91: test eax, eax
0x001CFE93: je 0x1401cfe9d
0x001CFE95: mov ecx, eax
0x001CFE97: call 0x14039219c
0x001CFE9C: nop
0x001CFE9D: mov rcx, qword ptr [rsp + 0x218]
0x001CFEA5: xor rcx, rsp
0x001CFEA8: call 0x1403b24c0
0x001CFEAD: mov rbx, qword ptr [rsp + 0x258]
0x001CFEB5: add rsp, 0x220
0x001CFEBC: pop r15
0x001CFEBE: pop r14
0x001CFEC0: pop r12
0x001CFEC2: pop rdi
0x001CFEC3: pop rsi
0x001CFEC4: ret
```