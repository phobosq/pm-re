# PM62C_MAIN indirect call census

range: `0x00129A50..0x0012DA40`

Static-only Capstone decode. Context = previous 5 + next 3 decoded instructions.

## 0x00129AA5: call qword ptr [rip + 0x30680d]
kind: `rip_indirect` target/source: `0x004302B8`

```asm
0x00129A8E: movsxd r15, ecx
0x00129A91: mov qword ptr [rsp + 0xb0], rdx
0x00129A99: xor r14d, r14d
0x00129A9C: mov dword ptr [rsp + 0x50], r14d
0x00129AA1: lea ecx, [r14 + 3]
0x00129AA5: call qword ptr [rip + 0x30680d]
0x00129AAB: mov qword ptr [rsp + 0x58], r15
0x00129AB0: mov eax, 1
0x00129AB5: mov qword ptr [rsp + 0x80], rax
```

## 0x0012B175: call qword ptr [rax + 0x10]
kind: `memory_indirect` target/source: `[rax+0x10]`

```asm
0x0012B164: nop
0x0012B165: mov rcx, qword ptr [rsp + 0x130]
0x0012B16D: test rcx, rcx
0x0012B170: je 0x14012b18b
0x0012B172: mov rax, qword ptr [rcx]
0x0012B175: call qword ptr [rax + 0x10]
0x0012B178: mov rcx, rax
0x0012B17B: test rax, rax
0x0012B17E: je 0x14012b18b
```

## 0x0012B188: call qword ptr [rax]
kind: `memory_indirect` target/source: `[rax]`

```asm
0x0012B178: mov rcx, rax
0x0012B17B: test rax, rax
0x0012B17E: je 0x14012b18b
0x0012B180: mov rax, qword ptr [rax]
0x0012B183: mov edx, 1
0x0012B188: call qword ptr [rax]
0x0012B18A: nop
0x0012B18B: lea rcx, [rsp + 0x720]
0x0012B193: call 0x140129720
```

## 0x0012BFB9: call qword ptr [rax + 8]
kind: `memory_indirect` target/source: `[rax+0x8]`

```asm
0x0012BF9E: call 0x14005caf0
0x0012BFA3: mov rbx, rax
0x0012BFA6: mov rcx, qword ptr [rsp + 0x110]
0x0012BFAE: mov qword ptr [rsp + 0x120], rcx
0x0012BFB6: mov rax, qword ptr [rcx]
0x0012BFB9: call qword ptr [rax + 8]
0x0012BFBC: nop
0x0012BFBD: lea r8, [rsp + 0x118]
0x0012BFC5: lea rdx, [rsp + 0x490]
```

## 0x0012BFF6: call qword ptr [rax + 0x10]
kind: `memory_indirect` target/source: `[rax+0x10]`

```asm
0x0012BFE5: nop
0x0012BFE6: mov rcx, qword ptr [rsp + 0x110]
0x0012BFEE: test rcx, rcx
0x0012BFF1: je 0x14012c00c
0x0012BFF3: mov rax, qword ptr [rcx]
0x0012BFF6: call qword ptr [rax + 0x10]
0x0012BFF9: mov rcx, rax
0x0012BFFC: test rax, rax
0x0012BFFF: je 0x14012c00c
```

## 0x0012C009: call qword ptr [rax]
kind: `memory_indirect` target/source: `[rax]`

```asm
0x0012BFF9: mov rcx, rax
0x0012BFFC: test rax, rax
0x0012BFFF: je 0x14012c00c
0x0012C001: mov rax, qword ptr [rax]
0x0012C004: mov edx, 1
0x0012C009: call qword ptr [rax]
0x0012C00B: nop
0x0012C00C: test bl, bl
0x0012C00E: je 0x14012c6b0
```
