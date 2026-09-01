# Type2 config -> NVIDIA child bridge 0x1305F0

Full Capstone decode. Entry obtains child through parent slot +0x90 and builds a local config snapshot via 0x06A320.

```asm
0x001305F0: mov qword ptr [rsp + 0x10], rbx
0x001305F5: mov qword ptr [rsp + 0x18], rsi
0x001305FA: mov qword ptr [rsp + 0x20], rdi
0x001305FF: push rbp
0x00130600: lea rbp, [rsp - 0x110]
0x00130608: sub rsp, 0x210
0x0013060F: mov rax, qword ptr [rip + 0x6a62da]
0x00130616: xor rax, rsp
0x00130619: mov qword ptr [rbp + 0x100], rax
0x00130620: mov rax, qword ptr [rcx]
0x00130623: mov esi, edx
0x00130625: mov rbx, rcx
0x00130628: call qword ptr [rax + 0x90]
0x0013062E: mov rdi, rax
0x00130631: test rax, rax
0x00130634: je 0x1401309b1
0x0013063A: lea rdx, [rbp + 0x20]
0x0013063E: mov rcx, rbx
0x00130641: call 0x14006a320
0x00130646: cmp esi, 1
0x00130649: ja 0x140130705
0x0013064F: mov edx, dword ptr [rbp + 0xb8]
0x00130655: test edx, edx
0x00130657: js 0x14013066c
0x00130659: mov r8, qword ptr [rdi]
0x0013065C: mov rcx, rdi
0x0013065F: call qword ptr [r8 + 0x38]
0x00130663: mov byte ptr [rbx + 0x544], 1
0x0013066A: jmp 0x140130687
0x0013066C: cmp byte ptr [rbx + 0x544], 0
0x00130673: je 0x140130687
0x00130675: mov rax, qword ptr [rdi]
0x00130678: xor edx, edx
0x0013067A: mov rcx, rdi
0x0013067D: call qword ptr [rax + 0x38]
0x00130680: mov byte ptr [rbx + 0x544], 0
0x00130687: mov edx, dword ptr [rbp + 0xcc]
0x0013068D: mov r8d, dword ptr [rbp + 0xd0]
0x00130694: test edx, edx
0x00130696: jg 0x1401306ef
0x00130698: test r8d, r8d
0x0013069B: jne 0x1401306ef
0x0013069D: mov eax, dword ptr [rbx + 0x98]
0x001306A3: imul rcx, rax, 0xa8
0x001306AA: mov rax, qword ptr [rip + 0x6b5d57]
0x001306B1: cmp dword ptr [rcx + rax + 0xc], 2
0x001306B6: jne 0x1401306d5
0x001306B8: lea rax, [rbp + 0xd4]
0x001306BF: nop
0x001306C0: cmp dword ptr [rax], 0
0x001306C3: jne 0x1401306ef
0x001306C5: add rax, 4
0x001306C9: lea rcx, [rbp + 0xe0]
0x001306D0: cmp rax, rcx
0x001306D3: jne 0x1401306c0
0x001306D5: cmp byte ptr [rbx + 0x545], 0
0x001306DC: je 0x140130705
0x001306DE: mov rcx, rdi
0x001306E1: call 0x14014b9d0
0x001306E6: mov byte ptr [rbx + 0x545], 0
0x001306ED: jmp 0x140130705
0x001306EF: lea r9, [rbp + 0xd4]
0x001306F6: mov rcx, rdi
0x001306F9: call 0x14014ba60
0x001306FE: mov byte ptr [rbx + 0x545], 1
0x00130705: test esi, 0xfffffffd
0x0013070B: jne 0x1401309b1
0x00130711: movzx ecx, byte ptr [rbx + 0x53f]
0x00130718: test cl, cl
0x0013071A: setne al
0x0013071D: cmp al, byte ptr [rbx + 0x546]
0x00130723: je 0x140130739
0x00130725: test cl, cl
0x00130727: mov byte ptr [rbx + 0x546], al
0x0013072D: mov rax, qword ptr [rdi]
0x00130730: mov rcx, rdi
0x00130733: sete dl
0x00130736: call qword ptr [rax + 0x48]
0x00130739: mov edx, dword ptr [rbp + 0x68]
0x0013073C: test edx, edx
0x0013073E: js 0x140130761
0x00130740: mov eax, dword ptr [rbp + 0x5c]
0x00130743: mov rcx, rdi
0x00130746: mov r8d, dword ptr [rbp + 0x98]
0x0013074D: test eax, eax
0x0013074F: mov r9d, dword ptr [rbp + 0xb0]
0x00130756: cmovg r8d, eax
0x0013075A: call 0x14014ba30
0x0013075F: jmp 0x1401307be
0x00130761: mov edx, dword ptr [rbp + 0x5c]
0x00130764: mov r9d, dword ptr [rbp + 0x64]
0x00130768: mov r8d, dword ptr [rbp + 0x60]
0x0013076C: test edx, edx
0x0013076E: jg 0x140130794
0x00130770: test r8d, r8d
0x00130773: jg 0x140130794
0x00130775: test r9d, r9d
0x00130778: jg 0x140130794
0x0013077A: cmp byte ptr [rbx + 0x540], 0
0x00130781: je 0x1401307c5
0x00130783: mov rcx, rdi
0x00130786: call 0x14014b9b0
0x0013078B: mov byte ptr [rbx + 0x540], 0
0x00130792: jmp 0x1401307c5
0x00130794: mov eax, dword ptr [rbp + 0xb0]
0x0013079A: mov rcx, rdi
0x0013079D: mov dword ptr [rsp + 0x38], eax
0x001307A1: mov eax, dword ptr [rbp + 0x98]
0x001307A7: mov dword ptr [rsp + 0x30], eax
0x001307AB: mov eax, dword ptr [rbp + 0x70]
0x001307AE: mov dword ptr [rsp + 0x28], eax
0x001307B2: mov eax, dword ptr [rbp + 0x6c]
0x001307B5: mov dword ptr [rsp + 0x20], eax
0x001307B9: call 0x14014b9f0
0x001307BE: mov byte ptr [rbx + 0x540], 1
0x001307C5: mov edx, dword ptr [rbp + 0x88]
0x001307CB: mov r8d, dword ptr [rbp + 0x98]
0x001307D2: test edx, edx
0x001307D4: jne 0x1401307fc
0x001307D6: test r8d, r8d
0x001307D9: jg 0x1401307fc
0x001307DB: cmp byte ptr [rbx + 0x541], dl
0x001307E1: je 0x1401308b3
0x001307E7: mov rax, qword ptr [rdi]
0x001307EA: mov rcx, rdi
0x001307ED: call qword ptr [rax + 0x18]
0x001307F0: mov byte ptr [rbx + 0x541], 0
0x001307F7: jmp 0x1401308b3
0x001307FC: mov rax, qword ptr [rdi]
0x001307FF: mov rcx, rdi
0x00130802: call qword ptr [rax + 0x10]
0x00130805: cmp dword ptr [rbp + 0x98], 0
0x0013080C: mov byte ptr [rbx + 0x541], 1
0x00130813: jle 0x1401308b3
0x00130819: cmp eax, 2
0x0013081C: jne 0x1401308b3
0x00130822: mov rcx, rbx
0x00130825: call 0x140136510
0x0013082A: lea rdx, [rsp + 0x40]
0x0013082F: mov rcx, rbx
0x00130832: call 0x14006a320
0x00130837: lea rcx, [rbp + 0x20]
0x0013083B: lea rcx, [rcx + 0x80]
0x00130842: movups xmm0, xmmword ptr [rax]
0x00130845: movups xmmword ptr [rcx - 0x80], xmm0
0x00130849: movups xmm1, xmmword ptr [rax + 0x10]
0x0013084D: movups xmmword ptr [rcx - 0x70], xmm1
0x00130851: movups xmm0, xmmword ptr [rax + 0x20]
0x00130855: movups xmmword ptr [rcx - 0x60], xmm0
0x00130859: movups xmm1, xmmword ptr [rax + 0x30]
0x0013085D: movups xmmword ptr [rcx - 0x50], xmm1
0x00130861: movups xmm0, xmmword ptr [rax + 0x40]
0x00130865: movups xmmword ptr [rcx - 0x40], xmm0
0x00130869: movups xmm1, xmmword ptr [rax + 0x50]
0x0013086D: movups xmmword ptr [rcx - 0x30], xmm1
0x00130871: movups xmm0, xmmword ptr [rax + 0x60]
0x00130875: movups xmmword ptr [rcx - 0x20], xmm0
0x00130879: movups xmm0, xmmword ptr [rax + 0x70]
0x0013087D: sub rax, -0x80
0x00130881: movups xmmword ptr [rcx - 0x10], xmm0
0x00130885: movups xmm1, xmmword ptr [rax]
0x00130888: movups xmmword ptr [rcx], xmm1
0x0013088B: movups xmm0, xmmword ptr [rax + 0x10]
0x0013088F: movups xmmword ptr [rcx + 0x10], xmm0
0x00130893: movups xmm1, xmmword ptr [rax + 0x20]
0x00130897: movups xmmword ptr [rcx + 0x20], xmm1
0x0013089B: movups xmm0, xmmword ptr [rax + 0x30]
0x0013089F: movups xmmword ptr [rcx + 0x30], xmm0
0x001308A3: movups xmm1, xmmword ptr [rax + 0x40]
0x001308A7: movups xmmword ptr [rcx + 0x40], xmm1
0x001308AB: mov rax, qword ptr [rax + 0x50]
0x001308AF: mov qword ptr [rcx + 0x50], rax
0x001308B3: mov edx, dword ptr [rbp + 0x78]
0x001308B6: mov ecx, dword ptr [rbp + 0x90]
0x001308BC: mov r9d, dword ptr [rbp + 0x8c]
0x001308C3: mov r8d, dword ptr [rbp + 0x7c]
0x001308C7: test edx, edx
0x001308C9: jg 0x1401308f4
0x001308CB: test r8d, r8d
0x001308CE: jne 0x1401308f4
0x001308D0: test r9d, r9d
0x001308D3: jg 0x1401308f4
0x001308D5: test ecx, ecx
0x001308D7: jne 0x1401308f4
0x001308D9: cmp byte ptr [rbx + 0x542], r8b
0x001308E0: je 0x140130908
0x001308E2: mov rax, qword ptr [rdi]
0x001308E5: mov rcx, rdi
0x001308E8: call qword ptr [rax + 0x28]
0x001308EB: mov byte ptr [rbx + 0x542], 0
0x001308F2: jmp 0x140130908
0x001308F4: mov rax, qword ptr [rdi]
0x001308F7: mov dword ptr [rsp + 0x20], ecx
0x001308FB: mov rcx, rdi
0x001308FE: call qword ptr [rax + 0x20]
0x00130901: mov byte ptr [rbx + 0x542], 1
0x00130908: cmp dword ptr [rbp + 0x80], 0
0x0013090F: jg 0x14013093e
0x00130911: cmp dword ptr [rbp + 0x84], 0
0x00130918: jne 0x14013093e
0x0013091A: cmp dword ptr [rbp + 0x94], 0
0x00130921: jg 0x14013093e
0x00130923: cmp byte ptr [rbx + 0x543], 0
0x0013092A: je 0x140130980
0x0013092C: mov rax, qword ptr [rdi]
0x0013092F: mov rcx, rdi
0x00130932: call qword ptr [rax + 0x40]
0x00130935: mov byte ptr [rbx + 0x543], 0
0x0013093C: jmp 0x140130980
0x0013093E: cmp byte ptr [rbp + 0xe5], 0
0x00130945: je 0x140130956
0x00130947: movzx eax, byte ptr [rbx + 0x9d]
0x0013094E: test al, al
0x00130950: je 0x140130956
0x00130952: mov cl, 1
0x00130954: jmp 0x140130958
0x00130956: xor ecx, ecx
0x00130958: mov rax, qword ptr [rdi]
0x0013095B: mov r9d, dword ptr [rbp + 0x94]
0x00130962: mov r8d, dword ptr [rbp + 0x84]
0x00130969: mov edx, dword ptr [rbp + 0x80]
0x0013096F: mov byte ptr [rsp + 0x20], cl
0x00130973: mov rcx, rdi
0x00130976: call qword ptr [rax + 0x30]
0x00130979: mov byte ptr [rbx + 0x543], 1
0x00130980: cmp dword ptr [rbp + 0x9c], 0
0x00130987: jg 0x1401309a7
0x00130989: cmp dword ptr [rbp + 0xa0], 0
0x00130990: jg 0x1401309a7
0x00130992: cmp dword ptr [rbp + 0xa4], 0
0x00130999: jg 0x1401309a7
0x0013099B: mov dword ptr [rbx + 0x744], 0
0x001309A5: jmp 0x1401309b1
0x001309A7: mov dword ptr [rbx + 0x744], 0x1388
0x001309B1: mov rcx, qword ptr [rbp + 0x100]
0x001309B8: xor rcx, rsp
0x001309BB: call 0x1403b24c0
0x001309C0: lea r11, [rsp + 0x210]
0x001309C8: mov rbx, qword ptr [r11 + 0x18]
0x001309CC: mov rsi, qword ptr [r11 + 0x20]
0x001309D0: mov rdi, qword ptr [r11 + 0x28]
0x001309D4: mov rsp, r11
0x001309D7: pop rbp
0x001309D8: ret
```