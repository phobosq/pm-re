# NVIDIA mode-setter wrapper reference trace

Wrapper `0x0016E0B0` tail-calls child slot +0x68.

## Absolute qword references (bytewise scan)

- none

## Direct CALL/JMP rel32 references

count: `1`

### `jmp` `0x001688BF`

```asm
0x0016889D: int3
0x0016889E: int3
0x0016889F: int3
0x001688A0: mov rax, qword ptr [rcx + 0x890]
0x001688A7: ret
0x001688A8: int3
0x001688A9: int3
0x001688AA: int3
0x001688AB: int3
0x001688AC: int3
0x001688AD: int3
0x001688AE: int3
0x001688AF: int3
0x001688B0: mov rcx, qword ptr [rcx + 0x888]
0x001688B7: test rcx, rcx
0x001688BA: jne 0x1401688bf
0x001688BC: xor al, al
0x001688BE: ret
0x001688BF: jmp 0x14016e0b0
0x001688C4: int3
0x001688C5: int3
0x001688C6: int3
0x001688C7: int3
0x001688C8: int3
```