# Runtime object provenance at 0x6FCC2

function `0x0006F940..0x000700E0`

Goal: identify provenance/type of the value in `r15` immediately before `call 0x1362D0`.

## Full function

```asm
0x0006F940: mov rax, rsp
0x0006F943: push rbp
0x0006F944: push r12
0x0006F946: push r13
0x0006F948: push r14
0x0006F94A: push r15
0x0006F94C: lea rbp, [rax - 0x4c8]
0x0006F953: sub rsp, 0x5a0
0x0006F95A: mov qword ptr [rbp + 0x40], 0xfffffffffffffffe
0x0006F962: mov qword ptr [rax + 0x10], rbx
0x0006F966: mov qword ptr [rax + 0x18], rsi
0x0006F96A: mov qword ptr [rax + 0x20], rdi
0x0006F96E: mov rax, qword ptr [rip + 0x766f7b]
0x0006F975: xor rax, rsp
0x0006F978: mov qword ptr [rbp + 0x490], rax
0x0006F97F: mov r13, rcx
0x0006F982: or edx, 0xffffffff
0x0006F985: add rcx, 0x300
0x0006F98C: call 0x14013a320
0x0006F991: xorps xmm0, xmm0
0x0006F994: movdqu xmmword ptr [rsp + 0x40], xmm0
0x0006F99A: xor esi, esi
0x0006F99C: mov qword ptr [rsp + 0x50], rsi
0x0006F9A1: lea rdx, [rsp + 0x40]
0x0006F9A6: mov rcx, r13
0x0006F9A9: call 0x1400e32c0
0x0006F9AE: test al, al
0x0006F9B0: je 0x14007001e
0x0006F9B6: lea rcx, [rbp + 0x190]
0x0006F9BD: call 0x1400e00c0
0x0006F9C2: nop
0x0006F9C3: xorps xmm0, xmm0
0x0006F9C6: movdqu xmmword ptr [rsp + 0x28], xmm0
0x0006F9CC: mov qword ptr [rsp + 0x38], rsi
0x0006F9D1: lea r8, [rsp + 0x28]
0x0006F9D6: lea rdx, [rsp + 0x40]
0x0006F9DB: lea rcx, [rbp + 0x190]
0x0006F9E2: call 0x1400ef860
0x0006F9E7: test al, al
0x0006F9E9: je 0x14006ffc9
0x0006F9EF: lea rcx, [rbp + 0x190]
0x0006F9F6: call 0x1400e2100
0x0006F9FB: mov r14d, esi
0x0006F9FE: lea rcx, [r13 + 0x300]
0x0006FA05: call 0x14013c5a0
0x0006FA0A: mov rbx, qword ptr [rax]
0x0006FA0D: mov rdi, qword ptr [rax + 8]
0x0006FA11: cmp rbx, rdi
0x0006FA14: je 0x14006fd27
0x0006FA1A: nop word ptr [rax + rax]
0x0006FA20: mov rsi, qword ptr [rbx + 8]
0x0006FA24: mov r15, qword ptr [rbx]
0x0006FA27: test rsi, rsi
0x0006FA2A: je 0x14006fa30
0x0006FA2C: lock inc dword ptr [rsi + 8]
0x0006FA30: mov qword ptr [rbp + 0x50], rsi
0x0006FA34: mov qword ptr [rbp + 0x48], r15
0x0006FA38: lea rdx, [rbp + 0x90]
0x0006FA3F: mov rcx, r15
0x0006FA42: call 0x140084a60
0x0006FA47: mov edx, r14d
0x0006FA4A: lea rcx, [rbp + 0x190]
0x0006FA51: call 0x1400e3f60
0x0006FA56: lea rcx, [rsp + 0x60]
0x0006FA5B: movups xmm0, xmmword ptr [rax]
0x0006FA5E: movups xmmword ptr [rcx], xmm0
0x0006FA61: movups xmm1, xmmword ptr [rax + 0x10]
0x0006FA65: movups xmmword ptr [rcx + 0x10], xmm1
0x0006FA69: movups xmm0, xmmword ptr [rax + 0x20]
0x0006FA6D: movups xmmword ptr [rcx + 0x20], xmm0
0x0006FA71: movups xmm1, xmmword ptr [rax + 0x30]
0x0006FA75: movups xmmword ptr [rcx + 0x30], xmm1
0x0006FA79: movups xmm0, xmmword ptr [rax + 0x40]
0x0006FA7D: movups xmmword ptr [rcx + 0x40], xmm0
0x0006FA81: movups xmm1, xmmword ptr [rax + 0x50]
0x0006FA85: movups xmmword ptr [rcx + 0x50], xmm1
0x0006FA89: movups xmm0, xmmword ptr [rax + 0x60]
0x0006FA8D: movups xmmword ptr [rcx + 0x60], xmm0
0x0006FA91: lea rcx, [rcx + 0x80]
0x0006FA98: movups xmm1, xmmword ptr [rax + 0x70]
0x0006FA9C: movups xmmword ptr [rcx - 0x10], xmm1
0x0006FAA0: sub rax, -0x80
0x0006FAA4: movups xmm0, xmmword ptr [rax]
0x0006FAA7: movups xmmword ptr [rcx], xmm0
0x0006FAAA: movups xmm1, xmmword ptr [rax + 0x10]
0x0006FAAE: movups xmmword ptr [rcx + 0x10], xmm1
0x0006FAB2: movups xmm0, xmmword ptr [rax + 0x20]
0x0006FAB6: movups xmmword ptr [rcx + 0x20], xmm0
0x0006FABA: movups xmm1, xmmword ptr [rax + 0x30]
0x0006FABE: movups xmmword ptr [rcx + 0x30], xmm1
0x0006FAC2: movups xmm0, xmmword ptr [rax + 0x40]
0x0006FAC6: movups xmmword ptr [rcx + 0x40], xmm0
0x0006FACA: mov rax, qword ptr [rax + 0x50]
0x0006FACE: mov qword ptr [rcx + 0x50], rax
0x0006FAD2: mov eax, dword ptr [rbp + 0x90]
0x0006FAD8: mov rdx, qword ptr [rsp + 0x60]
0x0006FADD: test edx, edx
0x0006FADF: cmovns eax, edx
0x0006FAE2: mov dword ptr [rbp + 0x90], eax
0x0006FAE8: mov rax, qword ptr [rsp + 0x78]
0x0006FAED: shr rax, 0x20
0x0006FAF1: mov dword ptr [rbp + 0xac], eax
0x0006FAF7: mov eax, dword ptr [rbp - 0x78]
0x0006FAFA: mov dword ptr [rbp + 0xb8], eax
0x0006FB00: mov eax, dword ptr [rbp + 0x98]
0x0006FB06: mov rcx, qword ptr [rsp + 0x68]
0x0006FB0B: test ecx, ecx
0x0006FB0D: cmovne eax, ecx
0x0006FB10: mov dword ptr [rbp + 0x98], eax
0x0006FB16: shr rcx, 0x20
0x0006FB1A: mov eax, dword ptr [rbp + 0x9c]
0x0006FB20: test ecx, ecx
0x0006FB22: cmovg eax, ecx
0x0006FB25: mov dword ptr [rbp + 0x9c], eax
0x0006FB2B: mov eax, dword ptr [rbp - 0x10]
0x0006FB2E: mov dword ptr [rbp + 0x120], eax
0x0006FB34: mov ecx, dword ptr [rbp + 0xd8]
0x0006FB3A: mov eax, dword ptr [rbp - 0x58]
0x0006FB3D: test eax, eax
0x0006FB3F: cmovns ecx, eax
0x0006FB42: mov dword ptr [rbp + 0xd8], ecx
0x0006FB48: mov ecx, dword ptr [rbp + 0xcc]
0x0006FB4E: mov eax, dword ptr [rbp - 0x64]
0x0006FB51: test eax, eax
0x0006FB53: cmovg ecx, eax
0x0006FB56: mov dword ptr [rbp + 0xcc], ecx
0x0006FB5C: mov ecx, dword ptr [rbp + 0xd0]
0x0006FB62: mov eax, dword ptr [rbp - 0x60]
0x0006FB65: test eax, eax
0x0006FB67: cmovg ecx, eax
0x0006FB6A: mov dword ptr [rbp + 0xd0], ecx
0x0006FB70: mov ecx, dword ptr [rbp + 0xd4]
0x0006FB76: mov eax, dword ptr [rbp - 0x5c]
0x0006FB79: test eax, eax
0x0006FB7B: cmovg ecx, eax
0x0006FB7E: mov dword ptr [rbp + 0xd4], ecx
0x0006FB84: mov ecx, dword ptr [rbp + 0xdc]
0x0006FB8A: mov eax, dword ptr [rbp - 0x54]
0x0006FB8D: test eax, eax
0x0006FB8F: cmovns ecx, eax
0x0006FB92: mov dword ptr [rbp + 0xdc], ecx
0x0006FB98: mov ecx, dword ptr [rbp + 0xe0]
0x0006FB9E: mov eax, dword ptr [rbp - 0x50]
0x0006FBA1: test eax, eax
0x0006FBA3: cmovns ecx, eax
0x0006FBA6: mov dword ptr [rbp + 0xe0], ecx
0x0006FBAC: mov eax, dword ptr [rbp - 0x38]
0x0006FBAF: mov dword ptr [rbp + 0xf8], eax
0x0006FBB5: mov ecx, dword ptr [rbp + 0x108]
0x0006FBBB: mov eax, dword ptr [rbp - 0x28]
0x0006FBBE: test eax, eax
0x0006FBC0: cmovg ecx, eax
0x0006FBC3: mov dword ptr [rbp + 0x108], ecx
0x0006FBC9: mov ecx, dword ptr [rbp + 0xe8]
0x0006FBCF: mov eax, dword ptr [rbp - 0x48]
0x0006FBD2: test eax, eax
0x0006FBD4: cmovg ecx, eax
0x0006FBD7: mov dword ptr [rbp + 0xe8], ecx
0x0006FBDD: mov ecx, dword ptr [rbp + 0xec]
0x0006FBE3: mov eax, dword ptr [rbp - 0x44]
0x0006FBE6: test eax, eax
0x0006FBE8: cmovne ecx, eax
0x0006FBEB: mov dword ptr [rbp + 0xec], ecx
0x0006FBF1: mov ecx, dword ptr [rbp + 0xfc]
0x0006FBF7: mov eax, dword ptr [rbp - 0x34]
0x0006FBFA: test eax, eax
0x0006FBFC: cmovg ecx, eax
0x0006FBFF: mov dword ptr [rbp + 0xfc], ecx
0x0006FC05: mov ecx, dword ptr [rbp + 0xf0]
0x0006FC0B: mov eax, dword ptr [rbp - 0x40]
0x0006FC0E: test eax, eax
0x0006FC10: cmovg ecx, eax
0x0006FC13: mov dword ptr [rbp + 0xf0], ecx
0x0006FC19: mov ecx, dword ptr [rbp + 0xf4]
0x0006FC1F: mov eax, dword ptr [rbp - 0x3c]
0x0006FC22: test eax, eax
0x0006FC24: cmovne ecx, eax
0x0006FC27: mov dword ptr [rbp + 0xf4], ecx
0x0006FC2D: mov ecx, dword ptr [rbp + 0x104]
0x0006FC33: mov eax, dword ptr [rbp - 0x2c]
0x0006FC36: test eax, eax
0x0006FC38: cmovg ecx, eax
0x0006FC3B: mov dword ptr [rbp + 0x104], ecx
0x0006FC41: mov eax, dword ptr [rbp]
0x0006FC44: mov dword ptr [rbp + 0x130], eax
0x0006FC4A: mov eax, dword ptr [rbp + 0xc]
0x0006FC4D: mov dword ptr [rbp + 0x13c], eax
0x0006FC53: mov eax, dword ptr [rbp + 0x10]
0x0006FC56: mov dword ptr [rbp + 0x140], eax
0x0006FC5C: movsd xmm0, qword ptr [rbp + 0x14]
0x0006FC61: movsd qword ptr [rbp + 0x144], xmm0
0x0006FC69: mov eax, dword ptr [rbp + 0x1c]
0x0006FC6C: mov dword ptr [rbp + 0x14c], eax
0x0006FC72: shr rdx, 0x20
0x0006FC76: mov dword ptr [rbp + 0x94], edx
0x0006FC7C: mov edx, dword ptr [rbp + 0x10c]
0x0006FC82: mov eax, dword ptr [rbp - 0x24]
0x0006FC85: test eax, eax
0x0006FC87: cmovg edx, eax
0x0006FC8A: mov dword ptr [rbp + 0x10c], edx
0x0006FC90: mov edx, dword ptr [rbp + 0x110]
0x0006FC96: mov eax, dword ptr [rbp - 0x20]
0x0006FC99: test eax, eax
0x0006FC9B: cmovg edx, eax
0x0006FC9E: mov dword ptr [rbp + 0x110], edx
0x0006FCA4: mov edx, dword ptr [rbp + 0x114]
0x0006FCAA: mov eax, dword ptr [rbp - 0x1c]
0x0006FCAD: test eax, eax
0x0006FCAF: cmovg edx, eax
0x0006FCB2: mov dword ptr [rbp + 0x114], edx
0x0006FCB8: lea rdx, [rbp + 0x90]
0x0006FCBF: mov rcx, r15
0x0006FCC2: call 0x1401362d0
0x0006FCC7: cmp qword ptr [r13 + 0x12a8], 0
0x0006FCCF: je 0x14006fce5
0x0006FCD1: mov r8d, dword ptr [rsp + 0x70]
0x0006FCD6: mov edx, r14d
0x0006FCD9: lea rcx, [r13 + 0x300]
0x0006FCE0: call 0x14013f7e0
0x0006FCE5: inc r14d
0x0006FCE8: test rsi, rsi
0x0006FCEB: je 0x14006fd18
0x0006FCED: or eax, 0xffffffff
0x0006FCF0: lock xadd dword ptr [rsi + 8], eax
0x0006FCF5: cmp eax, 1
0x0006FCF8: jne 0x14006fd18
0x0006FCFA: mov rax, qword ptr [rsi]
0x0006FCFD: mov rcx, rsi
0x0006FD00: call qword ptr [rax]
0x0006FD02: or eax, 0xffffffff
0x0006FD05: lock xadd dword ptr [rsi + 0xc], eax
0x0006FD0A: cmp eax, 1
0x0006FD0D: jne 0x14006fd18
0x0006FD0F: mov rax, qword ptr [rsi]
0x0006FD12: mov rcx, rsi
0x0006FD15: call qword ptr [rax + 8]
0x0006FD18: add rbx, 0x10
0x0006FD1C: cmp rbx, rdi
0x0006FD1F: jne 0x14006fa20
0x0006FD25: xor esi, esi
0x0006FD27: lea rdx, [rbp + 0x190]
0x0006FD2E: mov rcx, r13
0x0006FD31: call 0x140127270
0x0006FD36: mov rcx, qword ptr [r13 + 0x15a0]
0x0006FD3D: test rcx, rcx
0x0006FD40: je 0x14006fd49
0x0006FD42: xor edx, edx
0x0006FD44: call 0x1400594c0
0x0006FD49: mov eax, esi
0x0006FD4B: xchg byte ptr [r13 + 0x16a0], al
0x0006FD52: mov dword ptr [rbp + 0x58], 0x24
0x0006FD59: mov dword ptr [rbp + 0x5c], 0x4a
0x0006FD60: mov eax, dword ptr [rbp + 0x5c]
0x0006FD63: xor eax, 0x67
0x0006FD66: mov byte ptr [rbp + 0x60], al
0x0006FD69: movsx ecx, byte ptr [rbp + 0x60]
0x0006FD6D: xor ecx, 0x4b
0x0006FD70: mov byte ptr [rbp + 0x61], cl
0x0006FD73: movsx ecx, byte ptr [rbp + 0x61]
0x0006FD77: xor ecx, 0x4a
0x0006FD7A: mov byte ptr [rbp + 0x62], cl
0x0006FD7D: movsx ecx, byte ptr [rbp + 0x62]
0x0006FD81: xor ecx, 0x42
0x0006FD84: mov byte ptr [rbp + 0x63], cl
0x0006FD87: movsx ecx, byte ptr [rbp + 0x63]
0x0006FD8B: xor ecx, 0x4d
0x0006FD8E: mov byte ptr [rbp + 0x64], cl
0x0006FD91: movsx ecx, byte ptr [rbp + 0x64]
0x0006FD95: xor ecx, 0x43
0x0006FD98: mov byte ptr [rbp + 0x65], cl
0x0006FD9B: movsx ecx, byte ptr [rbp + 0x65]
0x0006FD9F: xor ecx, 4
0x0006FDA2: mov byte ptr [rbp + 0x66], cl
0x0006FDA5: movsx ecx, byte ptr [rbp + 0x66]
0x0006FDA9: xor ecx, 0x42
0x0006FDAC: mov byte ptr [rbp + 0x67], cl
0x0006FDAF: movsx ecx, byte ptr [rbp + 0x67]
0x0006FDB3: xor ecx, 0x4d
0x0006FDB6: mov byte ptr [rbp + 0x68], cl
0x0006FDB9: movsx ecx, byte ptr [rbp + 0x68]
0x0006FDBD: xor ecx, 0x48
0x0006FDC0: mov byte ptr [rbp + 0x69], cl
0x0006FDC3: movsx ecx, byte ptr [rbp + 0x69]
0x0006FDC7: xor ecx, 0x41
0x0006FDCA: mov byte ptr [rbp + 0x6a], cl
0x0006FDCD: movsx ecx, byte ptr [rbp + 0x6a]
0x0006FDD1: xor ecx, 4
0x0006FDD4: mov byte ptr [rbp + 0x6b], cl
0x0006FDD7: movsx ecx, byte ptr [rbp + 0x6b]
0x0006FDDB: xor ecx, 0x57
0x0006FDDE: mov byte ptr [rbp + 0x6c], cl
0x0006FDE1: movsx ecx, byte ptr [rbp + 0x6c]
0x0006FDE5: xor ecx, 0x41
0x0006FDE8: mov byte ptr [rbp + 0x6d], cl
0x0006FDEB: movsx ecx, byte ptr [rbp + 0x6d]
0x0006FDEF: xor ecx, 0x50
0x0006FDF2: mov byte ptr [rbp + 0x6e], cl
0x0006FDF5: movsx ecx, byte ptr [rbp + 0x6e]
0x0006FDF9: xor ecx, 0x50
0x0006FDFC: mov byte ptr [rbp + 0x6f], cl
0x0006FDFF: movsx ecx, byte ptr [rbp + 0x6f]
0x0006FE03: xor ecx, 0x4d
0x0006FE06: mov byte ptr [rbp + 0x70], cl
0x0006FE09: movsx ecx, byte ptr [rbp + 0x70]
0x0006FE0D: xor ecx, 0x4a
0x0006FE10: mov byte ptr [rbp + 0x71], cl
0x0006FE13: movsx ecx, byte ptr [rbp + 0x71]
0x0006FE17: xor ecx, 0x43
0x0006FE1A: mov byte ptr [rbp + 0x72], cl
0x0006FE1D: movsx ecx, byte ptr [rbp + 0x72]
0x0006FE21: xor ecx, 0x57
0x0006FE24: mov byte ptr [rbp + 0x73], cl
0x0006FE27: movsx ecx, byte ptr [rbp + 0x73]
0x0006FE2B: xor ecx, 4
0x0006FE2E: mov byte ptr [rbp + 0x74], cl
0x0006FE31: movsx ecx, byte ptr [rbp + 0x74]
0x0006FE35: xor ecx, 0x56
0x0006FE38: mov byte ptr [rbp + 0x75], cl
0x0006FE3B: movsx ecx, byte ptr [rbp + 0x75]
0x0006FE3F: xor ecx, 0x41
0x0006FE42: mov byte ptr [rbp + 0x76], cl
0x0006FE45: movsx ecx, byte ptr [rbp + 0x76]
0x0006FE49: xor ecx, 0x48
0x0006FE4C: mov byte ptr [rbp + 0x77], cl
0x0006FE4F: movsx ecx, byte ptr [rbp + 0x77]
0x0006FE53: xor ecx, 0x4b
0x0006FE56: mov byte ptr [rbp + 0x78], cl
0x0006FE59: movsx ecx, byte ptr [rbp + 0x78]
0x0006FE5D: xor ecx, 0x45
0x0006FE60: mov byte ptr [rbp + 0x79], cl
0x0006FE63: movsx ecx, byte ptr [rbp + 0x79]
0x0006FE67: xor ecx, 0x40
0x0006FE6A: mov byte ptr [rbp + 0x7a], cl
0x0006FE6D: movsx ecx, byte ptr [rbp + 0x7a]
0x0006FE71: xor ecx, 0x41
0x0006FE74: mov byte ptr [rbp + 0x7b], cl
0x0006FE77: movsx ecx, byte ptr [rbp + 0x7b]
0x0006FE7B: xor ecx, 0x40
0x0006FE7E: mov byte ptr [rbp + 0x7c], cl
0x0006FE81: movsx ecx, byte ptr [rbp + 0x7c]
0x0006FE85: xor ecx, 4
0x0006FE88: mov byte ptr [rbp + 0x7d], cl
0x0006FE8B: movsx ecx, byte ptr [rbp + 0x7d]
0x0006FE8F: xor ecx, 0x45
0x0006FE92: mov byte ptr [rbp + 0x7e], cl
0x0006FE95: movsx ecx, byte ptr [rbp + 0x7e]
0x0006FE99: xor ecx, 0x4a
0x0006FE9C: mov byte ptr [rbp + 0x7f], cl
0x0006FE9F: movsx ecx, byte ptr [rbp + 0x7f]
0x0006FEA3: xor ecx, 0x40
0x0006FEA6: mov byte ptr [rbp + 0x80], cl
0x0006FEAC: movsx ecx, byte ptr [rbp + 0x80]
0x0006FEB3: xor ecx, 4
0x0006FEB6: mov byte ptr [rbp + 0x81], cl
0x0006FEBC: movsx ecx, byte ptr [rbp + 0x81]
0x0006FEC3: xor ecx, 0x45
0x0006FEC6: mov byte ptr [rbp + 0x82], cl
0x0006FECC: movsx ecx, byte ptr [rbp + 0x82]
0x0006FED3: xor ecx, 0x54
0x0006FED6: mov byte ptr [rbp + 0x83], cl
0x0006FEDC: movsx ecx, byte ptr [rbp + 0x83]
0x0006FEE3: xor ecx, 0x54
0x0006FEE6: mov byte ptr [rbp + 0x84], cl
0x0006FEEC: movsx ecx, byte ptr [rbp + 0x84]
0x0006FEF3: xor ecx, 0x48
0x0006FEF6: mov byte ptr [rbp + 0x85], cl
0x0006FEFC: movsx ecx, byte ptr [rbp + 0x85]
0x0006FF03: xor ecx, 0x4d
0x0006FF06: mov byte ptr [rbp + 0x86], cl
0x0006FF0C: movsx ecx, byte ptr [rbp + 0x86]
0x0006FF13: xor ecx, 0x41
0x0006FF16: mov byte ptr [rbp + 0x87], cl
0x0006FF1C: movsx ecx, byte ptr [rbp + 0x87]
0x0006FF23: xor ecx, 0x40
0x0006FF26: mov byte ptr [rbp + 0x88], cl
0x0006FF2C: movsx ecx, byte ptr [rbp + 0x88]
0x0006FF33: xor ecx, 0xa
0x0006FF36: mov byte ptr [rbp + 0x89], cl
0x0006FF3C: xor eax, eax
0x0006FF3E: mov byte ptr [rbp + 0x8a], al
0x0006FF44: movzx eax, byte ptr [rbp + 0x60]
0x0006FF48: lea rdx, [rbp + 0x170]
0x0006FF4F: lea rcx, [rbp + 0x58]
0x0006FF53: call 0x1401a56a0
0x0006FF58: nop
0x0006FF59: cmp qword ptr [rax + 0x18], 0x10
0x0006FF5E: jb 0x14006ff63
0x0006FF60: mov rax, qword ptr [rax]
0x0006FF63: mov rcx, rax
0x0006FF66: call 0x140062ff0
0x0006FF6B: nop
0x0006FF6C: mov rax, qword ptr [rbp + 0x188]
0x0006FF73: cmp rax, 0x10
0x0006FF77: jb 0x14006ffc9
0x0006FF79: inc rax
0x0006FF7C: mov rcx, qword ptr [rbp + 0x170]
0x0006FF83: cmp rax, 0x1000
0x0006FF89: jb 0x14006ffc3
0x0006FF8B: test cl, 0x1f
0x0006FF8E: je 0x14006ff96
0x0006FF90: call 0x1403db020
0x0006FF95: int3
0x0006FF96: mov rax, qword ptr [rcx - 8]
0x0006FF9A: cmp rax, rcx
0x0006FF9D: jb 0x14006ffa5
0x0006FF9F: call 0x1403db020
0x0006FFA4: int3
0x0006FFA5: sub rcx, rax
0x0006FFA8: cmp rcx, 8
0x0006FFAC: jae 0x14006ffb4
0x0006FFAE: call 0x1403db020
0x0006FFB3: int3
0x0006FFB4: cmp rcx, 0x27
0x0006FFB8: jbe 0x14006ffc0
0x0006FFBA: call 0x1403db020
0x0006FFBF: int3
0x0006FFC0: mov rcx, rax
0x0006FFC3: call 0x1403b20d4
0x0006FFC8: nop
0x0006FFC9: mov rcx, qword ptr [rsp + 0x28]
0x0006FFCE: test rcx, rcx
0x0006FFD1: je 0x140070011
0x0006FFD3: movzx r9d, byte ptr [rsp + 0x20]
0x0006FFD9: lea r8, [rsp + 0x28]
0x0006FFDE: mov rdx, qword ptr [rsp + 0x30]
0x0006FFE3: call 0x14005fd40
0x0006FFE8: mov r8, qword ptr [rsp + 0x38]
0x0006FFED: mov rdx, qword ptr [rsp + 0x28]
0x0006FFF2: sub r8, rdx
0x0006FFF5: sar r8, 5
0x0006FFF9: lea rcx, [rsp + 0x28]
0x0006FFFE: call 0x14006f460
0x00070003: xorps xmm0, xmm0
0x00070006: movdqu xmmword ptr [rsp + 0x28], xmm0
0x0007000C: mov qword ptr [rsp + 0x38], rsi
0x00070011: lea rcx, [rbp + 0x190]
0x00070018: call 0x140067d70
0x0007001D: nop
0x0007001E: mov rcx, qword ptr [rsp + 0x40]
0x00070023: test rcx, rcx
0x00070026: je 0x1400700b0
0x0007002C: movzx r9d, byte ptr [rsp + 0x20]
0x00070032: lea r8, [rsp + 0x40]
0x00070037: mov rdx, qword ptr [rsp + 0x48]
0x0007003C: call 0x14005fd40
0x00070041: mov rax, qword ptr [rsp + 0x50]
0x00070046: mov rcx, qword ptr [rsp + 0x40]
0x0007004B: sub rax, rcx
0x0007004E: sar rax, 5
0x00070052: movabs rdx, 0x7ffffffffffffff
0x0007005C: cmp rax, rdx
0x0007005F: jbe 0x140070067
0x00070061: call 0x1403db020
0x00070066: int3
0x00070067: shl rax, 5
0x0007006B: cmp rax, 0x1000
0x00070071: jb 0x1400700ab
0x00070073: test cl, 0x1f
0x00070076: je 0x14007007e
0x00070078: call 0x1403db020
0x0007007D: int3
0x0007007E: mov rax, qword ptr [rcx - 8]
0x00070082: cmp rax, rcx
0x00070085: jb 0x14007008d
0x00070087: call 0x1403db020
0x0007008C: int3
0x0007008D: sub rcx, rax
0x00070090: cmp rcx, 8
0x00070094: jae 0x14007009c
0x00070096: call 0x1403db020
0x0007009B: int3
0x0007009C: cmp rcx, 0x27
0x000700A0: jbe 0x1400700a8
0x000700A2: call 0x1403db020
0x000700A7: int3
0x000700A8: mov rcx, rax
0x000700AB: call 0x1403b20d4
0x000700B0: mov rcx, qword ptr [rbp + 0x490]
0x000700B7: xor rcx, rsp
0x000700BA: call 0x1403b24c0
0x000700BF: lea r11, [rsp + 0x5a0]
0x000700C7: mov rbx, qword ptr [r11 + 0x38]
0x000700CB: mov rsi, qword ptr [r11 + 0x40]
0x000700CF: mov rdi, qword ptr [r11 + 0x48]
0x000700D3: mov rsp, r11
0x000700D6: pop r15
0x000700D8: pop r14
0x000700DA: pop r13
0x000700DC: pop r12
0x000700DE: pop rbp
0x000700DF: ret
```

## r15-affecting instructions before 0x6FCC2

- `0x0006F94A: push r15`
- `0x0006FA24: mov r15, qword ptr [rbx]`
- `0x0006FA34: mov qword ptr [rbp + 0x48], r15`
- `0x0006FA3F: mov rcx, r15`
- `0x0006FCBF: mov rcx, r15`

## Direct calls before handoff

| RVA | target/form |
|---|---|
| `0x0006F98C` | `RVA 0x0013A320` |
| `0x0006F9A9` | `RVA 0x000E32C0` |
| `0x0006F9BD` | `RVA 0x000E00C0` |
| `0x0006F9E2` | `RVA 0x000EF860` |
| `0x0006F9F6` | `RVA 0x000E2100` |
| `0x0006FA05` | `RVA 0x0013C5A0` |
| `0x0006FA42` | `RVA 0x00084A60` |
| `0x0006FA51` | `RVA 0x000E3F60` |
| `0x0006FCC2` | `RVA 0x001362D0` |