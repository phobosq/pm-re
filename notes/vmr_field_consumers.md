# VMR field consumer candidates

confirmed field: stride `0xD8`, offset `+0xB0`; total +0xB0 hits: 1117

| score | RVA | instruction | stride 0xD8 nearby | owner +0x2C0 nearby |
|---:|---|---|---|---|
| 7 | `0x000E10D8` | `mov dword ptr [rdx + rcx + 0xb0], eax` | True | True |
| 7 | `0x000E119B` | `mov dword ptr [rdx + rcx + 0xb0], r9d` | True | True |
| 4 | `0x0003799B` | `lea rcx, [rbp + 0xb0]` | False | True |
| 4 | `0x00078B83` | `mov qword ptr [rsp + 0xb0], 0` | False | True |
| 4 | `0x000B23C1` | `movdqa xmmword ptr [rbp + 0xb0], xmm0` | False | True |
| 4 | `0x000C917D` | `movdqu xmmword ptr [rbp + 0xb0], xmm0` | False | True |
| 4 | `0x000C91A0` | `lea rcx, [rbp + 0xb0]` | False | True |
| 4 | `0x001AD743` | `mov qword ptr [rsp + 0xb0], rax` | False | True |
| 4 | `0x001F90CA` | `mov qword ptr [rbp + 0xb0], rcx` | False | True |
| 4 | `0x0026A7D4` | `lea rdx, [rsp + 0xb0]` | False | True |
| 1 | `0x000017EF` | `lea r11, [rsp + 0xb0]` | False | False |
| 1 | `0x00008379` | `mov rbx, qword ptr [r13 + 0xb0]` | False | False |
| 1 | `0x000084E2` | `mov rbx, qword ptr [r13 + 0xb0]` | False | False |
| 1 | `0x0001790A` | `mov byte ptr [rbp + 0xb0], cl` | False | False |
| 1 | `0x00017910` | `movsx ecx, byte ptr [rbp + 0xb0]` | False | False |
| 1 | `0x0002B0C1` | `lea r11, [rsp + 0xb0]` | False | False |
| 1 | `0x0002B1A1` | `mov rsi, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0002B8C2` | `mov rsi, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0002BCEC` | `mov rdi, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0002E412` | `lea r11, [rsp + 0xb0]` | False | False |
| 1 | `0x00031646` | `mov qword ptr [rsp + 0xb0], r12` | False | False |
| 1 | `0x000316FC` | `mov r12, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x000319F6` | `mov qword ptr [rsp + 0xb0], r12` | False | False |
| 1 | `0x00031AAC` | `mov r12, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00031DC6` | `mov qword ptr [rsp + 0xb0], r12` | False | False |
| 1 | `0x00031E87` | `mov r12, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00032196` | `mov qword ptr [rsp + 0xb0], r12` | False | False |
| 1 | `0x00032257` | `mov r12, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00032556` | `mov qword ptr [rsp + 0xb0], r12` | False | False |
| 1 | `0x0003260C` | `mov r12, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0003418D` | `lea r11, [rsp + 0xb0]` | False | False |
| 1 | `0x00037932` | `mov dword ptr [rbp + 0xb0], 0x3b` | False | False |
| 1 | `0x0003ADFB` | `mov rax, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x0003AE57` | `mov qword ptr [rbp + 0xb0], 0xf` | False | False |
| 1 | `0x0003D02D` | `mov qword ptr [rbp + 0xb0], rsi` | False | False |
| 1 | `0x0003D0EE` | `mov qword ptr [rbp + 0xb0], rsi` | False | False |
| 1 | `0x0003DF0C` | `mov rdx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0003E8C8` | `mov rsi, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0003EB39` | `mov qword ptr [rsp + 0xb0], rdi` | False | False |
| 1 | `0x0003EB70` | `mov rbx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0003F0D8` | `mov r15, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0003FC14` | `mov rax, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00040F6D` | `mov qword ptr [rcx + 0xb0], rax` | False | False |
| 1 | `0x00041DE8` | `lea rdx, [rsp + 0xb0]` | False | False |
| 1 | `0x00043A3F` | `mov rbx, qword ptr [rcx + 0xb0]` | False | False |
| 1 | `0x0004486F` | `lea rbx, [rcx + 0xb0]` | False | False |
| 1 | `0x00044A73` | `lea rcx, [rdi + 0xb0]` | False | False |
| 1 | `0x0004683C` | `mov qword ptr [rsp + 0xb0], rbx` | False | False |
| 1 | `0x0004694E` | `mov rbx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0004706E` | `mov rbx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x000481FC` | `lea rsp, [rbp + 0xb0]` | False | False |
| 1 | `0x00048A66` | `mov qword ptr [rsp + 0xb0], rbx` | False | False |
| 1 | `0x00048C30` | `mov rbx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00049994` | `mov byte ptr [rbp + 0xb0], cl` | False | False |
| 1 | `0x0004999A` | `movsx ecx, byte ptr [rbp + 0xb0]` | False | False |
| 1 | `0x0004B86E` | `mov qword ptr [rbp + 0xb0], rax` | False | False |
| 1 | `0x00050FF2` | `lea rdx, [rsp + 0xb0]` | False | False |
| 1 | `0x00050FFA` | `mov byte ptr [rsp + 0xb0], r15b` | False | False |
| 1 | `0x00053951` | `mov byte ptr [rbp + 0xb0], al` | False | False |
| 1 | `0x00053957` | `movsx ecx, byte ptr [rbp + 0xb0]` | False | False |
| 1 | `0x00054802` | `mov dword ptr [rbp + 0xb0], 0xc` | False | False |
| 1 | `0x0005480C` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x0005492A` | `lea rcx, [rbp + 0xb0]` | False | False |
| 1 | `0x00054B4C` | `lea r11, [rsp + 0xb0]` | False | False |
| 1 | `0x0005ABBA` | `mov byte ptr [rbp + 0xb0], cl` | False | False |
| 1 | `0x0005F5E7` | `lea r11, [rsp + 0xb0]` | False | False |
| 1 | `0x00061492` | `lea r11, [rsp + 0xb0]` | False | False |
| 1 | `0x000628A5` | `mov rax, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00062AFE` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x00062C54` | `mov rax, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x000668B4` | `lea rdx, [rdi + 0xb0]` | False | False |
| 1 | `0x000668BB` | `lea rcx, [rbx + 0xb0]` | False | False |
| 1 | `0x00067E1E` | `lea rbx, [rdi + 0xb0]` | False | False |
| 1 | `0x00069299` | `lea rcx, [rsp + 0xb0]` | False | False |
| 1 | `0x0006D77D` | `mov qword ptr [rbp + 0xb0], rcx` | False | False |
| 1 | `0x0006EB57` | `lea rcx, [rsp + 0xb0]` | False | False |
| 1 | `0x0006F2A9` | `lea rcx, [rsp + 0xb0]` | False | False |
| 1 | `0x0007093C` | `lea rcx, [rsp + 0xb0]` | False | False |
| 1 | `0x000715E9` | `mov qword ptr [rbp + 0xb0], r12` | False | False |
| 1 | `0x000717D8` | `cmp qword ptr [rbp + 0xb0], 0` | False | False |
| 1 | `0x00071834` | `cmp qword ptr [rbp + 0xb0], 0` | False | False |
| 1 | `0x000721B0` | `lea r11, [rsp + 0xb0]` | False | False |
| 1 | `0x00079E7A` | `lea rdx, [rbp + 0xb0]` | False | False |
| 1 | `0x00079F9B` | `mov rcx, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x0007A81B` | `lea rdx, [rbp + 0xb0]` | False | False |
| 1 | `0x0007A865` | `lea rcx, [rbp + 0xb0]` | False | False |
| 1 | `0x0007D895` | `mov byte ptr [rbp + 0xb0], cl` | False | False |
| 1 | `0x0007D89B` | `movsx ecx, byte ptr [rbp + 0xb0]` | False | False |
| 1 | `0x00082797` | `mov dword ptr [rsp + 0xb0], r15d` | False | False |
| 1 | `0x000827B4` | `lea rdx, [rsp + 0xb0]` | False | False |
| 1 | `0x00083625` | `mov ecx, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x00089B69` | `mov r14, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0008A254` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x0008A307` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0008C323` | `mov qword ptr [rbp + 0xb0], rax` | False | False |
| 1 | `0x0008C499` | `mov rcx, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x0008D979` | `mov byte ptr [rsp + 0xb0], al` | False | False |
| 1 | `0x0008D980` | `movsx ecx, byte ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0008F057` | `mov byte ptr [rsp + 0xb0], cl` | False | False |
| 1 | `0x0008F05E` | `movsx ecx, byte ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0008FCF0` | `mov byte ptr [rsp + 0xb0], al` | False | False |
| 1 | `0x0008FCF7` | `movsx ecx, byte ptr [rsp + 0xb0]` | False | False |
| 1 | `0x000915F8` | `mov dword ptr [rsp + 0xb0], r15d` | False | False |
| 1 | `0x000917D6` | `mov dword ptr [rsp + 0xb0], r15d` | False | False |
| 1 | `0x000921FA` | `movdqa xmmword ptr [rbp + 0xb0], xmm0` | False | False |
| 1 | `0x00092202` | `lea rax, [rbp + 0xb0]` | False | False |
| 1 | `0x00092FE2` | `lea rdx, [rsp + 0xb0]` | False | False |
| 1 | `0x00095C05` | `mov qword ptr [rsp + 0xb0], rbx` | False | False |
| 1 | `0x00095D25` | `mov rbx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0009879E` | `lea r11, [rsp + 0xb0]` | False | False |
| 1 | `0x0009AC70` | `mov byte ptr [rdi + 0xb0], 0` | False | False |
| 1 | `0x0009B964` | `mov qword ptr [rdi + 0xb0], r11` | False | False |
| 1 | `0x0009BA06` | `mov dword ptr [rdi + 0xb0], 0` | False | False |
| 1 | `0x0009D8FD` | `lea rcx, [rsp + 0xb0]` | False | False |
| 1 | `0x0009D914` | `lea rcx, [rsp + 0xb0]` | False | False |
| 1 | `0x0009E00F` | `cmp dword ptr [rbx + 0xb0], edi` | False | False |
| 1 | `0x0009E036` | `cmp dword ptr [rbx + 0xb0], edi` | False | False |
| 1 | `0x0009EDA7` | `cmp byte ptr [rdi + 0xb0], 0` | False | False |
| 1 | `0x0009EDC7` | `cmp byte ptr [rdi + 0xb0], 0` | False | False |
| 1 | `0x0009FB6E` | `mov dword ptr [rsp + 0xb0], esi` | False | False |
| 1 | `0x000A0248` | `mov byte ptr [rdi + 0xb0], 1` | False | False |
| 1 | `0x000A1822` | `mov qword ptr [rsp + 0xb0], rbx` | False | False |
| 1 | `0x000A1913` | `mov rbx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x000A1A82` | `cmp dword ptr [rdi + 0xb0], esi` | False | False |
| 1 | `0x000A1A8A` | `mov dword ptr [rdi + 0xb0], esi` | False | False |
| 1 | `0x000A28B8` | `mov qword ptr [rbp + 0xb0], rdx` | False | False |
| 1 | `0x000A444D` | `mov r13, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x000A4CCC` | `mov dword ptr [rbp + 0xb0], eax` | False | False |
| 1 | `0x000A4CDF` | `lea rcx, [rbp + 0xb0]` | False | False |
| 1 | `0x000A83E4` | `mov qword ptr [rsp + 0xb0], rbx` | False | False |
| 1 | `0x000A862D` | `mov rbx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x000A8CCA` | `lea rdx, [rsi + 0xb0]` | False | False |
| 1 | `0x000AB6C2` | `mov byte ptr [rbp + 0xb0], cl` | False | False |
| 1 | `0x000AB6C8` | `movsx ecx, byte ptr [rbp + 0xb0]` | False | False |
| 1 | `0x000ABA44` | `movzx eax, byte ptr [rbp + 0xb0]` | False | False |
| 1 | `0x000AD511` | `mov qword ptr [rsp + 0xb0], rbx` | False | False |
| 1 | `0x000AE8D0` | `lea r11, [rsp + 0xb0]` | False | False |
| 1 | `0x000AF496` | `mov byte ptr [rbp + 0xb0], cl` | False | False |
| 1 | `0x000AF49C` | `movsx ecx, byte ptr [rbp + 0xb0]` | False | False |
| 1 | `0x000B1279` | `mov rax, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x000B1D8B` | `lea rdx, [rbp + 0xb0]` | False | False |
| 1 | `0x000B1DC1` | `mov rcx, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x000B4DD9` | `lea r8, [rsp + 0xb0]` | False | False |
| 1 | `0x000B652F` | `mov rdx, qword ptr [rbx + 0xb0]` | False | False |
| 1 | `0x000B7233` | `mov qword ptr [rbx + 0xb0], rdx` | False | False |
| 1 | `0x000B7B75` | `mov eax, dword ptr [rbx + 0xb0]` | False | False |
| 1 | `0x000B7B80` | `mov dword ptr [rdi + 0xb0], eax` | False | False |
| 1 | `0x000BBD57` | `lea r11, [rsp + 0xb0]` | False | False |
| 1 | `0x000BD0B0` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x000BD0DA` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x000BDB35` | `mov rsi, qword ptr [rcx + 0xb0]` | False | False |
| 1 | `0x000C6EA3` | `mov eax, dword ptr [rsi + 0xb0]` | False | False |
| 1 | `0x000C6ECC` | `mov eax, dword ptr [rbx + 0xb0]` | False | False |
| 1 | `0x000C6EDC` | `mov dword ptr [rdi + 0xb0], eax` | False | False |
| 1 | `0x000C91CC` | `lea rdx, [rbp + 0xb0]` | False | False |
| 1 | `0x000C91DC` | `lea rcx, [rbp + 0xb0]` | False | False |
| 1 | `0x000D2546` | `mov dword ptr [rbp + 0xb0], 0xb` | False | False |
| 1 | `0x000D2550` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x000D25B0` | `lea rcx, [rbp + 0xb0]` | False | False |
| 1 | `0x000D998B` | `mov eax, dword ptr [rbx + 0xb0]` | False | False |
| 1 | `0x000D9D92` | `mov byte ptr [rsp + 0xb0], 0` | False | False |
| 1 | `0x000DA1A6` | `mov byte ptr [rsp + 0xb0], 0` | False | False |
| 1 | `0x000E0179` | `mov qword ptr [rcx + 0xb0], rsi` | False | False |
| 1 | `0x000E2A7B` | `mov byte ptr [rbp + 0xb0], 0` | False | False |
| 1 | `0x000E332A` | `lea rcx, [rbp + 0xb0]` | False | False |
| 1 | `0x000E3337` | `mov rax, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x000E37C0` | `mov rax, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x000E37CB` | `lea rax, [rbp + 0xb0]` | False | False |
| 1 | `0x000E3823` | `lea rcx, [rbp + 0xb0]` | False | False |
| 1 | `0x000E3A73` | `mov rax, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x000E3A85` | `mov qword ptr [rbp + rcx + 0xb0], rax` | False | False |
| 1 | `0x000E3A8D` | `mov rax, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x000E3AB1` | `mov rax, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x000E3AC3` | `mov qword ptr [rbp + rcx + 0xb0], rax` | False | False |
| 1 | `0x000E3ACB` | `mov rax, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x000E40B4` | `mov rdi, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x000E4263` | `mov rdi, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x000E43DE` | `mov rdi, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x000E4541` | `mov rdi, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x000E4691` | `mov rdi, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x000E46A7` | `mov rdi, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x000E5CC7` | `lea rcx, [rdi + 0xb0]` | False | False |
| 1 | `0x000EB092` | `lea rcx, [rbp + 0xb0]` | False | False |
| 1 | `0x000ED273` | `lea rcx, [rsi + 0xb0]` | False | False |
| 1 | `0x00123553` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x00123601` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00124753` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x001247F2` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00124CE3` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x00124D83` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x001262D3` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x0012637B` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00126CA3` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x00126D4B` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00129A91` | `mov qword ptr [rsp + 0xb0], rdx` | False | False |
| 1 | `0x0012B4FE` | `mov r13, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0013074F` | `mov r9d, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x00130794` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x00131CAC` | `lea rcx, [rsp + 0xb0]` | False | False |
| 1 | `0x00131CD5` | `lea rdx, [rsp + 0xb0]` | False | False |
| 1 | `0x00133A19` | `lea rdx, [rbp + 0xb0]` | False | False |
| 1 | `0x00133B01` | `mov rcx, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x001360A0` | `mov dword ptr [rbp + 0xb0], esi` | False | False |
| 1 | `0x00138A22` | `mov dword ptr [rbp + 0xb0], esi` | False | False |
| 1 | `0x0013976D` | `mov qword ptr [r14 + 0xb0], rax` | False | False |
| 1 | `0x0013D061` | `lea rdx, [rbp + 0xb0]` | False | False |
| 1 | `0x0013D123` | `mov rcx, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x0013D181` | `mov byte ptr [rbp + 0xb0], 0` | False | False |
| 1 | `0x0013EC61` | `lea rdx, [rbp + 0xb0]` | False | False |
| 1 | `0x0013EC8F` | `lea rcx, [rbp + 0xb0]` | False | False |
| 1 | `0x0013FD55` | `mov rax, qword ptr [r15 + 0xb0]` | False | False |
| 1 | `0x0014249E` | `mov byte ptr [rbp + 0xb0], cl` | False | False |
| 1 | `0x001424A4` | `movsx ecx, byte ptr [rbp + 0xb0]` | False | False |
| 1 | `0x00142702` | `movzx eax, byte ptr [rbp + 0xb0]` | False | False |
| 1 | `0x001437B0` | `mov qword ptr [rbx + 0xb0], rdi` | False | False |
| 1 | `0x00146835` | `mov qword ptr [rbp + 0xb0], rdi` | False | False |
| 1 | `0x0014753F` | `cmp qword ptr [r13 + 0xb0], 0` | False | False |
| 1 | `0x00147557` | `mov rdx, qword ptr [r13 + 0xb0]` | False | False |
| 1 | `0x0014759E` | `lea rcx, [r13 + 0xb0]` | False | False |
| 1 | `0x00147608` | `mov rdx, qword ptr [r13 + 0xb0]` | False | False |
| 1 | `0x00147CDA` | `cmp qword ptr [rbx + 0xb0], 0` | False | False |
| 1 | `0x00147CF6` | `mov rdx, qword ptr [rbx + 0xb0]` | False | False |
| 1 | `0x001489E3` | `mov rax, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00148D4D` | `mov qword ptr [rdi + 0xb0], rbx` | False | False |
| 1 | `0x0014ABA3` | `mov qword ptr [rdi + 0xb0], r15` | False | False |
| 1 | `0x0014AE17` | `mov rbx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0014AE66` | `mov qword ptr [rsp + 0xb0], rbx` | False | False |
| 1 | `0x0014AF9F` | `mov rbx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0014B203` | `mov qword ptr [rbx + 0xb0], r15` | False | False |
| 1 | `0x0014B85B` | `mov rcx, qword ptr [rsi + 0xb0]` | False | False |
| 1 | `0x0014B922` | `mov qword ptr [rsi + 0xb0], rdi` | False | False |
| 1 | `0x00156817` | `movaps xmmword ptr [rbp + 0xb0], xmm10` | False | False |
| 1 | `0x001585F6` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x00158659` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00159CF9` | `lea rdx, [rsp + 0xb0]` | False | False |
| 1 | `0x00159D5B` | `mov eax, dword ptr [rsp + rdx*4 + 0xb0]` | False | False |
| 1 | `0x00159D95` | `lea rax, [rsp + 0xb0]` | False | False |
| 1 | `0x00159DA3` | `lea rcx, [rsp + 0xb0]` | False | False |
| 1 | `0x00159E5F` | `mov dword ptr [rsp + rax*4 + 0xb0], edx` | False | False |
| 1 | `0x00159E76` | `movaps xmm0, xmmword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0015BB8D` | `mov r10, qword ptr [rcx + 0xb0]` | False | False |
| 1 | `0x0015BC9F` | `xor rdx, qword ptr [rcx + 0xb0]` | False | False |
| 1 | `0x0015BCAF` | `mov qword ptr [rcx + 0xb0], rdx` | False | False |
| 1 | `0x0015BE66` | `mov rdx, qword ptr [rcx + 0xb0]` | False | False |
| 1 | `0x0015BE6D` | `mov qword ptr [rcx + 0xb0], rax` | False | False |
| 1 | `0x0015C031` | `mov rdx, qword ptr [rcx + 0xb0]` | False | False |
| 1 | `0x0015C07F` | `mov qword ptr [rcx + 0xb0], rax` | False | False |
| 1 | `0x0015C513` | `mov rax, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0015C72E` | `mov rax, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0015C8F8` | `mov rax, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0015CC16` | `mov rax, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0015D017` | `mov rax, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0015D141` | `mov rax, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0015D427` | `mov rax, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0015D7C8` | `mov rax, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0015DB8A` | `mov rax, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0015DF8F` | `mov rax, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0015E218` | `mov rax, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0015E41C` | `mov rax, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00161EA0` | `lea rcx, [rsp + 0xb0]` | False | False |
| 1 | `0x00161ED1` | `mov rdx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00161ED9` | `lea rcx, [rsp + 0xb0]` | False | False |
| 1 | `0x00161EFA` | `mov word ptr [rsp + 0xb0], di` | False | False |
| 1 | `0x0016555E` | `mov dword ptr [rsp + 0xb0], 0x38` | False | False |
| 1 | `0x00165569` | `mov eax, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00165586` | `mov ecx, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x001655A1` | `mov eax, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x001655BE` | `mov eax, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x001655DB` | `mov eax, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x001655F8` | `mov eax, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00165615` | `mov eax, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00165632` | `mov eax, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0016564F` | `mov eax, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0016566C` | `mov eax, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00165689` | `mov eax, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x001656A6` | `mov eax, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x001656C3` | `mov eax, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x001656E0` | `mov eax, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x001656FD` | `mov eax, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0016571A` | `mov eax, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00165737` | `mov eax, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00165754` | `mov eax, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00165771` | `mov eax, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0016578E` | `mov eax, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x001657AB` | `mov eax, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x001657C8` | `mov eax, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x001657E5` | `mov eax, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00165802` | `mov eax, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0016581F` | `mov eax, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0016583C` | `mov eax, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00165859` | `mov eax, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00165876` | `mov eax, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00165893` | `mov eax, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x001658B0` | `mov eax, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x001658CD` | `mov eax, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x001658EA` | `mov eax, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00165907` | `mov eax, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00165924` | `mov eax, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00165952` | `lea rcx, [rsp + 0xb0]` | False | False |
| 1 | `0x00165E57` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x00165E75` | `cmp rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00168471` | `mov qword ptr [rsp + 0xb0], rsi` | False | False |
| 1 | `0x001693CC` | `mov qword ptr [rsp + 0xb0], rcx` | False | False |
| 1 | `0x001693EC` | `lea rdx, [rsp + 0xb0]` | False | False |
| 1 | `0x001696F4` | `mov byte ptr [rsp + 0xb0], cl` | False | False |
| 1 | `0x001696FB` | `movsx ecx, byte ptr [rsp + 0xb0]` | False | False |
| 1 | `0x001699F6` | `movzx eax, byte ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0016CA2C` | `movsd qword ptr [rsp + 0xb0], xmm0` | False | False |
| 1 | `0x0016CE39` | `lea rcx, [rsp + 0xb0]` | False | False |
| 1 | `0x0016E175` | `mov qword ptr [rsp + 0xb0], rbx` | False | False |
| 1 | `0x0016E25C` | `lea rcx, [rsp + 0xb0]` | False | False |
| 1 | `0x00172ED4` | `mov byte ptr [rbp + 0xb0], cl` | False | False |
| 1 | `0x00172EDA` | `movsx ecx, byte ptr [rbp + 0xb0]` | False | False |
| 1 | `0x001774C3` | `mov qword ptr [rsp + 0xb0], rcx` | False | False |
| 1 | `0x001774E3` | `lea rdx, [rsp + 0xb0]` | False | False |
| 1 | `0x00179AF1` | `mov rsi, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0017A272` | `mov rbp, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0017A5E4` | `mov rdi, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0017C19E` | `lea rcx, [rbp + 0xb0]` | False | False |
| 1 | `0x0017C1AA` | `lea rdx, [rbp + 0xb0]` | False | False |
| 1 | `0x0017CEDF` | `mov qword ptr [rsp + 0xb0], 0xfffffffffffffffe` | False | False |
| 1 | `0x00182115` | `cmovne ax, word ptr [rbp + 0xb0]` | False | False |
| 1 | `0x0018FB62` | `mov byte ptr [rbp + 0xb0], al` | False | False |
| 1 | `0x0018FB68` | `movsx ecx, byte ptr [rbp + 0xb0]` | False | False |
| 1 | `0x0019331B` | `mov dword ptr [rbp + 0xb0], 0x6b` | False | False |
| 1 | `0x001936B1` | `lea rcx, [rbp + 0xb0]` | False | False |
| 1 | `0x00194AE3` | `mov byte ptr [rbp + 0xb0], al` | False | False |
| 1 | `0x00194AE9` | `movsx ecx, byte ptr [rbp + 0xb0]` | False | False |
| 1 | `0x00194D01` | `movzx eax, byte ptr [rbp + 0xb0]` | False | False |
| 1 | `0x0019D2FE` | `mov byte ptr [rbp + 0xb0], cl` | False | False |
| 1 | `0x0019D304` | `movsx ecx, byte ptr [rbp + 0xb0]` | False | False |
| 1 | `0x001A3513` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x001A35C1` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x001A50E3` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x001A518B` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x001A76F1` | `mov rsi, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x001A7EF0` | `mov qword ptr [rcx + 0xb0], r8` | False | False |
| 1 | `0x001A7F0C` | `mov rax, qword ptr [rdx + 0xb0]` | False | False |
| 1 | `0x001A7F13` | `mov qword ptr [rcx + 0xb0], rax` | False | False |
| 1 | `0x001A7F2F` | `mov qword ptr [rdx + 0xb0], r8` | False | False |
| 1 | `0x001A7FC6` | `mov qword ptr [rbx + 0xb0], rcx` | False | False |
| 1 | `0x001A96D6` | `lea r11, [rsp + 0xb0]` | False | False |
| 1 | `0x001AA0A2` | `mov qword ptr [rsp + 0xb0], rbx` | False | False |
| 1 | `0x001AA17E` | `mov rbx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x001AAC9E` | `mov rax, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x001AAE36` | `mov rax, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x001AAF86` | `mov rax, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x001AD28B` | `mov qword ptr [rbp + 0xb0], rcx` | False | False |
| 1 | `0x001AEF2D` | `mov dword ptr [rsp + 0xb0], ecx` | False | False |
| 1 | `0x001AF0D6` | `mov qword ptr [rsp + 0xb0], rcx` | False | False |
| 1 | `0x001B246A` | `movups xmm0, xmmword ptr [rax + 0xb0]` | False | False |
| 1 | `0x001B2471` | `movups xmmword ptr [rcx + 0xb0], xmm0` | False | False |
| 1 | `0x001B24EF` | `movups xmm1, xmmword ptr [rax + 0xb0]` | False | False |
| 1 | `0x001B24F6` | `movups xmmword ptr [rcx + 0xb0], xmm1` | False | False |
| 1 | `0x001B4296` | `mov dword ptr [rsp + 0xb0], eax` | False | False |
| 1 | `0x001B4990` | `mov eax, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x001B5938` | `mov qword ptr [rsp + 0xb0], rcx` | False | False |
| 1 | `0x001B6BE0` | `mov qword ptr [rsp + 0xb0], rcx` | False | False |
| 1 | `0x001B7629` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x001B764E` | `lea rcx, [rsp + 0xb0]` | False | False |
| 1 | `0x001B79BD` | `mov qword ptr [rsp + 0xb0], rcx` | False | False |
| 1 | `0x001B79E2` | `lea rcx, [rsp + 0xb0]` | False | False |
| 1 | `0x001B8F84` | `mov eax, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x001B9AD8` | `lea r11, [rsp + 0xb0]` | False | False |
| 1 | `0x001B9CB8` | `movaps xmm1, xmmword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x001B9F5D` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x001BC2A3` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x001BD7D6` | `lea rcx, [rsp + 0xb0]` | False | False |
| 1 | `0x001BD80A` | `lea rdx, [rsp + 0xb0]` | False | False |
| 1 | `0x001BD861` | `lea rcx, [rsp + 0xb0]` | False | False |
| 1 | `0x001BE380` | `movups xmm0, xmmword ptr [rdx + 0xb0]` | False | False |
| 1 | `0x001BE387` | `movups xmmword ptr [rcx + 0xb0], xmm0` | False | False |
| 1 | `0x001BE3FD` | `movups xmm1, xmmword ptr [rdx + 0xb0]` | False | False |
| 1 | `0x001BE404` | `movups xmmword ptr [rax + 0xb0], xmm1` | False | False |
| 1 | `0x001BE892` | `mov qword ptr [rbp + 0xb0], rcx` | False | False |
| 1 | `0x001BFAB8` | `mov qword ptr [rsp + 0xb0], rcx` | False | False |
| 1 | `0x001C16A4` | `mov byte ptr [rbp + 0xb0], cl` | False | False |
| 1 | `0x001C16AA` | `movsx ecx, byte ptr [rbp + 0xb0]` | False | False |
| 1 | `0x001C9529` | `lea r9, [rsp + 0xb0]` | False | False |
| 1 | `0x001CD58A` | `lea rcx, [rsp + 0xb0]` | False | False |
| 1 | `0x001CD5BE` | `lea rdx, [rsp + 0xb0]` | False | False |
| 1 | `0x001CD613` | `lea rcx, [rsp + 0xb0]` | False | False |
| 1 | `0x001CF949` | `lea rdx, [rsp + 0xb0]` | False | False |
| 1 | `0x001D250F` | `mov dword ptr [rbp + 0xb0], 0x6d` | False | False |
| 1 | `0x001D2519` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x001D26E7` | `lea rcx, [rbp + 0xb0]` | False | False |
| 1 | `0x001D4E83` | `mov qword ptr [rbp + 0xb0], rdi` | False | False |
| 1 | `0x001D62DE` | `lea rcx, [rbp + 0xb0]` | False | False |
| 1 | `0x001D62EA` | `mov dword ptr [rbp + 0xb0], 0x10098` | False | False |
| 1 | `0x001D62F4` | `lea r8, [rbp + 0xb0]` | False | False |
| 1 | `0x001DA330` | `lea rdx, [rbp + 0xb0]` | False | False |
| 1 | `0x001DA36C` | `mov rcx, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x001DAFBF` | `mov rax, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x001DB01B` | `mov qword ptr [rbp + 0xb0], 0xf` | False | False |
| 1 | `0x001E0386` | `movups xmmword ptr [rsp + 0xb0], xmm0` | False | False |
| 1 | `0x001E03C0` | `lea rcx, [rsp + 0xb0]` | False | False |
| 1 | `0x001E3373` | `mov esi, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x001E337F` | `mov dword ptr [rbp + 0xb0], eax` | False | False |
| 1 | `0x001E44A2` | `mov byte ptr [rbp + 0xb0], cl` | False | False |
| 1 | `0x001E44A8` | `movsx ecx, byte ptr [rbp + 0xb0]` | False | False |
| 1 | `0x001E9F0A` | `mov byte ptr [rbp + 0xb0], cl` | False | False |
| 1 | `0x001E9F10` | `movsx ecx, byte ptr [rbp + 0xb0]` | False | False |
| 1 | `0x001EC6A3` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x001EC74B` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x001ECAC3` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x001ECB6B` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x001EDE73` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x001F1ACC` | `mov qword ptr [rsp + 0xb0], rcx` | False | False |
| 1 | `0x001F3A3A` | `mov dword ptr [rbx + 0xb0], eax` | False | False |
| 1 | `0x001F56F6` | `mov qword ptr [rsp + 0xb0], rcx` | False | False |
| 1 | `0x001F56FE` | `lea rdx, [rsp + 0xb0]` | False | False |
| 1 | `0x001F5C0E` | `lea r8, [rsp + 0xb0]` | False | False |
| 1 | `0x001F5C52` | `mov rax, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x001F7591` | `cmp ebx, dword ptr [rdi + 0xb0]` | False | False |
| 1 | `0x001F76AC` | `mov dword ptr [rdi + 0xb0], ebx` | False | False |
| 1 | `0x001F8EA8` | `cmp r14d, dword ptr [rsi + 0xb0]` | False | False |
| 1 | `0x001F9466` | `mov rax, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x001FC55F` | `mov qword ptr [rsp + 0xb0], rcx` | False | False |
| 1 | `0x00201A9D` | `mov qword ptr [rbp + 0xb0], 0xfffffffffffffffe` | False | False |
| 1 | `0x002050EA` | `mov byte ptr [rsp + 0xb0], al` | False | False |
| 1 | `0x002050F1` | `movsx ecx, byte ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002083FB` | `mov qword ptr [rsp + 0xb0], rcx` | False | False |
| 1 | `0x00209A43` | `mov qword ptr [rbp + 0xb0], r14` | False | False |
| 1 | `0x00209A66` | `mov rcx, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x00209AA5` | `mov qword ptr [rbp + 0xb0], r14` | False | False |
| 1 | `0x0020CAFF` | `lea rdx, [rbp + 0xb0]` | False | False |
| 1 | `0x0020CB43` | `mov rcx, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x0020CBA1` | `mov byte ptr [rbp + 0xb0], 0` | False | False |
| 1 | `0x0021359D` | `mov qword ptr [rbp + 0xb0], rax` | False | False |
| 1 | `0x0021A9F3` | `mov dword ptr [rbp + 0xb0], 0x36` | False | False |
| 1 | `0x0021A9FD` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x0021AC25` | `lea rcx, [rbp + 0xb0]` | False | False |
| 1 | `0x0021BA25` | `mov rax, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x0021BA81` | `mov qword ptr [rbp + 0xb0], 0xf` | False | False |
| 1 | `0x0021DCF3` | `mov rax, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0021F830` | `mov qword ptr [rbp + 0xb0], 0xf` | False | False |
| 1 | `0x002201FC` | `mov rax, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x0022086B` | `lea rdx, [rbp + 0xb0]` | False | False |
| 1 | `0x002208A1` | `lea rcx, [rbp + 0xb0]` | False | False |
| 1 | `0x0022283F` | `lea rcx, [rbp + 0xb0]` | False | False |
| 1 | `0x00222873` | `mov rcx, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x002228D1` | `mov byte ptr [rbp + 0xb0], 0` | False | False |
| 1 | `0x0022855D` | `mov r10, qword ptr [rcx + 0xb0]` | False | False |
| 1 | `0x0022866F` | `xor rdx, qword ptr [rcx + 0xb0]` | False | False |
| 1 | `0x0022867F` | `mov qword ptr [rcx + 0xb0], rdx` | False | False |
| 1 | `0x00228836` | `mov rdx, qword ptr [rcx + 0xb0]` | False | False |
| 1 | `0x0022883D` | `mov qword ptr [rcx + 0xb0], rax` | False | False |
| 1 | `0x00228A01` | `mov rdx, qword ptr [rcx + 0xb0]` | False | False |
| 1 | `0x00228A4F` | `mov qword ptr [rcx + 0xb0], rax` | False | False |
| 1 | `0x00229FA7` | `mov qword ptr [rbp + 0xb0], 0xf` | False | False |
| 1 | `0x0022CC76` | `mov qword ptr [rsp + 0xb0], rbx` | False | False |
| 1 | `0x0022E3F0` | `movsd xmm1, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0022EA5C` | `lea r11, [rsp + 0xb0]` | False | False |
| 1 | `0x0022EA9C` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x0022EB48` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0022EB8C` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x0022EC38` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0022F566` | `mov rbx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0022FCD6` | `lea r11, [rsp + 0xb0]` | False | False |
| 1 | `0x0022FE5D` | `mov qword ptr [rbp + 0xb0], rax` | False | False |
| 1 | `0x0022FF9E` | `mov rcx, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x00230457` | `mov rbx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002304BF` | `mov r9, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002305FC` | `movzx r9d, byte ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002311E6` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x002312DD` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00234D7A` | `mov edx, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00234EA7` | `mov edx, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00235208` | `mov qword ptr [rdi + 0xb0], rax` | False | False |
| 1 | `0x00235739` | `movsd qword ptr [rdi + 0xb0], xmm1` | False | False |
| 1 | `0x00235A96` | `mov qword ptr [rbx + 0xb0], rax` | False | False |
| 1 | `0x00235BA4` | `mov rax, qword ptr [rdx + 0xb0]` | False | False |
| 1 | `0x00235BAB` | `mov qword ptr [rcx + 0xb0], rax` | False | False |
| 1 | `0x00235BBB` | `mov qword ptr [rdx + 0xb0], rax` | False | False |
| 1 | `0x00235CA8` | `mov qword ptr [rdi + 0xb0], r13` | False | False |
| 1 | `0x00237976` | `mov rbx, qword ptr [rcx + 0xb0]` | False | False |
| 1 | `0x0023D028` | `mov rdx, qword ptr [rsi + 0xb0]` | False | False |
| 1 | `0x0023DB09` | `lea r11, [rsp + 0xb0]` | False | False |
| 1 | `0x0023E700` | `mov byte ptr [rbp + 0xb0], al` | False | False |
| 1 | `0x0023E708` | `movsx ecx, byte ptr [rbp + 0xb0]` | False | False |
| 1 | `0x0023E745` | `movzx eax, byte ptr [rbp + 0xb0]` | False | False |
| 1 | `0x0023F053` | `mov qword ptr [rbp + 0xb0], r15` | False | False |
| 1 | `0x0023F081` | `mov r14, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x0023F10F` | `mov rax, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x0023F1E3` | `mov rcx, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x00240ED0` | `mov byte ptr [rbp + 0xb0], al` | False | False |
| 1 | `0x00243FE0` | `lea r11, [rsp + 0xb0]` | False | False |
| 1 | `0x0024490E` | `mov qword ptr [rbp + 0xb0], 0xf` | False | False |
| 1 | `0x00245882` | `mov byte ptr [rbp + 0xb0], cl` | False | False |
| 1 | `0x00245888` | `movsx ecx, byte ptr [rbp + 0xb0]` | False | False |
| 1 | `0x00247218` | `lea r11, [rsp + 0xb0]` | False | False |
| 1 | `0x00247970` | `mov rax, qword ptr [rdx + 0xb0]` | False | False |
| 1 | `0x00247CED` | `lea rcx, [rsi + 0xb0]` | False | False |
| 1 | `0x00247D4E` | `lea rcx, [rsp + 0xb0]` | False | False |
| 1 | `0x00248110` | `movsd xmm1, qword ptr [rsi + 0xb0]` | False | False |
| 1 | `0x002487B8` | `mov rax, qword ptr [rbx + 0xb0]` | False | False |
| 1 | `0x0024AF06` | `lea rcx, [rbx + 0xb0]` | False | False |
| 1 | `0x0024E714` | `mov qword ptr [rbp + 0xb0], r15` | False | False |
| 1 | `0x0024FAE8` | `mov rcx, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x0024FB4E` | `mov qword ptr [rbp + 0xb0], 0xf` | False | False |
| 1 | `0x00252336` | `mov dword ptr [rbp + 0xb0], 0x60` | False | False |
| 1 | `0x00252340` | `mov ecx, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x0025235B` | `mov edx, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x00252373` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x0025238D` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x002523A7` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x002523C1` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x002523DB` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x002523F5` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x0025240F` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x00252429` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x00252443` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x0025245D` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x00252477` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x00252491` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x002524AB` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x002524C5` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x002524DF` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x002524F9` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x00252513` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x0025252D` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x00252547` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x00252561` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x0025257B` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x00252595` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x002525AF` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x002525C9` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x002525E3` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x002525FD` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x00252617` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x00252631` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x0025264B` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x00252665` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x0025268E` | `lea rcx, [rbp + 0xb0]` | False | False |
| 1 | `0x002547C8` | `mov qword ptr [rbp + 0xb0], r13` | False | False |
| 1 | `0x00255C1A` | `movaps xmmword ptr [rbp + 0xb0], xmm1` | False | False |
| 1 | `0x002622D9` | `mov byte ptr [rbp + 0xb0], al` | False | False |
| 1 | `0x002622DF` | `movsx ecx, byte ptr [rbp + 0xb0]` | False | False |
| 1 | `0x00262A17` | `mov rax, qword ptr [rbx + 0xb0]` | False | False |
| 1 | `0x00262A73` | `mov rax, qword ptr [rbx + 0xb0]` | False | False |
| 1 | `0x0026480D` | `mov byte ptr [rbp + 0xb0], 0` | False | False |
| 1 | `0x00264C56` | `lea rcx, [rdi + 0xb0]` | False | False |
| 1 | `0x002655AC` | `mov qword ptr [rsp + 0xb0], rbx` | False | False |
| 1 | `0x00265895` | `mov rbx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00266A0B` | `mov r14, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002686E2` | `mov r14, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00269F1A` | `mov dword ptr [rsp + 0xb0], 1` | False | False |
| 1 | `0x00269FA8` | `movaps xmm6, xmmword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0026A7C5` | `mov dword ptr [rsp + 0xb0], eax` | False | False |
| 1 | `0x002707FA` | `mov qword ptr [rbp + 0xb0], 0xf` | False | False |
| 1 | `0x00271F9D` | `mov qword ptr [rdi + 0xb0], rsi` | False | False |
| 1 | `0x00274A6B` | `mov r8d, dword ptr [rdi + 0xb0]` | False | False |
| 1 | `0x00274A8C` | `mov rax, qword ptr [rdi + 0xb0]` | False | False |
| 1 | `0x00274BBD` | `mov r8d, dword ptr [rdi + 0xb0]` | False | False |
| 1 | `0x00274BDB` | `mov rax, qword ptr [rdi + 0xb0]` | False | False |
| 1 | `0x00274D53` | `mov r8d, dword ptr [rdi + 0xb0]` | False | False |
| 1 | `0x00274D74` | `mov rax, qword ptr [rdi + 0xb0]` | False | False |
| 1 | `0x00274EA7` | `mov r8d, dword ptr [rdi + 0xb0]` | False | False |
| 1 | `0x00274EC5` | `mov rax, qword ptr [rdi + 0xb0]` | False | False |
| 1 | `0x00274FC5` | `mov r8d, dword ptr [rdi + 0xb0]` | False | False |
| 1 | `0x00274FE6` | `mov rax, qword ptr [rdi + 0xb0]` | False | False |
| 1 | `0x00275107` | `mov r8d, dword ptr [rdi + 0xb0]` | False | False |
| 1 | `0x00275125` | `mov rax, qword ptr [rdi + 0xb0]` | False | False |
| 1 | `0x00275918` | `lea rcx, [rbp + 0xb0]` | False | False |
| 1 | `0x00275D58` | `lea rcx, [rbp + 0xb0]` | False | False |
| 1 | `0x00276DF0` | `lea r11, [rsp + 0xb0]` | False | False |
| 1 | `0x002771B9` | `mov qword ptr [rsp + 0xb0], rcx` | False | False |
| 1 | `0x002796DC` | `mov r12, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0027FBA6` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x0027FCA7` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002830AB` | `mov dword ptr [rbp + 0xb0], 0x41` | False | False |
| 1 | `0x00283234` | `lea rcx, [rbp + 0xb0]` | False | False |
| 1 | `0x002837BA` | `mov qword ptr [rsi + 0xb0], rax` | False | False |
| 1 | `0x00283EB7` | `lea r8, [rsp + 0xb0]` | False | False |
| 1 | `0x00284D1C` | `mov dword ptr [r15 + 0xb0], r14d` | False | False |
| 1 | `0x002850BB` | `mov eax, dword ptr [rbx + 0xb0]` | False | False |
| 1 | `0x002850C1` | `cmp dword ptr [rcx + 0xb0], eax` | False | False |
| 1 | `0x00286048` | `mov qword ptr [rbp + 0xb0], rax` | False | False |
| 1 | `0x0028690C` | `mov rcx, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x00286DDD` | `lea r11, [rsp + 0xb0]` | False | False |
| 1 | `0x00287CE7` | `mov qword ptr [rsp + 0xb0], 0xf` | False | False |
| 1 | `0x00287E57` | `mov qword ptr [rsp + 0xb0], 0xf` | False | False |
| 1 | `0x00288E66` | `mov dword ptr [rsp + 0xb0], ebx` | False | False |
| 1 | `0x00292508` | `mov qword ptr [rsp + 0xb0], rbx` | False | False |
| 1 | `0x002926FF` | `mov rbx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0029311B` | `mov qword ptr [rdi + 0xb0], rbp` | False | False |
| 1 | `0x00293914` | `mov rcx, qword ptr [rbx + 0xb0]` | False | False |
| 1 | `0x00294022` | `mov qword ptr [rdi + 0xb0], rax` | False | False |
| 1 | `0x00295C3C` | `cmp qword ptr [rax + 0xb0], rdi` | False | False |
| 1 | `0x00296438` | `cmp qword ptr [rax + 0xb0], r14` | False | False |
| 1 | `0x00296499` | `mov rbx, qword ptr [rax + 0xb0]` | False | False |
| 1 | `0x00296DD1` | `mov rcx, qword ptr [rax + 0xb0]` | False | False |
| 1 | `0x00296DF4` | `mov qword ptr [rax + 0xb0], rcx` | False | False |
| 1 | `0x0029809B` | `mov rcx, qword ptr [rcx + 0xb0]` | False | False |
| 1 | `0x002982FD` | `mov rcx, qword ptr [rcx + 0xb0]` | False | False |
| 1 | `0x00298A29` | `mov rcx, qword ptr [rcx + 0xb0]` | False | False |
| 1 | `0x00299887` | `movups xmm1, xmmword ptr [rax + 0xb0]` | False | False |
| 1 | `0x0029E0CA` | `mov rcx, qword ptr [rax + 0xb0]` | False | False |
| 1 | `0x0029E103` | `mov qword ptr [rax + 0xb0], rbp` | False | False |
| 1 | `0x0029E11A` | `mov rcx, qword ptr [rax + 0xb0]` | False | False |
| 1 | `0x0029E132` | `mov qword ptr [rax + 0xb0], r14` | False | False |
| 1 | `0x0029E4B3` | `movups xmmword ptr [rax + 0xb0], xmm1` | False | False |
| 1 | `0x0029EB86` | `mov r9, qword ptr [rax + 0xb0]` | False | False |
| 1 | `0x0029F8D8` | `lea rax, [rbp + 0xb0]` | False | False |
| 1 | `0x0029F9BE` | `lea rdx, [rbp + 0xb0]` | False | False |
| 1 | `0x0029F9E0` | `mov byte ptr [rbp + 0xb0], bl` | False | False |
| 1 | `0x0029FAD7` | `lea r8, [rbp + 0xb0]` | False | False |
| 1 | `0x0029FB39` | `lea rcx, [rbp + 0xb0]` | False | False |
| 1 | `0x002A307D` | `mov rdx, qword ptr [rbx + 0xb0]` | False | False |
| 1 | `0x002A3907` | `mov r15d, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002A3915` | `call qword ptr [rax + 0xb0]` | False | False |
| 1 | `0x002A42F4` | `mov qword ptr [rsp + 0xb0], r13` | False | False |
| 1 | `0x002A47BB` | `mov r13, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002A4A94` | `mov qword ptr [rsp + 0xb0], rdi` | False | False |
| 1 | `0x002A50D4` | `mov rdi, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002A6453` | `mov rcx, qword ptr [rbx + 0xb0]` | False | False |
| 1 | `0x002A7127` | `mov rcx, qword ptr [rdi + 0xb0]` | False | False |
| 1 | `0x002ABAEE` | `mov r15, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002AE8AD` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x002AE90C` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002B2D7A` | `mov rcx, qword ptr [rbx + 0xb0]` | False | False |
| 1 | `0x002B2D8B` | `mov qword ptr [rbx + 0xb0], r12` | False | False |
| 1 | `0x002B2E04` | `lea rcx, [rbx + 0xb0]` | False | False |
| 1 | `0x002B3A8A` | `mov qword ptr [rbp + 0xb0], rcx` | False | False |
| 1 | `0x002B3C33` | `mov rcx, qword ptr [rdi + 0xb0]` | False | False |
| 1 | `0x002B3F05` | `cmp qword ptr [rdi + 0xb0], 0` | False | False |
| 1 | `0x002B3F2E` | `mov rcx, qword ptr [rdi + 0xb0]` | False | False |
| 1 | `0x002B4695` | `cmp qword ptr [rax + 0xb0], r15` | False | False |
| 1 | `0x002B47DD` | `cmp qword ptr [rax + 0xb0], rcx` | False | False |
| 1 | `0x002B6313` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x002B64EA` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002B8845` | `lea rcx, [rbp + 0xb0]` | False | False |
| 1 | `0x002B886C` | `mov byte ptr [rbp + rbx + 0xb0], al` | False | False |
| 1 | `0x002B887A` | `mov byte ptr [rbp + rax + 0xb0], dl` | False | False |
| 1 | `0x002B888B` | `mov byte ptr [rbp + rax + 0xb0], dl` | False | False |
| 1 | `0x002B88AF` | `mov byte ptr [rbp + rax + 0xb0], dl` | False | False |
| 1 | `0x002B88C0` | `mov byte ptr [rbp + rax + 0xb0], dl` | False | False |
| 1 | `0x002B88D1` | `mov byte ptr [rbp + rax + 0xb0], dl` | False | False |
| 1 | `0x002B88DC` | `mov byte ptr [rbp + rax + 0xb0], r15b` | False | False |
| 1 | `0x002B8BA3` | `movzx edx, byte ptr [rbp + rcx + 0xb0]` | False | False |
| 1 | `0x002BA053` | `mov qword ptr [rsp + 0xb0], rcx` | False | False |
| 1 | `0x002BA19D` | `mov rbx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002BA474` | `mov r9, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002BAB42` | `movups xmm1, xmmword ptr [rax + 0xb0]` | False | False |
| 1 | `0x002BB085` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x002BB130` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002BEE93` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x002BF104` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002C8EFA` | `mov dword ptr [rcx + 0xb0], ebp` | False | False |
| 1 | `0x002C926C` | `mov qword ptr [rsp + 0xb0], rbx` | False | False |
| 1 | `0x002C94C6` | `mov rbx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002CAB8B` | `lea rdx, [rcx + 0xb0]` | False | False |
| 1 | `0x002CB85F` | `mov r15, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002CB999` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002CEB87` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x002CEEB9` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002D85F0` | `sub dword ptr [rdi + 0xb0], ebx` | False | False |
| 1 | `0x002D871B` | `cmp dword ptr [rbx + 0xb0], 0` | False | False |
| 1 | `0x002D8743` | `inc dword ptr [rbx + 0xb0]` | False | False |
| 1 | `0x002D878F` | `sub dword ptr [rcx + 0xb0], edi` | False | False |
| 1 | `0x002D884F` | `cmp dword ptr [rcx + 0xb0], 0` | False | False |
| 1 | `0x002D8875` | `inc dword ptr [rbx + 0xb0]` | False | False |
| 1 | `0x002DA9FA` | `mov qword ptr [rsp + 0xb0], r15` | False | False |
| 1 | `0x002DABD3` | `mov r15, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002DD802` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x002DD8FB` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002DD9E2` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x002DDAB8` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002DFC30` | `mov r11, qword ptr [r10 + 0xb0]` | False | False |
| 1 | `0x002E1552` | `mov qword ptr [rsp + 0xb0], r15` | False | False |
| 1 | `0x002E1731` | `mov r15, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002E23BF` | `cmp dword ptr [rbx + 0xb0], 0` | False | False |
| 1 | `0x002E68A8` | `cmp qword ptr [rax + 0xb0], 0` | False | False |
| 1 | `0x002E7A52` | `mov r9, qword ptr [rax + 0xb0]` | False | False |
| 1 | `0x002E9430` | `sub qword ptr [rsp + 0xb0], 1` | False | False |
| 1 | `0x002EB343` | `mov qword ptr [rsp + 0xb0], r12` | False | False |
| 1 | `0x002ECDA4` | `mov r12, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002ECE1F` | `mov qword ptr [rsp + 0xb0], r12` | False | False |
| 1 | `0x002EDC4E` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x002EDD44` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002EDDFD` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x002EDEB6` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002EF460` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x002EF598` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002F1995` | `mov qword ptr [rsp + 0xb0], r12` | False | False |
| 1 | `0x002F1B00` | `mov r12, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002F1D27` | `mov rdx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002F1E6B` | `mov rdx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002F1ED6` | `mov rax, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002F2336` | `mov qword ptr [rsp + 0xb0], rbx` | False | False |
| 1 | `0x002F248F` | `mov rbx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002F2512` | `mov r14d, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002F3FB0` | `mov qword ptr [rax + 0xb0], r13` | False | False |
| 1 | `0x002F4ED3` | `mov rbp, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002F92AF` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x002F9332` | `mov r8, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002F941A` | `call qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002FAEB2` | `mov qword ptr [rsp + 0xb0], rbx` | False | False |
| 1 | `0x002FAEFA` | `mov rbx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002FD06A` | `cmp dword ptr [rsp + 0xb0], r8d` | False | False |
| 1 | `0x002FD245` | `mov eax, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002FD499` | `mov qword ptr [rsp + 0xb0], rdi` | False | False |
| 1 | `0x002FD83E` | `mov rdi, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002FDD3F` | `movzx eax, byte ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002FDED8` | `movzx eax, byte ptr [rsp + 0xb0]` | False | False |
| 1 | `0x002FDEE0` | `mov byte ptr [rsp + 0xb0], al` | False | False |
| 1 | `0x002FDF93` | `lea r9, [rsp + 0xb0]` | False | False |
| 1 | `0x002FE0F5` | `cmp byte ptr [rsp + 0xb0], r13b` | False | False |
| 1 | `0x002FE126` | `cmp byte ptr [rsp + 0xb0], r13b` | False | False |
| 1 | `0x002FECB9` | `mov r12d, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0030416D` | `mov rbx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00305A53` | `mov ebx, dword ptr [rcx + 0xb0]` | False | False |
| 1 | `0x0030A7E6` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0030A7F3` | `mov rax, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0030A831` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0030A8C2` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0030A900` | `mov rax, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0030A953` | `mov rax, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0030A97B` | `add r10, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0030A9CA` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0030A9F4` | `mov rax, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0030AA90` | `mov rdx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0030AB25` | `add rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0030AB4D` | `mov rax, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0030ACB3` | `add rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0030ACC5` | `mov rdx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0030AD4C` | `mov rdx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0030ADFE` | `mov r8, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0030AE65` | `mov rdx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0030AEB9` | `mov r8, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0030AEFD` | `mov r8, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0030AF1A` | `mov r8, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0030AF8F` | `mov r8, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0030AFAC` | `mov r8, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0030B03C` | `mov r8, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0030F716` | `mov qword ptr [rsp + 0xb0], r14` | False | False |
| 1 | `0x0030F844` | `mov r14, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0030FB3A` | `mov qword ptr [rsp + 0xb0], r15` | False | False |
| 1 | `0x0030FE35` | `mov r15, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x003107C9` | `mov r9d, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x003107E6` | `mov r9d, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00310803` | `mov r9d, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0031398C` | `mov qword ptr [rbp + 0xb0], rbx` | False | False |
| 1 | `0x00314066` | `mov rbx, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x003141BC` | `mov r15, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00314A41` | `mov qword ptr [rsp + 0xb0], rdx` | False | False |
| 1 | `0x00314B03` | `mov rdx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00319CF7` | `mov qword ptr [rsp + 0xb0], r15` | False | False |
| 1 | `0x00319EB6` | `mov qword ptr [rsp + 0xb0], rsi` | False | False |
| 1 | `0x0031A2EB` | `mov rax, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0031B619` | `lea r8, [rsi + 0xb0]` | False | False |
| 1 | `0x0031BF97` | `lea rdx, [rdi + 0xb0]` | False | False |
| 1 | `0x0031BFCF` | `lea r8, [rdi + 0xb0]` | False | False |
| 1 | `0x00323472` | `lea r8, [rsp + 0xb0]` | False | False |
| 1 | `0x003234C8` | `mov r8d, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00323582` | `mov r8d, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00324829` | `mov qword ptr [rsp + 0xb0], rdi` | False | False |
| 1 | `0x00324869` | `mov rdi, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00326909` | `mov qword ptr [rsp + 0xb0], rsi` | False | False |
| 1 | `0x00326BCA` | `mov rsi, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00328F82` | `mov rsi, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0032901D` | `lea rdx, [rsp + 0xb0]` | False | False |
| 1 | `0x00329053` | `mov ecx, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0032C3DF` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x0032C533` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0032C723` | `cmp dword ptr [rbx + 0xb0], 0` | False | False |
| 1 | `0x0033517A` | `mov dword ptr [r14 + 0xb0], ecx` | False | False |
| 1 | `0x00335702` | `mov dword ptr [r14 + 0xb0], r10d` | False | False |
| 1 | `0x003367B3` | `mov qword ptr [rsp + 0xb0], rsi` | False | False |
| 1 | `0x0033683B` | `mov qword ptr [rsp + 0xb0], rdx` | False | False |
| 1 | `0x00336849` | `lea r9, [rsp + 0xb0]` | False | False |
| 1 | `0x003368C0` | `mov r8, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0033693B` | `mov rax, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0033696B` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x003369A1` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00336CBF` | `mov rsi, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x003371E4` | `mov qword ptr [rsp + 0xb0], rdi` | False | False |
| 1 | `0x0033775C` | `mov rdi, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x003386E4` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x0033886F` | `mov rsi, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0033B0AE` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x0033B313` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0033D6C1` | `mov qword ptr [rsp + 0xb0], r13` | False | False |
| 1 | `0x0033D8F9` | `mov r13, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0033DF62` | `mov qword ptr [rsp + 0xb0], rbx` | False | False |
| 1 | `0x0033E012` | `mov rbx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0033F775` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x0033F8D4` | `mov rax, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0033FC65` | `cmp qword ptr [rsp + 0xb0], rbx` | False | False |
| 1 | `0x0033FCDA` | `mov rax, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0034240D` | `mov qword ptr [rsp + 0xb0], rbp` | False | False |
| 1 | `0x00342695` | `mov rbp, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00343184` | `mov rbp, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00343361` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00344BB7` | `lea rcx, [rbx + 0xb0]` | False | False |
| 1 | `0x00344BF7` | `lea rcx, [rbx + 0xb0]` | False | False |
| 1 | `0x00344C37` | `lea rcx, [rbx + 0xb0]` | False | False |
| 1 | `0x00344CD3` | `lea rdx, [rbp + 0xb0]` | False | False |
| 1 | `0x00344CDF` | `lea rcx, [rbx + 0xb0]` | False | False |
| 1 | `0x00344D86` | `lea rax, [rbx + 0xb0]` | False | False |
| 1 | `0x00344D91` | `lea rcx, [rbx + 0xb0]` | False | False |
| 1 | `0x00344DF1` | `mov rax, qword ptr [rbx + 0xb0]` | False | False |
| 1 | `0x00344F64` | `lea rcx, [rbx + 0xb0]` | False | False |
| 1 | `0x00344F92` | `lea rax, [rbx + 0xb0]` | False | False |
| 1 | `0x00344F9D` | `lea rcx, [rbx + 0xb0]` | False | False |
| 1 | `0x00344FD0` | `mov rax, qword ptr [rbx + 0xb0]` | False | False |
| 1 | `0x0034505F` | `lea rdx, [rdi + 0xb0]` | False | False |
| 1 | `0x00345136` | `lea rdx, [r14 + 0xb0]` | False | False |
| 1 | `0x003454CD` | `mov rsi, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00345A4D` | `lea r8, [r14 + 0xb0]` | False | False |
| 1 | `0x00346530` | `mov rbx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0034744D` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x003478FF` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00348122` | `mov rbx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0034952C` | `mov rax, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0034957A` | `mov dword ptr [rsp + 0xb0], r15d` | False | False |
| 1 | `0x003495E1` | `mov qword ptr [rsp + 0xb0], rdi` | False | False |
| 1 | `0x00349703` | `mov rdi, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x003498EB` | `mov r13d, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00349A16` | `xor eax, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0034FBD4` | `sub qword ptr [rsp + 0xb0], 1` | False | False |
| 1 | `0x0034FDA1` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x0034FF62` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x003502C1` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x003519C2` | `mov rax, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00352223` | `mov rax, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0035481F` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x00354910` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00355197` | `lea rcx, [rbx + 0xb0]` | False | False |
| 1 | `0x003551E7` | `lea rcx, [rbx + 0xb0]` | False | False |
| 1 | `0x00355250` | `lea rdx, [rbx + 0xb0]` | False | False |
| 1 | `0x00355257` | `lea rcx, [rdi + 0xb0]` | False | False |
| 1 | `0x003553B2` | `lea rcx, [rdi + 0xb0]` | False | False |
| 1 | `0x003553DA` | `lea r8, [rdi + 0xb0]` | False | False |
| 1 | `0x003553E1` | `lea rdx, [rdi + 0xb0]` | False | False |
| 1 | `0x0035553E` | `lea r8, [rbx + 0xb0]` | False | False |
| 1 | `0x00355578` | `lea rdx, [rbx + 0xb0]` | False | False |
| 1 | `0x003556C7` | `lea r8, [rdi + 0xb0]` | False | False |
| 1 | `0x003556F9` | `lea rdx, [rdi + 0xb0]` | False | False |
| 1 | `0x0035603D` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x0035611F` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00356168` | `mov rdx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x003561C9` | `mov r8, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00356269` | `mov r8, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0035637A` | `mov rdx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00356395` | `mov r8, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x003563CD` | `mov rdx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00356BD5` | `lea r8, [rbx + 0xb0]` | False | False |
| 1 | `0x00356C2B` | `lea r8, [rbx + 0xb0]` | False | False |
| 1 | `0x003589AA` | `lea r8, [r15 + 0xb0]` | False | False |
| 1 | `0x003589C4` | `mov r9, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00358AFE` | `mov r9, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x003590B9` | `lea r8, [rbx + 0xb0]` | False | False |
| 1 | `0x00361CD0` | `lea r11, [rsp + 0xb0]` | False | False |
| 1 | `0x003628C8` | `mov rax, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x00362924` | `mov qword ptr [rbp + 0xb0], 0xf` | False | False |
| 1 | `0x00362F12` | `mov rax, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0036AA62` | `mov r9, qword ptr [rbx + 0xb0]` | False | False |
| 1 | `0x0036F863` | `mov r15, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0036FF6B` | `mov rax, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00370764` | `mov qword ptr [rbx + 0xb0], 0` | False | False |
| 1 | `0x00373D12` | `lea r11, [rsp + 0xb0]` | False | False |
| 1 | `0x00374DA5` | `mov qword ptr [rsp + 0xb0], rbp` | False | False |
| 1 | `0x00374F1D` | `mov rbp, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00378511` | `lea rdx, [rsp + 0xb0]` | False | False |
| 1 | `0x003785C0` | `lea rcx, [rsp + 0xb0]` | False | False |
| 1 | `0x0037A2CD` | `mov qword ptr [rsp + 0xb0], rbp` | False | False |
| 1 | `0x0037A51B` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x0037AFBF` | `cmp qword ptr [rsp + 0xb0], r12` | False | False |
| 1 | `0x0037B0C5` | `mov r14, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0037B996` | `mov qword ptr [rbx + 0xb0], rax` | False | False |
| 1 | `0x0037B9C7` | `mov qword ptr [rbx + 0xb0], rax` | False | False |
| 1 | `0x0037C13C` | `mov qword ptr [rsp + 0xb0], rbx` | False | False |
| 1 | `0x0037C221` | `mov rbx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0037F353` | `add rax, qword ptr [rdi + 0xb0]` | False | False |
| 1 | `0x00380BD2` | `lea rdx, [rsp + 0xb0]` | False | False |
| 1 | `0x00386987` | `mov r9, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00386E16` | `mov qword ptr [rbp + 0xb0], rax` | False | False |
| 1 | `0x0038726E` | `mov rcx, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x0038B114` | `cmp dword ptr [rdx + 0xb0], 0` | False | False |
| 1 | `0x0038B19C` | `mov dword ptr [rbx + 0xb0], 1` | False | False |
| 1 | `0x0038B1EF` | `cmp dword ptr [rdx + 0xb0], r12d` | False | False |
| 1 | `0x0038B2AE` | `mov dword ptr [rsi + 0xb0], 4` | False | False |
| 1 | `0x0038B2C8` | `mov dword ptr [rsi + 0xb0], 1` | False | False |
| 1 | `0x0038B2D2` | `mov ecx, dword ptr [rsi + 0xb0]` | False | False |
| 1 | `0x0038B354` | `mov dword ptr [rsi + 0xb0], r12d` | False | False |
| 1 | `0x0038B3B5` | `mov dword ptr [rsi + 0xb0], r12d` | False | False |
| 1 | `0x0038B42D` | `mov dword ptr [rsi + 0xb0], 2` | False | False |
| 1 | `0x0038B44C` | `mov dword ptr [rsi + 0xb0], 3` | False | False |
| 1 | `0x0038B5F7` | `mov dword ptr [rsi + 0xb0], r15d` | False | False |
| 1 | `0x0038B6FB` | `mov dword ptr [rsi + 0xb0], 0` | False | False |
| 1 | `0x0038B71B` | `mov dword ptr [rsi + 0xb0], r14d` | False | False |
| 1 | `0x0038B768` | `mov dword ptr [rsi + 0xb0], r14d` | False | False |
| 1 | `0x0038B844` | `mov rax, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x0038C0E1` | `lea r11, [rsp + 0xb0]` | False | False |
| 1 | `0x00392F66` | `lea rdx, [rsp + 0xb0]` | False | False |
| 1 | `0x0039A95E` | `mov dword ptr [rsp + 0xb0], esi` | False | False |
| 1 | `0x0039AA3E` | `mov dword ptr [rsp + 0xb0], esi` | False | False |
| 1 | `0x0039AB1E` | `mov dword ptr [rsp + 0xb0], esi` | False | False |
| 1 | `0x0039ABFE` | `mov dword ptr [rsp + 0xb0], esi` | False | False |
| 1 | `0x0039AFEE` | `mov dword ptr [rsp + 0xb0], esi` | False | False |
| 1 | `0x0039B0C2` | `mov dword ptr [rsp + 0xb0], esi` | False | False |
| 1 | `0x0039B192` | `mov dword ptr [rsp + 0xb0], esi` | False | False |
| 1 | `0x0039B25E` | `mov dword ptr [rsp + 0xb0], esi` | False | False |
| 1 | `0x003A0A1A` | `mov dword ptr [rsp + 0xb0], ecx` | False | False |
| 1 | `0x003A0B7A` | `mov eax, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x003A0BF2` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x003A0D8C` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x003A3299` | `mov r13, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x003A3C9D` | `mov r13, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x003A8CA8` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x003A8E7C` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x003A90EF` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x003A9203` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x003A974F` | `mov r14, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x003AD30E` | `mov dword ptr [rsp + 0xb0], esi` | False | False |
| 1 | `0x003AD3EE` | `mov dword ptr [rsp + 0xb0], esi` | False | False |
| 1 | `0x003AD4CA` | `mov dword ptr [rsp + 0xb0], esi` | False | False |
| 1 | `0x003AF125` | `mov r13, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x003B0AC0` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x003B0CDB` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x003B4C06` | `mov qword ptr [rbp + 0xb0], rbx` | False | False |
| 1 | `0x003B4DDE` | `mov rbx, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x003B74DB` | `add edx, dword ptr [rbx + 0xb0]` | False | False |
| 1 | `0x003B7520` | `mov edx, dword ptr [rbx + 0xb0]` | False | False |
| 1 | `0x003B763A` | `mov eax, dword ptr [rbx + 0xb0]` | False | False |
| 1 | `0x003B765F` | `add r8d, dword ptr [rbx + 0xb0]` | False | False |
| 1 | `0x003B7D36` | `mov r11d, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x003B7EBB` | `add dword ptr [rsp + 0xb0], r11d` | False | False |
| 1 | `0x003B8CDF` | `add edx, dword ptr [rcx + 0xb0]` | False | False |
| 1 | `0x003B9342` | `mov r8d, dword ptr [rbx + 0xb0]` | False | False |
| 1 | `0x003B93AB` | `mov esi, dword ptr [rbx + 0xb0]` | False | False |
| 1 | `0x003B96DE` | `add edx, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x003B9D50` | `add r11d, dword ptr [rdx + 0xb0]` | False | False |
| 1 | `0x003BA257` | `add ecx, dword ptr [rdi + 0xb0]` | False | False |
| 1 | `0x003BA31E` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x003BA39D` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x003BAAF0` | `mov eax, dword ptr [rbx + 0xb0]` | False | False |
| 1 | `0x003BAC06` | `add edx, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x003BAC6B` | `add edx, dword ptr [rdi + 0xb0]` | False | False |
| 1 | `0x003BAD7F` | `mov eax, dword ptr [rsi + 0xb0]` | False | False |
| 1 | `0x003BB10D` | `lea rcx, [rdi + 0xb0]` | False | False |
| 1 | `0x003BB47A` | `lea r11, [rsp + 0xb0]` | False | False |
| 1 | `0x003BB845` | `lea rcx, [rdi + 0xb0]` | False | False |
| 1 | `0x003BC516` | `mov rax, qword ptr [rdx + 0xb0]` | False | False |
| 1 | `0x003BC533` | `mov rax, qword ptr [rdx + 0xb0]` | False | False |
| 1 | `0x003BCD25` | `mov rax, qword ptr [r11 + 0xb0]` | False | False |
| 1 | `0x003BCD41` | `mov rax, qword ptr [r11 + 0xb0]` | False | False |
| 1 | `0x003BD3CD` | `mov rbx, qword ptr [rax + 0xb0]` | False | False |
| 1 | `0x003BE04A` | `lea rbp, [rcx + 0xb0]` | False | False |
| 1 | `0x003BF6CE` | `mov rax, qword ptr [r8 + 0xb0]` | False | False |
| 1 | `0x003BF6EA` | `mov rax, qword ptr [r8 + 0xb0]` | False | False |
| 1 | `0x003C004B` | `mov dword ptr [rsi + 0xb0], edi` | False | False |
| 1 | `0x003C04D7` | `lock dec dword ptr [rsi + 0xb0]` | False | False |
| 1 | `0x003C0A23` | `mov eax, dword ptr [rcx + 0xb0]` | False | False |
| 1 | `0x003C0A47` | `mov eax, dword ptr [rbx + 0xb0]` | False | False |
| 1 | `0x003C10A4` | `lock inc dword ptr [rcx + 0xb0]` | False | False |
| 1 | `0x003C10DE` | `mov eax, dword ptr [rdi + 0xb0]` | False | False |
| 1 | `0x003C1813` | `mov byte ptr [rdi + 0xb0], 0` | False | False |
| 1 | `0x003C195A` | `mov rax, qword ptr [rcx + 0xb0]` | False | False |
| 1 | `0x003C1961` | `mov qword ptr [rbx + 0xb0], rax` | False | False |
| 1 | `0x003C1968` | `lock cmpxchg qword ptr [rcx + 0xb0], rbx` | False | False |
| 1 | `0x003C1976` | `mov qword ptr [rbx + 0xb0], rax` | False | False |
| 1 | `0x003C1984` | `lock cmpxchg qword ptr [rcx + 0xb0], rbx` | False | False |
| 1 | `0x003C199B` | `and qword ptr [rbx + 0xb0], 0` | False | False |
| 1 | `0x003C1AA8` | `mov rcx, qword ptr [rdi + 0xb0]` | False | False |
| 1 | `0x003C1AB4` | `mov rbx, qword ptr [rcx + 0xb0]` | False | False |
| 1 | `0x003C1E63` | `mov rdi, qword ptr [rax + 0xb0]` | False | False |
| 1 | `0x003C1F69` | `mov rax, qword ptr [rax + 0xb0]` | False | False |
| 1 | `0x003C22A0` | `mov rbx, qword ptr [rbx + 0xb0]` | False | False |
| 1 | `0x003C24E0` | `mov rdx, qword ptr [rdx + 0xb0]` | False | False |
| 1 | `0x003C25E6` | `mov rdi, qword ptr [rdi + 0xb0]` | False | False |
| 1 | `0x003C2907` | `mov rdi, qword ptr [rdi + 0xb0]` | False | False |
| 1 | `0x003C29F8` | `mov rax, qword ptr [rbx + 0xb0]` | False | False |
| 1 | `0x003C2A05` | `mov rax, qword ptr [rax + 0xb0]` | False | False |
| 1 | `0x003C31E5` | `mov ecx, dword ptr [rcx + 0xb0]` | False | False |
| 1 | `0x003C3211` | `mov ebx, dword ptr [rdx + 0xb0]` | False | False |
| 1 | `0x003C35C6` | `add r8d, dword ptr [r9 + 0xb0]` | False | False |
| 1 | `0x003C3ACD` | `mov dword ptr [rsi + 0xb0], ebx` | False | False |
| 1 | `0x003C3ADF` | `mov dword ptr [rsi + 0xb0], eax` | False | False |
| 1 | `0x003C3AE5` | `mov r8d, dword ptr [rsi + 0xb0]` | False | False |
| 1 | `0x003C3FFE` | `add r10d, dword ptr [r8 + 0xb0]` | False | False |
| 1 | `0x003C43A3` | `mov eax, dword ptr [rcx + 0xb0]` | False | False |
| 1 | `0x003C46BC` | `mov ecx, dword ptr [rax + 0xb0]` | False | False |
| 1 | `0x003C4BE3` | `mov eax, dword ptr [rcx + 0xb0]` | False | False |
| 1 | `0x003C4CD7` | `mov ecx, dword ptr [rax + 0xb0]` | False | False |
| 1 | `0x003C6995` | `mov qword ptr [rcx + 0xb0], r15` | False | False |
| 1 | `0x003C7B1C` | `mov rax, qword ptr [r8 + 0xb0]` | False | False |
| 1 | `0x003C7B38` | `mov rax, qword ptr [r8 + 0xb0]` | False | False |
| 1 | `0x003C7BF4` | `mov rax, qword ptr [r8 + 0xb0]` | False | False |
| 1 | `0x003C7C10` | `mov rax, qword ptr [r8 + 0xb0]` | False | False |
| 1 | `0x003C7CF3` | `mov rax, qword ptr [rbx + 0xb0]` | False | False |
| 1 | `0x003C7D0F` | `mov rax, qword ptr [rbx + 0xb0]` | False | False |
| 1 | `0x003CBA5A` | `mov eax, dword ptr [rdx + 0xb0]` | False | False |
| 1 | `0x003CBD6C` | `mov eax, dword ptr [rbx + 0xb0]` | False | False |
| 1 | `0x003CC102` | `mov eax, dword ptr [rdi + 0xb0]` | False | False |
| 1 | `0x003CC183` | `mov eax, dword ptr [rdi + 0xb0]` | False | False |
| 1 | `0x003CC240` | `mov eax, dword ptr [rdi + 0xb0]` | False | False |
| 1 | `0x003CC27D` | `mov eax, dword ptr [rdi + 0xb0]` | False | False |
| 1 | `0x003CC372` | `mov eax, dword ptr [rdx + 0xb0]` | False | False |
| 1 | `0x003CD3E5` | `lea rcx, [rdi + 0xb0]` | False | False |
| 1 | `0x003CD519` | `mov dword ptr [rdi + 0xb0], eax` | False | False |
| 1 | `0x003CD9A8` | `mov eax, dword ptr [rcx + 0xb0]` | False | False |
| 1 | `0x003CD9F6` | `lea rcx, [rsi + 0xb0]` | False | False |
| 1 | `0x003CDA3C` | `lea rcx, [rsi + 0xb0]` | False | False |
| 1 | `0x003CE29D` | `mov ecx, dword ptr [rdx + 0xb0]` | False | False |
| 1 | `0x003D0BDD` | `mov r9, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x003D114B` | `lea r11, [rsp + 0xb0]` | False | False |
| 1 | `0x003D1286` | `lea rax, [rsp + 0xb0]` | False | False |
| 1 | `0x003D129E` | `mov ecx, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x003D13EA` | `mov ecx, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x003D13F7` | `mov dword ptr [rsp + 0xb0], ecx` | False | False |
| 1 | `0x003D17DF` | `and dword ptr [rsp + 0xb0], r15d` | False | False |
| 1 | `0x003D187D` | `mov dword ptr [rsp + 0xb0], 1` | False | False |
| 1 | `0x003D18D7` | `cmp dword ptr [rsp + 0xb0], 0` | False | False |
| 1 | `0x003D3858` | `cmp dword ptr [rsp + 0xb0], ebx` | False | False |
| 1 | `0x003E6886` | `mov rax, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x003F6651` | `mov rbx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x003FB3DD` | `mov eax, dword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x003FB7AF` | `mov rax, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x003FC133` | `mov r12, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x00402AEB` | `mov qword ptr [rsp + 0xb0], rax` | False | False |
| 1 | `0x00402DD9` | `mov rcx, qword ptr [rsp + 0xb0]` | False | False |
| 1 | `0x0040353A` | `mov dword ptr [r10 + 0xb0], eax` | False | False |
| 1 | `0x00405324` | `movsxd rsi, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x00406678` | `mov dword ptr [rbp + 0xb0], eax` | False | False |
| 1 | `0x00406871` | `add r15d, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x00406990` | `mov ecx, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x00406C6B` | `add r15d, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x00406F84` | `add r13d, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x00407059` | `add r12d, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x00407255` | `mov ecx, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x00407547` | `mov ecx, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x00407815` | `mov ecx, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x00407B36` | `mov ecx, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x004099BC` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x0040A57C` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x0040CD70` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x0040D710` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x0040DD10` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x0040DDB8` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x0040E6A5` | `mov byte ptr [rbp + 0xb0], cl` | False | False |
| 1 | `0x0040E6AB` | `movsx ecx, byte ptr [rbp + 0xb0]` | False | False |
| 1 | `0x0040EB1C` | `lea rcx, [rbp + 0xb0]` | False | False |
| 1 | `0x0040EB2D` | `lea rcx, [rbp + 0xb0]` | False | False |
| 1 | `0x0040EB5B` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x0040F688` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x0040F708` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x0040F7C0` | `mov rcx, qword ptr [rdx + 0xb0]` | False | False |
| 1 | `0x004102C9` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x004102D6` | `and dword ptr [rbp + 0xb0], 0xfffffffe` | False | False |
| 1 | `0x00411267` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x00412F4C` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x004144F0` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x00415312` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x004158CC` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x00415AC1` | `mov dword ptr [rbp + 0xb0], 0x5b` | False | False |
| 1 | `0x00415CDA` | `lea rcx, [rbp + 0xb0]` | False | False |
| 1 | `0x00416BA0` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x00417214` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x004175BD` | `mov rcx, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x00419E40` | `mov rcx, qword ptr [rdx + 0xb0]` | False | False |
| 1 | `0x0041A8ED` | `mov rcx, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x0041AD65` | `lea rcx, [rbp + 0xb0]` | False | False |
| 1 | `0x0041AE3E` | `lea rcx, [rbp + 0xb0]` | False | False |
| 1 | `0x0041AED1` | `lea rcx, [rbp + 0xb0]` | False | False |
| 1 | `0x0041B169` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x0041B210` | `mov rcx, qword ptr [rdx + 0xb0]` | False | False |
| 1 | `0x0041B21C` | `mov rcx, qword ptr [rdx + 0xb0]` | False | False |
| 1 | `0x0041B22F` | `mov rcx, qword ptr [rdx + 0xb0]` | False | False |
| 1 | `0x0041B56C` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x0041B8B0` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x0041BC10` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x0041BC1C` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x0041BEE8` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x0041D0FA` | `mov rax, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x0041D67A` | `mov byte ptr [rbp + 0xb0], cl` | False | False |
| 1 | `0x0041D680` | `movsx ecx, byte ptr [rbp + 0xb0]` | False | False |
| 1 | `0x0041DA4A` | `movzx eax, byte ptr [rbp + 0xb0]` | False | False |
| 1 | `0x0041DC5C` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x0041ED1C` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x0041F5BD` | `lea rcx, [rbp + 0xb0]` | False | False |
| 1 | `0x004205C7` | `lea rcx, [rbp + 0xb0]` | False | False |
| 1 | `0x00421594` | `mov byte ptr [rbp + 0xb0], cl` | False | False |
| 1 | `0x0042159A` | `movsx ecx, byte ptr [rbp + 0xb0]` | False | False |
| 1 | `0x004219D8` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x00421ACC` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x0042376C` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x00424040` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x004243B0` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x004245A0` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x004247C4` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x00424913` | `mov rcx, qword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x004259C8` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x004259D8` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x00426018` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x004263BF` | `lea rcx, [rbp + 0xb0]` | False | False |
| 1 | `0x00426446` | `lea rcx, [rbp + 0xb0]` | False | False |
| 1 | `0x00426770` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x00427B4C` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x0042A089` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x0042A096` | `and dword ptr [rbp + 0xb0], 0xfffffffe` | False | False |
| 1 | `0x0042B84C` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x0042B87C` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x0042B942` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x0042B9F8` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x0042BA1B` | `lea rcx, [rbp + 0xb0]` | False | False |
| 1 | `0x0042BA6D` | `lea rcx, [rbp + 0xb0]` | False | False |
| 1 | `0x0042BAB4` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x0042BB16` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x0042BB39` | `lea rcx, [rbp + 0xb0]` | False | False |
| 1 | `0x0042BB8B` | `lea rcx, [rbp + 0xb0]` | False | False |
| 1 | `0x0042BBD2` | `lea rcx, [rdx + 0xb0]` | False | False |
| 1 | `0x0042C009` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x0042C016` | `and dword ptr [rbp + 0xb0], 0xfffffffe` | False | False |
| 1 | `0x0042C061` | `mov eax, dword ptr [rbp + 0xb0]` | False | False |
| 1 | `0x0042C06E` | `and dword ptr [rbp + 0xb0], 0xfffffffe` | False | False |

## High-score contexts

### score 7 @ `0x000E10D8`

```asm
0x000E10AE: mov rcx, qword ptr [rax + 0x2c0]
0x000E10B5: mov eax, dword ptr [r8]
0x000E10B8: mov dword ptr [rdx + rcx + 0x50], eax
0x000E10BC: ret
0x000E10BD: int3
0x000E10BE: int3
0x000E10BF: int3
0x000E10C0: movsxd rax, dword ptr [rdx]
0x000E10C3: imul rdx, rax, 0xd8
0x000E10CA: mov rax, qword ptr [rcx + 8]
0x000E10CE: mov rcx, qword ptr [rax + 0x2c0]
0x000E10D5: mov eax, dword ptr [r8]
0x000E10D8: mov dword ptr [rdx + rcx + 0xb0], eax
0x000E10DF: ret
0x000E10E0: movsxd rax, dword ptr [rdx]
0x000E10E3: imul rdx, rax, 0xd8
0x000E10EA: mov rax, qword ptr [rcx + 8]
0x000E10EE: mov rcx, qword ptr [rax + 0x2c0]
0x000E10F5: mov eax, dword ptr [r8]
0x000E10F8: mov dword ptr [rdx + rcx + 0x84], eax
0x000E10FF: ret
0x000E1100: movsxd rax, dword ptr [rdx]
0x000E1103: cmp dword ptr [r8], 0
0x000E1107: setne r8b
0x000E110B: imul rdx, rax, 0xd8
```

### score 7 @ `0x000E119B`

```asm
0x000E1175: mov eax, dword ptr [r8]
0x000E1178: mov dword ptr [rdx + rcx + 0x7c], eax
0x000E117C: ret
0x000E117D: int3
0x000E117E: int3
0x000E117F: int3
0x000E1180: movsxd rax, dword ptr [rdx]
0x000E1183: mov r9d, dword ptr [r8]
0x000E1186: imul rdx, rax, 0xd8
0x000E118D: mov rax, qword ptr [rcx + 8]
0x000E1191: neg r9d
0x000E1194: mov rcx, qword ptr [rax + 0x2c0]
0x000E119B: mov dword ptr [rdx + rcx + 0xb0], r9d
0x000E11A3: ret
0x000E11A4: int3
0x000E11A5: int3
0x000E11A6: int3
0x000E11A7: int3
0x000E11A8: int3
0x000E11A9: int3
0x000E11AA: int3
0x000E11AB: int3
0x000E11AC: int3
0x000E11AD: int3
0x000E11AE: int3
```

### score 4 @ `0x0003799B`

```asm
0x0003795C: xor ecx, 0x6f
0x0003795F: mov byte ptr [rbp + 0xb9], cl
0x00037965: movsx ecx, byte ptr [rbp + 0xb9]
0x0003796C: xor ecx, 0x73
0x0003796F: mov byte ptr [rbp + 0xba], cl
0x00037975: movsx ecx, byte ptr [rbp + 0xba]
0x0003797C: xor ecx, 0x74
0x0003797F: mov byte ptr [rbp + 0xbb], cl
0x00037985: xor eax, eax
0x00037987: mov byte ptr [rbp + 0xbc], al
0x0003798D: movzx eax, byte ptr [rbp + 0xb8]
0x00037994: lea rdx, [rbp + 0x2c0]
0x0003799B: lea rcx, [rbp + 0xb0]
0x000379A2: call 0x14021d400
0x000379A7: mov rdx, rax
0x000379AA: lea rcx, [rsp + 0x58]
0x000379AF: call 0x140029c50
0x000379B4: movzx ebx, al
0x000379B7: lea rcx, [rbp + 0x2c0]
0x000379BE: call 0x140032ef0
0x000379C3: test bl, bl
0x000379C5: je 0x1400379d1
0x000379C7: mov edi, 0x10f
0x000379CC: jmp 0x140037da6
0x000379D1: mov dword ptr [rbp + 0x40], 0x29
```

### score 4 @ `0x00078B83`

```asm
0x00078B3E: lea rcx, [rsp + 0x9c8]
0x00078B46: call 0x140032ef0
0x00078B4B: nop
0x00078B4C: lea rcx, [rsp + 0x9e8]
0x00078B54: call 0x140032ef0
0x00078B59: nop
0x00078B5A: lea rcx, [rsp + 0x978]
0x00078B62: call 0x140032ef0
0x00078B67: lea rdx, [rsp + 0x1a0]
0x00078B6F: mov rcx, r12
0x00078B72: call 0x14013c100
0x00078B77: mov qword ptr [rsp + 0xa8], 0
0x00078B83: mov qword ptr [rsp + 0xb0], 0
0x00078B8F: mov dword ptr [rsp + 0xb8], r14d
0x00078B97: mov qword ptr [rsp + 0xc0], r14
0x00078B9F: mov qword ptr [rsp + 0xc8], r14
0x00078BA7: mov qword ptr [rsp + 0xd0], r14
0x00078BAF: mov qword ptr [rsp + 0xd8], r14
0x00078BB7: cmp qword ptr [r15 + 0x12a8], 0
0x00078BBF: je 0x140078c02
0x00078BC1: lea rdx, [rsp + 0x2c0]
0x00078BC9: mov rcx, r12
0x00078BCC: call 0x14013bfb0
0x00078BD1: movups xmm0, xmmword ptr [rax]
0x00078BD4: movups xmmword ptr [rsp + 0xa8], xmm0
```

### score 4 @ `0x000B23C1`

```asm
0x000B2385: lea rcx, [rdi + 0x80]
0x000B238C: call 0x14009d240
0x000B2391: mov rdx, qword ptr [rbp + 0xa8]
0x000B2398: test rdx, rdx
0x000B239B: je 0x1400b23c9
0x000B239D: mov r8, qword ptr [rbp + 0xb8]
0x000B23A4: sub r8, rdx
0x000B23A7: sar r8, 5
0x000B23AB: lea rcx, [rbp + 0xa8]
0x000B23B2: call 0x14006f460
0x000B23B7: mov qword ptr [rbp + 0xa8], r12
0x000B23BE: xorps xmm0, xmm0
0x000B23C1: movdqa xmmword ptr [rbp + 0xb0], xmm0
0x000B23C9: lea rcx, [rbp + 0x88]
0x000B23D0: call 0x14006a240
0x000B23D5: mov eax, dword ptr [rbx + 0x4ec]
0x000B23DB: mov dword ptr [rdi + 0x78], eax
0x000B23DE: mov rax, qword ptr [rbx + 0x50]
0x000B23E2: cmp qword ptr [rbx + 0x48], rax
0x000B23E6: jne 0x1400b24fa
0x000B23EC: mov edi, r12d
0x000B23EF: mov rcx, qword ptr [rbx + 0x2c8]
0x000B23F6: sub rcx, qword ptr [rbx + 0x2c0]
0x000B23FD: movabs rsi, 0x4bda12f684bda13
0x000B2407: mov rax, rsi
```

### score 4 @ `0x000C917D`

```asm
0x000C9141: mov byte ptr [rbp + 0x2e6], cl
0x000C9147: movsx ecx, byte ptr [rbp + 0x2e6]
0x000C914E: xor ecx, 0x2e
0x000C9151: mov byte ptr [rbp + 0x2e7], cl
0x000C9157: xor eax, eax
0x000C9159: mov byte ptr [rbp + 0x2e8], al
0x000C915F: movzx eax, byte ptr [rbp + 0x2c0]
0x000C9166: lea rdx, [rbp + 0x368]
0x000C916D: lea rcx, [rbp + 0x2b8]
0x000C9174: call 0x1400b9240
0x000C9179: nop
0x000C917A: xorps xmm0, xmm0
0x000C917D: movdqu xmmword ptr [rbp + 0xb0], xmm0
0x000C9185: mov qword ptr [rbp + 0xc0], rsi
0x000C918C: xor eax, eax
0x000C918E: movzx r9d, al
0x000C9192: lea r8, [rbp + 0x388]
0x000C9199: lea rdx, [rbp + 0x368]
0x000C91A0: lea rcx, [rbp + 0xb0]
0x000C91A7: call 0x1400b6270
0x000C91AC: nop
0x000C91AD: lea r9, [rip - 0x962c4]
0x000C91B4: mov edx, 0x20
0x000C91B9: lea r8d, [rdx - 0x1f]
0x000C91BD: lea rcx, [rbp + 0x368]
```

### score 4 @ `0x000C91A0`

```asm
0x000C915F: movzx eax, byte ptr [rbp + 0x2c0]
0x000C9166: lea rdx, [rbp + 0x368]
0x000C916D: lea rcx, [rbp + 0x2b8]
0x000C9174: call 0x1400b9240
0x000C9179: nop
0x000C917A: xorps xmm0, xmm0
0x000C917D: movdqu xmmword ptr [rbp + 0xb0], xmm0
0x000C9185: mov qword ptr [rbp + 0xc0], rsi
0x000C918C: xor eax, eax
0x000C918E: movzx r9d, al
0x000C9192: lea r8, [rbp + 0x388]
0x000C9199: lea rdx, [rbp + 0x368]
0x000C91A0: lea rcx, [rbp + 0xb0]
0x000C91A7: call 0x1400b6270
0x000C91AC: nop
0x000C91AD: lea r9, [rip - 0x962c4]
0x000C91B4: mov edx, 0x20
0x000C91B9: lea r8d, [rdx - 0x1f]
0x000C91BD: lea rcx, [rbp + 0x368]
0x000C91C4: call 0x1403b2554
0x000C91C9: mov r8d, edi
0x000C91CC: lea rdx, [rbp + 0xb0]
0x000C91D3: mov rcx, rbx
0x000C91D6: call 0x1400c6ef0
0x000C91DB: nop
```

### score 4 @ `0x001AD743`

```asm
0x001AD704: mov rbx, rax
0x001AD707: mov qword ptr [rsp + 0x48], rax
0x001AD70C: mov ecx, dword ptr [rsp + 0x34]
0x001AD710: test ecx, ecx
0x001AD712: je 0x1401ad760
0x001AD714: xor eax, eax
0x001AD716: mov qword ptr [rsp + 0x98], rax
0x001AD71E: mov qword ptr [rsp + 0xa0], rax
0x001AD726: lea rax, [rip + 0x29dd4b]
0x001AD72D: mov qword ptr [rsp + 0x90], rax
0x001AD735: mov dword ptr [rsp + 0xa8], ecx
0x001AD73C: lea rax, [rip + 0x29e415]
0x001AD743: mov qword ptr [rsp + 0xb0], rax
0x001AD74B: lea rdx, [rip + 0x5de25e]
0x001AD752: lea rcx, [rsp + 0x90]
0x001AD75A: call 0x1403d25d0
0x001AD75F: nop
0x001AD760: movsxd r15, esi
0x001AD763: lea r14, [rdi + 0x2c0]
0x001AD76A: lea r14, [r14 + r15*8]
0x001AD76E: lea rax, [rsp + 0x48]
0x001AD773: cmp r14, rax
0x001AD776: je 0x1401ad7e0
0x001AD778: mov rcx, qword ptr [r14]
0x001AD77B: test rcx, rcx
```

### score 4 @ `0x001F90CA`

```asm
0x001F909A: call 0x140291876
0x001F909F: mov dword ptr [rbp - 0x50], eax
0x001F90A2: test eax, eax
0x001F90A4: jne 0x1401f9f19
0x001F90AA: jmp 0x1401f90bf
0x001F90AC: mov rcx, rax
0x001F90AF: call 0x140291840
0x001F90B4: mov dword ptr [rbp - 0x30], eax
0x001F90B7: test eax, eax
0x001F90B9: jne 0x1401fb038
0x001F90BF: movsxd rbx, r13d
0x001F90C2: mov rcx, qword ptr [rdi + rbx*8 + 0x1c8]
0x001F90CA: mov qword ptr [rbp + 0xb0], rcx
0x001F90D1: mov rax, qword ptr [rdi]
0x001F90D4: mov r9, qword ptr [rbp + rbx*8 + 0x2c0]
0x001F90DC: mov r8, rcx
0x001F90DF: lea rdx, [rbp + 0xce0]
0x001F90E6: mov rcx, rdi
0x001F90E9: call qword ptr [rax + 0x60]
0x001F90EC: mov byte ptr [rsp + 0x52], al
0x001F90F0: mov byte ptr [rsp + 0x54], 1
0x001F90F5: xor ecx, ecx
0x001F90F7: mov qword ptr [rbp + 0x58], rcx
0x001F90FB: test al, al
0x001F90FD: je 0x1401f9141
```

### score 4 @ `0x0026A7D4`

```asm
0x0026A79F: call 0x140226a40
0x0026A7A4: mov r11, rax
0x0026A7A7: mov r10, qword ptr [rax]
0x0026A7AA: mov rcx, qword ptr [rax + 8]
0x0026A7AE: sub rcx, r10
0x0026A7B1: cmp rcx, 0x20
0x0026A7B5: jne 0x14026a7fb
0x0026A7B7: mov dword ptr [rsp + 0xa8], ecx
0x0026A7BE: mov rax, qword ptr [rax + 8]
0x0026A7C2: sub rax, r10
0x0026A7C5: mov dword ptr [rsp + 0xb0], eax
0x0026A7CC: lea rcx, [rsp + 0xa8]
0x0026A7D4: lea rdx, [rsp + 0xb0]
0x0026A7DC: cmp eax, 0x20
0x0026A7DF: cmovbe rcx, rdx
0x0026A7E3: mov r8d, dword ptr [rcx]
0x0026A7E6: mov rdx, r10
0x0026A7E9: lea rcx, [rsp + 0x2b8]
0x0026A7F1: call 0x1403d1f90
0x0026A7F6: jmp 0x14026a893
0x0026A7FB: xor eax, eax
0x0026A7FD: mov byte ptr [rsp + 0x33], al
0x0026A801: mov qword ptr [rsp + 0x2b8], rax
0x0026A809: mov qword ptr [rsp + 0x2c0], rax
0x0026A811: mov qword ptr [rsp + 0x2c8], rax
```
