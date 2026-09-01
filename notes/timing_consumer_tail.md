# Five-field timing consumer tail

function: `0x003053C0..0x00305BB6`
tail: `0x00305920..0x00305BB6`

Confirmed config fields: mt `+0x98`, straps `+0xAC`, vmr/rxboost `+0xB0`, vmt2 `+0xB8`, vmt3 `+0xBC`.

## Tail disassembly

```asm
0x00305920: fisubr word ptr [rbx]
0x00305922: fadd dword ptr [rbx + rax - 0x35]
0x00305926: xor r10d, r9d
0x00305929: xor r9d, edi
0x0030592C: mov edi, ebx
0x0030592E: xor ebx, r11d
0x00305931: xor edi, r8d
0x00305934: movzx eax, bx
0x00305937: mov ebx, dword ptr [rcx + 0x8c]
0x0030593D: mov r8d, ebx
0x00305940: imul r8d, eax
0x00305944: test r8d, r8d
0x00305947: je 0x14030595e
0x00305949: mov eax, r8d
0x0030594C: movzx r11d, r8w
0x00305950: shr eax, 0x10
0x00305953: sub r11d, eax
0x00305956: mov eax, r11d
0x00305959: shr eax, 0x10
0x0030595C: jmp 0x140305964
0x0030595E: mov r11d, edx
0x00305961: sub r11d, ebx
0x00305964: mov ebx, dword ptr [rcx + 0x98]
0x0030596A: sub r11d, eax
0x0030596D: add edi, dword ptr [rcx + 0x90]
0x00305973: mov r8d, ebx
0x00305976: add r9d, dword ptr [rcx + 0x94]
0x0030597D: movzx eax, r10w
0x00305981: imul r8d, eax
0x00305985: test r8d, r8d
0x00305988: je 0x14030599f
0x0030598A: mov eax, r8d
0x0030598D: movzx r10d, r8w
0x00305991: shr eax, 0x10
0x00305994: sub r10d, eax
0x00305997: mov eax, r10d
0x0030599A: shr eax, 0x10
0x0030599D: jmp 0x1403059a5
0x0030599F: mov r10d, edx
0x003059A2: sub r10d, ebx
0x003059A5: mov ebx, dword ptr [rcx + 0x9c]
0x003059AB: sub r10d, eax
0x003059AE: mov eax, r9d
0x003059B1: mov r8d, ebx
0x003059B4: xor eax, r11d
0x003059B7: movzx eax, ax
0x003059BA: imul r8d, eax
0x003059BE: test r8d, r8d
0x003059C1: je 0x1403059d8
0x003059C3: mov eax, r8d
0x003059C6: movzx r8d, r8w
0x003059CA: shr eax, 0x10
0x003059CD: sub r8d, eax
0x003059D0: mov eax, r8d
0x003059D3: shr eax, 0x10
0x003059D6: jmp 0x1403059de
0x003059D8: mov r8d, edx
0x003059DB: sub r8d, ebx
0x003059DE: mov esi, dword ptr [rcx + 0xa0]
0x003059E4: sub r8d, eax
0x003059E7: mov eax, r10d
0x003059EA: mov ebx, esi
0x003059EC: xor eax, edi
0x003059EE: add eax, r8d
0x003059F1: movzx eax, ax
0x003059F4: imul ebx, eax
0x003059F7: test ebx, ebx
0x003059F9: je 0x140305a0c
0x003059FB: mov eax, ebx
0x003059FD: movzx ebx, bx
0x00305A00: shr eax, 0x10
0x00305A03: sub ebx, eax
0x00305A05: mov eax, ebx
0x00305A07: shr eax, 0x10
0x00305A0A: jmp 0x140305a10
0x00305A0C: mov ebx, edx
0x00305A0E: sub ebx, esi
0x00305A10: sub ebx, eax
0x00305A12: add r8d, ebx
0x00305A15: xor r10d, r8d
0x00305A18: xor r8d, edi
0x00305A1B: mov edi, ebx
0x00305A1D: xor ebx, r11d
0x00305A20: xor edi, r9d
0x00305A23: movzx eax, bx
0x00305A26: mov ebx, dword ptr [rcx + 0xa4]
0x00305A2C: mov r9d, ebx
0x00305A2F: imul r9d, eax
0x00305A33: test r9d, r9d
0x00305A36: je 0x140305a4d
0x00305A38: mov eax, r9d
0x00305A3B: movzx r11d, r9w
0x00305A3F: shr eax, 0x10
0x00305A42: sub r11d, eax
0x00305A45: mov eax, r11d
0x00305A48: shr eax, 0x10
0x00305A4B: jmp 0x140305a53
0x00305A4D: mov r11d, edx
0x00305A50: sub r11d, ebx
0x00305A53: mov ebx, dword ptr [rcx + 0xb0]
0x00305A59: sub r11d, eax
0x00305A5C: add edi, dword ptr [rcx + 0xa8]
0x00305A62: mov r9d, ebx
0x00305A65: add r8d, dword ptr [rcx + 0xac]
0x00305A6C: movzx eax, r10w
0x00305A70: imul r9d, eax
0x00305A74: test r9d, r9d
0x00305A77: je 0x140305a8e
0x00305A79: mov eax, r9d
0x00305A7C: movzx r10d, r9w
0x00305A80: shr eax, 0x10
0x00305A83: sub r10d, eax
0x00305A86: mov eax, r10d
0x00305A89: shr eax, 0x10
0x00305A8C: jmp 0x140305a94
0x00305A8E: mov r10d, edx
0x00305A91: sub r10d, ebx
0x00305A94: mov ebx, dword ptr [rcx + 0xb4]
0x00305A9A: sub r10d, eax
0x00305A9D: mov eax, r8d
0x00305AA0: mov r9d, ebx
0x00305AA3: xor eax, r11d
0x00305AA6: movzx eax, ax
0x00305AA9: imul r9d, eax
0x00305AAD: test r9d, r9d
0x00305AB0: je 0x140305ac7
0x00305AB2: mov eax, r9d
0x00305AB5: movzx r9d, r9w
0x00305AB9: shr eax, 0x10
0x00305ABC: sub r9d, eax
0x00305ABF: mov eax, r9d
0x00305AC2: shr eax, 0x10
0x00305AC5: jmp 0x140305acd
0x00305AC7: mov r9d, edx
0x00305ACA: sub r9d, ebx
0x00305ACD: mov esi, dword ptr [rcx + 0xb8]
0x00305AD3: sub r9d, eax
0x00305AD6: mov eax, r10d
0x00305AD9: mov ebx, esi
0x00305ADB: xor eax, edi
0x00305ADD: add eax, r9d
0x00305AE0: movzx eax, ax
0x00305AE3: imul ebx, eax
0x00305AE6: test ebx, ebx
0x00305AE8: je 0x140305afb
0x00305AEA: mov eax, ebx
0x00305AEC: movzx ebx, bx
0x00305AEF: shr eax, 0x10
0x00305AF2: sub ebx, eax
0x00305AF4: mov eax, ebx
0x00305AF6: shr eax, 0x10
0x00305AF9: jmp 0x140305aff
0x00305AFB: mov ebx, edx
0x00305AFD: sub ebx, esi
0x00305AFF: sub ebx, eax
0x00305B01: add r9d, ebx
0x00305B04: xor r10d, r9d
0x00305B07: xor r9d, edi
0x00305B0A: mov edi, ebx
0x00305B0C: xor ebx, r11d
0x00305B0F: mov r11d, dword ptr [rcx + 0xbc]
0x00305B16: xor edi, r8d
0x00305B19: movzx eax, bx
0x00305B1C: mov r8d, r11d
0x00305B1F: imul r8d, eax
0x00305B23: test r8d, r8d
0x00305B26: je 0x140305b3d
0x00305B28: mov eax, r8d
0x00305B2B: movzx r8d, r8w
0x00305B2F: shr eax, 0x10
0x00305B32: sub r8d, eax
0x00305B35: mov eax, r8d
0x00305B38: shr eax, 0x10
0x00305B3B: jmp 0x140305b43
0x00305B3D: mov r8d, edx
0x00305B40: sub r8d, r11d
0x00305B43: mov r11d, dword ptr [rcx + 0xc0]
0x00305B4A: sub r8d, eax
0x00305B4D: add r11d, r9d
0x00305B50: movzx eax, r10w
0x00305B54: mov r9d, dword ptr [rcx + 0xc4]
0x00305B5B: mov r10d, dword ptr [rcx + 0xc8]
0x00305B62: add r9d, edi
0x00305B65: mov ecx, r10d
0x00305B68: imul ecx, eax
0x00305B6B: test ecx, ecx
0x00305B6D: je 0x140305b80
0x00305B6F: mov eax, ecx
0x00305B71: movzx edx, cx
0x00305B74: shr eax, 0x10
0x00305B77: sub edx, eax
0x00305B79: mov eax, edx
0x00305B7B: shr eax, 0x10
0x00305B7E: jmp 0x140305b83
0x00305B80: sub edx, r10d
0x00305B83: mov rbx, qword ptr [rsp + 8]
0x00305B88: sub edx, eax
0x00305B8A: mov rsi, qword ptr [rsp + 0x10]
0x00305B8F: mov rdi, qword ptr [rsp + 0x18]
0x00305B94: movzx eax, r11w
0x00305B98: shl r8d, 0x10
0x00305B9C: or eax, r8d
0x00305B9F: shl r9d, 0x10
0x00305BA3: mov dword ptr [r14], eax
0x00305BA6: movzx eax, dx
0x00305BA9: or r9d, eax
0x00305BAC: mov dword ptr [r14 + 4], r9d
0x00305BB0: mov r14, qword ptr [rsp + 0x20]
0x00305BB5: ret
```

## Calls in tail

| callsite | target/form |
|---|---|

## Direct callers to 0x3053C0

- `0x00304B39`
- `0x00304F5C`
- `0x00305062`
- `0x003051D6`
- `0x00305299`
- `0x00305C78`
- `0x00305D4D`
- `0x00305EEE`