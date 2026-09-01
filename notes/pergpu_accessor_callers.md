# Callers of per-GPU accessor 0xE3F60

direct callers: 5

| callsite | PDATA |
|---|---|
| `0x0006FA51` | `0x0006F940..0x000700E0` |
| `0x0007FC7A` | `0x0007F0F0..0x000831BB` |
| `0x000A9233` | `0x000A8650..0x000A9414` |
| `0x000A9247` | `0x000A8650..0x000A9414` |
| `0x000B2426` | `0x000B20D0..0x000B251B` |

## Contexts

### `0x0006FA51`

```asm
0x0006F9FB: mov r14d, esi
0x0006F9FE: lea rcx, [r13 + 0x300]
0x0006FA05: call 0x14013c5a0
0x0006FA0A: mov rbx, qword ptr [rax]
0x0006FA0D: mov rdi, qword ptr [rax + 8]
0x0006FA11: cmp rbx, rdi
0x0006FA14: je 0x14006fd27
0x0006FA1A: nop word ptr [rax + rax]
0x0006FA20: mov rsi, qword ptr [rbx + 8]
0x0006FA24: mov r15, qword ptr [rbx]
0x0006FA27: test rsi, rsi
0x0006FA2A: je 0x14006fa30
0x0006FA2C: lock inc dword ptr [rsi + 8]
0x0006FA30: mov qword ptr [rbp + 0x50], rsi
0x0006FA34: mov qword ptr [rbp + 0x48], r15
0x0006FA38: lea rdx, [rbp + 0x90]
0x0006FA3F: mov rcx, r15
0x0006FA42: call 0x140084a60
0x0006FA47: mov edx, r14d
0x0006FA4A: lea rcx, [rbp + 0x190]
0x0006FA51: call 0x1400e3f60
0x0006FA56: lea rcx, [rsp + 0x60]
0x0006FA5B: movups xmm0, xmmword ptr [rax]
0x0006FA5E: movups xmmword ptr [rcx], xmm0
0x0006FA61: movups xmm1, xmmword ptr [rax + 0x10]
0x0006FA65: movups xmmword ptr [rcx + 0x10], xmm1
0x0006FA69: movups xmm0, xmmword ptr [rax + 0x20]
0x0006FA6D: movups xmmword ptr [rcx + 0x20], xmm0
0x0006FA71: movups xmm1, xmmword ptr [rax + 0x30]
0x0006FA75: movups xmmword ptr [rcx + 0x30], xmm1
0x0006FA79: movups xmm0, xmmword ptr [rax + 0x40]
0x0006FA7D: movups xmmword ptr [rcx + 0x40], xmm0
0x0006FA81: movups xmm1, xmmword ptr [rax + 0x50]
0x0006FA85: movups xmmword ptr [rcx + 0x50], xmm1
0x0006FA89: movups xmm0, xmmword ptr [rax + 0x60]
0x0006FA8D: movups xmmword ptr [rcx + 0x60], xmm0
0x0006FA91: lea rcx, [rcx + 0x80]
0x0006FA98: movups xmm1, xmmword ptr [rax + 0x70]
0x0006FA9C: movups xmmword ptr [rcx - 0x10], xmm1
0x0006FAA0: sub rax, -0x80
0x0006FAA4: movups xmm0, xmmword ptr [rax]
0x0006FAA7: movups xmmword ptr [rcx], xmm0
0x0006FAAA: movups xmm1, xmmword ptr [rax + 0x10]
0x0006FAAE: movups xmmword ptr [rcx + 0x10], xmm1
0x0006FAB2: movups xmm0, xmmword ptr [rax + 0x20]
0x0006FAB6: movups xmmword ptr [rcx + 0x20], xmm0
0x0006FABA: movups xmm1, xmmword ptr [rax + 0x30]
0x0006FABE: movups xmmword ptr [rcx + 0x30], xmm1
0x0006FAC2: movups xmm0, xmmword ptr [rax + 0x40]
0x0006FAC6: movups xmmword ptr [rcx + 0x40], xmm0
0x0006FACA: mov rax, qword ptr [rax + 0x50]
```

### `0x0007FC7A`

```asm
0x0007FC27: call 0x1403b20dc
0x0007FC2C: jmp 0x14007fc31
0x0007FC2E: xor r15d, r15d
0x0007FC31: test bl, bl
0x0007FC33: je 0x14007fd4a
0x0007FC39: cmp qword ptr [rsi + 0x12a8], 0
0x0007FC41: jne 0x14007fd4a
0x0007FC47: mov ebx, r15d
0x0007FC4A: mov rcx, qword ptr [rdi + 8]
0x0007FC4E: sub rcx, qword ptr [rdi]
0x0007FC51: movabs r12, 0x4bda12f684bda13
0x0007FC5B: mov rax, r12
0x0007FC5E: imul rcx
0x0007FC61: sar rdx, 2
0x0007FC65: mov rax, rdx
0x0007FC68: shr rax, 0x3f
0x0007FC6C: add rdx, rax
0x0007FC6F: je 0x14007fd4a
0x0007FC75: mov edx, ebx
0x0007FC77: mov rcx, rsi
0x0007FC7A: call 0x1400e3f60
0x0007FC7F: cmp dword ptr [rax + 0x10], 0
0x0007FC83: je 0x14007fd22
0x0007FC89: lea rcx, [rsp + 0x870]
0x0007FC91: movups xmm0, xmmword ptr [rax]
0x0007FC94: movups xmmword ptr [rcx], xmm0
0x0007FC97: movups xmm1, xmmword ptr [rax + 0x10]
0x0007FC9B: movups xmmword ptr [rcx + 0x10], xmm1
0x0007FC9F: movups xmm0, xmmword ptr [rax + 0x20]
0x0007FCA3: movups xmmword ptr [rcx + 0x20], xmm0
0x0007FCA7: movups xmm1, xmmword ptr [rax + 0x30]
0x0007FCAB: movups xmmword ptr [rcx + 0x30], xmm1
0x0007FCAF: movups xmm0, xmmword ptr [rax + 0x40]
0x0007FCB3: movups xmmword ptr [rcx + 0x40], xmm0
0x0007FCB7: movups xmm1, xmmword ptr [rax + 0x50]
0x0007FCBB: movups xmmword ptr [rcx + 0x50], xmm1
0x0007FCBF: movups xmm0, xmmword ptr [rax + 0x60]
0x0007FCC3: movups xmmword ptr [rcx + 0x60], xmm0
0x0007FCC7: lea rcx, [rcx + 0x80]
0x0007FCCE: movups xmm1, xmmword ptr [rax + 0x70]
0x0007FCD2: movups xmmword ptr [rcx - 0x10], xmm1
0x0007FCD6: sub rax, -0x80
0x0007FCDA: movups xmm0, xmmword ptr [rax]
0x0007FCDD: movups xmmword ptr [rcx], xmm0
0x0007FCE0: movups xmm1, xmmword ptr [rax + 0x10]
0x0007FCE4: movups xmmword ptr [rcx + 0x10], xmm1
0x0007FCE8: movups xmm0, xmmword ptr [rax + 0x20]
0x0007FCEC: movups xmmword ptr [rcx + 0x20], xmm0
0x0007FCF0: movups xmm1, xmmword ptr [rax + 0x30]
0x0007FCF4: movups xmmword ptr [rcx + 0x30], xmm1
0x0007FCF8: movups xmm0, xmmword ptr [rax + 0x40]
```

### `0x000A9233`

```asm
0x000A91E1: lea rax, [rsi + 0x300]
0x000A91E8: xor r15d, r15d
0x000A91EB: nop dword ptr [rax + rax]
0x000A91F0: lea r14, [r8 + r15]
0x000A91F4: cmp dword ptr [r14], 1
0x000A91F8: jne 0x1400a9200
0x000A91FA: or r13b, 1
0x000A91FE: jmp 0x1400a9204
0x000A9200: or r12b, 1
0x000A9204: mov rdx, r14
0x000A9207: mov rcx, rax
0x000A920A: call 0x1400b0280
0x000A920F: mov rbx, qword ptr [rsi + 0x308]
0x000A9216: call 0x140134560
0x000A921B: add eax, edi
0x000A921D: mov dword ptr [rbx - 8], eax
0x000A9220: test byte ptr [r14 + 0x9c], 1
0x000A9228: je 0x1400a92df
0x000A922E: mov edx, edi
0x000A9230: mov rcx, rsi
0x000A9233: call 0x1400e3f60
0x000A9238: cmp dword ptr [rax + 0x2c], 0
0x000A923C: jge 0x1400a92df
0x000A9242: mov edx, edi
0x000A9244: mov rcx, rsi
0x000A9247: call 0x1400e3f60
0x000A924C: lea rcx, [rbp + 0x70]
0x000A9250: movups xmm0, xmmword ptr [rax]
0x000A9253: movups xmmword ptr [rcx], xmm0
0x000A9256: movups xmm1, xmmword ptr [rax + 0x10]
0x000A925A: movups xmmword ptr [rcx + 0x10], xmm1
0x000A925E: movups xmm0, xmmword ptr [rax + 0x20]
0x000A9262: movups xmmword ptr [rcx + 0x20], xmm0
0x000A9266: movups xmm1, xmmword ptr [rax + 0x30]
0x000A926A: movups xmmword ptr [rcx + 0x30], xmm1
0x000A926E: movups xmm0, xmmword ptr [rax + 0x40]
0x000A9272: movups xmmword ptr [rcx + 0x40], xmm0
0x000A9276: movups xmm1, xmmword ptr [rax + 0x50]
0x000A927A: movups xmmword ptr [rcx + 0x50], xmm1
0x000A927E: movups xmm0, xmmword ptr [rax + 0x60]
0x000A9282: movups xmmword ptr [rcx + 0x60], xmm0
0x000A9286: lea rcx, [rcx + 0x80]
0x000A928D: movups xmm1, xmmword ptr [rax + 0x70]
0x000A9291: movups xmmword ptr [rcx - 0x10], xmm1
0x000A9295: sub rax, -0x80
0x000A9299: movups xmm0, xmmword ptr [rax]
0x000A929C: movups xmmword ptr [rcx], xmm0
0x000A929F: movups xmm1, xmmword ptr [rax + 0x10]
0x000A92A3: movups xmmword ptr [rcx + 0x10], xmm1
0x000A92A7: movups xmm0, xmmword ptr [rax + 0x20]
0x000A92AB: movups xmmword ptr [rcx + 0x20], xmm0
```

### `0x000A9247`

```asm
0x000A91F8: jne 0x1400a9200
0x000A91FA: or r13b, 1
0x000A91FE: jmp 0x1400a9204
0x000A9200: or r12b, 1
0x000A9204: mov rdx, r14
0x000A9207: mov rcx, rax
0x000A920A: call 0x1400b0280
0x000A920F: mov rbx, qword ptr [rsi + 0x308]
0x000A9216: call 0x140134560
0x000A921B: add eax, edi
0x000A921D: mov dword ptr [rbx - 8], eax
0x000A9220: test byte ptr [r14 + 0x9c], 1
0x000A9228: je 0x1400a92df
0x000A922E: mov edx, edi
0x000A9230: mov rcx, rsi
0x000A9233: call 0x1400e3f60
0x000A9238: cmp dword ptr [rax + 0x2c], 0
0x000A923C: jge 0x1400a92df
0x000A9242: mov edx, edi
0x000A9244: mov rcx, rsi
0x000A9247: call 0x1400e3f60
0x000A924C: lea rcx, [rbp + 0x70]
0x000A9250: movups xmm0, xmmword ptr [rax]
0x000A9253: movups xmmword ptr [rcx], xmm0
0x000A9256: movups xmm1, xmmword ptr [rax + 0x10]
0x000A925A: movups xmmword ptr [rcx + 0x10], xmm1
0x000A925E: movups xmm0, xmmword ptr [rax + 0x20]
0x000A9262: movups xmmword ptr [rcx + 0x20], xmm0
0x000A9266: movups xmm1, xmmword ptr [rax + 0x30]
0x000A926A: movups xmmword ptr [rcx + 0x30], xmm1
0x000A926E: movups xmm0, xmmword ptr [rax + 0x40]
0x000A9272: movups xmmword ptr [rcx + 0x40], xmm0
0x000A9276: movups xmm1, xmmword ptr [rax + 0x50]
0x000A927A: movups xmmword ptr [rcx + 0x50], xmm1
0x000A927E: movups xmm0, xmmword ptr [rax + 0x60]
0x000A9282: movups xmmword ptr [rcx + 0x60], xmm0
0x000A9286: lea rcx, [rcx + 0x80]
0x000A928D: movups xmm1, xmmword ptr [rax + 0x70]
0x000A9291: movups xmmword ptr [rcx - 0x10], xmm1
0x000A9295: sub rax, -0x80
0x000A9299: movups xmm0, xmmword ptr [rax]
0x000A929C: movups xmmword ptr [rcx], xmm0
0x000A929F: movups xmm1, xmmword ptr [rax + 0x10]
0x000A92A3: movups xmmword ptr [rcx + 0x10], xmm1
0x000A92A7: movups xmm0, xmmword ptr [rax + 0x20]
0x000A92AB: movups xmmword ptr [rcx + 0x20], xmm0
0x000A92AF: movups xmm1, xmmword ptr [rax + 0x30]
0x000A92B3: movups xmmword ptr [rcx + 0x30], xmm1
0x000A92B7: movups xmm0, xmmword ptr [rax + 0x40]
0x000A92BB: movups xmmword ptr [rcx + 0x40], xmm0
0x000A92BF: mov rax, qword ptr [rax + 0x50]
```

### `0x000B2426`

```asm
0x000B23C9: lea rcx, [rbp + 0x88]
0x000B23D0: call 0x14006a240
0x000B23D5: mov eax, dword ptr [rbx + 0x4ec]
0x000B23DB: mov dword ptr [rdi + 0x78], eax
0x000B23DE: mov rax, qword ptr [rbx + 0x50]
0x000B23E2: cmp qword ptr [rbx + 0x48], rax
0x000B23E6: jne 0x1400b24fa
0x000B23EC: mov edi, r12d
0x000B23EF: mov rcx, qword ptr [rbx + 0x2c8]
0x000B23F6: sub rcx, qword ptr [rbx + 0x2c0]
0x000B23FD: movabs rsi, 0x4bda12f684bda13
0x000B2407: mov rax, rsi
0x000B240A: imul rcx
0x000B240D: sar rdx, 2
0x000B2411: mov rax, rdx
0x000B2414: shr rax, 0x3f
0x000B2418: add rdx, rax
0x000B241B: je 0x1400b24fa
0x000B2421: mov edx, edi
0x000B2423: mov rcx, rbx
0x000B2426: call 0x1400e3f60
0x000B242B: cmp dword ptr [rax + 0x10], 0
0x000B242F: je 0x1400b24cb
0x000B2435: lea rdx, [rbp + 0xd0]
0x000B243C: movups xmm0, xmmword ptr [rax]
0x000B243F: movups xmmword ptr [rdx], xmm0
0x000B2442: movups xmm1, xmmword ptr [rax + 0x10]
0x000B2446: movups xmmword ptr [rdx + 0x10], xmm1
0x000B244A: movups xmm0, xmmword ptr [rax + 0x20]
0x000B244E: movups xmmword ptr [rdx + 0x20], xmm0
0x000B2452: movups xmm1, xmmword ptr [rax + 0x30]
0x000B2456: movups xmmword ptr [rdx + 0x30], xmm1
0x000B245A: movups xmm0, xmmword ptr [rax + 0x40]
0x000B245E: movups xmmword ptr [rdx + 0x40], xmm0
0x000B2462: movups xmm1, xmmword ptr [rax + 0x50]
0x000B2466: movups xmmword ptr [rdx + 0x50], xmm1
0x000B246A: movups xmm0, xmmword ptr [rax + 0x60]
0x000B246E: movups xmmword ptr [rdx + 0x60], xmm0
0x000B2472: lea rdx, [rdx + 0x80]
0x000B2479: movups xmm1, xmmword ptr [rax + 0x70]
0x000B247D: movups xmmword ptr [rdx - 0x10], xmm1
0x000B2481: sub rax, -0x80
0x000B2485: movups xmm0, xmmword ptr [rax]
0x000B2488: movups xmmword ptr [rdx], xmm0
0x000B248B: movups xmm1, xmmword ptr [rax + 0x10]
0x000B248F: movups xmmword ptr [rdx + 0x10], xmm1
0x000B2493: movups xmm0, xmmword ptr [rax + 0x20]
0x000B2497: movups xmmword ptr [rdx + 0x20], xmm0
0x000B249B: movups xmm1, xmmword ptr [rax + 0x30]
0x000B249F: movups xmmword ptr [rdx + 0x30], xmm1
0x000B24A3: movups xmm0, xmmword ptr [rax + 0x40]
```
