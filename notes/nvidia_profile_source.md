# NVIDIA profile source helper around 0x1D78B0

## Disassembly

```asm
0x001D77B0: sal byte ptr [rbp + 0x16], 0x8b
0x001D77B4: and al, 0x60
0x001D77B7: test ecx, ecx
0x001D77B9: je 0x1401d77c9
0x001D77BB: mov eax, 0x10624dd3
0x001D77C0: mul ecx
0x001D77C2: shr edx, 6
0x001D77C5: mov word ptr [rbx + 0xe], dx
0x001D77C9: mov rax, qword ptr [rip + 0x6102c0]
0x001D77D0: test rax, rax
0x001D77D3: je 0x1401d77f6
0x001D77D5: mov rcx, qword ptr [rdi + 0xd0]
0x001D77DC: lea rdx, [rsp + 0x30]
0x001D77E1: mov dword ptr [rsp + 0x30], r12d
0x001D77E6: call rax
0x001D77E8: test eax, eax
0x001D77EA: jne 0x1401d77f6
0x001D77EC: movzx eax, byte ptr [rsp + 0x30]
0x001D77F1: add al, 0x64
0x001D77F3: mov byte ptr [rbx + 0x1c], al
0x001D77F6: mov r8d, 7
0x001D77FC: lea rdx, [rsp + 0x38]
0x001D7801: mov rcx, rdi
0x001D7804: call 0x14014b790
0x001D7809: mov rsi, qword ptr [rsp + 0x9b0]
0x001D7811: mov rcx, qword ptr [rax]
0x001D7814: mov qword ptr [rbx], rcx
0x001D7817: mov rcx, qword ptr [rdi + 0xc8]
0x001D781E: test rcx, rcx
0x001D7821: je 0x1401d7888
0x001D7823: mov rax, qword ptr [rip + 0x610066]
0x001D782A: test rax, rax
0x001D782D: je 0x1401d7888
0x001D782F: lea rdx, [rsp + 0x38]
0x001D7834: mov qword ptr [rsp + 0x38], r15
0x001D7839: call rax
0x001D783B: test eax, eax
0x001D783D: jne 0x1401d7888
0x001D783F: mov rax, qword ptr [rsp + 0x38]
0x001D7844: test al, 0x84
0x001D7846: je 0x1401d7851
0x001D7848: mov dword ptr [rbx + 0x18], 3
0x001D784F: jmp 0x1401d7888
0x001D7851: test al, 0x60
0x001D7853: je 0x1401d785e
0x001D7855: mov dword ptr [rbx + 0x18], 4
0x001D785C: jmp 0x1401d7888
0x001D785E: test rax, 0x102
0x001D7864: je 0x1401d786f
0x001D7866: mov dword ptr [rbx + 0x18], 5
0x001D786D: jmp 0x1401d7888
0x001D786F: test rax, rax
0x001D7872: je 0x1401d7881
0x001D7874: test al, 1
0x001D7876: jne 0x1401d7881
0x001D7878: mov dword ptr [rbx + 0x18], 2
0x001D787F: jmp 0x1401d7888
0x001D7881: mov dword ptr [rbx + 0x18], 1
0x001D7888: mov r12, qword ptr [rsp + 0x9b8]
0x001D7890: mov rax, rbx
0x001D7893: mov rcx, qword ptr [rbp + 0x860]
0x001D789A: xor rcx, rsp
0x001D789D: call 0x1403b24c0
0x001D78A2: add rsp, 0x978
0x001D78A9: pop r15
0x001D78AB: pop rdi
0x001D78AC: pop rbx
0x001D78AD: pop rbp
0x001D78AE: ret
0x001D78AF: int3
0x001D78B0: mov qword ptr [rsp + 8], rbx
0x001D78B5: push rdi
0x001D78B6: sub rsp, 0x20
0x001D78BA: mov eax, dword ptr [rcx + 0x3a0]
0x001D78C0: lea rbx, [rip + 0x2e5e09]
0x001D78C7: lea rcx, [rip + 0x2e5f82]
0x001D78CE: mov rdi, rdx
0x001D78D1: cmp dword ptr [rbx], eax
0x001D78D3: jne 0x1401d78db
0x001D78D5: cmp dword ptr [rbx + 4], r8d
0x001D78D9: je 0x1401d78f1
0x001D78DB: add rbx, 0x18
0x001D78DF: cmp rbx, rcx
0x001D78E2: jne 0x1401d78d1
0x001D78E4: xor al, al
0x001D78E6: mov rbx, qword ptr [rsp + 0x30]
0x001D78EB: add rsp, 0x20
0x001D78EF: pop rdi
0x001D78F0: ret
0x001D78F1: xor edx, edx
0x001D78F3: mov rcx, rdi
0x001D78F6: lea r8d, [rdx + 0x5c]
0x001D78FA: call 0x1403d3050
0x001D78FF: mov eax, dword ptr [rbx + 0x10]
0x001D7902: mov dword ptr [rdi + 0x2c], eax
0x001D7905: mov eax, dword ptr [rbx + 0xc]
0x001D7908: mov dword ptr [rdi + 0x38], eax
0x001D790B: mov eax, dword ptr [rbx + 8]
0x001D790E: mov dword ptr [rdi + 0x44], eax
0x001D7911: mov eax, dword ptr [rbx + 0x14]
0x001D7914: mov rbx, qword ptr [rsp + 0x30]
0x001D7919: mov dword ptr [rdi + 8], eax
0x001D791C: mov al, 1
0x001D791E: add rsp, 0x20
0x001D7922: pop rdi
0x001D7923: ret
0x001D7924: int3
0x001D7925: int3
0x001D7926: int3
0x001D7927: int3
0x001D7928: int3
0x001D7929: int3
0x001D792A: int3
0x001D792B: int3
0x001D792C: int3
0x001D792D: int3
0x001D792E: int3
0x001D792F: int3
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
```

## Direct callers of code RVAs in 0x1D78B0..0x1D7930

- call `0x001D7B5B` -> `0x001D78B0`

```asm
0x001D7ADB: stc
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
```
