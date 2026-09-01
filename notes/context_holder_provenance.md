# Context holder provenance

Factory functions pass `RDX = [r15]` into derived ctor -> base `this+0x90`.

## factory `0x00058210` PDATA `0x00058210..0x000582CA`

### Full body
```asm
0x00058210: mov qword ptr [rsp + 8], rcx
0x00058215: push rdi
0x00058216: push r14
0x00058218: push r15
0x0005821A: sub rsp, 0x40
0x0005821E: mov qword ptr [rsp + 0x28], 0xfffffffffffffffe
0x00058227: mov qword ptr [rsp + 0x68], rbx
0x0005822C: mov qword ptr [rsp + 0x70], rsi
0x00058231: mov rsi, r9
0x00058234: mov r14, r8
0x00058237: mov r15, rdx
0x0005823A: mov rdi, rcx
0x0005823D: mov dword ptr [rsp + 0x20], 0
0x00058245: mov ecx, 0x8d0
0x0005824A: call 0x1403b2098
0x0005824F: mov rbx, rax
0x00058252: mov qword ptr [rsp + 0x60], rax
0x00058257: test rax, rax
0x0005825A: je 0x140058293
0x0005825C: mov dword ptr [rax + 8], 1
0x00058263: mov dword ptr [rax + 0xc], 1
0x0005826A: lea rax, [rip + 0x3ddcaf]
0x00058271: mov qword ptr [rbx], rax
0x00058274: lea rcx, [rbx + 0x10]
0x00058278: mov qword ptr [rsp + 0x30], rcx
0x0005827D: test rcx, rcx
0x00058280: je 0x140058291
0x00058282: mov r9, rsi
0x00058285: mov r8d, dword ptr [r14]
0x00058288: mov rdx, qword ptr [r15]
0x0005828B: call 0x140161030
0x00058290: nop
0x00058291: jmp 0x140058295
0x00058293: xor ebx, ebx
0x00058295: mov qword ptr [rdi], 0
0x0005829C: mov qword ptr [rdi + 8], 0
0x000582A4: lea rdx, [rbx + 0x10]
0x000582A8: mov r8, rbx
0x000582AB: mov rcx, rdi
0x000582AE: call 0x140058410
0x000582B3: mov rax, rdi
0x000582B6: mov rbx, qword ptr [rsp + 0x68]
0x000582BB: mov rsi, qword ptr [rsp + 0x70]
0x000582C0: add rsp, 0x40
0x000582C4: pop r15
0x000582C6: pop r14
0x000582C8: pop rdi
0x000582C9: ret
```

### Direct callers

#### call `0x00058531` in `0x000584A0..0x00058581`

```asm
0x000584C1: xor eax, eax
0x000584C3: mov dword ptr [rsp + 0x20], eax
0x000584C7: mov qword ptr [rcx], rax
0x000584CA: mov qword ptr [rcx + 8], rax
0x000584CE: mov dword ptr [rsp + 0x20], 1
0x000584D6: mov r8d, dword ptr [rdx]
0x000584D9: sub r8d, 1
0x000584DD: je 0x140058514
0x000584DF: cmp r8d, 1
0x000584E3: jne 0x140058575
0x000584E9: mov r9, qword ptr [rsp + 0x90]
0x000584F1: lea r8, [r11 + 0x20]
0x000584F5: lea rdx, [r11 + 0x18]
0x000584F9: lea rcx, [r11 - 0x38]
0x000584FD: call 0x1400582d0
0x00058502: mov rdx, rax
0x00058505: mov rcx, rsi
0x00058508: call 0x140145010
0x0005850D: mov rdi, qword ptr [rsp + 0x38]
0x00058512: jmp 0x140058546
0x00058514: mov r9, qword ptr [rsp + 0x90]
0x0005851C: lea r8, [rsp + 0x88]
0x00058524: lea rdx, [rsp + 0x80]
0x0005852C: lea rcx, [rsp + 0x40]
0x00058531: call 0x140058210
0x00058536: mov rdx, rax
0x00058539: mov rcx, rsi
0x0005853C: call 0x140145010
0x00058541: mov rdi, qword ptr [rsp + 0x48]
0x00058546: test rdi, rdi
0x00058549: je 0x140058575
0x0005854B: or ebx, 0xffffffff
0x0005854E: mov eax, ebx
0x00058550: lock xadd dword ptr [rdi + 8], eax
0x00058555: cmp eax, 1
0x00058558: jne 0x140058575
0x0005855A: mov rax, qword ptr [rdi]
0x0005855D: mov rcx, rdi
0x00058560: call qword ptr [rax]
0x00058562: lock xadd dword ptr [rdi + 0xc], ebx
0x00058567: cmp ebx, 1
0x0005856A: jne 0x140058575
0x0005856C: mov rax, qword ptr [rdi]
0x0005856F: mov rcx, rdi
0x00058572: call qword ptr [rax + 8]
0x00058575: mov rax, rsi
0x00058578: add rsp, 0x50
0x0005857C: pop rdi
```

## factory `0x000582D0` PDATA `0x000582D0..0x0005838A`

### Full body
```asm
0x000582D0: mov qword ptr [rsp + 8], rcx
0x000582D5: push rdi
0x000582D6: push r14
0x000582D8: push r15
0x000582DA: sub rsp, 0x40
0x000582DE: mov qword ptr [rsp + 0x28], 0xfffffffffffffffe
0x000582E7: mov qword ptr [rsp + 0x68], rbx
0x000582EC: mov qword ptr [rsp + 0x70], rsi
0x000582F1: mov rsi, r9
0x000582F4: mov r14, r8
0x000582F7: mov r15, rdx
0x000582FA: mov rdi, rcx
0x000582FD: mov dword ptr [rsp + 0x20], 0
0x00058305: mov ecx, 0x858
0x0005830A: call 0x1403b2098
0x0005830F: mov rbx, rax
0x00058312: mov qword ptr [rsp + 0x60], rax
0x00058317: test rax, rax
0x0005831A: je 0x140058353
0x0005831C: mov dword ptr [rax + 8], 1
0x00058323: mov dword ptr [rax + 0xc], 1
0x0005832A: lea rax, [rip + 0x3ddc17]
0x00058331: mov qword ptr [rbx], rax
0x00058334: lea rcx, [rbx + 0x10]
0x00058338: mov qword ptr [rsp + 0x30], rcx
0x0005833D: test rcx, rcx
0x00058340: je 0x140058351
0x00058342: mov r9, rsi
0x00058345: mov r8d, dword ptr [r14]
0x00058348: mov rdx, qword ptr [r15]
0x0005834B: call 0x1401cdcc0
0x00058350: nop
0x00058351: jmp 0x140058355
0x00058353: xor ebx, ebx
0x00058355: mov qword ptr [rdi], 0
0x0005835C: mov qword ptr [rdi + 8], 0
0x00058364: lea rdx, [rbx + 0x10]
0x00058368: mov r8, rbx
0x0005836B: mov rcx, rdi
0x0005836E: call 0x140058410
0x00058373: mov rax, rdi
0x00058376: mov rbx, qword ptr [rsp + 0x68]
0x0005837B: mov rsi, qword ptr [rsp + 0x70]
0x00058380: add rsp, 0x40
0x00058384: pop r15
0x00058386: pop r14
0x00058388: pop rdi
0x00058389: ret
```

### Direct callers

#### call `0x000584FD` in `0x000584A0..0x00058581`

```asm
0x000584A0: mov r11, rsp
0x000584A3: mov dword ptr [r11 + 0x20], r9d
0x000584A7: mov qword ptr [r11 + 0x18], r8
0x000584AB: mov qword ptr [r11 + 8], rcx
0x000584AF: push rbx
0x000584B0: push rsi
0x000584B1: push rdi
0x000584B2: sub rsp, 0x50
0x000584B6: mov qword ptr [r11 - 0x40], 0xfffffffffffffffe
0x000584BE: mov rsi, rcx
0x000584C1: xor eax, eax
0x000584C3: mov dword ptr [rsp + 0x20], eax
0x000584C7: mov qword ptr [rcx], rax
0x000584CA: mov qword ptr [rcx + 8], rax
0x000584CE: mov dword ptr [rsp + 0x20], 1
0x000584D6: mov r8d, dword ptr [rdx]
0x000584D9: sub r8d, 1
0x000584DD: je 0x140058514
0x000584DF: cmp r8d, 1
0x000584E3: jne 0x140058575
0x000584E9: mov r9, qword ptr [rsp + 0x90]
0x000584F1: lea r8, [r11 + 0x20]
0x000584F5: lea rdx, [r11 + 0x18]
0x000584F9: lea rcx, [r11 - 0x38]
0x000584FD: call 0x1400582d0
0x00058502: mov rdx, rax
0x00058505: mov rcx, rsi
0x00058508: call 0x140145010
0x0005850D: mov rdi, qword ptr [rsp + 0x38]
0x00058512: jmp 0x140058546
0x00058514: mov r9, qword ptr [rsp + 0x90]
0x0005851C: lea r8, [rsp + 0x88]
0x00058524: lea rdx, [rsp + 0x80]
0x0005852C: lea rcx, [rsp + 0x40]
0x00058531: call 0x140058210
0x00058536: mov rdx, rax
0x00058539: mov rcx, rsi
0x0005853C: call 0x140145010
0x00058541: mov rdi, qword ptr [rsp + 0x48]
0x00058546: test rdi, rdi
0x00058549: je 0x140058575
0x0005854B: or ebx, 0xffffffff
0x0005854E: mov eax, ebx
0x00058550: lock xadd dword ptr [rdi + 8], eax
0x00058555: cmp eax, 1
0x00058558: jne 0x140058575
0x0005855A: mov rax, qword ptr [rdi]
0x0005855D: mov rcx, rdi
```
