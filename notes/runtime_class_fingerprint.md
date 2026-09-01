# Derived snapshot-base handoffs

Seeds: confirmed derived vtable methods; snapshot bases `this+0x368` and `this+0x440`.
snapshot-base hits: 4

## type1

### method `0x001688D0` hit `0x00168C97` snapshotA

```asm
0x00168C5B: test al, al
0x00168C5D: jne 0x140169065
0x00168C63: mov dword ptr [rsp + 0x360], 0x34
0x00168C6E: mov eax, dword ptr [rsp + 0x360]
0x00168C75: add al, 0x34
0x00168C77: movsx ecx, al
0x00168C7A: xor ecx, 0x53
0x00168C7D: mov dword ptr [rsp + 0x364], ecx
0x00168C84: mov eax, dword ptr [rsp + 0x364]
0x00168C8B: mov ecx, dword ptr [rsp + 0x360]
0x00168C92: xor ecx, eax
0x00168C94: xor ecx, 0x55
0x00168C97: mov byte ptr [rsp + 0x368], cl
0x00168C9E: movsx ecx, byte ptr [rsp + 0x368]
0x00168CA6: mov eax, dword ptr [rsp + 0x360]
0x00168CAD: inc al
0x00168CAF: xor eax, ecx
0x00168CB1: xor eax, 0x6e
0x00168CB4: mov byte ptr [rsp + 0x369], al
0x00168CBB: movsx ecx, byte ptr [rsp + 0x369]
0x00168CC3: mov eax, dword ptr [rsp + 0x360]
0x00168CCA: add al, 2
0x00168CCC: xor eax, ecx
0x00168CCE: xor eax, 0x61
0x00168CD1: mov byte ptr [rsp + 0x36a], al
0x00168CD8: movsx ecx, byte ptr [rsp + 0x36a]
0x00168CE0: mov eax, dword ptr [rsp + 0x360]
0x00168CE7: add al, 3
0x00168CE9: xor eax, ecx
0x00168CEB: xor eax, 0x62
0x00168CEE: mov byte ptr [rsp + 0x36b], al
0x00168CF5: movsx ecx, byte ptr [rsp + 0x36b]
```

Next direct callees:

- call `0x00168FEB` -> `0x00093190`
- call `0x0016903C` -> `0x003D23C8`
- call `0x0016905F` -> `0x003D25D0`
- call `0x00169067` -> `0x00058850`

### method `0x001688D0` hit `0x00168C9E` snapshotA

```asm
0x00168C5D: jne 0x140169065
0x00168C63: mov dword ptr [rsp + 0x360], 0x34
0x00168C6E: mov eax, dword ptr [rsp + 0x360]
0x00168C75: add al, 0x34
0x00168C77: movsx ecx, al
0x00168C7A: xor ecx, 0x53
0x00168C7D: mov dword ptr [rsp + 0x364], ecx
0x00168C84: mov eax, dword ptr [rsp + 0x364]
0x00168C8B: mov ecx, dword ptr [rsp + 0x360]
0x00168C92: xor ecx, eax
0x00168C94: xor ecx, 0x55
0x00168C97: mov byte ptr [rsp + 0x368], cl
0x00168C9E: movsx ecx, byte ptr [rsp + 0x368]
0x00168CA6: mov eax, dword ptr [rsp + 0x360]
0x00168CAD: inc al
0x00168CAF: xor eax, ecx
0x00168CB1: xor eax, 0x6e
0x00168CB4: mov byte ptr [rsp + 0x369], al
0x00168CBB: movsx ecx, byte ptr [rsp + 0x369]
0x00168CC3: mov eax, dword ptr [rsp + 0x360]
0x00168CCA: add al, 2
0x00168CCC: xor eax, ecx
0x00168CCE: xor eax, 0x61
0x00168CD1: mov byte ptr [rsp + 0x36a], al
0x00168CD8: movsx ecx, byte ptr [rsp + 0x36a]
0x00168CE0: mov eax, dword ptr [rsp + 0x360]
0x00168CE7: add al, 3
0x00168CE9: xor eax, ecx
0x00168CEB: xor eax, 0x62
0x00168CEE: mov byte ptr [rsp + 0x36b], al
0x00168CF5: movsx ecx, byte ptr [rsp + 0x36b]
0x00168CFD: mov eax, dword ptr [rsp + 0x360]
```

Next direct callees:

- call `0x00168FEB` -> `0x00093190`
- call `0x0016903C` -> `0x003D23C8`
- call `0x0016905F` -> `0x003D25D0`
- call `0x00169067` -> `0x00058850`

### method `0x001688D0` hit `0x00168FD3` snapshotA

```asm
0x00168F9F: add al, 0x1b
0x00168FA1: xor eax, ecx
0x00168FA3: xor eax, 0x65
0x00168FA6: mov byte ptr [rsp + 0x383], al
0x00168FAD: movsx ecx, byte ptr [rsp + 0x383]
0x00168FB5: mov eax, dword ptr [rsp + 0x360]
0x00168FBC: add al, 0x1c
0x00168FBE: xor eax, ecx
0x00168FC0: xor eax, 0x72
0x00168FC3: mov byte ptr [rsp + 0x384], al
0x00168FCA: xor eax, eax
0x00168FCC: mov byte ptr [rsp + 0x385], al
0x00168FD3: movzx eax, byte ptr [rsp + 0x368]
0x00168FDB: lea rdx, [rsp + 0x3f8]
0x00168FE3: lea rcx, [rsp + 0x360]
0x00168FEB: call 0x140093190
0x00168FF0: nop
0x00168FF1: cmp qword ptr [rax + 0x18], 0x10
0x00168FF6: jb 0x140168ffb
0x00168FF8: mov rax, qword ptr [rax]
0x00168FFB: lea rcx, [rip + 0x2ca96e]
0x00169002: mov qword ptr [rsp + 0xc0], rcx
0x0016900A: xor ecx, ecx
0x0016900C: mov qword ptr [rsp + 0xc8], rcx
0x00169014: mov qword ptr [rsp + 0xd0], rcx
0x0016901C: mov qword ptr [rsp + 0x130], rax
0x00169024: mov byte ptr [rsp + 0x138], 1
0x0016902C: lea rdx, [rsp + 0xc8]
0x00169034: lea rcx, [rsp + 0x130]
0x0016903C: call 0x1403d23c8
0x00169041: lea rax, [rip + 0x2ca940]
0x00169048: mov qword ptr [rsp + 0xc0], rax
```

Next direct callees:

- call `0x00168FEB` -> `0x00093190`
- call `0x0016903C` -> `0x003D23C8`
- call `0x0016905F` -> `0x003D25D0`
- call `0x00169067` -> `0x00058850`

### method `0x001688D0` hit `0x001694A3` snapshotB

```asm
0x00169478: call 0x14039219c
0x0016947D: nop
0x0016947E: lea rcx, [rbx + 0x50]
0x00169482: call 0x140391e8c
0x00169487: test eax, eax
0x00169489: je 0x140169493
0x0016948B: mov ecx, eax
0x0016948D: call 0x14039219c
0x00169492: nop
0x00169493: mov rcx, qword ptr [rsp + 0x438]
0x0016949B: xor rcx, rsp
0x0016949E: call 0x1403b24c0
0x001694A3: lea r11, [rsp + 0x440]
0x001694AB: mov rbx, qword ptr [r11 + 0x38]
0x001694AF: mov rsi, qword ptr [r11 + 0x48]
0x001694B3: mov rsp, r11
0x001694B6: pop r15
0x001694B8: pop r14
0x001694BA: pop r13
0x001694BC: pop r12
0x001694BE: pop rdi
0x001694BF: ret
```

Next direct callees:


## type2
