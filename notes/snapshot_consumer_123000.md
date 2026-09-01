# Snapshot consumer 0x123000

PDATA: `0x00123000..0x00124000`

Confirmed caller `0x7FD1D` supplies `R8 = per-GPU 0xD8 snapshot`.

## Timing-field accesses

| RVA | field | instruction |
|---|---|---|
| `0x00123553` | vmr_rxboost `+0xB0` | `mov qword ptr [rsp + 0xb0], rax` |
| `0x00123601` | vmr_rxboost `+0xB0` | `mov rcx, qword ptr [rsp + 0xb0]` |

## Full function

```asm
0x00123000: mov rcx, qword ptr [rcx + 0x2c0]
0x00123007: movups xmm0, xmmword ptr [r8]
0x0012300B: movsxd rax, edx
0x0012300E: imul rdx, rax, 0xd8
0x00123015: add rcx, rdx
0x00123018: movups xmmword ptr [rcx], xmm0
0x0012301B: movups xmm1, xmmword ptr [r8 + 0x10]
0x00123020: movups xmmword ptr [rcx + 0x10], xmm1
0x00123024: movups xmm0, xmmword ptr [r8 + 0x20]
0x00123029: movups xmmword ptr [rcx + 0x20], xmm0
0x0012302D: movups xmm1, xmmword ptr [r8 + 0x30]
0x00123032: movups xmmword ptr [rcx + 0x30], xmm1
0x00123036: movups xmm0, xmmword ptr [r8 + 0x40]
0x0012303B: movups xmmword ptr [rcx + 0x40], xmm0
0x0012303F: movups xmm1, xmmword ptr [r8 + 0x50]
0x00123044: movups xmmword ptr [rcx + 0x50], xmm1
0x00123048: movups xmm0, xmmword ptr [r8 + 0x60]
0x0012304D: movups xmmword ptr [rcx + 0x60], xmm0
0x00123051: sub rcx, -0x80
0x00123055: movups xmm0, xmmword ptr [r8 + 0x70]
0x0012305A: sub r8, -0x80
0x0012305E: movups xmmword ptr [rcx - 0x10], xmm0
0x00123062: movups xmm1, xmmword ptr [r8]
0x00123066: movups xmmword ptr [rcx], xmm1
0x00123069: movups xmm0, xmmword ptr [r8 + 0x10]
0x0012306E: movups xmmword ptr [rcx + 0x10], xmm0
0x00123072: movups xmm1, xmmword ptr [r8 + 0x20]
0x00123077: movups xmmword ptr [rcx + 0x20], xmm1
0x0012307B: movups xmm0, xmmword ptr [r8 + 0x30]
0x00123080: movups xmmword ptr [rcx + 0x30], xmm0
0x00123084: movups xmm1, xmmword ptr [r8 + 0x40]
0x00123089: movups xmmword ptr [rcx + 0x40], xmm1
0x0012308D: mov rax, qword ptr [r8 + 0x50]
0x00123091: mov qword ptr [rcx + 0x50], rax
0x00123095: ret
0x00123096: int3
0x00123097: int3
0x00123098: int3
0x00123099: int3
0x0012309A: int3
0x0012309B: int3
0x0012309C: int3
0x0012309D: int3
0x0012309E: int3
0x0012309F: int3
0x001230A0: push rbx
0x001230A2: sub rsp, 0x270
0x001230A9: mov rax, qword ptr [rip + 0x6b3840]
0x001230B0: xor rax, rsp
0x001230B3: mov qword ptr [rsp + 0x260], rax
0x001230BB: xor r11d, r11d
0x001230BE: mov rbx, rdx
0x001230C1: mov qword ptr [rsp + 0x20], r11
0x001230C6: mov rax, qword ptr [rsp + 0x20]
0x001230CB: mov dword ptr [rsp + 0x2c], r11d
0x001230D0: cmp rax, 0x22d
0x001230D6: jae 0x140123135
0x001230D8: nop dword ptr [rax + rax]
0x001230E0: mov rax, qword ptr [rsp + 0x20]
0x001230E5: test rax, rax
0x001230E8: jne 0x1401230f0
0x001230EA: mov r10d, dword ptr [rcx + 4]
0x001230EE: jmp 0x1401230fb
0x001230F0: mov rax, qword ptr [rsp + 0x20]
0x001230F5: movsx r10d, byte ptr [rax + rcx + 7]
0x001230FB: mov rdx, qword ptr [rsp + 0x20]
0x00123100: mov rax, qword ptr [rsp + 0x20]
0x00123105: movsx r8d, byte ptr [rax + rcx + 8]
0x0012310B: mov eax, dword ptr [rcx]
0x0012310D: add al, dl
0x0012310F: movsx r9d, al
0x00123113: mov rax, qword ptr [rsp + 0x20]
0x00123118: xor r9d, r8d
0x0012311B: xor r9d, r10d
0x0012311E: mov byte ptr [rsp + rax + 0x30], r9b
0x00123123: inc qword ptr [rsp + 0x20]
0x00123128: mov rax, qword ptr [rsp + 0x20]
0x0012312D: cmp rax, 0x22d
0x00123133: jb 0x1401230e0
0x00123135: mov qword ptr [rbx + 0x18], 0xf
0x0012313D: mov edx, 0x22d
0x00123142: mov qword ptr [rbx + 0x10], r11
0x00123146: mov rcx, rbx
0x00123149: mov byte ptr [rbx], r11b
0x0012314C: call 0x140039c30
0x00123151: movzx r9d, byte ptr [rsp + 0x28]
0x00123157: lea r8, [rsp + 0x25d]
0x0012315F: lea rdx, [rsp + 0x30]
0x00123164: mov rcx, rbx
0x00123167: call 0x14002bdb0
0x0012316C: mov rax, rbx
0x0012316F: mov rcx, qword ptr [rsp + 0x260]
0x00123177: xor rcx, rsp
0x0012317A: call 0x1403b24c0
0x0012317F: add rsp, 0x270
0x00123186: pop rbx
0x00123187: ret
0x00123188: int3
0x00123189: int3
0x0012318A: int3
0x0012318B: int3
0x0012318C: int3
0x0012318D: int3
0x0012318E: int3
0x0012318F: int3
0x00123190: push rbx
0x00123192: sub rsp, 0x160
0x00123199: mov rax, qword ptr [rip + 0x6b3750]
0x001231A0: xor rax, rsp
0x001231A3: mov qword ptr [rsp + 0x150], rax
0x001231AB: xor r11d, r11d
0x001231AE: mov rbx, rdx
0x001231B1: mov qword ptr [rsp + 0x20], r11
0x001231B6: mov rax, qword ptr [rsp + 0x20]
0x001231BB: mov dword ptr [rsp + 0x2c], r11d
0x001231C0: cmp rax, 0x11a
0x001231C6: jae 0x140123225
0x001231C8: nop dword ptr [rax + rax]
0x001231D0: mov rax, qword ptr [rsp + 0x20]
0x001231D5: test rax, rax
0x001231D8: jne 0x1401231e0
0x001231DA: mov r10d, dword ptr [rcx + 4]
0x001231DE: jmp 0x1401231eb
0x001231E0: mov rax, qword ptr [rsp + 0x20]
0x001231E5: movsx r10d, byte ptr [rax + rcx + 7]
0x001231EB: mov rdx, qword ptr [rsp + 0x20]
0x001231F0: mov rax, qword ptr [rsp + 0x20]
0x001231F5: movsx r8d, byte ptr [rax + rcx + 8]
0x001231FB: mov eax, dword ptr [rcx]
0x001231FD: add al, dl
0x001231FF: movsx r9d, al
0x00123203: mov rax, qword ptr [rsp + 0x20]
0x00123208: xor r9d, r8d
0x0012320B: xor r9d, r10d
0x0012320E: mov byte ptr [rsp + rax + 0x30], r9b
0x00123213: inc qword ptr [rsp + 0x20]
0x00123218: mov rax, qword ptr [rsp + 0x20]
0x0012321D: cmp rax, 0x11a
0x00123223: jb 0x1401231d0
0x00123225: mov qword ptr [rbx + 0x18], 0xf
0x0012322D: mov edx, 0x11a
0x00123232: mov qword ptr [rbx + 0x10], r11
0x00123236: mov rcx, rbx
0x00123239: mov byte ptr [rbx], r11b
0x0012323C: call 0x140039c30
0x00123241: movzx r9d, byte ptr [rsp + 0x28]
0x00123247: lea r8, [rsp + 0x14a]
0x0012324F: lea rdx, [rsp + 0x30]
0x00123254: mov rcx, rbx
0x00123257: call 0x14002bdb0
0x0012325C: mov rax, rbx
0x0012325F: mov rcx, qword ptr [rsp + 0x150]
0x00123267: xor rcx, rsp
0x0012326A: call 0x1403b24c0
0x0012326F: add rsp, 0x160
0x00123276: pop rbx
0x00123277: ret
0x00123278: int3
0x00123279: int3
0x0012327A: int3
0x0012327B: int3
0x0012327C: int3
0x0012327D: int3
0x0012327E: int3
0x0012327F: int3
0x00123280: push rbx
0x00123282: sub rsp, 0xf0
0x00123289: mov rax, qword ptr [rip + 0x6b3660]
0x00123290: xor rax, rsp
0x00123293: mov qword ptr [rsp + 0xe0], rax
0x0012329B: xor r11d, r11d
0x0012329E: mov rbx, rdx
0x001232A1: mov qword ptr [rsp + 0x20], r11
0x001232A6: mov rax, qword ptr [rsp + 0x20]
0x001232AB: mov dword ptr [rsp + 0x2c], r11d
0x001232B0: cmp rax, 0xac
0x001232B6: jae 0x140123315
0x001232B8: nop dword ptr [rax + rax]
0x001232C0: mov rax, qword ptr [rsp + 0x20]
0x001232C5: test rax, rax
0x001232C8: jne 0x1401232d0
0x001232CA: mov r10d, dword ptr [rcx + 4]
0x001232CE: jmp 0x1401232db
0x001232D0: mov rax, qword ptr [rsp + 0x20]
0x001232D5: movsx r10d, byte ptr [rax + rcx + 7]
0x001232DB: mov rdx, qword ptr [rsp + 0x20]
0x001232E0: mov rax, qword ptr [rsp + 0x20]
0x001232E5: movsx r8d, byte ptr [rax + rcx + 8]
0x001232EB: mov eax, dword ptr [rcx]
0x001232ED: add al, dl
0x001232EF: movsx r9d, al
0x001232F3: mov rax, qword ptr [rsp + 0x20]
0x001232F8: xor r9d, r8d
0x001232FB: xor r9d, r10d
0x001232FE: mov byte ptr [rsp + rax + 0x30], r9b
0x00123303: inc qword ptr [rsp + 0x20]
0x00123308: mov rax, qword ptr [rsp + 0x20]
0x0012330D: cmp rax, 0xac
0x00123313: jb 0x1401232c0
0x00123315: mov qword ptr [rbx + 0x18], 0xf
0x0012331D: mov edx, 0xac
0x00123322: mov qword ptr [rbx + 0x10], r11
0x00123326: mov rcx, rbx
0x00123329: mov byte ptr [rbx], r11b
0x0012332C: call 0x140039c30
0x00123331: movzx r9d, byte ptr [rsp + 0x28]
0x00123337: lea r8, [rsp + 0xdc]
0x0012333F: lea rdx, [rsp + 0x30]
0x00123344: mov rcx, rbx
0x00123347: call 0x14002bdb0
0x0012334C: mov rax, rbx
0x0012334F: mov rcx, qword ptr [rsp + 0xe0]
0x00123357: xor rcx, rsp
0x0012335A: call 0x1403b24c0
0x0012335F: add rsp, 0xf0
0x00123366: pop rbx
0x00123367: ret
0x00123368: int3
0x00123369: int3
0x0012336A: int3
0x0012336B: int3
0x0012336C: int3
0x0012336D: int3
0x0012336E: int3
0x0012336F: int3
0x00123370: push rbx
0x00123372: sub rsp, 0x130
0x00123379: mov rax, qword ptr [rip + 0x6b3570]
0x00123380: xor rax, rsp
0x00123383: mov qword ptr [rsp + 0x120], rax
0x0012338B: xor r11d, r11d
0x0012338E: mov rbx, rdx
0x00123391: mov qword ptr [rsp + 0x20], r11
0x00123396: mov rax, qword ptr [rsp + 0x20]
0x0012339B: mov dword ptr [rsp + 0x2c], r11d
0x001233A0: cmp rax, 0xf0
0x001233A6: jae 0x140123405
0x001233A8: nop dword ptr [rax + rax]
0x001233B0: mov rax, qword ptr [rsp + 0x20]
0x001233B5: test rax, rax
0x001233B8: jne 0x1401233c0
0x001233BA: mov r10d, dword ptr [rcx + 4]
0x001233BE: jmp 0x1401233cb
0x001233C0: mov rax, qword ptr [rsp + 0x20]
0x001233C5: movsx r10d, byte ptr [rax + rcx + 7]
0x001233CB: mov rdx, qword ptr [rsp + 0x20]
0x001233D0: mov rax, qword ptr [rsp + 0x20]
0x001233D5: movsx r8d, byte ptr [rax + rcx + 8]
0x001233DB: mov eax, dword ptr [rcx]
0x001233DD: add al, dl
0x001233DF: movsx r9d, al
0x001233E3: mov rax, qword ptr [rsp + 0x20]
0x001233E8: xor r9d, r8d
0x001233EB: xor r9d, r10d
0x001233EE: mov byte ptr [rsp + rax + 0x30], r9b
0x001233F3: inc qword ptr [rsp + 0x20]
0x001233F8: mov rax, qword ptr [rsp + 0x20]
0x001233FD: cmp rax, 0xf0
0x00123403: jb 0x1401233b0
0x00123405: mov qword ptr [rbx + 0x18], 0xf
0x0012340D: mov edx, 0xf0
0x00123412: mov qword ptr [rbx + 0x10], r11
0x00123416: mov rcx, rbx
0x00123419: mov byte ptr [rbx], r11b
0x0012341C: call 0x140039c30
0x00123421: movzx r9d, byte ptr [rsp + 0x28]
0x00123427: lea r8, [rsp + 0x120]
0x0012342F: lea rdx, [rsp + 0x30]
0x00123434: mov rcx, rbx
0x00123437: call 0x14002bdb0
0x0012343C: mov rax, rbx
0x0012343F: mov rcx, qword ptr [rsp + 0x120]
0x00123447: xor rcx, rsp
0x0012344A: call 0x1403b24c0
0x0012344F: add rsp, 0x130
0x00123456: pop rbx
0x00123457: ret
0x00123458: int3
0x00123459: int3
0x0012345A: int3
0x0012345B: int3
0x0012345C: int3
0x0012345D: int3
0x0012345E: int3
0x0012345F: int3
0x00123460: push rbx
0x00123462: sub rsp, 0x90
0x00123469: mov rax, qword ptr [rip + 0x6b3480]
0x00123470: xor rax, rsp
0x00123473: mov qword ptr [rsp + 0x80], rax
0x0012347B: xor r10d, r10d
0x0012347E: mov rbx, rdx
0x00123481: mov qword ptr [rsp + 0x20], r10
0x00123486: mov rax, qword ptr [rsp + 0x20]
0x0012348B: mov dword ptr [rsp + 0x2c], r10d
0x00123490: cmp rax, 0x4e
0x00123494: jae 0x1401234e7
0x00123496: mov rax, qword ptr [rsp + 0x20]
0x0012349B: test rax, rax
0x0012349E: jne 0x1401234a6
0x001234A0: mov r9d, dword ptr [rcx + 4]
0x001234A4: jmp 0x1401234b1
0x001234A6: mov rax, qword ptr [rsp + 0x20]
0x001234AB: movsx r9d, byte ptr [rax + rcx + 7]
0x001234B1: mov rdx, qword ptr [rsp + 0x20]
0x001234B6: mov rax, qword ptr [rsp + 0x20]
0x001234BB: movsx r8d, byte ptr [rax + rcx + 8]
0x001234C1: mov eax, dword ptr [rcx]
0x001234C3: add al, dl
0x001234C5: movsx edx, al
0x001234C8: mov rax, qword ptr [rsp + 0x20]
0x001234CD: xor edx, r8d
0x001234D0: xor edx, r9d
0x001234D3: mov byte ptr [rsp + rax + 0x30], dl
0x001234D7: inc qword ptr [rsp + 0x20]
0x001234DC: mov rax, qword ptr [rsp + 0x20]
0x001234E1: cmp rax, 0x4e
0x001234E5: jb 0x140123496
0x001234E7: mov qword ptr [rbx + 0x18], 0xf
0x001234EF: mov edx, 0x4e
0x001234F4: mov qword ptr [rbx + 0x10], r10
0x001234F8: mov rcx, rbx
0x001234FB: mov byte ptr [rbx], r10b
0x001234FE: call 0x140039c30
0x00123503: movzx r9d, byte ptr [rsp + 0x28]
0x00123509: lea r8, [rsp + 0x7e]
0x0012350E: lea rdx, [rsp + 0x30]
0x00123513: mov rcx, rbx
0x00123516: call 0x14002bdb0
0x0012351B: mov rax, rbx
0x0012351E: mov rcx, qword ptr [rsp + 0x80]
0x00123526: xor rcx, rsp
0x00123529: call 0x1403b24c0
0x0012352E: add rsp, 0x90
0x00123535: pop rbx
0x00123536: ret
0x00123537: int3
0x00123538: int3
0x00123539: int3
0x0012353A: int3
0x0012353B: int3
0x0012353C: int3
0x0012353D: int3
0x0012353E: int3
0x0012353F: int3
0x00123540: push rbx
0x00123542: sub rsp, 0xc0
0x00123549: mov rax, qword ptr [rip + 0x6b33a0]
0x00123550: xor rax, rsp
0x00123553: mov qword ptr [rsp + 0xb0], rax
0x0012355B: xor r10d, r10d
0x0012355E: mov rbx, rdx
0x00123561: mov qword ptr [rsp + 0x20], r10
0x00123566: mov rax, qword ptr [rsp + 0x20]
0x0012356B: mov dword ptr [rsp + 0x2c], r10d
0x00123570: cmp rax, 0x79
0x00123574: jae 0x1401235c7
0x00123576: mov rax, qword ptr [rsp + 0x20]
0x0012357B: test rax, rax
0x0012357E: jne 0x140123586
0x00123580: mov r9d, dword ptr [rcx + 4]
0x00123584: jmp 0x140123591
0x00123586: mov rax, qword ptr [rsp + 0x20]
0x0012358B: movsx r9d, byte ptr [rax + rcx + 7]
0x00123591: mov rdx, qword ptr [rsp + 0x20]
0x00123596: mov rax, qword ptr [rsp + 0x20]
0x0012359B: movsx r8d, byte ptr [rax + rcx + 8]
0x001235A1: mov eax, dword ptr [rcx]
0x001235A3: add al, dl
0x001235A5: movsx edx, al
0x001235A8: mov rax, qword ptr [rsp + 0x20]
0x001235AD: xor edx, r8d
0x001235B0: xor edx, r9d
0x001235B3: mov byte ptr [rsp + rax + 0x30], dl
0x001235B7: inc qword ptr [rsp + 0x20]
0x001235BC: mov rax, qword ptr [rsp + 0x20]
0x001235C1: cmp rax, 0x79
0x001235C5: jb 0x140123576
0x001235C7: mov qword ptr [rbx + 0x18], 0xf
0x001235CF: mov edx, 0x79
0x001235D4: mov qword ptr [rbx + 0x10], r10
0x001235D8: mov rcx, rbx
0x001235DB: mov byte ptr [rbx], r10b
0x001235DE: call 0x140039c30
0x001235E3: movzx r9d, byte ptr [rsp + 0x28]
0x001235E9: lea r8, [rsp + 0xa9]
0x001235F1: lea rdx, [rsp + 0x30]
0x001235F6: mov rcx, rbx
0x001235F9: call 0x14002bdb0
0x001235FE: mov rax, rbx
0x00123601: mov rcx, qword ptr [rsp + 0xb0]
0x00123609: xor rcx, rsp
0x0012360C: call 0x1403b24c0
0x00123611: add rsp, 0xc0
0x00123618: pop rbx
0x00123619: ret
0x0012361A: int3
0x0012361B: int3
0x0012361C: int3
0x0012361D: int3
0x0012361E: int3
0x0012361F: int3
0x00123620: push rbx
0x00123622: sub rsp, 0x1b0
0x00123629: mov rax, qword ptr [rip + 0x6b32c0]
0x00123630: xor rax, rsp
0x00123633: mov qword ptr [rsp + 0x1a0], rax
0x0012363B: xor r11d, r11d
0x0012363E: mov rbx, rdx
0x00123641: mov qword ptr [rsp + 0x20], r11
0x00123646: mov rax, qword ptr [rsp + 0x20]
0x0012364B: mov dword ptr [rsp + 0x2c], r11d
0x00123650: cmp rax, 0x170
0x00123656: jae 0x1401236b5
0x00123658: nop dword ptr [rax + rax]
0x00123660: mov rax, qword ptr [rsp + 0x20]
0x00123665: test rax, rax
0x00123668: jne 0x140123670
0x0012366A: mov r10d, dword ptr [rcx + 4]
0x0012366E: jmp 0x14012367b
0x00123670: mov rax, qword ptr [rsp + 0x20]
0x00123675: movsx r10d, byte ptr [rax + rcx + 7]
0x0012367B: mov rdx, qword ptr [rsp + 0x20]
0x00123680: mov rax, qword ptr [rsp + 0x20]
0x00123685: movsx r8d, byte ptr [rax + rcx + 8]
0x0012368B: mov eax, dword ptr [rcx]
0x0012368D: add al, dl
0x0012368F: movsx r9d, al
0x00123693: mov rax, qword ptr [rsp + 0x20]
0x00123698: xor r9d, r8d
0x0012369B: xor r9d, r10d
0x0012369E: mov byte ptr [rsp + rax + 0x30], r9b
0x001236A3: inc qword ptr [rsp + 0x20]
0x001236A8: mov rax, qword ptr [rsp + 0x20]
0x001236AD: cmp rax, 0x170
0x001236B3: jb 0x140123660
0x001236B5: mov qword ptr [rbx + 0x18], 0xf
0x001236BD: mov edx, 0x170
0x001236C2: mov qword ptr [rbx + 0x10], r11
0x001236C6: mov rcx, rbx
0x001236C9: mov byte ptr [rbx], r11b
0x001236CC: call 0x140039c30
0x001236D1: movzx r9d, byte ptr [rsp + 0x28]
0x001236D7: lea r8, [rsp + 0x1a0]
0x001236DF: lea rdx, [rsp + 0x30]
0x001236E4: mov rcx, rbx
0x001236E7: call 0x14002bdb0
0x001236EC: mov rax, rbx
0x001236EF: mov rcx, qword ptr [rsp + 0x1a0]
0x001236F7: xor rcx, rsp
0x001236FA: call 0x1403b24c0
0x001236FF: add rsp, 0x1b0
0x00123706: pop rbx
0x00123707: ret
0x00123708: int3
0x00123709: int3
0x0012370A: int3
0x0012370B: int3
0x0012370C: int3
0x0012370D: int3
0x0012370E: int3
0x0012370F: int3
0x00123710: push rbx
0x00123712: sub rsp, 0x150
0x00123719: mov rax, qword ptr [rip + 0x6b31d0]
0x00123720: xor rax, rsp
0x00123723: mov qword ptr [rsp + 0x140], rax
0x0012372B: xor r11d, r11d
0x0012372E: mov rbx, rdx
0x00123731: mov qword ptr [rsp + 0x20], r11
0x00123736: mov rax, qword ptr [rsp + 0x20]
0x0012373B: mov dword ptr [rsp + 0x2c], r11d
0x00123740: cmp rax, 0x10e
0x00123746: jae 0x1401237a5
0x00123748: nop dword ptr [rax + rax]
0x00123750: mov rax, qword ptr [rsp + 0x20]
0x00123755: test rax, rax
0x00123758: jne 0x140123760
0x0012375A: mov r10d, dword ptr [rcx + 4]
0x0012375E: jmp 0x14012376b
0x00123760: mov rax, qword ptr [rsp + 0x20]
0x00123765: movsx r10d, byte ptr [rax + rcx + 7]
0x0012376B: mov rdx, qword ptr [rsp + 0x20]
0x00123770: mov rax, qword ptr [rsp + 0x20]
0x00123775: movsx r8d, byte ptr [rax + rcx + 8]
0x0012377B: mov eax, dword ptr [rcx]
0x0012377D: add al, dl
0x0012377F: movsx r9d, al
0x00123783: mov rax, qword ptr [rsp + 0x20]
0x00123788: xor r9d, r8d
0x0012378B: xor r9d, r10d
0x0012378E: mov byte ptr [rsp + rax + 0x30], r9b
0x00123793: inc qword ptr [rsp + 0x20]
0x00123798: mov rax, qword ptr [rsp + 0x20]
0x0012379D: cmp rax, 0x10e
0x001237A3: jb 0x140123750
0x001237A5: mov qword ptr [rbx + 0x18], 0xf
0x001237AD: mov edx, 0x10e
0x001237B2: mov qword ptr [rbx + 0x10], r11
0x001237B6: mov rcx, rbx
0x001237B9: mov byte ptr [rbx], r11b
0x001237BC: call 0x140039c30
0x001237C1: movzx r9d, byte ptr [rsp + 0x28]
0x001237C7: lea r8, [rsp + 0x13e]
0x001237CF: lea rdx, [rsp + 0x30]
0x001237D4: mov rcx, rbx
0x001237D7: call 0x14002bdb0
0x001237DC: mov rax, rbx
0x001237DF: mov rcx, qword ptr [rsp + 0x140]
0x001237E7: xor rcx, rsp
0x001237EA: call 0x1403b24c0
0x001237EF: add rsp, 0x150
0x001237F6: pop rbx
0x001237F7: ret
0x001237F8: int3
0x001237F9: int3
0x001237FA: int3
0x001237FB: int3
0x001237FC: int3
0x001237FD: int3
0x001237FE: int3
0x001237FF: int3
0x00123800: push rbx
0x00123802: sub rsp, 0xd0
0x00123809: mov rax, qword ptr [rip + 0x6b30e0]
0x00123810: xor rax, rsp
0x00123813: mov qword ptr [rsp + 0xc0], rax
0x0012381B: xor r11d, r11d
0x0012381E: mov rbx, rdx
0x00123821: mov qword ptr [rsp + 0x20], r11
0x00123826: mov rax, qword ptr [rsp + 0x20]
0x0012382B: mov dword ptr [rsp + 0x2c], r11d
0x00123830: cmp rax, 0x81
0x00123836: jae 0x140123895
0x00123838: nop dword ptr [rax + rax]
0x00123840: mov rax, qword ptr [rsp + 0x20]
0x00123845: test rax, rax
0x00123848: jne 0x140123850
0x0012384A: mov r10d, dword ptr [rcx + 4]
0x0012384E: jmp 0x14012385b
0x00123850: mov rax, qword ptr [rsp + 0x20]
0x00123855: movsx r10d, byte ptr [rax + rcx + 7]
0x0012385B: mov rdx, qword ptr [rsp + 0x20]
0x00123860: mov rax, qword ptr [rsp + 0x20]
0x00123865: movsx r8d, byte ptr [rax + rcx + 8]
0x0012386B: mov eax, dword ptr [rcx]
0x0012386D: add al, dl
0x0012386F: movsx r9d, al
0x00123873: mov rax, qword ptr [rsp + 0x20]
0x00123878: xor r9d, r8d
0x0012387B: xor r9d, r10d
0x0012387E: mov byte ptr [rsp + rax + 0x30], r9b
0x00123883: inc qword ptr [rsp + 0x20]
0x00123888: mov rax, qword ptr [rsp + 0x20]
0x0012388D: cmp rax, 0x81
0x00123893: jb 0x140123840
0x00123895: mov qword ptr [rbx + 0x18], 0xf
0x0012389D: mov edx, 0x81
0x001238A2: mov qword ptr [rbx + 0x10], r11
0x001238A6: mov rcx, rbx
0x001238A9: mov byte ptr [rbx], r11b
0x001238AC: call 0x140039c30
0x001238B1: movzx r9d, byte ptr [rsp + 0x28]
0x001238B7: lea r8, [rsp + 0xb1]
0x001238BF: lea rdx, [rsp + 0x30]
0x001238C4: mov rcx, rbx
0x001238C7: call 0x14002bdb0
0x001238CC: mov rax, rbx
0x001238CF: mov rcx, qword ptr [rsp + 0xc0]
0x001238D7: xor rcx, rsp
0x001238DA: call 0x1403b24c0
0x001238DF: add rsp, 0xd0
0x001238E6: pop rbx
0x001238E7: ret
0x001238E8: int3
0x001238E9: int3
0x001238EA: int3
0x001238EB: int3
0x001238EC: int3
0x001238ED: int3
0x001238EE: int3
0x001238EF: int3
0x001238F0: push rbx
0x001238F2: sub rsp, 0xa0
0x001238F9: mov rax, qword ptr [rip + 0x6b2ff0]
0x00123900: xor rax, rsp
0x00123903: mov qword ptr [rsp + 0x90], rax
0x0012390B: xor r10d, r10d
0x0012390E: mov rbx, rdx
0x00123911: mov qword ptr [rsp + 0x20], r10
0x00123916: mov rax, qword ptr [rsp + 0x20]
0x0012391B: mov dword ptr [rsp + 0x2c], r10d
0x00123920: cmp rax, 0x5d
0x00123924: jae 0x140123977
0x00123926: mov rax, qword ptr [rsp + 0x20]
0x0012392B: test rax, rax
0x0012392E: jne 0x140123936
0x00123930: mov r9d, dword ptr [rcx + 4]
0x00123934: jmp 0x140123941
0x00123936: mov rax, qword ptr [rsp + 0x20]
0x0012393B: movsx r9d, byte ptr [rax + rcx + 7]
0x00123941: mov rdx, qword ptr [rsp + 0x20]
0x00123946: mov rax, qword ptr [rsp + 0x20]
0x0012394B: movsx r8d, byte ptr [rax + rcx + 8]
0x00123951: mov eax, dword ptr [rcx]
0x00123953: add al, dl
0x00123955: movsx edx, al
0x00123958: mov rax, qword ptr [rsp + 0x20]
0x0012395D: xor edx, r8d
0x00123960: xor edx, r9d
0x00123963: mov byte ptr [rsp + rax + 0x30], dl
0x00123967: inc qword ptr [rsp + 0x20]
0x0012396C: mov rax, qword ptr [rsp + 0x20]
0x00123971: cmp rax, 0x5d
0x00123975: jb 0x140123926
0x00123977: mov qword ptr [rbx + 0x18], 0xf
0x0012397F: mov edx, 0x5d
0x00123984: mov qword ptr [rbx + 0x10], r10
0x00123988: mov rcx, rbx
0x0012398B: mov byte ptr [rbx], r10b
0x0012398E: call 0x140039c30
0x00123993: movzx r9d, byte ptr [rsp + 0x28]
0x00123999: lea r8, [rsp + 0x8d]
0x001239A1: lea rdx, [rsp + 0x30]
0x001239A6: mov rcx, rbx
0x001239A9: call 0x14002bdb0
0x001239AE: mov rax, rbx
0x001239B1: mov rcx, qword ptr [rsp + 0x90]
0x001239B9: xor rcx, rsp
0x001239BC: call 0x1403b24c0
0x001239C1: add rsp, 0xa0
0x001239C8: pop rbx
0x001239C9: ret
0x001239CA: int3
0x001239CB: int3
0x001239CC: int3
0x001239CD: int3
0x001239CE: int3
0x001239CF: int3
0x001239D0: push rbx
0x001239D2: sub rsp, 0x110
0x001239D9: mov rax, qword ptr [rip + 0x6b2f10]
0x001239E0: xor rax, rsp
0x001239E3: mov qword ptr [rsp + 0x100], rax
0x001239EB: xor r11d, r11d
0x001239EE: mov rbx, rdx
0x001239F1: mov qword ptr [rsp + 0x20], r11
0x001239F6: mov rax, qword ptr [rsp + 0x20]
0x001239FB: mov dword ptr [rsp + 0x2c], r11d
0x00123A00: cmp rax, 0xc9
0x00123A06: jae 0x140123a65
0x00123A08: nop dword ptr [rax + rax]
0x00123A10: mov rax, qword ptr [rsp + 0x20]
0x00123A15: test rax, rax
0x00123A18: jne 0x140123a20
0x00123A1A: mov r10d, dword ptr [rcx + 4]
0x00123A1E: jmp 0x140123a2b
0x00123A20: mov rax, qword ptr [rsp + 0x20]
0x00123A25: movsx r10d, byte ptr [rax + rcx + 7]
0x00123A2B: mov rdx, qword ptr [rsp + 0x20]
0x00123A30: mov rax, qword ptr [rsp + 0x20]
0x00123A35: movsx r8d, byte ptr [rax + rcx + 8]
0x00123A3B: mov eax, dword ptr [rcx]
0x00123A3D: add al, dl
0x00123A3F: movsx r9d, al
0x00123A43: mov rax, qword ptr [rsp + 0x20]
0x00123A48: xor r9d, r8d
0x00123A4B: xor r9d, r10d
0x00123A4E: mov byte ptr [rsp + rax + 0x30], r9b
0x00123A53: inc qword ptr [rsp + 0x20]
0x00123A58: mov rax, qword ptr [rsp + 0x20]
0x00123A5D: cmp rax, 0xc9
0x00123A63: jb 0x140123a10
0x00123A65: mov qword ptr [rbx + 0x18], 0xf
0x00123A6D: mov edx, 0xc9
0x00123A72: mov qword ptr [rbx + 0x10], r11
0x00123A76: mov rcx, rbx
0x00123A79: mov byte ptr [rbx], r11b
0x00123A7C: call 0x140039c30
0x00123A81: movzx r9d, byte ptr [rsp + 0x28]
0x00123A87: lea r8, [rsp + 0xf9]
0x00123A8F: lea rdx, [rsp + 0x30]
0x00123A94: mov rcx, rbx
0x00123A97: call 0x14002bdb0
0x00123A9C: mov rax, rbx
0x00123A9F: mov rcx, qword ptr [rsp + 0x100]
0x00123AA7: xor rcx, rsp
0x00123AAA: call 0x1403b24c0
0x00123AAF: add rsp, 0x110
0x00123AB6: pop rbx
0x00123AB7: ret
0x00123AB8: int3
0x00123AB9: int3
0x00123ABA: int3
0x00123ABB: int3
0x00123ABC: int3
0x00123ABD: int3
0x00123ABE: int3
0x00123ABF: int3
0x00123AC0: push rbx
0x00123AC2: sub rsp, 0x40
0x00123AC6: mov rax, qword ptr [rip + 0x6b2e23]
0x00123ACD: xor rax, rsp
0x00123AD0: mov qword ptr [rsp + 0x38], rax
0x00123AD5: xor r10d, r10d
0x00123AD8: mov rbx, rdx
0x00123ADB: mov qword ptr [rsp + 0x20], r10
0x00123AE0: mov rax, qword ptr [rsp + 0x20]
0x00123AE5: mov dword ptr [rsp + 0x2c], r10d
0x00123AEA: cmp rax, 7
0x00123AEE: jae 0x140123b41
0x00123AF0: mov rax, qword ptr [rsp + 0x20]
0x00123AF5: test rax, rax
0x00123AF8: jne 0x140123b00
0x00123AFA: mov r9d, dword ptr [rcx + 4]
0x00123AFE: jmp 0x140123b0b
0x00123B00: mov rax, qword ptr [rsp + 0x20]
0x00123B05: movsx r9d, byte ptr [rax + rcx + 7]
0x00123B0B: mov rdx, qword ptr [rsp + 0x20]
0x00123B10: mov rax, qword ptr [rsp + 0x20]
0x00123B15: movsx r8d, byte ptr [rax + rcx + 8]
0x00123B1B: mov eax, dword ptr [rcx]
0x00123B1D: add al, dl
0x00123B1F: movsx edx, al
0x00123B22: mov rax, qword ptr [rsp + 0x20]
0x00123B27: xor edx, r8d
0x00123B2A: xor edx, r9d
0x00123B2D: mov byte ptr [rsp + rax + 0x30], dl
0x00123B31: inc qword ptr [rsp + 0x20]
0x00123B36: mov rax, qword ptr [rsp + 0x20]
0x00123B3B: cmp rax, 7
0x00123B3F: jb 0x140123af0
0x00123B41: mov qword ptr [rbx + 0x18], 0xf
0x00123B49: mov edx, 7
0x00123B4E: mov qword ptr [rbx + 0x10], r10
0x00123B52: mov rcx, rbx
0x00123B55: mov byte ptr [rbx], r10b
0x00123B58: call 0x140039c30
0x00123B5D: movzx r9d, byte ptr [rsp + 0x28]
0x00123B63: lea r8, [rsp + 0x37]
0x00123B68: lea rdx, [rsp + 0x30]
0x00123B6D: mov rcx, rbx
0x00123B70: call 0x14002bdb0
0x00123B75: mov rax, rbx
0x00123B78: mov rcx, qword ptr [rsp + 0x38]
0x00123B7D: xor rcx, rsp
0x00123B80: call 0x1403b24c0
0x00123B85: add rsp, 0x40
0x00123B89: pop rbx
0x00123B8A: ret
0x00123B8B: int3
0x00123B8C: int3
0x00123B8D: int3
0x00123B8E: int3
0x00123B8F: int3
0x00123B90: push rbx
0x00123B92: sub rsp, 0x90
0x00123B99: mov rax, qword ptr [rip + 0x6b2d50]
0x00123BA0: xor rax, rsp
0x00123BA3: mov qword ptr [rsp + 0x80], rax
0x00123BAB: xor r10d, r10d
0x00123BAE: mov rbx, rdx
0x00123BB1: mov qword ptr [rsp + 0x20], r10
0x00123BB6: mov rax, qword ptr [rsp + 0x20]
0x00123BBB: mov dword ptr [rsp + 0x2c], r10d
0x00123BC0: cmp rax, 0x44
0x00123BC4: jae 0x140123c17
0x00123BC6: mov rax, qword ptr [rsp + 0x20]
0x00123BCB: test rax, rax
0x00123BCE: jne 0x140123bd6
0x00123BD0: mov r9d, dword ptr [rcx + 4]
0x00123BD4: jmp 0x140123be1
0x00123BD6: mov rax, qword ptr [rsp + 0x20]
0x00123BDB: movsx r9d, byte ptr [rax + rcx + 7]
0x00123BE1: mov rdx, qword ptr [rsp + 0x20]
0x00123BE6: mov rax, qword ptr [rsp + 0x20]
0x00123BEB: movsx r8d, byte ptr [rax + rcx + 8]
0x00123BF1: mov eax, dword ptr [rcx]
0x00123BF3: add al, dl
0x00123BF5: movsx edx, al
0x00123BF8: mov rax, qword ptr [rsp + 0x20]
0x00123BFD: xor edx, r8d
0x00123C00: xor edx, r9d
0x00123C03: mov byte ptr [rsp + rax + 0x30], dl
0x00123C07: inc qword ptr [rsp + 0x20]
0x00123C0C: mov rax, qword ptr [rsp + 0x20]
0x00123C11: cmp rax, 0x44
0x00123C15: jb 0x140123bc6
0x00123C17: mov qword ptr [rbx + 0x18], 0xf
0x00123C1F: mov edx, 0x44
0x00123C24: mov qword ptr [rbx + 0x10], r10
0x00123C28: mov rcx, rbx
0x00123C2B: mov byte ptr [rbx], r10b
0x00123C2E: call 0x140039c30
0x00123C33: movzx r9d, byte ptr [rsp + 0x28]
0x00123C39: lea r8, [rsp + 0x74]
0x00123C3E: lea rdx, [rsp + 0x30]
0x00123C43: mov rcx, rbx
0x00123C46: call 0x14002bdb0
0x00123C4B: mov rax, rbx
0x00123C4E: mov rcx, qword ptr [rsp + 0x80]
0x00123C56: xor rcx, rsp
0x00123C59: call 0x1403b24c0
0x00123C5E: add rsp, 0x90
0x00123C65: pop rbx
0x00123C66: ret
0x00123C67: int3
0x00123C68: int3
0x00123C69: int3
0x00123C6A: int3
0x00123C6B: int3
0x00123C6C: int3
0x00123C6D: int3
0x00123C6E: int3
0x00123C6F: int3
0x00123C70: push rbx
0x00123C72: sub rsp, 0x160
0x00123C79: mov rax, qword ptr [rip + 0x6b2c70]
0x00123C80: xor rax, rsp
0x00123C83: mov qword ptr [rsp + 0x150], rax
0x00123C8B: xor r11d, r11d
0x00123C8E: mov rbx, rdx
0x00123C91: mov qword ptr [rsp + 0x20], r11
0x00123C96: mov rax, qword ptr [rsp + 0x20]
0x00123C9B: mov dword ptr [rsp + 0x2c], r11d
0x00123CA0: cmp rax, 0x118
0x00123CA6: jae 0x140123d05
0x00123CA8: nop dword ptr [rax + rax]
0x00123CB0: mov rax, qword ptr [rsp + 0x20]
0x00123CB5: test rax, rax
0x00123CB8: jne 0x140123cc0
0x00123CBA: mov r10d, dword ptr [rcx + 4]
0x00123CBE: jmp 0x140123ccb
0x00123CC0: mov rax, qword ptr [rsp + 0x20]
0x00123CC5: movsx r10d, byte ptr [rax + rcx + 7]
0x00123CCB: mov rdx, qword ptr [rsp + 0x20]
0x00123CD0: mov rax, qword ptr [rsp + 0x20]
0x00123CD5: movsx r8d, byte ptr [rax + rcx + 8]
0x00123CDB: mov eax, dword ptr [rcx]
0x00123CDD: add al, dl
0x00123CDF: movsx r9d, al
0x00123CE3: mov rax, qword ptr [rsp + 0x20]
0x00123CE8: xor r9d, r8d
0x00123CEB: xor r9d, r10d
0x00123CEE: mov byte ptr [rsp + rax + 0x30], r9b
0x00123CF3: inc qword ptr [rsp + 0x20]
0x00123CF8: mov rax, qword ptr [rsp + 0x20]
0x00123CFD: cmp rax, 0x118
0x00123D03: jb 0x140123cb0
0x00123D05: mov qword ptr [rbx + 0x18], 0xf
0x00123D0D: mov edx, 0x118
0x00123D12: mov qword ptr [rbx + 0x10], r11
0x00123D16: mov rcx, rbx
0x00123D19: mov byte ptr [rbx], r11b
0x00123D1C: call 0x140039c30
0x00123D21: movzx r9d, byte ptr [rsp + 0x28]
0x00123D27: lea r8, [rsp + 0x148]
0x00123D2F: lea rdx, [rsp + 0x30]
0x00123D34: mov rcx, rbx
0x00123D37: call 0x14002bdb0
0x00123D3C: mov rax, rbx
0x00123D3F: mov rcx, qword ptr [rsp + 0x150]
0x00123D47: xor rcx, rsp
0x00123D4A: call 0x1403b24c0
0x00123D4F: add rsp, 0x160
0x00123D56: pop rbx
0x00123D57: ret
0x00123D58: int3
0x00123D59: int3
0x00123D5A: int3
0x00123D5B: int3
0x00123D5C: int3
0x00123D5D: int3
0x00123D5E: int3
0x00123D5F: int3
0x00123D60: push rbx
0x00123D62: sub rsp, 0x40
0x00123D66: mov rax, qword ptr [rip + 0x6b2b83]
0x00123D6D: xor rax, rsp
0x00123D70: mov qword ptr [rsp + 0x38], rax
0x00123D75: xor r10d, r10d
0x00123D78: mov rbx, rdx
0x00123D7B: mov qword ptr [rsp + 0x20], r10
0x00123D80: mov rax, qword ptr [rsp + 0x20]
0x00123D85: mov dword ptr [rsp + 0x2c], r10d
0x00123D8A: cmp rax, 5
0x00123D8E: jae 0x140123de1
0x00123D90: mov rax, qword ptr [rsp + 0x20]
0x00123D95: test rax, rax
0x00123D98: jne 0x140123da0
0x00123D9A: mov r9d, dword ptr [rcx + 4]
0x00123D9E: jmp 0x140123dab
0x00123DA0: mov rax, qword ptr [rsp + 0x20]
0x00123DA5: movsx r9d, byte ptr [rax + rcx + 7]
0x00123DAB: mov rdx, qword ptr [rsp + 0x20]
0x00123DB0: mov rax, qword ptr [rsp + 0x20]
0x00123DB5: movsx r8d, byte ptr [rax + rcx + 8]
0x00123DBB: mov eax, dword ptr [rcx]
0x00123DBD: add al, dl
0x00123DBF: movsx edx, al
0x00123DC2: mov rax, qword ptr [rsp + 0x20]
0x00123DC7: xor edx, r8d
0x00123DCA: xor edx, r9d
0x00123DCD: mov byte ptr [rsp + rax + 0x30], dl
0x00123DD1: inc qword ptr [rsp + 0x20]
0x00123DD6: mov rax, qword ptr [rsp + 0x20]
0x00123DDB: cmp rax, 5
0x00123DDF: jb 0x140123d90
0x00123DE1: mov qword ptr [rbx + 0x18], 0xf
0x00123DE9: mov edx, 5
0x00123DEE: mov qword ptr [rbx + 0x10], r10
0x00123DF2: mov rcx, rbx
0x00123DF5: mov byte ptr [rbx], r10b
0x00123DF8: call 0x140039c30
0x00123DFD: movzx r9d, byte ptr [rsp + 0x28]
0x00123E03: lea r8, [rsp + 0x35]
0x00123E08: lea rdx, [rsp + 0x30]
0x00123E0D: mov rcx, rbx
0x00123E10: call 0x14002bdb0
0x00123E15: mov rax, rbx
0x00123E18: mov rcx, qword ptr [rsp + 0x38]
0x00123E1D: xor rcx, rsp
0x00123E20: call 0x1403b24c0
0x00123E25: add rsp, 0x40
0x00123E29: pop rbx
0x00123E2A: ret
0x00123E2B: int3
0x00123E2C: int3
0x00123E2D: int3
0x00123E2E: int3
0x00123E2F: int3
0x00123E30: push rbx
0x00123E32: sub rsp, 0xf0
0x00123E39: mov rax, qword ptr [rip + 0x6b2ab0]
0x00123E40: xor rax, rsp
0x00123E43: mov qword ptr [rsp + 0xe0], rax
0x00123E4B: xor r11d, r11d
0x00123E4E: mov rbx, rdx
0x00123E51: mov qword ptr [rsp + 0x20], r11
0x00123E56: mov rax, qword ptr [rsp + 0x20]
0x00123E5B: mov dword ptr [rsp + 0x2c], r11d
0x00123E60: cmp rax, 0xa9
0x00123E66: jae 0x140123ec5
0x00123E68: nop dword ptr [rax + rax]
0x00123E70: mov rax, qword ptr [rsp + 0x20]
0x00123E75: test rax, rax
0x00123E78: jne 0x140123e80
0x00123E7A: mov r10d, dword ptr [rcx + 4]
0x00123E7E: jmp 0x140123e8b
0x00123E80: mov rax, qword ptr [rsp + 0x20]
0x00123E85: movsx r10d, byte ptr [rax + rcx + 7]
0x00123E8B: mov rdx, qword ptr [rsp + 0x20]
0x00123E90: mov rax, qword ptr [rsp + 0x20]
0x00123E95: movsx r8d, byte ptr [rax + rcx + 8]
0x00123E9B: mov eax, dword ptr [rcx]
0x00123E9D: add al, dl
0x00123E9F: movsx r9d, al
0x00123EA3: mov rax, qword ptr [rsp + 0x20]
0x00123EA8: xor r9d, r8d
0x00123EAB: xor r9d, r10d
0x00123EAE: mov byte ptr [rsp + rax + 0x30], r9b
0x00123EB3: inc qword ptr [rsp + 0x20]
0x00123EB8: mov rax, qword ptr [rsp + 0x20]
0x00123EBD: cmp rax, 0xa9
0x00123EC3: jb 0x140123e70
0x00123EC5: mov qword ptr [rbx + 0x18], 0xf
0x00123ECD: mov edx, 0xa9
0x00123ED2: mov qword ptr [rbx + 0x10], r11
0x00123ED6: mov rcx, rbx
0x00123ED9: mov byte ptr [rbx], r11b
0x00123EDC: call 0x140039c30
0x00123EE1: movzx r9d, byte ptr [rsp + 0x28]
0x00123EE7: lea r8, [rsp + 0xd9]
0x00123EEF: lea rdx, [rsp + 0x30]
0x00123EF4: mov rcx, rbx
0x00123EF7: call 0x14002bdb0
0x00123EFC: mov rax, rbx
0x00123EFF: mov rcx, qword ptr [rsp + 0xe0]
0x00123F07: xor rcx, rsp
0x00123F0A: call 0x1403b24c0
0x00123F0F: add rsp, 0xf0
0x00123F16: pop rbx
0x00123F17: ret
0x00123F18: int3
0x00123F19: int3
0x00123F1A: int3
0x00123F1B: int3
0x00123F1C: int3
0x00123F1D: int3
0x00123F1E: int3
0x00123F1F: int3
0x00123F20: push rbx
0x00123F22: sub rsp, 0x150
0x00123F29: mov rax, qword ptr [rip + 0x6b29c0]
0x00123F30: xor rax, rsp
0x00123F33: mov qword ptr [rsp + 0x140], rax
0x00123F3B: xor r11d, r11d
0x00123F3E: mov rbx, rdx
0x00123F41: mov qword ptr [rsp + 0x20], r11
0x00123F46: mov rax, qword ptr [rsp + 0x20]
0x00123F4B: mov dword ptr [rsp + 0x2c], r11d
0x00123F50: cmp rax, 0x107
0x00123F56: jae 0x140123fb5
0x00123F58: nop dword ptr [rax + rax]
0x00123F60: mov rax, qword ptr [rsp + 0x20]
0x00123F65: test rax, rax
0x00123F68: jne 0x140123f70
0x00123F6A: mov r10d, dword ptr [rcx + 4]
0x00123F6E: jmp 0x140123f7b
0x00123F70: mov rax, qword ptr [rsp + 0x20]
0x00123F75: movsx r10d, byte ptr [rax + rcx + 7]
0x00123F7B: mov rdx, qword ptr [rsp + 0x20]
0x00123F80: mov rax, qword ptr [rsp + 0x20]
0x00123F85: movsx r8d, byte ptr [rax + rcx + 8]
0x00123F8B: mov eax, dword ptr [rcx]
0x00123F8D: add al, dl
0x00123F8F: movsx r9d, al
0x00123F93: mov rax, qword ptr [rsp + 0x20]
0x00123F98: xor r9d, r8d
0x00123F9B: xor r9d, r10d
0x00123F9E: mov byte ptr [rsp + rax + 0x30], r9b
0x00123FA3: inc qword ptr [rsp + 0x20]
0x00123FA8: mov rax, qword ptr [rsp + 0x20]
0x00123FAD: cmp rax, 0x107
0x00123FB3: jb 0x140123f60
0x00123FB5: mov qword ptr [rbx + 0x18], 0xf
0x00123FBD: mov edx, 0x107
0x00123FC2: mov qword ptr [rbx + 0x10], r11
0x00123FC6: mov rcx, rbx
0x00123FC9: mov byte ptr [rbx], r11b
0x00123FCC: call 0x140039c30
0x00123FD1: movzx r9d, byte ptr [rsp + 0x28]
0x00123FD7: lea r8, [rsp + 0x137]
0x00123FDF: lea rdx, [rsp + 0x30]
0x00123FE4: mov rcx, rbx
0x00123FE7: call 0x14002bdb0
0x00123FEC: mov rax, rbx
0x00123FEF: mov rcx, qword ptr [rsp + 0x140]
0x00123FF7: xor rcx, rsp
0x00123FFA: call 0x1403b24c0
```

## Calls

| RVA | target/form |
|---|---|
| `0x0012314C` | `RVA 0x00039C30` |
| `0x00123167` | `RVA 0x0002BDB0` |
| `0x0012317A` | `RVA 0x003B24C0` |
| `0x0012323C` | `RVA 0x00039C30` |
| `0x00123257` | `RVA 0x0002BDB0` |
| `0x0012326A` | `RVA 0x003B24C0` |
| `0x0012332C` | `RVA 0x00039C30` |
| `0x00123347` | `RVA 0x0002BDB0` |
| `0x0012335A` | `RVA 0x003B24C0` |
| `0x0012341C` | `RVA 0x00039C30` |
| `0x00123437` | `RVA 0x0002BDB0` |
| `0x0012344A` | `RVA 0x003B24C0` |
| `0x001234FE` | `RVA 0x00039C30` |
| `0x00123516` | `RVA 0x0002BDB0` |
| `0x00123529` | `RVA 0x003B24C0` |
| `0x001235DE` | `RVA 0x00039C30` |
| `0x001235F9` | `RVA 0x0002BDB0` |
| `0x0012360C` | `RVA 0x003B24C0` |
| `0x001236CC` | `RVA 0x00039C30` |
| `0x001236E7` | `RVA 0x0002BDB0` |
| `0x001236FA` | `RVA 0x003B24C0` |
| `0x001237BC` | `RVA 0x00039C30` |
| `0x001237D7` | `RVA 0x0002BDB0` |
| `0x001237EA` | `RVA 0x003B24C0` |
| `0x001238AC` | `RVA 0x00039C30` |
| `0x001238C7` | `RVA 0x0002BDB0` |
| `0x001238DA` | `RVA 0x003B24C0` |
| `0x0012398E` | `RVA 0x00039C30` |
| `0x001239A9` | `RVA 0x0002BDB0` |
| `0x001239BC` | `RVA 0x003B24C0` |
| `0x00123A7C` | `RVA 0x00039C30` |
| `0x00123A97` | `RVA 0x0002BDB0` |
| `0x00123AAA` | `RVA 0x003B24C0` |
| `0x00123B58` | `RVA 0x00039C30` |
| `0x00123B70` | `RVA 0x0002BDB0` |
| `0x00123B80` | `RVA 0x003B24C0` |
| `0x00123C2E` | `RVA 0x00039C30` |
| `0x00123C46` | `RVA 0x0002BDB0` |
| `0x00123C59` | `RVA 0x003B24C0` |
| `0x00123D1C` | `RVA 0x00039C30` |
| `0x00123D37` | `RVA 0x0002BDB0` |
| `0x00123D4A` | `RVA 0x003B24C0` |
| `0x00123DF8` | `RVA 0x00039C30` |
| `0x00123E10` | `RVA 0x0002BDB0` |
| `0x00123E20` | `RVA 0x003B24C0` |
| `0x00123EDC` | `RVA 0x00039C30` |
| `0x00123EF7` | `RVA 0x0002BDB0` |
| `0x00123F0A` | `RVA 0x003B24C0` |
| `0x00123FCC` | `RVA 0x00039C30` |
| `0x00123FE7` | `RVA 0x0002BDB0` |
| `0x00123FFA` | `RVA 0x003B24C0` |

## Context around timing-field accesses

### vmr_rxboost at `0x00123553`

```asm
0x00123538: int3
0x00123539: int3
0x0012353A: int3
0x0012353B: int3
0x0012353C: int3
0x0012353D: int3
0x0012353E: int3
0x0012353F: int3
0x00123540: push rbx
0x00123542: sub rsp, 0xc0
0x00123549: mov rax, qword ptr [rip + 0x6b33a0]
0x00123550: xor rax, rsp
0x00123553: mov qword ptr [rsp + 0xb0], rax
0x0012355B: xor r10d, r10d
0x0012355E: mov rbx, rdx
0x00123561: mov qword ptr [rsp + 0x20], r10
0x00123566: mov rax, qword ptr [rsp + 0x20]
0x0012356B: mov dword ptr [rsp + 0x2c], r10d
0x00123570: cmp rax, 0x79
0x00123574: jae 0x1401235c7
0x00123576: mov rax, qword ptr [rsp + 0x20]
0x0012357B: test rax, rax
0x0012357E: jne 0x140123586
0x00123580: mov r9d, dword ptr [rcx + 4]
0x00123584: jmp 0x140123591
0x00123586: mov rax, qword ptr [rsp + 0x20]
0x0012358B: movsx r9d, byte ptr [rax + rcx + 7]
0x00123591: mov rdx, qword ptr [rsp + 0x20]
0x00123596: mov rax, qword ptr [rsp + 0x20]
0x0012359B: movsx r8d, byte ptr [rax + rcx + 8]
```

### vmr_rxboost at `0x00123601`

```asm
0x001235C7: mov qword ptr [rbx + 0x18], 0xf
0x001235CF: mov edx, 0x79
0x001235D4: mov qword ptr [rbx + 0x10], r10
0x001235D8: mov rcx, rbx
0x001235DB: mov byte ptr [rbx], r10b
0x001235DE: call 0x140039c30
0x001235E3: movzx r9d, byte ptr [rsp + 0x28]
0x001235E9: lea r8, [rsp + 0xa9]
0x001235F1: lea rdx, [rsp + 0x30]
0x001235F6: mov rcx, rbx
0x001235F9: call 0x14002bdb0
0x001235FE: mov rax, rbx
0x00123601: mov rcx, qword ptr [rsp + 0xb0]
0x00123609: xor rcx, rsp
0x0012360C: call 0x1403b24c0
0x00123611: add rsp, 0xc0
0x00123618: pop rbx
0x00123619: ret
0x0012361A: int3
0x0012361B: int3
0x0012361C: int3
0x0012361D: int3
0x0012361E: int3
0x0012361F: int3
0x00123620: push rbx
0x00123622: sub rsp, 0x1b0
0x00123629: mov rax, qword ptr [rip + 0x6b32c0]
0x00123630: xor rax, rsp
0x00123633: mov qword ptr [rsp + 0x1a0], rax
0x0012363B: xor r11d, r11d
```
