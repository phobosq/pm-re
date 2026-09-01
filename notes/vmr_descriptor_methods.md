# VMR descriptor method summary

vtable: `0x0043F0E8`

## slot `+0x0` -> `0x000E0AC0`

```asm
0x000E0AC0: test rdx, rdx
0x000E0AC3: je 0x1400e0ad7
0x000E0AC5: lea rax, [rip + 0x35e61c]
0x000E0ACC: mov qword ptr [rdx], rax
0x000E0ACF: mov rax, qword ptr [rcx + 8]
0x000E0AD3: mov qword ptr [rdx + 8], rax
0x000E0AD7: mov rax, rdx
0x000E0ADA: ret
```

Field-like memory displacements:
`+0x35e61c`, `+0x8`

## slot `+0x8` -> `0x000E0AC0`

```asm
0x000E0AC0: test rdx, rdx
0x000E0AC3: je 0x1400e0ad7
0x000E0AC5: lea rax, [rip + 0x35e61c]
0x000E0ACC: mov qword ptr [rdx], rax
0x000E0ACF: mov rax, qword ptr [rcx + 8]
0x000E0AD3: mov qword ptr [rdx + 8], rax
0x000E0AD7: mov rax, rdx
0x000E0ADA: ret
```

Field-like memory displacements:
`+0x35e61c`, `+0x8`

## slot `+0x10` -> `0x000E10C0`

```asm
0x000E10C0: movsxd rax, dword ptr [rdx]
0x000E10C3: imul rdx, rax, 0xd8
0x000E10CA: mov rax, qword ptr [rcx + 8]
0x000E10CE: mov rcx, qword ptr [rax + 0x2c0]
0x000E10D5: mov eax, dword ptr [r8]
0x000E10D8: mov dword ptr [rdx + rcx + 0xb0], eax
0x000E10DF: ret
```

Field-like memory displacements:
`+0x8`, `+0x2c0`, `+0xb0`

## slot `+0x18` -> `0x000E1CF0`

```asm
0x000E1CF0: lea rax, [rip + 0x6fd6d9]
0x000E1CF7: ret
```

Field-like memory displacements:
`+0x6fd6d9`

## slot `+0x20` -> `0x000E0E40`

```asm
0x000E0E40: lea rax, [rip + 0x35da19]
0x000E0E47: mov qword ptr [rcx], rax
0x000E0E4A: test dl, dl
0x000E0E4C: jne 0x1403b20d4
0x000E0E52: ret
```

Field-like memory displacements:
`+0x35da19`

## slot `+0x28` -> `0x00068CE0`

```asm
0x00068CE0: lea rax, [rcx + 8]
0x00068CE4: ret
```

Field-like memory displacements:
`+0x8`

## slot `+0x30` -> `0x00725E88`

```asm
0x00725E88: add dword ptr [rax], eax
0x00725E8A: add byte ptr [rax], al
0x00725E8C: add byte ptr [rax], al
0x00725E8E: add byte ptr [rax], al
0x00725E90: add byte ptr [rax], al
0x00725E92: add byte ptr [rax], al
0x00725E94: ror byte ptr [rsi], 0x7e
0x00725E97: add byte ptr [rax - 0x77ff8da2], dh
0x00725E9D: pop rsi
0x00725E9E: jb 0x140725ea0
0x00725EA0: add byte ptr [rax], al
0x00725EA2: add byte ptr [rax], al
0x00725EA4: add byte ptr [rax], al
0x00725EA6: add byte ptr [rax], al
0x00725EA8: add byte ptr [rax], al
0x00725EAA: add byte ptr [rax], al
0x00725EAC: add byte ptr [rax], al
0x00725EAE: add byte ptr [rax], al
0x00725EB0: add byte ptr [rax], al
0x00725EB2: add byte ptr [rax], al
0x00725EB4: add byte ptr [rax], al
0x00725EB6: add byte ptr [rax], al
0x00725EB8: add al, byte ptr [rax]
0x00725EBA: add byte ptr [rax], al
0x00725EBC: enter 0x725e, 0
0x00725EC0: add byte ptr [rax], al
0x00725EC2: add byte ptr [rax], al
0x00725EC4: add byte ptr [rax], al
0x00725EC6: add byte ptr [rax], al
0x00725EC8: loopne 0x140725f28
0x00725ECA: jb 0x140725ecc
```

Field-like memory displacements:
`-0x77ff8da2`

## slot `+0x38` -> `0x000E18F0`

```asm
0x000E18F0: test rdx, rdx
0x000E18F3: je 0x1400e1907
0x000E18F5: lea rax, [rip + 0x35d824]
0x000E18FC: mov qword ptr [rdx], rax
0x000E18FF: mov rax, qword ptr [rcx + 8]
0x000E1903: mov qword ptr [rdx + 8], rax
0x000E1907: mov rax, rdx
0x000E190A: ret
```

Field-like memory displacements:
`+0x35d824`, `+0x8`
