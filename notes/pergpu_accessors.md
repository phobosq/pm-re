# Per-GPU stride accessors and callers

## helper `0x000E07F0..0x000E0876`

```asm
0x000E07F0: mov qword ptr [rsp + 8], rbx
0x000E07F5: push rdi
0x000E07F6: sub rsp, 0x20
0x000E07FA: movsxd rbx, edx
0x000E07FD: mov rdi, rcx
0x000E0800: test r8d, r8d
0x000E0803: js 0x1400e0851
0x000E0805: mov eax, 1
0x000E080A: cmp r8d, eax
0x000E080D: cmovg eax, r8d
0x000E0811: movd xmm0, eax
0x000E0815: cvtdq2pd xmm0, xmm0
0x000E0819: call 0x1403e69f8
0x000E081E: mov rax, qword ptr [rdi]
0x000E0821: addsd xmm0, xmm0
0x000E0825: imul rbx, rbx, 0xd8
0x000E082C: add rbx, qword ptr [rax + 0x2c0]
0x000E0833: call 0x1403e6d3c
0x000E0838: addsd xmm0, qword ptr [rip + 0x3537f0]
0x000E0840: cvttsd2si eax, xmm0
0x000E0844: mov dword ptr [rbx], eax
0x000E0846: mov rbx, qword ptr [rsp + 0x30]
0x000E084B: add rsp, 0x20
0x000E084F: pop rdi
0x000E0850: ret
0x000E0851: mov rcx, qword ptr [rcx]
0x000E0854: mov eax, r8d
0x000E0857: mov rbx, qword ptr [rsp + 0x30]
0x000E085C: cdq
0x000E085D: xor eax, edx
0x000E085F: sub eax, edx
0x000E0861: mov dword ptr [rcx + 0x130], eax
0x000E0867: mov rcx, qword ptr [rdi]
0x000E086A: mov dword ptr [rcx + 0x138], eax
0x000E0870: add rsp, 0x20
0x000E0874: pop rdi
0x000E0875: ret
```

### direct callers

count: 0
## helper `0x000E15A0..0x000E1605`

```asm
0x000E15A0: mov qword ptr [rsp + 8], rbx
0x000E15A5: push rdi
0x000E15A6: sub rsp, 0x20
0x000E15AA: mov r9d, dword ptr [r8]
0x000E15AD: mov rdi, rcx
0x000E15B0: movsxd rbx, dword ptr [rdx]
0x000E15B3: test r9d, r9d
0x000E15B6: js 0x1400e15fa
0x000E15B8: mov eax, 1
0x000E15BD: cmp r9d, eax
0x000E15C0: cmovg eax, r9d
0x000E15C4: movd xmm0, eax
0x000E15C8: cvtdq2pd xmm0, xmm0
0x000E15CC: call 0x1403e69f8
0x000E15D1: mov rax, qword ptr [rdi + 8]
0x000E15D5: addsd xmm0, xmm0
0x000E15D9: imul rbx, rbx, 0xd8
0x000E15E0: add rbx, qword ptr [rax + 0x2c0]
0x000E15E7: call 0x1403e6d3c
0x000E15EC: addsd xmm0, qword ptr [rip + 0x352a3c]
0x000E15F4: cvttsd2si eax, xmm0
0x000E15F8: mov dword ptr [rbx], eax
0x000E15FA: mov rbx, qword ptr [rsp + 0x30]
0x000E15FF: add rsp, 0x20
0x000E1603: pop rdi
0x000E1604: ret
```

### direct callers

count: 0