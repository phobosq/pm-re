# Type2 ctor config-record provenance

PDATA `0x001CDCC0..0x001CDDAC`. Entry R9 is original 0xD8 config record.

Aliases observed: `r9`

## Config-pointer memory accesses

| RVA | disp | label | instruction |
|---|---:|---|---|

## Calls

| RVA | target |
|---|---|
| `0x001CDCEB` | `0x0012F250` |
| `0x001CDD07` | `0x00391A94` |
| `0x001CDD53` | `0x003B2098` |
| `0x001CDD6E` | `0x001D4A80` |
| `0x001CDD91` | `qword ptr [rax]` |

## Full body

```asm
0x001CDCC0: mov qword ptr [rsp + 8], rcx
0x001CDCC5: push rdi
0x001CDCC6: sub rsp, 0x30
0x001CDCCA: mov qword ptr [rsp + 0x20], 0xfffffffffffffffe
0x001CDCD3: mov qword ptr [rsp + 0x48], rbx
0x001CDCD8: mov qword ptr [rsp + 0x50], rbp
0x001CDCDD: mov qword ptr [rsp + 0x58], rsi
0x001CDCE2: mov rsi, r9
0x001CDCE5: mov ebp, r8d
0x001CDCE8: mov rbx, rcx
0x001CDCEB: call 0x14012f250
0x001CDCF0: nop
0x001CDCF1: lea rax, [rip + 0x2ef860]
0x001CDCF8: mov qword ptr [rbx], rax
0x001CDCFB: lea rcx, [rbx + 0x7c0]
0x001CDD02: mov edx, 2
0x001CDD07: call 0x140391a94
0x001CDD0C: nop
0x001CDD0D: xor eax, eax
0x001CDD0F: mov qword ptr [rbx + 0x810], rax
0x001CDD16: mov qword ptr [rbx + 0x818], rax
0x001CDD1D: mov qword ptr [rbx + 0x820], rax
0x001CDD24: mov qword ptr [rbx + 0x828], rax
0x001CDD2B: mov dword ptr [rbx + 0x830], 0x3e8
0x001CDD35: xor edi, edi
0x001CDD37: mov qword ptr [rbx + 0x838], rdi
0x001CDD3E: mov qword ptr [rbx + 0x840], rdi
0x001CDD45: cmp byte ptr [rip + 0x619b9c], dil
0x001CDD4C: je 0x1401cdd94
0x001CDD4E: mov ecx, 0x3a8
0x001CDD53: call 0x1403b2098
0x001CDD58: mov qword ptr [rsp + 0x28], rax
0x001CDD5D: test rax, rax
0x001CDD60: je 0x1401cdd76
0x001CDD62: lea r8, [rbx + 8]
0x001CDD66: mov r9, rsi
0x001CDD69: mov edx, ebp
0x001CDD6B: mov rcx, rax
0x001CDD6E: call 0x1401d4a80
0x001CDD73: mov rdi, rax
0x001CDD76: mov rcx, qword ptr [rbx + 0x840]
0x001CDD7D: mov qword ptr [rbx + 0x840], rdi
0x001CDD84: test rcx, rcx
0x001CDD87: je 0x1401cdd94
0x001CDD89: mov rax, qword ptr [rcx]
0x001CDD8C: mov edx, 1
0x001CDD91: call qword ptr [rax]
0x001CDD93: nop
0x001CDD94: mov rax, rbx
0x001CDD97: mov rbx, qword ptr [rsp + 0x48]
0x001CDD9C: mov rbp, qword ptr [rsp + 0x50]
0x001CDDA1: mov rsi, qword ptr [rsp + 0x58]
0x001CDDA6: add rsp, 0x30
0x001CDDAA: pop rdi
0x001CDDAB: ret
```