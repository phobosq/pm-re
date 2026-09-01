# VMR consumer function correlation

candidate functions: 5

| score | PDATA | +0x2C0 | imul 0xD8 | +0xB0 reads |
|---:|---|---:|---:|---:|
| 9 | `0x000CAAD0..0x000D9A27` | 2 | 0 | 1 |
| 9 | `0x001F7F40..0x001FB9C1` | 2 | 0 | 1 |
| 9 | `0x00283B10..0x0028560C` | 2 | 0 | 2 |
| 8 | `0x000E07F0..0x000E0876` | 1 | 1 | 0 |
| 8 | `0x000E15A0..0x000E1605` | 1 | 1 | 0 |

## Exact/high candidates

### score 9 `0x000CAAD0..0x000D9A27`

Key instructions:

- owner: `0x000D394C: mov dword ptr [rbp + 0x2c0], 0x25`
- owner: `0x000D39B5: lea rcx, [rbp + 0x2c0]`
- vmr-read: `0x000D998B: mov eax, dword ptr [rbx + 0xb0]`

### score 9 `0x001F7F40..0x001FB9C1`

Key instructions:

- owner: `0x001F9038: mov qword ptr [rbp + r12*8 + 0x2c0], rdx`
- owner: `0x001F90D4: mov r9, qword ptr [rbp + rbx*8 + 0x2c0]`
- vmr-read: `0x001F8EA8: cmp r14d, dword ptr [rsi + 0xb0]`

### score 9 `0x00283B10..0x0028560C`

Key instructions:

- owner: `0x00284B99: mov byte ptr [rsp + 0x2c0], cl`
- owner: `0x00284BA0: movsx ecx, byte ptr [rsp + 0x2c0]`
- vmr-read: `0x002850BB: mov eax, dword ptr [rbx + 0xb0]`
- vmr-read: `0x002850C1: cmp dword ptr [rcx + 0xb0], eax`

### score 8 `0x000E07F0..0x000E0876`

Key instructions:

- owner: `0x000E082C: add rbx, qword ptr [rax + 0x2c0]`
- stride: `0x000E0825: imul rbx, rbx, 0xd8`

### score 8 `0x000E15A0..0x000E1605`

Key instructions:

- owner: `0x000E15E0: add rbx, qword ptr [rax + 0x2c0]`
- stride: `0x000E15D9: imul rbx, rbx, 0xd8`
