# PM62C_MAIN argument-flow candidates

Windows x64 entry candidates: RCX/RDX/R8/R9. These are not assigned semantics until verified.

## First 160 instructions

```asm
0x00129A50: mov rax, rsp
0x00129A53: mov dword ptr [rax + 8], ecx
0x00129A56: push rdi
0x00129A57: push r12
0x00129A59: push r13
0x00129A5B: push r14
0x00129A5D: push r15
0x00129A5F: sub rsp, 0xeb0
0x00129A66: mov qword ptr [rax - 0xd60], 0xfffffffffffffffe
0x00129A71: mov qword ptr [rax + 0x18], rbx
0x00129A75: mov qword ptr [rax + 0x20], rsi
0x00129A79: mov rax, qword ptr [rip + 0x6ace70]
0x00129A80: xor rax, rsp
0x00129A83: mov qword ptr [rsp + 0xea0], rax
0x00129A8B: mov r13, rdx
0x00129A8E: movsxd r15, ecx
0x00129A91: mov qword ptr [rsp + 0xb0], rdx
0x00129A99: xor r14d, r14d
0x00129A9C: mov dword ptr [rsp + 0x50], r14d
0x00129AA1: lea ecx, [r14 + 3]
0x00129AA5: call qword ptr [rip + 0x30680d]
0x00129AAB: mov qword ptr [rsp + 0x58], r15
0x00129AB0: mov eax, 1
0x00129AB5: mov qword ptr [rsp + 0x80], rax
0x00129ABD: cmp rax, r15
0x00129AC0: jge 0x140129dd8
0x00129AC6: mov rdx, qword ptr [r13 + rax*8]
0x00129ACB: mov qword ptr [rsp + 0x4f8], 0xf
0x00129AD7: mov qword ptr [rsp + 0x4f0], r14
0x00129ADF: mov byte ptr [rsp + 0x4e0], 0
0x00129AE7: cmp byte ptr [rdx], 0
0x00129AEA: jne 0x140129af1
0x00129AEC: mov r8, r14
0x00129AEF: jmp 0x140129aff
0x00129AF1: or r8, 0xffffffffffffffff
0x00129AF5: inc r8
0x00129AF8: cmp byte ptr [rdx + r8], 0
0x00129AFD: jne 0x140129af5
0x00129AFF: lea rcx, [rsp + 0x4e0]
0x00129B07: call 0x1400355e0
0x00129B0C: nop
0x00129B0D: mov dword ptr [rsp + 0x3e0], 0x58
0x00129B18: mov eax, dword ptr [rsp + 0x3e0]
0x00129B1F: add al, 0x58
0x00129B21: movsx ecx, al
0x00129B24: xor ecx, 0x4c
0x00129B27: mov dword ptr [rsp + 0x3e4], ecx
0x00129B2E: mov eax, dword ptr [rsp + 0x3e4]
0x00129B35: mov ecx, dword ptr [rsp + 0x3e0]
0x00129B3C: xor ecx, eax
0x00129B3E: xor ecx, 0x2d
0x00129B41: mov byte ptr [rsp + 0x3e8], cl
0x00129B48: movsx ecx, byte ptr [rsp + 0x3e8]
0x00129B50: mov eax, dword ptr [rsp + 0x3e0]
0x00129B57: inc al
0x00129B59: xor eax, ecx
0x00129B5B: xor eax, 0x76
0x00129B5E: mov byte ptr [rsp + 0x3e9], al
0x00129B65: movsx ecx, byte ptr [rsp + 0x3e9]
0x00129B6D: mov eax, dword ptr [rsp + 0x3e0]
0x00129B74: add al, 2
0x00129B76: xor eax, ecx
0x00129B78: xor eax, 0x73
0x00129B7B: mov byte ptr [rsp + 0x3ea], al
0x00129B82: xor eax, eax
0x00129B84: mov byte ptr [rsp + 0x3eb], al
0x00129B8B: movzx eax, byte ptr [rsp + 0x3e8]
0x00129B93: lea rdx, [rsp + 0x5a0]
0x00129B9B: lea rcx, [rsp + 0x3e0]
0x00129BA3: call 0x140220eb0
0x00129BA8: lea r15, [rax + 0x10]
0x00129BAC: cmp qword ptr [rax + 0x18], 0x10
0x00129BB1: jb 0x140129bb6
0x00129BB3: mov rax, qword ptr [rax]
0x00129BB6: lea rcx, [rsp + 0x4e0]
0x00129BBE: mov rbx, qword ptr [rsp + 0x4e0]
0x00129BC6: mov rsi, qword ptr [rsp + 0x4f8]
0x00129BCE: cmp rsi, 0x10
0x00129BD2: cmovae rcx, rbx
0x00129BD6: mov r15, qword ptr [r15]
0x00129BD9: mov r8, r15
0x00129BDC: mov r12, qword ptr [rsp + 0x4f0]
0x00129BE4: cmp r12, r15
0x00129BE7: cmovb r8, r12
0x00129BEB: test r8, r8
0x00129BEE: je 0x140129bfe
0x00129BF0: mov rdx, rax
0x00129BF3: call 0x1403d2f70
0x00129BF8: mov edi, eax
0x00129BFA: test eax, eax
0x00129BFC: jne 0x140129c12
0x00129BFE: cmp r12, r15
0x00129C01: jae 0x140129c08
0x00129C03: or edi, 0xffffffff
0x00129C06: jmp 0x140129c12
0x00129C08: mov edi, r14d
0x00129C0B: cmp r12, r15
0x00129C0E: seta dil
0x00129C12: mov rax, qword ptr [rsp + 0x5b8]
0x00129C1A: cmp rax, 0x10
0x00129C1E: jb 0x140129c78
0x00129C20: inc rax
0x00129C23: mov rcx, qword ptr [rsp + 0x5a0]
0x00129C2B: cmp rax, 0x1000
0x00129C31: jb 0x140129c63
0x00129C33: test cl, 0x1f
0x00129C36: jne 0x140129d2c
0x00129C3C: mov rax, qword ptr [rcx - 8]
0x00129C40: cmp rax, rcx
0x00129C43: jae 0x140129d26
0x00129C49: sub rcx, rax
0x00129C4C: cmp rcx, 8
0x00129C50: jb 0x140129d20
0x00129C56: cmp rcx, 0x27
0x00129C5A: ja 0x140129d1a
0x00129C60: mov rcx, rax
0x00129C63: call 0x1403b20d4
0x00129C68: mov rsi, qword ptr [rsp + 0x4f8]
0x00129C70: mov rbx, qword ptr [rsp + 0x4e0]
0x00129C78: mov qword ptr [rsp + 0x5b8], 0xf
0x00129C84: mov qword ptr [rsp + 0x5b0], r14
0x00129C8C: mov byte ptr [rsp + 0x5a0], 0
0x00129C94: test edi, edi
0x00129C96: je 0x140129d57
0x00129C9C: cmp rsi, 0x10
0x00129CA0: jb 0x140129cdf
0x00129CA2: lea rax, [rsi + 1]
0x00129CA6: cmp rax, 0x1000
0x00129CAC: jb 0x140129cd7
0x00129CAE: test byte ptr [rsp + 0x4e0], 0x1f
0x00129CB6: jne 0x140129d44
0x00129CBC: mov rax, qword ptr [rbx - 8]
0x00129CC0: cmp rax, rbx
0x00129CC3: jae 0x140129d3e
0x00129CC5: sub rbx, rax
0x00129CC8: cmp rbx, 8
0x00129CCC: jb 0x140129d38
0x00129CCE: cmp rbx, 0x27
0x00129CD2: ja 0x140129d32
0x00129CD4: mov rbx, rax
0x00129CD7: mov rcx, rbx
0x00129CDA: call 0x1403b20d4
0x00129CDF: mov qword ptr [rsp + 0x4f8], 0xf
0x00129CEB: mov qword ptr [rsp + 0x4f0], r14
0x00129CF3: mov byte ptr [rsp + 0x4e0], 0
0x00129CFB: mov rax, qword ptr [rsp + 0x80]
0x00129D03: inc rax
0x00129D06: mov qword ptr [rsp + 0x80], rax
0x00129D0E: cmp rax, qword ptr [rsp + 0x58]
0x00129D13: jge 0x140129d4a
0x00129D15: jmp 0x140129ac6
0x00129D1A: call 0x1403db020
0x00129D1F: int3
0x00129D20: call 0x1403db020
0x00129D25: int3
0x00129D26: call 0x1403db020
0x00129D2B: int3
0x00129D2C: call 0x1403db020
0x00129D31: nop
0x00129D32: call 0x1403db020
```

## Calls by kind

- direct: 197
- memory_indirect: 5
- rip_indirect: 1

## Manual review targets

1. Identify where RCX/RDX/R8 are copied into nonvolatile registers or stack locals.
2. Find loops with scale-8 array reads from the register derived from argv.
3. Inspect the first calls fed with an argv[i] pointer.
4. Classify conversion helpers (strtol/atoi/custom numeric parse) and token discriminators.
5. Do not promote a handler to VMR relevance without an option-dependent value flow.