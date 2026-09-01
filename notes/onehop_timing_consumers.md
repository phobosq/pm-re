# One-hop timing consumers

Scope: direct callees of vendor-specific methods in confirmed type1/type2 runtime vtables.
A hit is only a candidate until the callsite proves the relevant object/snapshot is passed.

unique callees: 48
callees with timing-like accesses: 3

## candidate 1: `0x0015FA00` range `0x0015FA00..0x0015FA80`

Fields: record.mt?(+0x98)

### Origins / callsites

- type1 slot `+0x48` method `0x00168780`, call `0x001687E0`
```asm
0x001687B9: imul r9, rax, 0x3b9aca00
0x001687C0: imul rax, rdx, 0x3b9aca00
0x001687C7: cqo
0x001687C9: idiv rbx
0x001687CC: lea rdx, [r9 + 0x77359400]
0x001687D3: add rdx, rax
0x001687D6: lea rbx, [rdi + 0x7c0]
0x001687DD: mov rcx, rbx
0x001687E0: call 0x14015fa00
```

### Timing-like accesses

- `0x0015FA4E` record.mt? `+0x98`: `mov dword ptr [rbx + 0x98], 0xffffffff`

### Access contexts

```asm
0x0015FA2B: mov byte ptr [rsp + 0x30], 1
0x0015FA30: lea rcx, [rbx + 0x50]
0x0015FA34: mov r9, rbx
0x0015FA37: lea r8, [rsp + 0x58]
0x0015FA3C: lea rdx, [rsp + 0x28]
0x0015FA41: call 0x140160b40
0x0015FA46: test al, al
0x0015FA48: jne 0x14015fa4e
0x0015FA4A: xor bl, bl
0x0015FA4C: jmp 0x14015fa5a
0x0015FA4E: mov dword ptr [rbx + 0x98], 0xffffffff
0x0015FA58: mov bl, 1
0x0015FA5A: cmp byte ptr [rsp + 0x30], 0
0x0015FA5F: je 0x14015fa77
0x0015FA61: mov rcx, qword ptr [rsp + 0x28]
0x0015FA66: call 0x140391b24
0x0015FA6B: test eax, eax
0x0015FA6D: je 0x14015fa77
0x0015FA6F: mov ecx, eax
0x0015FA71: call 0x14039219c
0x0015FA76: nop
0x0015FA77: movzx eax, bl
0x0015FA7A: add rsp, 0x40
0x0015FA7E: pop rbx
0x0015FA7F: ret
```

## candidate 2: `0x00169520` range `0x00169520..0x001695A9`

Fields: record.mt?(+0x98)

### Origins / callsites

- type1 slot `+0x50` method `0x001688D0`, call `0x00168925`
```asm
0x001688FD: xor rax, rsp
0x00168900: mov qword ptr [rsp + 0x438], rax
0x00168908: mov r14, r8
0x0016890B: mov qword ptr [rsp + 0x60], rdx
0x00168910: mov rsi, rcx
0x00168913: mov qword ptr [rsp + 0x98], rcx
0x0016891B: lea rbx, [rcx + 0x7c0]
0x00168922: mov rcx, rbx
0x00168925: call 0x140169520
```
- type1 slot `+0x50` method `0x001688D0`, call `0x00168A22`
```asm
0x00168A04: mov r13d, dword ptr [rsp + 0x1b4]
0x00168A0C: cmp dword ptr [rsp + 0x1cc], 0
0x00168A14: jg 0x140168a1f
0x00168A16: test r13d, r13d
0x00168A19: je 0x140168a1f
0x00168A1B: test dl, dl
0x00168A1D: je 0x140168a98
0x00168A1F: mov rcx, rbx
0x00168A22: call 0x140169520
```
- type1 slot `+0x50` method `0x001688D0`, call `0x00168ACA`
```asm
0x00168A9C: mov rcx, qword ptr [r14 + 0x10]
0x00168AA0: call 0x140159b40
0x00168AA5: mov dword ptr [rsp + 0x58], eax
0x00168AA9: cmp qword ptr [rsi + 0x888], 0
0x00168AB1: jne 0x1401690b7
0x00168AB7: mov qword ptr [rsp + 0xd8], rbx
0x00168ABF: mov byte ptr [rsp + 0xe0], 0
0x00168AC7: mov rcx, rbx
0x00168ACA: call 0x140169520
```
- type1 slot `+0x50` method `0x001688D0`, call `0x00169428`
```asm
0x001693FC: call 0x1403d23c8
0x00169401: lea rax, [rip + 0x2ca580]
0x00169408: mov qword ptr [rsp + 0xa8], rax
0x00169410: lea rdx, [rip + 0x621b49]
0x00169417: lea rcx, [rsp + 0xa8]
0x0016941F: call 0x1403d25d0
0x00169424: nop
0x00169425: mov rcx, rbx
0x00169428: call 0x140169520
```
- type1 slot `+0x70` method `0x001620F0`, call `0x0016211E`
```asm
0x001620F6: mov qword ptr [rsp + 0x20], 0xfffffffffffffffe
0x001620FF: mov qword ptr [rsp + 0x48], rbx
0x00162104: mov qword ptr [rsp + 0x50], rsi
0x00162109: mov rsi, rdx
0x0016210C: mov rdi, rcx
0x0016210F: lea rbx, [rcx + 0x7c0]
0x00162116: mov qword ptr [rsp + 0x40], rbx
0x0016211B: mov rcx, rbx
0x0016211E: call 0x140169520
```
- type1 slot `+0x78` method `0x00169F20`, call `0x00169F46`
```asm
0x00169F20: push rdi
0x00169F22: sub rsp, 0x30
0x00169F26: mov qword ptr [rsp + 0x20], 0xfffffffffffffffe
0x00169F2F: mov qword ptr [rsp + 0x48], rbx
0x00169F34: mov rdi, rcx
0x00169F37: lea rbx, [rcx + 0x7c0]
0x00169F3E: mov qword ptr [rsp + 0x40], rbx
0x00169F43: mov rcx, rbx
0x00169F46: call 0x140169520
```
- type1 slot `+0x80` method `0x00164350`, call `0x00164373`
```asm
0x00164350: push rdi
0x00164352: sub rsp, 0x30
0x00164356: mov qword ptr [rsp + 0x20], 0xfffffffffffffffe
0x0016435F: mov qword ptr [rsp + 0x40], rbx
0x00164364: mov qword ptr [rsp + 0x48], rsi
0x00164369: mov rdi, rcx
0x0016436C: add rcx, 0x7c0
0x00164373: call 0x140169520
```

### Timing-like accesses

- `0x00169551` record.mt? `+0x98`: `cmp dword ptr [rbx + 0x98], 0`
- `0x00169577` record.mt? `+0x98`: `cmp dword ptr [rbx + 0x98], 0`
- `0x00169580` record.mt? `+0x98`: `mov dword ptr [rbx + 0x98], 0xffffffff`

### Access contexts

```asm
0x00169526: mov qword ptr [rsp + 0x20], 0xfffffffffffffffe
0x0016952F: mov qword ptr [rsp + 0x50], rbx
0x00169534: mov rbx, rcx
0x00169537: mov qword ptr [rsp + 0x28], rcx
0x0016953C: call 0x140391ac4
0x00169541: test eax, eax
0x00169543: je 0x14016954c
0x00169545: mov ecx, eax
0x00169547: call 0x14039219c
0x0016954C: mov byte ptr [rsp + 0x30], 1
0x00169551: cmp dword ptr [rbx + 0x98], 0
0x00169558: je 0x140169580
0x0016955A: nop word ptr [rax + rax]
0x00169560: mov rdx, rbx
0x00169563: lea rcx, [rbx + 0x50]
0x00169567: call 0x140391ec4
0x0016956C: test eax, eax
0x0016956E: je 0x140169577
0x00169570: mov ecx, eax
0x00169572: call 0x14039219c
0x00169577: cmp dword ptr [rbx + 0x98], 0
0x0016957E: jne 0x140169560
0x00169580: mov dword ptr [rbx + 0x98], 0xffffffff
0x0016958A: mov rcx, rbx
0x0016958D: call 0x140391b24
0x00169592: test eax, eax
0x00169594: je 0x14016959e
0x00169596: mov ecx, eax
```

```asm
0x00169551: cmp dword ptr [rbx + 0x98], 0
0x00169558: je 0x140169580
0x0016955A: nop word ptr [rax + rax]
0x00169560: mov rdx, rbx
0x00169563: lea rcx, [rbx + 0x50]
0x00169567: call 0x140391ec4
0x0016956C: test eax, eax
0x0016956E: je 0x140169577
0x00169570: mov ecx, eax
0x00169572: call 0x14039219c
0x00169577: cmp dword ptr [rbx + 0x98], 0
0x0016957E: jne 0x140169560
0x00169580: mov dword ptr [rbx + 0x98], 0xffffffff
0x0016958A: mov rcx, rbx
0x0016958D: call 0x140391b24
0x00169592: test eax, eax
0x00169594: je 0x14016959e
0x00169596: mov ecx, eax
0x00169598: call 0x14039219c
0x0016959D: nop
0x0016959E: mov rbx, qword ptr [rsp + 0x50]
0x001695A3: add rsp, 0x40
0x001695A7: pop rdi
0x001695A8: ret
```

```asm
0x0016955A: nop word ptr [rax + rax]
0x00169560: mov rdx, rbx
0x00169563: lea rcx, [rbx + 0x50]
0x00169567: call 0x140391ec4
0x0016956C: test eax, eax
0x0016956E: je 0x140169577
0x00169570: mov ecx, eax
0x00169572: call 0x14039219c
0x00169577: cmp dword ptr [rbx + 0x98], 0
0x0016957E: jne 0x140169560
0x00169580: mov dword ptr [rbx + 0x98], 0xffffffff
0x0016958A: mov rcx, rbx
0x0016958D: call 0x140391b24
0x00169592: test eax, eax
0x00169594: je 0x14016959e
0x00169596: mov ecx, eax
0x00169598: call 0x14039219c
0x0016959D: nop
0x0016959E: mov rbx, qword ptr [rsp + 0x50]
0x001695A3: add rsp, 0x40
0x001695A7: pop rdi
0x001695A8: ret
```

## candidate 3: `0x0016AAF0` range `0x0016AAF0..0x0016AB4B`

Fields: record.mt?(+0x98)

### Origins / callsites

- type1 slot `+0x50` method `0x001688D0`, call `0x00168B36`
```asm
0x00168B15: mov rcx, rdi
0x00168B18: call 0x14016b960
0x00168B1D: mov edx, 0x88
0x00168B22: mov rcx, rdi
0x00168B25: call 0x1403b20dc
0x00168B2A: test rbx, rbx
0x00168B2D: je 0x140169067
0x00168B33: mov rcx, rbx
0x00168B36: call 0x14016aaf0
```

### Timing-like accesses

- `0x0016AB12` record.mt? `+0x98`: `mov dword ptr [rbx + 0x98], 0`

### Access contexts

```asm
0x0016AAF0: push rbx
0x0016AAF2: sub rsp, 0x30
0x0016AAF6: mov qword ptr [rsp + 0x20], 0xfffffffffffffffe
0x0016AAFF: mov rbx, rcx
0x0016AB02: call 0x140391ac4
0x0016AB07: test eax, eax
0x0016AB09: je 0x14016ab12
0x0016AB0B: mov ecx, eax
0x0016AB0D: call 0x14039219c
0x0016AB12: mov dword ptr [rbx + 0x98], 0
0x0016AB1C: mov rcx, rbx
0x0016AB1F: call 0x140391b24
0x0016AB24: test eax, eax
0x0016AB26: je 0x14016ab30
0x0016AB28: mov ecx, eax
0x0016AB2A: call 0x14039219c
0x0016AB2F: nop
0x0016AB30: lea rcx, [rbx + 0x50]
0x0016AB34: call 0x140391e8c
0x0016AB39: test eax, eax
0x0016AB3B: je 0x14016ab45
0x0016AB3D: mov ecx, eax
0x0016AB3F: call 0x14039219c
0x0016AB44: nop
0x0016AB45: add rsp, 0x30
0x0016AB49: pop rbx
0x0016AB4A: ret
```
