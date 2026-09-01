# VMR setter path — accessors and common parser tail

## timing accessors dd510/dd570/dd5f0 `0x000DD4D0..0x000DD630`

```asm
0x000DD4D0: and al, 0x20
0x000DD4D3: movups xmmword ptr [rbx + 0x28], xmm0
0x000DD4D7: mov qword ptr [rbx + 0x38], rax
0x000DD4DB: cmp qword ptr [rdi + 0x10], 0x10
0x000DD4E0: jbe 0x1400dd4ef
0x000DD4E2: mov rcx, qword ptr [rdi]
0x000DD4E5: test rcx, rcx
0x000DD4E8: je 0x1400dd4ef
0x000DD4EA: call 0x1403b20dc
0x000DD4EF: mov rax, rbx
0x000DD4F2: mov rcx, qword ptr [rsp + 0x68]
0x000DD4F7: xor rcx, rsp
0x000DD4FA: call 0x1403b24c0
0x000DD4FF: add rsp, 0x78
0x000DD503: pop rdi
0x000DD504: pop rbx
0x000DD505: ret
0x000DD506: int3
0x000DD507: int3
0x000DD508: int3
0x000DD509: int3
0x000DD50A: int3
0x000DD50B: int3
0x000DD50C: int3
0x000DD50D: int3
0x000DD50E: int3
0x000DD50F: int3
0x000DD510: lea rax, [rip + 0x361b99]
0x000DD517: mov qword ptr [rcx], rax
0x000DD51A: mov rax, rcx
0x000DD51D: mov qword ptr [rcx + 8], rdx
0x000DD521: mov qword ptr [rcx + 0x38], rcx
0x000DD525: ret
0x000DD526: int3
0x000DD527: int3
0x000DD528: int3
0x000DD529: int3
0x000DD52A: int3
0x000DD52B: int3
0x000DD52C: int3
0x000DD52D: int3
0x000DD52E: int3
0x000DD52F: int3
0x000DD530: lea rax, [rip + 0x361e89]
0x000DD537: mov qword ptr [rcx], rax
0x000DD53A: mov rax, rcx
0x000DD53D: mov qword ptr [rcx + 8], rdx
0x000DD541: mov qword ptr [rcx + 0x38], rcx
0x000DD545: ret
0x000DD546: int3
0x000DD547: int3
0x000DD548: int3
0x000DD549: int3
0x000DD54A: int3
0x000DD54B: int3
0x000DD54C: int3
0x000DD54D: int3
0x000DD54E: int3
0x000DD54F: int3
0x000DD550: lea rax, [rip + 0x361d19]
0x000DD557: mov qword ptr [rcx], rax
0x000DD55A: mov rax, rcx
0x000DD55D: mov qword ptr [rcx + 8], rdx
0x000DD561: mov qword ptr [rcx + 0x38], rcx
0x000DD565: ret
0x000DD566: int3
0x000DD567: int3
0x000DD568: int3
0x000DD569: int3
0x000DD56A: int3
0x000DD56B: int3
0x000DD56C: int3
0x000DD56D: int3
0x000DD56E: int3
0x000DD56F: int3
0x000DD570: lea rax, [rip + 0x361b71]
0x000DD577: mov qword ptr [rcx], rax
0x000DD57A: mov rax, rcx
0x000DD57D: mov qword ptr [rcx + 8], rdx
0x000DD581: mov qword ptr [rcx + 0x38], rcx
0x000DD585: ret
0x000DD586: int3
0x000DD587: int3
0x000DD588: int3
0x000DD589: int3
0x000DD58A: int3
0x000DD58B: int3
0x000DD58C: int3
0x000DD58D: int3
0x000DD58E: int3
0x000DD58F: int3
0x000DD590: lea rax, [rip + 0x361a71]
0x000DD597: mov qword ptr [rcx], rax
0x000DD59A: mov rax, rcx
0x000DD59D: mov qword ptr [rcx + 8], rdx
0x000DD5A1: mov qword ptr [rcx + 0x38], rcx
0x000DD5A5: ret
0x000DD5A6: int3
0x000DD5A7: int3
0x000DD5A8: int3
0x000DD5A9: int3
0x000DD5AA: int3
0x000DD5AB: int3
0x000DD5AC: int3
0x000DD5AD: int3
0x000DD5AE: int3
0x000DD5AF: int3
0x000DD5B0: lea rax, [rip + 0x3619a9]
0x000DD5B7: mov qword ptr [rcx], rax
0x000DD5BA: mov rax, rcx
0x000DD5BD: mov qword ptr [rcx + 8], rdx
0x000DD5C1: mov qword ptr [rcx + 0x38], rcx
0x000DD5C5: ret
0x000DD5C6: int3
0x000DD5C7: int3
0x000DD5C8: int3
0x000DD5C9: int3
0x000DD5CA: int3
0x000DD5CB: int3
0x000DD5CC: int3
0x000DD5CD: int3
0x000DD5CE: int3
0x000DD5CF: int3
0x000DD5D0: lea rax, [rip + 0x361d09]
0x000DD5D7: mov qword ptr [rcx], rax
0x000DD5DA: mov rax, rcx
0x000DD5DD: mov qword ptr [rcx + 8], rdx
0x000DD5E1: mov qword ptr [rcx + 0x38], rcx
0x000DD5E5: ret
0x000DD5E6: int3
0x000DD5E7: int3
0x000DD5E8: int3
0x000DD5E9: int3
0x000DD5EA: int3
0x000DD5EB: int3
0x000DD5EC: int3
0x000DD5ED: int3
0x000DD5EE: int3
0x000DD5EF: int3
0x000DD5F0: lea rax, [rip + 0x361b29]
0x000DD5F7: mov qword ptr [rcx], rax
0x000DD5FA: mov rax, rcx
0x000DD5FD: mov qword ptr [rcx + 8], rdx
0x000DD601: mov qword ptr [rcx + 0x38], rcx
0x000DD605: ret
0x000DD606: int3
0x000DD607: int3
0x000DD608: int3
0x000DD609: int3
0x000DD60A: int3
0x000DD60B: int3
0x000DD60C: int3
0x000DD60D: int3
0x000DD60E: int3
0x000DD60F: int3
0x000DD610: lea rax, [rip + 0x361981]
0x000DD617: mov qword ptr [rcx], rax
0x000DD61A: mov rax, rcx
0x000DD61D: mov qword ptr [rcx + 8], rdx
0x000DD621: mov qword ptr [rcx + 0x38], rcx
0x000DD625: ret
0x000DD626: int3
0x000DD627: int3
0x000DD628: int3
0x000DD629: int3
0x000DD62A: int3
0x000DD62B: int3
0x000DD62C: int3
0x000DD62D: int3
0x000DD62E: int3
0x000DD62F: int3
```

## common option tail `0x000E9D40..0x000E9DE0`

```asm
0x000E9D40: add byte ptr [rax - 0x73], cl
0x000E9D43: lea edi, [rax]
0x000E9D45: or eax, 0xe3e80000
0x000E9D4A: add al, 0xf5
0x000E9D4C: dec dword ptr [rax - 0x75]
0x000E9D4F: ror byte ptr [rax - 0x73], 1
0x000E9D52: lea ebx, [rax + 0xc]
0x000E9D55: add byte ptr [rax], al
0x000E9D57: call 0x140029c50
0x000E9D5C: movzx ebx, al
0x000E9D5F: lea rcx, [rbp + 0x1110]
0x000E9D66: call 0x140032ef0
0x000E9D6B: test bl, bl
0x000E9D6D: je 0x1400e9da4
0x000E9D6F: mov rdx, rdi
0x000E9D72: lea rcx, [rbp + 0x8c8]
0x000E9D79: call 0x1400dd530
0x000E9D7E: mov r9, rax
0x000E9D81: mov dword ptr [rsp + 0x28], 1
0x000E9D89: mov dword ptr [rsp + 0x20], r13d
0x000E9D8E: mov r8, r14
0x000E9D91: mov rdx, rsi
0x000E9D94: lea rcx, [rdi + 0x2d8]
0x000E9D9B: call 0x140090ab0
0x000E9DA0: mov bl, 1
0x000E9DA2: jmp 0x1400e9da6
0x000E9DA4: xor bl, bl
0x000E9DA6: lea rcx, [rbp + 0xc58]
0x000E9DAD: call 0x140032ef0
0x000E9DB2: movzx eax, bl
0x000E9DB5: mov rcx, qword ptr [rbp + 0x15d0]
0x000E9DBC: xor rcx, rsp
0x000E9DBF: call 0x1403b24c0
0x000E9DC4: mov rbx, qword ptr [rsp + 0x1738]
0x000E9DCC: add rsp, 0x16e0
0x000E9DD3: pop r15
0x000E9DD5: pop r14
0x000E9DD7: pop r13
0x000E9DD9: pop r12
0x000E9DDB: pop rdi
0x000E9DDC: pop rsi
0x000E9DDD: pop rbp
0x000E9DDE: ret
0x000E9DDF: int3
```
