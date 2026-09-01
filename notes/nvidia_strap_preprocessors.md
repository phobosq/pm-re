# NVIDIA strap preprocessors 0x1D97E0 / 0x1D7930

Called by child vtable slot +0x80 immediately before RegisterOp-backed apply.

## target `0x001D97E0` PDATA `0x001D9490..0x001D97A5`

### Calls

| RVA | target/form |
|---|---|
| `0x001D94DC` | `qword ptr [rip + 0x60e37e]` |
| `0x001D94EF` | `qword ptr [rip + 0x60e363]` |
| `0x001D9689` | `RVA 0x001EC910` |
| `0x001D969A` | `RVA 0x0012DA50` |
| `0x001D96B5` | `RVA 0x001D4140` |
| `0x001D96D9` | `RVA 0x003DB020` |
| `0x001D96E8` | `RVA 0x003DB020` |
| `0x001D96F7` | `RVA 0x003DB020` |
| `0x001D9703` | `RVA 0x003DB020` |
| `0x001D970C` | `RVA 0x003B20D4` |
| `0x001D9743` | `RVA 0x003DB020` |
| `0x001D9752` | `RVA 0x003DB020` |
| `0x001D9761` | `RVA 0x003DB020` |
| `0x001D976D` | `RVA 0x003DB020` |
| `0x001D9776` | `RVA 0x003B20D4` |
| `0x001D978F` | `RVA 0x003B24C0` |

### Object/struct accesses

| RVA | base | disp | instruction |
|---|---|---:|---|
| `0x001D94BF` | `rcx` | `0xC8` | `mov rcx, qword ptr [rcx + 0xc8]` |
| `0x001D968F` | `rbx` | `0x8` | `lea rdx, [rbx + 8]` |
| `0x001D96A0` | `rax` | `0x18` | `cmp qword ptr [rax + 0x18], 0x10` |
| `0x001D96A7` | `rax` | `0x0` | `mov rax, qword ptr [rax]` |

### Full body

```asm
0x001D9490: push rbp
0x001D9492: lea rbp, [rsp - 0x57]
0x001D9497: sub rsp, 0xb0
0x001D949E: mov qword ptr [rbp - 0x29], 0xfffffffffffffffe
0x001D94A6: mov qword ptr [rsp + 0xc8], rbx
0x001D94AE: mov rax, qword ptr [rip + 0x5fd43b]
0x001D94B5: xor rax, rsp
0x001D94B8: mov qword ptr [rbp + 0x4f], rax
0x001D94BC: mov rbx, rcx
0x001D94BF: mov rcx, qword ptr [rcx + 0xc8]
0x001D94C6: test rcx, rcx
0x001D94C9: je 0x1401d9785
0x001D94CF: mov dword ptr [rbp - 0x39], 0xffffffff
0x001D94D6: lea r8, [rbp - 0x39]
0x001D94DA: xor edx, edx
0x001D94DC: call qword ptr [rip + 0x60e37e]
0x001D94E2: mov dword ptr [rbp - 0x35], eax
0x001D94E5: test eax, eax
0x001D94E7: je 0x1401d977d
0x001D94ED: mov ecx, eax
0x001D94EF: call qword ptr [rip + 0x60e363]
0x001D94F5: mov qword ptr [rbp - 0x31], rax
0x001D94F9: mov dword ptr [rbp - 0x21], 0x23
0x001D9500: mov dword ptr [rbp - 0x1d], 0x52
0x001D9507: mov eax, dword ptr [rbp - 0x1d]
0x001D950A: xor eax, 0x19
0x001D950D: mov byte ptr [rbp - 0x19], al
0x001D9510: movsx ecx, byte ptr [rbp - 0x19]
0x001D9514: xor ecx, 3
0x001D9517: mov byte ptr [rbp - 0x18], cl
0x001D951A: movsx ecx, byte ptr [rbp - 0x18]
0x001D951E: xor ecx, 0x56
0x001D9521: mov byte ptr [rbp - 0x17], cl
0x001D9524: movsx ecx, byte ptr [rbp - 0x17]
0x001D9528: xor ecx, 0x4d
0x001D952B: mov byte ptr [rbp - 0x16], cl
0x001D952E: movsx ecx, byte ptr [rbp - 0x16]
0x001D9532: xor ecx, 0x42
0x001D9535: mov byte ptr [rbp - 0x15], cl
0x001D9538: movsx ecx, byte ptr [rbp - 0x15]
0x001D953C: xor ecx, 0x41
0x001D953F: mov byte ptr [rbp - 0x14], cl
0x001D9542: movsx ecx, byte ptr [rbp - 0x14]
0x001D9546: xor ecx, 0x4f
0x001D9549: mov byte ptr [rbp - 0x13], cl
0x001D954C: movsx ecx, byte ptr [rbp - 0x13]
0x001D9550: xor ecx, 0x46
0x001D9553: mov byte ptr [rbp - 0x12], cl
0x001D9556: movsx ecx, byte ptr [rbp - 0x12]
0x001D955A: xor ecx, 3
0x001D955D: mov byte ptr [rbp - 0x11], cl
0x001D9560: movsx ecx, byte ptr [rbp - 0x11]
0x001D9564: xor ecx, 0x57
0x001D9567: mov byte ptr [rbp - 0x10], cl
0x001D956A: movsx ecx, byte ptr [rbp - 0x10]
0x001D956E: xor ecx, 0x4c
0x001D9571: mov byte ptr [rbp - 0xf], cl
0x001D9574: movsx ecx, byte ptr [rbp - 0xf]
0x001D9578: xor ecx, 3
0x001D957B: mov byte ptr [rbp - 0xe], cl
0x001D957E: movsx ecx, byte ptr [rbp - 0xe]
0x001D9582: xor ecx, 0x44
0x001D9585: mov byte ptr [rbp - 0xd], cl
0x001D9588: movsx ecx, byte ptr [rbp - 0xd]
0x001D958C: xor ecx, 0x46
0x001D958F: mov byte ptr [rbp - 0xc], cl
0x001D9592: movsx ecx, byte ptr [rbp - 0xc]
0x001D9596: xor ecx, 0x57
0x001D9599: mov byte ptr [rbp - 0xb], cl
0x001D959C: movsx ecx, byte ptr [rbp - 0xb]
0x001D95A0: xor ecx, 3
0x001D95A3: mov byte ptr [rbp - 0xa], cl
0x001D95A6: movsx ecx, byte ptr [rbp - 0xa]
0x001D95AA: xor ecx, 0x57
0x001D95AD: mov byte ptr [rbp - 9], cl
0x001D95B0: movsx ecx, byte ptr [rbp - 9]
0x001D95B4: xor ecx, 0x46
0x001D95B7: mov byte ptr [rbp - 8], cl
0x001D95BA: movsx ecx, byte ptr [rbp - 8]
0x001D95BE: xor ecx, 0x4e
0x001D95C1: mov byte ptr [rbp - 7], cl
0x001D95C4: movsx ecx, byte ptr [rbp - 7]
0x001D95C8: xor ecx, 0x53
0x001D95CB: mov byte ptr [rbp - 6], cl
0x001D95CE: movsx ecx, byte ptr [rbp - 6]
0x001D95D2: xor ecx, 0x46
0x001D95D5: mov byte ptr [rbp - 5], cl
0x001D95D8: movsx ecx, byte ptr [rbp - 5]
0x001D95DC: xor ecx, 0x51
0x001D95DF: mov byte ptr [rbp - 4], cl
0x001D95E2: movsx ecx, byte ptr [rbp - 4]
0x001D95E6: xor ecx, 0x42
0x001D95E9: mov byte ptr [rbp - 3], cl
0x001D95EC: movsx ecx, byte ptr [rbp - 3]
0x001D95F0: xor ecx, 0x57
0x001D95F3: mov byte ptr [rbp - 2], cl
0x001D95F6: movsx ecx, byte ptr [rbp - 2]
0x001D95FA: xor ecx, 0x56
0x001D95FD: mov byte ptr [rbp - 1], cl
0x001D9600: movsx ecx, byte ptr [rbp - 1]
0x001D9604: xor ecx, 0x51
0x001D9607: mov byte ptr [rbp], cl
0x001D960A: movsx ecx, byte ptr [rbp]
0x001D960E: xor ecx, 0x46
0x001D9611: mov byte ptr [rbp + 1], cl
0x001D9614: movsx ecx, byte ptr [rbp + 1]
0x001D9618: xor ecx, 3
0x001D961B: mov byte ptr [rbp + 2], cl
0x001D961E: movsx ecx, byte ptr [rbp + 2]
0x001D9622: xor ecx, 0xe
0x001D9625: mov byte ptr [rbp + 3], cl
0x001D9628: movsx ecx, byte ptr [rbp + 3]
0x001D962C: xor ecx, 3
0x001D962F: mov byte ptr [rbp + 4], cl
0x001D9632: movsx ecx, byte ptr [rbp + 4]
0x001D9636: xor ecx, 0x58
0x001D9639: mov byte ptr [rbp + 5], cl
0x001D963C: movsx ecx, byte ptr [rbp + 5]
0x001D9640: xor ecx, 0x5e
0x001D9643: mov byte ptr [rbp + 6], cl
0x001D9646: movsx ecx, byte ptr [rbp + 6]
0x001D964A: xor ecx, 3
0x001D964D: mov byte ptr [rbp + 7], cl
0x001D9650: movsx ecx, byte ptr [rbp + 7]
0x001D9654: xor ecx, 0xb
0x001D9657: mov byte ptr [rbp + 8], cl
0x001D965A: movsx ecx, byte ptr [rbp + 8]
0x001D965E: xor ecx, 0x58
0x001D9661: mov byte ptr [rbp + 9], cl
0x001D9664: movsx ecx, byte ptr [rbp + 9]
0x001D9668: xor ecx, 0x5e
0x001D966B: mov byte ptr [rbp + 0xa], cl
0x001D966E: movsx ecx, byte ptr [rbp + 0xa]
0x001D9672: xor ecx, 0xa
0x001D9675: mov byte ptr [rbp + 0xb], cl
0x001D9678: xor eax, eax
0x001D967A: mov byte ptr [rbp + 0xc], al
0x001D967D: movzx eax, byte ptr [rbp - 0x19]
0x001D9681: lea rdx, [rbp + 0x2f]
0x001D9685: lea rcx, [rbp - 0x21]
0x001D9689: call 0x1401ec910
0x001D968E: nop
0x001D968F: lea rdx, [rbx + 8]
0x001D9693: mov r8, rax
0x001D9696: lea rcx, [rbp + 0xf]
0x001D969A: call 0x14012da50
0x001D969F: nop
0x001D96A0: cmp qword ptr [rax + 0x18], 0x10
0x001D96A5: jb 0x1401d96aa
0x001D96A7: mov rax, qword ptr [rax]
0x001D96AA: lea r8, [rbp - 0x35]
0x001D96AE: lea rdx, [rbp - 0x31]
0x001D96B2: mov rcx, rax
0x001D96B5: call 0x1401d4140
0x001D96BA: nop
0x001D96BB: mov rax, qword ptr [rbp + 0x27]
0x001D96BF: cmp rax, 0x10
0x001D96C3: jb 0x1401d9711
0x001D96C5: inc rax
0x001D96C8: mov rcx, qword ptr [rbp + 0xf]
0x001D96CC: cmp rax, 0x1000
0x001D96D2: jb 0x1401d970c
0x001D96D4: test cl, 0x1f
0x001D96D7: je 0x1401d96df
0x001D96D9: call 0x1403db020
0x001D96DE: int3
0x001D96DF: mov rax, qword ptr [rcx - 8]
0x001D96E3: cmp rax, rcx
0x001D96E6: jb 0x1401d96ee
0x001D96E8: call 0x1403db020
0x001D96ED: int3
0x001D96EE: sub rcx, rax
0x001D96F1: cmp rcx, 8
0x001D96F5: jae 0x1401d96fd
0x001D96F7: call 0x1403db020
0x001D96FC: int3
0x001D96FD: cmp rcx, 0x27
0x001D9701: jbe 0x1401d9709
0x001D9703: call 0x1403db020
0x001D9708: int3
0x001D9709: mov rcx, rax
0x001D970C: call 0x1403b20d4
0x001D9711: mov qword ptr [rbp + 0x27], 0xf
0x001D9719: mov qword ptr [rbp + 0x1f], 0
0x001D9721: mov byte ptr [rbp + 0xf], 0
0x001D9725: mov rax, qword ptr [rbp + 0x47]
0x001D9729: cmp rax, 0x10
0x001D972D: jb 0x1401d9785
0x001D972F: inc rax
0x001D9732: mov rcx, qword ptr [rbp + 0x2f]
0x001D9736: cmp rax, 0x1000
0x001D973C: jb 0x1401d9776
0x001D973E: test cl, 0x1f
0x001D9741: je 0x1401d9749
0x001D9743: call 0x1403db020
0x001D9748: int3
0x001D9749: mov rax, qword ptr [rcx - 8]
0x001D974D: cmp rax, rcx
0x001D9750: jb 0x1401d9758
0x001D9752: call 0x1403db020
0x001D9757: int3
0x001D9758: sub rcx, rax
0x001D975B: cmp rcx, 8
0x001D975F: jae 0x1401d9767
0x001D9761: call 0x1403db020
0x001D9766: int3
0x001D9767: cmp rcx, 0x27
0x001D976B: jbe 0x1401d9773
0x001D976D: call 0x1403db020
0x001D9772: int3
0x001D9773: mov rcx, rax
0x001D9776: call 0x1403b20d4
0x001D977B: jmp 0x1401d9785
0x001D977D: mov eax, dword ptr [rbp - 0x39]
0x001D9780: cmp eax, -1
0x001D9783: jne 0x1401d9788
0x001D9785: or eax, 0xffffffff
0x001D9788: mov rcx, qword ptr [rbp + 0x4f]
0x001D978C: xor rcx, rsp
0x001D978F: call 0x1403b24c0
0x001D9794: mov rbx, qword ptr [rsp + 0xc8]
0x001D979C: add rsp, 0xb0
0x001D97A3: pop rbp
0x001D97A4: ret
```

## target `0x001D7930` PDATA `0x001D7930..0x001D9483`

### Calls

| RVA | target/form |
|---|---|
| `0x001D7A16` | `RVA 0x003D3050` |
| `0x001D7A6C` | `RVA 0x003D3050` |
| `0x001D7B3E` | `RVA 0x003D3050` |
| `0x001D7B5B` | `RVA 0x001D78B0` |
| `0x001D7DED` | `RVA 0x00206E40` |
| `0x001D7E0B` | `RVA 0x0012EE60` |
| `0x001D82D8` | `RVA 0x001269F0` |
| `0x001D8416` | `RVA 0x00036AD0` |
| `0x001D844E` | `RVA 0x0006F540` |
| `0x001D8489` | `RVA 0x000328E0` |
| `0x001D8495` | `RVA 0x00073470` |
| `0x001D84A2` | `RVA 0x00032DC0` |
| `0x001D84BC` | `RVA 0x00032EF0` |
| `0x001D84FB` | `RVA 0x001D97B0` |
| `0x001D8AD4` | `RVA 0x001372A0` |
| `0x001D8AFE` | `RVA 0x001D42C0` |
| `0x001D8B0B` | `RVA 0x00032EF0` |
| `0x001D8EF2` | `RVA 0x001EB3D0` |
| `0x001D8F10` | `RVA 0x0017B170` |
| `0x001D8F1D` | `RVA 0x00032EF0` |
| `0x001D91DD` | `RVA 0x001EBFA0` |
| `0x001D91F4` | `RVA 0x00040530` |
| `0x001D9426` | `RVA 0x001B62E0` |
| `0x001D943D` | `RVA 0x00040530` |
| `0x001D944A` | `RVA 0x00032EF0` |
| `0x001D945B` | `RVA 0x003B24C0` |

### Object/struct accesses

| RVA | base | disp | instruction |
|---|---|---:|---|
| `0x001D7957` | `rax` | `0x20` | `mov qword ptr [rax + 0x20], rbx` |
| `0x001D7986` | `rcx` | `0x398` | `cmp byte ptr [rcx + rax + 0x398], 0` |
| `0x001D7998` | `rcx` | `0x0` | `movups xmm0, xmmword ptr [rcx + rbx]` |
| `0x001D799C` | `rdx` | `0x0` | `movups xmmword ptr [rdx], xmm0` |
| `0x001D799F` | `rcx` | `0x10` | `movups xmm1, xmmword ptr [rcx + rbx + 0x10]` |
| `0x001D79A4` | `rdx` | `0x10` | `movups xmmword ptr [rdx + 0x10], xmm1` |
| `0x001D79A8` | `rcx` | `0x20` | `movups xmm0, xmmword ptr [rcx + rbx + 0x20]` |
| `0x001D79AD` | `rdx` | `0x20` | `movups xmmword ptr [rdx + 0x20], xmm0` |
| `0x001D79B1` | `rcx` | `0x30` | `movups xmm1, xmmword ptr [rcx + rbx + 0x30]` |
| `0x001D79B6` | `rdx` | `0x30` | `movups xmmword ptr [rdx + 0x30], xmm1` |
| `0x001D79BA` | `rcx` | `0x40` | `movups xmm0, xmmword ptr [rcx + rbx + 0x40]` |
| `0x001D79BF` | `rdx` | `0x40` | `movups xmmword ptr [rdx + 0x40], xmm0` |
| `0x001D79C3` | `rcx` | `0x50` | `movsd xmm1, qword ptr [rcx + rbx + 0x50]` |
| `0x001D79C9` | `rdx` | `0x50` | `movsd qword ptr [rdx + 0x50], xmm1` |
| `0x001D79CE` | `rcx` | `0x58` | `mov eax, dword ptr [rcx + rbx + 0x58]` |
| `0x001D79D2` | `rdx` | `0x58` | `mov dword ptr [rdx + 0x58], eax` |
| `0x001D79E6` | `rcx` | `0x3A0` | `mov eax, dword ptr [rcx + 0x3a0]` |
| `0x001D79F3` | `rsi` | `0x0` | `cmp dword ptr [rsi], eax` |
| `0x001D79F7` | `rsi` | `0x4` | `cmp dword ptr [rsi + 4], 8` |
| `0x001D7A0E` | `rdx` | `0x5C` | `lea r8d, [rdx + 0x5c]` |
| `0x001D7A1B` | `rsi` | `0x10` | `mov r12d, dword ptr [rsi + 0x10]` |
| `0x001D7A23` | `rsi` | `0xC` | `mov r15d, dword ptr [rsi + 0xc]` |
| `0x001D7A2B` | `rsi` | `0x8` | `mov r14d, dword ptr [rsi + 8]` |
| `0x001D7A33` | `rsi` | `0x14` | `mov esi, dword ptr [rsi + 0x14]` |
| `0x001D7A39` | `rbx` | `0x3A0` | `mov eax, dword ptr [rbx + 0x3a0]` |
| `0x001D7A46` | `rdi` | `0x0` | `cmp dword ptr [rdi], eax` |
| `0x001D7A4A` | `rdi` | `0x4` | `cmp dword ptr [rdi + 4], 9` |
| `0x001D7A61` | `rdx` | `0x5C` | `lea r8d, [rdx + 0x5c]` |
| `0x001D7A71` | `rdi` | `0x10` | `mov ecx, dword ptr [rdi + 0x10]` |
| `0x001D7A7E` | `rdi` | `0xC` | `mov edx, dword ptr [rdi + 0xc]` |
| `0x001D7A8B` | `rdi` | `0x8` | `mov r8d, dword ptr [rdi + 8]` |
| `0x001D7A9B` | `rdi` | `0x14` | `mov eax, dword ptr [rdi + 0x14]` |
| `0x001D7AB1` | `rdi` | `0x188` | `mov r9d, dword ptr [rdi + rbx + 0x188]` |
| `0x001D7AC9` | `rdi` | `0x17C` | `mov r9d, dword ptr [rdi + rbx + 0x17c]` |
| `0x001D7AE1` | `rdi` | `0x170` | `mov r9d, dword ptr [rdi + rbx + 0x170]` |
| `0x001D7AF9` | `rdi` | `0x14C` | `mov r9d, dword ptr [rdi + rbx + 0x14c]` |
| `0x001D7B35` | `rdx` | `0x5C` | `lea r8d, [rdx + 0x5c]` |
| `0x001D7B43` | `rbx` | `0x258` | `mov r8d, dword ptr [rbx + 0x258]` |
| `0x001D7DF3` | `rax` | `0x18` | `cmp qword ptr [rax + 0x18], 0x10` |
| `0x001D7DFA` | `rax` | `0x0` | `mov rax, qword ptr [rax]` |
| `0x001D7DFD` | `rbx` | `0x8` | `lea rdx, [rbx + 8]` |
| `0x001D7E01` | `rbx` | `0x258` | `lea r8, [rbx + 0x258]` |
| `0x001D82E0` | `rax` | `0x18` | `cmp qword ptr [rax + 0x18], 0x10` |
| `0x001D82E7` | `rax` | `0x0` | `mov rdx, qword ptr [rax]` |
| `0x001D833E` | `rbx` | `0x20` | `cmp qword ptr [rbx + 0x20], 0x10` |
| `0x001D8345` | `rbx` | `0x8` | `mov rcx, qword ptr [rbx + 8]` |
| `0x001D834B` | `rbx` | `0x8` | `lea rcx, [rbx + 8]` |
| `0x001D8356` | `rbx` | `0x18` | `mov rax, qword ptr [rbx + 0x18]` |
| `0x001D837B` | `rbx` | `0x258` | `mov eax, dword ptr [rbx + 0x258]` |
| `0x001D8510` | `rbx` | `0x260` | `mov ecx, dword ptr [rbx + 0x260]` |
| `0x001D8551` | `rbx` | `0x264` | `mov ecx, dword ptr [rbx + 0x264]` |
| `0x001D8592` | `rbx` | `0x268` | `lea rsi, [rbx + 0x268]` |
| `0x001D8599` | `rsi` | `0x0` | `mov ecx, dword ptr [rsi]` |
| `0x001D8ADA` | `rax` | `0x18` | `cmp qword ptr [rax + 0x18], 0x10` |
| `0x001D8AE1` | `rax` | `0x0` | `mov rax, qword ptr [rax]` |
| `0x001D8AE4` | `rbx` | `0x8` | `lea rdx, [rbx + 8]` |
| `0x001D8AED` | `rbx` | `0x264` | `lea r9, [rbx + 0x264]` |
| `0x001D8AF4` | `rbx` | `0x260` | `lea r8, [rbx + 0x260]` |
| `0x001D8B1F` | `rbx` | `0x25C` | `mov edx, dword ptr [rbx + 0x25c]` |
| `0x001D8EF8` | `rax` | `0x18` | `cmp qword ptr [rax + 0x18], 0x10` |
| `0x001D8EFF` | `rax` | `0x0` | `mov rax, qword ptr [rax]` |
| `0x001D8F02` | `rbx` | `0x8` | `lea rdx, [rbx + 8]` |
| `0x001D8F06` | `rbx` | `0x25C` | `lea r8, [rbx + 0x25c]` |
| `0x001D8F22` | `rdi` | `0x144` | `cmp dword ptr [rdi + rbx + 0x144], 0` |
| `0x001D8F32` | `rdi` | `0x188` | `mov eax, dword ptr [rdi + rbx + 0x188]` |
| `0x001D8F42` | `rdi` | `0x17C` | `mov eax, dword ptr [rdi + rbx + 0x17c]` |
| `0x001D8F52` | `rdi` | `0x170` | `mov eax, dword ptr [rdi + rbx + 0x170]` |
| `0x001D8F63` | `rdi` | `0x14C` | `mov eax, dword ptr [rdi + rbx + 0x14c]` |
| `0x001D8F73` | `r13` | `0x0` | `movups xmmword ptr [r13], xmm6` |
| `0x001D8F7C` | `r13` | `0x10` | `movups xmmword ptr [r13 + 0x10], xmm5` |
| `0x001D8F85` | `r13` | `0x20` | `movups xmmword ptr [r13 + 0x20], xmm4` |
| `0x001D8F8E` | `r13` | `0x30` | `movups xmmword ptr [r13 + 0x30], xmm3` |
| `0x001D8F97` | `r13` | `0x40` | `movups xmmword ptr [r13 + 0x40], xmm2` |
| `0x001D8FA1` | `r13` | `0x50` | `movsd qword ptr [r13 + 0x50], xmm1` |
| `0x001D8FAA` | `r13` | `0x58` | `mov dword ptr [r13 + 0x58], edx` |
| `0x001D8FBE` | `rcx` | `0x0` | `movups xmmword ptr [rcx + rbx], xmm6` |
| `0x001D8FC2` | `rcx` | `0x10` | `movups xmmword ptr [rcx + rbx + 0x10], xmm5` |
| `0x001D8FC7` | `rcx` | `0x20` | `movups xmmword ptr [rcx + rbx + 0x20], xmm4` |
| `0x001D8FCC` | `rcx` | `0x30` | `movups xmmword ptr [rcx + rbx + 0x30], xmm3` |
| `0x001D8FD1` | `rcx` | `0x40` | `movups xmmword ptr [rcx + rbx + 0x40], xmm2` |
| `0x001D8FD6` | `rcx` | `0x50` | `movsd qword ptr [rcx + rbx + 0x50], xmm1` |
| `0x001D8FDC` | `rcx` | `0x58` | `mov dword ptr [rcx + rbx + 0x58], edx` |
| `0x001D8FE0` | `rbx` | `0x398` | `mov byte ptr [rbx + r8 + 0x398], 1` |
| `0x001D91E3` | `rax` | `0x18` | `cmp qword ptr [rax + 0x18], 0x10` |
| `0x001D91EA` | `rax` | `0x0` | `mov rax, qword ptr [rax]` |
| `0x001D91ED` | `rbx` | `0x8` | `lea rdx, [rbx + 8]` |
| `0x001D942C` | `rax` | `0x18` | `cmp qword ptr [rax + 0x18], 0x10` |
| `0x001D9433` | `rax` | `0x0` | `mov rax, qword ptr [rax]` |
| `0x001D9436` | `rbx` | `0x8` | `lea rdx, [rbx + 8]` |

### Full body

```asm
0x001D7930: mov rax, rsp
0x001D7933: push rbp
0x001D7934: push rsi
0x001D7935: push rdi
0x001D7936: push r12
0x001D7938: push r13
0x001D793A: push r14
0x001D793C: push r15
0x001D793E: lea rbp, [rax - 0x808]
0x001D7945: sub rsp, 0x8d0
0x001D794C: mov qword ptr [rbp + 0x80], 0xfffffffffffffffe
0x001D7957: mov qword ptr [rax + 0x20], rbx
0x001D795B: movaps xmmword ptr [rax - 0x48], xmm6
0x001D795F: mov rax, qword ptr [rip + 0x5fef8a]
0x001D7966: xor rax, rsp
0x001D7969: mov qword ptr [rbp + 0x7b0], rax
0x001D7970: movsxd rax, r8d
0x001D7973: mov dword ptr [rsp + 0x3c], eax
0x001D7977: mov r13, rdx
0x001D797A: mov rbx, rcx
0x001D797D: cmp eax, 2
0x001D7980: ja 0x1401d944f
0x001D7986: cmp byte ptr [rcx + rax + 0x398], 0
0x001D798E: je 0x1401d79dc
0x001D7990: add rax, 7
0x001D7994: imul rcx, rax, 0x5c
0x001D7998: movups xmm0, xmmword ptr [rcx + rbx]
0x001D799C: movups xmmword ptr [rdx], xmm0
0x001D799F: movups xmm1, xmmword ptr [rcx + rbx + 0x10]
0x001D79A4: movups xmmword ptr [rdx + 0x10], xmm1
0x001D79A8: movups xmm0, xmmword ptr [rcx + rbx + 0x20]
0x001D79AD: movups xmmword ptr [rdx + 0x20], xmm0
0x001D79B1: movups xmm1, xmmword ptr [rcx + rbx + 0x30]
0x001D79B6: movups xmmword ptr [rdx + 0x30], xmm1
0x001D79BA: movups xmm0, xmmword ptr [rcx + rbx + 0x40]
0x001D79BF: movups xmmword ptr [rdx + 0x40], xmm0
0x001D79C3: movsd xmm1, qword ptr [rcx + rbx + 0x50]
0x001D79C9: movsd qword ptr [rdx + 0x50], xmm1
0x001D79CE: mov eax, dword ptr [rcx + rbx + 0x58]
0x001D79D2: mov dword ptr [rdx + 0x58], eax
0x001D79D5: mov al, 1
0x001D79D7: jmp 0x1401d9451
0x001D79DC: lea rdi, [rip + 0x2e5ced]
0x001D79E3: mov rsi, rdi
0x001D79E6: mov eax, dword ptr [rcx + 0x3a0]
0x001D79EC: lea rcx, [rip + 0x2e5e5d]
0x001D79F3: cmp dword ptr [rsi], eax
0x001D79F5: jne 0x1401d79fd
0x001D79F7: cmp dword ptr [rsi + 4], 8
0x001D79FB: je 0x1401d7a0c
0x001D79FD: add rsi, 0x18
0x001D7A01: cmp rsi, rcx
0x001D7A04: je 0x1401d9206
0x001D7A0A: jmp 0x1401d79f3
0x001D7A0C: xor edx, edx
0x001D7A0E: lea r8d, [rdx + 0x5c]
0x001D7A12: lea rcx, [rbp + 0x20]
0x001D7A16: call 0x1403d3050
0x001D7A1B: mov r12d, dword ptr [rsi + 0x10]
0x001D7A1F: mov dword ptr [rbp + 0x4c], r12d
0x001D7A23: mov r15d, dword ptr [rsi + 0xc]
0x001D7A27: mov dword ptr [rbp + 0x58], r15d
0x001D7A2B: mov r14d, dword ptr [rsi + 8]
0x001D7A2F: mov dword ptr [rbp + 0x64], r14d
0x001D7A33: mov esi, dword ptr [rsi + 0x14]
0x001D7A36: mov dword ptr [rbp + 0x28], esi
0x001D7A39: mov eax, dword ptr [rbx + 0x3a0]
0x001D7A3F: lea rcx, [rip + 0x2e5e0a]
0x001D7A46: cmp dword ptr [rdi], eax
0x001D7A48: jne 0x1401d7a50
0x001D7A4A: cmp dword ptr [rdi + 4], 9
0x001D7A4E: je 0x1401d7a5f
0x001D7A50: add rdi, 0x18
0x001D7A54: cmp rdi, rcx
0x001D7A57: je 0x1401d9206
0x001D7A5D: jmp 0x1401d7a46
0x001D7A5F: xor edx, edx
0x001D7A61: lea r8d, [rdx + 0x5c]
0x001D7A65: lea rcx, [rbp + 0xa0]
0x001D7A6C: call 0x1403d3050
0x001D7A71: mov ecx, dword ptr [rdi + 0x10]
0x001D7A74: mov dword ptr [rsp + 0x38], ecx
0x001D7A78: mov dword ptr [rbp + 0xcc], ecx
0x001D7A7E: mov edx, dword ptr [rdi + 0xc]
0x001D7A81: mov dword ptr [rsp + 0x34], edx
0x001D7A85: mov dword ptr [rbp + 0xd8], edx
0x001D7A8B: mov r8d, dword ptr [rdi + 8]
0x001D7A8F: mov dword ptr [rsp + 0x30], r8d
0x001D7A94: mov dword ptr [rbp + 0xe4], r8d
0x001D7A9B: mov eax, dword ptr [rdi + 0x14]
0x001D7A9E: mov dword ptr [rsp + 0x40], eax
0x001D7AA2: mov dword ptr [rbp + 0xa8], eax
0x001D7AA8: movsxd r10, dword ptr [rsp + 0x3c]
0x001D7AAD: imul rdi, r10, 0x5c
0x001D7AB1: mov r9d, dword ptr [rdi + rbx + 0x188]
0x001D7AB9: test r9d, r9d
0x001D7ABC: je 0x1401d7ac9
0x001D7ABE: cmp r9d, r14d
0x001D7AC1: cmovne r14d, r9d
0x001D7AC5: mov dword ptr [rbp + 0x64], r14d
0x001D7AC9: mov r9d, dword ptr [rdi + rbx + 0x17c]
0x001D7AD1: test r9d, r9d
0x001D7AD4: je 0x1401d7ae1
0x001D7AD6: cmp r9d, r15d
0x001D7AD9: cmovne r15d, r9d
0x001D7ADD: mov dword ptr [rbp + 0x58], r15d
0x001D7AE1: mov r9d, dword ptr [rdi + rbx + 0x170]
0x001D7AE9: test r9d, r9d
0x001D7AEC: je 0x1401d7af9
0x001D7AEE: cmp r9d, r12d
0x001D7AF1: cmovne r12d, r9d
0x001D7AF5: mov dword ptr [rbp + 0x4c], r12d
0x001D7AF9: mov r9d, dword ptr [rdi + rbx + 0x14c]
0x001D7B01: test r9d, r9d
0x001D7B04: je 0x1401d7b10
0x001D7B06: cmp r9d, esi
0x001D7B09: cmovne esi, r9d
0x001D7B0D: mov dword ptr [rbp + 0x28], esi
0x001D7B10: cmp esi, eax
0x001D7B12: jb 0x1401d8ff0
0x001D7B18: cmp r14d, r8d
0x001D7B1B: jb 0x1401d8ff0
0x001D7B21: cmp r15d, edx
0x001D7B24: jb 0x1401d8ff0
0x001D7B2A: cmp r12d, ecx
0x001D7B2D: jb 0x1401d8ff0
0x001D7B33: xor edx, edx
0x001D7B35: lea r8d, [rdx + 0x5c]
0x001D7B39: lea rcx, [rsp + 0x70]
0x001D7B3E: call 0x1403d3050
0x001D7B43: mov r8d, dword ptr [rbx + 0x258]
0x001D7B4A: test r8d, r8d
0x001D7B4D: jle 0x1401d84f8
0x001D7B53: lea rdx, [rsp + 0x70]
0x001D7B58: mov rcx, rbx
0x001D7B5B: call 0x1401d78b0
0x001D7B60: test al, al
0x001D7B62: jne 0x1401d7e1d
0x001D7B68: mov dword ptr [rbp + 0x3f0], 0x5f
0x001D7B72: mov eax, dword ptr [rbp + 0x3f0]
0x001D7B78: xor eax, 0x7b
0x001D7B7B: add eax, 2
0x001D7B7E: mov byte ptr [rbp + 0x3f4], al
0x001D7B84: movsx ecx, byte ptr [rbp + 0x3f4]
0x001D7B8B: xor ecx, 0x7d
0x001D7B8E: add ecx, 2
0x001D7B91: mov byte ptr [rbp + 0x3f5], cl
0x001D7B97: movsx ecx, byte ptr [rbp + 0x3f5]
0x001D7B9E: xor ecx, 0x3a
0x001D7BA1: add ecx, 2
0x001D7BA4: mov byte ptr [rbp + 0x3f6], cl
0x001D7BAA: movsx ecx, byte ptr [rbp + 0x3f6]
0x001D7BB1: xor ecx, 0x20
0x001D7BB4: add ecx, 2
0x001D7BB7: mov byte ptr [rbp + 0x3f7], cl
0x001D7BBD: movsx ecx, byte ptr [rbp + 0x3f7]
0x001D7BC4: xor ecx, 0x75
0x001D7BC7: add ecx, 2
0x001D7BCA: mov byte ptr [rbp + 0x3f8], cl
0x001D7BD0: movsx ecx, byte ptr [rbp + 0x3f8]
0x001D7BD7: xor ecx, 0x6e
0x001D7BDA: add ecx, 2
0x001D7BDD: mov byte ptr [rbp + 0x3f9], cl
0x001D7BE3: movsx ecx, byte ptr [rbp + 0x3f9]
0x001D7BEA: xor ecx, 0x61
0x001D7BED: add ecx, 2
0x001D7BF0: mov byte ptr [rbp + 0x3fa], cl
0x001D7BF6: movsx ecx, byte ptr [rbp + 0x3fa]
0x001D7BFD: xor ecx, 0x62
0x001D7C00: add ecx, 2
0x001D7C03: mov byte ptr [rbp + 0x3fb], cl
0x001D7C09: movsx ecx, byte ptr [rbp + 0x3fb]
0x001D7C10: xor ecx, 0x6c
0x001D7C13: add ecx, 2
0x001D7C16: mov byte ptr [rbp + 0x3fc], cl
0x001D7C1C: movsx ecx, byte ptr [rbp + 0x3fc]
0x001D7C23: xor ecx, 0x65
0x001D7C26: add ecx, 2
0x001D7C29: mov byte ptr [rbp + 0x3fd], cl
0x001D7C2F: movsx ecx, byte ptr [rbp + 0x3fd]
0x001D7C36: xor ecx, 0x20
0x001D7C39: add ecx, 2
0x001D7C3C: mov byte ptr [rbp + 0x3fe], cl
0x001D7C42: movsx ecx, byte ptr [rbp + 0x3fe]
0x001D7C49: xor ecx, 0x74
0x001D7C4C: add ecx, 2
0x001D7C4F: mov byte ptr [rbp + 0x3ff], cl
0x001D7C55: movsx ecx, byte ptr [rbp + 0x3ff]
0x001D7C5C: xor ecx, 0x6f
0x001D7C5F: add ecx, 2
0x001D7C62: mov byte ptr [rbp + 0x400], cl
0x001D7C68: movsx ecx, byte ptr [rbp + 0x400]
0x001D7C6F: xor ecx, 0x20
0x001D7C72: add ecx, 2
0x001D7C75: mov byte ptr [rbp + 0x401], cl
0x001D7C7B: movsx ecx, byte ptr [rbp + 0x401]
0x001D7C82: xor ecx, 0x66
0x001D7C85: add ecx, 2
0x001D7C88: mov byte ptr [rbp + 0x402], cl
0x001D7C8E: movsx ecx, byte ptr [rbp + 0x402]
0x001D7C95: xor ecx, 0x69
0x001D7C98: add ecx, 2
0x001D7C9B: mov byte ptr [rbp + 0x403], cl
0x001D7CA1: movsx ecx, byte ptr [rbp + 0x403]
0x001D7CA8: xor ecx, 0x6e
0x001D7CAB: add ecx, 2
0x001D7CAE: mov byte ptr [rbp + 0x404], cl
0x001D7CB4: movsx ecx, byte ptr [rbp + 0x404]
0x001D7CBB: xor ecx, 0x64
0x001D7CBE: add ecx, 2
0x001D7CC1: mov byte ptr [rbp + 0x405], cl
0x001D7CC7: movsx ecx, byte ptr [rbp + 0x405]
0x001D7CCE: xor ecx, 0x20
0x001D7CD1: add ecx, 2
0x001D7CD4: mov byte ptr [rbp + 0x406], cl
0x001D7CDA: movsx ecx, byte ptr [rbp + 0x406]
0x001D7CE1: xor ecx, 0x73
0x001D7CE4: add ecx, 2
0x001D7CE7: mov byte ptr [rbp + 0x407], cl
0x001D7CED: movsx ecx, byte ptr [rbp + 0x407]
0x001D7CF4: xor ecx, 0x74
0x001D7CF7: add ecx, 2
0x001D7CFA: mov byte ptr [rbp + 0x408], cl
0x001D7D00: movsx ecx, byte ptr [rbp + 0x408]
0x001D7D07: xor ecx, 0x72
0x001D7D0A: add ecx, 2
0x001D7D0D: mov byte ptr [rbp + 0x409], cl
0x001D7D13: movsx ecx, byte ptr [rbp + 0x409]
0x001D7D1A: xor ecx, 0x61
0x001D7D1D: add ecx, 2
0x001D7D20: mov byte ptr [rbp + 0x40a], cl
0x001D7D26: movsx ecx, byte ptr [rbp + 0x40a]
0x001D7D2D: xor ecx, 0x70
0x001D7D30: add ecx, 2
0x001D7D33: mov byte ptr [rbp + 0x40b], cl
0x001D7D39: movsx ecx, byte ptr [rbp + 0x40b]
0x001D7D40: xor ecx, 0x20
0x001D7D43: add ecx, 2
0x001D7D46: mov byte ptr [rbp + 0x40c], cl
0x001D7D4C: movsx ecx, byte ptr [rbp + 0x40c]
0x001D7D53: xor ecx, 0x7b
0x001D7D56: add ecx, 2
0x001D7D59: mov byte ptr [rbp + 0x40d], cl
0x001D7D5F: movsx ecx, byte ptr [rbp + 0x40d]
0x001D7D66: xor ecx, 0x7d
0x001D7D69: add ecx, 2
0x001D7D6C: mov byte ptr [rbp + 0x40e], cl
0x001D7D72: movsx ecx, byte ptr [rbp + 0x40e]
0x001D7D79: xor ecx, 0x20
0x001D7D7C: add ecx, 2
0x001D7D7F: mov byte ptr [rbp + 0x40f], cl
0x001D7D85: movsx ecx, byte ptr [rbp + 0x40f]
0x001D7D8C: xor ecx, 0x69
0x001D7D8F: add ecx, 2
0x001D7D92: mov byte ptr [rbp + 0x410], cl
0x001D7D98: movsx ecx, byte ptr [rbp + 0x410]
0x001D7D9F: xor ecx, 0x6e
0x001D7DA2: add ecx, 2
0x001D7DA5: mov byte ptr [rbp + 0x411], cl
0x001D7DAB: movsx ecx, byte ptr [rbp + 0x411]
0x001D7DB2: xor ecx, 0x66
0x001D7DB5: add ecx, 2
0x001D7DB8: mov byte ptr [rbp + 0x412], cl
0x001D7DBE: movsx ecx, byte ptr [rbp + 0x412]
0x001D7DC5: xor ecx, 0x6f
0x001D7DC8: add ecx, 2
0x001D7DCB: mov byte ptr [rbp + 0x413], cl
0x001D7DD1: mov byte ptr [rbp + 0x414], 0
0x001D7DD8: movzx eax, byte ptr [rbp + 0x3f4]
0x001D7DDF: lea rdx, [rbp + 0x460]
0x001D7DE6: lea rcx, [rbp + 0x3f0]
0x001D7DED: call 0x140206e40
0x001D7DF2: nop
0x001D7DF3: cmp qword ptr [rax + 0x18], 0x10
0x001D7DF8: jb 0x1401d7dfd
0x001D7DFA: mov rax, qword ptr [rax]
0x001D7DFD: lea rdx, [rbx + 8]
0x001D7E01: lea r8, [rbx + 0x258]
0x001D7E08: mov rcx, rax
0x001D7E0B: call 0x14012ee60
0x001D7E10: nop
0x001D7E11: lea rcx, [rbp + 0x460]
0x001D7E18: jmp 0x1401d944a
0x001D7E1D: mov ecx, dword ptr [rsp + 0x78]
0x001D7E21: test ecx, ecx
0x001D7E23: je 0x1401d7e54
0x001D7E25: cmp ecx, esi
0x001D7E27: jae 0x1401d7e54
0x001D7E29: mov eax, esi
0x001D7E2B: sub eax, ecx
0x001D7E2D: imul ecx, eax, 0x64
0x001D7E30: xorps xmm1, xmm1
0x001D7E33: cvtsi2sd xmm1, rcx
0x001D7E38: sub esi, dword ptr [rsp + 0x40]
0x001D7E3C: mov eax, esi
0x001D7E3E: xorps xmm0, xmm0
0x001D7E41: cvtsi2sd xmm0, rax
0x001D7E46: divsd xmm1, xmm0
0x001D7E4A: cvttsd2si eax, xmm1
0x001D7E4E: mov dword ptr [rsp + 0x40], eax
0x001D7E52: jmp 0x1401d7e5c
0x001D7E54: mov dword ptr [rsp + 0x40], 0
0x001D7E5C: mov ecx, dword ptr [rbp - 0x64]
0x001D7E5F: test ecx, ecx
0x001D7E61: je 0x1401d7e93
0x001D7E63: cmp ecx, r12d
0x001D7E66: jae 0x1401d7e93
0x001D7E68: mov eax, r12d
0x001D7E6B: sub eax, ecx
0x001D7E6D: imul ecx, eax, 0x64
0x001D7E70: xorps xmm1, xmm1
0x001D7E73: cvtsi2sd xmm1, rcx
0x001D7E78: sub r12d, dword ptr [rsp + 0x38]
0x001D7E7D: mov eax, r12d
0x001D7E80: xorps xmm0, xmm0
0x001D7E83: cvtsi2sd xmm0, rax
0x001D7E88: divsd xmm1, xmm0
0x001D7E8C: cvttsd2si r12d, xmm1
0x001D7E91: jmp 0x1401d7e96
0x001D7E93: xor r12d, r12d
0x001D7E96: mov ecx, dword ptr [rbp - 0x58]
0x001D7E99: test ecx, ecx
0x001D7E9B: je 0x1401d7ecd
0x001D7E9D: cmp ecx, r15d
0x001D7EA0: jae 0x1401d7ecd
0x001D7EA2: mov eax, r15d
0x001D7EA5: sub eax, ecx
0x001D7EA7: imul ecx, eax, 0x64
0x001D7EAA: xorps xmm1, xmm1
0x001D7EAD: cvtsi2sd xmm1, rcx
0x001D7EB2: sub r15d, dword ptr [rsp + 0x34]
0x001D7EB7: mov eax, r15d
0x001D7EBA: xorps xmm0, xmm0
0x001D7EBD: cvtsi2sd xmm0, rax
0x001D7EC2: divsd xmm1, xmm0
0x001D7EC6: cvttsd2si r15d, xmm1
0x001D7ECB: jmp 0x1401d7ed0
0x001D7ECD: xor r15d, r15d
0x001D7ED0: mov ecx, dword ptr [rbp - 0x4c]
0x001D7ED3: test ecx, ecx
0x001D7ED5: je 0x1401d7f06
0x001D7ED7: cmp ecx, r14d
0x001D7EDA: jae 0x1401d7f06
0x001D7EDC: mov eax, r14d
0x001D7EDF: sub eax, ecx
0x001D7EE1: imul ecx, eax, 0x64
0x001D7EE4: xorps xmm1, xmm1
0x001D7EE7: cvtsi2sd xmm1, rcx
0x001D7EEC: sub r14d, dword ptr [rsp + 0x30]
0x001D7EF1: mov eax, r14d
0x001D7EF4: xorps xmm0, xmm0
0x001D7EF7: cvtsi2sd xmm0, rax
0x001D7EFC: divsd xmm1, xmm0
0x001D7F00: cvttsd2si esi, xmm1
0x001D7F04: jmp 0x1401d7f08
0x001D7F06: xor esi, esi
0x001D7F08: mov dword ptr [rbp + 0x3a0], 0x50
0x001D7F12: mov dword ptr [rbp + 0x3a4], 0x3d
0x001D7F1C: mov eax, dword ptr [rbp + 0x3a4]
0x001D7F22: xor eax, 0x2b
0x001D7F25: mov byte ptr [rbp + 0x3a8], al
0x001D7F2B: movsx ecx, byte ptr [rbp + 0x3a8]
0x001D7F32: xor ecx, 0x2d
0x001D7F35: mov byte ptr [rbp + 0x3a9], cl
0x001D7F3B: movsx ecx, byte ptr [rbp + 0x3a9]
0x001D7F42: xor ecx, 0x6a
0x001D7F45: mov byte ptr [rbp + 0x3aa], cl
0x001D7F4B: movsx ecx, byte ptr [rbp + 0x3aa]
0x001D7F52: xor ecx, 0x70
0x001D7F55: mov byte ptr [rbp + 0x3ab], cl
0x001D7F5B: movsx ecx, byte ptr [rbp + 0x3ab]
0x001D7F62: xor ecx, 0x23
0x001D7F65: mov byte ptr [rbp + 0x3ac], cl
0x001D7F6B: movsx ecx, byte ptr [rbp + 0x3ac]
0x001D7F72: xor ecx, 0x35
0x001D7F75: mov byte ptr [rbp + 0x3ad], cl
0x001D7F7B: movsx ecx, byte ptr [rbp + 0x3ad]
0x001D7F82: xor ecx, 0x24
0x001D7F85: mov byte ptr [rbp + 0x3ae], cl
0x001D7F8B: movsx ecx, byte ptr [rbp + 0x3ae]
0x001D7F92: xor ecx, 0x70
0x001D7F95: mov byte ptr [rbp + 0x3af], cl
0x001D7F9B: movsx ecx, byte ptr [rbp + 0x3af]
0x001D7FA2: xor ecx, 6
0x001D7FA5: mov byte ptr [rbp + 0x3b0], cl
0x001D7FAB: movsx ecx, byte ptr [rbp + 0x3b0]
0x001D7FB2: xor ecx, 2
0x001D7FB5: mov byte ptr [rbp + 0x3b1], cl
0x001D7FBB: movsx ecx, byte ptr [rbp + 0x3b1]
0x001D7FC2: xor ecx, 0x11
0x001D7FC5: mov byte ptr [rbp + 0x3b2], cl
0x001D7FCB: movsx ecx, byte ptr [rbp + 0x3b2]
0x001D7FD2: xor ecx, 0x1d
0x001D7FD5: mov byte ptr [rbp + 0x3b3], cl
0x001D7FDB: movsx ecx, byte ptr [rbp + 0x3b3]
0x001D7FE2: xor ecx, 0x70
0x001D7FE5: mov byte ptr [rbp + 0x3b4], cl
0x001D7FEB: movsx ecx, byte ptr [rbp + 0x3b4]
0x001D7FF2: xor ecx, 0x23
0x001D7FF5: mov byte ptr [rbp + 0x3b5], cl
0x001D7FFB: movsx ecx, byte ptr [rbp + 0x3b5]
0x001D8002: xor ecx, 0x24
0x001D8005: mov byte ptr [rbp + 0x3b6], cl
0x001D800B: movsx ecx, byte ptr [rbp + 0x3b6]
0x001D8012: xor ecx, 0x22
0x001D8015: mov byte ptr [rbp + 0x3b7], cl
0x001D801B: movsx ecx, byte ptr [rbp + 0x3b7]
0x001D8022: xor ecx, 0x31
0x001D8025: mov byte ptr [rbp + 0x3b8], cl
0x001D802B: movsx ecx, byte ptr [rbp + 0x3b8]
0x001D8032: xor ecx, 0x20
0x001D8035: mov byte ptr [rbp + 0x3b9], cl
0x001D803B: movsx ecx, byte ptr [rbp + 0x3b9]
0x001D8042: xor ecx, 0x70
0x001D8045: mov byte ptr [rbp + 0x3ba], cl
0x001D804B: movsx ecx, byte ptr [rbp + 0x3ba]
0x001D8052: xor ecx, 0x2b
0x001D8055: mov byte ptr [rbp + 0x3bb], cl
0x001D805B: movsx ecx, byte ptr [rbp + 0x3bb]
0x001D8062: xor ecx, 0x2d
0x001D8065: mov byte ptr [rbp + 0x3bc], cl
0x001D806B: movsx ecx, byte ptr [rbp + 0x3bc]
0x001D8072: xor ecx, 0x70
0x001D8075: mov byte ptr [rbp + 0x3bd], cl
0x001D807B: movsx ecx, byte ptr [rbp + 0x3bd]
0x001D8082: xor ecx, 0x78
0x001D8085: mov byte ptr [rbp + 0x3be], cl
0x001D808B: movsx ecx, byte ptr [rbp + 0x3be]
0x001D8092: xor ecx, 0x7d
0x001D8095: mov byte ptr [rbp + 0x3bf], cl
0x001D809B: movsx ecx, byte ptr [rbp + 0x3bf]
0x001D80A2: xor ecx, 0x26
0x001D80A5: mov byte ptr [rbp + 0x3c0], cl
0x001D80AB: movsx ecx, byte ptr [rbp + 0x3c0]
0x001D80B2: xor ecx, 0x3d
0x001D80B5: mov byte ptr [rbp + 0x3c1], cl
0x001D80BB: movsx ecx, byte ptr [rbp + 0x3c1]
0x001D80C2: xor ecx, 0x24
0x001D80C5: mov byte ptr [rbp + 0x3c2], cl
0x001D80CB: movsx ecx, byte ptr [rbp + 0x3c2]
0x001D80D2: xor ecx, 0x61
0x001D80D5: mov byte ptr [rbp + 0x3c3], cl
0x001D80DB: movsx ecx, byte ptr [rbp + 0x3c3]
0x001D80E2: xor ecx, 0x70
0x001D80E5: mov byte ptr [rbp + 0x3c4], cl
0x001D80EB: movsx ecx, byte ptr [rbp + 0x3c4]
0x001D80F2: xor ecx, 0x2b
0x001D80F5: mov byte ptr [rbp + 0x3c5], cl
0x001D80FB: movsx ecx, byte ptr [rbp + 0x3c5]
0x001D8102: xor ecx, 0x2d
0x001D8105: mov byte ptr [rbp + 0x3c6], cl
0x001D810B: movsx ecx, byte ptr [rbp + 0x3c6]
0x001D8112: xor ecx, 0x70
0x001D8115: mov byte ptr [rbp + 0x3c7], cl
0x001D811B: movsx ecx, byte ptr [rbp + 0x3c7]
0x001D8122: xor ecx, 0x7d
0x001D8125: mov byte ptr [rbp + 0x3c8], cl
0x001D812B: movsx ecx, byte ptr [rbp + 0x3c8]
0x001D8132: xor ecx, 0x26
0x001D8135: mov byte ptr [rbp + 0x3c9], cl
0x001D813B: movsx ecx, byte ptr [rbp + 0x3c9]
0x001D8142: xor ecx, 0x3d
0x001D8145: mov byte ptr [rbp + 0x3ca], cl
0x001D814B: movsx ecx, byte ptr [rbp + 0x3ca]
0x001D8152: xor ecx, 0x24
0x001D8155: mov byte ptr [rbp + 0x3cb], cl
0x001D815B: movsx ecx, byte ptr [rbp + 0x3cb]
0x001D8162: xor ecx, 0x62
0x001D8165: mov byte ptr [rbp + 0x3cc], cl
0x001D816B: movsx ecx, byte ptr [rbp + 0x3cc]
0x001D8172: xor ecx, 0x70
0x001D8175: mov byte ptr [rbp + 0x3cd], cl
0x001D817B: movsx ecx, byte ptr [rbp + 0x3cd]
0x001D8182: xor ecx, 0x2b
0x001D8185: mov byte ptr [rbp + 0x3ce], cl
0x001D818B: movsx ecx, byte ptr [rbp + 0x3ce]
0x001D8192: xor ecx, 0x2d
0x001D8195: mov byte ptr [rbp + 0x3cf], cl
0x001D819B: movsx ecx, byte ptr [rbp + 0x3cf]
0x001D81A2: xor ecx, 0x70
0x001D81A5: mov byte ptr [rbp + 0x3d0], cl
0x001D81AB: movsx ecx, byte ptr [rbp + 0x3d0]
0x001D81B2: xor ecx, 0x7d
0x001D81B5: mov byte ptr [rbp + 0x3d1], cl
0x001D81BB: movsx ecx, byte ptr [rbp + 0x3d1]
0x001D81C2: xor ecx, 0x26
0x001D81C5: mov byte ptr [rbp + 0x3d2], cl
0x001D81CB: movsx ecx, byte ptr [rbp + 0x3d2]
0x001D81D2: xor ecx, 0x3d
0x001D81D5: mov byte ptr [rbp + 0x3d3], cl
0x001D81DB: movsx ecx, byte ptr [rbp + 0x3d3]
0x001D81E2: xor ecx, 0x24
0x001D81E5: mov byte ptr [rbp + 0x3d4], cl
0x001D81EB: movsx ecx, byte ptr [rbp + 0x3d4]
0x001D81F2: xor ecx, 0x63
0x001D81F5: mov byte ptr [rbp + 0x3d5], cl
0x001D81FB: movsx ecx, byte ptr [rbp + 0x3d5]
0x001D8202: xor ecx, 0x70
0x001D8205: mov byte ptr [rbp + 0x3d6], cl
0x001D820B: movsx ecx, byte ptr [rbp + 0x3d6]
0x001D8212: xor ecx, 0x2b
0x001D8215: mov byte ptr [rbp + 0x3d7], cl
0x001D821B: movsx ecx, byte ptr [rbp + 0x3d7]
0x001D8222: xor ecx, 0x2d
0x001D8225: mov byte ptr [rbp + 0x3d8], cl
0x001D822B: movsx ecx, byte ptr [rbp + 0x3d8]
0x001D8232: xor ecx, 0x70
0x001D8235: mov byte ptr [rbp + 0x3d9], cl
0x001D823B: movsx ecx, byte ptr [rbp + 0x3d9]
0x001D8242: xor ecx, 0x7d
0x001D8245: mov byte ptr [rbp + 0x3da], cl
0x001D824B: movsx ecx, byte ptr [rbp + 0x3da]
0x001D8252: xor ecx, 0x26
0x001D8255: mov byte ptr [rbp + 0x3db], cl
0x001D825B: movsx ecx, byte ptr [rbp + 0x3db]
0x001D8262: xor ecx, 0x3d
0x001D8265: mov byte ptr [rbp + 0x3dc], cl
0x001D826B: movsx ecx, byte ptr [rbp + 0x3dc]
0x001D8272: xor ecx, 0x22
0x001D8275: mov byte ptr [rbp + 0x3dd], cl
0x001D827B: movsx ecx, byte ptr [rbp + 0x3dd]
0x001D8282: xor ecx, 0x70
0x001D8285: mov byte ptr [rbp + 0x3de], cl
0x001D828B: movsx ecx, byte ptr [rbp + 0x3de]
0x001D8292: xor ecx, 0x2b
0x001D8295: mov byte ptr [rbp + 0x3df], cl
0x001D829B: movsx ecx, byte ptr [rbp + 0x3df]
0x001D82A2: xor ecx, 0x2d
0x001D82A5: mov byte ptr [rbp + 0x3e0], cl
0x001D82AB: movsx ecx, byte ptr [rbp + 0x3e0]
0x001D82B2: xor ecx, 0x79
0x001D82B5: mov byte ptr [rbp + 0x3e1], cl
0x001D82BB: xor eax, eax
0x001D82BD: mov byte ptr [rbp + 0x3e2], al
0x001D82C3: movzx eax, byte ptr [rbp + 0x3a8]
0x001D82CA: lea rdx, [rbp + 0x480]
0x001D82D1: lea rcx, [rbp + 0x3a0]
0x001D82D8: call 0x1401269f0
0x001D82DD: mov rdx, rax
0x001D82E0: cmp qword ptr [rax + 0x18], 0x10
0x001D82E5: jb 0x1401d82ea
0x001D82E7: mov rdx, qword ptr [rax]
0x001D82EA: lea rcx, [rbp + 0x530]
0x001D82F1: mov qword ptr [rbp + 0x528], rcx
0x001D82F8: lea rcx, [rip + 0x25b9b9]
0x001D82FF: mov qword ptr [rbp + 0x520], rcx
0x001D8306: lea rcx, [rbp + 0x550]
0x001D830D: mov qword ptr [rbp + 0x538], rcx
0x001D8314: xor r14d, r14d
0x001D8317: mov qword ptr [rbp + 0x540], r14
0x001D831E: mov qword ptr [rbp + 0x548], 0x1f4
0x001D8329: lea rcx, [rip + 0x25b8e0]
0x001D8330: mov qword ptr [rbp + 0x530], rcx
0x001D8337: mov qword ptr [rbp + 0x88], rdx
0x001D833E: cmp qword ptr [rbx + 0x20], 0x10
0x001D8343: jb 0x1401d834b
0x001D8345: mov rcx, qword ptr [rbx + 8]
0x001D8349: jmp 0x1401d834f
0x001D834B: lea rcx, [rbx + 8]
0x001D834F: mov qword ptr [rbp + 0x90], rcx
0x001D8356: mov rax, qword ptr [rbx + 0x18]
0x001D835A: mov qword ptr [rbp + 0x98], rax
0x001D8361: mov qword ptr [rbp - 0x30], rcx
0x001D8365: mov qword ptr [rbp - 0x28], rax
0x001D8369: movups xmm0, xmmword ptr [rbp - 0x30]
0x001D836D: movups xmmword ptr [rbp + 0x100], xmm0
0x001D8374: movups xmmword ptr [rbp + 0x750], xmm0
0x001D837B: mov eax, dword ptr [rbx + 0x258]
0x001D8381: mov dword ptr [rbp - 0x30], eax
0x001D8384: movups xmm0, xmmword ptr [rbp - 0x30]
0x001D8388: movups xmmword ptr [rbp - 0x30], xmm0
0x001D838C: movups xmmword ptr [rbp + 0x760], xmm0
0x001D8393: mov dword ptr [rsp + 0x50], esi
0x001D8397: movups xmm0, xmmword ptr [rsp + 0x50]
0x001D839C: movaps xmmword ptr [rbp + 0x770], xmm0
0x001D83A3: mov dword ptr [rsp + 0x50], r15d
0x001D83A8: movups xmm0, xmmword ptr [rsp + 0x50]
0x001D83AD: movaps xmmword ptr [rbp + 0x780], xmm0
0x001D83B4: mov dword ptr [rsp + 0x50], r12d
0x001D83B9: movups xmm0, xmmword ptr [rsp + 0x50]
0x001D83BE: movaps xmmword ptr [rbp + 0x790], xmm0
0x001D83C5: mov eax, dword ptr [rsp + 0x40]
0x001D83C9: mov dword ptr [rsp + 0x50], eax
0x001D83CD: movups xmm0, xmmword ptr [rsp + 0x50]
0x001D83D2: movaps xmmword ptr [rbp + 0x7a0], xmm0
0x001D83D9: mov qword ptr [rsp + 0x40], 0x22222b
0x001D83E2: lea rax, [rbp + 0x750]
0x001D83E9: mov qword ptr [rsp + 0x48], rax
0x001D83EE: movups xmm0, xmmword ptr [rsp + 0x40]
0x001D83F3: movups xmmword ptr [rbp - 0x18], xmm0
0x001D83F7: mov dword ptr [rbp - 8], r14d
0x001D83FB: lea rax, [rbp + 0x520]
0x001D8402: mov qword ptr [rbp], rax
0x001D8406: xorps xmm0, xmm0
0x001D8409: movdqu xmmword ptr [rbp + 8], xmm0
0x001D840E: mov qword ptr [rbp + 0x18], r14
0x001D8412: lea rcx, [rbp - 0x18]
0x001D8416: call 0x140036ad0
0x001D841B: nop
0x001D841C: mov r9, qword ptr [rbp + 8]
0x001D8420: test r9, r9
0x001D8423: je 0x1401d845f
0x001D8425: mov rcx, qword ptr [rbp + 0x18]
0x001D8429: sub rcx, r9
0x001D842C: movabs rax, 0x6666666666666667
0x001D8436: imul rcx
0x001D8439: sar rdx, 4
0x001D843D: mov r8, rdx
0x001D8440: shr r8, 0x3f
0x001D8444: add r8, rdx
0x001D8447: mov rdx, r9
0x001D844A: lea rcx, [rbp + 8]
0x001D844E: call 0x14006f540
0x001D8453: xorps xmm0, xmm0
0x001D8456: movdqu xmmword ptr [rbp + 8], xmm0
0x001D845B: mov qword ptr [rbp + 0x18], r14
0x001D845F: lea rax, [rbp + 0x120]
0x001D8466: mov qword ptr [rbp + 0x118], rax
0x001D846D: lea rax, [rip + 0x25b844]
0x001D8474: mov qword ptr [rbp + 0x110], rax
0x001D847B: lea rdx, [rbp + 0x530]
0x001D8482: lea rcx, [rbp + 0x120]
0x001D8489: call 0x1400328e0
0x001D848E: lea rcx, [rbp + 0x110]
0x001D8495: call 0x140073470
0x001D849A: nop
0x001D849B: lea rcx, [rbp + 0x530]
0x001D84A2: call 0x140032dc0
0x001D84A7: lea rax, [rip + 0x25b7fa]
0x001D84AE: mov qword ptr [rbp + 0x520], rax
0x001D84B5: lea rcx, [rbp + 0x480]
0x001D84BC: call 0x140032ef0
0x001D84C1: mov r14d, dword ptr [rbp + 0x64]
0x001D84C5: mov r15d, dword ptr [rbp + 0x58]
0x001D84C9: mov r12d, dword ptr [rbp + 0x4c]
0x001D84CD: mov esi, dword ptr [rbp + 0x28]
0x001D84D0: mov eax, dword ptr [rbp + 0xe4]
0x001D84D6: mov dword ptr [rsp + 0x30], eax
0x001D84DA: mov eax, dword ptr [rbp + 0xd8]
0x001D84E0: mov dword ptr [rsp + 0x34], eax
0x001D84E4: mov eax, dword ptr [rbp + 0xcc]
0x001D84EA: mov dword ptr [rsp + 0x38], eax
0x001D84EE: mov eax, dword ptr [rbp + 0xa8]
0x001D84F4: mov dword ptr [rsp + 0x40], eax
0x001D84F8: mov rcx, rbx
0x001D84FB: call 0x1401d97b0
0x001D8500: movsd xmm6, qword ptr [rip + 0x2601b0]
0x001D8508: test al, al
0x001D850A: je 0x1401d8b1b
0x001D8510: mov ecx, dword ptr [rbx + 0x260]
0x001D8516: test ecx, ecx
0x001D8518: jle 0x1401d8551
0x001D851A: mov eax, r14d
0x001D851D: xorps xmm2, xmm2
0x001D8520: cvtsi2sd xmm2, rax
0x001D8525: sub r14d, dword ptr [rsp + 0x30]
0x001D852A: mov eax, r14d
0x001D852D: xorps xmm1, xmm1
0x001D8530: cvtsi2sd xmm1, rax
0x001D8535: movd xmm0, ecx
0x001D8539: cvtdq2pd xmm0, xmm0
0x001D853D: divsd xmm0, xmm6
0x001D8541: mulsd xmm1, xmm0
0x001D8545: subsd xmm2, xmm1
0x001D8549: cvttsd2si rax, xmm2
0x001D854E: mov dword ptr [rbp - 0x4c], eax
0x001D8551: mov ecx, dword ptr [rbx + 0x264]
0x001D8557: test ecx, ecx
0x001D8559: jle 0x1401d8592
0x001D855B: mov eax, r15d
0x001D855E: xorps xmm2, xmm2
0x001D8561: cvtsi2sd xmm2, rax
0x001D8566: sub r15d, dword ptr [rsp + 0x34]
0x001D856B: mov eax, r15d
0x001D856E: xorps xmm1, xmm1
0x001D8571: cvtsi2sd xmm1, rax
0x001D8576: movd xmm0, ecx
0x001D857A: cvtdq2pd xmm0, xmm0
0x001D857E: divsd xmm0, xmm6
0x001D8582: mulsd xmm1, xmm0
0x001D8586: subsd xmm2, xmm1
0x001D858A: cvttsd2si rax, xmm2
0x001D858F: mov dword ptr [rbp - 0x58], eax
0x001D8592: lea rsi, [rbx + 0x268]
0x001D8599: mov ecx, dword ptr [rsi]
0x001D859B: test ecx, ecx
0x001D859D: jle 0x1401d85d6
0x001D859F: mov eax, r12d
0x001D85A2: xorps xmm2, xmm2
0x001D85A5: cvtsi2sd xmm2, rax
0x001D85AA: sub r12d, dword ptr [rsp + 0x38]
0x001D85AF: mov eax, r12d
0x001D85B2: xorps xmm1, xmm1
0x001D85B5: cvtsi2sd xmm1, rax
0x001D85BA: movd xmm0, ecx
0x001D85BE: cvtdq2pd xmm0, xmm0
0x001D85C2: divsd xmm0, xmm6
0x001D85C6: mulsd xmm1, xmm0
0x001D85CA: subsd xmm2, xmm1
0x001D85CE: cvttsd2si rax, xmm2
0x001D85D3: mov dword ptr [rbp - 0x64], eax
0x001D85D6: mov dword ptr [rbp + 0x338], 0x5d
0x001D85E0: mov eax, dword ptr [rbp + 0x338]
0x001D85E6: add al, 0x5d
0x001D85E8: movsx ecx, al
0x001D85EB: xor ecx, 0x72
0x001D85EE: mov dword ptr [rbp + 0x33c], ecx
0x001D85F4: mov eax, dword ptr [rbp + 0x33c]
0x001D85FA: mov ecx, dword ptr [rbp + 0x338]
0x001D8600: xor ecx, eax
0x001D8602: xor ecx, 0x7b
0x001D8605: mov byte ptr [rbp + 0x340], cl
0x001D860B: movsx ecx, byte ptr [rbp + 0x340]
0x001D8612: mov eax, dword ptr [rbp + 0x338]
0x001D8618: inc al
0x001D861A: xor eax, ecx
0x001D861C: xor eax, 0x7d
0x001D861F: mov byte ptr [rbp + 0x341], al
0x001D8625: movsx ecx, byte ptr [rbp + 0x341]
0x001D862C: mov eax, dword ptr [rbp + 0x338]
0x001D8632: add al, 2
0x001D8634: xor eax, ecx
0x001D8636: xor eax, 0x3a
0x001D8639: mov byte ptr [rbp + 0x342], al
0x001D863F: movsx ecx, byte ptr [rbp + 0x342]
0x001D8646: mov eax, dword ptr [rbp + 0x338]
0x001D864C: add al, 3
0x001D864E: xor eax, ecx
0x001D8650: xor eax, 0x20
0x001D8653: mov byte ptr [rbp + 0x343], al
0x001D8659: movsx ecx, byte ptr [rbp + 0x343]
0x001D8660: mov eax, dword ptr [rbp + 0x338]
0x001D8666: add al, 4
0x001D8668: xor eax, ecx
0x001D866A: xor eax, 0x73
0x001D866D: mov byte ptr [rbp + 0x344], al
0x001D8673: movsx ecx, byte ptr [rbp + 0x344]
0x001D867A: mov eax, dword ptr [rbp + 0x338]
0x001D8680: add al, 5
0x001D8682: xor eax, ecx
0x001D8684: xor eax, 0x65
0x001D8687: mov byte ptr [rbp + 0x345], al
0x001D868D: movsx ecx, byte ptr [rbp + 0x345]
0x001D8694: mov eax, dword ptr [rbp + 0x338]
0x001D869A: add al, 6
0x001D869C: xor eax, ecx
0x001D869E: xor eax, 0x74
0x001D86A1: mov byte ptr [rbp + 0x346], al
0x001D86A7: movsx ecx, byte ptr [rbp + 0x346]
0x001D86AE: mov eax, dword ptr [rbp + 0x338]
0x001D86B4: add al, 7
0x001D86B6: xor eax, ecx
0x001D86B8: xor eax, 0x20
0x001D86BB: mov byte ptr [rbp + 0x347], al
0x001D86C1: movsx ecx, byte ptr [rbp + 0x347]
0x001D86C8: mov eax, dword ptr [rbp + 0x338]
0x001D86CE: add al, 8
0x001D86D0: xor eax, ecx
0x001D86D2: xor eax, 0x56
0x001D86D5: mov byte ptr [rbp + 0x348], al
0x001D86DB: movsx ecx, byte ptr [rbp + 0x348]
0x001D86E2: mov eax, dword ptr [rbp + 0x338]
0x001D86E8: add al, 9
0x001D86EA: xor eax, ecx
0x001D86EC: xor eax, 0x52
0x001D86EF: mov byte ptr [rbp + 0x349], al
0x001D86F5: movsx ecx, byte ptr [rbp + 0x349]
0x001D86FC: mov eax, dword ptr [rbp + 0x338]
0x001D8702: add al, 0xa
0x001D8704: xor eax, ecx
0x001D8706: xor eax, 0x41
0x001D8709: mov byte ptr [rbp + 0x34a], al
0x001D870F: movsx ecx, byte ptr [rbp + 0x34a]
0x001D8716: mov eax, dword ptr [rbp + 0x338]
0x001D871C: add al, 0xb
0x001D871E: xor eax, ecx
0x001D8720: xor eax, 0x4d
0x001D8723: mov byte ptr [rbp + 0x34b], al
0x001D8729: movsx ecx, byte ptr [rbp + 0x34b]
0x001D8730: mov eax, dword ptr [rbp + 0x338]
0x001D8736: add al, 0xc
0x001D8738: xor eax, ecx
0x001D873A: xor eax, 0x20
0x001D873D: mov byte ptr [rbp + 0x34c], al
0x001D8743: movsx ecx, byte ptr [rbp + 0x34c]
0x001D874A: mov eax, dword ptr [rbp + 0x338]
0x001D8750: add al, 0xd
0x001D8752: xor eax, ecx
0x001D8754: xor eax, 0x74
0x001D8757: mov byte ptr [rbp + 0x34d], al
0x001D875D: movsx ecx, byte ptr [rbp + 0x34d]
0x001D8764: mov eax, dword ptr [rbp + 0x338]
0x001D876A: add al, 0xe
0x001D876C: xor eax, ecx
0x001D876E: xor eax, 0x69
0x001D8771: mov byte ptr [rbp + 0x34e], al
0x001D8777: movsx ecx, byte ptr [rbp + 0x34e]
0x001D877E: mov eax, dword ptr [rbp + 0x338]
0x001D8784: add al, 0xf
0x001D8786: xor eax, ecx
0x001D8788: xor eax, 0x6d
0x001D878B: mov byte ptr [rbp + 0x34f], al
0x001D8791: movsx ecx, byte ptr [rbp + 0x34f]
0x001D8798: mov eax, dword ptr [rbp + 0x338]
0x001D879E: add al, 0x10
0x001D87A0: xor eax, ecx
0x001D87A2: xor eax, 0x69
0x001D87A5: mov byte ptr [rbp + 0x350], al
0x001D87AB: movsx ecx, byte ptr [rbp + 0x350]
0x001D87B2: mov eax, dword ptr [rbp + 0x338]
0x001D87B8: add al, 0x11
0x001D87BA: xor eax, ecx
0x001D87BC: xor eax, 0x6e
0x001D87BF: mov byte ptr [rbp + 0x351], al
0x001D87C5: movsx ecx, byte ptr [rbp + 0x351]
0x001D87CC: mov eax, dword ptr [rbp + 0x338]
0x001D87D2: add al, 0x12
0x001D87D4: xor eax, ecx
0x001D87D6: xor eax, 0x67
0x001D87D9: mov byte ptr [rbp + 0x352], al
0x001D87DF: movsx ecx, byte ptr [rbp + 0x352]
0x001D87E6: mov eax, dword ptr [rbp + 0x338]
0x001D87EC: add al, 0x13
0x001D87EE: xor eax, ecx
0x001D87F0: xor eax, 0x73
0x001D87F3: mov byte ptr [rbp + 0x353], al
0x001D87F9: movsx ecx, byte ptr [rbp + 0x353]
0x001D8800: mov eax, dword ptr [rbp + 0x338]
0x001D8806: add al, 0x14
0x001D8808: xor eax, ecx
0x001D880A: xor eax, 0x20
0x001D880D: mov byte ptr [rbp + 0x354], al
0x001D8813: movsx ecx, byte ptr [rbp + 0x354]
0x001D881A: mov eax, dword ptr [rbp + 0x338]
0x001D8820: add al, 0x15
0x001D8822: xor eax, ecx
0x001D8824: xor eax, 0x2d
0x001D8827: mov byte ptr [rbp + 0x355], al
0x001D882D: movsx ecx, byte ptr [rbp + 0x355]
0x001D8834: mov eax, dword ptr [rbp + 0x338]
0x001D883A: add al, 0x16
0x001D883C: xor eax, ecx
0x001D883E: xor eax, 0x76
0x001D8841: mov byte ptr [rbp + 0x356], al
0x001D8847: movsx ecx, byte ptr [rbp + 0x356]
0x001D884E: mov eax, dword ptr [rbp + 0x338]
0x001D8854: add al, 0x17
0x001D8856: xor eax, ecx
0x001D8858: xor eax, 0x6d
0x001D885B: mov byte ptr [rbp + 0x357], al
0x001D8861: movsx ecx, byte ptr [rbp + 0x357]
0x001D8868: mov eax, dword ptr [rbp + 0x338]
0x001D886E: add al, 0x18
0x001D8870: xor eax, ecx
0x001D8872: xor eax, 0x74
0x001D8875: mov byte ptr [rbp + 0x358], al
0x001D887B: movsx ecx, byte ptr [rbp + 0x358]
0x001D8882: mov eax, dword ptr [rbp + 0x338]
0x001D8888: add al, 0x19
0x001D888A: xor eax, ecx
0x001D888C: xor eax, 0x31
0x001D888F: mov byte ptr [rbp + 0x359], al
0x001D8895: movsx ecx, byte ptr [rbp + 0x359]
0x001D889C: mov eax, dword ptr [rbp + 0x338]
0x001D88A2: add al, 0x1a
0x001D88A4: xor eax, ecx
0x001D88A6: xor eax, 0x20
0x001D88A9: mov byte ptr [rbp + 0x35a], al
0x001D88AF: movsx ecx, byte ptr [rbp + 0x35a]
0x001D88B6: mov eax, dword ptr [rbp + 0x338]
0x001D88BC: add al, 0x1b
0x001D88BE: xor eax, ecx
0x001D88C0: xor eax, 0x7b
0x001D88C3: mov byte ptr [rbp + 0x35b], al
0x001D88C9: movsx ecx, byte ptr [rbp + 0x35b]
0x001D88D0: mov eax, dword ptr [rbp + 0x338]
0x001D88D6: add al, 0x1c
0x001D88D8: xor eax, ecx
0x001D88DA: xor eax, 0x7d
0x001D88DD: mov byte ptr [rbp + 0x35c], al
0x001D88E3: movsx ecx, byte ptr [rbp + 0x35c]
0x001D88EA: mov eax, dword ptr [rbp + 0x338]
0x001D88F0: add al, 0x1d
0x001D88F2: xor eax, ecx
0x001D88F4: xor eax, 0x20
0x001D88F7: mov byte ptr [rbp + 0x35d], al
0x001D88FD: movsx ecx, byte ptr [rbp + 0x35d]
0x001D8904: mov eax, dword ptr [rbp + 0x338]
0x001D890A: add al, 0x1e
0x001D890C: xor eax, ecx
0x001D890E: xor eax, 0x2d
0x001D8911: mov byte ptr [rbp + 0x35e], al
0x001D8917: movsx ecx, byte ptr [rbp + 0x35e]
0x001D891E: mov eax, dword ptr [rbp + 0x338]
0x001D8924: add al, 0x1f
0x001D8926: xor eax, ecx
0x001D8928: xor eax, 0x76
0x001D892B: mov byte ptr [rbp + 0x35f], al
0x001D8931: movsx ecx, byte ptr [rbp + 0x35f]
0x001D8938: mov eax, dword ptr [rbp + 0x338]
0x001D893E: add al, 0x20
0x001D8940: xor eax, ecx
0x001D8942: xor eax, 0x6d
0x001D8945: mov byte ptr [rbp + 0x360], al
0x001D894B: movsx ecx, byte ptr [rbp + 0x360]
0x001D8952: mov eax, dword ptr [rbp + 0x338]
0x001D8958: add al, 0x21
0x001D895A: xor eax, ecx
0x001D895C: xor eax, 0x74
0x001D895F: mov byte ptr [rbp + 0x361], al
0x001D8965: movsx ecx, byte ptr [rbp + 0x361]
0x001D896C: mov eax, dword ptr [rbp + 0x338]
0x001D8972: add al, 0x22
0x001D8974: xor eax, ecx
0x001D8976: xor eax, 0x32
0x001D8979: mov byte ptr [rbp + 0x362], al
0x001D897F: movsx ecx, byte ptr [rbp + 0x362]
0x001D8986: mov eax, dword ptr [rbp + 0x338]
0x001D898C: add al, 0x23
0x001D898E: xor eax, ecx
0x001D8990: xor eax, 0x20
0x001D8993: mov byte ptr [rbp + 0x363], al
0x001D8999: movsx ecx, byte ptr [rbp + 0x363]
0x001D89A0: mov eax, dword ptr [rbp + 0x338]
0x001D89A6: add al, 0x24
0x001D89A8: xor eax, ecx
0x001D89AA: xor eax, 0x7b
0x001D89AD: mov byte ptr [rbp + 0x364], al
0x001D89B3: movsx ecx, byte ptr [rbp + 0x364]
0x001D89BA: mov eax, dword ptr [rbp + 0x338]
0x001D89C0: add al, 0x25
0x001D89C2: xor eax, ecx
0x001D89C4: xor eax, 0x7d
0x001D89C7: mov byte ptr [rbp + 0x365], al
0x001D89CD: movsx ecx, byte ptr [rbp + 0x365]
0x001D89D4: mov eax, dword ptr [rbp + 0x338]
0x001D89DA: add al, 0x26
0x001D89DC: xor eax, ecx
0x001D89DE: xor eax, 0x20
0x001D89E1: mov byte ptr [rbp + 0x366], al
0x001D89E7: movsx ecx, byte ptr [rbp + 0x366]
0x001D89EE: mov eax, dword ptr [rbp + 0x338]
0x001D89F4: add al, 0x27
0x001D89F6: xor eax, ecx
0x001D89F8: xor eax, 0x2d
0x001D89FB: mov byte ptr [rbp + 0x367], al
0x001D8A01: movsx ecx, byte ptr [rbp + 0x367]
0x001D8A08: mov eax, dword ptr [rbp + 0x338]
0x001D8A0E: add al, 0x28
0x001D8A10: xor eax, ecx
0x001D8A12: xor eax, 0x76
0x001D8A15: mov byte ptr [rbp + 0x368], al
0x001D8A1B: movsx ecx, byte ptr [rbp + 0x368]
0x001D8A22: mov eax, dword ptr [rbp + 0x338]
0x001D8A28: add al, 0x29
0x001D8A2A: xor eax, ecx
0x001D8A2C: xor eax, 0x6d
0x001D8A2F: mov byte ptr [rbp + 0x369], al
0x001D8A35: movsx ecx, byte ptr [rbp + 0x369]
0x001D8A3C: mov eax, dword ptr [rbp + 0x338]
0x001D8A42: add al, 0x2a
0x001D8A44: xor eax, ecx
0x001D8A46: xor eax, 0x74
0x001D8A49: mov byte ptr [rbp + 0x36a], al
0x001D8A4F: movsx ecx, byte ptr [rbp + 0x36a]
0x001D8A56: mov eax, dword ptr [rbp + 0x338]
0x001D8A5C: add al, 0x2b
0x001D8A5E: xor eax, ecx
0x001D8A60: xor eax, 0x33
0x001D8A63: mov byte ptr [rbp + 0x36b], al
0x001D8A69: movsx ecx, byte ptr [rbp + 0x36b]
0x001D8A70: mov eax, dword ptr [rbp + 0x338]
0x001D8A76: add al, 0x2c
0x001D8A78: xor eax, ecx
0x001D8A7A: xor eax, 0x20
0x001D8A7D: mov byte ptr [rbp + 0x36c], al
0x001D8A83: movsx ecx, byte ptr [rbp + 0x36c]
0x001D8A8A: mov eax, dword ptr [rbp + 0x338]
0x001D8A90: add al, 0x2d
0x001D8A92: xor eax, ecx
0x001D8A94: xor eax, 0x7b
0x001D8A97: mov byte ptr [rbp + 0x36d], al
0x001D8A9D: movsx ecx, byte ptr [rbp + 0x36d]
0x001D8AA4: mov eax, dword ptr [rbp + 0x338]
0x001D8AAA: add al, 0x2e
0x001D8AAC: xor eax, ecx
0x001D8AAE: xor eax, 0x7d
0x001D8AB1: mov byte ptr [rbp + 0x36e], al
0x001D8AB7: xor eax, eax
0x001D8AB9: mov byte ptr [rbp + 0x36f], al
0x001D8ABF: movzx eax, byte ptr [rbp + 0x340]
0x001D8AC6: lea rdx, [rbp + 0x4a0]
0x001D8ACD: lea rcx, [rbp + 0x338]
0x001D8AD4: call 0x1401372a0
0x001D8AD9: nop
0x001D8ADA: cmp qword ptr [rax + 0x18], 0x10
0x001D8ADF: jb 0x1401d8ae4
0x001D8AE1: mov rax, qword ptr [rax]
0x001D8AE4: lea rdx, [rbx + 8]
0x001D8AE8: mov qword ptr [rsp + 0x20], rsi
0x001D8AED: lea r9, [rbx + 0x264]
0x001D8AF4: lea r8, [rbx + 0x260]
0x001D8AFB: mov rcx, rax
0x001D8AFE: call 0x1401d42c0
0x001D8B03: nop
0x001D8B04: lea rcx, [rbp + 0x4a0]
0x001D8B0B: call 0x140032ef0
0x001D8B10: mov esi, dword ptr [rbp + 0x28]
0x001D8B13: mov ecx, dword ptr [rbp + 0xa8]
0x001D8B19: jmp 0x1401d8b1f
0x001D8B1B: mov ecx, dword ptr [rsp + 0x40]
0x001D8B1F: mov edx, dword ptr [rbx + 0x25c]
0x001D8B25: test edx, edx
0x001D8B27: jle 0x1401d8f22
0x001D8B2D: mov eax, esi
0x001D8B2F: xorps xmm2, xmm2
0x001D8B32: cvtsi2sd xmm2, rax
0x001D8B37: sub esi, ecx
0x001D8B39: mov eax, esi
0x001D8B3B: xorps xmm1, xmm1
0x001D8B3E: cvtsi2sd xmm1, rax
0x001D8B43: movd xmm0, edx
0x001D8B47: cvtdq2pd xmm0, xmm0
0x001D8B4B: divsd xmm0, xmm6
0x001D8B4F: mulsd xmm1, xmm0
0x001D8B53: subsd xmm2, xmm1
0x001D8B57: cvttsd2si rax, xmm2
0x001D8B5C: mov dword ptr [rsp + 0x78], eax
0x001D8B60: mov dword ptr [rbp + 0x370], 0x50
0x001D8B6A: mov eax, dword ptr [rbp + 0x370]
0x001D8B70: add al, 0x50
0x001D8B72: movsx ecx, al
0x001D8B75: xor ecx, 0x46
0x001D8B78: mov dword ptr [rbp + 0x374], ecx
0x001D8B7E: mov eax, dword ptr [rbp + 0x374]
0x001D8B84: mov ecx, dword ptr [rbp + 0x370]
0x001D8B8A: xor ecx, eax
0x001D8B8C: xor ecx, 0x7b
0x001D8B8F: mov byte ptr [rbp + 0x378], cl
0x001D8B95: movsx ecx, byte ptr [rbp + 0x378]
0x001D8B9C: mov eax, dword ptr [rbp + 0x370]
0x001D8BA2: inc al
0x001D8BA4: xor eax, ecx
0x001D8BA6: xor eax, 0x7d
0x001D8BA9: mov byte ptr [rbp + 0x379], al
0x001D8BAF: movsx ecx, byte ptr [rbp + 0x379]
0x001D8BB6: mov eax, dword ptr [rbp + 0x370]
0x001D8BBC: add al, 2
0x001D8BBE: xor eax, ecx
0x001D8BC0: xor eax, 0x3a
0x001D8BC3: mov byte ptr [rbp + 0x37a], al
0x001D8BC9: movsx ecx, byte ptr [rbp + 0x37a]
0x001D8BD0: mov eax, dword ptr [rbp + 0x370]
0x001D8BD6: add al, 3
0x001D8BD8: xor eax, ecx
0x001D8BDA: xor eax, 0x20
0x001D8BDD: mov byte ptr [rbp + 0x37b], al
0x001D8BE3: movsx ecx, byte ptr [rbp + 0x37b]
0x001D8BEA: mov eax, dword ptr [rbp + 0x370]
0x001D8BF0: add al, 4
0x001D8BF2: xor eax, ecx
0x001D8BF4: xor eax, 0x73
0x001D8BF7: mov byte ptr [rbp + 0x37c], al
0x001D8BFD: movsx ecx, byte ptr [rbp + 0x37c]
0x001D8C04: mov eax, dword ptr [rbp + 0x370]
0x001D8C0A: add al, 5
0x001D8C0C: xor eax, ecx
0x001D8C0E: xor eax, 0x65
0x001D8C11: mov byte ptr [rbp + 0x37d], al
0x001D8C17: movsx ecx, byte ptr [rbp + 0x37d]
0x001D8C1E: mov eax, dword ptr [rbp + 0x370]
0x001D8C24: add al, 6
0x001D8C26: xor eax, ecx
0x001D8C28: xor eax, 0x74
0x001D8C2B: mov byte ptr [rbp + 0x37e], al
0x001D8C31: movsx ecx, byte ptr [rbp + 0x37e]
0x001D8C38: mov eax, dword ptr [rbp + 0x370]
0x001D8C3E: add al, 7
0x001D8C40: xor eax, ecx
0x001D8C42: xor eax, 0x20
0x001D8C45: mov byte ptr [rbp + 0x37f], al
0x001D8C4B: movsx ecx, byte ptr [rbp + 0x37f]
0x001D8C52: mov eax, dword ptr [rbp + 0x370]
0x001D8C58: add al, 8
0x001D8C5A: xor eax, ecx
0x001D8C5C: xor eax, 0x56
0x001D8C5F: mov byte ptr [rbp + 0x380], al
0x001D8C65: movsx ecx, byte ptr [rbp + 0x380]
0x001D8C6C: mov eax, dword ptr [rbp + 0x370]
0x001D8C72: add al, 9
0x001D8C74: xor eax, ecx
0x001D8C76: xor eax, 0x52
0x001D8C79: mov byte ptr [rbp + 0x381], al
0x001D8C7F: movsx ecx, byte ptr [rbp + 0x381]
0x001D8C86: mov eax, dword ptr [rbp + 0x370]
0x001D8C8C: add al, 0xa
0x001D8C8E: xor eax, ecx
0x001D8C90: xor eax, 0x41
0x001D8C93: mov byte ptr [rbp + 0x382], al
0x001D8C99: movsx ecx, byte ptr [rbp + 0x382]
0x001D8CA0: mov eax, dword ptr [rbp + 0x370]
0x001D8CA6: add al, 0xb
0x001D8CA8: xor eax, ecx
0x001D8CAA: xor eax, 0x4d
0x001D8CAD: mov byte ptr [rbp + 0x383], al
0x001D8CB3: movsx ecx, byte ptr [rbp + 0x383]
0x001D8CBA: mov eax, dword ptr [rbp + 0x370]
0x001D8CC0: add al, 0xc
0x001D8CC2: xor eax, ecx
0x001D8CC4: xor eax, 0x20
0x001D8CC7: mov byte ptr [rbp + 0x384], al
0x001D8CCD: movsx ecx, byte ptr [rbp + 0x384]
0x001D8CD4: mov eax, dword ptr [rbp + 0x370]
0x001D8CDA: add al, 0xd
0x001D8CDC: xor eax, ecx
0x001D8CDE: xor eax, 0x72
0x001D8CE1: mov byte ptr [rbp + 0x385], al
0x001D8CE7: movsx ecx, byte ptr [rbp + 0x385]
0x001D8CEE: mov eax, dword ptr [rbp + 0x370]
0x001D8CF4: add al, 0xe
0x001D8CF6: xor eax, ecx
0x001D8CF8: xor eax, 0x65
0x001D8CFB: mov byte ptr [rbp + 0x386], al
0x001D8D01: movsx ecx, byte ptr [rbp + 0x386]
0x001D8D08: mov eax, dword ptr [rbp + 0x370]
0x001D8D0E: add al, 0xf
0x001D8D10: xor eax, ecx
0x001D8D12: xor eax, 0x66
0x001D8D15: mov byte ptr [rbp + 0x387], al
0x001D8D1B: movsx ecx, byte ptr [rbp + 0x387]
0x001D8D22: mov eax, dword ptr [rbp + 0x370]
0x001D8D28: add al, 0x10
0x001D8D2A: xor eax, ecx
0x001D8D2C: xor eax, 0x72
0x001D8D2F: mov byte ptr [rbp + 0x388], al
0x001D8D35: movsx ecx, byte ptr [rbp + 0x388]
0x001D8D3C: mov eax, dword ptr [rbp + 0x370]
0x001D8D42: add al, 0x11
0x001D8D44: xor eax, ecx
0x001D8D46: xor eax, 0x65
0x001D8D49: mov byte ptr [rbp + 0x389], al
0x001D8D4F: movsx ecx, byte ptr [rbp + 0x389]
0x001D8D56: mov eax, dword ptr [rbp + 0x370]
0x001D8D5C: add al, 0x12
0x001D8D5E: xor eax, ecx
0x001D8D60: xor eax, 0x73
0x001D8D63: mov byte ptr [rbp + 0x38a], al
0x001D8D69: movsx ecx, byte ptr [rbp + 0x38a]
0x001D8D70: mov eax, dword ptr [rbp + 0x370]
0x001D8D76: add al, 0x13
0x001D8D78: xor eax, ecx
0x001D8D7A: xor eax, 0x68
0x001D8D7D: mov byte ptr [rbp + 0x38b], al
0x001D8D83: movsx ecx, byte ptr [rbp + 0x38b]
0x001D8D8A: mov eax, dword ptr [rbp + 0x370]
0x001D8D90: add al, 0x14
0x001D8D92: xor eax, ecx
0x001D8D94: xor eax, 0x20
0x001D8D97: mov byte ptr [rbp + 0x38c], al
0x001D8D9D: movsx ecx, byte ptr [rbp + 0x38c]
0x001D8DA4: mov eax, dword ptr [rbp + 0x370]
0x001D8DAA: add al, 0x15
0x001D8DAC: xor eax, ecx
0x001D8DAE: xor eax, 0x72
0x001D8DB1: mov byte ptr [rbp + 0x38d], al
0x001D8DB7: movsx ecx, byte ptr [rbp + 0x38d]
0x001D8DBE: mov eax, dword ptr [rbp + 0x370]
0x001D8DC4: add al, 0x16
0x001D8DC6: xor eax, ecx
0x001D8DC8: xor eax, 0x61
0x001D8DCB: mov byte ptr [rbp + 0x38e], al
0x001D8DD1: movsx ecx, byte ptr [rbp + 0x38e]
0x001D8DD8: mov eax, dword ptr [rbp + 0x370]
0x001D8DDE: add al, 0x17
0x001D8DE0: xor eax, ecx
0x001D8DE2: xor eax, 0x74
0x001D8DE5: mov byte ptr [rbp + 0x38f], al
0x001D8DEB: movsx ecx, byte ptr [rbp + 0x38f]
0x001D8DF2: mov eax, dword ptr [rbp + 0x370]
0x001D8DF8: add al, 0x18
0x001D8DFA: xor eax, ecx
0x001D8DFC: xor eax, 0x65
0x001D8DFF: mov byte ptr [rbp + 0x390], al
0x001D8E05: movsx ecx, byte ptr [rbp + 0x390]
0x001D8E0C: mov eax, dword ptr [rbp + 0x370]
0x001D8E12: add al, 0x19
0x001D8E14: xor eax, ecx
0x001D8E16: xor eax, 0x20
0x001D8E19: mov byte ptr [rbp + 0x391], al
0x001D8E1F: movsx ecx, byte ptr [rbp + 0x391]
0x001D8E26: mov eax, dword ptr [rbp + 0x370]
0x001D8E2C: add al, 0x1a
0x001D8E2E: xor eax, ecx
0x001D8E30: xor eax, 0x2d
0x001D8E33: mov byte ptr [rbp + 0x392], al
0x001D8E39: movsx ecx, byte ptr [rbp + 0x392]
0x001D8E40: mov eax, dword ptr [rbp + 0x370]
0x001D8E46: add al, 0x1b
0x001D8E48: xor eax, ecx
0x001D8E4A: xor eax, 0x76
0x001D8E4D: mov byte ptr [rbp + 0x393], al
0x001D8E53: movsx ecx, byte ptr [rbp + 0x393]
0x001D8E5A: mov eax, dword ptr [rbp + 0x370]
0x001D8E60: add al, 0x1c
0x001D8E62: xor eax, ecx
0x001D8E64: xor eax, 0x6d
0x001D8E67: mov byte ptr [rbp + 0x394], al
0x001D8E6D: movsx ecx, byte ptr [rbp + 0x394]
0x001D8E74: mov eax, dword ptr [rbp + 0x370]
0x001D8E7A: add al, 0x1d
0x001D8E7C: xor eax, ecx
0x001D8E7E: xor eax, 0x72
0x001D8E81: mov byte ptr [rbp + 0x395], al
0x001D8E87: movsx ecx, byte ptr [rbp + 0x395]
0x001D8E8E: mov eax, dword ptr [rbp + 0x370]
0x001D8E94: add al, 0x1e
0x001D8E96: xor eax, ecx
0x001D8E98: xor eax, 0x20
0x001D8E9B: mov byte ptr [rbp + 0x396], al
0x001D8EA1: movsx ecx, byte ptr [rbp + 0x396]
0x001D8EA8: mov eax, dword ptr [rbp + 0x370]
0x001D8EAE: add al, 0x1f
0x001D8EB0: xor eax, ecx
0x001D8EB2: xor eax, 0x7b
0x001D8EB5: mov byte ptr [rbp + 0x397], al
0x001D8EBB: movsx ecx, byte ptr [rbp + 0x397]
0x001D8EC2: mov eax, dword ptr [rbp + 0x370]
0x001D8EC8: add al, 0x20
0x001D8ECA: xor eax, ecx
0x001D8ECC: xor eax, 0x7d
0x001D8ECF: mov byte ptr [rbp + 0x398], al
0x001D8ED5: xor eax, eax
0x001D8ED7: mov byte ptr [rbp + 0x399], al
0x001D8EDD: movzx eax, byte ptr [rbp + 0x378]
0x001D8EE4: lea rdx, [rbp + 0x4c0]
0x001D8EEB: lea rcx, [rbp + 0x370]
0x001D8EF2: call 0x1401eb3d0
0x001D8EF7: nop
0x001D8EF8: cmp qword ptr [rax + 0x18], 0x10
0x001D8EFD: jb 0x1401d8f02
0x001D8EFF: mov rax, qword ptr [rax]
0x001D8F02: lea rdx, [rbx + 8]
0x001D8F06: lea r8, [rbx + 0x25c]
0x001D8F0D: mov rcx, rax
0x001D8F10: call 0x14017b170
0x001D8F15: nop
0x001D8F16: lea rcx, [rbp + 0x4c0]
0x001D8F1D: call 0x140032ef0
0x001D8F22: cmp dword ptr [rdi + rbx + 0x144], 0
0x001D8F2A: je 0x1401d8f6e
0x001D8F2C: cmp dword ptr [rbp - 0x4c], 0
0x001D8F30: jne 0x1401d8f3c
0x001D8F32: mov eax, dword ptr [rdi + rbx + 0x188]
0x001D8F39: mov dword ptr [rbp - 0x4c], eax
0x001D8F3C: cmp dword ptr [rbp - 0x58], 0
0x001D8F40: jne 0x1401d8f4c
0x001D8F42: mov eax, dword ptr [rdi + rbx + 0x17c]
0x001D8F49: mov dword ptr [rbp - 0x58], eax
0x001D8F4C: cmp dword ptr [rbp - 0x64], 0
0x001D8F50: jne 0x1401d8f5c
0x001D8F52: mov eax, dword ptr [rdi + rbx + 0x170]
0x001D8F59: mov dword ptr [rbp - 0x64], eax
0x001D8F5C: cmp dword ptr [rsp + 0x78], 0
0x001D8F61: jne 0x1401d8f6e
0x001D8F63: mov eax, dword ptr [rdi + rbx + 0x14c]
0x001D8F6A: mov dword ptr [rsp + 0x78], eax
0x001D8F6E: movaps xmm6, xmmword ptr [rsp + 0x70]
0x001D8F73: movups xmmword ptr [r13], xmm6
0x001D8F78: movaps xmm5, xmmword ptr [rbp - 0x80]
0x001D8F7C: movups xmmword ptr [r13 + 0x10], xmm5
0x001D8F81: movaps xmm4, xmmword ptr [rbp - 0x70]
0x001D8F85: movups xmmword ptr [r13 + 0x20], xmm4
0x001D8F8A: movaps xmm3, xmmword ptr [rbp - 0x60]
0x001D8F8E: movups xmmword ptr [r13 + 0x30], xmm3
0x001D8F93: movaps xmm2, xmmword ptr [rbp - 0x50]
0x001D8F97: movups xmmword ptr [r13 + 0x40], xmm2
0x001D8F9C: movsd xmm1, qword ptr [rbp - 0x40]
0x001D8FA1: movsd qword ptr [r13 + 0x50], xmm1
0x001D8FA7: mov edx, dword ptr [rbp - 0x38]
0x001D8FAA: mov dword ptr [r13 + 0x58], edx
0x001D8FAE: movsxd rax, dword ptr [rsp + 0x3c]
0x001D8FB3: mov r8, rax
0x001D8FB6: add rax, 7
0x001D8FBA: imul rcx, rax, 0x5c
0x001D8FBE: movups xmmword ptr [rcx + rbx], xmm6
0x001D8FC2: movups xmmword ptr [rcx + rbx + 0x10], xmm5
0x001D8FC7: movups xmmword ptr [rcx + rbx + 0x20], xmm4
0x001D8FCC: movups xmmword ptr [rcx + rbx + 0x30], xmm3
0x001D8FD1: movups xmmword ptr [rcx + rbx + 0x40], xmm2
0x001D8FD6: movsd qword ptr [rcx + rbx + 0x50], xmm1
0x001D8FDC: mov dword ptr [rcx + rbx + 0x58], edx
0x001D8FE0: mov byte ptr [rbx + r8 + 0x398], 1
0x001D8FE9: mov al, 1
0x001D8FEB: jmp 0x1401d9451
0x001D8FF0: mov dword ptr [rbp + 0x440], 0x7a
0x001D8FFA: mov eax, dword ptr [rbp + 0x440]
0x001D9000: xor eax, 0x7b
0x001D9003: add eax, 4
0x001D9006: mov byte ptr [rbp + 0x444], al
0x001D900C: movsx ecx, byte ptr [rbp + 0x444]
0x001D9013: xor ecx, 0x7d
0x001D9016: add ecx, 4
0x001D9019: mov byte ptr [rbp + 0x445], cl
0x001D901F: movsx ecx, byte ptr [rbp + 0x445]
0x001D9026: xor ecx, 0x3a
0x001D9029: add ecx, 4
0x001D902C: mov byte ptr [rbp + 0x446], cl
0x001D9032: movsx ecx, byte ptr [rbp + 0x446]
0x001D9039: xor ecx, 0x20
0x001D903C: add ecx, 4
0x001D903F: mov byte ptr [rbp + 0x447], cl
0x001D9045: movsx ecx, byte ptr [rbp + 0x447]
0x001D904C: xor ecx, 0x69
0x001D904F: add ecx, 4
0x001D9052: mov byte ptr [rbp + 0x448], cl
0x001D9058: movsx ecx, byte ptr [rbp + 0x448]
0x001D905F: xor ecx, 0x6e
0x001D9062: add ecx, 4
0x001D9065: mov byte ptr [rbp + 0x449], cl
0x001D906B: movsx ecx, byte ptr [rbp + 0x449]
0x001D9072: xor ecx, 0x76
0x001D9075: add ecx, 4
0x001D9078: mov byte ptr [rbp + 0x44a], cl
0x001D907E: movsx ecx, byte ptr [rbp + 0x44a]
0x001D9085: xor ecx, 0x61
0x001D9088: add ecx, 4
0x001D908B: mov byte ptr [rbp + 0x44b], cl
0x001D9091: movsx ecx, byte ptr [rbp + 0x44b]
0x001D9098: xor ecx, 0x6c
0x001D909B: add ecx, 4
0x001D909E: mov byte ptr [rbp + 0x44c], cl
0x001D90A4: movsx ecx, byte ptr [rbp + 0x44c]
0x001D90AB: xor ecx, 0x69
0x001D90AE: add ecx, 4
0x001D90B1: mov byte ptr [rbp + 0x44d], cl
0x001D90B7: movsx ecx, byte ptr [rbp + 0x44d]
0x001D90BE: xor ecx, 0x64
0x001D90C1: add ecx, 4
0x001D90C4: mov byte ptr [rbp + 0x44e], cl
0x001D90CA: movsx ecx, byte ptr [rbp + 0x44e]
0x001D90D1: xor ecx, 0x20
0x001D90D4: add ecx, 4
0x001D90D7: mov byte ptr [rbp + 0x44f], cl
0x001D90DD: movsx ecx, byte ptr [rbp + 0x44f]
0x001D90E4: xor ecx, 0x73
0x001D90E7: add ecx, 4
0x001D90EA: mov byte ptr [rbp + 0x450], cl
0x001D90F0: movsx ecx, byte ptr [rbp + 0x450]
0x001D90F7: xor ecx, 0x74
0x001D90FA: add ecx, 4
0x001D90FD: mov byte ptr [rbp + 0x451], cl
0x001D9103: movsx ecx, byte ptr [rbp + 0x451]
0x001D910A: xor ecx, 0x72
0x001D910D: add ecx, 4
0x001D9110: mov byte ptr [rbp + 0x452], cl
0x001D9116: movsx ecx, byte ptr [rbp + 0x452]
0x001D911D: xor ecx, 0x61
0x001D9120: add ecx, 4
0x001D9123: mov byte ptr [rbp + 0x453], cl
0x001D9129: movsx ecx, byte ptr [rbp + 0x453]
0x001D9130: xor ecx, 0x70
0x001D9133: add ecx, 4
0x001D9136: mov byte ptr [rbp + 0x454], cl
0x001D913C: movsx ecx, byte ptr [rbp + 0x454]
0x001D9143: xor ecx, 0x20
0x001D9146: add ecx, 4
0x001D9149: mov byte ptr [rbp + 0x455], cl
0x001D914F: movsx ecx, byte ptr [rbp + 0x455]
0x001D9156: xor ecx, 0x6c
0x001D9159: add ecx, 4
0x001D915C: mov byte ptr [rbp + 0x456], cl
0x001D9162: movsx ecx, byte ptr [rbp + 0x456]
0x001D9169: xor ecx, 0x69
0x001D916C: add ecx, 4
0x001D916F: mov byte ptr [rbp + 0x457], cl
0x001D9175: movsx ecx, byte ptr [rbp + 0x457]
0x001D917C: xor ecx, 0x6d
0x001D917F: add ecx, 4
0x001D9182: mov byte ptr [rbp + 0x458], cl
0x001D9188: movsx ecx, byte ptr [rbp + 0x458]
0x001D918F: xor ecx, 0x69
0x001D9192: add ecx, 4
0x001D9195: mov byte ptr [rbp + 0x459], cl
0x001D919B: movsx ecx, byte ptr [rbp + 0x459]
0x001D91A2: xor ecx, 0x74
0x001D91A5: add ecx, 4
0x001D91A8: mov byte ptr [rbp + 0x45a], cl
0x001D91AE: movsx ecx, byte ptr [rbp + 0x45a]
0x001D91B5: xor ecx, 0x73
0x001D91B8: add ecx, 4
0x001D91BB: mov byte ptr [rbp + 0x45b], cl
0x001D91C1: mov byte ptr [rbp + 0x45c], 0
0x001D91C8: movzx eax, byte ptr [rbp + 0x444]
0x001D91CF: lea rdx, [rbp + 0x4e0]
0x001D91D6: lea rcx, [rbp + 0x440]
0x001D91DD: call 0x1401ebfa0
0x001D91E2: nop
0x001D91E3: cmp qword ptr [rax + 0x18], 0x10
0x001D91E8: jb 0x1401d91ed
0x001D91EA: mov rax, qword ptr [rax]
0x001D91ED: lea rdx, [rbx + 8]
0x001D91F1: mov rcx, rax
0x001D91F4: call 0x140040530
0x001D91F9: nop
0x001D91FA: lea rcx, [rbp + 0x4e0]
0x001D9201: jmp 0x1401d944a
0x001D9206: mov dword ptr [rbp + 0x418], 0x3c
0x001D9210: mov dword ptr [rbp + 0x41c], 0x53
0x001D921A: mov eax, dword ptr [rbp + 0x41c]
0x001D9220: xor eax, 0x47
0x001D9223: mov byte ptr [rbp + 0x420], al
0x001D9229: movsx ecx, byte ptr [rbp + 0x420]
0x001D9230: xor ecx, 0x41
0x001D9233: mov byte ptr [rbp + 0x421], cl
0x001D9239: movsx ecx, byte ptr [rbp + 0x421]
0x001D9240: xor ecx, 6
0x001D9243: mov byte ptr [rbp + 0x422], cl
0x001D9249: movsx ecx, byte ptr [rbp + 0x422]
0x001D9250: xor ecx, 0x1c
0x001D9253: mov byte ptr [rbp + 0x423], cl
0x001D9259: movsx ecx, byte ptr [rbp + 0x423]
0x001D9260: xor ecx, 0x49
0x001D9263: mov byte ptr [rbp + 0x424], cl
0x001D9269: movsx ecx, byte ptr [rbp + 0x424]
0x001D9270: xor ecx, 0x52
0x001D9273: mov byte ptr [rbp + 0x425], cl
0x001D9279: movsx ecx, byte ptr [rbp + 0x425]
0x001D9280: xor ecx, 0x5d
0x001D9283: mov byte ptr [rbp + 0x426], cl
0x001D9289: movsx ecx, byte ptr [rbp + 0x426]
0x001D9290: xor ecx, 0x5e
0x001D9293: mov byte ptr [rbp + 0x427], cl
0x001D9299: movsx ecx, byte ptr [rbp + 0x427]
0x001D92A0: xor ecx, 0x50
0x001D92A3: mov byte ptr [rbp + 0x428], cl
0x001D92A9: movsx ecx, byte ptr [rbp + 0x428]
0x001D92B0: xor ecx, 0x59
0x001D92B3: mov byte ptr [rbp + 0x429], cl
0x001D92B9: movsx ecx, byte ptr [rbp + 0x429]
0x001D92C0: xor ecx, 0x1c
0x001D92C3: mov byte ptr [rbp + 0x42a], cl
0x001D92C9: movsx ecx, byte ptr [rbp + 0x42a]
0x001D92D0: xor ecx, 0x48
0x001D92D3: mov byte ptr [rbp + 0x42b], cl
0x001D92D9: movsx ecx, byte ptr [rbp + 0x42b]
0x001D92E0: xor ecx, 0x53
0x001D92E3: mov byte ptr [rbp + 0x42c], cl
0x001D92E9: movsx ecx, byte ptr [rbp + 0x42c]
0x001D92F0: xor ecx, 0x1c
0x001D92F3: mov byte ptr [rbp + 0x42d], cl
0x001D92F9: movsx ecx, byte ptr [rbp + 0x42d]
0x001D9300: xor ecx, 0x5a
0x001D9303: mov byte ptr [rbp + 0x42e], cl
0x001D9309: movsx ecx, byte ptr [rbp + 0x42e]
0x001D9310: xor ecx, 0x55
0x001D9313: mov byte ptr [rbp + 0x42f], cl
0x001D9319: movsx ecx, byte ptr [rbp + 0x42f]
0x001D9320: xor ecx, 0x52
0x001D9323: mov byte ptr [rbp + 0x430], cl
0x001D9329: movsx ecx, byte ptr [rbp + 0x430]
0x001D9330: xor ecx, 0x58
0x001D9333: mov byte ptr [rbp + 0x431], cl
0x001D9339: movsx ecx, byte ptr [rbp + 0x431]
0x001D9340: xor ecx, 0x1c
0x001D9343: mov byte ptr [rbp + 0x432], cl
0x001D9349: movsx ecx, byte ptr [rbp + 0x432]
0x001D9350: xor ecx, 0x4f
0x001D9353: mov byte ptr [rbp + 0x433], cl
0x001D9359: movsx ecx, byte ptr [rbp + 0x433]
0x001D9360: xor ecx, 0x48
0x001D9363: mov byte ptr [rbp + 0x434], cl
0x001D9369: movsx ecx, byte ptr [rbp + 0x434]
0x001D9370: xor ecx, 0x4e
0x001D9373: mov byte ptr [rbp + 0x435], cl
0x001D9379: movsx ecx, byte ptr [rbp + 0x435]
0x001D9380: xor ecx, 0x5d
0x001D9383: mov byte ptr [rbp + 0x436], cl
0x001D9389: movsx ecx, byte ptr [rbp + 0x436]
0x001D9390: xor ecx, 0x4c
0x001D9393: mov byte ptr [rbp + 0x437], cl
0x001D9399: movsx ecx, byte ptr [rbp + 0x437]
0x001D93A0: xor ecx, 0x1c
0x001D93A3: mov byte ptr [rbp + 0x438], cl
0x001D93A9: movsx ecx, byte ptr [rbp + 0x438]
0x001D93B0: xor ecx, 0x50
0x001D93B3: mov byte ptr [rbp + 0x439], cl
0x001D93B9: movsx ecx, byte ptr [rbp + 0x439]
0x001D93C0: xor ecx, 0x55
0x001D93C3: mov byte ptr [rbp + 0x43a], cl
0x001D93C9: movsx ecx, byte ptr [rbp + 0x43a]
0x001D93D0: xor ecx, 0x51
0x001D93D3: mov byte ptr [rbp + 0x43b], cl
0x001D93D9: movsx ecx, byte ptr [rbp + 0x43b]
0x001D93E0: xor ecx, 0x55
0x001D93E3: mov byte ptr [rbp + 0x43c], cl
0x001D93E9: movsx ecx, byte ptr [rbp + 0x43c]
0x001D93F0: xor ecx, 0x48
0x001D93F3: mov byte ptr [rbp + 0x43d], cl
0x001D93F9: movsx ecx, byte ptr [rbp + 0x43d]
0x001D9400: xor ecx, 0x4f
0x001D9403: mov byte ptr [rbp + 0x43e], cl
0x001D9409: xor eax, eax
0x001D940B: mov byte ptr [rbp + 0x43f], al
0x001D9411: movzx eax, byte ptr [rbp + 0x420]
0x001D9418: lea rdx, [rbp + 0x500]
0x001D941F: lea rcx, [rbp + 0x418]
0x001D9426: call 0x1401b62e0
0x001D942B: nop
0x001D942C: cmp qword ptr [rax + 0x18], 0x10
0x001D9431: jb 0x1401d9436
0x001D9433: mov rax, qword ptr [rax]
0x001D9436: lea rdx, [rbx + 8]
0x001D943A: mov rcx, rax
0x001D943D: call 0x140040530
0x001D9442: nop
0x001D9443: lea rcx, [rbp + 0x500]
0x001D944A: call 0x140032ef0
0x001D944F: xor al, al
0x001D9451: mov rcx, qword ptr [rbp + 0x7b0]
0x001D9458: xor rcx, rsp
0x001D945B: call 0x1403b24c0
0x001D9460: mov rbx, qword ptr [rsp + 0x928]
0x001D9468: movaps xmm6, xmmword ptr [rsp + 0x8c0]
0x001D9470: add rsp, 0x8d0
0x001D9477: pop r15
0x001D9479: pop r14
0x001D947B: pop r13
0x001D947D: pop r12
0x001D947F: pop rdi
0x001D9480: pop rsi
0x001D9481: pop rbp
0x001D9482: ret
```
