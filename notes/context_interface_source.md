# Context interface / factory dispatch provenance

data refs: 0  code refs: 2

## Data qwords

| RVA | section | target | label |
|---|---|---|---|

## Code refs

| RVA | ref/target | instruction |
|---|---|---|
| `0x000584FD` | `0x000582D0` | `call 0x1400582d0` |
| `0x00058531` | `0x00058210` | `call 0x140058210` |

## Contexts

### `0x000584FD` -> `0x000582D0`

```asm
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
```

### `0x00058531` -> `0x00058210`

```asm
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
```
