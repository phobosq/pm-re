# Timing consumer candidate profiles

## `0x003053C0` PDATA `0x003053C0..0x00305BB6`

direct callers: `8`

- `0x00304B39` from `0x00304AD0..0x00304B87`
- `0x00304F5C` from `0x00304E50..0x00305108`
- `0x00305062` from `0x00304E50..0x00305108`
- `0x003051D6` from `0x00305108..0x003053C0`
- `0x00305299` from `0x00305108..0x003053C0`
- `0x00305C78` from `0x00305BC0..0x00305DDD`
- `0x00305D4D` from `0x00305BC0..0x00305DDD`
- `0x00305EEE` from `0x00305DE0..0x00305FCC`

### Calls

| RVA | target |
|---|---|

### Full body

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

## `0x003C397C` PDATA `0x003C397C..0x003C3C19`

direct callers: `1`

- `0x003B6E25` from `0x003B6DC8..0x003B6E4A`

### Calls

| RVA | target |
|---|---|
| `0x003C39B7` | `RVA 0x003B3374` |
| `0x003C39F9` | `RVA 0x003C2BB4` |
| `0x003C3A0A` | `RVA 0x003C2BB4` |
| `0x003C3A1B` | `RVA 0x003C2BB4` |
| `0x003C3A2C` | `RVA 0x003C2BB4` |
| `0x003C3A3D` | `RVA 0x003C2BB4` |
| `0x003C3A4E` | `RVA 0x003C2BB4` |
| `0x003C3A6B` | `KERNEL32.dll!GetCurrentThread` |
| `0x003C3A74` | `RVA 0x003B5AE0` |
| `0x003C3A8F` | `RVA 0x003B2E14` |
| `0x003C3A97` | `rbx` |
| `0x003C3A9F` | `RVA 0x003B868C` |
| `0x003C3B7F` | `RVA 0x003B9ED8` |
| `0x003C3B92` | `RVA 0x003B2098` |
| `0x003C3BB0` | `RVA 0x003C3260` |
| `0x003C3BBE` | `RVA 0x003B89AC` |
| `0x003C3BE5` | `RVA 0x003B2624` |

### Full body

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

## `0x0041D627` PDATA `0x0041D627..0x0041DAA6`

direct callers: `0`


### Calls

| RVA | target |
|---|---|
| `0x0041D644` | `qword ptr [rax + 8]` |
| `0x0041DA5F` | `RVA 0x000B28C0` |
| `0x0041DA85` | `RVA 0x001603F0` |
| `0x0041DA92` | `RVA 0x00032EF0` |

### Full body

```asm
0x0041D627: mov qword ptr [rsp + 0x10], rdx
0x0041D62C: push rbp
0x0041D62D: sub rsp, 0x30
0x0041D631: mov rbp, rdx
0x0041D634: mov rcx, qword ptr [rbp + 0x88]
0x0041D63B: mov eax, dword ptr [rcx + 0x18]
0x0041D63E: mov dword ptr [rbp + 0x30], eax
0x0041D641: mov rax, qword ptr [rcx]
0x0041D644: call qword ptr [rax + 8]
0x0041D647: mov qword ptr [rbp + 0x70], rax
0x0041D64B: mov dword ptr [rbp + 0xa8], 0x3a
0x0041D655: mov eax, dword ptr [rbp + 0xa8]
0x0041D65B: add al, 0x3a
0x0041D65D: movsx ecx, al
0x0041D660: xor ecx, 0x7d
0x0041D663: mov dword ptr [rbp + 0xac], ecx
0x0041D669: mov eax, dword ptr [rbp + 0xac]
0x0041D66F: mov ecx, dword ptr [rbp + 0xa8]
0x0041D675: xor ecx, eax
0x0041D677: xor ecx, 0x7b
0x0041D67A: mov byte ptr [rbp + 0xb0], cl
0x0041D680: movsx ecx, byte ptr [rbp + 0xb0]
0x0041D687: mov eax, dword ptr [rbp + 0xa8]
0x0041D68D: inc al
0x0041D68F: xor eax, ecx
0x0041D691: xor eax, 0x7d
0x0041D694: mov byte ptr [rbp + 0xb1], al
0x0041D69A: movsx ecx, byte ptr [rbp + 0xb1]
0x0041D6A1: mov eax, dword ptr [rbp + 0xa8]
0x0041D6A7: add al, 2
0x0041D6A9: xor eax, ecx
0x0041D6AB: xor eax, 0x3a
0x0041D6AE: mov byte ptr [rbp + 0xb2], al
0x0041D6B4: movsx ecx, byte ptr [rbp + 0xb2]
0x0041D6BB: mov eax, dword ptr [rbp + 0xa8]
0x0041D6C1: add al, 3
0x0041D6C3: xor eax, ecx
0x0041D6C5: xor eax, 0x20
0x0041D6C8: mov byte ptr [rbp + 0xb3], al
0x0041D6CE: movsx ecx, byte ptr [rbp + 0xb3]
0x0041D6D5: mov eax, dword ptr [rbp + 0xa8]
0x0041D6DB: add al, 4
0x0041D6DD: xor eax, ecx
0x0041D6DF: xor eax, 0x55
0x0041D6E2: mov byte ptr [rbp + 0xb4], al
0x0041D6E8: movsx ecx, byte ptr [rbp + 0xb4]
0x0041D6EF: mov eax, dword ptr [rbp + 0xa8]
0x0041D6F5: add al, 5
0x0041D6F7: xor eax, ecx
0x0041D6F9: xor eax, 0x6e
0x0041D6FC: mov byte ptr [rbp + 0xb5], al
0x0041D702: movsx ecx, byte ptr [rbp + 0xb5]
0x0041D709: mov eax, dword ptr [rbp + 0xa8]
0x0041D70F: add al, 6
0x0041D711: xor eax, ecx
0x0041D713: xor eax, 0x61
0x0041D716: mov byte ptr [rbp + 0xb6], al
0x0041D71C: movsx ecx, byte ptr [rbp + 0xb6]
0x0041D723: mov eax, dword ptr [rbp + 0xa8]
0x0041D729: add al, 7
0x0041D72B: xor eax, ecx
0x0041D72D: xor eax, 0x62
0x0041D730: mov byte ptr [rbp + 0xb7], al
0x0041D736: movsx ecx, byte ptr [rbp + 0xb7]
0x0041D73D: mov eax, dword ptr [rbp + 0xa8]
0x0041D743: add al, 8
0x0041D745: xor eax, ecx
0x0041D747: xor eax, 0x6c
0x0041D74A: mov byte ptr [rbp + 0xb8], al
0x0041D750: movsx ecx, byte ptr [rbp + 0xb8]
0x0041D757: mov eax, dword ptr [rbp + 0xa8]
0x0041D75D: add al, 9
0x0041D75F: xor eax, ecx
0x0041D761: xor eax, 0x65
0x0041D764: mov byte ptr [rbp + 0xb9], al
0x0041D76A: movsx ecx, byte ptr [rbp + 0xb9]
0x0041D771: mov eax, dword ptr [rbp + 0xa8]
0x0041D777: add al, 0xa
0x0041D779: xor eax, ecx
0x0041D77B: xor eax, 0x20
0x0041D77E: mov byte ptr [rbp + 0xba], al
0x0041D784: movsx ecx, byte ptr [rbp + 0xba]
0x0041D78B: mov eax, dword ptr [rbp + 0xa8]
0x0041D791: add al, 0xb
0x0041D793: xor eax, ecx
0x0041D795: xor eax, 0x74
0x0041D798: mov byte ptr [rbp + 0xbb], al
0x0041D79E: movsx ecx, byte ptr [rbp + 0xbb]
0x0041D7A5: mov eax, dword ptr [rbp + 0xa8]
0x0041D7AB: add al, 0xc
0x0041D7AD: xor eax, ecx
0x0041D7AF: xor eax, 0x6f
0x0041D7B2: mov byte ptr [rbp + 0xbc], al
0x0041D7B8: movsx ecx, byte ptr [rbp + 0xbc]
0x0041D7BF: mov eax, dword ptr [rbp + 0xa8]
0x0041D7C5: add al, 0xd
0x0041D7C7: xor eax, ecx
0x0041D7C9: xor eax, 0x20
0x0041D7CC: mov byte ptr [rbp + 0xbd], al
0x0041D7D2: movsx ecx, byte ptr [rbp + 0xbd]
0x0041D7D9: mov eax, dword ptr [rbp + 0xa8]
0x0041D7DF: add al, 0xe
0x0041D7E1: xor eax, ecx
0x0041D7E3: xor eax, 0x70
0x0041D7E6: mov byte ptr [rbp + 0xbe], al
0x0041D7EC: movsx ecx, byte ptr [rbp + 0xbe]
0x0041D7F3: mov eax, dword ptr [rbp + 0xa8]
0x0041D7F9: add al, 0xf
0x0041D7FB: xor eax, ecx
0x0041D7FD: xor eax, 0x72
0x0041D800: mov byte ptr [rbp + 0xbf], al
0x0041D806: movsx ecx, byte ptr [rbp + 0xbf]
0x0041D80D: mov eax, dword ptr [rbp + 0xa8]
0x0041D813: add al, 0x10
0x0041D815: xor eax, ecx
0x0041D817: xor eax, 0x65
0x0041D81A: mov byte ptr [rbp + 0xc0], al
0x0041D820: movsx ecx, byte ptr [rbp + 0xc0]
0x0041D827: mov eax, dword ptr [rbp + 0xa8]
0x0041D82D: add al, 0x11
0x0041D82F: xor eax, ecx
0x0041D831: xor eax, 0x70
0x0041D834: mov byte ptr [rbp + 0xc1], al
0x0041D83A: movsx ecx, byte ptr [rbp + 0xc1]
0x0041D841: mov eax, dword ptr [rbp + 0xa8]
0x0041D847: add al, 0x12
0x0041D849: xor eax, ecx
0x0041D84B: xor eax, 0x61
0x0041D84E: mov byte ptr [rbp + 0xc2], al
0x0041D854: movsx ecx, byte ptr [rbp + 0xc2]
0x0041D85B: mov eax, dword ptr [rbp + 0xa8]
0x0041D861: add al, 0x13
0x0041D863: xor eax, ecx
0x0041D865: xor eax, 0x72
0x0041D868: mov byte ptr [rbp + 0xc3], al
0x0041D86E: movsx ecx, byte ptr [rbp + 0xc3]
0x0041D875: mov eax, dword ptr [rbp + 0xa8]
0x0041D87B: add al, 0x14
0x0041D87D: xor eax, ecx
0x0041D87F: xor eax, 0x65
0x0041D882: mov byte ptr [rbp + 0xc4], al
0x0041D888: movsx ecx, byte ptr [rbp + 0xc4]
0x0041D88F: mov eax, dword ptr [rbp + 0xa8]
0x0041D895: add al, 0x15
0x0041D897: xor eax, ecx
0x0041D899: xor eax, 0x20
0x0041D89C: mov byte ptr [rbp + 0xc5], al
0x0041D8A2: movsx ecx, byte ptr [rbp + 0xc5]
0x0041D8A9: mov eax, dword ptr [rbp + 0xa8]
0x0041D8AF: add al, 0x16
0x0041D8B1: xor eax, ecx
0x0041D8B3: xor eax, 0x6b
0x0041D8B6: mov byte ptr [rbp + 0xc6], al
0x0041D8BC: movsx ecx, byte ptr [rbp + 0xc6]
0x0041D8C3: mov eax, dword ptr [rbp + 0xa8]
0x0041D8C9: add al, 0x17
0x0041D8CB: xor eax, ecx
0x0041D8CD: xor eax, 0x65
0x0041D8D0: mov byte ptr [rbp + 0xc7], al
0x0041D8D6: movsx ecx, byte ptr [rbp + 0xc7]
0x0041D8DD: mov eax, dword ptr [rbp + 0xa8]
0x0041D8E3: add al, 0x18
0x0041D8E5: xor eax, ecx
0x0041D8E7: xor eax, 0x72
0x0041D8EA: mov byte ptr [rbp + 0xc8], al
0x0041D8F0: movsx ecx, byte ptr [rbp + 0xc8]
0x0041D8F7: mov eax, dword ptr [rbp + 0xa8]
0x0041D8FD: add al, 0x19
0x0041D8FF: xor eax, ecx
0x0041D901: xor eax, 0x6e
0x0041D904: mov byte ptr [rbp + 0xc9], al
0x0041D90A: movsx ecx, byte ptr [rbp + 0xc9]
0x0041D911: mov eax, dword ptr [rbp + 0xa8]
0x0041D917: add al, 0x1a
0x0041D919: xor eax, ecx
0x0041D91B: xor eax, 0x65
0x0041D91E: mov byte ptr [rbp + 0xca], al
0x0041D924: movsx ecx, byte ptr [rbp + 0xca]
0x0041D92B: mov eax, dword ptr [rbp + 0xa8]
0x0041D931: add al, 0x1b
0x0041D933: xor eax, ecx
0x0041D935: xor eax, 0x6c
0x0041D938: mov byte ptr [rbp + 0xcb], al
0x0041D93E: movsx ecx, byte ptr [rbp + 0xcb]
0x0041D945: mov eax, dword ptr [rbp + 0xa8]
0x0041D94B: add al, 0x1c
0x0041D94D: xor eax, ecx
0x0041D94F: xor eax, 0x73
0x0041D952: mov byte ptr [rbp + 0xcc], al
0x0041D958: movsx ecx, byte ptr [rbp + 0xcc]
0x0041D95F: mov eax, dword ptr [rbp + 0xa8]
0x0041D965: add al, 0x1d
0x0041D967: xor eax, ecx
0x0041D969: xor eax, 0x3a
0x0041D96C: mov byte ptr [rbp + 0xcd], al
0x0041D972: movsx ecx, byte ptr [rbp + 0xcd]
0x0041D979: mov eax, dword ptr [rbp + 0xa8]
0x0041D97F: add al, 0x1e
0x0041D981: xor eax, ecx
0x0041D983: xor eax, 0x20
0x0041D986: mov byte ptr [rbp + 0xce], al
0x0041D98C: movsx ecx, byte ptr [rbp + 0xce]
0x0041D993: mov eax, dword ptr [rbp + 0xa8]
0x0041D999: add al, 0x1f
0x0041D99B: xor eax, ecx
0x0041D99D: xor eax, 0x7b
0x0041D9A0: mov byte ptr [rbp + 0xcf], al
0x0041D9A6: movsx ecx, byte ptr [rbp + 0xcf]
0x0041D9AD: mov eax, dword ptr [rbp + 0xa8]
0x0041D9B3: add al, 0x20
0x0041D9B5: xor eax, ecx
0x0041D9B7: xor eax, 0x7d
0x0041D9BA: mov byte ptr [rbp + 0xd0], al
0x0041D9C0: movsx ecx, byte ptr [rbp + 0xd0]
0x0041D9C7: mov eax, dword ptr [rbp + 0xa8]
0x0041D9CD: add al, 0x21
0x0041D9CF: xor eax, ecx
0x0041D9D1: xor eax, 0x20
0x0041D9D4: mov byte ptr [rbp + 0xd1], al
0x0041D9DA: movsx ecx, byte ptr [rbp + 0xd1]
0x0041D9E1: mov eax, dword ptr [rbp + 0xa8]
0x0041D9E7: add al, 0x22
0x0041D9E9: xor eax, ecx
0x0041D9EB: xor eax, 0x28
0x0041D9EE: mov byte ptr [rbp + 0xd2], al
0x0041D9F4: movsx ecx, byte ptr [rbp + 0xd2]
0x0041D9FB: mov eax, dword ptr [rbp + 0xa8]
0x0041DA01: add al, 0x23
0x0041DA03: xor eax, ecx
0x0041DA05: xor eax, 0x7b
0x0041DA08: mov byte ptr [rbp + 0xd3], al
0x0041DA0E: movsx ecx, byte ptr [rbp + 0xd3]
0x0041DA15: mov eax, dword ptr [rbp + 0xa8]
0x0041DA1B: add al, 0x24
0x0041DA1D: xor eax, ecx
0x0041DA1F: xor eax, 0x7d
0x0041DA22: mov byte ptr [rbp + 0xd4], al
0x0041DA28: movsx ecx, byte ptr [rbp + 0xd4]
0x0041DA2F: mov eax, dword ptr [rbp + 0xa8]
0x0041DA35: add al, 0x25
0x0041DA37: xor eax, ecx
0x0041DA39: xor eax, 0x29
0x0041DA3C: mov byte ptr [rbp + 0xd5], al
0x0041DA42: xor eax, eax
0x0041DA44: mov byte ptr [rbp + 0xd6], al
0x0041DA4A: movzx eax, byte ptr [rbp + 0xb0]
0x0041DA51: lea rdx, [rbp + 0x608]
0x0041DA58: lea rcx, [rbp + 0xa8]
0x0041DA5F: call 0x1400b28c0
0x0041DA64: mov rcx, rax
0x0041DA67: cmp qword ptr [rax + 0x18], 0x10
0x0041DA6C: jb 0x14041da71
0x0041DA6E: mov rcx, qword ptr [rax]
0x0041DA71: mov rax, qword ptr [rbp + 0x40]
0x0041DA75: mov rdx, qword ptr [rax + 8]
0x0041DA79: add rdx, 8
0x0041DA7D: lea r9, [rbp + 0x30]
0x0041DA81: lea r8, [rbp + 0x70]
0x0041DA85: call 0x1401603f0
0x0041DA8A: nop
0x0041DA8B: lea rcx, [rbp + 0x608]
0x0041DA92: call 0x140032ef0
0x0041DA97: nop
0x0041DA98: lea rax, [rip - 0x26c87e]
0x0041DA9F: add rsp, 0x30
0x0041DAA3: pop rbp
0x0041DAA4: ret
0x0041DAA5: int3
```

## `0x0015BB20` PDATA `0x0015BB20..0x0015C0CC`

direct callers: `3`

- `0x0015BA6C` from `0x0015B940..0x0015BB14`
- `0x0015BAA6` from `0x0015B940..0x0015BB14`
- `0x0015BACA` from `0x0015B940..0x0015BB14`

### Calls

| RVA | target |
|---|---|

### Full body

```asm
0x0015BB20: mov qword ptr [rsp + 0x10], rbx
0x0015BB25: mov qword ptr [rsp + 0x18], rsi
0x0015BB2A: mov qword ptr [rsp + 0x20], rdi
0x0015BB2F: lea rdi, [rip + 0x2eef0a]
0x0015BB36: lea rsi, [rip + 0x2eefc3]
0x0015BB3D: nop dword ptr [rax]
0x0015BB40: mov r9, qword ptr [rcx + 8]
0x0015BB44: xor r9, qword ptr [rcx + 0x80]
0x0015BB4B: xor r9, qword ptr [rcx + 0x30]
0x0015BB4F: xor r9, qword ptr [rcx + 0xa8]
0x0015BB56: xor r9, qword ptr [rcx + 0x58]
0x0015BB5A: mov r8, qword ptr [rcx + 0x20]
0x0015BB5E: mov rdx, r9
0x0015BB61: xor r8, qword ptr [rcx + 0x98]
0x0015BB68: xor r8, qword ptr [rcx + 0x48]
0x0015BB6C: xor r8, qword ptr [rcx + 0xc0]
0x0015BB73: xor r8, qword ptr [rcx + 0x70]
0x0015BB77: mov rbx, qword ptr [rcx + 0x78]
0x0015BB7B: xor rbx, qword ptr [rcx + 0x28]
0x0015BB7F: xor rbx, qword ptr [rcx]
0x0015BB82: xor rbx, qword ptr [rcx + 0xa0]
0x0015BB89: xor rbx, qword ptr [rcx + 0x50]
0x0015BB8D: mov r10, qword ptr [rcx + 0xb0]
0x0015BB94: xor r10, qword ptr [rcx + 0x60]
0x0015BB98: xor r10, qword ptr [rcx + 0x10]
0x0015BB9C: xor r10, qword ptr [rcx + 0x88]
0x0015BBA3: xor r10, qword ptr [rcx + 0x38]
0x0015BBA7: mov r11, qword ptr [rcx + 0xb8]
0x0015BBAE: xor r11, qword ptr [rcx + 0x68]
0x0015BBB2: xor r11, qword ptr [rcx + 0x18]
0x0015BBB6: xor r11, qword ptr [rcx + 0x90]
0x0015BBBD: xor r11, qword ptr [rcx + 0x40]
0x0015BBC1: rol rdx, 1
0x0015BBC4: mov rax, rdx
0x0015BBC7: xor rax, qword ptr [rcx]
0x0015BBCA: xor rax, r8
0x0015BBCD: mov qword ptr [rcx], rax
0x0015BBD0: mov rax, qword ptr [rcx + 0x28]
0x0015BBD4: xor rax, rdx
0x0015BBD7: xor rax, r8
0x0015BBDA: mov qword ptr [rcx + 0x28], rax
0x0015BBDE: mov rax, rdx
0x0015BBE1: xor rax, qword ptr [rcx + 0x50]
0x0015BBE5: xor rax, r8
0x0015BBE8: mov qword ptr [rcx + 0x50], rax
0x0015BBEC: mov rax, qword ptr [rcx + 0x78]
0x0015BBF0: xor rax, rdx
0x0015BBF3: xor rax, r8
0x0015BBF6: mov qword ptr [rcx + 0x78], rax
0x0015BBFA: xor rdx, qword ptr [rcx + 0xa0]
0x0015BC01: xor rdx, r8
0x0015BC04: mov qword ptr [rcx + 0xa0], rdx
0x0015BC0B: mov rdx, r10
0x0015BC0E: rol rdx, 1
0x0015BC11: mov rax, rdx
0x0015BC14: xor rax, qword ptr [rcx + 8]
0x0015BC18: xor rax, rbx
0x0015BC1B: mov qword ptr [rcx + 8], rax
0x0015BC1F: mov rax, rdx
0x0015BC22: xor rax, qword ptr [rcx + 0x30]
0x0015BC26: xor rax, rbx
0x0015BC29: mov qword ptr [rcx + 0x30], rax
0x0015BC2D: mov rax, rdx
0x0015BC30: xor rax, rbx
0x0015BC33: xor qword ptr [rcx + 0x58], rax
0x0015BC37: mov rax, rdx
0x0015BC3A: xor rax, qword ptr [rcx + 0x80]
0x0015BC41: xor rdx, rbx
0x0015BC44: xor rax, rbx
0x0015BC47: mov qword ptr [rcx + 0x80], rax
0x0015BC4E: xor qword ptr [rcx + 0xa8], rdx
0x0015BC55: mov rdx, r11
0x0015BC58: rol rdx, 1
0x0015BC5B: mov rax, rdx
0x0015BC5E: xor rax, qword ptr [rcx + 0x10]
0x0015BC62: xor rax, r9
0x0015BC65: mov qword ptr [rcx + 0x10], rax
0x0015BC69: mov rax, rdx
0x0015BC6C: xor rax, qword ptr [rcx + 0x38]
0x0015BC70: xor rax, r9
0x0015BC73: mov qword ptr [rcx + 0x38], rax
0x0015BC77: mov rax, rdx
0x0015BC7A: xor rax, qword ptr [rcx + 0x60]
0x0015BC7E: xor rax, r9
0x0015BC81: mov qword ptr [rcx + 0x60], rax
0x0015BC85: mov rax, rdx
0x0015BC88: xor rax, qword ptr [rcx + 0x88]
0x0015BC8F: xor rax, r9
0x0015BC92: rol r8, 1
0x0015BC95: mov qword ptr [rcx + 0x88], rax
0x0015BC9C: mov rax, r8
0x0015BC9F: xor rdx, qword ptr [rcx + 0xb0]
0x0015BCA6: xor rax, r10
0x0015BCA9: xor rdx, r9
0x0015BCAC: rol rbx, 1
0x0015BCAF: mov qword ptr [rcx + 0xb0], rdx
0x0015BCB6: xor qword ptr [rcx + 0x18], rax
0x0015BCBA: mov rax, r8
0x0015BCBD: xor rax, r10
0x0015BCC0: xor qword ptr [rcx + 0x40], rax
0x0015BCC4: mov rax, r8
0x0015BCC7: xor rax, qword ptr [rcx + 0x68]
0x0015BCCB: xor rax, r10
0x0015BCCE: mov qword ptr [rcx + 0x68], rax
0x0015BCD2: mov rax, r8
0x0015BCD5: xor rax, r10
0x0015BCD8: xor qword ptr [rcx + 0x90], rax
0x0015BCDF: mov rax, rbx
0x0015BCE2: xor r8, qword ptr [rcx + 0xb8]
0x0015BCE9: xor r8, r10
0x0015BCEC: mov qword ptr [rcx + 0xb8], r8
0x0015BCF3: xor rax, qword ptr [rcx + 0x20]
0x0015BCF7: xor rax, r11
0x0015BCFA: mov qword ptr [rcx + 0x20], rax
0x0015BCFE: mov rax, rbx
0x0015BD01: xor rax, qword ptr [rcx + 0x48]
0x0015BD05: xor rax, r11
0x0015BD08: mov qword ptr [rcx + 0x48], rax
0x0015BD0C: mov rax, rbx
0x0015BD0F: xor rax, qword ptr [rcx + 0x70]
0x0015BD13: xor rax, r11
0x0015BD16: mov qword ptr [rcx + 0x70], rax
0x0015BD1A: mov rax, rbx
0x0015BD1D: xor rax, qword ptr [rcx + 0x98]
0x0015BD24: xor rax, r11
0x0015BD27: mov qword ptr [rcx + 0x98], rax
0x0015BD2E: xor rbx, qword ptr [rcx + 0xc0]
0x0015BD35: xor rbx, r11
0x0015BD38: mov qword ptr [rcx + 0xc0], rbx
0x0015BD3F: mov rax, qword ptr [rcx + 8]
0x0015BD43: mov rdx, qword ptr [rcx + 0x50]
0x0015BD47: rol rax, 1
0x0015BD4A: mov qword ptr [rcx + 0x50], rax
0x0015BD4E: mov rax, qword ptr [rcx + 0x38]
0x0015BD52: rol rdx, 3
0x0015BD56: mov qword ptr [rcx + 0x38], rdx
0x0015BD5A: mov rdx, qword ptr [rcx + 0x58]
0x0015BD5E: rol rax, 6
0x0015BD62: mov qword ptr [rcx + 0x58], rax
0x0015BD66: mov rax, qword ptr [rcx + 0x88]
0x0015BD6D: rol rdx, 0xa
0x0015BD71: mov qword ptr [rcx + 0x88], rdx
0x0015BD78: mov rdx, qword ptr [rcx + 0x90]
0x0015BD7F: rol rax, 0xf
0x0015BD83: mov qword ptr [rcx + 0x90], rax
0x0015BD8A: mov rax, qword ptr [rcx + 0x18]
0x0015BD8E: rol rdx, 0x15
0x0015BD92: mov qword ptr [rcx + 0x18], rdx
0x0015BD96: mov rdx, qword ptr [rcx + 0x28]
0x0015BD9A: rol rax, 0x1c
0x0015BD9E: mov qword ptr [rcx + 0x28], rax
0x0015BDA2: mov rax, qword ptr [rcx + 0x80]
0x0015BDA9: rol rdx, 0x24
0x0015BDAD: mov qword ptr [rcx + 0x80], rdx
0x0015BDB4: mov rdx, qword ptr [rcx + 0x40]
0x0015BDB8: rol rax, 0x2d
0x0015BDBC: mov qword ptr [rcx + 0x40], rax
0x0015BDC0: mov rax, qword ptr [rcx + 0xa8]
0x0015BDC7: rol rdx, 0x37
0x0015BDCB: mov qword ptr [rcx + 0xa8], rdx
0x0015BDD2: mov rdx, qword ptr [rcx + 0xc0]
0x0015BDD9: rol rax, 2
0x0015BDDD: mov qword ptr [rcx + 0xc0], rax
0x0015BDE4: mov rax, qword ptr [rcx + 0x20]
0x0015BDE8: rol rdx, 0xe
0x0015BDEC: mov qword ptr [rcx + 0x20], rdx
0x0015BDF0: mov rdx, qword ptr [rcx + 0x78]
0x0015BDF4: rol rax, 0x1b
0x0015BDF8: mov qword ptr [rcx + 0x78], rax
0x0015BDFC: mov rax, qword ptr [rcx + 0xb8]
0x0015BE03: rol rax, 0x38
0x0015BE07: rol rdx, 0x29
0x0015BE0B: mov qword ptr [rcx + 0xb8], rdx
0x0015BE12: mov rdx, qword ptr [rcx + 0x98]
0x0015BE19: mov qword ptr [rcx + 0x98], rax
0x0015BE20: mov rax, qword ptr [rcx + 0x68]
0x0015BE24: rol rax, 0x19
0x0015BE28: rol rdx, 8
0x0015BE2C: mov qword ptr [rcx + 0x68], rdx
0x0015BE30: mov rdx, qword ptr [rcx + 0x60]
0x0015BE34: mov qword ptr [rcx + 0x60], rax
0x0015BE38: mov rax, qword ptr [rcx + 0x10]
0x0015BE3C: rol rax, 0x3e
0x0015BE40: rol rdx, 0x2b
0x0015BE44: mov qword ptr [rcx + 0x10], rdx
0x0015BE48: mov rdx, qword ptr [rcx + 0xa0]
0x0015BE4F: mov qword ptr [rcx + 0xa0], rax
0x0015BE56: mov rax, qword ptr [rcx + 0x70]
0x0015BE5A: rol rax, 0x27
0x0015BE5E: rol rdx, 0x12
0x0015BE62: mov qword ptr [rcx + 0x70], rdx
0x0015BE66: mov rdx, qword ptr [rcx + 0xb0]
0x0015BE6D: mov qword ptr [rcx + 0xb0], rax
0x0015BE74: mov rax, qword ptr [rcx + 0x48]
0x0015BE78: rol rax, 0x14
0x0015BE7C: rol rdx, 0x3d
0x0015BE80: mov qword ptr [rcx + 0x48], rdx
0x0015BE84: mov r11, qword ptr [rcx + 0x30]
0x0015BE88: mov qword ptr [rcx + 0x30], rax
0x0015BE8C: rol r11, 0x2c
0x0015BE90: mov qword ptr [rcx + 8], r11
0x0015BE94: mov rax, r11
0x0015BE97: mov rdx, qword ptr [rcx + 0x10]
0x0015BE9B: not rax
0x0015BE9E: mov r8, qword ptr [rcx + 0x18]
0x0015BEA2: and rax, rdx
0x0015BEA5: mov r9, qword ptr [rcx + 0x20]
0x0015BEA9: mov r10, qword ptr [rcx]
0x0015BEAC: xor rax, r10
0x0015BEAF: mov qword ptr [rcx], rax
0x0015BEB2: mov rax, rdx
0x0015BEB5: not rax
0x0015BEB8: and rax, r8
0x0015BEBB: xor rax, r11
0x0015BEBE: mov qword ptr [rcx + 8], rax
0x0015BEC2: mov rax, r8
0x0015BEC5: not rax
0x0015BEC8: and rax, r9
0x0015BECB: xor rax, rdx
0x0015BECE: mov qword ptr [rcx + 0x10], rax
0x0015BED2: mov rax, r9
0x0015BED5: not rax
0x0015BED8: and rax, r10
0x0015BEDB: not r10
0x0015BEDE: xor rax, r8
0x0015BEE1: and r10, r11
0x0015BEE4: mov qword ptr [rcx + 0x18], rax
0x0015BEE8: xor r10, r9
0x0015BEEB: mov qword ptr [rcx + 0x20], r10
0x0015BEEF: mov rdx, qword ptr [rcx + 0x38]
0x0015BEF3: mov r10, qword ptr [rcx + 0x30]
0x0015BEF7: mov r8, qword ptr [rcx + 0x40]
0x0015BEFB: mov rax, r10
0x0015BEFE: mov r11, qword ptr [rcx + 0x28]
0x0015BF02: not rax
0x0015BF05: mov r9, qword ptr [rcx + 0x48]
0x0015BF09: and rax, rdx
0x0015BF0C: xor rax, r11
0x0015BF0F: mov qword ptr [rcx + 0x28], rax
0x0015BF13: mov rax, rdx
0x0015BF16: not rax
0x0015BF19: and rax, r8
0x0015BF1C: xor rax, r10
0x0015BF1F: mov qword ptr [rcx + 0x30], rax
0x0015BF23: mov rax, r8
0x0015BF26: not rax
0x0015BF29: and rax, r9
0x0015BF2C: xor rax, rdx
0x0015BF2F: mov qword ptr [rcx + 0x38], rax
0x0015BF33: mov rax, r9
0x0015BF36: not rax
0x0015BF39: and rax, r11
0x0015BF3C: not r11
0x0015BF3F: xor rax, r8
0x0015BF42: and r11, r10
0x0015BF45: mov qword ptr [rcx + 0x40], rax
0x0015BF49: xor r11, r9
0x0015BF4C: mov qword ptr [rcx + 0x48], r11
0x0015BF50: mov r10, qword ptr [rcx + 0x58]
0x0015BF54: mov rdx, qword ptr [rcx + 0x60]
0x0015BF58: mov rax, r10
0x0015BF5B: mov r8, qword ptr [rcx + 0x68]
0x0015BF5F: not rax
0x0015BF62: mov r9, qword ptr [rcx + 0x70]
0x0015BF66: and rax, rdx
0x0015BF69: mov r11, qword ptr [rcx + 0x50]
0x0015BF6D: xor rax, r11
0x0015BF70: mov qword ptr [rcx + 0x50], rax
0x0015BF74: mov rax, rdx
0x0015BF77: not rax
0x0015BF7A: and rax, r8
0x0015BF7D: xor rax, r10
0x0015BF80: mov qword ptr [rcx + 0x58], rax
0x0015BF84: mov rax, r8
0x0015BF87: not rax
0x0015BF8A: and rax, r9
0x0015BF8D: xor rax, rdx
0x0015BF90: mov qword ptr [rcx + 0x60], rax
0x0015BF94: mov rax, r9
0x0015BF97: not rax
0x0015BF9A: and rax, r11
0x0015BF9D: not r11
0x0015BFA0: xor rax, r8
0x0015BFA3: and r11, r10
0x0015BFA6: mov qword ptr [rcx + 0x68], rax
0x0015BFAA: xor r11, r9
0x0015BFAD: mov qword ptr [rcx + 0x70], r11
0x0015BFB1: mov r10, qword ptr [rcx + 0x80]
0x0015BFB8: mov rdx, qword ptr [rcx + 0x88]
0x0015BFBF: mov rax, r10
0x0015BFC2: mov r8, qword ptr [rcx + 0x90]
0x0015BFC9: not rax
0x0015BFCC: mov r9, qword ptr [rcx + 0x98]
0x0015BFD3: and rax, rdx
0x0015BFD6: mov r11, qword ptr [rcx + 0x78]
0x0015BFDA: xor rax, r11
0x0015BFDD: mov qword ptr [rcx + 0x78], rax
0x0015BFE1: mov rax, rdx
0x0015BFE4: not rax
0x0015BFE7: and rax, r8
0x0015BFEA: xor rax, r10
0x0015BFED: mov qword ptr [rcx + 0x80], rax
0x0015BFF4: mov rax, r8
0x0015BFF7: not rax
0x0015BFFA: and rax, r9
0x0015BFFD: xor rax, rdx
0x0015C000: mov qword ptr [rcx + 0x88], rax
0x0015C007: mov rax, r9
0x0015C00A: not rax
0x0015C00D: and rax, r11
0x0015C010: not r11
0x0015C013: xor rax, r8
0x0015C016: and r11, r10
0x0015C019: mov qword ptr [rcx + 0x90], rax
0x0015C020: xor r11, r9
0x0015C023: mov qword ptr [rcx + 0x98], r11
0x0015C02A: mov r10, qword ptr [rcx + 0xa8]
0x0015C031: mov rdx, qword ptr [rcx + 0xb0]
0x0015C038: mov rax, r10
0x0015C03B: mov r11, qword ptr [rcx + 0xa0]
0x0015C042: not rax
0x0015C045: mov r8, qword ptr [rcx + 0xb8]
0x0015C04C: and rax, rdx
0x0015C04F: mov r9, qword ptr [rcx + 0xc0]
0x0015C056: xor rax, r11
0x0015C059: mov qword ptr [rcx + 0xa0], rax
0x0015C060: mov rax, rdx
0x0015C063: not rax
0x0015C066: and rax, r8
0x0015C069: xor rax, r10
0x0015C06C: mov qword ptr [rcx + 0xa8], rax
0x0015C073: mov rax, r8
0x0015C076: not rax
0x0015C079: and rax, r9
0x0015C07C: xor rax, rdx
0x0015C07F: mov qword ptr [rcx + 0xb0], rax
0x0015C086: mov rax, r9
0x0015C089: not rax
0x0015C08C: and rax, r11
0x0015C08F: not r11
0x0015C092: xor rax, r8
0x0015C095: and r11, r10
0x0015C098: mov qword ptr [rcx + 0xb8], rax
0x0015C09F: xor r11, r9
0x0015C0A2: mov rax, qword ptr [rdi]
0x0015C0A5: add rdi, 8
0x0015C0A9: mov qword ptr [rcx + 0xc0], r11
0x0015C0B0: xor qword ptr [rcx], rax
0x0015C0B3: cmp rdi, rsi
0x0015C0B6: jl 0x14015bb40
0x0015C0BC: mov rbx, qword ptr [rsp + 0x10]
0x0015C0C1: mov rsi, qword ptr [rsp + 0x18]
0x0015C0C6: mov rdi, qword ptr [rsp + 0x20]
0x0015C0CB: ret
```

## `0x002284F0` PDATA `0x002284F0..0x00228A9C`

direct callers: `3`

- `0x0022843C` from `0x00228310..0x002284E4`
- `0x00228476` from `0x00228310..0x002284E4`
- `0x0022849A` from `0x00228310..0x002284E4`

### Calls

| RVA | target |
|---|---|

### Full body

```asm
0x002284F0: mov qword ptr [rsp + 0x10], rbx
0x002284F5: mov qword ptr [rsp + 0x18], rsi
0x002284FA: mov qword ptr [rsp + 0x20], rdi
0x002284FF: lea rdi, [rip + 0x49abfa]
0x00228506: lea rsi, [rip + 0x49acb3]
0x0022850D: nop dword ptr [rax]
0x00228510: mov r9, qword ptr [rcx + 8]
0x00228514: xor r9, qword ptr [rcx + 0x80]
0x0022851B: xor r9, qword ptr [rcx + 0x30]
0x0022851F: xor r9, qword ptr [rcx + 0xa8]
0x00228526: xor r9, qword ptr [rcx + 0x58]
0x0022852A: mov r8, qword ptr [rcx + 0x20]
0x0022852E: mov rdx, r9
0x00228531: xor r8, qword ptr [rcx + 0x98]
0x00228538: xor r8, qword ptr [rcx + 0x48]
0x0022853C: xor r8, qword ptr [rcx + 0xc0]
0x00228543: xor r8, qword ptr [rcx + 0x70]
0x00228547: mov rbx, qword ptr [rcx + 0x78]
0x0022854B: xor rbx, qword ptr [rcx + 0x28]
0x0022854F: xor rbx, qword ptr [rcx]
0x00228552: xor rbx, qword ptr [rcx + 0xa0]
0x00228559: xor rbx, qword ptr [rcx + 0x50]
0x0022855D: mov r10, qword ptr [rcx + 0xb0]
0x00228564: xor r10, qword ptr [rcx + 0x60]
0x00228568: xor r10, qword ptr [rcx + 0x10]
0x0022856C: xor r10, qword ptr [rcx + 0x88]
0x00228573: xor r10, qword ptr [rcx + 0x38]
0x00228577: mov r11, qword ptr [rcx + 0xb8]
0x0022857E: xor r11, qword ptr [rcx + 0x68]
0x00228582: xor r11, qword ptr [rcx + 0x18]
0x00228586: xor r11, qword ptr [rcx + 0x90]
0x0022858D: xor r11, qword ptr [rcx + 0x40]
0x00228591: rol rdx, 1
0x00228594: mov rax, rdx
0x00228597: xor rax, qword ptr [rcx]
0x0022859A: xor rax, r8
0x0022859D: mov qword ptr [rcx], rax
0x002285A0: mov rax, qword ptr [rcx + 0x28]
0x002285A4: xor rax, rdx
0x002285A7: xor rax, r8
0x002285AA: mov qword ptr [rcx + 0x28], rax
0x002285AE: mov rax, rdx
0x002285B1: xor rax, qword ptr [rcx + 0x50]
0x002285B5: xor rax, r8
0x002285B8: mov qword ptr [rcx + 0x50], rax
0x002285BC: mov rax, qword ptr [rcx + 0x78]
0x002285C0: xor rax, rdx
0x002285C3: xor rax, r8
0x002285C6: mov qword ptr [rcx + 0x78], rax
0x002285CA: xor rdx, qword ptr [rcx + 0xa0]
0x002285D1: xor rdx, r8
0x002285D4: mov qword ptr [rcx + 0xa0], rdx
0x002285DB: mov rdx, r10
0x002285DE: rol rdx, 1
0x002285E1: mov rax, rdx
0x002285E4: xor rax, qword ptr [rcx + 8]
0x002285E8: xor rax, rbx
0x002285EB: mov qword ptr [rcx + 8], rax
0x002285EF: mov rax, rdx
0x002285F2: xor rax, qword ptr [rcx + 0x30]
0x002285F6: xor rax, rbx
0x002285F9: mov qword ptr [rcx + 0x30], rax
0x002285FD: mov rax, rdx
0x00228600: xor rax, rbx
0x00228603: xor qword ptr [rcx + 0x58], rax
0x00228607: mov rax, rdx
0x0022860A: xor rax, qword ptr [rcx + 0x80]
0x00228611: xor rdx, rbx
0x00228614: xor rax, rbx
0x00228617: mov qword ptr [rcx + 0x80], rax
0x0022861E: xor qword ptr [rcx + 0xa8], rdx
0x00228625: mov rdx, r11
0x00228628: rol rdx, 1
0x0022862B: mov rax, rdx
0x0022862E: xor rax, qword ptr [rcx + 0x10]
0x00228632: xor rax, r9
0x00228635: mov qword ptr [rcx + 0x10], rax
0x00228639: mov rax, rdx
0x0022863C: xor rax, qword ptr [rcx + 0x38]
0x00228640: xor rax, r9
0x00228643: mov qword ptr [rcx + 0x38], rax
0x00228647: mov rax, rdx
0x0022864A: xor rax, qword ptr [rcx + 0x60]
0x0022864E: xor rax, r9
0x00228651: mov qword ptr [rcx + 0x60], rax
0x00228655: mov rax, rdx
0x00228658: xor rax, qword ptr [rcx + 0x88]
0x0022865F: xor rax, r9
0x00228662: rol r8, 1
0x00228665: mov qword ptr [rcx + 0x88], rax
0x0022866C: mov rax, r8
0x0022866F: xor rdx, qword ptr [rcx + 0xb0]
0x00228676: xor rax, r10
0x00228679: xor rdx, r9
0x0022867C: rol rbx, 1
0x0022867F: mov qword ptr [rcx + 0xb0], rdx
0x00228686: xor qword ptr [rcx + 0x18], rax
0x0022868A: mov rax, r8
0x0022868D: xor rax, r10
0x00228690: xor qword ptr [rcx + 0x40], rax
0x00228694: mov rax, r8
0x00228697: xor rax, qword ptr [rcx + 0x68]
0x0022869B: xor rax, r10
0x0022869E: mov qword ptr [rcx + 0x68], rax
0x002286A2: mov rax, r8
0x002286A5: xor rax, r10
0x002286A8: xor qword ptr [rcx + 0x90], rax
0x002286AF: mov rax, rbx
0x002286B2: xor r8, qword ptr [rcx + 0xb8]
0x002286B9: xor r8, r10
0x002286BC: mov qword ptr [rcx + 0xb8], r8
0x002286C3: xor rax, qword ptr [rcx + 0x20]
0x002286C7: xor rax, r11
0x002286CA: mov qword ptr [rcx + 0x20], rax
0x002286CE: mov rax, rbx
0x002286D1: xor rax, qword ptr [rcx + 0x48]
0x002286D5: xor rax, r11
0x002286D8: mov qword ptr [rcx + 0x48], rax
0x002286DC: mov rax, rbx
0x002286DF: xor rax, qword ptr [rcx + 0x70]
0x002286E3: xor rax, r11
0x002286E6: mov qword ptr [rcx + 0x70], rax
0x002286EA: mov rax, rbx
0x002286ED: xor rax, qword ptr [rcx + 0x98]
0x002286F4: xor rax, r11
0x002286F7: mov qword ptr [rcx + 0x98], rax
0x002286FE: xor rbx, qword ptr [rcx + 0xc0]
0x00228705: xor rbx, r11
0x00228708: mov qword ptr [rcx + 0xc0], rbx
0x0022870F: mov rax, qword ptr [rcx + 8]
0x00228713: mov rdx, qword ptr [rcx + 0x50]
0x00228717: rol rax, 1
0x0022871A: mov qword ptr [rcx + 0x50], rax
0x0022871E: mov rax, qword ptr [rcx + 0x38]
0x00228722: rol rdx, 3
0x00228726: mov qword ptr [rcx + 0x38], rdx
0x0022872A: mov rdx, qword ptr [rcx + 0x58]
0x0022872E: rol rax, 6
0x00228732: mov qword ptr [rcx + 0x58], rax
0x00228736: mov rax, qword ptr [rcx + 0x88]
0x0022873D: rol rdx, 0xa
0x00228741: mov qword ptr [rcx + 0x88], rdx
0x00228748: mov rdx, qword ptr [rcx + 0x90]
0x0022874F: rol rax, 0xf
0x00228753: mov qword ptr [rcx + 0x90], rax
0x0022875A: mov rax, qword ptr [rcx + 0x18]
0x0022875E: rol rdx, 0x15
0x00228762: mov qword ptr [rcx + 0x18], rdx
0x00228766: mov rdx, qword ptr [rcx + 0x28]
0x0022876A: rol rax, 0x1c
0x0022876E: mov qword ptr [rcx + 0x28], rax
0x00228772: mov rax, qword ptr [rcx + 0x80]
0x00228779: rol rdx, 0x24
0x0022877D: mov qword ptr [rcx + 0x80], rdx
0x00228784: mov rdx, qword ptr [rcx + 0x40]
0x00228788: rol rax, 0x2d
0x0022878C: mov qword ptr [rcx + 0x40], rax
0x00228790: mov rax, qword ptr [rcx + 0xa8]
0x00228797: rol rdx, 0x37
0x0022879B: mov qword ptr [rcx + 0xa8], rdx
0x002287A2: mov rdx, qword ptr [rcx + 0xc0]
0x002287A9: rol rax, 2
0x002287AD: mov qword ptr [rcx + 0xc0], rax
0x002287B4: mov rax, qword ptr [rcx + 0x20]
0x002287B8: rol rdx, 0xe
0x002287BC: mov qword ptr [rcx + 0x20], rdx
0x002287C0: mov rdx, qword ptr [rcx + 0x78]
0x002287C4: rol rax, 0x1b
0x002287C8: mov qword ptr [rcx + 0x78], rax
0x002287CC: mov rax, qword ptr [rcx + 0xb8]
0x002287D3: rol rax, 0x38
0x002287D7: rol rdx, 0x29
0x002287DB: mov qword ptr [rcx + 0xb8], rdx
0x002287E2: mov rdx, qword ptr [rcx + 0x98]
0x002287E9: mov qword ptr [rcx + 0x98], rax
0x002287F0: mov rax, qword ptr [rcx + 0x68]
0x002287F4: rol rax, 0x19
0x002287F8: rol rdx, 8
0x002287FC: mov qword ptr [rcx + 0x68], rdx
0x00228800: mov rdx, qword ptr [rcx + 0x60]
0x00228804: mov qword ptr [rcx + 0x60], rax
0x00228808: mov rax, qword ptr [rcx + 0x10]
0x0022880C: rol rax, 0x3e
0x00228810: rol rdx, 0x2b
0x00228814: mov qword ptr [rcx + 0x10], rdx
0x00228818: mov rdx, qword ptr [rcx + 0xa0]
0x0022881F: mov qword ptr [rcx + 0xa0], rax
0x00228826: mov rax, qword ptr [rcx + 0x70]
0x0022882A: rol rax, 0x27
0x0022882E: rol rdx, 0x12
0x00228832: mov qword ptr [rcx + 0x70], rdx
0x00228836: mov rdx, qword ptr [rcx + 0xb0]
0x0022883D: mov qword ptr [rcx + 0xb0], rax
0x00228844: mov rax, qword ptr [rcx + 0x48]
0x00228848: rol rax, 0x14
0x0022884C: rol rdx, 0x3d
0x00228850: mov qword ptr [rcx + 0x48], rdx
0x00228854: mov r11, qword ptr [rcx + 0x30]
0x00228858: mov qword ptr [rcx + 0x30], rax
0x0022885C: rol r11, 0x2c
0x00228860: mov qword ptr [rcx + 8], r11
0x00228864: mov rax, r11
0x00228867: mov rdx, qword ptr [rcx + 0x10]
0x0022886B: not rax
0x0022886E: mov r8, qword ptr [rcx + 0x18]
0x00228872: and rax, rdx
0x00228875: mov r9, qword ptr [rcx + 0x20]
0x00228879: mov r10, qword ptr [rcx]
0x0022887C: xor rax, r10
0x0022887F: mov qword ptr [rcx], rax
0x00228882: mov rax, rdx
0x00228885: not rax
0x00228888: and rax, r8
0x0022888B: xor rax, r11
0x0022888E: mov qword ptr [rcx + 8], rax
0x00228892: mov rax, r8
0x00228895: not rax
0x00228898: and rax, r9
0x0022889B: xor rax, rdx
0x0022889E: mov qword ptr [rcx + 0x10], rax
0x002288A2: mov rax, r9
0x002288A5: not rax
0x002288A8: and rax, r10
0x002288AB: not r10
0x002288AE: xor rax, r8
0x002288B1: and r10, r11
0x002288B4: mov qword ptr [rcx + 0x18], rax
0x002288B8: xor r10, r9
0x002288BB: mov qword ptr [rcx + 0x20], r10
0x002288BF: mov rdx, qword ptr [rcx + 0x38]
0x002288C3: mov r10, qword ptr [rcx + 0x30]
0x002288C7: mov r8, qword ptr [rcx + 0x40]
0x002288CB: mov rax, r10
0x002288CE: mov r11, qword ptr [rcx + 0x28]
0x002288D2: not rax
0x002288D5: mov r9, qword ptr [rcx + 0x48]
0x002288D9: and rax, rdx
0x002288DC: xor rax, r11
0x002288DF: mov qword ptr [rcx + 0x28], rax
0x002288E3: mov rax, rdx
0x002288E6: not rax
0x002288E9: and rax, r8
0x002288EC: xor rax, r10
0x002288EF: mov qword ptr [rcx + 0x30], rax
0x002288F3: mov rax, r8
0x002288F6: not rax
0x002288F9: and rax, r9
0x002288FC: xor rax, rdx
0x002288FF: mov qword ptr [rcx + 0x38], rax
0x00228903: mov rax, r9
0x00228906: not rax
0x00228909: and rax, r11
0x0022890C: not r11
0x0022890F: xor rax, r8
0x00228912: and r11, r10
0x00228915: mov qword ptr [rcx + 0x40], rax
0x00228919: xor r11, r9
0x0022891C: mov qword ptr [rcx + 0x48], r11
0x00228920: mov r10, qword ptr [rcx + 0x58]
0x00228924: mov rdx, qword ptr [rcx + 0x60]
0x00228928: mov rax, r10
0x0022892B: mov r8, qword ptr [rcx + 0x68]
0x0022892F: not rax
0x00228932: mov r9, qword ptr [rcx + 0x70]
0x00228936: and rax, rdx
0x00228939: mov r11, qword ptr [rcx + 0x50]
0x0022893D: xor rax, r11
0x00228940: mov qword ptr [rcx + 0x50], rax
0x00228944: mov rax, rdx
0x00228947: not rax
0x0022894A: and rax, r8
0x0022894D: xor rax, r10
0x00228950: mov qword ptr [rcx + 0x58], rax
0x00228954: mov rax, r8
0x00228957: not rax
0x0022895A: and rax, r9
0x0022895D: xor rax, rdx
0x00228960: mov qword ptr [rcx + 0x60], rax
0x00228964: mov rax, r9
0x00228967: not rax
0x0022896A: and rax, r11
0x0022896D: not r11
0x00228970: xor rax, r8
0x00228973: and r11, r10
0x00228976: mov qword ptr [rcx + 0x68], rax
0x0022897A: xor r11, r9
0x0022897D: mov qword ptr [rcx + 0x70], r11
0x00228981: mov r10, qword ptr [rcx + 0x80]
0x00228988: mov rdx, qword ptr [rcx + 0x88]
0x0022898F: mov rax, r10
0x00228992: mov r8, qword ptr [rcx + 0x90]
0x00228999: not rax
0x0022899C: mov r9, qword ptr [rcx + 0x98]
0x002289A3: and rax, rdx
0x002289A6: mov r11, qword ptr [rcx + 0x78]
0x002289AA: xor rax, r11
0x002289AD: mov qword ptr [rcx + 0x78], rax
0x002289B1: mov rax, rdx
0x002289B4: not rax
0x002289B7: and rax, r8
0x002289BA: xor rax, r10
0x002289BD: mov qword ptr [rcx + 0x80], rax
0x002289C4: mov rax, r8
0x002289C7: not rax
0x002289CA: and rax, r9
0x002289CD: xor rax, rdx
0x002289D0: mov qword ptr [rcx + 0x88], rax
0x002289D7: mov rax, r9
0x002289DA: not rax
0x002289DD: and rax, r11
0x002289E0: not r11
0x002289E3: xor rax, r8
0x002289E6: and r11, r10
0x002289E9: mov qword ptr [rcx + 0x90], rax
0x002289F0: xor r11, r9
0x002289F3: mov qword ptr [rcx + 0x98], r11
0x002289FA: mov r10, qword ptr [rcx + 0xa8]
0x00228A01: mov rdx, qword ptr [rcx + 0xb0]
0x00228A08: mov rax, r10
0x00228A0B: mov r11, qword ptr [rcx + 0xa0]
0x00228A12: not rax
0x00228A15: mov r8, qword ptr [rcx + 0xb8]
0x00228A1C: and rax, rdx
0x00228A1F: mov r9, qword ptr [rcx + 0xc0]
0x00228A26: xor rax, r11
0x00228A29: mov qword ptr [rcx + 0xa0], rax
0x00228A30: mov rax, rdx
0x00228A33: not rax
0x00228A36: and rax, r8
0x00228A39: xor rax, r10
0x00228A3C: mov qword ptr [rcx + 0xa8], rax
0x00228A43: mov rax, r8
0x00228A46: not rax
0x00228A49: and rax, r9
0x00228A4C: xor rax, rdx
0x00228A4F: mov qword ptr [rcx + 0xb0], rax
0x00228A56: mov rax, r9
0x00228A59: not rax
0x00228A5C: and rax, r11
0x00228A5F: not r11
0x00228A62: xor rax, r8
0x00228A65: and r11, r10
0x00228A68: mov qword ptr [rcx + 0xb8], rax
0x00228A6F: xor r11, r9
0x00228A72: mov rax, qword ptr [rdi]
0x00228A75: add rdi, 8
0x00228A79: mov qword ptr [rcx + 0xc0], r11
0x00228A80: xor qword ptr [rcx], rax
0x00228A83: cmp rdi, rsi
0x00228A86: jl 0x140228510
0x00228A8C: mov rbx, qword ptr [rsp + 0x10]
0x00228A91: mov rsi, qword ptr [rsp + 0x18]
0x00228A96: mov rdi, qword ptr [rsp + 0x20]
0x00228A9B: ret
```
