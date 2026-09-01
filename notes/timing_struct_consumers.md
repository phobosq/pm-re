# Multi-field timing structure consumers

functions reading >=3 confirmed fields: 3

| fields | PDATA | matched |
|---:|---|---|
| 5 | `0x003053C0..0x00305BB6` | mt, straps, vmr_rxboost, vmt2, vmt3 |
| 4 | `0x003C397C..0x003C3C19` | straps, vmr_rxboost, vmt2, vmt3 |
| 3 | `0x003BF648..0x003BF8A4` | straps, vmt2, vmt3 |

## Candidate details

### 5 fields `0x003053C0..0x00305BB6`

Key accesses:
- mt +0x98: `0x00305964: mov ebx, dword ptr [rcx + 0x98]`
- straps +0xAC: `0x00305A65: add r8d, dword ptr [rcx + 0xac]`
- vmr_rxboost +0xB0: `0x00305A53: mov ebx, dword ptr [rcx + 0xb0]`
- vmt2 +0xB8: `0x00305ACD: mov esi, dword ptr [rcx + 0xb8]`
- vmt3 +0xBC: `0x00305B0F: mov r11d, dword ptr [rcx + 0xbc]`

```asm
0x003053C0: mov qword ptr [rsp + 8], rbx
0x003053C5: mov qword ptr [rsp + 0x10], rsi
0x003053CA: mov qword ptr [rsp + 0x18], rdi
0x003053CF: mov qword ptr [rsp + 0x20], r14
0x003053D4: mov r9d, dword ptr [rdx]
0x003053D7: mov r11, rdx
0x003053DA: mov edi, dword ptr [rcx]
0x003053DC: mov r8d, r9d
0x003053DF: mov esi, dword ptr [rcx + 4]
0x003053E2: mov eax, edi
0x003053E4: shr eax, 0x10
0x003053E7: mov ebx, esi
0x003053E9: imul r8d, eax
0x003053ED: mov r14, rcx
0x003053F0: shr ebx, 0x10
0x003053F3: mov edx, 1
0x003053F8: test r8d, r8d
0x003053FB: je 0x140305412
0x003053FD: mov eax, r8d
0x00305400: movzx r10d, r8w
0x00305404: shr eax, 0x10
0x00305407: sub r10d, eax
0x0030540A: mov eax, r10d
0x0030540D: shr eax, 0x10
0x00305410: jmp 0x140305418
0x00305412: mov r10d, edx
0x00305415: sub r10d, r9d
0x00305418: add edi, dword ptr [r11 + 4]
0x0030541C: lea rcx, [r11 + 4]
0x00305420: mov r11d, dword ptr [r11 + 0xc]
0x00305424: sub r10d, eax
0x00305427: add ebx, dword ptr [rcx + 4]
0x0030542A: mov r8d, r11d
0x0030542D: movzx eax, si
0x00305430: imul r8d, eax
0x00305434: test r8d, r8d
0x00305437: je 0x14030544e
0x00305439: mov eax, r8d
0x0030543C: movzx r9d, r8w
0x00305440: shr eax, 0x10
0x00305443: sub r9d, eax
0x00305446: mov eax, r9d
0x00305449: shr eax, 0x10
0x0030544C: jmp 0x140305454
0x0030544E: mov r9d, edx
0x00305451: sub r9d, r11d
0x00305454: sub r9d, eax
0x00305457: mov eax, ebx
0x00305459: xor eax, r10d
0x0030545C: movzx r11d, ax
0x00305460: mov eax, dword ptr [rcx + 0xc]
0x00305463: mov r8d, eax
0x00305466: imul r8d, r11d
0x0030546A: test r8d, r8d
0x0030546D: je 0x140305487
0x0030546F: mov eax, r8d
0x00305472: movzx r8d, r8w
0x00305476: shr eax, 0x10
0x00305479: sub r8d, eax
0x0030547C: mov eax, r8d
0x0030547F: shr eax, 0x10
0x00305482: sub r8d, eax
0x00305485: jmp 0x140305490
0x00305487: mov r8d, edx
0x0030548A: sub r8d, eax
0x0030548D: sub r8d, r11d
0x00305490: mov esi, dword ptr [rcx + 0x10]
0x00305493: mov eax, r9d
0x00305496: xor eax, edi
0x00305498: mov r11d, esi
0x0030549B: add eax, r8d
0x0030549E: movzx eax, ax
0x003054A1: imul r11d, eax
0x003054A5: test r11d, r11d
0x003054A8: je 0x1403054bf
0x003054AA: mov eax, r11d
0x003054AD: movzx r11d, r11w
0x003054B1: shr eax, 0x10
0x003054B4: sub r11d, eax
0x003054B7: mov eax, r11d
0x003054BA: shr eax, 0x10
0x003054BD: jmp 0x1403054c5
0x003054BF: mov r11d, edx
0x003054C2: sub r11d, esi
0x003054C5: sub r11d, eax
0x003054C8: add r8d, r11d
0x003054CB: xor r9d, r8d
0x003054CE: xor r8d, edi
0x003054D1: mov edi, r11d
0x003054D4: xor r11d, r10d
0x003054D7: xor edi, ebx
0x003054D9: movzx eax, r11w
0x003054DD: mov ebx, dword ptr [rcx + 0x14]
0x003054E0: mov r10d, ebx
0x003054E3: imul r10d, eax
0x003054E7: test r10d, r10d
0x003054EA: je 0x140305501
0x003054EC: mov eax, r10d
0x003054EF: movzx r11d, r10w
0x003054F3: shr eax, 0x10
0x003054F6: sub r11d, eax
0x003054F9: mov eax, r11d
0x003054FC: shr eax, 0x10
0x003054FF: jmp 0x140305507
0x00305501: mov r11d, edx
0x00305504: sub r11d, ebx
0x00305507: mov ebx, dword ptr [rcx + 0x20]
0x0030550A: sub r11d, eax
0x0030550D: add edi, dword ptr [rcx + 0x18]
0x00305510: add r8d, dword ptr [rcx + 0x1c]
0x00305514: movzx eax, r9w
0x00305518: mov r9d, ebx
0x0030551B: imul r9d, eax
0x0030551F: test r9d, r9d
0x00305522: je 0x140305539
0x00305524: mov eax, r9d
0x00305527: movzx r10d, r9w
0x0030552B: shr eax, 0x10
0x0030552E: sub r10d, eax
0x00305531: mov eax, r10d
0x00305534: shr eax, 0x10
0x00305537: jmp 0x14030553f
0x00305539: mov r10d, edx
0x0030553C: sub r10d, ebx
0x0030553F: mov ebx, dword ptr [rcx + 0x24]
0x00305542: sub r10d, eax
0x00305545: mov eax, r8d
0x00305548: mov r9d, ebx
0x0030554B: xor eax, r11d
0x0030554E: movzx eax, ax
0x00305551: imul r9d, eax
0x00305555: test r9d, r9d
0x00305558: je 0x14030556f
0x0030555A: mov eax, r9d
0x0030555D: movzx r9d, r9w
0x00305561: shr eax, 0x10
0x00305564: sub r9d, eax
0x00305567: mov eax, r9d
0x0030556A: shr eax, 0x10
0x0030556D: jmp 0x140305575
0x0030556F: mov r9d, edx
0x00305572: sub r9d, ebx
0x00305575: mov esi, dword ptr [rcx + 0x28]
0x00305578: sub r9d, eax
0x0030557B: mov eax, r10d
0x0030557E: mov ebx, esi
0x00305580: xor eax, edi
0x00305582: add eax, r9d
0x00305585: movzx eax, ax
0x00305588: imul ebx, eax
0x0030558B: test ebx, ebx
0x0030558D: je 0x1403055a0
0x0030558F: mov eax, ebx
0x00305591: movzx ebx, bx
0x00305594: shr eax, 0x10
0x00305597: sub ebx, eax
0x00305599: mov eax, ebx
0x0030559B: shr eax, 0x10
0x0030559E: jmp 0x1403055a4
0x003055A0: mov ebx, edx
0x003055A2: sub ebx, esi
0x003055A4: sub ebx, eax
0x003055A6: add r9d, ebx
0x003055A9: xor r10d, r9d
0x003055AC: xor r9d, edi
0x003055AF: mov edi, ebx
0x003055B1: xor ebx, r11d
0x003055B4: xor edi, r8d
0x003055B7: movzx eax, bx
0x003055BA: mov ebx, dword ptr [rcx + 0x2c]
0x003055BD: mov r8d, ebx
0x003055C0: imul r8d, eax
0x003055C4: test r8d, r8d
0x003055C7: je 0x1403055de
0x003055C9: mov eax, r8d
0x003055CC: movzx r11d, r8w
0x003055D0: shr eax, 0x10
0x003055D3: sub r11d, eax
0x003055D6: mov eax, r11d
0x003055D9: shr eax, 0x10
0x003055DC: jmp 0x1403055e4
0x003055DE: mov r11d, edx
0x003055E1: sub r11d, ebx
0x003055E4: mov ebx, dword ptr [rcx + 0x38]
0x003055E7: sub r11d, eax
0x003055EA: add edi, dword ptr [rcx + 0x30]
0x003055ED: mov r8d, ebx
0x003055F0: add r9d, dword ptr [rcx + 0x34]
0x003055F4: movzx eax, r10w
0x003055F8: imul r8d, eax
0x003055FC: test r8d, r8d
0x003055FF: je 0x140305616
0x00305601: mov eax, r8d
0x00305604: movzx r10d, r8w
0x00305608: shr eax, 0x10
0x0030560B: sub r10d, eax
0x0030560E: mov eax, r10d
0x00305611: shr eax, 0x10
0x00305614: jmp 0x14030561c
0x00305616: mov r10d, edx
0x00305619: sub r10d, ebx
0x0030561C: mov ebx, dword ptr [rcx + 0x3c]
0x0030561F: sub r10d, eax
0x00305622: mov eax, r9d
0x00305625: mov r8d, ebx
0x00305628: xor eax, r11d
0x0030562B: movzx eax, ax
0x0030562E: imul r8d, eax
0x00305632: test r8d, r8d
0x00305635: je 0x14030564c
0x00305637: mov eax, r8d
0x0030563A: movzx r8d, r8w
0x0030563E: shr eax, 0x10
0x00305641: sub r8d, eax
0x00305644: mov eax, r8d
0x00305647: shr eax, 0x10
0x0030564A: jmp 0x140305652
0x0030564C: mov r8d, edx
0x0030564F: sub r8d, ebx
0x00305652: mov esi, dword ptr [rcx + 0x40]
0x00305655: sub r8d, eax
0x00305658: mov eax, r10d
0x0030565B: mov ebx, esi
0x0030565D: xor eax, edi
0x0030565F: add eax, r8d
0x00305662: movzx eax, ax
0x00305665: imul ebx, eax
0x00305668: test ebx, ebx
0x0030566A: je 0x14030567d
0x0030566C: mov eax, ebx
0x0030566E: movzx ebx, bx
0x00305671: shr eax, 0x10
0x00305674: sub ebx, eax
0x00305676: mov eax, ebx
0x00305678: shr eax, 0x10
0x0030567B: jmp 0x140305681
0x0030567D: mov ebx, edx
0x0030567F: sub ebx, esi
0x00305681: sub ebx, eax
0x00305683: add r8d, ebx
0x00305686: xor r10d, r8d
0x00305689: xor r8d, edi
0x0030568C: mov edi, ebx
0x0030568E: xor ebx, r11d
0x00305691: xor edi, r9d
0x00305694: movzx eax, bx
0x00305697: mov ebx, dword ptr [rcx + 0x44]
0x0030569A: mov r9d, ebx
0x0030569D: imul r9d, eax
0x003056A1: test r9d, r9d
0x003056A4: je 0x1403056bb
0x003056A6: mov eax, r9d
0x003056A9: movzx r11d, r9w
0x003056AD: shr eax, 0x10
0x003056B0: sub r11d, eax
0x003056B3: mov eax, r11d
0x003056B6: shr eax, 0x10
0x003056B9: jmp 0x1403056c1
0x003056BB: mov r11d, edx
0x003056BE: sub r11d, ebx
0x003056C1: mov ebx, dword ptr [rcx + 0x50]
0x003056C4: sub r11d, eax
0x003056C7: add edi, dword ptr [rcx + 0x48]
0x003056CA: mov r9d, ebx
0x003056CD: add r8d, dword ptr [rcx + 0x4c]
0x003056D1: movzx eax, r10w
0x003056D5: imul r9d, eax
0x003056D9: test r9d, r9d
0x003056DC: je 0x1403056f3
0x003056DE: mov eax, r9d
0x003056E1: movzx r10d, r9w
0x003056E5: shr eax, 0x10
0x003056E8: sub r10d, eax
0x003056EB: mov eax, r10d
0x003056EE: shr eax, 0x10
0x003056F1: jmp 0x1403056f9
0x003056F3: mov r10d, edx
0x003056F6: sub r10d, ebx
0x003056F9: mov ebx, dword ptr [rcx + 0x54]
0x003056FC: sub r10d, eax
0x003056FF: mov eax, r8d
0x00305702: mov r9d, ebx
0x00305705: xor eax, r11d
0x00305708: movzx eax, ax
0x0030570B: imul r9d, eax
0x0030570F: test r9d, r9d
0x00305712: je 0x140305729
0x00305714: mov eax, r9d
0x00305717: movzx r9d, r9w
0x0030571B: shr eax, 0x10
0x0030571E: sub r9d, eax
0x00305721: mov eax, r9d
0x00305724: shr eax, 0x10
0x00305727: jmp 0x14030572f
0x00305729: mov r9d, edx
0x0030572C: sub r9d, ebx
0x0030572F: mov esi, dword ptr [rcx + 0x58]
0x00305732: sub r9d, eax
0x00305735: mov eax, r10d
0x00305738: mov ebx, esi
0x0030573A: xor eax, edi
0x0030573C: add eax, r9d
0x0030573F: movzx eax, ax
0x00305742: imul ebx, eax
0x00305745: test ebx, ebx
0x00305747: je 0x14030575a
0x00305749: mov eax, ebx
0x0030574B: movzx ebx, bx
0x0030574E: shr eax, 0x10
0x00305751: sub ebx, eax
0x00305753: mov eax, ebx
0x00305755: shr eax, 0x10
0x00305758: jmp 0x14030575e
0x0030575A: mov ebx, edx
0x0030575C: sub ebx, esi
0x0030575E: sub ebx, eax
0x00305760: add r9d, ebx
0x00305763: xor r10d, r9d
0x00305766: xor r9d, edi
0x00305769: mov edi, ebx
0x0030576B: xor ebx, r11d
0x0030576E: xor edi, r8d
0x00305771: movzx eax, bx
0x00305774: mov ebx, dword ptr [rcx + 0x5c]
0x00305777: mov r8d, ebx
0x0030577A: imul r8d, eax
0x0030577E: test r8d, r8d
0x00305781: je 0x140305798
0x00305783: mov eax, r8d
0x00305786: movzx r11d, r8w
0x0030578A: shr eax, 0x10
0x0030578D: sub r11d, eax
0x00305790: mov eax, r11d
0x00305793: shr eax, 0x10
0x00305796: jmp 0x14030579e
0x00305798: mov r11d, edx
0x0030579B: sub r11d, ebx
0x0030579E: mov ebx, dword ptr [rcx + 0x68]
0x003057A1: sub r11d, eax
0x003057A4: add edi, dword ptr [rcx + 0x60]
0x003057A7: mov r8d, ebx
0x003057AA: add r9d, dword ptr [rcx + 0x64]
0x003057AE: movzx eax, r10w
0x003057B2: imul r8d, eax
0x003057B6: test r8d, r8d
0x003057B9: je 0x1403057d0
0x003057BB: mov eax, r8d
0x003057BE: movzx r10d, r8w
0x003057C2: shr eax, 0x10
0x003057C5: sub r10d, eax
0x003057C8: mov eax, r10d
0x003057CB: shr eax, 0x10
0x003057CE: jmp 0x1403057d6
0x003057D0: mov r10d, edx
0x003057D3: sub r10d, ebx
0x003057D6: mov ebx, dword ptr [rcx + 0x6c]
0x003057D9: sub r10d, eax
0x003057DC: mov eax, r9d
0x003057DF: mov r8d, ebx
0x003057E2: xor eax, r11d
0x003057E5: movzx eax, ax
0x003057E8: imul r8d, eax
0x003057EC: test r8d, r8d
0x003057EF: je 0x140305806
0x003057F1: mov eax, r8d
0x003057F4: movzx r8d, r8w
0x003057F8: shr eax, 0x10
0x003057FB: sub r8d, eax
0x003057FE: mov eax, r8d
0x00305801: shr eax, 0x10
0x00305804: jmp 0x14030580c
0x00305806: mov r8d, edx
0x00305809: sub r8d, ebx
0x0030580C: mov esi, dword ptr [rcx + 0x70]
0x0030580F: sub r8d, eax
0x00305812: mov eax, r10d
0x00305815: mov ebx, esi
0x00305817: xor eax, edi
0x00305819: add eax, r8d
0x0030581C: movzx eax, ax
0x0030581F: imul ebx, eax
0x00305822: test ebx, ebx
0x00305824: je 0x140305837
0x00305826: mov eax, ebx
0x00305828: movzx ebx, bx
0x0030582B: shr eax, 0x10
0x0030582E: sub ebx, eax
0x00305830: mov eax, ebx
0x00305832: shr eax, 0x10
0x00305835: jmp 0x14030583b
0x00305837: mov ebx, edx
0x00305839: sub ebx, esi
0x0030583B: sub ebx, eax
0x0030583D: add r8d, ebx
0x00305840: xor r10d, r8d
0x00305843: xor r8d, edi
0x00305846: mov edi, ebx
0x00305848: xor ebx, r11d
0x0030584B: xor edi, r9d
0x0030584E: movzx eax, bx
0x00305851: mov ebx, dword ptr [rcx + 0x74]
0x00305854: mov r9d, ebx
0x00305857: imul r9d, eax
0x0030585B: test r9d, r9d
0x0030585E: je 0x140305875
0x00305860: mov eax, r9d
0x00305863: movzx r11d, r9w
0x00305867: shr eax, 0x10
0x0030586A: sub r11d, eax
0x0030586D: mov eax, r11d
0x00305870: shr eax, 0x10
0x00305873: jmp 0x14030587b
0x00305875: mov r11d, edx
0x00305878: sub r11d, ebx
0x0030587B: mov ebx, dword ptr [rcx + 0x80]
0x00305881: sub r11d, eax
0x00305884: add edi, dword ptr [rcx + 0x78]
0x00305887: mov r9d, ebx
0x0030588A: add r8d, dword ptr [rcx + 0x7c]
0x0030588E: movzx eax, r10w
0x00305892: imul r9d, eax
0x00305896: test r9d, r9d
0x00305899: je 0x1403058b0
0x0030589B: mov eax, r9d
0x0030589E: movzx r10d, r9w
0x003058A2: shr eax, 0x10
0x003058A5: sub r10d, eax
0x003058A8: mov eax, r10d
0x003058AB: shr eax, 0x10
0x003058AE: jmp 0x1403058b6
0x003058B0: mov r10d, edx
0x003058B3: sub r10d, ebx
0x003058B6: mov ebx, dword ptr [rcx + 0x84]
0x003058BC: sub r10d, eax
0x003058BF: mov eax, r8d
0x003058C2: mov r9d, ebx
0x003058C5: xor eax, r11d
0x003058C8: movzx eax, ax
0x003058CB: imul r9d, eax
0x003058CF: test r9d, r9d
0x003058D2: je 0x1403058e9
0x003058D4: mov eax, r9d
0x003058D7: movzx r9d, r9w
0x003058DB: shr eax, 0x10
0x003058DE: sub r9d, eax
0x003058E1: mov eax, r9d
0x003058E4: shr eax, 0x10
0x003058E7: jmp 0x1403058ef
0x003058E9: mov r9d, edx
0x003058EC: sub r9d, ebx
0x003058EF: mov esi, dword ptr [rcx + 0x88]
0x003058F5: sub r9d, eax
0x003058F8: mov eax, r10d
0x003058FB: mov ebx, esi
0x003058FD: xor eax, edi
0x003058FF: add eax, r9d
0x00305902: movzx eax, ax
0x00305905: imul ebx, eax
0x00305908: test ebx, ebx
0x0030590A: je 0x14030591d
0x0030590C: mov eax, ebx
0x0030590E: movzx ebx, bx
0x00305911: shr eax, 0x10
0x00305914: sub ebx, eax
0x00305916: mov eax, ebx
0x00305918: shr eax, 0x10
0x0030591B: jmp 0x140305921
0x0030591D: mov ebx, edx
0x0030591F: sub ebx, esi
0x00305921: sub ebx, eax
0x00305923: add r9d, ebx
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

### 4 fields `0x003C397C..0x003C3C19`

Key accesses:
- straps +0xAC: `0x003C3BA7: mov edx, dword ptr [rsi + 0xac]`
- vmr_rxboost +0xB0: `0x003C3AE5: mov r8d, dword ptr [rsi + 0xb0]`
- vmt2 +0xB8: `0x003C3B08: mov eax, dword ptr [rsi + 0xb8]`
- vmt2 +0xB8: `0x003C3B51: mov eax, dword ptr [rsi + 0xb8]`
- vmt3 +0xBC: `0x003C3AB2: mov r10d, dword ptr [rsi + 0xbc]`

```asm
0x003C397C: mov qword ptr [rsp + 8], rcx
0x003C3981: push rbp
0x003C3982: push rsi
0x003C3983: push rdi
0x003C3984: sub rsp, 0x30
0x003C3988: mov qword ptr [rsp + 0x20], 0xfffffffffffffffe
0x003C3991: mov qword ptr [rsp + 0x60], rbx
0x003C3996: mov rdi, r9
0x003C3999: mov rbx, rdx
0x003C399C: mov rsi, rcx
0x003C399F: lea rax, [rip + 0x34ebc2]
0x003C39A6: mov qword ptr [rcx], rax
0x003C39A9: xor ebp, ebp
0x003C39AB: mov qword ptr [rcx + 8], rbp
0x003C39AF: mov qword ptr [rcx + 0x18], r8
0x003C39B3: add rcx, 0x40
0x003C39B7: call 0x1403b3374
0x003C39BC: nop
0x003C39BD: mov qword ptr [rsi + 0x68], rbp
0x003C39C1: mov dword ptr [rsi + 0xa8], ebp
0x003C39C7: mov qword ptr [rsi + 0xcc], rbp
0x003C39CE: mov qword ptr [rsi + 0xd8], rbp
0x003C39D5: mov qword ptr [rsi + 0xe0], rbp
0x003C39DC: mov dword ptr [rsi + 0xe8], ebp
0x003C39E2: mov dword ptr [rsi + 0xf8], ebp
0x003C39E8: mov qword ptr [rsi + 0x100], rbp
0x003C39EF: mov qword ptr [rsi + 0x10], rbx
0x003C39F3: lea edx, [rbp + 1]
0x003C39F6: mov rcx, rdi
0x003C39F9: call 0x1403c2bb4
0x003C39FE: mov dword ptr [rsi + 0xbc], eax
0x003C3A04: lea edx, [rbp + 2]
0x003C3A07: mov rcx, rdi
0x003C3A0A: call 0x1403c2bb4
0x003C3A0F: mov dword ptr [rsi + 0xb8], eax
0x003C3A15: lea edx, [rbp + 3]
0x003C3A18: mov rcx, rdi
0x003C3A1B: call 0x1403c2bb4
0x003C3A20: mov dword ptr [rsi + 0xc0], eax
0x003C3A26: lea edx, [rbp + 5]
0x003C3A29: mov rcx, rdi
0x003C3A2C: call 0x1403c2bb4
0x003C3A31: mov dword ptr [rsi + 0xc4], eax
0x003C3A37: lea edx, [rbp + 6]
0x003C3A3A: mov rcx, rdi
0x003C3A3D: call 0x1403c2bb4
0x003C3A42: mov dword ptr [rsi + 0xc8], eax
0x003C3A48: lea edx, [rbp + 8]
0x003C3A4B: mov rcx, rdi
0x003C3A4E: call 0x1403c2bb4
0x003C3A53: cmp eax, 1
0x003C3A56: sete al
0x003C3A59: mov byte ptr [rsi + 0x108], al
0x003C3A5F: cmp dword ptr [rsi + 0xc8], 0xf000
0x003C3A69: jne 0x1403c3a82
0x003C3A6B: call qword ptr [rip + 0x6c757]
0x003C3A71: mov rcx, rax
0x003C3A74: call 0x1403b5ae0
0x003C3A79: movsx ecx, al
0x003C3A7C: mov dword ptr [rsi + 0xc8], ecx
0x003C3A82: mov rdi, qword ptr [rsi + 0x10]
0x003C3A86: mov rax, qword ptr [rdi]
0x003C3A89: mov rbx, qword ptr [rax]
0x003C3A8C: mov rcx, rbx
0x003C3A8F: call 0x1403b2e14
0x003C3A94: mov rcx, rdi
0x003C3A97: call rbx
0x003C3A99: mov dword ptr [rsi + 0xac], eax
0x003C3A9F: call 0x1403b868c
0x003C3AA4: mov ebx, eax
0x003C3AA6: mov dword ptr [rsi + 0xec], eax
0x003C3AAC: mov ecx, dword ptr [rsi + 0xc0]
0x003C3AB2: mov r10d, dword ptr [rsi + 0xbc]
0x003C3AB9: lea eax, [r10 - 1]
0x003C3ABD: add eax, ebx
0x003C3ABF: xor edx, edx
0x003C3AC1: div ebx
0x003C3AC3: cmp ecx, eax
0x003C3AC5: jae 0x1403c3ad5
0x003C3AC7: mov dword ptr [rsi + 0xc0], eax
0x003C3ACD: mov dword ptr [rsi + 0xb0], ebx
0x003C3AD3: jmp 0x1403c3ae5
0x003C3AD5: lea eax, [rcx - 1]
0x003C3AD8: add eax, r10d
0x003C3ADB: xor edx, edx
0x003C3ADD: div ecx
0x003C3ADF: mov dword ptr [rsi + 0xb0], eax
0x003C3AE5: mov r8d, dword ptr [rsi + 0xb0]
0x003C3AEC: xor edx, edx
0x003C3AEE: mov eax, r10d
0x003C3AF1: div r8d
0x003C3AF4: mov r9d, eax
0x003C3AF7: test edx, edx
0x003C3AF9: jne 0x1403c3b1a
0x003C3AFB: mov dword ptr [rsi + 0xc0], eax
0x003C3B01: mov dword ptr [rsi + 0xd4], r8d
0x003C3B08: mov eax, dword ptr [rsi + 0xb8]
0x003C3B0E: dec eax
0x003C3B10: add eax, r9d
0x003C3B13: xor edx, edx
0x003C3B15: div r9d
0x003C3B18: jmp 0x1403c3b75
0x003C3B1A: lea eax, [r10 - 1]
0x003C3B1E: add eax, r8d
0x003C3B21: xor edx, edx
0x003C3B23: div r8d
0x003C3B26: mov r9d, eax
0x003C3B29: mov dword ptr [rsi + 0xc0], eax
0x003C3B2F: mov ecx, 1
0x003C3B34: sub ecx, eax
0x003C3B36: imul ecx, r8d
0x003C3B3A: add ecx, r10d
0x003C3B3D: mov dword ptr [rsi + 0xd4], ecx
0x003C3B43: sub r8d, ecx
0x003C3B46: lea r10d, [rax - 1]
0x003C3B4A: mov ecx, r10d
0x003C3B4D: imul ecx, r8d
0x003C3B51: mov eax, dword ptr [rsi + 0xb8]
0x003C3B57: xor edx, edx
0x003C3B59: cmp ecx, eax
0x003C3B5B: jb 0x1403c3b68
0x003C3B5D: add eax, -2
0x003C3B60: add eax, r9d
0x003C3B63: div r10d
0x003C3B66: jmp 0x1403c3b75
0x003C3B68: sub eax, ecx
0x003C3B6A: dec eax
0x003C3B6C: add eax, r9d
0x003C3B6F: div r9d
0x003C3B72: add eax, r8d
0x003C3B75: mov dword ptr [rsi + 0xb4], eax
0x003C3B7B: mov rcx, qword ptr [rsi + 0x18]
0x003C3B7F: call 0x1403b9ed8
0x003C3B84: cmp byte ptr [rsi + 0x108], bpl
0x003C3B8B: je 0x1403c3bbe
0x003C3B8D: mov ecx, 0x838
0x003C3B92: call 0x1403b2098
0x003C3B97: mov qword ptr [rsp + 0x58], rax
0x003C3B9C: test rax, rax
0x003C3B9F: je 0x1403c3bb7
0x003C3BA1: mov r9, rsi
0x003C3BA4: mov r8d, ebx
0x003C3BA7: mov edx, dword ptr [rsi + 0xac]
0x003C3BAD: mov rcx, rax
0x003C3BB0: call 0x1403c3260
0x003C3BB5: jmp 0x1403c3bba
0x003C3BB7: mov rax, rbp
0x003C3BBA: mov qword ptr [rsi + 0x68], rax
0x003C3BBE: call 0x1403b89ac
0x003C3BC3: mov ecx, eax
0x003C3BC5: mov dword ptr [rsi + 0xf0], ecx
0x003C3BCB: mov qword ptr [rsi + 0x20], rbp
0x003C3BCF: mov eax, 4
0x003C3BD4: mul rcx
0x003C3BD7: mov rcx, 0xffffffffffffffff
0x003C3BDE: cmovo rax, rcx
0x003C3BE2: mov rcx, rax
0x003C3BE5: call 0x1403b2624
0x003C3BEA: mov qword ptr [rsi + 0x28], rax
0x003C3BEE: cmp dword ptr [rsi + 0xf0], ebp
0x003C3BF4: jbe 0x1403c3c09
0x003C3BF6: mov ecx, ebp
0x003C3BF8: mov rax, qword ptr [rsi + 0x28]
0x003C3BFC: mov dword ptr [rax + rcx*4], ebp
0x003C3BFF: inc ebp
0x003C3C01: cmp ebp, dword ptr [rsi + 0xf0]
0x003C3C07: jb 0x1403c3bf6
0x003C3C09: mov rax, rsi
0x003C3C0C: mov rbx, qword ptr [rsp + 0x60]
0x003C3C11: add rsp, 0x30
0x003C3C15: pop rdi
0x003C3C16: pop rsi
0x003C3C17: pop rbp
0x003C3C18: ret
```

### 3 fields `0x003BF648..0x003BF8A4`

Key accesses:
- straps +0xAC: `0x003BF736: sub ecx, dword ptr [r10 + 0xac]`
- vmt2 +0xB8: `0x003BF6BB: mov ebx, dword ptr [r8 + 0xb8]`
- vmt3 +0xBC: `0x003BF6AE: cmp edx, dword ptr [r8 + 0xbc]`

```asm
0x003BF648: mov rax, rsp
0x003BF64B: mov qword ptr [rax + 8], rbx
0x003BF64F: mov qword ptr [rax + 0x10], rbp
0x003BF653: mov qword ptr [rax + 0x18], rsi
0x003BF657: mov qword ptr [rax + 0x20], rdi
0x003BF65B: push r12
0x003BF65D: push r14
0x003BF65F: push r15
0x003BF661: sub rsp, 0x20
0x003BF665: xor esi, esi
0x003BF667: mov r14, r9
0x003BF66A: mov r15, r8
0x003BF66D: mov r12, rdx
0x003BF670: mov rdi, rcx
0x003BF673: cmp dword ptr [rcx + 0x44], esi
0x003BF676: jle 0x1403bf772
0x003BF67C: xor r11d, r11d
0x003BF67F: mov rax, qword ptr [rdi + 0x30]
0x003BF683: mov r8, qword ptr [r11 + rax]
0x003BF687: test r8, r8
0x003BF68A: je 0x1403bf763
0x003BF690: mov eax, dword ptr [r8 + 0xc0]
0x003BF697: xor r9d, r9d
0x003BF69A: test eax, eax
0x003BF69C: jle 0x1403bf763
0x003BF6A2: mov ecx, dword ptr [r8 + 0xa4]
0x003BF6A9: mov edx, r9d
0x003BF6AC: sar edx, cl
0x003BF6AE: cmp edx, dword ptr [r8 + 0xbc]
0x003BF6B5: jge 0x1403bf750
0x003BF6BB: mov ebx, dword ptr [r8 + 0xb8]
0x003BF6C2: cmp edx, ebx
0x003BF6C4: jl 0x1403bf6ea
0x003BF6C6: sub edx, ebx
0x003BF6C8: lea eax, [rbx - 1]
0x003BF6CB: movsxd rcx, eax
0x003BF6CE: mov rax, qword ptr [r8 + 0xb0]
0x003BF6D5: mov r10, qword ptr [rax + rcx*8]
0x003BF6D9: js 0x1403bf6f8
0x003BF6DB: lea ecx, [rdx + 1]
0x003BF6DE: mov r10, qword ptr [r10 + 8]
0x003BF6E2: sub rcx, 1
0x003BF6E6: jne 0x1403bf6de
0x003BF6E8: jmp 0x1403bf6f8
0x003BF6EA: mov rax, qword ptr [r8 + 0xb0]
0x003BF6F1: movsxd rcx, edx
0x003BF6F4: mov r10, qword ptr [rax + rcx*8]
0x003BF6F8: mov eax, dword ptr [r8 + 0xa0]
0x003BF6FF: dec eax
0x003BF701: movsxd rcx, eax
0x003BF704: movsxd rax, r9d
0x003BF707: and rcx, rax
0x003BF70A: mov rax, qword ptr [r10]
0x003BF70D: mov r10, qword ptr [rax + rcx*8]
0x003BF711: test r10, r10
0x003BF714: je 0x1403bf750
0x003BF716: mov eax, dword ptr [r10 + 0xa0]
0x003BF71D: mov edx, eax
0x003BF71F: sub edx, dword ptr [r10 + 0xa8]
0x003BF726: mov dword ptr [r10 + 0xa8], eax
0x003BF72D: mov eax, dword ptr [r10 + 0xa4]
0x003BF734: mov ecx, eax
0x003BF736: sub ecx, dword ptr [r10 + 0xac]
0x003BF73D: mov dword ptr [r10 + 0xac], eax
0x003BF744: add dword ptr [r15], edx
0x003BF747: sub edx, ecx
0x003BF749: add dword ptr [r12], ecx
0x003BF74D: add dword ptr [r14], edx
0x003BF750: mov eax, dword ptr [r8 + 0xc0]
0x003BF757: inc r9d
0x003BF75A: cmp r9d, eax
0x003BF75D: jl 0x1403bf6a2
0x003BF763: inc esi
0x003BF765: add r11, 8
0x003BF769: cmp esi, dword ptr [rdi + 0x44]
0x003BF76C: jl 0x1403bf67f
0x003BF772: mov eax, dword ptr [rdi + 0x2ac]
0x003BF778: xor ebp, ebp
0x003BF77A: mov edx, eax
0x003BF77C: sub edx, dword ptr [rdi + 0x2b4]
0x003BF782: mov dword ptr [rdi + 0x2b4], eax
0x003BF788: mov eax, dword ptr [rdi + 0x2b0]
0x003BF78E: mov ecx, eax
0x003BF790: sub ecx, dword ptr [rdi + 0x2b8]
0x003BF796: mov dword ptr [rdi + 0x2b8], eax
0x003BF79C: add dword ptr [r15], edx
0x003BF79F: sub edx, ecx
0x003BF7A1: add dword ptr [r12], ecx
0x003BF7A5: add dword ptr [r14], edx
0x003BF7A8: mov eax, dword ptr [rdi + 0x1c0]
0x003BF7AE: test eax, eax
0x003BF7B0: jle 0x1403bf885
0x003BF7B6: lea rsi, [rdi + 0x150]
0x003BF7BD: mov ecx, dword ptr [rsi + 0x54]
0x003BF7C0: mov edx, ebp
0x003BF7C2: sar edx, cl
0x003BF7C4: cmp edx, dword ptr [rsi + 0x6c]
0x003BF7C7: jge 0x1403bf875
0x003BF7CD: mov r9d, dword ptr [rsi + 0x68]
0x003BF7D1: cmp edx, r9d
0x003BF7D4: jl 0x1403bf7f9
0x003BF7D6: sub edx, r9d
0x003BF7D9: lea eax, [r9 - 1]
0x003BF7DD: movsxd rcx, eax
0x003BF7E0: mov rax, qword ptr [rsi + 0x60]
0x003BF7E4: mov r8, qword ptr [rax + rcx*8]
0x003BF7E8: js 0x1403bf804
0x003BF7EA: lea ecx, [rdx + 1]
0x003BF7ED: mov r8, qword ptr [r8 + 8]
0x003BF7F1: sub rcx, 1
0x003BF7F5: jne 0x1403bf7ed
0x003BF7F7: jmp 0x1403bf804
0x003BF7F9: mov rax, qword ptr [rsi + 0x60]
0x003BF7FD: movsxd rcx, edx
0x003BF800: mov r8, qword ptr [rax + rcx*8]
0x003BF804: mov eax, dword ptr [rsi + 0x50]
0x003BF807: dec eax
0x003BF809: movsxd rcx, eax
0x003BF80C: movsxd rax, ebp
0x003BF80F: and rcx, rax
0x003BF812: mov rax, qword ptr [r8]
0x003BF815: mov rbx, qword ptr [rax + rcx*8]
0x003BF819: test rbx, rbx
0x003BF81C: je 0x1403bf875
0x003BF81E: mov eax, dword ptr [rbx + 0x20]
0x003BF821: mov edx, eax
0x003BF823: sub edx, dword ptr [rbx + 0x28]
0x003BF826: mov dword ptr [rbx + 0x28], eax
0x003BF829: mov eax, dword ptr [rbx + 0x24]
0x003BF82C: mov ecx, eax
0x003BF82E: sub ecx, dword ptr [rbx + 0x2c]
0x003BF831: mov dword ptr [rbx + 0x2c], eax
0x003BF834: add dword ptr [r15], edx
0x003BF837: sub edx, ecx
0x003BF839: add dword ptr [r12], ecx
0x003BF83D: add dword ptr [r14], edx
0x003BF840: mov eax, dword ptr [rbx + 0x30]
0x003BF843: test eax, eax
0x003BF845: jne 0x1403bf875
0x003BF847: mov eax, dword ptr [rbx + 0x28]
0x003BF84A: cmp dword ptr [rbx + 0x20], eax
0x003BF84D: jne 0x1403bf875
0x003BF84F: mov eax, dword ptr [rbx + 0x2c]
0x003BF852: cmp dword ptr [rbx + 0x24], eax
0x003BF855: jne 0x1403bf875
0x003BF857: mov r8d, dword ptr [rbx]
0x003BF85A: xor r9d, r9d
0x003BF85D: mov rdx, rbx
0x003BF860: mov rcx, rsi
0x003BF863: call 0x1403bed14
0x003BF868: mov edx, 0x40
0x003BF86D: mov rcx, rbx
0x003BF870: call 0x1403b20dc
0x003BF875: mov eax, dword ptr [rdi + 0x1c0]
0x003BF87B: inc ebp
0x003BF87D: cmp ebp, eax
0x003BF87F: jl 0x1403bf7bd
0x003BF885: mov rbx, qword ptr [rsp + 0x40]
0x003BF88A: mov rbp, qword ptr [rsp + 0x48]
0x003BF88F: mov rsi, qword ptr [rsp + 0x50]
0x003BF894: mov rdi, qword ptr [rsp + 0x58]
0x003BF899: add rsp, 0x20
0x003BF89D: pop r15
0x003BF89F: pop r14
0x003BF8A1: pop r12
0x003BF8A3: ret
```
