# Transform callable invocation

## `0x00139F00` PDATA `0x00139F00..0x00139F4D`

```asm
0x00139F00: mov qword ptr [rsp + 0x20], r9
0x00139F05: push rbx
0x00139F06: sub rsp, 0x40
0x00139F0A: mov rcx, qword ptr [rcx + 0x38]
0x00139F0E: mov rbx, rdx
0x00139F11: mov dword ptr [rsp + 0x30], 0
0x00139F19: test rcx, rcx
0x00139F1C: je 0x140139f47
0x00139F1E: mov rax, qword ptr [rsp + 0x78]
0x00139F23: lea r9, [rsp + 0x68]
0x00139F28: mov r10, qword ptr [rcx]
0x00139F2B: mov qword ptr [rsp + 0x28], rax
0x00139F30: lea rax, [rsp + 0x70]
0x00139F35: mov qword ptr [rsp + 0x20], rax
0x00139F3A: call qword ptr [r10 + 0x10]
0x00139F3E: mov rax, rbx
0x00139F41: add rsp, 0x40
0x00139F45: pop rbx
0x00139F46: ret
0x00139F47: call 0x140390a54
0x00139F4C: int3
```

## `0x00139D60` PDATA `0x00139D60..0x00139EFE`

```asm
0x00139D60: mov qword ptr [rsp + 8], rcx
0x00139D65: push rdi
0x00139D66: push r14
0x00139D68: push r15
0x00139D6A: sub rsp, 0x30
0x00139D6E: mov qword ptr [rsp + 0x20], 0xfffffffffffffffe
0x00139D77: mov qword ptr [rsp + 0x58], rbx
0x00139D7C: mov qword ptr [rsp + 0x60], rsi
0x00139D81: mov r15, rdx
0x00139D84: mov r14, rcx
0x00139D87: cmp rcx, rdx
0x00139D8A: je 0x140139ee7
0x00139D90: mov r9, qword ptr [rdx]
0x00139D93: mov r8, qword ptr [rdx + 8]
0x00139D97: cmp r9, r8
0x00139D9A: jne 0x140139da8
0x00139D9C: mov rax, qword ptr [rcx]
0x00139D9F: mov qword ptr [rcx + 8], rax
0x00139DA3: jmp 0x140139ee7
0x00139DA8: mov rcx, r8
0x00139DAB: sub rcx, r9
0x00139DAE: movabs rdi, 0x4bda12f684bda13
0x00139DB8: mov rax, rdi
0x00139DBB: imul rcx
0x00139DBE: mov r11, rdx
0x00139DC1: sar r11, 2
0x00139DC5: mov rax, r11
0x00139DC8: shr rax, 0x3f
0x00139DCC: add r11, rax
0x00139DCF: mov r10, qword ptr [r14]
0x00139DD2: mov rcx, qword ptr [r14 + 8]
0x00139DD6: sub rcx, r10
0x00139DD9: mov rax, rdi
0x00139DDC: imul rcx
0x00139DDF: mov rbx, rdx
0x00139DE2: sar rbx, 2
0x00139DE6: mov rax, rbx
0x00139DE9: shr rax, 0x3f
0x00139DED: add rbx, rax
0x00139DF0: cmp r11, rbx
0x00139DF3: ja 0x140139e2d
0x00139DF5: sub r8, r9
0x00139DF8: mov rdx, r9
0x00139DFB: mov rcx, r10
0x00139DFE: call 0x1403d1f90
0x00139E03: mov rcx, qword ptr [r15 + 8]
0x00139E07: sub rcx, qword ptr [r15]
0x00139E0A: mov rax, rdi
0x00139E0D: imul rcx
0x00139E10: sar rdx, 2
0x00139E14: mov rax, rdx
0x00139E17: shr rax, 0x3f
0x00139E1B: add rdx, rax
0x00139E1E: imul rax, rdx, 0xd8
0x00139E25: add rax, qword ptr [r14]
0x00139E28: jmp 0x140139ee3
0x00139E2D: mov rcx, qword ptr [r14 + 0x10]
0x00139E31: sub rcx, r10
0x00139E34: mov rax, rdi
0x00139E37: imul rcx
0x00139E3A: sar rdx, 2
0x00139E3E: mov rax, rdx
0x00139E41: shr rax, 0x3f
0x00139E45: add rdx, rax
0x00139E48: cmp r11, rdx
0x00139E4B: ja 0x140139e87
0x00139E4D: imul rsi, rbx, 0xd8
0x00139E54: add rsi, r9
0x00139E57: mov r8, rsi
0x00139E5A: sub r8, r9
0x00139E5D: mov rdx, r9
0x00139E60: mov rcx, r10
0x00139E63: call 0x1403d1f90
0x00139E68: mov rdi, qword ptr [r14 + 8]
0x00139E6C: mov rbx, qword ptr [r15 + 8]
0x00139E70: sub rbx, rsi
0x00139E73: mov r8, rbx
0x00139E76: mov rdx, rsi
0x00139E79: mov rcx, rdi
0x00139E7C: call 0x1403d1f90
0x00139E81: lea rax, [rbx + rdi]
0x00139E85: jmp 0x140139ee3
0x00139E87: test r10, r10
0x00139E8A: je 0x140139e9a
0x00139E8C: mov r8, rdx
0x00139E8F: mov rdx, r10
0x00139E92: mov rcx, r14
0x00139E95: call 0x14006f380
0x00139E9A: mov rcx, qword ptr [r15 + 8]
0x00139E9E: sub rcx, qword ptr [r15]
0x00139EA1: mov rax, rdi
0x00139EA4: imul rcx
0x00139EA7: sar rdx, 2
0x00139EAB: mov rax, rdx
0x00139EAE: shr rax, 0x3f
0x00139EB2: add rdx, rax
0x00139EB5: mov rcx, r14
0x00139EB8: call 0x140139f90
0x00139EBD: test al, al
0x00139EBF: je 0x140139ee7
0x00139EC1: mov rdi, qword ptr [r14]
0x00139EC4: mov rbx, qword ptr [r15 + 8]
0x00139EC8: mov rdx, qword ptr [r15]
0x00139ECB: sub rbx, rdx
0x00139ECE: mov r8, rbx
0x00139ED1: mov rcx, rdi
0x00139ED4: call 0x1403d1f90
0x00139ED9: lea rax, [rbx + rdi]
0x00139EDD: mov qword ptr [r14 + 8], rax
0x00139EE1: jmp 0x140139ee7
0x00139EE3: mov qword ptr [r14 + 8], rax
0x00139EE7: mov rax, r14
0x00139EEA: mov rbx, qword ptr [rsp + 0x58]
0x00139EEF: mov rsi, qword ptr [rsp + 0x60]
0x00139EF4: add rsp, 0x30
0x00139EF8: pop r15
0x00139EFA: pop r14
0x00139EFC: pop rdi
0x00139EFD: ret
```
