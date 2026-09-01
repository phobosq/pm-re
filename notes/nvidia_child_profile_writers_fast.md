# Focused NVIDIA child profile/cache writers

Range `0x001D4A80..0x001F1000`
hits: `175`

| RVA | base | disp | label | instruction |
|---|---|---:|---|---|
| `0x001D4B3B` | `rbx` | `0x260` | flag0 | `mov dword ptr [rbx + 0x260], edi` |
| `0x001D4B43` | `rbx` | `0x264` | flag1 | `mov qword ptr [rbx + 0x264], rax` |
| `0x001D4B50` | `rbx` | `0x270` | state_idx | `mov qword ptr [rbx + 0x270], 0xffffffffffffffff` |
| `0x001D4B5B` | `rbx` | `0x278` | retry | `mov qword ptr [rbx + 0x278], rdi` |
| `0x001D4B6F` | `rbx` | `0x398` | profile_valid_flags | `mov byte ptr [rbx + 0x398], al` |
| `0x001D4B82` | `rbx` | `0x3A0` | gpu_table_key | `mov qword ptr [rbx + 0x3a0], 0xffffffffffffffff` |
| `0x001D4BB6` | `rbx` | `0x3A0` | gpu_table_key | `mov dword ptr [rbx + 0x3a0], eax` |
| `0x001D4D3A` | `rbp` | `0x2C` | reg_9A0298_field | `mov byte ptr [rbp + 0x2c], cl` |
| `0x001D4DB2` | `rbp` | `0x38` | reg_9A029C_field | `mov byte ptr [rbp + 0x38], cl` |
| `0x001D4EF2` | `rbp` | `0x44` | reg_9A02A0_field | `mov dword ptr [rbp + 0x44], 0x54` |
| `0x001D51C6` | `r10` | `0x8` | reg_9A0290_field | `mov dword ptr [r10 + rax*8 + 8], 0xffffffff` |
| `0x001D51F8` | `rsp` | `0x38` | reg_9A029C_field | `mov dword ptr [rsp + 0x38], eax` |
| `0x001D5381` | `rbp` | `0x8` | reg_9A0290_field | `mov byte ptr [rbp + 8], cl` |
| `0x001D5461` | `rsp` | `0x44` | reg_9A02A0_field | `mov dword ptr [rsp + 0x44], 0x23d` |
| `0x001D5DD0` | `rsp` | `0x8` | reg_9A0290_field | `mov qword ptr [rsp + 8], rbx` |
| `0x001D5E45` | `rsp` | `0x8` | reg_9A0290_field | `mov qword ptr [rsp + 8], rcx` |
| `0x001D5EBA` | `rbx` | `0x8` | reg_9A0290_field | `mov qword ptr [rbx + 8], rdi` |
| `0x001D5ED5` | `rsp` | `0x8` | reg_9A0290_field | `mov qword ptr [rsp + 8], rcx` |
| `0x001D5FA9` | `rbx` | `0x8` | reg_9A0290_field | `mov qword ptr [rbx + 8], rcx` |
| `0x001D656A` | `rbp` | `0x8` | reg_9A0290_field | `mov qword ptr [rbp + 8], rax` |
| `0x001D6576` | `rbp` | `0x8` | reg_9A0290_field | `mov dword ptr [rbp + 8], 0x1001c` |
| `0x001D65BB` | `rsp` | `0x38` | reg_9A029C_field | `mov dword ptr [rsp + 0x38], 0x46f` |
| `0x001D67D4` | `rbp` | `0x38` | reg_9A029C_field | `mov qword ptr [rbp + 0x38], rbx` |
| `0x001D6E56` | `rsp` | `0x38` | reg_9A029C_field | `mov qword ptr [rsp + 0x38], rsi` |
| `0x001D6EE6` | `rsp` | `0x38` | reg_9A029C_field | `mov qword ptr [rsp + 0x38], rsi` |
| `0x001D712E` | `rsp` | `0x38` | reg_9A029C_field | `mov dword ptr [rsp + 0x38], 0x3c` |
| `0x001D71A3` | `rsp` | `0x44` | reg_9A02A0_field | `mov byte ptr [rsp + 0x44], al` |
| `0x001D74D1` | `rdx` | `0x8` | reg_9A0290_field | `mov word ptr [rdx + 8], ax` |
| `0x001D7508` | `rbx` | `0x8` | reg_9A0290_field | `mov word ptr [rbx + 8], ax` |
| `0x001D7834` | `rsp` | `0x38` | reg_9A029C_field | `mov qword ptr [rsp + 0x38], r15` |
| `0x001D78B0` | `rsp` | `0x8` | reg_9A0290_field | `mov qword ptr [rsp + 8], rbx` |
| `0x001D7902` | `rdi` | `0x2C` | reg_9A0298_field | `mov dword ptr [rdi + 0x2c], eax` |
| `0x001D7908` | `rdi` | `0x38` | reg_9A029C_field | `mov dword ptr [rdi + 0x38], eax` |
| `0x001D790E` | `rdi` | `0x44` | reg_9A02A0_field | `mov dword ptr [rdi + 0x44], eax` |
| `0x001D7919` | `rdi` | `0x8` | reg_9A0290_field | `mov dword ptr [rdi + 8], eax` |
| `0x001D7A74` | `rsp` | `0x38` | reg_9A029C_field | `mov dword ptr [rsp + 0x38], ecx` |
| `0x001D8409` | `rbp` | `0x8` | reg_9A0290_field | `movdqu xmmword ptr [rbp + 8], xmm0` |
| `0x001D8456` | `rbp` | `0x8` | reg_9A0290_field | `movdqu xmmword ptr [rbp + 8], xmm0` |
| `0x001D84EA` | `rsp` | `0x38` | reg_9A029C_field | `mov dword ptr [rsp + 0x38], eax` |
| `0x001D8FE0` | `rbx` | `0x398` | profile_valid_flags | `mov byte ptr [rbx + r8 + 0x398], 1` |
| `0x001D9657` | `rbp` | `0x8` | reg_9A0290_field | `mov byte ptr [rbp + 8], cl` |
| `0x001D9D9B` | `rbp` | `0x38` | reg_9A029C_field | `mov dword ptr [rbp + 0x38], eax` |
| `0x001D9DA4` | `rbp` | `0x44` | reg_9A02A0_field | `mov dword ptr [rbp + 0x44], ecx` |
| `0x001DA013` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], eax` |
| `0x001DA01F` | `rsp` | `0x38` | reg_9A029C_field | `mov dword ptr [rsp + 0x38], 0x4fe` |
| `0x001DA17B` | `rbp` | `0x8` | reg_9A0290_field | `mov byte ptr [rbp + 8], cl` |
| `0x001DA7EB` | `rbx` | `0x3A0` | gpu_table_key | `mov dword ptr [rbx + 0x3a0], eax` |
| `0x001DA817` | `rbx` | `0x260` | flag0 | `mov qword ptr [rbx + 0x260], rax` |
| `0x001DA81E` | `rbx` | `0x268` | flag2 | `mov dword ptr [rbx + 0x268], eax` |
| `0x001DA85E` | `rbx` | `0x27C` | counter | `mov dword ptr [rbx + 0x27c], edi` |
| `0x001DA8AD` | `rsp` | `0x38` | reg_9A029C_field | `mov dword ptr [rsp + 0x38], r8d` |
| `0x001DADA9` | `rbp` | `0x8` | reg_9A0290_field | `mov byte ptr [rbp + 8], al` |
| `0x001DB11D` | `rbp` | `0x44` | reg_9A02A0_field | `mov byte ptr [rbp + 0x44], al` |
| `0x001DB4BF` | `rbp` | `0x2C` | reg_9A0298_field | `mov byte ptr [rbp + 0x2c], al` |
| `0x001DB55B` | `rbp` | `0x38` | reg_9A029C_field | `mov byte ptr [rbp + 0x38], cl` |
| `0x001DB9E0` | `rsp` | `0x8` | reg_9A0290_field | `mov qword ptr [rsp + 8], rbx` |
| `0x001DBA9B` | `rbx` | `0x3A0` | gpu_table_key | `mov dword ptr [rbx + 0x3a0], eax` |
| `0x001DBAEE` | `rbx` | `0x260` | flag0 | `movsd qword ptr [rbx + 0x260], xmm0` |
| `0x001DBAFA` | `rbx` | `0x268` | flag2 | `mov dword ptr [rbx + 0x268], eax` |
| `0x001DBB63` | `rbx` | `0x278` | retry | `mov dword ptr [rbx + 0x278], eax` |
| `0x001DC6C9` | `rsp` | `0x38` | reg_9A029C_field | `mov qword ptr [rsp + 0x38], rcx` |
| `0x001DCCE4` | `rbp` | `0x8` | reg_9A0290_field | `mov qword ptr [rbp + 8], rax` |
| `0x001DCD2D` | `rsp` | `0x38` | reg_9A029C_field | `mov qword ptr [rsp + 0x38], rcx` |
| `0x001DDAF5` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], ebx` |
| `0x001DE1AA` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], ebx` |
| `0x001DE968` | `rbx` | `0x274` | max_idx | `mov dword ptr [rbx + 0x274], edi` |
| `0x001DE987` | `rbx` | `0x278` | retry | `mov dword ptr [rbx + 0x278], ecx` |
| `0x001DE98D` | `rbx` | `0x270` | state_idx | `mov dword ptr [rbx + 0x270], edi` |
| `0x001DE998` | `rbx` | `0x27C` | counter | `mov dword ptr [rbx + 0x27c], ecx` |
| `0x001DE9B1` | `rbx` | `0x27C` | counter | `mov dword ptr [rbx + 0x27c], eax` |
| `0x001DE9DD` | `rbx` | `0x278` | retry | `mov dword ptr [rbx + 0x278], eax` |
| `0x001DEA11` | `rsp` | `0x38` | reg_9A029C_field | `mov byte ptr [rsp + 0x38], cl` |
| `0x001DEB01` | `rsp` | `0x44` | reg_9A02A0_field | `mov byte ptr [rsp + 0x44], al` |
| `0x001DF25C` | `rbx` | `0x278` | retry | `mov dword ptr [rbx + 0x278], eax` |
| `0x001DF454` | `rbx` | `0x278` | retry | `mov dword ptr [rbx + 0x278], eax` |
| `0x001DF64B` | `rax` | `0x8` | reg_9A0290_field | `mov qword ptr [rax + 8], rbx` |
| `0x001DFACF` | `rsp` | `0x38` | reg_9A029C_field | `mov qword ptr [rsp + 0x38], rcx` |
| `0x001E0546` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], 0xdc` |
| `0x001E0B40` | `rsp` | `0x8` | reg_9A0290_field | `mov qword ptr [rsp + 8], rbx` |
| `0x001E0B8E` | `rbx` | `0x8` | reg_9A0290_field | `add qword ptr [rbx + 8], 0x10` |
| `0x001E0BC0` | `rbx` | `0x8` | reg_9A0290_field | `add qword ptr [rbx + 8], 0x10` |
| `0x001E0BD0` | `rsp` | `0x8` | reg_9A0290_field | `mov qword ptr [rsp + 8], rbx` |
| `0x001E0C8C` | `rbx` | `0x8` | reg_9A0290_field | `add qword ptr [rbx + 8], 0x28` |
| `0x001E0D3A` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], 0x9a0290` |
| `0x001E0D42` | `rsp` | `0x44` | reg_9A02A0_field | `mov dword ptr [rsp + 0x44], 0x9a0294` |
| `0x001E0DB0` | `rbx` | `0x8` | reg_9A0290_field | `mov dword ptr [rbx + 8], ecx` |
| `0x001E0E12` | `rbx` | `0x2C` | reg_9A0298_field | `mov dword ptr [rbx + 0x2c], eax` |
| `0x001E0E3A` | `rbx` | `0x38` | reg_9A029C_field | `mov dword ptr [rbx + 0x38], eax` |
| `0x001E0E5E` | `rbx` | `0x44` | reg_9A02A0_field | `mov dword ptr [rbx + 0x44], eax` |
| `0x001E1E41` | `rsp` | `0x38` | reg_9A029C_field | `movups xmmword ptr [rsp + 0x38], xmm0` |
| `0x001E2EB5` | `rsp` | `0x38` | reg_9A029C_field | `movups xmmword ptr [rsp + 0x38], xmm0` |
| `0x001E314A` | `rbp` | `0x2C` | reg_9A0298_field | `mov byte ptr [rbp + 0x2c], cl` |
| `0x001E31E6` | `rbp` | `0x38` | reg_9A029C_field | `mov byte ptr [rbp + 0x38], cl` |
| `0x001E3282` | `rbp` | `0x44` | reg_9A02A0_field | `mov byte ptr [rbp + 0x44], cl` |
| `0x001E33BC` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], edx` |
| `0x001E3B10` | `rsp` | `0x38` | reg_9A029C_field | `mov dword ptr [rsp + 0x38], edx` |
| `0x001E3CF8` | `rbp` | `0x8` | reg_9A0290_field | `mov byte ptr [rbp + 8], cl` |
| `0x001E3ECE` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], eax` |
| `0x001E41E0` | `rsp` | `0x44` | reg_9A02A0_field | `mov dword ptr [rsp + 0x44], 0x37` |
| `0x001E41E8` | `rsp` | `0x38` | reg_9A029C_field | `mov dword ptr [rsp + 0x38], 0x5a` |
| `0x001E4735` | `rbp` | `0x8` | reg_9A0290_field | `mov byte ptr [rbp + 8], cl` |
| `0x001E4EF0` | `rbp` | `0x2C` | reg_9A0298_field | `mov byte ptr [rbp + 0x2c], cl` |
| `0x001E4F68` | `rbp` | `0x38` | reg_9A029C_field | `mov byte ptr [rbp + 0x38], cl` |
| `0x001E4FE0` | `rbp` | `0x44` | reg_9A02A0_field | `mov byte ptr [rbp + 0x44], cl` |
| `0x001E6B3A` | `rsp` | `0x38` | reg_9A029C_field | `mov qword ptr [rsp + 0x38], rax` |
| `0x001E6BA7` | `rsp` | `0x38` | reg_9A029C_field | `mov qword ptr [rsp + 0x38], rax` |
| `0x001E88C7` | `rsp` | `0x38` | reg_9A029C_field | `mov qword ptr [rsp + 0x38], rax` |
| `0x001E8934` | `rsp` | `0x38` | reg_9A029C_field | `mov qword ptr [rsp + 0x38], rax` |
| `0x001E8B32` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], 0x5b5` |
| `0x001E8B41` | `rbp` | `0x44` | reg_9A02A0_field | `mov dword ptr [rbp + 0x44], 0x38` |
| `0x001E8E2B` | `rbp` | `0x2C` | reg_9A0298_field | `mov byte ptr [rbp + 0x2c], cl` |
| `0x001E8EC7` | `rbp` | `0x38` | reg_9A029C_field | `mov byte ptr [rbp + 0x38], cl` |
| `0x001E8F7E` | `rsp` | `0x38` | reg_9A029C_field | `mov dword ptr [rsp + 0x38], edx` |
| `0x001E93ED` | `rbp` | `0x8` | reg_9A0290_field | `mov byte ptr [rbp + 8], cl` |
| `0x001E9CD9` | `rsp` | `0x44` | reg_9A02A0_field | `mov dword ptr [rsp + 0x44], eax` |
| `0x001EA092` | `rbp` | `0x38` | reg_9A029C_field | `mov byte ptr [rbp + 0x38], cl` |
| `0x001EA12E` | `rbp` | `0x44` | reg_9A02A0_field | `mov byte ptr [rbp + 0x44], cl` |
| `0x001EAC80` | `rbp` | `0x8` | reg_9A0290_field | `mov byte ptr [rbp + 8], cl` |
| `0x001EADE8` | `rbp` | `0x2C` | reg_9A0298_field | `mov byte ptr [rbp + 0x2c], cl` |
| `0x001EAF82` | `rbp` | `0x8` | reg_9A0290_field | `mov byte ptr [rbp + 8], al` |
| `0x001EB23B` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], r11d` |
| `0x001EB325` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], r10d` |
| `0x001EB3F5` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], r10d` |
| `0x001EB4CB` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], r10d` |
| `0x001EB5A8` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], r10d` |
| `0x001EB685` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], r10d` |
| `0x001EB755` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], r10d` |
| `0x001EB825` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], r10d` |
| `0x001EB8E5` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], r10d` |
| `0x001EB9A5` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], r10d` |
| `0x001EBA65` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], r10d` |
| `0x001EBB25` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], r10d` |
| `0x001EBBE5` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], r10d` |
| `0x001EBCA5` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], r10d` |
| `0x001EBD65` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], r10d` |
| `0x001EBE25` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], r10d` |
| `0x001EBEEB` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], r10d` |
| `0x001EBFC5` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], r10d` |
| `0x001EC085` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], r10d` |
| `0x001EC145` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], r10d` |
| `0x001EC205` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], r10d` |
| `0x001EC2C5` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], r10d` |
| `0x001EC385` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], r10d` |
| `0x001EC445` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], r11d` |
| `0x001EC518` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], r11d` |
| `0x001EC5E5` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], r11d` |
| `0x001EC6BB` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], r11d` |
| `0x001EC795` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], r11d` |
| `0x001EC868` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], r11d` |
| `0x001EC935` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], r11d` |
| `0x001ECA05` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], r11d` |
| `0x001ECADB` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], r11d` |
| `0x001ECE99` | `rsp` | `0x38` | reg_9A029C_field | `mov byte ptr [rsp + 0x38], cl` |
| `0x001ECF89` | `rsp` | `0x44` | reg_9A02A0_field | `mov byte ptr [rsp + 0x44], al` |
| `0x001ED15C` | `rsp` | `0x38` | reg_9A029C_field | `mov byte ptr [rsp + 0x38], al` |
| `0x001ED1EC` | `rsp` | `0x44` | reg_9A02A0_field | `mov byte ptr [rsp + 0x44], cl` |
| `0x001ED885` | `rcx` | `0x8` | reg_9A0290_field | `mov dword ptr [rcx + 8], eax` |
| `0x001ED894` | `rcx` | `0x2C` | reg_9A0298_field | `mov dword ptr [rcx + 0x2c], 0x3e8` |
| `0x001EE972` | `rsp` | `0x38` | reg_9A029C_field | `mov qword ptr [rsp + 0x38], rcx` |
| `0x001EEDDA` | `rax` | `0x8` | reg_9A0290_field | `mov qword ptr [rax + 8], rbx` |
| `0x001EF310` | `rsp` | `0x38` | reg_9A029C_field | `mov dword ptr [rsp + 0x38], 0xbd` |
| `0x001EF324` | `rsp` | `0x38` | reg_9A029C_field | `mov qword ptr [rsp + 0x38], rsi` |
| `0x001EF335` | `rsp` | `0x38` | reg_9A029C_field | `mov dword ptr [rsp + 0x38], edi` |
| `0x001EF970` | `rsp` | `0x38` | reg_9A029C_field | `mov qword ptr [rsp + 0x38], rax` |
| `0x001EF9A1` | `rsp` | `0x38` | reg_9A029C_field | `mov qword ptr [rsp + 0x38], rax` |
| `0x001EFCC7` | `rsp` | `0x38` | reg_9A029C_field | `mov qword ptr [rsp + 0x38], rcx` |
| `0x001F007E` | `rdi` | `0x2C` | reg_9A0298_field | `mov dword ptr [rdi + 0x2c], r14d` |
| `0x001F0088` | `rdi` | `0x8` | reg_9A0290_field | `mov dword ptr [rdi + 8], eax` |
| `0x001F049A` | `rsp` | `0x38` | reg_9A029C_field | `mov qword ptr [rsp + 0x38], rbx` |
| `0x001F09A5` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], r10d` |
| `0x001F0A65` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], r10d` |
| `0x001F0B25` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], r10d` |
| `0x001F0BE5` | `rsp` | `0x2C` | reg_9A0298_field | `mov dword ptr [rsp + 0x2c], r10d` |
| `0x001F0C91` | `rsp` | `0x38` | reg_9A029C_field | `mov qword ptr [rsp + 0x38], 0xfffffffffffffffe` |
| `0x001F0ECE` | `rsp` | `0x38` | reg_9A029C_field | `mov dword ptr [rsp + 0x38], eax` |

## Contexts

### flag0 @ `0x001D4B3B`

```asm
0x001D4AFA: mov byte ptr [rbx + 0xd8], dil
0x001D4B01: mov qword ptr [rbx + 0xdc], rdi
0x001D4B08: mov byte ptr [rbx + 0xe4], dil
0x001D4B0F: lea rcx, [rbx + 0xe8]
0x001D4B16: mov rdx, r13
0x001D4B19: call 0x140408a20
0x001D4B1E: nop
0x001D4B1F: mov qword ptr [rbx + 0x138], 0xffffffffffffffff
0x001D4B2A: mov dword ptr [rbx + 0x140], 0xffffffff
0x001D4B34: mov qword ptr [rbx + 0x258], rdi
0x001D4B3B: mov dword ptr [rbx + 0x260], edi
0x001D4B41: xor eax, eax
0x001D4B43: mov qword ptr [rbx + 0x264], rax
0x001D4B4A: mov byte ptr [rbx + 0x26c], al
0x001D4B50: mov qword ptr [rbx + 0x270], 0xffffffffffffffff
0x001D4B5B: mov qword ptr [rbx + 0x278], rdi
0x001D4B62: mov byte ptr [rbx + 0x280], al
0x001D4B68: mov word ptr [rbx + 0x281], ax
0x001D4B6F: mov byte ptr [rbx + 0x398], al
0x001D4B75: mov word ptr [rbx + 0x399], ax
0x001D4B7C: mov dword ptr [rbx + 0x39c], edi
0x001D4B82: mov qword ptr [rbx + 0x3a0], 0xffffffffffffffff
0x001D4B8D: lea rcx, [rbx + 0x144]
0x001D4B94: xor edx, edx
```

### flag1 @ `0x001D4B43`

```asm
0x001D4B08: mov byte ptr [rbx + 0xe4], dil
0x001D4B0F: lea rcx, [rbx + 0xe8]
0x001D4B16: mov rdx, r13
0x001D4B19: call 0x140408a20
0x001D4B1E: nop
0x001D4B1F: mov qword ptr [rbx + 0x138], 0xffffffffffffffff
0x001D4B2A: mov dword ptr [rbx + 0x140], 0xffffffff
0x001D4B34: mov qword ptr [rbx + 0x258], rdi
0x001D4B3B: mov dword ptr [rbx + 0x260], edi
0x001D4B41: xor eax, eax
0x001D4B43: mov qword ptr [rbx + 0x264], rax
0x001D4B4A: mov byte ptr [rbx + 0x26c], al
0x001D4B50: mov qword ptr [rbx + 0x270], 0xffffffffffffffff
0x001D4B5B: mov qword ptr [rbx + 0x278], rdi
0x001D4B62: mov byte ptr [rbx + 0x280], al
0x001D4B68: mov word ptr [rbx + 0x281], ax
0x001D4B6F: mov byte ptr [rbx + 0x398], al
0x001D4B75: mov word ptr [rbx + 0x399], ax
0x001D4B7C: mov dword ptr [rbx + 0x39c], edi
0x001D4B82: mov qword ptr [rbx + 0x3a0], 0xffffffffffffffff
0x001D4B8D: lea rcx, [rbx + 0x144]
0x001D4B94: xor edx, edx
0x001D4B96: mov r8d, 0x114
0x001D4B9C: call 0x1403d3050
```

### state_idx @ `0x001D4B50`

```asm
0x001D4B16: mov rdx, r13
0x001D4B19: call 0x140408a20
0x001D4B1E: nop
0x001D4B1F: mov qword ptr [rbx + 0x138], 0xffffffffffffffff
0x001D4B2A: mov dword ptr [rbx + 0x140], 0xffffffff
0x001D4B34: mov qword ptr [rbx + 0x258], rdi
0x001D4B3B: mov dword ptr [rbx + 0x260], edi
0x001D4B41: xor eax, eax
0x001D4B43: mov qword ptr [rbx + 0x264], rax
0x001D4B4A: mov byte ptr [rbx + 0x26c], al
0x001D4B50: mov qword ptr [rbx + 0x270], 0xffffffffffffffff
0x001D4B5B: mov qword ptr [rbx + 0x278], rdi
0x001D4B62: mov byte ptr [rbx + 0x280], al
0x001D4B68: mov word ptr [rbx + 0x281], ax
0x001D4B6F: mov byte ptr [rbx + 0x398], al
0x001D4B75: mov word ptr [rbx + 0x399], ax
0x001D4B7C: mov dword ptr [rbx + 0x39c], edi
0x001D4B82: mov qword ptr [rbx + 0x3a0], 0xffffffffffffffff
0x001D4B8D: lea rcx, [rbx + 0x144]
0x001D4B94: xor edx, edx
0x001D4B96: mov r8d, 0x114
0x001D4B9C: call 0x1403d3050
0x001D4BA1: cmp dword ptr [rsi + 0xc0], edi
0x001D4BA7: jl 0x1401d4bbc
```

### retry @ `0x001D4B5B`

```asm
0x001D4B19: call 0x140408a20
0x001D4B1E: nop
0x001D4B1F: mov qword ptr [rbx + 0x138], 0xffffffffffffffff
0x001D4B2A: mov dword ptr [rbx + 0x140], 0xffffffff
0x001D4B34: mov qword ptr [rbx + 0x258], rdi
0x001D4B3B: mov dword ptr [rbx + 0x260], edi
0x001D4B41: xor eax, eax
0x001D4B43: mov qword ptr [rbx + 0x264], rax
0x001D4B4A: mov byte ptr [rbx + 0x26c], al
0x001D4B50: mov qword ptr [rbx + 0x270], 0xffffffffffffffff
0x001D4B5B: mov qword ptr [rbx + 0x278], rdi
0x001D4B62: mov byte ptr [rbx + 0x280], al
0x001D4B68: mov word ptr [rbx + 0x281], ax
0x001D4B6F: mov byte ptr [rbx + 0x398], al
0x001D4B75: mov word ptr [rbx + 0x399], ax
0x001D4B7C: mov dword ptr [rbx + 0x39c], edi
0x001D4B82: mov qword ptr [rbx + 0x3a0], 0xffffffffffffffff
0x001D4B8D: lea rcx, [rbx + 0x144]
0x001D4B94: xor edx, edx
0x001D4B96: mov r8d, 0x114
0x001D4B9C: call 0x1403d3050
0x001D4BA1: cmp dword ptr [rsi + 0xc0], edi
0x001D4BA7: jl 0x1401d4bbc
0x001D4BA9: mov byte ptr [rbx + 0x26c], 1
```

### profile_valid_flags @ `0x001D4B6F`

```asm
0x001D4B2A: mov dword ptr [rbx + 0x140], 0xffffffff
0x001D4B34: mov qword ptr [rbx + 0x258], rdi
0x001D4B3B: mov dword ptr [rbx + 0x260], edi
0x001D4B41: xor eax, eax
0x001D4B43: mov qword ptr [rbx + 0x264], rax
0x001D4B4A: mov byte ptr [rbx + 0x26c], al
0x001D4B50: mov qword ptr [rbx + 0x270], 0xffffffffffffffff
0x001D4B5B: mov qword ptr [rbx + 0x278], rdi
0x001D4B62: mov byte ptr [rbx + 0x280], al
0x001D4B68: mov word ptr [rbx + 0x281], ax
0x001D4B6F: mov byte ptr [rbx + 0x398], al
0x001D4B75: mov word ptr [rbx + 0x399], ax
0x001D4B7C: mov dword ptr [rbx + 0x39c], edi
0x001D4B82: mov qword ptr [rbx + 0x3a0], 0xffffffffffffffff
0x001D4B8D: lea rcx, [rbx + 0x144]
0x001D4B94: xor edx, edx
0x001D4B96: mov r8d, 0x114
0x001D4B9C: call 0x1403d3050
0x001D4BA1: cmp dword ptr [rsi + 0xc0], edi
0x001D4BA7: jl 0x1401d4bbc
0x001D4BA9: mov byte ptr [rbx + 0x26c], 1
0x001D4BB0: mov eax, dword ptr [rsi + 0xc0]
0x001D4BB6: mov dword ptr [rbx + 0x3a0], eax
0x001D4BBC: imul r10, r12, 0xa8
```

### gpu_table_key @ `0x001D4B82`

```asm
0x001D4B41: xor eax, eax
0x001D4B43: mov qword ptr [rbx + 0x264], rax
0x001D4B4A: mov byte ptr [rbx + 0x26c], al
0x001D4B50: mov qword ptr [rbx + 0x270], 0xffffffffffffffff
0x001D4B5B: mov qword ptr [rbx + 0x278], rdi
0x001D4B62: mov byte ptr [rbx + 0x280], al
0x001D4B68: mov word ptr [rbx + 0x281], ax
0x001D4B6F: mov byte ptr [rbx + 0x398], al
0x001D4B75: mov word ptr [rbx + 0x399], ax
0x001D4B7C: mov dword ptr [rbx + 0x39c], edi
0x001D4B82: mov qword ptr [rbx + 0x3a0], 0xffffffffffffffff
0x001D4B8D: lea rcx, [rbx + 0x144]
0x001D4B94: xor edx, edx
0x001D4B96: mov r8d, 0x114
0x001D4B9C: call 0x1403d3050
0x001D4BA1: cmp dword ptr [rsi + 0xc0], edi
0x001D4BA7: jl 0x1401d4bbc
0x001D4BA9: mov byte ptr [rbx + 0x26c], 1
0x001D4BB0: mov eax, dword ptr [rsi + 0xc0]
0x001D4BB6: mov dword ptr [rbx + 0x3a0], eax
0x001D4BBC: imul r10, r12, 0xa8
0x001D4BC3: mov qword ptr [rsp + 0x60], r10
0x001D4BC8: mov rax, qword ptr [rip + 0x611839]
0x001D4BCF: mov r9, qword ptr [r10 + rax + 0x80]
```

### gpu_table_key @ `0x001D4BB6`

```asm
0x001D4B7C: mov dword ptr [rbx + 0x39c], edi
0x001D4B82: mov qword ptr [rbx + 0x3a0], 0xffffffffffffffff
0x001D4B8D: lea rcx, [rbx + 0x144]
0x001D4B94: xor edx, edx
0x001D4B96: mov r8d, 0x114
0x001D4B9C: call 0x1403d3050
0x001D4BA1: cmp dword ptr [rsi + 0xc0], edi
0x001D4BA7: jl 0x1401d4bbc
0x001D4BA9: mov byte ptr [rbx + 0x26c], 1
0x001D4BB0: mov eax, dword ptr [rsi + 0xc0]
0x001D4BB6: mov dword ptr [rbx + 0x3a0], eax
0x001D4BBC: imul r10, r12, 0xa8
0x001D4BC3: mov qword ptr [rsp + 0x60], r10
0x001D4BC8: mov rax, qword ptr [rip + 0x611839]
0x001D4BCF: mov r9, qword ptr [r10 + rax + 0x80]
0x001D4BD7: mov qword ptr [r14], r9
0x001D4BDA: mov qword ptr [r15], rdi
0x001D4BDD: or r12d, 0xffffffff
0x001D4BE1: mov esi, edi
0x001D4BE3: mov rcx, qword ptr [rip + 0x612d66]
0x001D4BEA: mov r8, qword ptr [rip + 0x612d57]
0x001D4BF1: sub rcx, r8
0x001D4BF4: movabs rax, 0x6666666666666667
0x001D4BFE: imul rcx
```

### reg_9A0298_field @ `0x001D4D3A`

```asm
0x001D4D19: xor ecx, 0x2e
0x001D4D1C: mov byte ptr [rbp + 0x29], cl
0x001D4D1F: movsx ecx, byte ptr [rbp + 0x29]
0x001D4D23: xor ecx, 0x7a
0x001D4D26: mov byte ptr [rbp + 0x2a], cl
0x001D4D29: movsx ecx, byte ptr [rbp + 0x2a]
0x001D4D2D: xor ecx, 0x14
0x001D4D30: mov byte ptr [rbp + 0x2b], cl
0x001D4D33: movsx ecx, byte ptr [rbp + 0x2b]
0x001D4D37: xor ecx, 0xc
0x001D4D3A: mov byte ptr [rbp + 0x2c], cl
0x001D4D3D: movsx ecx, byte ptr [rbp + 0x2c]
0x001D4D41: xor ecx, 0x17
0x001D4D44: mov byte ptr [rbp + 0x2d], cl
0x001D4D47: movsx ecx, byte ptr [rbp + 0x2d]
0x001D4D4B: xor ecx, 0x16
0x001D4D4E: mov byte ptr [rbp + 0x2e], cl
0x001D4D51: movsx ecx, byte ptr [rbp + 0x2e]
0x001D4D55: xor ecx, 0x7a
0x001D4D58: mov byte ptr [rbp + 0x2f], cl
0x001D4D5B: movsx ecx, byte ptr [rbp + 0x2f]
0x001D4D5F: xor ecx, 0x38
0x001D4D62: mov byte ptr [rbp + 0x30], cl
0x001D4D65: movsx ecx, byte ptr [rbp + 0x30]
```

### reg_9A029C_field @ `0x001D4DB2`

```asm
0x001D4D91: xor ecx, 0x29
0x001D4D94: mov byte ptr [rbp + 0x35], cl
0x001D4D97: movsx ecx, byte ptr [rbp + 0x35]
0x001D4D9B: xor ecx, 0x7a
0x001D4D9E: mov byte ptr [rbp + 0x36], cl
0x001D4DA1: movsx ecx, byte ptr [rbp + 0x36]
0x001D4DA5: xor ecx, 0x13
0x001D4DA8: mov byte ptr [rbp + 0x37], cl
0x001D4DAB: movsx ecx, byte ptr [rbp + 0x37]
0x001D4DAF: xor ecx, 0x1e
0x001D4DB2: mov byte ptr [rbp + 0x38], cl
0x001D4DB5: movsx ecx, byte ptr [rbp + 0x38]
0x001D4DB9: xor ecx, 0x7a
0x001D4DBC: mov byte ptr [rbp + 0x39], cl
0x001D4DBF: movsx ecx, byte ptr [rbp + 0x39]
0x001D4DC3: xor ecx, 0x77
0x001D4DC6: mov byte ptr [rbp + 0x3a], cl
0x001D4DC9: movsx ecx, byte ptr [rbp + 0x3a]
0x001D4DCD: xor ecx, 0x7a
0x001D4DD0: mov byte ptr [rbp + 0x3b], cl
0x001D4DD3: movsx ecx, byte ptr [rbp + 0x3b]
0x001D4DD7: xor ecx, 0x21
0x001D4DDA: mov byte ptr [rbp + 0x3c], cl
0x001D4DDD: movsx ecx, byte ptr [rbp + 0x3c]
```

### reg_9A02A0_field @ `0x001D4EF2`

```asm
0x001D4EC6: mov rdx, r15
0x001D4EC9: mov ecx, r12d
0x001D4ECC: call qword ptr [rip + 0x61296e]
0x001D4ED2: mov dword ptr [rsp + 0x34], eax
0x001D4ED6: test eax, eax
0x001D4ED8: je 0x1401d5165
0x001D4EDE: mov ecx, eax
0x001D4EE0: call qword ptr [rip + 0x612972]
0x001D4EE6: mov qword ptr [rsp + 0x68], rax
0x001D4EEB: mov dword ptr [rbp + 0x40], 0x39
0x001D4EF2: mov dword ptr [rbp + 0x44], 0x54
0x001D4EF9: mov eax, dword ptr [rbp + 0x44]
0x001D4EFC: xor eax, 3
0x001D4EFF: mov byte ptr [rbp + 0x48], al
0x001D4F02: movsx ecx, byte ptr [rbp + 0x48]
0x001D4F06: xor ecx, 0x19
0x001D4F09: mov byte ptr [rbp + 0x49], cl
0x001D4F0C: movsx ecx, byte ptr [rbp + 0x49]
0x001D4F10: xor ecx, 0x4c
0x001D4F13: mov byte ptr [rbp + 0x4a], cl
0x001D4F16: movsx ecx, byte ptr [rbp + 0x4a]
0x001D4F1A: xor ecx, 0x57
0x001D4F1D: mov byte ptr [rbp + 0x4b], cl
0x001D4F20: movsx ecx, byte ptr [rbp + 0x4b]
```

### reg_9A0290_field @ `0x001D51C6`

```asm
0x001D51A8: shl ecx, 0x10
0x001D51AB: cmp rcx, r9
0x001D51AE: je 0x1401d51bb
0x001D51B0: inc edx
0x001D51B2: mov eax, edx
0x001D51B4: cmp rax, r8
0x001D51B7: jb 0x1401d51a0
0x001D51B9: jmp 0x1401d51cf
0x001D51BB: mov rcx, qword ptr [r10 + rax*8]
0x001D51BF: mov qword ptr [rbx + 0xd0], rcx
0x001D51C6: mov dword ptr [r10 + rax*8 + 8], 0xffffffff
0x001D51CF: mov rcx, qword ptr [rbx + 0xd0]
0x001D51D6: test rcx, rcx
0x001D51D9: je 0x1401d5b26
0x001D51DF: mov rax, qword ptr [rip + 0x61290a]
0x001D51E6: test rax, rax
0x001D51E9: je 0x1401d5435
0x001D51EF: lea rdx, [rbx + 0xdc]
0x001D51F6: call rax
0x001D51F8: mov dword ptr [rsp + 0x38], eax
0x001D51FC: test eax, eax
0x001D51FE: je 0x1401d5435
0x001D5204: mov dword ptr [rsp + 0x3c], 0x239
0x001D520C: mov dword ptr [rbp - 0x20], 0x7e
```

### reg_9A029C_field @ `0x001D51F8`

```asm
0x001D51BF: mov qword ptr [rbx + 0xd0], rcx
0x001D51C6: mov dword ptr [r10 + rax*8 + 8], 0xffffffff
0x001D51CF: mov rcx, qword ptr [rbx + 0xd0]
0x001D51D6: test rcx, rcx
0x001D51D9: je 0x1401d5b26
0x001D51DF: mov rax, qword ptr [rip + 0x61290a]
0x001D51E6: test rax, rax
0x001D51E9: je 0x1401d5435
0x001D51EF: lea rdx, [rbx + 0xdc]
0x001D51F6: call rax
0x001D51F8: mov dword ptr [rsp + 0x38], eax
0x001D51FC: test eax, eax
0x001D51FE: je 0x1401d5435
0x001D5204: mov dword ptr [rsp + 0x3c], 0x239
0x001D520C: mov dword ptr [rbp - 0x20], 0x7e
0x001D5213: mov eax, dword ptr [rbp - 0x20]
0x001D5216: xor eax, 0x4e
0x001D5219: mov byte ptr [rbp - 0x1c], al
0x001D521C: movsx ecx, byte ptr [rbp - 0x1c]
0x001D5220: xor ecx, 0x56
0x001D5223: mov byte ptr [rbp - 0x1b], cl
0x001D5226: movsx ecx, byte ptr [rbp - 0x1b]
0x001D522A: xor ecx, 0x41
0x001D522D: mov byte ptr [rbp - 0x1a], cl
```

### reg_9A0290_field @ `0x001D5381`

```asm
0x001D5360: xor ecx, 0x3a
0x001D5363: mov byte ptr [rbp + 5], cl
0x001D5366: movsx ecx, byte ptr [rbp + 5]
0x001D536A: xor ecx, 0x20
0x001D536D: mov byte ptr [rbp + 6], cl
0x001D5370: movsx ecx, byte ptr [rbp + 6]
0x001D5374: xor ecx, 0x7b
0x001D5377: mov byte ptr [rbp + 7], cl
0x001D537A: movsx ecx, byte ptr [rbp + 7]
0x001D537E: xor ecx, 0x7d
0x001D5381: mov byte ptr [rbp + 8], cl
0x001D5384: mov byte ptr [rbp + 9], 0
0x001D5388: movzx eax, byte ptr [rbp - 0x1c]
0x001D538C: lea rdx, [rbp + 0x100]
0x001D5393: lea rcx, [rbp - 0x20]
0x001D5397: call 0x14026de30
0x001D539C: nop
0x001D539D: cmp qword ptr [rax + 0x18], 0x10
0x001D53A2: jb 0x1401d53a7
0x001D53A4: mov rax, qword ptr [rax]
0x001D53A7: lea r8, [rsp + 0x38]
0x001D53AC: lea rdx, [rsp + 0x3c]
0x001D53B1: mov rcx, rax
0x001D53B4: call 0x1401d3fc0
```

### reg_9A02A0_field @ `0x001D5461`

```asm
0x001D542F: mov dword ptr [rbx + 0xdc], edi
0x001D5435: mov rax, qword ptr [rip + 0x6126bc]
0x001D543C: test rax, rax
0x001D543F: je 0x1401d57a2
0x001D5445: lea rdx, [rbx + 0xe0]
0x001D544C: mov rcx, qword ptr [rbx + 0xd0]
0x001D5453: call rax
0x001D5455: mov dword ptr [rsp + 0x40], eax
0x001D5459: test eax, eax
0x001D545B: je 0x1401d57a2
0x001D5461: mov dword ptr [rsp + 0x44], 0x23d
0x001D5469: mov dword ptr [rbp - 0x80], 0x35
0x001D5470: mov eax, dword ptr [rbp - 0x80]
0x001D5473: add al, 0x35
0x001D5475: movsx ecx, al
0x001D5478: xor ecx, 0x15
0x001D547B: mov dword ptr [rbp - 0x7c], ecx
0x001D547E: mov eax, dword ptr [rbp - 0x7c]
0x001D5481: mov ecx, dword ptr [rbp - 0x80]
0x001D5484: xor ecx, eax
0x001D5486: xor ecx, 0x4e
0x001D5489: mov byte ptr [rbp - 0x78], cl
0x001D548C: movsx ecx, byte ptr [rbp - 0x78]
0x001D5490: mov eax, dword ptr [rbp - 0x80]
```

### reg_9A0290_field @ `0x001D5DD0`

```asm
0x001D5DC6: pop rbx
0x001D5DC7: pop rbp
0x001D5DC8: ret
0x001D5DC9: int3
0x001D5DCA: int3
0x001D5DCB: int3
0x001D5DCC: int3
0x001D5DCD: int3
0x001D5DCE: int3
0x001D5DCF: int3
0x001D5DD0: mov qword ptr [rsp + 8], rbx
0x001D5DD5: push rdi
0x001D5DD6: sub rsp, 0x20
0x001D5DDA: lea rax, [rip + 0x2e808f]
0x001D5DE1: mov rdi, rcx
0x001D5DE4: mov qword ptr [rcx], rax
0x001D5DE7: mov ebx, edx
0x001D5DE9: add rcx, 0xe8
0x001D5DF0: call 0x140032ef0
0x001D5DF5: lea rax, [rip + 0x26bc94]
0x001D5DFC: lea rcx, [rdi + 0x48]
0x001D5E00: mov qword ptr [rdi], rax
0x001D5E03: call 0x140391a10
0x001D5E08: lea rcx, [rdi + 8]
```

### reg_9A0290_field @ `0x001D5E45`

```asm
0x001D5E37: int3
0x001D5E38: int3
0x001D5E39: int3
0x001D5E3A: int3
0x001D5E3B: int3
0x001D5E3C: int3
0x001D5E3D: int3
0x001D5E3E: int3
0x001D5E3F: int3
0x001D5E40: mov qword ptr [rsp + 0x10], rdx
0x001D5E45: mov qword ptr [rsp + 8], rcx
0x001D5E4A: push rsi
0x001D5E4B: push rdi
0x001D5E4C: push r14
0x001D5E4E: sub rsp, 0x30
0x001D5E52: mov qword ptr [rsp + 0x20], 0xfffffffffffffffe
0x001D5E5B: mov qword ptr [rsp + 0x68], rbx
0x001D5E60: mov rsi, rdx
0x001D5E63: mov rbx, rcx
0x001D5E66: call 0x1400be320
0x001D5E6B: mov r14, rax
0x001D5E6E: mov qword ptr [rsp + 0x60], rax
0x001D5E73: mov r8, qword ptr [rbx + 8]
0x001D5E77: mov rdx, qword ptr [rbx]
```

### reg_9A0290_field @ `0x001D5EBA`

```asm
0x001D5E95: mov r8, qword ptr [rbx + 0x10]
0x001D5E99: sub r8, rdx
0x001D5E9C: sar r8, 4
0x001D5EA0: mov rcx, rbx
0x001D5EA3: call 0x1400a26a0
0x001D5EA8: shl rsi, 4
0x001D5EAC: add rsi, r14
0x001D5EAF: mov qword ptr [rbx + 0x10], rsi
0x001D5EB3: and rdi, 0xfffffffffffffff0
0x001D5EB7: add rdi, r14
0x001D5EBA: mov qword ptr [rbx + 8], rdi
0x001D5EBE: mov qword ptr [rbx], r14
0x001D5EC1: mov rbx, qword ptr [rsp + 0x68]
0x001D5EC6: add rsp, 0x30
0x001D5ECA: pop r14
0x001D5ECC: pop rdi
0x001D5ECD: pop rsi
0x001D5ECE: ret
0x001D5ECF: int3
0x001D5ED0: mov qword ptr [rsp + 0x10], rdx
0x001D5ED5: mov qword ptr [rsp + 8], rcx
0x001D5EDA: push rbx
0x001D5EDB: push rsi
0x001D5EDC: push rdi
```

### reg_9A0290_field @ `0x001D5ED5`

```asm
0x001D5EBA: mov qword ptr [rbx + 8], rdi
0x001D5EBE: mov qword ptr [rbx], r14
0x001D5EC1: mov rbx, qword ptr [rsp + 0x68]
0x001D5EC6: add rsp, 0x30
0x001D5ECA: pop r14
0x001D5ECC: pop rdi
0x001D5ECD: pop rsi
0x001D5ECE: ret
0x001D5ECF: int3
0x001D5ED0: mov qword ptr [rsp + 0x10], rdx
0x001D5ED5: mov qword ptr [rsp + 8], rcx
0x001D5EDA: push rbx
0x001D5EDB: push rsi
0x001D5EDC: push rdi
0x001D5EDD: push r14
0x001D5EDF: push r15
0x001D5EE1: sub rsp, 0x40
0x001D5EE5: mov qword ptr [rsp + 0x30], 0xfffffffffffffffe
0x001D5EEE: mov r14, rdx
0x001D5EF1: mov rbx, rcx
0x001D5EF4: call 0x1401d6120
0x001D5EF9: mov rsi, rax
0x001D5EFC: mov qword ptr [rsp + 0x80], rax
0x001D5F04: xor eax, eax
```

### reg_9A0290_field @ `0x001D5FA9`

```asm
0x001D5F83: shr r8, 0x3f
0x001D5F87: add r8, rdx
0x001D5F8A: mov rdx, qword ptr [rbx]
0x001D5F8D: mov rcx, rbx
0x001D5F90: call 0x14006f540
0x001D5F95: lea rax, [r14 + r14*4]
0x001D5F99: lea rcx, [rsi + rax*8]
0x001D5F9D: mov qword ptr [rbx + 0x10], rcx
0x001D5FA1: lea rax, [rdi + rdi*4]
0x001D5FA5: lea rcx, [rsi + rax*8]
0x001D5FA9: mov qword ptr [rbx + 8], rcx
0x001D5FAD: mov qword ptr [rbx], rsi
0x001D5FB0: add rsp, 0x40
0x001D5FB4: pop r15
0x001D5FB6: pop r14
0x001D5FB8: pop rdi
0x001D5FB9: pop rsi
0x001D5FBA: pop rbx
0x001D5FBB: ret
0x001D5FBC: int3
0x001D5FBD: int3
0x001D5FBE: int3
0x001D5FBF: int3
0x001D5FC0: sub rsp, 0x28
```

### reg_9A0290_field @ `0x001D656A`

```asm
0x001D6546: add rcx, rcx
0x001D6549: cmp dword ptr [rbp + rcx*8 + 0xd0], edi
0x001D6550: jne 0x1401d6568
0x001D6552: cmp dword ptr [rbp + rcx*8 + 0xd8], 1
0x001D655A: jne 0x1401d6568
0x001D655C: inc edx
0x001D655E: cmp edx, r8d
0x001D6561: jb 0x1401d6540
0x001D6563: jmp 0x1401d6e0c
0x001D6568: xor eax, eax
0x001D656A: mov qword ptr [rbp + 8], rax
0x001D656E: mov qword ptr [rbp + 0x10], rax
0x001D6572: mov qword ptr [rbp + 0x18], rax
0x001D6576: mov dword ptr [rbp + 8], 0x1001c
0x001D657D: mov dword ptr [rbp + 0xc], edi
0x001D6580: mov dword ptr [rbp + 0x10], 1
0x001D6587: mov dword ptr [rbp + 0x14], edi
0x001D658A: mov dword ptr [rbp + 0x18], 1
0x001D6591: mov dword ptr [rbp + 0x1c], edi
0x001D6594: mov dword ptr [rbp + 0x20], 1
0x001D659B: lea r8, [rbp + 8]
0x001D659F: lea edx, [rax + 7]
0x001D65A2: mov rcx, qword ptr [rsi + 0xd0]
0x001D65A9: call qword ptr [rip + 0x611491]
```

### reg_9A0290_field @ `0x001D6576`

```asm
0x001D6552: cmp dword ptr [rbp + rcx*8 + 0xd8], 1
0x001D655A: jne 0x1401d6568
0x001D655C: inc edx
0x001D655E: cmp edx, r8d
0x001D6561: jb 0x1401d6540
0x001D6563: jmp 0x1401d6e0c
0x001D6568: xor eax, eax
0x001D656A: mov qword ptr [rbp + 8], rax
0x001D656E: mov qword ptr [rbp + 0x10], rax
0x001D6572: mov qword ptr [rbp + 0x18], rax
0x001D6576: mov dword ptr [rbp + 8], 0x1001c
0x001D657D: mov dword ptr [rbp + 0xc], edi
0x001D6580: mov dword ptr [rbp + 0x10], 1
0x001D6587: mov dword ptr [rbp + 0x14], edi
0x001D658A: mov dword ptr [rbp + 0x18], 1
0x001D6591: mov dword ptr [rbp + 0x1c], edi
0x001D6594: mov dword ptr [rbp + 0x20], 1
0x001D659B: lea r8, [rbp + 8]
0x001D659F: lea edx, [rax + 7]
0x001D65A2: mov rcx, qword ptr [rsi + 0xd0]
0x001D65A9: call qword ptr [rip + 0x611491]
0x001D65AF: mov dword ptr [rsp + 0x24], eax
0x001D65B3: test eax, eax
0x001D65B5: je 0x1401d67e4
```

### reg_9A029C_field @ `0x001D65BB`

```asm
0x001D658A: mov dword ptr [rbp + 0x18], 1
0x001D6591: mov dword ptr [rbp + 0x1c], edi
0x001D6594: mov dword ptr [rbp + 0x20], 1
0x001D659B: lea r8, [rbp + 8]
0x001D659F: lea edx, [rax + 7]
0x001D65A2: mov rcx, qword ptr [rsi + 0xd0]
0x001D65A9: call qword ptr [rip + 0x611491]
0x001D65AF: mov dword ptr [rsp + 0x24], eax
0x001D65B3: test eax, eax
0x001D65B5: je 0x1401d67e4
0x001D65BB: mov dword ptr [rsp + 0x38], 0x46f
0x001D65C3: mov dword ptr [rbp - 0x28], 0x26
0x001D65CA: mov dword ptr [rbp - 0x24], 0x54
0x001D65D1: mov eax, dword ptr [rbp - 0x24]
0x001D65D4: xor eax, 0x68
0x001D65D7: mov byte ptr [rbp - 0x20], al
0x001D65DA: movsx ecx, byte ptr [rbp - 0x20]
0x001D65DE: xor ecx, 0x70
0x001D65E1: mov byte ptr [rbp - 0x1f], cl
0x001D65E4: movsx ecx, byte ptr [rbp - 0x1f]
0x001D65E8: xor ecx, 0x67
0x001D65EB: mov byte ptr [rbp - 0x1e], cl
0x001D65EE: movsx ecx, byte ptr [rbp - 0x1e]
0x001D65F2: xor ecx, 0x76
```

### reg_9A029C_field @ `0x001D67D4`

```asm
0x001D67B0: jae 0x1401d67b8
0x001D67B2: call 0x1403db020
0x001D67B7: int3
0x001D67B8: cmp rcx, 0x27
0x001D67BC: jbe 0x1401d67c4
0x001D67BE: call 0x1403db020
0x001D67C3: int3
0x001D67C4: mov rcx, rax
0x001D67C7: call 0x1403b20d4
0x001D67CC: mov qword ptr [rbp + 0x40], 0xf
0x001D67D4: mov qword ptr [rbp + 0x38], rbx
0x001D67D8: mov byte ptr [rbp + 0x28], 0
0x001D67DC: mov ebx, dword ptr [rsp + 0x24]
0x001D67E0: mov dword ptr [rsp + 0x20], ebx
0x001D67E4: test r12b, r12b
0x001D67E7: je 0x1401d6e08
0x001D67ED: test ebx, ebx
0x001D67EF: jne 0x1401d6ab9
0x001D67F5: mov dword ptr [rsp + 0x48], 0x47
0x001D67FD: mov eax, dword ptr [rsp + 0x48]
0x001D6801: add al, 0x47
0x001D6803: movsx ecx, al
0x001D6806: xor ecx, 0xc
0x001D6809: mov dword ptr [rsp + 0x4c], ecx
```

### reg_9A029C_field @ `0x001D6E56`

```asm
0x001D6E3C: int3
0x001D6E3D: int3
0x001D6E3E: int3
0x001D6E3F: int3
0x001D6E40: mov qword ptr [rsp + 0x18], rsi
0x001D6E45: push rdi
0x001D6E46: sub rsp, 0x20
0x001D6E4A: xor esi, esi
0x001D6E4C: mov rdi, rcx
0x001D6E4F: cmp byte ptr [rip + 0x610a92], sil
0x001D6E56: mov qword ptr [rsp + 0x38], rsi
0x001D6E5B: jne 0x1401d6e6a
0x001D6E5D: xor eax, eax
0x001D6E5F: mov rsi, qword ptr [rsp + 0x40]
0x001D6E64: add rsp, 0x20
0x001D6E68: pop rdi
0x001D6E69: ret
0x001D6E6A: mov rcx, qword ptr [rip + 0x610adf]
0x001D6E71: movabs rax, 0x6666666666666667
0x001D6E7B: mov r9, qword ptr [rip + 0x610ac6]
0x001D6E82: sub rcx, r9
0x001D6E85: mov qword ptr [rsp + 0x30], rbx
0x001D6E8A: imul rcx
0x001D6E8D: mov ebx, esi
```

### reg_9A029C_field @ `0x001D6EE6`

```asm
0x001D6EC5: jb 0x1401d6eb0
0x001D6EC7: jmp 0x1401d6efc
0x001D6EC9: add rcx, 8
0x001D6ECD: cmp qword ptr [rcx + 0x18], 0x10
0x001D6ED2: jb 0x1401d6ed7
0x001D6ED4: mov rcx, qword ptr [rcx]
0x001D6ED7: lea rdx, [rsp + 0x38]
0x001D6EDC: call qword ptr [rip + 0x610966]
0x001D6EE2: test eax, eax
0x001D6EE4: je 0x1401d6ef2
0x001D6EE6: mov qword ptr [rsp + 0x38], rsi
0x001D6EEB: cmp ebx, -1
0x001D6EEE: jne 0x1401d6eff
0x001D6EF0: jmp 0x1401d6efc
0x001D6EF2: mov rcx, qword ptr [rsp + 0x38]
0x001D6EF7: test rcx, rcx
0x001D6EFA: jne 0x1401d6f17
0x001D6EFC: mov ebx, dword ptr [rdi + 0x10]
0x001D6EFF: lea rdx, [rsp + 0x38]
0x001D6F04: mov ecx, ebx
0x001D6F06: call qword ptr [rip + 0x610934]
0x001D6F0C: mov rcx, qword ptr [rsp + 0x38]
0x001D6F11: test eax, eax
0x001D6F13: cmovne rcx, rsi
```

### reg_9A029C_field @ `0x001D712E`

```asm
0x001D7101: lea rdx, [rsp + 0x20]
0x001D7106: call qword ptr [rip + 0x61075c]
0x001D710C: mov dword ptr [rsp + 0x24], eax
0x001D7110: test eax, eax
0x001D7112: je 0x1401d745e
0x001D7118: cmp eax, 3
0x001D711B: je 0x1401d7467
0x001D7121: mov ecx, eax
0x001D7123: call qword ptr [rip + 0x61072f]
0x001D7129: mov qword ptr [rsp + 0x28], rax
0x001D712E: mov dword ptr [rsp + 0x38], 0x3c
0x001D7136: mov eax, dword ptr [rsp + 0x38]
0x001D713A: add al, 0x3c
0x001D713C: movsx ecx, al
0x001D713F: xor ecx, 0x6c
0x001D7142: mov dword ptr [rsp + 0x3c], ecx
0x001D7146: mov eax, dword ptr [rsp + 0x3c]
0x001D714A: mov ecx, dword ptr [rsp + 0x38]
0x001D714E: xor ecx, eax
0x001D7150: xor ecx, 0x3a
0x001D7153: mov byte ptr [rsp + 0x40], cl
0x001D7157: movsx ecx, byte ptr [rsp + 0x40]
0x001D715C: mov eax, dword ptr [rsp + 0x38]
0x001D7160: inc al
```

### reg_9A02A0_field @ `0x001D71A3`

```asm
0x001D7184: mov eax, dword ptr [rsp + 0x38]
0x001D7188: add al, 3
0x001D718A: xor eax, ecx
0x001D718C: xor eax, 0x6e
0x001D718F: mov byte ptr [rsp + 0x43], al
0x001D7193: movsx ecx, byte ptr [rsp + 0x43]
0x001D7198: mov eax, dword ptr [rsp + 0x38]
0x001D719C: add al, 4
0x001D719E: xor eax, ecx
0x001D71A0: xor eax, 0x61
0x001D71A3: mov byte ptr [rsp + 0x44], al
0x001D71A7: movsx ecx, byte ptr [rsp + 0x44]
0x001D71AC: mov eax, dword ptr [rsp + 0x38]
0x001D71B0: add al, 5
0x001D71B2: xor eax, ecx
0x001D71B4: xor eax, 0x62
0x001D71B7: mov byte ptr [rsp + 0x45], al
0x001D71BB: movsx ecx, byte ptr [rsp + 0x45]
0x001D71C0: mov eax, dword ptr [rsp + 0x38]
0x001D71C4: add al, 6
0x001D71C6: xor eax, ecx
0x001D71C8: xor eax, 0x6c
0x001D71CB: mov byte ptr [rsp + 0x46], al
0x001D71CF: movsx ecx, byte ptr [rsp + 0x46]
```

### reg_9A0290_field @ `0x001D74D1`

```asm
0x001D74AC: xor rax, rsp
0x001D74AF: mov qword ptr [rbp + 0x860], rax
0x001D74B6: or eax, 0xffffffff
0x001D74B9: xor r15d, r15d
0x001D74BC: mov word ptr [rdx], ax
0x001D74BF: mov rbx, rdx
0x001D74C2: mov word ptr [rdx + 2], ax
0x001D74C6: mov rdi, rcx
0x001D74C9: mov word ptr [rdx + 4], ax
0x001D74CD: mov word ptr [rdx + 6], ax
0x001D74D1: mov word ptr [rdx + 8], ax
0x001D74D5: mov qword ptr [rdx + 0xa], r15
0x001D74D9: mov qword ptr [rdx + 0x14], r15
0x001D74DD: mov word ptr [rdx + 0x1c], 0xffff
0x001D74E3: cmp dword ptr [rip + 0x60f22e], 1
0x001D74EA: ja 0x1401d7500
0x001D74EC: lea r8d, [rax + 2]
0x001D74F0: lea rdx, [rsp + 0x38]
0x001D74F5: call 0x14014b790
0x001D74FA: mov rcx, qword ptr [rax]
0x001D74FD: mov qword ptr [rbx], rcx
0x001D7500: mov rcx, rdi
0x001D7503: call 0x1401d6f30
0x001D7508: mov word ptr [rbx + 8], ax
```

### reg_9A0290_field @ `0x001D7508`

```asm
0x001D74DD: mov word ptr [rdx + 0x1c], 0xffff
0x001D74E3: cmp dword ptr [rip + 0x60f22e], 1
0x001D74EA: ja 0x1401d7500
0x001D74EC: lea r8d, [rax + 2]
0x001D74F0: lea rdx, [rsp + 0x38]
0x001D74F5: call 0x14014b790
0x001D74FA: mov rcx, qword ptr [rax]
0x001D74FD: mov qword ptr [rbx], rcx
0x001D7500: mov rcx, rdi
0x001D7503: call 0x1401d6f30
0x001D7508: mov word ptr [rbx + 8], ax
0x001D750C: cmp dword ptr [rip + 0x60f205], r15d
0x001D7513: je 0x1401d7890
0x001D7519: mov rcx, qword ptr [rdi + 0xc8]
0x001D7520: mov qword ptr [rsp + 0x9b8], r12
0x001D7528: mov r12d, 0x10
0x001D752E: test rcx, rcx
0x001D7531: je 0x1401d761a
0x001D7537: mov rax, qword ptr [rip + 0x61033a]
0x001D753E: test rax, rax
0x001D7541: je 0x1401d7557
0x001D7543: lea rdx, [rsp + 0x40]
0x001D7548: call rax
0x001D754A: test eax, eax
```

### reg_9A029C_field @ `0x001D7834`

```asm
0x001D7809: mov rsi, qword ptr [rsp + 0x9b0]
0x001D7811: mov rcx, qword ptr [rax]
0x001D7814: mov qword ptr [rbx], rcx
0x001D7817: mov rcx, qword ptr [rdi + 0xc8]
0x001D781E: test rcx, rcx
0x001D7821: je 0x1401d7888
0x001D7823: mov rax, qword ptr [rip + 0x610066]
0x001D782A: test rax, rax
0x001D782D: je 0x1401d7888
0x001D782F: lea rdx, [rsp + 0x38]
0x001D7834: mov qword ptr [rsp + 0x38], r15
0x001D7839: call rax
0x001D783B: test eax, eax
0x001D783D: jne 0x1401d7888
0x001D783F: mov rax, qword ptr [rsp + 0x38]
0x001D7844: test al, 0x84
0x001D7846: je 0x1401d7851
0x001D7848: mov dword ptr [rbx + 0x18], 3
0x001D784F: jmp 0x1401d7888
0x001D7851: test al, 0x60
0x001D7853: je 0x1401d785e
0x001D7855: mov dword ptr [rbx + 0x18], 4
0x001D785C: jmp 0x1401d7888
0x001D785E: test rax, 0x102
```

### reg_9A0290_field @ `0x001D78B0`

```asm
0x001D7893: mov rcx, qword ptr [rbp + 0x860]
0x001D789A: xor rcx, rsp
0x001D789D: call 0x1403b24c0
0x001D78A2: add rsp, 0x978
0x001D78A9: pop r15
0x001D78AB: pop rdi
0x001D78AC: pop rbx
0x001D78AD: pop rbp
0x001D78AE: ret
0x001D78AF: int3
0x001D78B0: mov qword ptr [rsp + 8], rbx
0x001D78B5: push rdi
0x001D78B6: sub rsp, 0x20
0x001D78BA: mov eax, dword ptr [rcx + 0x3a0]
0x001D78C0: lea rbx, [rip + 0x2e5e09]
0x001D78C7: lea rcx, [rip + 0x2e5f82]
0x001D78CE: mov rdi, rdx
0x001D78D1: cmp dword ptr [rbx], eax
0x001D78D3: jne 0x1401d78db
0x001D78D5: cmp dword ptr [rbx + 4], r8d
0x001D78D9: je 0x1401d78f1
0x001D78DB: add rbx, 0x18
0x001D78DF: cmp rbx, rcx
0x001D78E2: jne 0x1401d78d1
```

### reg_9A0298_field @ `0x001D7902`

```asm
0x001D78E4: xor al, al
0x001D78E6: mov rbx, qword ptr [rsp + 0x30]
0x001D78EB: add rsp, 0x20
0x001D78EF: pop rdi
0x001D78F0: ret
0x001D78F1: xor edx, edx
0x001D78F3: mov rcx, rdi
0x001D78F6: lea r8d, [rdx + 0x5c]
0x001D78FA: call 0x1403d3050
0x001D78FF: mov eax, dword ptr [rbx + 0x10]
0x001D7902: mov dword ptr [rdi + 0x2c], eax
0x001D7905: mov eax, dword ptr [rbx + 0xc]
0x001D7908: mov dword ptr [rdi + 0x38], eax
0x001D790B: mov eax, dword ptr [rbx + 8]
0x001D790E: mov dword ptr [rdi + 0x44], eax
0x001D7911: mov eax, dword ptr [rbx + 0x14]
0x001D7914: mov rbx, qword ptr [rsp + 0x30]
0x001D7919: mov dword ptr [rdi + 8], eax
0x001D791C: mov al, 1
0x001D791E: add rsp, 0x20
0x001D7922: pop rdi
0x001D7923: ret
0x001D7924: int3
0x001D7925: int3
```

### reg_9A029C_field @ `0x001D7908`

```asm
0x001D78EB: add rsp, 0x20
0x001D78EF: pop rdi
0x001D78F0: ret
0x001D78F1: xor edx, edx
0x001D78F3: mov rcx, rdi
0x001D78F6: lea r8d, [rdx + 0x5c]
0x001D78FA: call 0x1403d3050
0x001D78FF: mov eax, dword ptr [rbx + 0x10]
0x001D7902: mov dword ptr [rdi + 0x2c], eax
0x001D7905: mov eax, dword ptr [rbx + 0xc]
0x001D7908: mov dword ptr [rdi + 0x38], eax
0x001D790B: mov eax, dword ptr [rbx + 8]
0x001D790E: mov dword ptr [rdi + 0x44], eax
0x001D7911: mov eax, dword ptr [rbx + 0x14]
0x001D7914: mov rbx, qword ptr [rsp + 0x30]
0x001D7919: mov dword ptr [rdi + 8], eax
0x001D791C: mov al, 1
0x001D791E: add rsp, 0x20
0x001D7922: pop rdi
0x001D7923: ret
0x001D7924: int3
0x001D7925: int3
0x001D7926: int3
0x001D7927: int3
```

### reg_9A02A0_field @ `0x001D790E`

```asm
0x001D78F0: ret
0x001D78F1: xor edx, edx
0x001D78F3: mov rcx, rdi
0x001D78F6: lea r8d, [rdx + 0x5c]
0x001D78FA: call 0x1403d3050
0x001D78FF: mov eax, dword ptr [rbx + 0x10]
0x001D7902: mov dword ptr [rdi + 0x2c], eax
0x001D7905: mov eax, dword ptr [rbx + 0xc]
0x001D7908: mov dword ptr [rdi + 0x38], eax
0x001D790B: mov eax, dword ptr [rbx + 8]
0x001D790E: mov dword ptr [rdi + 0x44], eax
0x001D7911: mov eax, dword ptr [rbx + 0x14]
0x001D7914: mov rbx, qword ptr [rsp + 0x30]
0x001D7919: mov dword ptr [rdi + 8], eax
0x001D791C: mov al, 1
0x001D791E: add rsp, 0x20
0x001D7922: pop rdi
0x001D7923: ret
0x001D7924: int3
0x001D7925: int3
0x001D7926: int3
0x001D7927: int3
0x001D7928: int3
0x001D7929: int3
```

### reg_9A0290_field @ `0x001D7919`

```asm
0x001D78F6: lea r8d, [rdx + 0x5c]
0x001D78FA: call 0x1403d3050
0x001D78FF: mov eax, dword ptr [rbx + 0x10]
0x001D7902: mov dword ptr [rdi + 0x2c], eax
0x001D7905: mov eax, dword ptr [rbx + 0xc]
0x001D7908: mov dword ptr [rdi + 0x38], eax
0x001D790B: mov eax, dword ptr [rbx + 8]
0x001D790E: mov dword ptr [rdi + 0x44], eax
0x001D7911: mov eax, dword ptr [rbx + 0x14]
0x001D7914: mov rbx, qword ptr [rsp + 0x30]
0x001D7919: mov dword ptr [rdi + 8], eax
0x001D791C: mov al, 1
0x001D791E: add rsp, 0x20
0x001D7922: pop rdi
0x001D7923: ret
0x001D7924: int3
0x001D7925: int3
0x001D7926: int3
0x001D7927: int3
0x001D7928: int3
0x001D7929: int3
0x001D792A: int3
0x001D792B: int3
0x001D792C: int3
```

### reg_9A029C_field @ `0x001D7A74`

```asm
0x001D7A4E: je 0x1401d7a5f
0x001D7A50: add rdi, 0x18
0x001D7A54: cmp rdi, rcx
0x001D7A57: je 0x1401d9206
0x001D7A5D: jmp 0x1401d7a46
0x001D7A5F: xor edx, edx
0x001D7A61: lea r8d, [rdx + 0x5c]
0x001D7A65: lea rcx, [rbp + 0xa0]
0x001D7A6C: call 0x1403d3050
0x001D7A71: mov ecx, dword ptr [rdi + 0x10]
0x001D7A74: mov dword ptr [rsp + 0x38], ecx
0x001D7A78: mov dword ptr [rbp + 0xcc], ecx
0x001D7A7E: mov edx, dword ptr [rdi + 0xc]
0x001D7A81: mov dword ptr [rsp + 0x34], edx
0x001D7A85: mov dword ptr [rbp + 0xd8], edx
0x001D7A8B: mov r8d, dword ptr [rdi + 8]
0x001D7A8F: mov dword ptr [rsp + 0x30], r8d
0x001D7A94: mov dword ptr [rbp + 0xe4], r8d
0x001D7A9B: mov eax, dword ptr [rdi + 0x14]
0x001D7A9E: mov dword ptr [rsp + 0x40], eax
0x001D7AA2: mov dword ptr [rbp + 0xa8], eax
0x001D7AA8: movsxd r10, dword ptr [rsp + 0x3c]
0x001D7AAD: imul rdi, r10, 0x5c
0x001D7AB1: mov r9d, dword ptr [rdi + rbx + 0x188]
```

### reg_9A0290_field @ `0x001D8409`

```asm
0x001D83D2: movaps xmmword ptr [rbp + 0x7a0], xmm0
0x001D83D9: mov qword ptr [rsp + 0x40], 0x22222b
0x001D83E2: lea rax, [rbp + 0x750]
0x001D83E9: mov qword ptr [rsp + 0x48], rax
0x001D83EE: movups xmm0, xmmword ptr [rsp + 0x40]
0x001D83F3: movups xmmword ptr [rbp - 0x18], xmm0
0x001D83F7: mov dword ptr [rbp - 8], r14d
0x001D83FB: lea rax, [rbp + 0x520]
0x001D8402: mov qword ptr [rbp], rax
0x001D8406: xorps xmm0, xmm0
0x001D8409: movdqu xmmword ptr [rbp + 8], xmm0
0x001D840E: mov qword ptr [rbp + 0x18], r14
0x001D8412: lea rcx, [rbp - 0x18]
0x001D8416: call 0x140036ad0
0x001D841B: nop
0x001D841C: mov r9, qword ptr [rbp + 8]
0x001D8420: test r9, r9
0x001D8423: je 0x1401d845f
0x001D8425: mov rcx, qword ptr [rbp + 0x18]
0x001D8429: sub rcx, r9
0x001D842C: movabs rax, 0x6666666666666667
0x001D8436: imul rcx
0x001D8439: sar rdx, 4
0x001D843D: mov r8, rdx
```

### reg_9A0290_field @ `0x001D8456`

```asm
0x001D842C: movabs rax, 0x6666666666666667
0x001D8436: imul rcx
0x001D8439: sar rdx, 4
0x001D843D: mov r8, rdx
0x001D8440: shr r8, 0x3f
0x001D8444: add r8, rdx
0x001D8447: mov rdx, r9
0x001D844A: lea rcx, [rbp + 8]
0x001D844E: call 0x14006f540
0x001D8453: xorps xmm0, xmm0
0x001D8456: movdqu xmmword ptr [rbp + 8], xmm0
0x001D845B: mov qword ptr [rbp + 0x18], r14
0x001D845F: lea rax, [rbp + 0x120]
0x001D8466: mov qword ptr [rbp + 0x118], rax
0x001D846D: lea rax, [rip + 0x25b844]
0x001D8474: mov qword ptr [rbp + 0x110], rax
0x001D847B: lea rdx, [rbp + 0x530]
0x001D8482: lea rcx, [rbp + 0x120]
0x001D8489: call 0x1400328e0
0x001D848E: lea rcx, [rbp + 0x110]
0x001D8495: call 0x140073470
0x001D849A: nop
0x001D849B: lea rcx, [rbp + 0x530]
0x001D84A2: call 0x140032dc0
```

### reg_9A029C_field @ `0x001D84EA`

```asm
0x001D84BC: call 0x140032ef0
0x001D84C1: mov r14d, dword ptr [rbp + 0x64]
0x001D84C5: mov r15d, dword ptr [rbp + 0x58]
0x001D84C9: mov r12d, dword ptr [rbp + 0x4c]
0x001D84CD: mov esi, dword ptr [rbp + 0x28]
0x001D84D0: mov eax, dword ptr [rbp + 0xe4]
0x001D84D6: mov dword ptr [rsp + 0x30], eax
0x001D84DA: mov eax, dword ptr [rbp + 0xd8]
0x001D84E0: mov dword ptr [rsp + 0x34], eax
0x001D84E4: mov eax, dword ptr [rbp + 0xcc]
0x001D84EA: mov dword ptr [rsp + 0x38], eax
0x001D84EE: mov eax, dword ptr [rbp + 0xa8]
0x001D84F4: mov dword ptr [rsp + 0x40], eax
0x001D84F8: mov rcx, rbx
0x001D84FB: call 0x1401d97b0
0x001D8500: movsd xmm6, qword ptr [rip + 0x2601b0]
0x001D8508: test al, al
0x001D850A: je 0x1401d8b1b
0x001D8510: mov ecx, dword ptr [rbx + 0x260]
0x001D8516: test ecx, ecx
0x001D8518: jle 0x1401d8551
0x001D851A: mov eax, r14d
0x001D851D: xorps xmm2, xmm2
0x001D8520: cvtsi2sd xmm2, rax
```

### profile_valid_flags @ `0x001D8FE0`

```asm
0x001D8FB3: mov r8, rax
0x001D8FB6: add rax, 7
0x001D8FBA: imul rcx, rax, 0x5c
0x001D8FBE: movups xmmword ptr [rcx + rbx], xmm6
0x001D8FC2: movups xmmword ptr [rcx + rbx + 0x10], xmm5
0x001D8FC7: movups xmmword ptr [rcx + rbx + 0x20], xmm4
0x001D8FCC: movups xmmword ptr [rcx + rbx + 0x30], xmm3
0x001D8FD1: movups xmmword ptr [rcx + rbx + 0x40], xmm2
0x001D8FD6: movsd qword ptr [rcx + rbx + 0x50], xmm1
0x001D8FDC: mov dword ptr [rcx + rbx + 0x58], edx
0x001D8FE0: mov byte ptr [rbx + r8 + 0x398], 1
0x001D8FE9: mov al, 1
0x001D8FEB: jmp 0x1401d9451
0x001D8FF0: mov dword ptr [rbp + 0x440], 0x7a
0x001D8FFA: mov eax, dword ptr [rbp + 0x440]
0x001D9000: xor eax, 0x7b
0x001D9003: add eax, 4
0x001D9006: mov byte ptr [rbp + 0x444], al
0x001D900C: movsx ecx, byte ptr [rbp + 0x444]
0x001D9013: xor ecx, 0x7d
0x001D9016: add ecx, 4
0x001D9019: mov byte ptr [rbp + 0x445], cl
0x001D901F: movsx ecx, byte ptr [rbp + 0x445]
0x001D9026: xor ecx, 0x3a
```

### reg_9A0290_field @ `0x001D9657`

```asm
0x001D9636: xor ecx, 0x58
0x001D9639: mov byte ptr [rbp + 5], cl
0x001D963C: movsx ecx, byte ptr [rbp + 5]
0x001D9640: xor ecx, 0x5e
0x001D9643: mov byte ptr [rbp + 6], cl
0x001D9646: movsx ecx, byte ptr [rbp + 6]
0x001D964A: xor ecx, 3
0x001D964D: mov byte ptr [rbp + 7], cl
0x001D9650: movsx ecx, byte ptr [rbp + 7]
0x001D9654: xor ecx, 0xb
0x001D9657: mov byte ptr [rbp + 8], cl
0x001D965A: movsx ecx, byte ptr [rbp + 8]
0x001D965E: xor ecx, 0x58
0x001D9661: mov byte ptr [rbp + 9], cl
0x001D9664: movsx ecx, byte ptr [rbp + 9]
0x001D9668: xor ecx, 0x5e
0x001D966B: mov byte ptr [rbp + 0xa], cl
0x001D966E: movsx ecx, byte ptr [rbp + 0xa]
0x001D9672: xor ecx, 0xa
0x001D9675: mov byte ptr [rbp + 0xb], cl
0x001D9678: xor eax, eax
0x001D967A: mov byte ptr [rbp + 0xc], al
0x001D967D: movzx eax, byte ptr [rbp - 0x19]
0x001D9681: lea rdx, [rbp + 0x2f]
```

### reg_9A029C_field @ `0x001D9D9B`

```asm
0x001D9D67: call 0x1403b20d4
0x001D9D6C: mov qword ptr [rbp + 0x68], 0xf
0x001D9D74: mov qword ptr [rbp + 0x60], r14
0x001D9D78: mov byte ptr [rbp + 0x50], 0
0x001D9D7C: mov ebx, dword ptr [rsp + 0x24]
0x001D9D80: jmp 0x1401d9ff1
0x001D9D85: mov dword ptr [rbp + 0x30], 0x1001c
0x001D9D8C: mov ecx, dword ptr [rbp + 0x100]
0x001D9D92: mov dword ptr [rbp + 0x34], ecx
0x001D9D95: mov eax, dword ptr [rbp + 0x114]
0x001D9D9B: mov dword ptr [rbp + 0x38], eax
0x001D9D9E: mov dword ptr [rbp + 0x3c], ecx
0x001D9DA1: mov dword ptr [rbp + 0x40], eax
0x001D9DA4: mov dword ptr [rbp + 0x44], ecx
0x001D9DA7: mov dword ptr [rbp + 0x48], eax
0x001D9DAA: lea r8, [rbp + 0x30]
0x001D9DAE: mov edx, 7
0x001D9DB3: mov rcx, qword ptr [rdi + 0xd0]
0x001D9DBA: call qword ptr [rip + 0x60dc80]
0x001D9DC0: mov dword ptr [rsp + 0x28], eax
0x001D9DC4: test eax, eax
0x001D9DC6: je 0x1401d9ff5
0x001D9DCC: mov dword ptr [rsp + 0x34], 0x4fa
0x001D9DD4: mov dword ptr [rbp - 0x50], 5
```

### reg_9A02A0_field @ `0x001D9DA4`

```asm
0x001D9D78: mov byte ptr [rbp + 0x50], 0
0x001D9D7C: mov ebx, dword ptr [rsp + 0x24]
0x001D9D80: jmp 0x1401d9ff1
0x001D9D85: mov dword ptr [rbp + 0x30], 0x1001c
0x001D9D8C: mov ecx, dword ptr [rbp + 0x100]
0x001D9D92: mov dword ptr [rbp + 0x34], ecx
0x001D9D95: mov eax, dword ptr [rbp + 0x114]
0x001D9D9B: mov dword ptr [rbp + 0x38], eax
0x001D9D9E: mov dword ptr [rbp + 0x3c], ecx
0x001D9DA1: mov dword ptr [rbp + 0x40], eax
0x001D9DA4: mov dword ptr [rbp + 0x44], ecx
0x001D9DA7: mov dword ptr [rbp + 0x48], eax
0x001D9DAA: lea r8, [rbp + 0x30]
0x001D9DAE: mov edx, 7
0x001D9DB3: mov rcx, qword ptr [rdi + 0xd0]
0x001D9DBA: call qword ptr [rip + 0x60dc80]
0x001D9DC0: mov dword ptr [rsp + 0x28], eax
0x001D9DC4: test eax, eax
0x001D9DC6: je 0x1401d9ff5
0x001D9DCC: mov dword ptr [rsp + 0x34], 0x4fa
0x001D9DD4: mov dword ptr [rbp - 0x50], 5
0x001D9DDB: mov eax, dword ptr [rbp - 0x50]
0x001D9DDE: xor eax, 0x4e
0x001D9DE1: mov byte ptr [rbp - 0x4c], al
```

### reg_9A0298_field @ `0x001DA013`

```asm
0x001D9FE9: mov byte ptr [rbp + 0x70], 0
0x001D9FED: mov ebx, dword ptr [rsp + 0x28]
0x001D9FF1: mov dword ptr [rsp + 0x20], ebx
0x001D9FF5: mov rax, qword ptr [rip + 0x60da4c]
0x001D9FFC: test rax, rax
0x001D9FFF: je 0x1401da25a
0x001DA005: xor r8d, r8d
0x001DA008: xor edx, edx
0x001DA00A: mov rcx, qword ptr [rdi + 0xd0]
0x001DA011: call rax
0x001DA013: mov dword ptr [rsp + 0x2c], eax
0x001DA017: test eax, eax
0x001DA019: je 0x1401da25a
0x001DA01F: mov dword ptr [rsp + 0x38], 0x4fe
0x001DA027: mov dword ptr [rbp - 0x20], 0x5e
0x001DA02E: mov dword ptr [rbp - 0x1c], 0x3c
0x001DA035: mov eax, dword ptr [rbp - 0x1c]
0x001DA038: xor eax, 0x10
0x001DA03B: mov byte ptr [rbp - 0x18], al
0x001DA03E: movsx ecx, byte ptr [rbp - 0x18]
0x001DA042: xor ecx, 8
0x001DA045: mov byte ptr [rbp - 0x17], cl
0x001DA048: movsx ecx, byte ptr [rbp - 0x17]
0x001DA04C: xor ecx, 0x1f
```

### reg_9A029C_field @ `0x001DA01F`

```asm
0x001D9FF5: mov rax, qword ptr [rip + 0x60da4c]
0x001D9FFC: test rax, rax
0x001D9FFF: je 0x1401da25a
0x001DA005: xor r8d, r8d
0x001DA008: xor edx, edx
0x001DA00A: mov rcx, qword ptr [rdi + 0xd0]
0x001DA011: call rax
0x001DA013: mov dword ptr [rsp + 0x2c], eax
0x001DA017: test eax, eax
0x001DA019: je 0x1401da25a
0x001DA01F: mov dword ptr [rsp + 0x38], 0x4fe
0x001DA027: mov dword ptr [rbp - 0x20], 0x5e
0x001DA02E: mov dword ptr [rbp - 0x1c], 0x3c
0x001DA035: mov eax, dword ptr [rbp - 0x1c]
0x001DA038: xor eax, 0x10
0x001DA03B: mov byte ptr [rbp - 0x18], al
0x001DA03E: movsx ecx, byte ptr [rbp - 0x18]
0x001DA042: xor ecx, 8
0x001DA045: mov byte ptr [rbp - 0x17], cl
0x001DA048: movsx ecx, byte ptr [rbp - 0x17]
0x001DA04C: xor ecx, 0x1f
0x001DA04F: mov byte ptr [rbp - 0x16], cl
0x001DA052: movsx ecx, byte ptr [rbp - 0x16]
0x001DA056: xor ecx, 0xe
```

### reg_9A0290_field @ `0x001DA17B`

```asm
0x001DA15A: xor ecx, 0x64
0x001DA15D: mov byte ptr [rbp + 5], cl
0x001DA160: movsx ecx, byte ptr [rbp + 5]
0x001DA164: xor ecx, 0x25
0x001DA167: mov byte ptr [rbp + 6], cl
0x001DA16A: movsx ecx, byte ptr [rbp + 6]
0x001DA16E: xor ecx, 0x23
0x001DA171: mov byte ptr [rbp + 7], cl
0x001DA174: movsx ecx, byte ptr [rbp + 7]
0x001DA178: xor ecx, 0x7e
0x001DA17B: mov byte ptr [rbp + 8], cl
0x001DA17E: movsx ecx, byte ptr [rbp + 8]
0x001DA182: xor ecx, 0x64
0x001DA185: mov byte ptr [rbp + 9], cl
0x001DA188: movsx ecx, byte ptr [rbp + 9]
0x001DA18C: xor ecx, 0x7e
0x001DA18F: mov byte ptr [rbp + 0xa], cl
0x001DA192: movsx ecx, byte ptr [rbp + 0xa]
0x001DA196: xor ecx, 0x25
0x001DA199: mov byte ptr [rbp + 0xb], cl
0x001DA19C: movsx ecx, byte ptr [rbp + 0xb]
0x001DA1A0: xor ecx, 0x23
0x001DA1A3: mov byte ptr [rbp + 0xc], cl
0x001DA1A6: xor eax, eax
```

### gpu_table_key @ `0x001DA7EB`

```asm
0x001DA7C8: lea rax, [rip + 0x2e2e51]
0x001DA7CF: lea rdx, [rip + 0x2e2efa]
0x001DA7D6: cmp dword ptr [rax], ecx
0x001DA7D8: je 0x1401da7e8
0x001DA7DA: add rax, 8
0x001DA7DE: cmp rax, rdx
0x001DA7E1: jne 0x1401da7d6
0x001DA7E3: or eax, 0xffffffff
0x001DA7E6: jmp 0x1401da7eb
0x001DA7E8: mov eax, dword ptr [rax + 4]
0x001DA7EB: mov dword ptr [rbx + 0x3a0], eax
0x001DA7F1: cmp dword ptr [rbx + 0x3a0], 0
0x001DA7F8: jl 0x1401da869
0x001DA7FA: xor eax, eax
0x001DA7FC: mov qword ptr [rsp + 0x30], rdi
0x001DA801: xor edi, edi
0x001DA803: lea rcx, [rbx + 0x398]
0x001DA80A: mov qword ptr [rbx + 0x258], rdi
0x001DA811: mov r8d, 3
0x001DA817: mov qword ptr [rbx + 0x260], rax
0x001DA81E: mov dword ptr [rbx + 0x268], eax
0x001DA824: lea rax, [rcx + 3]
0x001DA828: cmp rcx, rax
0x001DA82B: cmova r8d, edi
```

### flag0 @ `0x001DA817`

```asm
0x001DA7E8: mov eax, dword ptr [rax + 4]
0x001DA7EB: mov dword ptr [rbx + 0x3a0], eax
0x001DA7F1: cmp dword ptr [rbx + 0x3a0], 0
0x001DA7F8: jl 0x1401da869
0x001DA7FA: xor eax, eax
0x001DA7FC: mov qword ptr [rsp + 0x30], rdi
0x001DA801: xor edi, edi
0x001DA803: lea rcx, [rbx + 0x398]
0x001DA80A: mov qword ptr [rbx + 0x258], rdi
0x001DA811: mov r8d, 3
0x001DA817: mov qword ptr [rbx + 0x260], rax
0x001DA81E: mov dword ptr [rbx + 0x268], eax
0x001DA824: lea rax, [rcx + 3]
0x001DA828: cmp rcx, rax
0x001DA82B: cmova r8d, edi
0x001DA82F: ja 0x1401da850
0x001DA831: mov rdx, rcx
0x001DA834: neg rdx
0x001DA837: nop word ptr [rax + rax]
0x001DA840: mov byte ptr [rcx], dil
0x001DA843: lea rcx, [rcx + 1]
0x001DA847: lea rax, [rdx + rcx]
0x001DA84B: cmp rax, r8
0x001DA84E: jne 0x1401da840
```

### flag2 @ `0x001DA81E`

```asm
0x001DA7EB: mov dword ptr [rbx + 0x3a0], eax
0x001DA7F1: cmp dword ptr [rbx + 0x3a0], 0
0x001DA7F8: jl 0x1401da869
0x001DA7FA: xor eax, eax
0x001DA7FC: mov qword ptr [rsp + 0x30], rdi
0x001DA801: xor edi, edi
0x001DA803: lea rcx, [rbx + 0x398]
0x001DA80A: mov qword ptr [rbx + 0x258], rdi
0x001DA811: mov r8d, 3
0x001DA817: mov qword ptr [rbx + 0x260], rax
0x001DA81E: mov dword ptr [rbx + 0x268], eax
0x001DA824: lea rax, [rcx + 3]
0x001DA828: cmp rcx, rax
0x001DA82B: cmova r8d, edi
0x001DA82F: ja 0x1401da850
0x001DA831: mov rdx, rcx
0x001DA834: neg rdx
0x001DA837: nop word ptr [rax + rax]
0x001DA840: mov byte ptr [rcx], dil
0x001DA843: lea rcx, [rcx + 1]
0x001DA847: lea rax, [rdx + rcx]
0x001DA84B: cmp rax, r8
0x001DA84E: jne 0x1401da840
0x001DA850: mov rax, qword ptr [rbx]
```

### counter @ `0x001DA85E`

```asm
0x001DA837: nop word ptr [rax + rax]
0x001DA840: mov byte ptr [rcx], dil
0x001DA843: lea rcx, [rcx + 1]
0x001DA847: lea rax, [rdx + rcx]
0x001DA84B: cmp rax, r8
0x001DA84E: jne 0x1401da840
0x001DA850: mov rax, qword ptr [rbx]
0x001DA853: xor edx, edx
0x001DA855: mov rcx, rbx
0x001DA858: call qword ptr [rax + 0x80]
0x001DA85E: mov dword ptr [rbx + 0x27c], edi
0x001DA864: mov rdi, qword ptr [rsp + 0x30]
0x001DA869: add rsp, 0x20
0x001DA86D: pop rbx
0x001DA86E: ret
0x001DA86F: int3
0x001DA870: push rbp
0x001DA872: push rbx
0x001DA873: push rsi
0x001DA874: push rdi
0x001DA875: push r12
0x001DA877: push r14
0x001DA879: push r15
0x001DA87B: lea rbp, [rsp - 0x920]
```

### reg_9A029C_field @ `0x001DA8AD`

```asm
0x001DA879: push r15
0x001DA87B: lea rbp, [rsp - 0x920]
0x001DA883: sub rsp, 0xa20
0x001DA88A: mov qword ptr [rsp + 0x70], 0xfffffffffffffffe
0x001DA893: mov rax, qword ptr [rip + 0x5fc056]
0x001DA89A: xor rax, rsp
0x001DA89D: mov qword ptr [rbp + 0x910], rax
0x001DA8A4: mov esi, edx
0x001DA8A6: mov rdi, rcx
0x001DA8A9: mov dword ptr [rsp + 0x30], edx
0x001DA8AD: mov dword ptr [rsp + 0x38], r8d
0x001DA8B2: mov dword ptr [rsp + 0x40], r9d
0x001DA8B7: mov eax, dword ptr [rbp + 0x980]
0x001DA8BD: xor r12d, r12d
0x001DA8C0: test eax, eax
0x001DA8C2: cmovs eax, r12d
0x001DA8C6: mov dword ptr [rbp + 0x980], eax
0x001DA8CC: mov eax, dword ptr [rbp + 0x988]
0x001DA8D2: mov ecx, 0x64
0x001DA8D7: test eax, eax
0x001DA8D9: cmovs eax, ecx
0x001DA8DC: mov dword ptr [rbp + 0x988], eax
0x001DA8E2: mov dword ptr [rsp + 0x58], ecx
0x001DA8E6: mov dword ptr [rsp + 0x50], r12d
```

### reg_9A0290_field @ `0x001DADA9`

```asm
0x001DAD8E: mov eax, dword ptr [rbp - 8]
0x001DAD91: add al, 7
0x001DAD93: xor eax, ecx
0x001DAD95: xor eax, 0x72
0x001DAD98: mov byte ptr [rbp + 7], al
0x001DAD9B: movsx ecx, byte ptr [rbp + 7]
0x001DAD9F: mov eax, dword ptr [rbp - 8]
0x001DADA2: add al, 8
0x001DADA4: xor eax, ecx
0x001DADA6: xor eax, 0x72
0x001DADA9: mov byte ptr [rbp + 8], al
0x001DADAC: movsx ecx, byte ptr [rbp + 8]
0x001DADB0: mov eax, dword ptr [rbp - 8]
0x001DADB3: add al, 9
0x001DADB5: xor eax, ecx
0x001DADB7: xor eax, 0x6f
0x001DADBA: mov byte ptr [rbp + 9], al
0x001DADBD: movsx ecx, byte ptr [rbp + 9]
0x001DADC1: mov eax, dword ptr [rbp - 8]
0x001DADC4: add al, 0xa
0x001DADC6: xor eax, ecx
0x001DADC8: xor eax, 0x72
0x001DADCB: mov byte ptr [rbp + 0xa], al
0x001DADCE: movsx ecx, byte ptr [rbp + 0xa]
```

### reg_9A02A0_field @ `0x001DB11D`

```asm
0x001DB0EA: je 0x1401db95c
0x001DB0F0: mov qword ptr [rbp + 0x90], 0xf
0x001DB0FB: mov qword ptr [rbp + 0x88], r12
0x001DB102: mov byte ptr [rbp + 0x78], 0
0x001DB106: test esi, esi
0x001DB108: jle 0x1401db306
0x001DB10E: mov dword ptr [rbp + 0x40], 0xe
0x001DB115: mov eax, dword ptr [rbp + 0x40]
0x001DB118: xor eax, 0x7b
0x001DB11B: inc eax
0x001DB11D: mov byte ptr [rbp + 0x44], al
0x001DB120: movsx ecx, byte ptr [rbp + 0x44]
0x001DB124: xor ecx, 0x7d
0x001DB127: inc ecx
0x001DB129: mov byte ptr [rbp + 0x45], cl
0x001DB12C: movsx ecx, byte ptr [rbp + 0x45]
0x001DB130: xor ecx, 0x43
0x001DB133: inc ecx
0x001DB135: mov byte ptr [rbp + 0x46], cl
0x001DB138: movsx ecx, byte ptr [rbp + 0x46]
0x001DB13C: xor ecx, 0x20
0x001DB13F: inc ecx
0x001DB141: mov byte ptr [rbp + 0x47], cl
0x001DB144: movsx ecx, byte ptr [rbp + 0x47]
```

### reg_9A0298_field @ `0x001DB4BF`

```asm
0x001DB48A: mov qword ptr [rbp + 0x108], r12
0x001DB491: mov byte ptr [rbp + 0xf8], 0
0x001DB498: lea rcx, [rbp + 0x138]
0x001DB49F: call 0x140032ef0
0x001DB4A4: cmp dword ptr [rsp + 0x40], 0
0x001DB4A9: jle 0x1401db5d4
0x001DB4AF: mov dword ptr [rbp + 0x28], 0x31
0x001DB4B6: mov eax, dword ptr [rbp + 0x28]
0x001DB4B9: xor eax, 0x7b
0x001DB4BC: add eax, 3
0x001DB4BF: mov byte ptr [rbp + 0x2c], al
0x001DB4C2: movsx ecx, byte ptr [rbp + 0x2c]
0x001DB4C6: xor ecx, 0x7d
0x001DB4C9: add ecx, 3
0x001DB4CC: mov byte ptr [rbp + 0x2d], cl
0x001DB4CF: movsx ecx, byte ptr [rbp + 0x2d]
0x001DB4D3: xor ecx, 0x43
0x001DB4D6: add ecx, 3
0x001DB4D9: mov byte ptr [rbp + 0x2e], cl
0x001DB4DC: movsx ecx, byte ptr [rbp + 0x2e]
0x001DB4E0: xor ecx, 0x20
0x001DB4E3: add ecx, 3
0x001DB4E6: mov byte ptr [rbp + 0x2f], cl
0x001DB4E9: movsx ecx, byte ptr [rbp + 0x2f]
```

### reg_9A029C_field @ `0x001DB55B`

```asm
0x001DB53B: xor ecx, 0x65
0x001DB53E: add ecx, 3
0x001DB541: mov byte ptr [rbp + 0x36], cl
0x001DB544: movsx ecx, byte ptr [rbp + 0x36]
0x001DB548: xor ecx, 0x6d
0x001DB54B: add ecx, 3
0x001DB54E: mov byte ptr [rbp + 0x37], cl
0x001DB551: movsx ecx, byte ptr [rbp + 0x37]
0x001DB555: xor ecx, 0x70
0x001DB558: add ecx, 3
0x001DB55B: mov byte ptr [rbp + 0x38], cl
0x001DB55E: movsx ecx, byte ptr [rbp + 0x38]
0x001DB562: xor ecx, 0x20
0x001DB565: add ecx, 3
0x001DB568: mov byte ptr [rbp + 0x39], cl
0x001DB56B: mov byte ptr [rbp + 0x3a], 0
0x001DB56F: movzx eax, byte ptr [rbp + 0x2c]
0x001DB573: lea rdx, [rbp + 0x178]
0x001DB57A: lea rcx, [rbp + 0x28]
0x001DB57E: call 0x1401ec2a0
0x001DB583: nop
0x001DB584: cmp qword ptr [rax + 0x18], 0x10
0x001DB589: jb 0x1401db58e
0x001DB58B: mov rax, qword ptr [rax]
```

### reg_9A0290_field @ `0x001DB9E0`

```asm
0x001DB9C9: call 0x1403b24c0
0x001DB9CE: add rsp, 0xa20
0x001DB9D5: pop r15
0x001DB9D7: pop r14
0x001DB9D9: pop r12
0x001DB9DB: pop rdi
0x001DB9DC: pop rsi
0x001DB9DD: pop rbx
0x001DB9DE: pop rbp
0x001DB9DF: ret
0x001DB9E0: mov qword ptr [rsp + 8], rbx
0x001DB9E5: push rdi
0x001DB9E6: sub rsp, 0x20
0x001DB9EA: cmp qword ptr [rcx + 0xd0], 0
0x001DB9F2: mov edi, r8d
0x001DB9F5: mov rbx, rcx
0x001DB9F8: je 0x1401dba1c
0x001DB9FA: mov r8b, 1
0x001DB9FD: call 0x1401d61a0
0x001DBA02: test edi, edi
0x001DBA04: jle 0x1401dba10
0x001DBA06: mov edx, edi
0x001DBA08: mov rcx, rbx
0x001DBA0B: call 0x1401e9930
```

### gpu_table_key @ `0x001DBA9B`

```asm
0x001DBA79: mov ecx, dword ptr [rcx + 0x39c]
0x001DBA7F: lea r10, [rip + 0x2e1c4a]
0x001DBA86: cmp dword ptr [rax], ecx
0x001DBA88: je 0x1401dba98
0x001DBA8A: add rax, 8
0x001DBA8E: cmp rax, r10
0x001DBA91: jne 0x1401dba86
0x001DBA93: or eax, 0xffffffff
0x001DBA96: jmp 0x1401dba9b
0x001DBA98: mov eax, dword ptr [rax + 4]
0x001DBA9B: mov dword ptr [rbx + 0x3a0], eax
0x001DBAA1: cmp dword ptr [rbx + 0x3a0], esi
0x001DBAA7: jl 0x1401dbb5a
0x001DBAAD: cmp dword ptr [rbx + 0x258], edx
0x001DBAB3: jne 0x1401dbada
0x001DBAB5: cmp dword ptr [rbx + 0x25c], r8d
0x001DBABC: jne 0x1401dbada
0x001DBABE: mov rax, qword ptr [rbx + 0x260]
0x001DBAC5: cmp rax, qword ptr [r9]
0x001DBAC8: jne 0x1401dbada
0x001DBACA: mov eax, dword ptr [rbx + 0x268]
0x001DBAD0: cmp eax, dword ptr [r9 + 8]
0x001DBAD4: jne 0x1401dbada
0x001DBAD6: xor cl, cl
```

### flag0 @ `0x001DBAEE`

```asm
0x001DBAC8: jne 0x1401dbada
0x001DBACA: mov eax, dword ptr [rbx + 0x268]
0x001DBAD0: cmp eax, dword ptr [r9 + 8]
0x001DBAD4: jne 0x1401dbada
0x001DBAD6: xor cl, cl
0x001DBAD8: jmp 0x1401dbadc
0x001DBADA: mov cl, 1
0x001DBADC: mov dword ptr [rbx + 0x258], edx
0x001DBAE2: mov dword ptr [rbx + 0x25c], r8d
0x001DBAE9: movsd xmm0, qword ptr [r9]
0x001DBAEE: movsd qword ptr [rbx + 0x260], xmm0
0x001DBAF6: mov eax, dword ptr [r9 + 8]
0x001DBAFA: mov dword ptr [rbx + 0x268], eax
0x001DBB00: lea eax, [rdx - 8]
0x001DBB03: cmp eax, 1
0x001DBB06: cmovbe edx, esi
0x001DBB09: mov dword ptr [rbx + 0x258], edx
0x001DBB0F: test cl, cl
0x001DBB11: je 0x1401dbb50
0x001DBB13: lea rax, [rbx + 0x398]
0x001DBB1A: lea rcx, [rax + 3]
0x001DBB1E: mov edx, 3
0x001DBB23: cmp rax, rcx
0x001DBB26: cmova rdx, rsi
```

### flag2 @ `0x001DBAFA`

```asm
0x001DBAD0: cmp eax, dword ptr [r9 + 8]
0x001DBAD4: jne 0x1401dbada
0x001DBAD6: xor cl, cl
0x001DBAD8: jmp 0x1401dbadc
0x001DBADA: mov cl, 1
0x001DBADC: mov dword ptr [rbx + 0x258], edx
0x001DBAE2: mov dword ptr [rbx + 0x25c], r8d
0x001DBAE9: movsd xmm0, qword ptr [r9]
0x001DBAEE: movsd qword ptr [rbx + 0x260], xmm0
0x001DBAF6: mov eax, dword ptr [r9 + 8]
0x001DBAFA: mov dword ptr [rbx + 0x268], eax
0x001DBB00: lea eax, [rdx - 8]
0x001DBB03: cmp eax, 1
0x001DBB06: cmovbe edx, esi
0x001DBB09: mov dword ptr [rbx + 0x258], edx
0x001DBB0F: test cl, cl
0x001DBB11: je 0x1401dbb50
0x001DBB13: lea rax, [rbx + 0x398]
0x001DBB1A: lea rcx, [rax + 3]
0x001DBB1E: mov edx, 3
0x001DBB23: cmp rax, rcx
0x001DBB26: cmova rdx, rsi
0x001DBB2A: ja 0x1401dbb50
0x001DBB2C: mov r8, rax
```

### retry @ `0x001DBB63`

```asm
0x001DBB36: nop word ptr [rax + rax]
0x001DBB40: mov byte ptr [rax], sil
0x001DBB43: lea rax, [rax + 1]
0x001DBB47: lea rcx, [r8 + rax]
0x001DBB4B: cmp rcx, rdx
0x001DBB4E: jne 0x1401dbb40
0x001DBB50: mov eax, 0x1f4
0x001DBB55: jmp 0x1401dc09a
0x001DBB5A: mov ecx, dword ptr [rbx + 0x278]
0x001DBB60: lea eax, [rcx + 1]
0x001DBB63: mov dword ptr [rbx + 0x278], eax
0x001DBB69: cmp ecx, 4
0x001DBB6C: jge 0x1401dc098
0x001DBB72: mov edx, 3
0x001DBB77: mov dword ptr [rbp - 0x39], edx
0x001DBB7A: mov eax, dword ptr [rbp - 0x39]
0x001DBB7D: add al, dl
0x001DBB7F: movsx ecx, al
0x001DBB82: xor ecx, 0x77
0x001DBB85: mov dword ptr [rbp - 0x35], ecx
0x001DBB88: mov eax, dword ptr [rbp - 0x35]
0x001DBB8B: mov ecx, dword ptr [rbp - 0x39]
0x001DBB8E: xor ecx, eax
0x001DBB90: xor ecx, 0x2d
```

### reg_9A029C_field @ `0x001DC6C9`

```asm
0x001DC68C: movups xmm0, xmmword ptr [rsp + 0x30]
0x001DC691: movups xmmword ptr [rbp + 0xc80], xmm0
0x001DC698: mov qword ptr [rsp + 0x30], r14
0x001DC69D: movups xmm0, xmmword ptr [rsp + 0x30]
0x001DC6A2: movups xmmword ptr [rbp + 0xc90], xmm0
0x001DC6A9: mov dword ptr [rsp + 0x30], esi
0x001DC6AD: movups xmm0, xmmword ptr [rsp + 0x30]
0x001DC6B2: movups xmmword ptr [rbp + 0xca0], xmm0
0x001DC6B9: mov qword ptr [rsp + 0x30], 0x2a2
0x001DC6C2: lea rcx, [rbp + 0xc80]
0x001DC6C9: mov qword ptr [rsp + 0x38], rcx
0x001DC6CE: movups xmm0, xmmword ptr [rsp + 0x30]
0x001DC6D3: movups xmmword ptr [rsp + 0x78], xmm0
0x001DC6D8: mov dword ptr [rbp - 0x78], ebx
0x001DC6DB: lea rcx, [rbp + 0x820]
0x001DC6E2: mov qword ptr [rbp - 0x70], rcx
0x001DC6E6: xorps xmm0, xmm0
0x001DC6E9: movdqu xmmword ptr [rbp - 0x68], xmm0
0x001DC6EE: mov qword ptr [rbp - 0x58], rbx
0x001DC6F2: mov rdx, rax
0x001DC6F5: lea rcx, [rsp + 0x78]
0x001DC6FA: call 0x140036ad0
0x001DC6FF: nop
0x001DC700: mov r9, qword ptr [rbp - 0x68]
```

### reg_9A0290_field @ `0x001DCCE4`

```asm
0x001DCC9A: lea rcx, [rbp + 0xa60]
0x001DCCA1: mov qword ptr [rbp + 0xa58], rcx
0x001DCCA8: lea rdi, [rip + 0x257009]
0x001DCCAF: mov qword ptr [rbp + 0xa50], rdi
0x001DCCB6: lea rcx, [rbp + 0xa80]
0x001DCCBD: mov qword ptr [rbp + 0xa68], rcx
0x001DCCC4: mov qword ptr [rbp + 0xa70], rbx
0x001DCCCB: mov qword ptr [rbp + 0xa78], 0x1f4
0x001DCCD6: lea rcx, [rip + 0x256f33]
0x001DCCDD: mov qword ptr [rbp + 0xa60], rcx
0x001DCCE4: mov qword ptr [rbp + 8], rax
0x001DCCE8: mov dword ptr [rsp + 0x30], 0x13a
0x001DCCF0: movups xmm0, xmmword ptr [rsp + 0x30]
0x001DCCF5: movups xmmword ptr [rbp + 0xcb0], xmm0
0x001DCCFC: mov qword ptr [rsp + 0x30], r14
0x001DCD01: movups xmm0, xmmword ptr [rsp + 0x30]
0x001DCD06: movups xmmword ptr [rbp + 0xcc0], xmm0
0x001DCD0D: mov dword ptr [rsp + 0x30], esi
0x001DCD11: movups xmm0, xmmword ptr [rsp + 0x30]
0x001DCD16: movups xmmword ptr [rbp + 0xcd0], xmm0
0x001DCD1D: mov qword ptr [rsp + 0x30], 0x2a2
0x001DCD26: lea rcx, [rbp + 0xcb0]
0x001DCD2D: mov qword ptr [rsp + 0x38], rcx
0x001DCD32: movups xmm0, xmmword ptr [rsp + 0x30]
```

### reg_9A029C_field @ `0x001DCD2D`

```asm
0x001DCCF0: movups xmm0, xmmword ptr [rsp + 0x30]
0x001DCCF5: movups xmmword ptr [rbp + 0xcb0], xmm0
0x001DCCFC: mov qword ptr [rsp + 0x30], r14
0x001DCD01: movups xmm0, xmmword ptr [rsp + 0x30]
0x001DCD06: movups xmmword ptr [rbp + 0xcc0], xmm0
0x001DCD0D: mov dword ptr [rsp + 0x30], esi
0x001DCD11: movups xmm0, xmmword ptr [rsp + 0x30]
0x001DCD16: movups xmmword ptr [rbp + 0xcd0], xmm0
0x001DCD1D: mov qword ptr [rsp + 0x30], 0x2a2
0x001DCD26: lea rcx, [rbp + 0xcb0]
0x001DCD2D: mov qword ptr [rsp + 0x38], rcx
0x001DCD32: movups xmm0, xmmword ptr [rsp + 0x30]
0x001DCD37: movups xmmword ptr [rbp - 0x50], xmm0
0x001DCD3B: mov dword ptr [rbp - 0x40], ebx
0x001DCD3E: lea rcx, [rbp + 0xa50]
0x001DCD45: mov qword ptr [rbp - 0x38], rcx
0x001DCD49: xorps xmm0, xmm0
0x001DCD4C: movdqu xmmword ptr [rbp - 0x30], xmm0
0x001DCD51: mov qword ptr [rbp - 0x20], rbx
0x001DCD55: mov rdx, rax
0x001DCD58: lea rcx, [rbp - 0x50]
0x001DCD5C: call 0x140036ad0
0x001DCD61: nop
0x001DCD62: mov r9, qword ptr [rbp - 0x30]
```

### reg_9A0298_field @ `0x001DDAF5`

```asm
0x001DDAC5: lea r8, [rsp + 0x4c]
0x001DDACA: lea rdx, [rsp + 0x50]
0x001DDACF: mov rcx, rax
0x001DDAD2: call 0x1401d3fc0
0x001DDAD7: nop
0x001DDAD8: lea rcx, [rbp + 0x778]
0x001DDADF: call 0x140032ef0
0x001DDAE4: mov dword ptr [rsp + 0x20], 1
0x001DDAEC: jmp 0x1401de505
0x001DDAF1: mov dword ptr [rsp + 0x24], ebx
0x001DDAF5: mov dword ptr [rsp + 0x2c], ebx
0x001DDAF9: mov esi, ebx
0x001DDAFB: lea rdx, [rsp + 0x24]
0x001DDB00: lea rcx, [rbp + 0xce0]
0x001DDB07: call qword ptr [rip + 0x609f0b]
0x001DDB0D: mov dword ptr [rsp + 0x54], eax
0x001DDB11: test eax, eax
0x001DDB13: je 0x1401dde41
0x001DDB19: mov dword ptr [rsp + 0x58], 0x163
0x001DDB21: mov dword ptr [rbp + 0x4f0], 0x2e
0x001DDB2B: mov eax, dword ptr [rbp + 0x4f0]
0x001DDB31: xor eax, 0x4e
0x001DDB34: add eax, 0xa
0x001DDB37: mov byte ptr [rbp + 0x4f4], al
```

### reg_9A0298_field @ `0x001DE1AA`

```asm
0x001DE181: mov rax, qword ptr [rax]
0x001DE184: lea r8, [rsp + 0x5c]
0x001DE189: lea rdx, [rsp + 0x60]
0x001DE18E: mov rcx, rax
0x001DE191: call 0x1401d3fc0
0x001DE196: nop
0x001DE197: lea rcx, [rbp + 0x7b8]
0x001DE19E: call 0x140032ef0
0x001DE1A3: mov edi, 3
0x001DE1A8: mov ecx, ebx
0x001DE1AA: mov dword ptr [rsp + 0x2c], ebx
0x001DE1AE: jmp 0x1401de1b4
0x001DE1B0: mov ecx, dword ptr [rsp + 0x2c]
0x001DE1B4: mov eax, dword ptr [rsp + 0x24]
0x001DE1B8: add eax, ecx
0x001DE1BA: mov dword ptr [rsp + 0x24], eax
0x001DE1BE: jne 0x1401de1d1
0x001DE1C0: test esi, esi
0x001DE1C2: cmovne edi, esi
0x001DE1C5: mov dword ptr [rsp + 0x20], edi
0x001DE1C9: test edi, edi
0x001DE1CB: jne 0x1401de505
0x001DE1D1: cmp eax, 0x80
0x001DE1D6: ja 0x1401de7a7
```

### max_idx @ `0x001DE968`

```asm
0x001DE945: test eax, eax
0x001DE947: jne 0x1401df608
0x001DE94D: mov edi, dword ptr [rsp + 0x24]
0x001DE951: cmp edi, 0xf
0x001DE954: ja 0x1401df608
0x001DE95A: mov eax, dword ptr [rbx + 0x274]
0x001DE960: cmp edi, eax
0x001DE962: jl 0x1401de968
0x001DE964: test eax, eax
0x001DE966: jns 0x1401de96e
0x001DE968: mov dword ptr [rbx + 0x274], edi
0x001DE96E: movsxd rax, dword ptr [rbx + 0x270]
0x001DE975: xor ecx, ecx
0x001DE977: cmp edi, eax
0x001DE979: je 0x1401de993
0x001DE97B: cmp eax, 2
0x001DE97E: ja 0x1401de987
0x001DE980: mov byte ptr [rax + rbx + 0x280], cl
0x001DE987: mov dword ptr [rbx + 0x278], ecx
0x001DE98D: mov dword ptr [rbx + 0x270], edi
0x001DE993: cmp edi, 2
0x001DE996: jle 0x1401de9a3
0x001DE998: mov dword ptr [rbx + 0x27c], ecx
0x001DE99E: jmp 0x1401df608
```

### retry @ `0x001DE987`

```asm
0x001DE964: test eax, eax
0x001DE966: jns 0x1401de96e
0x001DE968: mov dword ptr [rbx + 0x274], edi
0x001DE96E: movsxd rax, dword ptr [rbx + 0x270]
0x001DE975: xor ecx, ecx
0x001DE977: cmp edi, eax
0x001DE979: je 0x1401de993
0x001DE97B: cmp eax, 2
0x001DE97E: ja 0x1401de987
0x001DE980: mov byte ptr [rax + rbx + 0x280], cl
0x001DE987: mov dword ptr [rbx + 0x278], ecx
0x001DE98D: mov dword ptr [rbx + 0x270], edi
0x001DE993: cmp edi, 2
0x001DE996: jle 0x1401de9a3
0x001DE998: mov dword ptr [rbx + 0x27c], ecx
0x001DE99E: jmp 0x1401df608
0x001DE9A3: test sil, sil
0x001DE9A6: jne 0x1401de998
0x001DE9A8: mov ecx, dword ptr [rbx + 0x27c]
0x001DE9AE: lea eax, [rcx + 1]
0x001DE9B1: mov dword ptr [rbx + 0x27c], eax
0x001DE9B7: cmp ecx, 0x14
0x001DE9BA: jl 0x1401df608
0x001DE9C0: lea rdx, [rbp]
```

### state_idx @ `0x001DE98D`

```asm
0x001DE966: jns 0x1401de96e
0x001DE968: mov dword ptr [rbx + 0x274], edi
0x001DE96E: movsxd rax, dword ptr [rbx + 0x270]
0x001DE975: xor ecx, ecx
0x001DE977: cmp edi, eax
0x001DE979: je 0x1401de993
0x001DE97B: cmp eax, 2
0x001DE97E: ja 0x1401de987
0x001DE980: mov byte ptr [rax + rbx + 0x280], cl
0x001DE987: mov dword ptr [rbx + 0x278], ecx
0x001DE98D: mov dword ptr [rbx + 0x270], edi
0x001DE993: cmp edi, 2
0x001DE996: jle 0x1401de9a3
0x001DE998: mov dword ptr [rbx + 0x27c], ecx
0x001DE99E: jmp 0x1401df608
0x001DE9A3: test sil, sil
0x001DE9A6: jne 0x1401de998
0x001DE9A8: mov ecx, dword ptr [rbx + 0x27c]
0x001DE9AE: lea eax, [rcx + 1]
0x001DE9B1: mov dword ptr [rbx + 0x27c], eax
0x001DE9B7: cmp ecx, 0x14
0x001DE9BA: jl 0x1401df608
0x001DE9C0: lea rdx, [rbp]
0x001DE9C4: mov rcx, rbx
```

### counter @ `0x001DE998`

```asm
0x001DE975: xor ecx, ecx
0x001DE977: cmp edi, eax
0x001DE979: je 0x1401de993
0x001DE97B: cmp eax, 2
0x001DE97E: ja 0x1401de987
0x001DE980: mov byte ptr [rax + rbx + 0x280], cl
0x001DE987: mov dword ptr [rbx + 0x278], ecx
0x001DE98D: mov dword ptr [rbx + 0x270], edi
0x001DE993: cmp edi, 2
0x001DE996: jle 0x1401de9a3
0x001DE998: mov dword ptr [rbx + 0x27c], ecx
0x001DE99E: jmp 0x1401df608
0x001DE9A3: test sil, sil
0x001DE9A6: jne 0x1401de998
0x001DE9A8: mov ecx, dword ptr [rbx + 0x27c]
0x001DE9AE: lea eax, [rcx + 1]
0x001DE9B1: mov dword ptr [rbx + 0x27c], eax
0x001DE9B7: cmp ecx, 0x14
0x001DE9BA: jl 0x1401df608
0x001DE9C0: lea rdx, [rbp]
0x001DE9C4: mov rcx, rbx
0x001DE9C7: call 0x1401e0ca0
0x001DE9CC: test al, al
0x001DE9CE: jne 0x1401df1af
```

### counter @ `0x001DE9B1`

```asm
0x001DE987: mov dword ptr [rbx + 0x278], ecx
0x001DE98D: mov dword ptr [rbx + 0x270], edi
0x001DE993: cmp edi, 2
0x001DE996: jle 0x1401de9a3
0x001DE998: mov dword ptr [rbx + 0x27c], ecx
0x001DE99E: jmp 0x1401df608
0x001DE9A3: test sil, sil
0x001DE9A6: jne 0x1401de998
0x001DE9A8: mov ecx, dword ptr [rbx + 0x27c]
0x001DE9AE: lea eax, [rcx + 1]
0x001DE9B1: mov dword ptr [rbx + 0x27c], eax
0x001DE9B7: cmp ecx, 0x14
0x001DE9BA: jl 0x1401df608
0x001DE9C0: lea rdx, [rbp]
0x001DE9C4: mov rcx, rbx
0x001DE9C7: call 0x1401e0ca0
0x001DE9CC: test al, al
0x001DE9CE: jne 0x1401df1af
0x001DE9D4: mov ecx, dword ptr [rbx + 0x278]
0x001DE9DA: lea eax, [rcx + 1]
0x001DE9DD: mov dword ptr [rbx + 0x278], eax
0x001DE9E3: cmp ecx, 4
0x001DE9E6: jge 0x1401df608
0x001DE9EC: mov dword ptr [rsp + 0x30], 0x61
```

### retry @ `0x001DE9DD`

```asm
0x001DE9B1: mov dword ptr [rbx + 0x27c], eax
0x001DE9B7: cmp ecx, 0x14
0x001DE9BA: jl 0x1401df608
0x001DE9C0: lea rdx, [rbp]
0x001DE9C4: mov rcx, rbx
0x001DE9C7: call 0x1401e0ca0
0x001DE9CC: test al, al
0x001DE9CE: jne 0x1401df1af
0x001DE9D4: mov ecx, dword ptr [rbx + 0x278]
0x001DE9DA: lea eax, [rcx + 1]
0x001DE9DD: mov dword ptr [rbx + 0x278], eax
0x001DE9E3: cmp ecx, 4
0x001DE9E6: jge 0x1401df608
0x001DE9EC: mov dword ptr [rsp + 0x30], 0x61
0x001DE9F4: mov eax, dword ptr [rsp + 0x30]
0x001DE9F8: add al, 0x61
0x001DE9FA: movsx ecx, al
0x001DE9FD: xor ecx, 0x76
0x001DEA00: mov dword ptr [rsp + 0x34], ecx
0x001DEA04: mov eax, dword ptr [rsp + 0x34]
0x001DEA08: mov ecx, dword ptr [rsp + 0x30]
0x001DEA0C: xor ecx, eax
0x001DEA0E: xor ecx, 0x7b
0x001DEA11: mov byte ptr [rsp + 0x38], cl
```

### reg_9A029C_field @ `0x001DEA11`

```asm
0x001DE9EC: mov dword ptr [rsp + 0x30], 0x61
0x001DE9F4: mov eax, dword ptr [rsp + 0x30]
0x001DE9F8: add al, 0x61
0x001DE9FA: movsx ecx, al
0x001DE9FD: xor ecx, 0x76
0x001DEA00: mov dword ptr [rsp + 0x34], ecx
0x001DEA04: mov eax, dword ptr [rsp + 0x34]
0x001DEA08: mov ecx, dword ptr [rsp + 0x30]
0x001DEA0C: xor ecx, eax
0x001DEA0E: xor ecx, 0x7b
0x001DEA11: mov byte ptr [rsp + 0x38], cl
0x001DEA15: movsx ecx, byte ptr [rsp + 0x38]
0x001DEA1A: mov eax, dword ptr [rsp + 0x30]
0x001DEA1E: inc al
0x001DEA20: xor eax, ecx
0x001DEA22: xor eax, 0x7d
0x001DEA25: mov byte ptr [rsp + 0x39], al
0x001DEA29: movsx ecx, byte ptr [rsp + 0x39]
0x001DEA2E: mov eax, dword ptr [rsp + 0x30]
0x001DEA32: add al, 2
0x001DEA34: xor eax, ecx
0x001DEA36: xor eax, 0x3a
0x001DEA39: mov byte ptr [rsp + 0x3a], al
0x001DEA3D: movsx ecx, byte ptr [rsp + 0x3a]
```

### reg_9A02A0_field @ `0x001DEB01`

```asm
0x001DEAE2: mov eax, dword ptr [rsp + 0x30]
0x001DEAE6: add al, 0xb
0x001DEAE8: xor eax, ecx
0x001DEAEA: xor eax, 0x74
0x001DEAED: mov byte ptr [rsp + 0x43], al
0x001DEAF1: movsx ecx, byte ptr [rsp + 0x43]
0x001DEAF6: mov eax, dword ptr [rsp + 0x30]
0x001DEAFA: add al, 0xc
0x001DEAFC: xor eax, ecx
0x001DEAFE: xor eax, 0x6f
0x001DEB01: mov byte ptr [rsp + 0x44], al
0x001DEB05: movsx ecx, byte ptr [rsp + 0x44]
0x001DEB0A: mov eax, dword ptr [rsp + 0x30]
0x001DEB0E: add al, 0xd
0x001DEB10: xor eax, ecx
0x001DEB12: xor eax, 0x20
0x001DEB15: mov byte ptr [rsp + 0x45], al
0x001DEB19: movsx ecx, byte ptr [rsp + 0x45]
0x001DEB1E: mov eax, dword ptr [rsp + 0x30]
0x001DEB22: add al, 0xe
0x001DEB24: xor eax, ecx
0x001DEB26: xor eax, 0x73
0x001DEB29: mov byte ptr [rsp + 0x46], al
0x001DEB2D: movsx ecx, byte ptr [rsp + 0x46]
```

### retry @ `0x001DF25C`

```asm
0x001DF233: je 0x1401df608
0x001DF239: mov r9d, edi
0x001DF23C: mov r8, rsi
0x001DF23F: lea rdx, [rbp]
0x001DF243: mov rcx, rbx
0x001DF246: call 0x1401ecb90
0x001DF24B: test al, al
0x001DF24D: jne 0x1401df608
0x001DF253: mov ecx, dword ptr [rbx + 0x278]
0x001DF259: lea eax, [rcx + 1]
0x001DF25C: mov dword ptr [rbx + 0x278], eax
0x001DF262: cmp ecx, 4
0x001DF265: jge 0x1401df608
0x001DF26B: mov dword ptr [rbp - 0x60], 0x21
0x001DF272: mov dword ptr [rbp - 0x5c], 0x7c
0x001DF279: mov eax, dword ptr [rbp - 0x5c]
0x001DF27C: xor eax, 0x5a
0x001DF27F: mov byte ptr [rbp - 0x58], al
0x001DF282: movsx ecx, byte ptr [rbp - 0x58]
0x001DF286: xor ecx, 0x5c
0x001DF289: mov byte ptr [rbp - 0x57], cl
0x001DF28C: movsx ecx, byte ptr [rbp - 0x57]
0x001DF290: xor ecx, 0x1b
0x001DF293: mov byte ptr [rbp - 0x56], cl
```

### retry @ `0x001DF454`

```asm
0x001DF427: je 0x1401df608
0x001DF42D: mov r9d, edi
0x001DF430: lea r8, [rbp + 0xc0]
0x001DF437: lea rdx, [rbp]
0x001DF43B: mov rcx, rbx
0x001DF43E: call 0x1401ecb90
0x001DF443: test al, al
0x001DF445: jne 0x1401df608
0x001DF44B: mov ecx, dword ptr [rbx + 0x278]
0x001DF451: lea eax, [rcx + 1]
0x001DF454: mov dword ptr [rbx + 0x278], eax
0x001DF45A: cmp ecx, 4
0x001DF45D: jge 0x1401df608
0x001DF463: mov dword ptr [rbp - 0x30], 0x6c
0x001DF46A: mov dword ptr [rbp - 0x2c], 0x1f
0x001DF471: mov eax, dword ptr [rbp - 0x2c]
0x001DF474: xor eax, 0x17
0x001DF477: mov byte ptr [rbp - 0x28], al
0x001DF47A: movsx ecx, byte ptr [rbp - 0x28]
0x001DF47E: xor ecx, 0x11
0x001DF481: mov byte ptr [rbp - 0x27], cl
0x001DF484: movsx ecx, byte ptr [rbp - 0x27]
0x001DF488: xor ecx, 0x56
0x001DF48B: mov byte ptr [rbp - 0x26], cl
```

### reg_9A0290_field @ `0x001DF64B`

```asm
0x001DF627: mov rdi, qword ptr [r11 + 0x28]
0x001DF62B: mov rsp, r11
0x001DF62E: pop rbp
0x001DF62F: ret
0x001DF630: mov rax, rsp
0x001DF633: push r13
0x001DF635: push r14
0x001DF637: push r15
0x001DF639: sub rsp, 0xc00
0x001DF640: mov qword ptr [rax - 0xb30], 0xfffffffffffffffe
0x001DF64B: mov qword ptr [rax + 8], rbx
0x001DF64F: mov qword ptr [rax + 0x10], rsi
0x001DF653: mov qword ptr [rax + 0x18], rdi
0x001DF657: mov qword ptr [rax + 0x20], r12
0x001DF65B: mov rax, qword ptr [rip + 0x5f728e]
0x001DF662: xor rax, rsp
0x001DF665: mov qword ptr [rsp + 0xbf0], rax
0x001DF66D: xor r14d, r14d
0x001DF670: mov dword ptr [rsp + 0x24], r14d
0x001DF675: lea rcx, [rsp + 0x24]
0x001DF67A: call qword ptr [rip + 0x6081b8]
0x001DF680: mov ebx, eax
0x001DF682: test eax, eax
0x001DF684: je 0x1401dfd9d
```

### reg_9A029C_field @ `0x001DFACF`

```asm
0x001DFA8E: movups xmm0, xmmword ptr [rsp + 0x50]
0x001DFA93: movups xmmword ptr [rsp + 0xb90], xmm0
0x001DFA9B: mov qword ptr [rsp + 0x50], rdi
0x001DFAA0: movups xmm0, xmmword ptr [rsp + 0x50]
0x001DFAA5: movups xmmword ptr [rsp + 0xba0], xmm0
0x001DFAAD: mov dword ptr [rsp + 0x50], ebx
0x001DFAB1: movups xmm0, xmmword ptr [rsp + 0x50]
0x001DFAB6: movups xmmword ptr [rsp + 0xbb0], xmm0
0x001DFABE: mov qword ptr [rsp + 0x30], 0x2a2
0x001DFAC7: lea rcx, [rsp + 0xb90]
0x001DFACF: mov qword ptr [rsp + 0x38], rcx
0x001DFAD4: movups xmm0, xmmword ptr [rsp + 0x30]
0x001DFAD9: movups xmmword ptr [rsp + 0x78], xmm0
0x001DFADE: mov dword ptr [rsp + 0x88], r14d
0x001DFAE6: lea rcx, [rsp + 0x730]
0x001DFAEE: mov qword ptr [rsp + 0x90], rcx
0x001DFAF6: xorps xmm0, xmm0
0x001DFAF9: movdqu xmmword ptr [rsp + 0x98], xmm0
0x001DFB02: mov qword ptr [rsp + 0xa8], r14
0x001DFB0A: mov rdx, rax
0x001DFB0D: lea rcx, [rsp + 0x78]
0x001DFB12: call 0x140036ad0
0x001DFB17: nop
0x001DFB18: mov r8, qword ptr [rsp + 0x98]
```

### reg_9A0298_field @ `0x001E0546`

```asm
0x001E0513: mov rcx, qword ptr [rsp + 0x48]
0x001E0518: mov byte ptr [rsp + 0x6c4], 0
0x001E0520: lea rdx, [rsp + 0x6a0]
0x001E0528: call 0x1401d3a40
0x001E052D: mov dword ptr [rsp + 0x28], eax
0x001E0531: test eax, eax
0x001E0533: je 0x1401e0a67
0x001E0539: mov ecx, eax
0x001E053B: call qword ptr [rip + 0x607317]
0x001E0541: mov qword ptr [rsp + 0x68], rax
0x001E0546: mov dword ptr [rsp + 0x2c], 0xdc
0x001E054E: mov dword ptr [rsp + 0x590], 0x38
0x001E0559: mov eax, dword ptr [rsp + 0x590]
0x001E0560: add al, 0x38
0x001E0562: movsx ecx, al
0x001E0565: xor ecx, 0x24
0x001E0568: mov dword ptr [rsp + 0x594], ecx
0x001E056F: mov eax, dword ptr [rsp + 0x594]
0x001E0576: mov ecx, dword ptr [rsp + 0x590]
0x001E057D: xor ecx, eax
0x001E057F: xor ecx, 0x4e
0x001E0582: mov byte ptr [rsp + 0x598], cl
0x001E0589: movsx ecx, byte ptr [rsp + 0x598]
0x001E0591: mov eax, dword ptr [rsp + 0x590]
```

### reg_9A0290_field @ `0x001E0B40`

```asm
0x001E0B2E: mov r12, qword ptr [r11 + 0x38]
0x001E0B32: mov rsp, r11
0x001E0B35: pop r15
0x001E0B37: pop r14
0x001E0B39: pop r13
0x001E0B3B: ret
0x001E0B3C: int3
0x001E0B3D: int3
0x001E0B3E: int3
0x001E0B3F: int3
0x001E0B40: mov qword ptr [rsp + 8], rbx
0x001E0B45: push rdi
0x001E0B46: sub rsp, 0x20
0x001E0B4A: mov rax, qword ptr [rcx + 8]
0x001E0B4E: mov rdi, rdx
0x001E0B51: mov rbx, rcx
0x001E0B54: cmp rdx, rax
0x001E0B57: jae 0x1401e0b9e
0x001E0B59: mov rcx, qword ptr [rcx]
0x001E0B5C: cmp rcx, rdx
0x001E0B5F: ja 0x1401e0b9e
0x001E0B61: sub rdi, rcx
0x001E0B64: cmp rax, qword ptr [rbx + 0x10]
0x001E0B68: jne 0x1401e0b77
```

### reg_9A0290_field @ `0x001E0B8E`

```asm
0x001E0B6A: mov edx, 1
0x001E0B6F: mov rcx, rbx
0x001E0B72: call 0x1401d5fc0
0x001E0B77: mov rcx, qword ptr [rbx + 8]
0x001E0B7B: test rcx, rcx
0x001E0B7E: je 0x1401e0bc0
0x001E0B80: mov rax, qword ptr [rbx]
0x001E0B83: and rdi, 0xfffffffffffffff0
0x001E0B87: movups xmm0, xmmword ptr [rdi + rax]
0x001E0B8B: movups xmmword ptr [rcx], xmm0
0x001E0B8E: add qword ptr [rbx + 8], 0x10
0x001E0B93: mov rbx, qword ptr [rsp + 0x30]
0x001E0B98: add rsp, 0x20
0x001E0B9C: pop rdi
0x001E0B9D: ret
0x001E0B9E: cmp rax, qword ptr [rbx + 0x10]
0x001E0BA2: jne 0x1401e0bb1
0x001E0BA4: mov edx, 1
0x001E0BA9: mov rcx, rbx
0x001E0BAC: call 0x1401d5fc0
0x001E0BB1: mov rax, qword ptr [rbx + 8]
0x001E0BB5: test rax, rax
0x001E0BB8: je 0x1401e0bc0
0x001E0BBA: movups xmm0, xmmword ptr [rdi]
```

### reg_9A0290_field @ `0x001E0BC0`

```asm
0x001E0B9E: cmp rax, qword ptr [rbx + 0x10]
0x001E0BA2: jne 0x1401e0bb1
0x001E0BA4: mov edx, 1
0x001E0BA9: mov rcx, rbx
0x001E0BAC: call 0x1401d5fc0
0x001E0BB1: mov rax, qword ptr [rbx + 8]
0x001E0BB5: test rax, rax
0x001E0BB8: je 0x1401e0bc0
0x001E0BBA: movups xmm0, xmmword ptr [rdi]
0x001E0BBD: movups xmmword ptr [rax], xmm0
0x001E0BC0: add qword ptr [rbx + 8], 0x10
0x001E0BC5: mov rbx, qword ptr [rsp + 0x30]
0x001E0BCA: add rsp, 0x20
0x001E0BCE: pop rdi
0x001E0BCF: ret
0x001E0BD0: mov qword ptr [rsp + 8], rbx
0x001E0BD5: push rdi
0x001E0BD6: sub rsp, 0x20
0x001E0BDA: mov rbx, rcx
0x001E0BDD: mov rdi, rdx
0x001E0BE0: mov rcx, qword ptr [rcx + 8]
0x001E0BE4: cmp rdx, rcx
0x001E0BE7: jae 0x1401e0c4a
0x001E0BE9: mov rax, qword ptr [rbx]
```

### reg_9A0290_field @ `0x001E0BD0`

```asm
0x001E0BB1: mov rax, qword ptr [rbx + 8]
0x001E0BB5: test rax, rax
0x001E0BB8: je 0x1401e0bc0
0x001E0BBA: movups xmm0, xmmword ptr [rdi]
0x001E0BBD: movups xmmword ptr [rax], xmm0
0x001E0BC0: add qword ptr [rbx + 8], 0x10
0x001E0BC5: mov rbx, qword ptr [rsp + 0x30]
0x001E0BCA: add rsp, 0x20
0x001E0BCE: pop rdi
0x001E0BCF: ret
0x001E0BD0: mov qword ptr [rsp + 8], rbx
0x001E0BD5: push rdi
0x001E0BD6: sub rsp, 0x20
0x001E0BDA: mov rbx, rcx
0x001E0BDD: mov rdi, rdx
0x001E0BE0: mov rcx, qword ptr [rcx + 8]
0x001E0BE4: cmp rdx, rcx
0x001E0BE7: jae 0x1401e0c4a
0x001E0BE9: mov rax, qword ptr [rbx]
0x001E0BEC: cmp rax, rdx
0x001E0BEF: ja 0x1401e0c4a
0x001E0BF1: sub rdi, rax
0x001E0BF4: movabs rax, 0x6666666666666667
0x001E0BFE: imul rdi
```

### reg_9A0290_field @ `0x001E0C8C`

```asm
0x001E0C61: test rcx, rcx
0x001E0C64: je 0x1401e0c8c
0x001E0C66: mov rax, qword ptr [rdi]
0x001E0C69: lea rdx, [rdi + 8]
0x001E0C6D: mov qword ptr [rcx], rax
0x001E0C70: add rcx, 8
0x001E0C74: mov qword ptr [rcx + 0x18], 0xf
0x001E0C7C: mov qword ptr [rcx + 0x10], 0
0x001E0C84: mov byte ptr [rcx], 0
0x001E0C87: call 0x140044ef0
0x001E0C8C: add qword ptr [rbx + 8], 0x28
0x001E0C91: mov rbx, qword ptr [rsp + 0x30]
0x001E0C96: add rsp, 0x20
0x001E0C9A: pop rdi
0x001E0C9B: ret
0x001E0C9C: int3
0x001E0C9D: int3
0x001E0C9E: int3
0x001E0C9F: int3
0x001E0CA0: mov qword ptr [rsp + 0x18], rbx
0x001E0CA5: push rbp
0x001E0CA6: push rsi
0x001E0CA7: push rdi
0x001E0CA8: lea rbp, [rsp - 0x1740]
```

### reg_9A0298_field @ `0x001E0D3A`

```asm
0x001E0D05: mov eax, 0x15
0x001E0D0A: mov dword ptr [rsp + 0x20], 0x11808
0x001E0D12: mov word ptr [rsp + 0x28], ax
0x001E0D17: mov word ptr [rsp + 0x40], ax
0x001E0D1C: mov word ptr [rsp + 0x58], ax
0x001E0D21: mov word ptr [rsp + 0x70], ax
0x001E0D26: mov word ptr [rbp - 0x78], ax
0x001E0D2A: mov word ptr [rbp - 0x60], ax
0x001E0D2E: mov word ptr [rbp - 0x48], ax
0x001E0D32: mov dword ptr [rsp + 0x24], 7
0x001E0D3A: mov dword ptr [rsp + 0x2c], 0x9a0290
0x001E0D42: mov dword ptr [rsp + 0x44], 0x9a0294
0x001E0D4A: mov dword ptr [rsp + 0x5c], 0x9a0298
0x001E0D52: mov dword ptr [rsp + 0x74], 0x9a029c
0x001E0D5A: mov dword ptr [rbp - 0x74], 0x9a02a0
0x001E0D61: mov dword ptr [rbp - 0x5c], 0x9a02a4
0x001E0D68: mov dword ptr [rbp - 0x44], 0x9a02a8
0x001E0D6F: call rdi
0x001E0D71: test eax, eax
0x001E0D73: jne 0x1401e0ce0
0x001E0D79: mov rcx, qword ptr [rsp + 0x38]
0x001E0D7E: mov rax, rcx
0x001E0D81: shr rax, 0x11
0x001E0D85: and eax, 0x7f
```

### reg_9A02A0_field @ `0x001E0D42`

```asm
0x001E0D0A: mov dword ptr [rsp + 0x20], 0x11808
0x001E0D12: mov word ptr [rsp + 0x28], ax
0x001E0D17: mov word ptr [rsp + 0x40], ax
0x001E0D1C: mov word ptr [rsp + 0x58], ax
0x001E0D21: mov word ptr [rsp + 0x70], ax
0x001E0D26: mov word ptr [rbp - 0x78], ax
0x001E0D2A: mov word ptr [rbp - 0x60], ax
0x001E0D2E: mov word ptr [rbp - 0x48], ax
0x001E0D32: mov dword ptr [rsp + 0x24], 7
0x001E0D3A: mov dword ptr [rsp + 0x2c], 0x9a0290
0x001E0D42: mov dword ptr [rsp + 0x44], 0x9a0294
0x001E0D4A: mov dword ptr [rsp + 0x5c], 0x9a0298
0x001E0D52: mov dword ptr [rsp + 0x74], 0x9a029c
0x001E0D5A: mov dword ptr [rbp - 0x74], 0x9a02a0
0x001E0D61: mov dword ptr [rbp - 0x5c], 0x9a02a4
0x001E0D68: mov dword ptr [rbp - 0x44], 0x9a02a8
0x001E0D6F: call rdi
0x001E0D71: test eax, eax
0x001E0D73: jne 0x1401e0ce0
0x001E0D79: mov rcx, qword ptr [rsp + 0x38]
0x001E0D7E: mov rax, rcx
0x001E0D81: shr rax, 0x11
0x001E0D85: and eax, 0x7f
0x001E0D88: mov dword ptr [rbx], eax
```

### reg_9A0290_field @ `0x001E0DB0`

```asm
0x001E0D8A: mov rax, rcx
0x001E0D8D: shr rax, 0x18
0x001E0D91: and eax, 0x7f
0x001E0D94: shr rcx, 8
0x001E0D98: mov dword ptr [rbx + 4], eax
0x001E0D9B: and ecx, 0x1ff
0x001E0DA1: movzx eax, byte ptr [rsp + 0x38]
0x001E0DA6: mov dword ptr [rbx + 0xc], eax
0x001E0DA9: mov eax, dword ptr [rsp + 0x50]
0x001E0DAD: and eax, 0x7f
0x001E0DB0: mov dword ptr [rbx + 8], ecx
0x001E0DB3: mov rcx, qword ptr [rsp + 0x50]
0x001E0DB8: mov dword ptr [rbx + 0x10], eax
0x001E0DBB: mov rax, rcx
0x001E0DBE: shr rax, 7
0x001E0DC2: and eax, 0x7f
0x001E0DC5: mov dword ptr [rbx + 0x14], eax
0x001E0DC8: mov rax, rcx
0x001E0DCB: shr rax, 0xe
0x001E0DCF: and eax, 0x3f
0x001E0DD2: shr rcx, 0x14
0x001E0DD6: mov dword ptr [rbx + 0x18], eax
0x001E0DD9: and ecx, 0x3f
0x001E0DDC: mov eax, dword ptr [rsp + 0x68]
```

### reg_9A0298_field @ `0x001E0E12`

```asm
0x001E0DF1: shr rax, 4
0x001E0DF5: and eax, 0xf
0x001E0DF8: mov dword ptr [rbx + 0x24], eax
0x001E0DFB: mov rax, rcx
0x001E0DFE: shr rax, 8
0x001E0E02: and eax, 0x7f
0x001E0E05: mov dword ptr [rbx + 0x28], eax
0x001E0E08: mov rax, rcx
0x001E0E0B: shr rax, 0x10
0x001E0E0F: and eax, 0x7f
0x001E0E12: mov dword ptr [rbx + 0x2c], eax
0x001E0E15: mov rax, rcx
0x001E0E18: shr rax, 0x18
0x001E0E1C: and eax, 0xf
0x001E0E1F: shr rcx, 0x1c
0x001E0E23: mov dword ptr [rbx + 0x30], eax
0x001E0E26: and ecx, 0xf
0x001E0E29: mov dword ptr [rbx + 0x34], ecx
0x001E0E2C: mov rcx, qword ptr [rbp - 0x80]
0x001E0E30: mov rax, rcx
0x001E0E33: shr rax, 9
0x001E0E37: movzx eax, al
0x001E0E3A: mov dword ptr [rbx + 0x38], eax
0x001E0E3D: mov eax, ecx
```

### reg_9A029C_field @ `0x001E0E3A`

```asm
0x001E0E18: shr rax, 0x18
0x001E0E1C: and eax, 0xf
0x001E0E1F: shr rcx, 0x1c
0x001E0E23: mov dword ptr [rbx + 0x30], eax
0x001E0E26: and ecx, 0xf
0x001E0E29: mov dword ptr [rbx + 0x34], ecx
0x001E0E2C: mov rcx, qword ptr [rbp - 0x80]
0x001E0E30: mov rax, rcx
0x001E0E33: shr rax, 9
0x001E0E37: movzx eax, al
0x001E0E3A: mov dword ptr [rbx + 0x38], eax
0x001E0E3D: mov eax, ecx
0x001E0E3F: and eax, 0x1f
0x001E0E42: shr rcx, 0x18
0x001E0E46: mov dword ptr [rbx + 0x3c], eax
0x001E0E49: and ecx, 0xf
0x001E0E4C: mov rax, qword ptr [rbp - 0x68]
0x001E0E50: shr rax, 0xf
0x001E0E54: and eax, 0x3f
0x001E0E57: mov dword ptr [rbx + 0x40], ecx
0x001E0E5A: mov rcx, qword ptr [rbp - 0x50]
0x001E0E5E: mov dword ptr [rbx + 0x44], eax
0x001E0E61: mov eax, dword ptr [rbp - 0x50]
0x001E0E64: and eax, 7
```

### reg_9A02A0_field @ `0x001E0E5E`

```asm
0x001E0E3D: mov eax, ecx
0x001E0E3F: and eax, 0x1f
0x001E0E42: shr rcx, 0x18
0x001E0E46: mov dword ptr [rbx + 0x3c], eax
0x001E0E49: and ecx, 0xf
0x001E0E4C: mov rax, qword ptr [rbp - 0x68]
0x001E0E50: shr rax, 0xf
0x001E0E54: and eax, 0x3f
0x001E0E57: mov dword ptr [rbx + 0x40], ecx
0x001E0E5A: mov rcx, qword ptr [rbp - 0x50]
0x001E0E5E: mov dword ptr [rbx + 0x44], eax
0x001E0E61: mov eax, dword ptr [rbp - 0x50]
0x001E0E64: and eax, 7
0x001E0E67: mov dword ptr [rbx + 0x48], eax
0x001E0E6A: mov rax, rcx
0x001E0E6D: shr rcx, 0x12
0x001E0E71: and ecx, 3
0x001E0E74: shr rax, 4
0x001E0E78: and eax, 0x7f
0x001E0E7B: mov dword ptr [rbx + 0x50], ecx
0x001E0E7E: mov rcx, qword ptr [rbp - 0x38]
0x001E0E82: mov dword ptr [rbx + 0x4c], eax
0x001E0E85: mov rax, rcx
0x001E0E88: shr rax, 0x10
```

### reg_9A029C_field @ `0x001E1E41`

```asm
0x001E1E05: movups xmm0, xmmword ptr [rsp + 0x20]
0x001E1E0A: movaps xmmword ptr [rbp + 0x3f00], xmm0
0x001E1E11: mov ecx, dword ptr [rbp + 0x4dc]
0x001E1E17: mov dword ptr [rsp + 0x20], ecx
0x001E1E1B: movups xmm0, xmmword ptr [rsp + 0x20]
0x001E1E20: movaps xmmword ptr [rbp + 0x3f10], xmm0
0x001E1E27: mov qword ptr [rsp + 0x20], 0x3232b
0x001E1E30: lea rcx, [rbp + 0x3ed0]
0x001E1E37: mov qword ptr [rsp + 0x28], rcx
0x001E1E3C: movups xmm0, xmmword ptr [rsp + 0x20]
0x001E1E41: movups xmmword ptr [rsp + 0x38], xmm0
0x001E1E46: mov dword ptr [rsp + 0x48], r14d
0x001E1E4B: lea rcx, [rbp + 0x2a0]
0x001E1E52: mov qword ptr [rsp + 0x50], rcx
0x001E1E57: xorps xmm0, xmm0
0x001E1E5A: movdqu xmmword ptr [rsp + 0x58], xmm0
0x001E1E60: mov qword ptr [rsp + 0x68], r14
0x001E1E65: mov rdx, rax
0x001E1E68: lea rcx, [rsp + 0x38]
0x001E1E6D: call 0x140036ad0
0x001E1E72: nop
0x001E1E73: mov r9, qword ptr [rsp + 0x58]
0x001E1E78: test r9, r9
0x001E1E7B: je 0x1401e1ead
```

### reg_9A029C_field @ `0x001E2EB5`

```asm
0x001E2E79: movups xmm0, xmmword ptr [rsp + 0x20]
0x001E2E7E: movaps xmmword ptr [rbp + 0x3f10], xmm0
0x001E2E85: mov ecx, dword ptr [rbp + 0x4ec]
0x001E2E8B: mov dword ptr [rsp + 0x20], ecx
0x001E2E8F: movups xmm0, xmmword ptr [rsp + 0x20]
0x001E2E94: movaps xmmword ptr [rbp + 0x3f20], xmm0
0x001E2E9B: mov qword ptr [rsp + 0x20], 0x3232b
0x001E2EA4: lea rcx, [rbp + 0x3ee0]
0x001E2EAB: mov qword ptr [rsp + 0x28], rcx
0x001E2EB0: movups xmm0, xmmword ptr [rsp + 0x20]
0x001E2EB5: movups xmmword ptr [rsp + 0x38], xmm0
0x001E2EBA: mov dword ptr [rsp + 0x48], r14d
0x001E2EBF: lea rcx, [rbp + 0x2b0]
0x001E2EC6: mov qword ptr [rsp + 0x50], rcx
0x001E2ECB: xorps xmm0, xmm0
0x001E2ECE: movdqu xmmword ptr [rsp + 0x58], xmm0
0x001E2ED4: mov qword ptr [rsp + 0x68], r14
0x001E2ED9: mov rdx, rax
0x001E2EDC: lea rcx, [rsp + 0x38]
0x001E2EE1: call 0x140036ad0
0x001E2EE6: nop
0x001E2EE7: mov r9, qword ptr [rsp + 0x58]
0x001E2EEC: test r9, r9
0x001E2EEF: je 0x1401e2f21
```

### reg_9A0298_field @ `0x001E314A`

```asm
0x001E312A: xor ecx, 0x65
0x001E312D: add ecx, 0xb
0x001E3130: mov byte ptr [rbp + 0x2a], cl
0x001E3133: movsx ecx, byte ptr [rbp + 0x2a]
0x001E3137: xor ecx, 0x72
0x001E313A: add ecx, 0xb
0x001E313D: mov byte ptr [rbp + 0x2b], cl
0x001E3140: movsx ecx, byte ptr [rbp + 0x2b]
0x001E3144: xor ecx, 0x72
0x001E3147: add ecx, 0xb
0x001E314A: mov byte ptr [rbp + 0x2c], cl
0x001E314D: movsx ecx, byte ptr [rbp + 0x2c]
0x001E3151: xor ecx, 0x6f
0x001E3154: add ecx, 0xb
0x001E3157: mov byte ptr [rbp + 0x2d], cl
0x001E315A: movsx ecx, byte ptr [rbp + 0x2d]
0x001E315E: xor ecx, 0x72
0x001E3161: add ecx, 0xb
0x001E3164: mov byte ptr [rbp + 0x2e], cl
0x001E3167: movsx ecx, byte ptr [rbp + 0x2e]
0x001E316B: xor ecx, 0x20
0x001E316E: add ecx, 0xb
0x001E3171: mov byte ptr [rbp + 0x2f], cl
0x001E3174: movsx ecx, byte ptr [rbp + 0x2f]
```

### reg_9A029C_field @ `0x001E31E6`

```asm
0x001E31C6: xor ecx, 0x70
0x001E31C9: add ecx, 0xb
0x001E31CC: mov byte ptr [rbp + 0x36], cl
0x001E31CF: movsx ecx, byte ptr [rbp + 0x36]
0x001E31D3: xor ecx, 0x69
0x001E31D6: add ecx, 0xb
0x001E31D9: mov byte ptr [rbp + 0x37], cl
0x001E31DC: movsx ecx, byte ptr [rbp + 0x37]
0x001E31E0: xor ecx, 0x57
0x001E31E3: add ecx, 0xb
0x001E31E6: mov byte ptr [rbp + 0x38], cl
0x001E31E9: movsx ecx, byte ptr [rbp + 0x38]
0x001E31ED: xor ecx, 0x72
0x001E31F0: add ecx, 0xb
0x001E31F3: mov byte ptr [rbp + 0x39], cl
0x001E31F6: movsx ecx, byte ptr [rbp + 0x39]
0x001E31FA: xor ecx, 0x61
0x001E31FD: add ecx, 0xb
0x001E3200: mov byte ptr [rbp + 0x3a], cl
0x001E3203: movsx ecx, byte ptr [rbp + 0x3a]
0x001E3207: xor ecx, 0x70
0x001E320A: add ecx, 0xb
0x001E320D: mov byte ptr [rbp + 0x3b], cl
0x001E3210: movsx ecx, byte ptr [rbp + 0x3b]
```

### reg_9A02A0_field @ `0x001E3282`

```asm
0x001E3262: xor ecx, 0x7b
0x001E3265: add ecx, 0xb
0x001E3268: mov byte ptr [rbp + 0x42], cl
0x001E326B: movsx ecx, byte ptr [rbp + 0x42]
0x001E326F: xor ecx, 0x7d
0x001E3272: add ecx, 0xb
0x001E3275: mov byte ptr [rbp + 0x43], cl
0x001E3278: movsx ecx, byte ptr [rbp + 0x43]
0x001E327C: xor ecx, 0x20
0x001E327F: add ecx, 0xb
0x001E3282: mov byte ptr [rbp + 0x44], cl
0x001E3285: movsx ecx, byte ptr [rbp + 0x44]
0x001E3289: xor ecx, 0x3a
0x001E328C: add ecx, 0xb
0x001E328F: mov byte ptr [rbp + 0x45], cl
0x001E3292: movsx ecx, byte ptr [rbp + 0x45]
0x001E3296: xor ecx, 0x20
0x001E3299: add ecx, 0xb
0x001E329C: mov byte ptr [rbp + 0x46], cl
0x001E329F: movsx ecx, byte ptr [rbp + 0x46]
0x001E32A3: xor ecx, 0x7b
0x001E32A6: add ecx, 0xb
0x001E32A9: mov byte ptr [rbp + 0x47], cl
0x001E32AC: movsx ecx, byte ptr [rbp + 0x47]
```

### reg_9A0298_field @ `0x001E33BC`

```asm
0x001E3399: mov edi, eax
0x001E339B: mov dword ptr [rsp + 0x20], eax
0x001E339F: test eax, eax
0x001E33A1: jne 0x1401e351f
0x001E33A7: mov eax, 0x10624dd3
0x001E33AC: imul dword ptr [rbx + 0x140]
0x001E33B2: sar edx, 6
0x001E33B5: mov eax, edx
0x001E33B7: shr eax, 0x1f
0x001E33BA: add edx, eax
0x001E33BC: mov dword ptr [rsp + 0x2c], edx
0x001E33C0: mov dword ptr [rbp + 0x50], 0x4c
0x001E33C7: mov eax, dword ptr [rbp + 0x50]
0x001E33CA: xor eax, 0x7b
0x001E33CD: mov byte ptr [rbp + 0x54], al
0x001E33D0: movsx ecx, byte ptr [rbp + 0x54]
0x001E33D4: xor ecx, 0x7d
0x001E33D7: mov byte ptr [rbp + 0x55], cl
0x001E33DA: movsx ecx, byte ptr [rbp + 0x55]
0x001E33DE: xor ecx, 0x3a
0x001E33E1: mov byte ptr [rbp + 0x56], cl
0x001E33E4: movsx ecx, byte ptr [rbp + 0x56]
0x001E33E8: xor ecx, 0x20
0x001E33EB: mov byte ptr [rbp + 0x57], cl
```

### reg_9A029C_field @ `0x001E3B10`

```asm
0x001E3AEF: mov rcx, rax
0x001E3AF2: call 0x14017b330
0x001E3AF7: nop
0x001E3AF8: lea rcx, [rbp + 0x110]
0x001E3AFF: jmp 0x1401e3dff
0x001E3B04: imul ecx
0x001E3B06: sar edx, 6
0x001E3B09: mov eax, edx
0x001E3B0B: shr eax, 0x1f
0x001E3B0E: add edx, eax
0x001E3B10: mov dword ptr [rsp + 0x38], edx
0x001E3B14: mov dword ptr [rbp - 0x20], 0x7a
0x001E3B1B: mov eax, dword ptr [rbp - 0x20]
0x001E3B1E: xor eax, 0x7b
0x001E3B21: add eax, 5
0x001E3B24: mov byte ptr [rbp - 0x1c], al
0x001E3B27: movsx ecx, byte ptr [rbp - 0x1c]
0x001E3B2B: xor ecx, 0x7d
0x001E3B2E: add ecx, 5
0x001E3B31: mov byte ptr [rbp - 0x1b], cl
0x001E3B34: movsx ecx, byte ptr [rbp - 0x1b]
0x001E3B38: xor ecx, 0x3a
0x001E3B3B: add ecx, 5
0x001E3B3E: mov byte ptr [rbp - 0x1a], cl
```

### reg_9A0290_field @ `0x001E3CF8`

```asm
0x001E3CD8: xor ecx, 0x20
0x001E3CDB: add ecx, 5
0x001E3CDE: mov byte ptr [rbp + 6], cl
0x001E3CE1: movsx ecx, byte ptr [rbp + 6]
0x001E3CE5: xor ecx, 0x7b
0x001E3CE8: add ecx, 5
0x001E3CEB: mov byte ptr [rbp + 7], cl
0x001E3CEE: movsx ecx, byte ptr [rbp + 7]
0x001E3CF2: xor ecx, 0x7d
0x001E3CF5: add ecx, 5
0x001E3CF8: mov byte ptr [rbp + 8], cl
0x001E3CFB: movsx ecx, byte ptr [rbp + 8]
0x001E3CFF: xor ecx, 0x25
0x001E3D02: add ecx, 5
0x001E3D05: mov byte ptr [rbp + 9], cl
0x001E3D08: movsx ecx, byte ptr [rbp + 9]
0x001E3D0C: xor ecx, 0x20
0x001E3D0F: add ecx, 5
0x001E3D12: mov byte ptr [rbp + 0xa], cl
0x001E3D15: movsx ecx, byte ptr [rbp + 0xa]
0x001E3D19: xor ecx, 0x2d
0x001E3D1C: add ecx, 5
0x001E3D1F: mov byte ptr [rbp + 0xb], cl
0x001E3D22: movsx ecx, byte ptr [rbp + 0xb]
```

### reg_9A0298_field @ `0x001E3ECE`

```asm
0x001E3E98: mov esi, ebx
0x001E3E9A: mov dword ptr [rsp + 0x20], ebx
0x001E3E9E: xor edx, edx
0x001E3EA0: lea r8d, [rbx + 0x68]
0x001E3EA4: lea rcx, [rbp + 0x1a0]
0x001E3EAB: call 0x1403d3050
0x001E3EB0: mov dword ptr [rbp + 0x1a0], 0x20068
0x001E3EBA: lea rdx, [rbp + 0x1a0]
0x001E3EC1: mov rcx, qword ptr [rdi + 0xd0]
0x001E3EC8: call qword ptr [rip + 0x603b82]
0x001E3ECE: mov dword ptr [rsp + 0x2c], eax
0x001E3ED2: test eax, eax
0x001E3ED4: je 0x1401e41b1
0x001E3EDA: mov dword ptr [rsp + 0x34], 0x55a
0x001E3EE2: mov dword ptr [rbp + 0x60], 0x7f
0x001E3EE9: mov eax, dword ptr [rbp + 0x60]
0x001E3EEC: xor eax, 0x4e
0x001E3EEF: add eax, 4
0x001E3EF2: mov byte ptr [rbp + 0x64], al
0x001E3EF5: movsx ecx, byte ptr [rbp + 0x64]
0x001E3EF9: xor ecx, 0x56
0x001E3EFC: add ecx, 4
0x001E3EFF: mov byte ptr [rbp + 0x65], cl
0x001E3F02: movsx ecx, byte ptr [rbp + 0x65]
```

### reg_9A02A0_field @ `0x001E41E0`

```asm
0x001E41B5: mov dword ptr [rsp + 0x30], ebx
0x001E41B9: test esi, esi
0x001E41BB: jne 0x1401e512e
0x001E41C1: cmp byte ptr [rbp + 0x1a4], 1
0x001E41C8: jb 0x1401e4213
0x001E41CA: cmp dword ptr [rbp + 0x1a8], 1
0x001E41D1: jne 0x1401e4213
0x001E41D3: mov eax, dword ptr [rbp + 0x1b4]
0x001E41D9: sar eax, 8
0x001E41DC: mov dword ptr [rsp + 0x24], eax
0x001E41E0: mov dword ptr [rsp + 0x44], 0x37
0x001E41E8: mov dword ptr [rsp + 0x38], 0x5a
0x001E41F0: lea rcx, [rsp + 0x24]
0x001E41F5: lea rdx, [rsp + 0x44]
0x001E41FA: cmp eax, 0x37
0x001E41FD: cmovle rcx, rdx
0x001E4201: lea rax, [rsp + 0x38]
0x001E4206: cmp dword ptr [rcx], 0x5a
0x001E4209: cmovl rax, rcx
0x001E420D: mov ebx, dword ptr [rax]
0x001E420F: mov dword ptr [rsp + 0x24], ebx
0x001E4213: xor eax, eax
0x001E4215: mov qword ptr [rbp + 0xc0], rax
0x001E421C: mov qword ptr [rbp + 0xc8], rax
```

### reg_9A029C_field @ `0x001E41E8`

```asm
0x001E41B9: test esi, esi
0x001E41BB: jne 0x1401e512e
0x001E41C1: cmp byte ptr [rbp + 0x1a4], 1
0x001E41C8: jb 0x1401e4213
0x001E41CA: cmp dword ptr [rbp + 0x1a8], 1
0x001E41D1: jne 0x1401e4213
0x001E41D3: mov eax, dword ptr [rbp + 0x1b4]
0x001E41D9: sar eax, 8
0x001E41DC: mov dword ptr [rsp + 0x24], eax
0x001E41E0: mov dword ptr [rsp + 0x44], 0x37
0x001E41E8: mov dword ptr [rsp + 0x38], 0x5a
0x001E41F0: lea rcx, [rsp + 0x24]
0x001E41F5: lea rdx, [rsp + 0x44]
0x001E41FA: cmp eax, 0x37
0x001E41FD: cmovle rcx, rdx
0x001E4201: lea rax, [rsp + 0x38]
0x001E4206: cmp dword ptr [rcx], 0x5a
0x001E4209: cmovl rax, rcx
0x001E420D: mov ebx, dword ptr [rax]
0x001E420F: mov dword ptr [rsp + 0x24], ebx
0x001E4213: xor eax, eax
0x001E4215: mov qword ptr [rbp + 0xc0], rax
0x001E421C: mov qword ptr [rbp + 0xc8], rax
0x001E4223: mov qword ptr [rbp + 0xd0], rax
```

### reg_9A0290_field @ `0x001E4735`

```asm
0x001E4718: xor ecx, 0x6c
0x001E471B: inc ecx
0x001E471D: mov byte ptr [rbp + 6], cl
0x001E4720: movsx ecx, byte ptr [rbp + 6]
0x001E4724: xor ecx, 0x69
0x001E4727: inc ecx
0x001E4729: mov byte ptr [rbp + 7], cl
0x001E472C: movsx ecx, byte ptr [rbp + 7]
0x001E4730: xor ecx, 0x6d
0x001E4733: inc ecx
0x001E4735: mov byte ptr [rbp + 8], cl
0x001E4738: movsx ecx, byte ptr [rbp + 8]
0x001E473C: xor ecx, 0x69
0x001E473F: inc ecx
0x001E4741: mov byte ptr [rbp + 9], cl
0x001E4744: movsx ecx, byte ptr [rbp + 9]
0x001E4748: xor ecx, 0x74
0x001E474B: inc ecx
0x001E474D: mov byte ptr [rbp + 0xa], cl
0x001E4750: movsx ecx, byte ptr [rbp + 0xa]
0x001E4754: xor ecx, 0x20
0x001E4757: inc ecx
0x001E4759: mov byte ptr [rbp + 0xb], cl
0x001E475C: movsx ecx, byte ptr [rbp + 0xb]
```

### reg_9A0298_field @ `0x001E4EF0`

```asm
0x001E4ECF: xor ecx, 0x64
0x001E4ED2: mov byte ptr [rbp + 0x29], cl
0x001E4ED5: movsx ecx, byte ptr [rbp + 0x29]
0x001E4ED9: xor ecx, 0x23
0x001E4EDC: mov byte ptr [rbp + 0x2a], cl
0x001E4EDF: movsx ecx, byte ptr [rbp + 0x2a]
0x001E4EE3: xor ecx, 0x39
0x001E4EE6: mov byte ptr [rbp + 0x2b], cl
0x001E4EE9: movsx ecx, byte ptr [rbp + 0x2b]
0x001E4EED: xor ecx, 0x4c
0x001E4EF0: mov byte ptr [rbp + 0x2c], cl
0x001E4EF3: movsx ecx, byte ptr [rbp + 0x2c]
0x001E4EF7: xor ecx, 0x77
0x001E4EFA: mov byte ptr [rbp + 0x2d], cl
0x001E4EFD: movsx ecx, byte ptr [rbp + 0x2d]
0x001E4F01: xor ecx, 0x78
0x001E4F04: mov byte ptr [rbp + 0x2e], cl
0x001E4F07: movsx ecx, byte ptr [rbp + 0x2e]
0x001E4F0B: xor ecx, 0x7b
0x001E4F0E: mov byte ptr [rbp + 0x2f], cl
0x001E4F11: movsx ecx, byte ptr [rbp + 0x2f]
0x001E4F15: xor ecx, 0x75
0x001E4F18: mov byte ptr [rbp + 0x30], cl
0x001E4F1B: movsx ecx, byte ptr [rbp + 0x30]
```

### reg_9A029C_field @ `0x001E4F68`

```asm
0x001E4F47: xor ecx, 0x39
0x001E4F4A: mov byte ptr [rbp + 0x35], cl
0x001E4F4D: movsx ecx, byte ptr [rbp + 0x35]
0x001E4F51: xor ecx, 0x6b
0x001E4F54: mov byte ptr [rbp + 0x36], cl
0x001E4F57: movsx ecx, byte ptr [rbp + 0x36]
0x001E4F5B: xor ecx, 0x7c
0x001E4F5E: mov byte ptr [rbp + 0x37], cl
0x001E4F61: movsx ecx, byte ptr [rbp + 0x37]
0x001E4F65: xor ecx, 0x6a
0x001E4F68: mov byte ptr [rbp + 0x38], cl
0x001E4F6B: movsx ecx, byte ptr [rbp + 0x38]
0x001E4F6F: xor ecx, 0x7c
0x001E4F72: mov byte ptr [rbp + 0x39], cl
0x001E4F75: movsx ecx, byte ptr [rbp + 0x39]
0x001E4F79: xor ecx, 0x6d
0x001E4F7C: mov byte ptr [rbp + 0x3a], cl
0x001E4F7F: movsx ecx, byte ptr [rbp + 0x3a]
0x001E4F83: xor ecx, 0x39
0x001E4F86: mov byte ptr [rbp + 0x3b], cl
0x001E4F89: movsx ecx, byte ptr [rbp + 0x3b]
0x001E4F8D: xor ecx, 0x6d
0x001E4F90: mov byte ptr [rbp + 0x3c], cl
0x001E4F93: movsx ecx, byte ptr [rbp + 0x3c]
```

### reg_9A02A0_field @ `0x001E4FE0`

```asm
0x001E4FBF: xor ecx, 0x78
0x001E4FC2: mov byte ptr [rbp + 0x41], cl
0x001E4FC5: movsx ecx, byte ptr [rbp + 0x41]
0x001E4FC9: xor ecx, 0x75
0x001E4FCC: mov byte ptr [rbp + 0x42], cl
0x001E4FCF: movsx ecx, byte ptr [rbp + 0x42]
0x001E4FD3: xor ecx, 0x39
0x001E4FD6: mov byte ptr [rbp + 0x43], cl
0x001E4FD9: movsx ecx, byte ptr [rbp + 0x43]
0x001E4FDD: xor ecx, 0x75
0x001E4FE0: mov byte ptr [rbp + 0x44], cl
0x001E4FE3: movsx ecx, byte ptr [rbp + 0x44]
0x001E4FE7: xor ecx, 0x70
0x001E4FEA: mov byte ptr [rbp + 0x45], cl
0x001E4FED: movsx ecx, byte ptr [rbp + 0x45]
0x001E4FF1: xor ecx, 0x74
0x001E4FF4: mov byte ptr [rbp + 0x46], cl
0x001E4FF7: movsx ecx, byte ptr [rbp + 0x46]
0x001E4FFB: xor ecx, 0x70
0x001E4FFE: mov byte ptr [rbp + 0x47], cl
0x001E5001: movsx ecx, byte ptr [rbp + 0x47]
0x001E5005: xor ecx, 0x6d
0x001E5008: mov byte ptr [rbp + 0x48], cl
0x001E500B: movsx ecx, byte ptr [rbp + 0x48]
```

### reg_9A029C_field @ `0x001E6B3A`

```asm
0x001E6B09: mov qword ptr [rbp + 0x4c8], 0x1f4
0x001E6B14: lea rcx, [rip + 0x24d0f5]
0x001E6B1B: mov qword ptr [rbp + 0x4b0], rcx
0x001E6B22: cmp qword ptr [rax + 0x18], 0x10
0x001E6B27: jb 0x1401e6b2e
0x001E6B29: mov rcx, qword ptr [rax]
0x001E6B2C: jmp 0x1401e6b31
0x001E6B2E: mov rcx, rax
0x001E6B31: mov rax, qword ptr [rax + 0x10]
0x001E6B35: mov qword ptr [rsp + 0x30], rcx
0x001E6B3A: mov qword ptr [rsp + 0x38], rax
0x001E6B3F: movups xmm0, xmmword ptr [rsp + 0x30]
0x001E6B44: movaps xmmword ptr [rbp + 0x40d0], xmm0
0x001E6B4B: mov dword ptr [rsp + 0x30], ebx
0x001E6B4F: movups xmm0, xmmword ptr [rsp + 0x30]
0x001E6B54: movaps xmmword ptr [rbp + 0x40e0], xmm0
0x001E6B5B: mov eax, dword ptr [rbp + 0x6d8]
0x001E6B61: mov dword ptr [rsp + 0x30], eax
0x001E6B65: movups xmm0, xmmword ptr [rsp + 0x30]
0x001E6B6A: movaps xmmword ptr [rbp + 0x40f0], xmm0
0x001E6B71: mov dword ptr [rsp + 0x30], edi
0x001E6B75: movups xmm0, xmmword ptr [rsp + 0x30]
0x001E6B7A: movaps xmmword ptr [rbp + 0x4100], xmm0
0x001E6B81: mov eax, dword ptr [rbp + 0x6dc]
```

### reg_9A029C_field @ `0x001E6BA7`

```asm
0x001E6B6A: movaps xmmword ptr [rbp + 0x40f0], xmm0
0x001E6B71: mov dword ptr [rsp + 0x30], edi
0x001E6B75: movups xmm0, xmmword ptr [rsp + 0x30]
0x001E6B7A: movaps xmmword ptr [rbp + 0x4100], xmm0
0x001E6B81: mov eax, dword ptr [rbp + 0x6dc]
0x001E6B87: mov dword ptr [rsp + 0x30], eax
0x001E6B8B: movups xmm0, xmmword ptr [rsp + 0x30]
0x001E6B90: movaps xmmword ptr [rbp + 0x4110], xmm0
0x001E6B97: mov qword ptr [rsp + 0x30], 0x3232b
0x001E6BA0: lea rax, [rbp + 0x40d0]
0x001E6BA7: mov qword ptr [rsp + 0x38], rax
0x001E6BAC: movups xmm0, xmmword ptr [rsp + 0x30]
0x001E6BB1: movups xmmword ptr [rsp + 0x50], xmm0
0x001E6BB6: mov dword ptr [rsp + 0x60], r15d
0x001E6BBB: lea rax, [rbp + 0x4a0]
0x001E6BC2: mov qword ptr [rsp + 0x68], rax
0x001E6BC7: xorps xmm0, xmm0
0x001E6BCA: movdqu xmmword ptr [rsp + 0x70], xmm0
0x001E6BD0: mov qword ptr [rbp - 0x80], r15
0x001E6BD4: lea rcx, [rsp + 0x50]
0x001E6BD9: call 0x140036ad0
0x001E6BDE: nop
0x001E6BDF: mov r9, qword ptr [rsp + 0x70]
0x001E6BE4: test r9, r9
```

### reg_9A029C_field @ `0x001E88C7`

```asm
0x001E8896: mov qword ptr [rbp + 0x4d8], 0x1f4
0x001E88A1: lea rcx, [rip + 0x24b368]
0x001E88A8: mov qword ptr [rbp + 0x4c0], rcx
0x001E88AF: cmp qword ptr [rax + 0x18], 0x10
0x001E88B4: jb 0x1401e88bb
0x001E88B6: mov rcx, qword ptr [rax]
0x001E88B9: jmp 0x1401e88be
0x001E88BB: mov rcx, rax
0x001E88BE: mov rax, qword ptr [rax + 0x10]
0x001E88C2: mov qword ptr [rsp + 0x30], rcx
0x001E88C7: mov qword ptr [rsp + 0x38], rax
0x001E88CC: movups xmm0, xmmword ptr [rsp + 0x30]
0x001E88D1: movaps xmmword ptr [rbp + 0x40e0], xmm0
0x001E88D8: mov dword ptr [rsp + 0x30], ebx
0x001E88DC: movups xmm0, xmmword ptr [rsp + 0x30]
0x001E88E1: movaps xmmword ptr [rbp + 0x40f0], xmm0
0x001E88E8: mov eax, dword ptr [rbp + 0x6e8]
0x001E88EE: mov dword ptr [rsp + 0x30], eax
0x001E88F2: movups xmm0, xmmword ptr [rsp + 0x30]
0x001E88F7: movaps xmmword ptr [rbp + 0x4100], xmm0
0x001E88FE: mov dword ptr [rsp + 0x30], edi
0x001E8902: movups xmm0, xmmword ptr [rsp + 0x30]
0x001E8907: movaps xmmword ptr [rbp + 0x4110], xmm0
0x001E890E: mov eax, dword ptr [rbp + 0x6ec]
```

### reg_9A029C_field @ `0x001E8934`

```asm
0x001E88F7: movaps xmmword ptr [rbp + 0x4100], xmm0
0x001E88FE: mov dword ptr [rsp + 0x30], edi
0x001E8902: movups xmm0, xmmword ptr [rsp + 0x30]
0x001E8907: movaps xmmword ptr [rbp + 0x4110], xmm0
0x001E890E: mov eax, dword ptr [rbp + 0x6ec]
0x001E8914: mov dword ptr [rsp + 0x30], eax
0x001E8918: movups xmm0, xmmword ptr [rsp + 0x30]
0x001E891D: movaps xmmword ptr [rbp + 0x4120], xmm0
0x001E8924: mov qword ptr [rsp + 0x30], 0x3232b
0x001E892D: lea rax, [rbp + 0x40e0]
0x001E8934: mov qword ptr [rsp + 0x38], rax
0x001E8939: movups xmm0, xmmword ptr [rsp + 0x30]
0x001E893E: movups xmmword ptr [rsp + 0x50], xmm0
0x001E8943: mov dword ptr [rsp + 0x60], r15d
0x001E8948: lea rax, [rbp + 0x4b0]
0x001E894F: mov qword ptr [rsp + 0x68], rax
0x001E8954: xorps xmm0, xmm0
0x001E8957: movdqu xmmword ptr [rsp + 0x70], xmm0
0x001E895D: mov qword ptr [rbp - 0x80], r15
0x001E8961: lea rcx, [rsp + 0x50]
0x001E8966: call 0x140036ad0
0x001E896B: nop
0x001E896C: mov r9, qword ptr [rsp + 0x70]
0x001E8971: test r9, r9
```

### reg_9A0298_field @ `0x001E8B32`

```asm
0x001E8AFA: mov qword ptr [rbp + 0x9c], rax
0x001E8B01: mov qword ptr [rbp + 0xa4], rax
0x001E8B08: mov qword ptr [rbp + 0xac], rax
0x001E8B0F: mov dword ptr [rbp + 0xb4], eax
0x001E8B15: lea rdx, [rbp + 0x70]
0x001E8B19: mov rcx, qword ptr [rdi + 0xd0]
0x001E8B20: call qword ptr [rip + 0x5fef9a]
0x001E8B26: mov dword ptr [rsp + 0x28], eax
0x001E8B2A: test eax, eax
0x001E8B2C: je 0x1401e8d55
0x001E8B32: mov dword ptr [rsp + 0x2c], 0x5b5
0x001E8B3A: mov dword ptr [rbp + 0x40], 0x18
0x001E8B41: mov dword ptr [rbp + 0x44], 0x38
0x001E8B48: mov eax, dword ptr [rbp + 0x44]
0x001E8B4B: xor eax, 0x56
0x001E8B4E: mov byte ptr [rbp + 0x48], al
0x001E8B51: movsx ecx, byte ptr [rbp + 0x48]
0x001E8B55: xor ecx, 0x4e
0x001E8B58: mov byte ptr [rbp + 0x49], cl
0x001E8B5B: movsx ecx, byte ptr [rbp + 0x49]
0x001E8B5F: xor ecx, 0x59
0x001E8B62: mov byte ptr [rbp + 0x4a], cl
0x001E8B65: movsx ecx, byte ptr [rbp + 0x4a]
0x001E8B69: xor ecx, 0x48
```

### reg_9A02A0_field @ `0x001E8B41`

```asm
0x001E8B08: mov qword ptr [rbp + 0xac], rax
0x001E8B0F: mov dword ptr [rbp + 0xb4], eax
0x001E8B15: lea rdx, [rbp + 0x70]
0x001E8B19: mov rcx, qword ptr [rdi + 0xd0]
0x001E8B20: call qword ptr [rip + 0x5fef9a]
0x001E8B26: mov dword ptr [rsp + 0x28], eax
0x001E8B2A: test eax, eax
0x001E8B2C: je 0x1401e8d55
0x001E8B32: mov dword ptr [rsp + 0x2c], 0x5b5
0x001E8B3A: mov dword ptr [rbp + 0x40], 0x18
0x001E8B41: mov dword ptr [rbp + 0x44], 0x38
0x001E8B48: mov eax, dword ptr [rbp + 0x44]
0x001E8B4B: xor eax, 0x56
0x001E8B4E: mov byte ptr [rbp + 0x48], al
0x001E8B51: movsx ecx, byte ptr [rbp + 0x48]
0x001E8B55: xor ecx, 0x4e
0x001E8B58: mov byte ptr [rbp + 0x49], cl
0x001E8B5B: movsx ecx, byte ptr [rbp + 0x49]
0x001E8B5F: xor ecx, 0x59
0x001E8B62: mov byte ptr [rbp + 0x4a], cl
0x001E8B65: movsx ecx, byte ptr [rbp + 0x4a]
0x001E8B69: xor ecx, 0x48
0x001E8B6C: mov byte ptr [rbp + 0x4b], cl
0x001E8B6F: movsx ecx, byte ptr [rbp + 0x4b]
```

### reg_9A0298_field @ `0x001E8E2B`

```asm
0x001E8E0B: xor ecx, 0x74
0x001E8E0E: add ecx, 0xb
0x001E8E11: mov byte ptr [rbp + 0x2a], cl
0x001E8E14: movsx ecx, byte ptr [rbp + 0x2a]
0x001E8E18: xor ecx, 0x20
0x001E8E1B: add ecx, 0xb
0x001E8E1E: mov byte ptr [rbp + 0x2b], cl
0x001E8E21: movsx ecx, byte ptr [rbp + 0x2b]
0x001E8E25: xor ecx, 0x70
0x001E8E28: add ecx, 0xb
0x001E8E2B: mov byte ptr [rbp + 0x2c], cl
0x001E8E2E: movsx ecx, byte ptr [rbp + 0x2c]
0x001E8E32: xor ecx, 0x6f
0x001E8E35: add ecx, 0xb
0x001E8E38: mov byte ptr [rbp + 0x2d], cl
0x001E8E3B: movsx ecx, byte ptr [rbp + 0x2d]
0x001E8E3F: xor ecx, 0x77
0x001E8E42: add ecx, 0xb
0x001E8E45: mov byte ptr [rbp + 0x2e], cl
0x001E8E48: movsx ecx, byte ptr [rbp + 0x2e]
0x001E8E4C: xor ecx, 0x65
0x001E8E4F: add ecx, 0xb
0x001E8E52: mov byte ptr [rbp + 0x2f], cl
0x001E8E55: movsx ecx, byte ptr [rbp + 0x2f]
```

### reg_9A029C_field @ `0x001E8EC7`

```asm
0x001E8EA7: xor ecx, 0x74
0x001E8EAA: add ecx, 0xb
0x001E8EAD: mov byte ptr [rbp + 0x36], cl
0x001E8EB0: movsx ecx, byte ptr [rbp + 0x36]
0x001E8EB4: xor ecx, 0x20
0x001E8EB7: add ecx, 0xb
0x001E8EBA: mov byte ptr [rbp + 0x37], cl
0x001E8EBD: movsx ecx, byte ptr [rbp + 0x37]
0x001E8EC1: xor ecx, 0x74
0x001E8EC4: add ecx, 0xb
0x001E8EC7: mov byte ptr [rbp + 0x38], cl
0x001E8ECA: movsx ecx, byte ptr [rbp + 0x38]
0x001E8ECE: xor ecx, 0x6f
0x001E8ED1: add ecx, 0xb
0x001E8ED4: mov byte ptr [rbp + 0x39], cl
0x001E8ED7: movsx ecx, byte ptr [rbp + 0x39]
0x001E8EDB: xor ecx, 0x20
0x001E8EDE: add ecx, 0xb
0x001E8EE1: mov byte ptr [rbp + 0x3a], cl
0x001E8EE4: movsx ecx, byte ptr [rbp + 0x3a]
0x001E8EE8: xor ecx, 0x7b
0x001E8EEB: add ecx, 0xb
0x001E8EEE: mov byte ptr [rbp + 0x3b], cl
0x001E8EF1: movsx ecx, byte ptr [rbp + 0x3b]
```

### reg_9A029C_field @ `0x001E8F7E`

```asm
0x001E8F62: mov eax, edx
0x001E8F64: shr eax, 0x1f
0x001E8F67: add edx, eax
0x001E8F69: mov dword ptr [rsp + 0x34], edx
0x001E8F6D: mov eax, 0x10624dd3
0x001E8F72: imul ebx
0x001E8F74: sar edx, 6
0x001E8F77: mov eax, edx
0x001E8F79: shr eax, 0x1f
0x001E8F7C: add edx, eax
0x001E8F7E: mov dword ptr [rsp + 0x38], edx
0x001E8F82: mov dword ptr [rbp - 0x70], 0x7b
0x001E8F89: mov dword ptr [rbp - 0x6c], 0x2b
0x001E8F90: mov eax, dword ptr [rbp - 0x6c]
0x001E8F93: mov byte ptr [rbp - 0x68], al
0x001E8F96: movsx ecx, byte ptr [rbp - 0x68]
0x001E8F9A: xor ecx, 6
0x001E8F9D: mov byte ptr [rbp - 0x67], cl
0x001E8FA0: movsx ecx, byte ptr [rbp - 0x67]
0x001E8FA4: xor ecx, 0x41
0x001E8FA7: mov byte ptr [rbp - 0x66], cl
0x001E8FAA: movsx ecx, byte ptr [rbp - 0x66]
0x001E8FAE: xor ecx, 0x5b
0x001E8FB1: mov byte ptr [rbp - 0x65], cl
```

### reg_9A0290_field @ `0x001E93ED`

```asm
0x001E93CC: xor ecx, 0x16
0x001E93CF: mov byte ptr [rbp + 5], cl
0x001E93D2: movsx ecx, byte ptr [rbp + 5]
0x001E93D6: xor ecx, 0x1a
0x001E93D9: mov byte ptr [rbp + 6], cl
0x001E93DC: movsx ecx, byte ptr [rbp + 6]
0x001E93E0: xor ecx, 0x12
0x001E93E3: mov byte ptr [rbp + 7], cl
0x001E93E6: movsx ecx, byte ptr [rbp + 7]
0x001E93EA: xor ecx, 0x15
0x001E93ED: mov byte ptr [rbp + 8], cl
0x001E93F0: movsx ecx, byte ptr [rbp + 8]
0x001E93F4: xor ecx, 8
0x001E93F7: mov byte ptr [rbp + 9], cl
0x001E93FA: movsx ecx, byte ptr [rbp + 9]
0x001E93FE: xor ecx, 0x5b
0x001E9401: mov byte ptr [rbp + 0xa], cl
0x001E9404: movsx ecx, byte ptr [rbp + 0xa]
0x001E9408: xor ecx, 0x12
0x001E940B: mov byte ptr [rbp + 0xb], cl
0x001E940E: movsx ecx, byte ptr [rbp + 0xb]
0x001E9412: xor ecx, 0x15
0x001E9415: mov byte ptr [rbp + 0xc], cl
0x001E9418: movsx ecx, byte ptr [rbp + 0xc]
```

### reg_9A02A0_field @ `0x001E9CD9`

```asm
0x001E9C91: mov qword ptr [rbp + 0xc0], rax
0x001E9C98: mov qword ptr [rbp + 0xc8], rax
0x001E9C9F: mov qword ptr [rbp + 0xd0], rax
0x001E9CA6: mov qword ptr [rbp + 0xd8], rax
0x001E9CAD: mov qword ptr [rbp + 0xe0], rax
0x001E9CB4: mov qword ptr [rbp + 0xe8], rax
0x001E9CBB: mov dword ptr [rbp + 0xb8], 0x20038
0x001E9CC5: lea rdx, [rbp + 0xb8]
0x001E9CCC: mov rcx, qword ptr [rdi + 0xd0]
0x001E9CD3: call qword ptr [rip + 0x5fdd7f]
0x001E9CD9: mov dword ptr [rsp + 0x44], eax
0x001E9CDD: test eax, eax
0x001E9CDF: je 0x1401e9ff5
0x001E9CE5: mov dword ptr [rsp + 0x48], 0x528
0x001E9CED: mov dword ptr [rbp + 0x88], 0x1c
0x001E9CF7: mov dword ptr [rbp + 0x8c], 0x63
0x001E9D01: mov eax, dword ptr [rbp + 0x8c]
0x001E9D07: xor eax, 0x52
0x001E9D0A: mov byte ptr [rbp + 0x90], al
0x001E9D10: movsx ecx, byte ptr [rbp + 0x90]
0x001E9D17: xor ecx, 0x4a
0x001E9D1A: mov byte ptr [rbp + 0x91], cl
0x001E9D20: movsx ecx, byte ptr [rbp + 0x91]
0x001E9D27: xor ecx, 0x5d
```

### reg_9A029C_field @ `0x001EA092`

```asm
0x001EA072: xor ecx, 0x3a
0x001EA075: add ecx, 7
0x001EA078: mov byte ptr [rbp + 0x36], cl
0x001EA07B: movsx ecx, byte ptr [rbp + 0x36]
0x001EA07F: xor ecx, 0x20
0x001EA082: add ecx, 7
0x001EA085: mov byte ptr [rbp + 0x37], cl
0x001EA088: movsx ecx, byte ptr [rbp + 0x37]
0x001EA08C: xor ecx, 0x53
0x001EA08F: add ecx, 7
0x001EA092: mov byte ptr [rbp + 0x38], cl
0x001EA095: movsx ecx, byte ptr [rbp + 0x38]
0x001EA099: xor ecx, 0x65
0x001EA09C: add ecx, 7
0x001EA09F: mov byte ptr [rbp + 0x39], cl
0x001EA0A2: movsx ecx, byte ptr [rbp + 0x39]
0x001EA0A6: xor ecx, 0x74
0x001EA0A9: add ecx, 7
0x001EA0AC: mov byte ptr [rbp + 0x3a], cl
0x001EA0AF: movsx ecx, byte ptr [rbp + 0x3a]
0x001EA0B3: xor ecx, 0x20
0x001EA0B6: add ecx, 7
0x001EA0B9: mov byte ptr [rbp + 0x3b], cl
0x001EA0BC: movsx ecx, byte ptr [rbp + 0x3b]
```

### reg_9A02A0_field @ `0x001EA12E`

```asm
0x001EA10E: xor ecx, 0x6c
0x001EA111: add ecx, 7
0x001EA114: mov byte ptr [rbp + 0x42], cl
0x001EA117: movsx ecx, byte ptr [rbp + 0x42]
0x001EA11B: xor ecx, 0x20
0x001EA11E: add ecx, 7
0x001EA121: mov byte ptr [rbp + 0x43], cl
0x001EA124: movsx ecx, byte ptr [rbp + 0x43]
0x001EA128: xor ecx, 0x6c
0x001EA12B: add ecx, 7
0x001EA12E: mov byte ptr [rbp + 0x44], cl
0x001EA131: movsx ecx, byte ptr [rbp + 0x44]
0x001EA135: xor ecx, 0x69
0x001EA138: add ecx, 7
0x001EA13B: mov byte ptr [rbp + 0x45], cl
0x001EA13E: movsx ecx, byte ptr [rbp + 0x45]
0x001EA142: xor ecx, 0x6d
0x001EA145: add ecx, 7
0x001EA148: mov byte ptr [rbp + 0x46], cl
0x001EA14B: movsx ecx, byte ptr [rbp + 0x46]
0x001EA14F: xor ecx, 0x69
0x001EA152: add ecx, 7
0x001EA155: mov byte ptr [rbp + 0x47], cl
0x001EA158: movsx ecx, byte ptr [rbp + 0x47]
```

### reg_9A0290_field @ `0x001EAC80`

```asm
0x001EAC5F: xor ecx, 0x61
0x001EAC62: mov byte ptr [rbp + 5], cl
0x001EAC65: movsx ecx, byte ptr [rbp + 5]
0x001EAC69: xor ecx, 0x32
0x001EAC6C: mov byte ptr [rbp + 6], cl
0x001EAC6F: movsx ecx, byte ptr [rbp + 6]
0x001EAC73: xor ecx, 0x24
0x001EAC76: mov byte ptr [rbp + 7], cl
0x001EAC79: movsx ecx, byte ptr [rbp + 7]
0x001EAC7D: xor ecx, 0x35
0x001EAC80: mov byte ptr [rbp + 8], cl
0x001EAC83: movsx ecx, byte ptr [rbp + 8]
0x001EAC87: xor ecx, 0x61
0x001EAC8A: mov byte ptr [rbp + 9], cl
0x001EAC8D: movsx ecx, byte ptr [rbp + 9]
0x001EAC91: xor ecx, 0x35
0x001EAC94: mov byte ptr [rbp + 0xa], cl
0x001EAC97: movsx ecx, byte ptr [rbp + 0xa]
0x001EAC9B: xor ecx, 0x29
0x001EAC9E: mov byte ptr [rbp + 0xb], cl
0x001EACA1: movsx ecx, byte ptr [rbp + 0xb]
0x001EACA5: xor ecx, 0x24
0x001EACA8: mov byte ptr [rbp + 0xc], cl
0x001EACAB: movsx ecx, byte ptr [rbp + 0xc]
```

### reg_9A0298_field @ `0x001EADE8`

```asm
0x001EADC7: xor ecx, 0x33
0x001EADCA: mov byte ptr [rbp + 0x29], cl
0x001EADCD: movsx ecx, byte ptr [rbp + 0x29]
0x001EADD1: xor ecx, 0x61
0x001EADD4: mov byte ptr [rbp + 0x2a], cl
0x001EADD7: movsx ecx, byte ptr [rbp + 0x2a]
0x001EADDB: xor ecx, 0x3a
0x001EADDE: mov byte ptr [rbp + 0x2b], cl
0x001EADE1: movsx ecx, byte ptr [rbp + 0x2b]
0x001EADE5: xor ecx, 0x3c
0x001EADE8: mov byte ptr [rbp + 0x2c], cl
0x001EADEB: xor eax, eax
0x001EADED: mov byte ptr [rbp + 0x2d], al
0x001EADF0: movzx eax, byte ptr [rbp - 8]
0x001EADF4: lea rdx, [rbp + 0x1e0]
0x001EADFB: lea rcx, [rbp - 0x10]
0x001EADFF: call 0x14026ecb0
0x001EAE04: nop
0x001EAE05: cmp qword ptr [rax + 0x18], 0x10
0x001EAE0A: jb 0x1401eae0f
0x001EAE0C: mov rax, qword ptr [rax]
0x001EAE0F: lea rdx, [rdi + 8]
0x001EAE13: lea r9, [rsp + 0x20]
0x001EAE18: lea r8, [rsp + 0x34]
```

### reg_9A0290_field @ `0x001EAF82`

```asm
0x001EAF67: mov eax, dword ptr [rbp - 9]
0x001EAF6A: add al, 8
0x001EAF6C: xor eax, ecx
0x001EAF6E: xor eax, 0x72
0x001EAF71: mov byte ptr [rbp + 7], al
0x001EAF74: movsx ecx, byte ptr [rbp + 7]
0x001EAF78: mov eax, dword ptr [rbp - 9]
0x001EAF7B: add al, 9
0x001EAF7D: xor eax, ecx
0x001EAF7F: xor eax, 0x6f
0x001EAF82: mov byte ptr [rbp + 8], al
0x001EAF85: movsx ecx, byte ptr [rbp + 8]
0x001EAF89: mov eax, dword ptr [rbp - 9]
0x001EAF8C: add al, 0xa
0x001EAF8E: xor eax, ecx
0x001EAF90: xor eax, 0x72
0x001EAF93: mov byte ptr [rbp + 9], al
0x001EAF96: movsx ecx, byte ptr [rbp + 9]
0x001EAF9A: mov eax, dword ptr [rbp - 9]
0x001EAF9D: add al, 0xb
0x001EAF9F: xor eax, ecx
0x001EAFA1: xor eax, 0x20
0x001EAFA4: mov byte ptr [rbp + 0xa], al
0x001EAFA7: movsx ecx, byte ptr [rbp + 0xa]
```

### reg_9A0298_field @ `0x001EB23B`

```asm
0x001EB20F: int3
0x001EB210: push rbx
0x001EB212: sub rsp, 0xd0
0x001EB219: mov rax, qword ptr [rip + 0x5eb6d0]
0x001EB220: xor rax, rsp
0x001EB223: mov qword ptr [rsp + 0xc0], rax
0x001EB22B: xor r11d, r11d
0x001EB22E: mov rbx, rdx
0x001EB231: mov qword ptr [rsp + 0x20], r11
0x001EB236: mov rax, qword ptr [rsp + 0x20]
0x001EB23B: mov dword ptr [rsp + 0x2c], r11d
0x001EB240: cmp rax, 0x82
0x001EB246: jae 0x1401eb2a5
0x001EB248: nop dword ptr [rax + rax]
0x001EB250: mov rax, qword ptr [rsp + 0x20]
0x001EB255: test rax, rax
0x001EB258: jne 0x1401eb260
0x001EB25A: mov r10d, dword ptr [rcx + 4]
0x001EB25E: jmp 0x1401eb26b
0x001EB260: mov rax, qword ptr [rsp + 0x20]
0x001EB265: movsx r10d, byte ptr [rax + rcx + 7]
0x001EB26B: mov rdx, qword ptr [rsp + 0x20]
0x001EB270: mov rax, qword ptr [rsp + 0x20]
0x001EB275: movsx r8d, byte ptr [rax + rcx + 8]
```

### reg_9A0298_field @ `0x001EB325`

```asm
0x001EB2FF: int3
0x001EB300: push rbx
0x001EB302: sub rsp, 0x70
0x001EB306: mov rax, qword ptr [rip + 0x5eb5e3]
0x001EB30D: xor rax, rsp
0x001EB310: mov qword ptr [rsp + 0x68], rax
0x001EB315: xor r10d, r10d
0x001EB318: mov rbx, rdx
0x001EB31B: mov qword ptr [rsp + 0x20], r10
0x001EB320: mov rax, qword ptr [rsp + 0x20]
0x001EB325: mov dword ptr [rsp + 0x2c], r10d
0x001EB32A: cmp rax, 0x36
0x001EB32E: jae 0x1401eb381
0x001EB330: mov rax, qword ptr [rsp + 0x20]
0x001EB335: test rax, rax
0x001EB338: jne 0x1401eb340
0x001EB33A: mov r9d, dword ptr [rcx + 4]
0x001EB33E: jmp 0x1401eb34b
0x001EB340: mov rax, qword ptr [rsp + 0x20]
0x001EB345: movsx r9d, byte ptr [rax + rcx + 7]
0x001EB34B: mov rdx, qword ptr [rsp + 0x20]
0x001EB350: mov rax, qword ptr [rsp + 0x20]
0x001EB355: movsx r8d, byte ptr [rax + rcx + 8]
0x001EB35B: mov eax, dword ptr [rcx]
```

### reg_9A0298_field @ `0x001EB3F5`

```asm
0x001EB3CF: int3
0x001EB3D0: push rbx
0x001EB3D2: sub rsp, 0x60
0x001EB3D6: mov rax, qword ptr [rip + 0x5eb513]
0x001EB3DD: xor rax, rsp
0x001EB3E0: mov qword ptr [rsp + 0x58], rax
0x001EB3E5: xor r10d, r10d
0x001EB3E8: mov rbx, rdx
0x001EB3EB: mov qword ptr [rsp + 0x20], r10
0x001EB3F0: mov rax, qword ptr [rsp + 0x20]
0x001EB3F5: mov dword ptr [rsp + 0x2c], r10d
0x001EB3FA: cmp rax, 0x21
0x001EB3FE: jae 0x1401eb451
0x001EB400: mov rax, qword ptr [rsp + 0x20]
0x001EB405: test rax, rax
0x001EB408: jne 0x1401eb410
0x001EB40A: mov r9d, dword ptr [rcx + 4]
0x001EB40E: jmp 0x1401eb41b
0x001EB410: mov rax, qword ptr [rsp + 0x20]
0x001EB415: movsx r9d, byte ptr [rax + rcx + 7]
0x001EB41B: mov rdx, qword ptr [rsp + 0x20]
0x001EB420: mov rax, qword ptr [rsp + 0x20]
0x001EB425: movsx r8d, byte ptr [rax + rcx + 8]
0x001EB42B: mov eax, dword ptr [rcx]
```

### reg_9A0298_field @ `0x001EB4CB`

```asm
0x001EB49F: int3
0x001EB4A0: push rbx
0x001EB4A2: sub rsp, 0xb0
0x001EB4A9: mov rax, qword ptr [rip + 0x5eb440]
0x001EB4B0: xor rax, rsp
0x001EB4B3: mov qword ptr [rsp + 0xa0], rax
0x001EB4BB: xor r10d, r10d
0x001EB4BE: mov rbx, rdx
0x001EB4C1: mov qword ptr [rsp + 0x20], r10
0x001EB4C6: mov rax, qword ptr [rsp + 0x20]
0x001EB4CB: mov dword ptr [rsp + 0x2c], r10d
0x001EB4D0: cmp rax, 0x62
0x001EB4D4: jae 0x1401eb527
0x001EB4D6: mov rax, qword ptr [rsp + 0x20]
0x001EB4DB: test rax, rax
0x001EB4DE: jne 0x1401eb4e6
0x001EB4E0: mov r9d, dword ptr [rcx + 4]
0x001EB4E4: jmp 0x1401eb4f1
0x001EB4E6: mov rax, qword ptr [rsp + 0x20]
0x001EB4EB: movsx r9d, byte ptr [rax + rcx + 7]
0x001EB4F1: mov rdx, qword ptr [rsp + 0x20]
0x001EB4F6: mov rax, qword ptr [rsp + 0x20]
0x001EB4FB: movsx r8d, byte ptr [rax + rcx + 8]
0x001EB501: mov eax, dword ptr [rcx]
```

### reg_9A0298_field @ `0x001EB5A8`

```asm
0x001EB57F: int3
0x001EB580: push rbx
0x001EB582: sub rsp, 0x80
0x001EB589: mov rax, qword ptr [rip + 0x5eb360]
0x001EB590: xor rax, rsp
0x001EB593: mov qword ptr [rsp + 0x70], rax
0x001EB598: xor r10d, r10d
0x001EB59B: mov rbx, rdx
0x001EB59E: mov qword ptr [rsp + 0x20], r10
0x001EB5A3: mov rax, qword ptr [rsp + 0x20]
0x001EB5A8: mov dword ptr [rsp + 0x2c], r10d
0x001EB5AD: cmp rax, 0x3f
0x001EB5B1: jae 0x1401eb604
0x001EB5B3: mov rax, qword ptr [rsp + 0x20]
0x001EB5B8: test rax, rax
0x001EB5BB: jne 0x1401eb5c3
0x001EB5BD: mov r9d, dword ptr [rcx + 4]
0x001EB5C1: jmp 0x1401eb5ce
0x001EB5C3: mov rax, qword ptr [rsp + 0x20]
0x001EB5C8: movsx r9d, byte ptr [rax + rcx + 7]
0x001EB5CE: mov rdx, qword ptr [rsp + 0x20]
0x001EB5D3: mov rax, qword ptr [rsp + 0x20]
0x001EB5D8: movsx r8d, byte ptr [rax + rcx + 8]
0x001EB5DE: mov eax, dword ptr [rcx]
```

### reg_9A0298_field @ `0x001EB685`

```asm
0x001EB65F: int3
0x001EB660: push rbx
0x001EB662: sub rsp, 0x70
0x001EB666: mov rax, qword ptr [rip + 0x5eb283]
0x001EB66D: xor rax, rsp
0x001EB670: mov qword ptr [rsp + 0x60], rax
0x001EB675: xor r10d, r10d
0x001EB678: mov rbx, rdx
0x001EB67B: mov qword ptr [rsp + 0x20], r10
0x001EB680: mov rax, qword ptr [rsp + 0x20]
0x001EB685: mov dword ptr [rsp + 0x2c], r10d
0x001EB68A: cmp rax, 0x2b
0x001EB68E: jae 0x1401eb6e1
0x001EB690: mov rax, qword ptr [rsp + 0x20]
0x001EB695: test rax, rax
0x001EB698: jne 0x1401eb6a0
0x001EB69A: mov r9d, dword ptr [rcx + 4]
0x001EB69E: jmp 0x1401eb6ab
0x001EB6A0: mov rax, qword ptr [rsp + 0x20]
0x001EB6A5: movsx r9d, byte ptr [rax + rcx + 7]
0x001EB6AB: mov rdx, qword ptr [rsp + 0x20]
0x001EB6B0: mov rax, qword ptr [rsp + 0x20]
0x001EB6B5: movsx r8d, byte ptr [rax + rcx + 8]
0x001EB6BB: mov eax, dword ptr [rcx]
```

### reg_9A0298_field @ `0x001EB755`

```asm
0x001EB72F: int3
0x001EB730: push rbx
0x001EB732: sub rsp, 0x70
0x001EB736: mov rax, qword ptr [rip + 0x5eb1b3]
0x001EB73D: xor rax, rsp
0x001EB740: mov qword ptr [rsp + 0x68], rax
0x001EB745: xor r10d, r10d
0x001EB748: mov rbx, rdx
0x001EB74B: mov qword ptr [rsp + 0x20], r10
0x001EB750: mov rax, qword ptr [rsp + 0x20]
0x001EB755: mov dword ptr [rsp + 0x2c], r10d
0x001EB75A: cmp rax, 0x31
0x001EB75E: jae 0x1401eb7b1
0x001EB760: mov rax, qword ptr [rsp + 0x20]
0x001EB765: test rax, rax
0x001EB768: jne 0x1401eb770
0x001EB76A: mov r9d, dword ptr [rcx + 4]
0x001EB76E: jmp 0x1401eb77b
0x001EB770: mov rax, qword ptr [rsp + 0x20]
0x001EB775: movsx r9d, byte ptr [rax + rcx + 7]
0x001EB77B: mov rdx, qword ptr [rsp + 0x20]
0x001EB780: mov rax, qword ptr [rsp + 0x20]
0x001EB785: movsx r8d, byte ptr [rax + rcx + 8]
0x001EB78B: mov eax, dword ptr [rcx]
```

### reg_9A0298_field @ `0x001EB825`

```asm
0x001EB7FF: int3
0x001EB800: push rbx
0x001EB802: sub rsp, 0x50
0x001EB806: mov rax, qword ptr [rip + 0x5eb0e3]
0x001EB80D: xor rax, rsp
0x001EB810: mov qword ptr [rsp + 0x40], rax
0x001EB815: xor r10d, r10d
0x001EB818: mov rbx, rdx
0x001EB81B: mov qword ptr [rsp + 0x20], r10
0x001EB820: mov rax, qword ptr [rsp + 0x20]
0x001EB825: mov dword ptr [rsp + 0x2c], r10d
0x001EB82A: cmp rax, 0x10
0x001EB82E: jae 0x1401eb872
0x001EB830: mov rax, qword ptr [rsp + 0x20]
0x001EB835: test rax, rax
0x001EB838: jne 0x1401eb83f
0x001EB83A: mov r9d, dword ptr [rcx]
0x001EB83D: jmp 0x1401eb84a
0x001EB83F: mov rax, qword ptr [rsp + 0x20]
0x001EB844: movsx r9d, byte ptr [rax + rcx + 3]
0x001EB84A: mov rax, qword ptr [rsp + 0x20]
0x001EB84F: movsx edx, byte ptr [rax + rcx + 4]
0x001EB854: mov rax, qword ptr [rsp + 0x20]
0x001EB859: dec edx
```

### reg_9A0298_field @ `0x001EB8E5`

```asm
0x001EB8BF: int3
0x001EB8C0: push rbx
0x001EB8C2: sub rsp, 0x70
0x001EB8C6: mov rax, qword ptr [rip + 0x5eb023]
0x001EB8CD: xor rax, rsp
0x001EB8D0: mov qword ptr [rsp + 0x68], rax
0x001EB8D5: xor r10d, r10d
0x001EB8D8: mov rbx, rdx
0x001EB8DB: mov qword ptr [rsp + 0x20], r10
0x001EB8E0: mov rax, qword ptr [rsp + 0x20]
0x001EB8E5: mov dword ptr [rsp + 0x2c], r10d
0x001EB8EA: cmp rax, 0x34
0x001EB8EE: jae 0x1401eb933
0x001EB8F0: mov rax, qword ptr [rsp + 0x20]
0x001EB8F5: test rax, rax
0x001EB8F8: jne 0x1401eb8ff
0x001EB8FA: mov r9d, dword ptr [rcx]
0x001EB8FD: jmp 0x1401eb90a
0x001EB8FF: mov rax, qword ptr [rsp + 0x20]
0x001EB904: movsx r9d, byte ptr [rax + rcx + 3]
0x001EB90A: mov rax, qword ptr [rsp + 0x20]
0x001EB90F: movsx edx, byte ptr [rax + rcx + 4]
0x001EB914: mov rax, qword ptr [rsp + 0x20]
0x001EB919: sub edx, 5
```

### reg_9A0298_field @ `0x001EB9A5`

```asm
0x001EB97F: int3
0x001EB980: push rbx
0x001EB982: sub rsp, 0x50
0x001EB986: mov rax, qword ptr [rip + 0x5eaf63]
0x001EB98D: xor rax, rsp
0x001EB990: mov qword ptr [rsp + 0x48], rax
0x001EB995: xor r10d, r10d
0x001EB998: mov rbx, rdx
0x001EB99B: mov qword ptr [rsp + 0x20], r10
0x001EB9A0: mov rax, qword ptr [rsp + 0x20]
0x001EB9A5: mov dword ptr [rsp + 0x2c], r10d
0x001EB9AA: cmp rax, 0x18
0x001EB9AE: jae 0x1401eb9f3
0x001EB9B0: mov rax, qword ptr [rsp + 0x20]
0x001EB9B5: test rax, rax
0x001EB9B8: jne 0x1401eb9bf
0x001EB9BA: mov r9d, dword ptr [rcx]
0x001EB9BD: jmp 0x1401eb9ca
0x001EB9BF: mov rax, qword ptr [rsp + 0x20]
0x001EB9C4: movsx r9d, byte ptr [rax + rcx + 3]
0x001EB9CA: mov rax, qword ptr [rsp + 0x20]
0x001EB9CF: movsx edx, byte ptr [rax + rcx + 4]
0x001EB9D4: mov rax, qword ptr [rsp + 0x20]
0x001EB9D9: sub edx, 9
```

### reg_9A0298_field @ `0x001EBA65`

```asm
0x001EBA3F: int3
0x001EBA40: push rbx
0x001EBA42: sub rsp, 0x60
0x001EBA46: mov rax, qword ptr [rip + 0x5eaea3]
0x001EBA4D: xor rax, rsp
0x001EBA50: mov qword ptr [rsp + 0x58], rax
0x001EBA55: xor r10d, r10d
0x001EBA58: mov rbx, rdx
0x001EBA5B: mov qword ptr [rsp + 0x20], r10
0x001EBA60: mov rax, qword ptr [rsp + 0x20]
0x001EBA65: mov dword ptr [rsp + 0x2c], r10d
0x001EBA6A: cmp rax, 0x25
0x001EBA6E: jae 0x1401ebab3
0x001EBA70: mov rax, qword ptr [rsp + 0x20]
0x001EBA75: test rax, rax
0x001EBA78: jne 0x1401eba7f
0x001EBA7A: mov r9d, dword ptr [rcx]
0x001EBA7D: jmp 0x1401eba8a
0x001EBA7F: mov rax, qword ptr [rsp + 0x20]
0x001EBA84: movsx r9d, byte ptr [rax + rcx + 3]
0x001EBA8A: mov rax, qword ptr [rsp + 0x20]
0x001EBA8F: movsx edx, byte ptr [rax + rcx + 4]
0x001EBA94: mov rax, qword ptr [rsp + 0x20]
0x001EBA99: sub edx, 0xa
```

### reg_9A0298_field @ `0x001EBB25`

```asm
0x001EBAFF: int3
0x001EBB00: push rbx
0x001EBB02: sub rsp, 0x60
0x001EBB06: mov rax, qword ptr [rip + 0x5eade3]
0x001EBB0D: xor rax, rsp
0x001EBB10: mov qword ptr [rsp + 0x50], rax
0x001EBB15: xor r10d, r10d
0x001EBB18: mov rbx, rdx
0x001EBB1B: mov qword ptr [rsp + 0x20], r10
0x001EBB20: mov rax, qword ptr [rsp + 0x20]
0x001EBB25: mov dword ptr [rsp + 0x2c], r10d
0x001EBB2A: cmp rax, 0x1e
0x001EBB2E: jae 0x1401ebb73
0x001EBB30: mov rax, qword ptr [rsp + 0x20]
0x001EBB35: test rax, rax
0x001EBB38: jne 0x1401ebb3f
0x001EBB3A: mov r9d, dword ptr [rcx]
0x001EBB3D: jmp 0x1401ebb4a
0x001EBB3F: mov rax, qword ptr [rsp + 0x20]
0x001EBB44: movsx r9d, byte ptr [rax + rcx + 3]
0x001EBB4A: mov rax, qword ptr [rsp + 0x20]
0x001EBB4F: movsx edx, byte ptr [rax + rcx + 4]
0x001EBB54: mov rax, qword ptr [rsp + 0x20]
0x001EBB59: sub edx, 0xa
```

### reg_9A0298_field @ `0x001EBBE5`

```asm
0x001EBBBF: int3
0x001EBBC0: push rbx
0x001EBBC2: sub rsp, 0x70
0x001EBBC6: mov rax, qword ptr [rip + 0x5ead23]
0x001EBBCD: xor rax, rsp
0x001EBBD0: mov qword ptr [rsp + 0x68], rax
0x001EBBD5: xor r10d, r10d
0x001EBBD8: mov rbx, rdx
0x001EBBDB: mov qword ptr [rsp + 0x20], r10
0x001EBBE0: mov rax, qword ptr [rsp + 0x20]
0x001EBBE5: mov dword ptr [rsp + 0x2c], r10d
0x001EBBEA: cmp rax, 0x33
0x001EBBEE: jae 0x1401ebc33
0x001EBBF0: mov rax, qword ptr [rsp + 0x20]
0x001EBBF5: test rax, rax
0x001EBBF8: jne 0x1401ebbff
0x001EBBFA: mov r9d, dword ptr [rcx]
0x001EBBFD: jmp 0x1401ebc0a
0x001EBBFF: mov rax, qword ptr [rsp + 0x20]
0x001EBC04: movsx r9d, byte ptr [rax + rcx + 3]
0x001EBC0A: mov rax, qword ptr [rsp + 0x20]
0x001EBC0F: movsx edx, byte ptr [rax + rcx + 4]
0x001EBC14: mov rax, qword ptr [rsp + 0x20]
0x001EBC19: sub edx, 2
```

### reg_9A0298_field @ `0x001EBCA5`

```asm
0x001EBC7F: int3
0x001EBC80: push rbx
0x001EBC82: sub rsp, 0x60
0x001EBC86: mov rax, qword ptr [rip + 0x5eac63]
0x001EBC8D: xor rax, rsp
0x001EBC90: mov qword ptr [rsp + 0x58], rax
0x001EBC95: xor r10d, r10d
0x001EBC98: mov rbx, rdx
0x001EBC9B: mov qword ptr [rsp + 0x20], r10
0x001EBCA0: mov rax, qword ptr [rsp + 0x20]
0x001EBCA5: mov dword ptr [rsp + 0x2c], r10d
0x001EBCAA: cmp rax, 0x25
0x001EBCAE: jae 0x1401ebcf2
0x001EBCB0: mov rax, qword ptr [rsp + 0x20]
0x001EBCB5: test rax, rax
0x001EBCB8: jne 0x1401ebcbf
0x001EBCBA: mov r9d, dword ptr [rcx]
0x001EBCBD: jmp 0x1401ebcca
0x001EBCBF: mov rax, qword ptr [rsp + 0x20]
0x001EBCC4: movsx r9d, byte ptr [rax + rcx + 3]
0x001EBCCA: mov rax, qword ptr [rsp + 0x20]
0x001EBCCF: movsx edx, byte ptr [rax + rcx + 4]
0x001EBCD4: mov rax, qword ptr [rsp + 0x20]
0x001EBCD9: dec edx
```

### reg_9A0298_field @ `0x001EBD65`

```asm
0x001EBD3F: int3
0x001EBD40: push rbx
0x001EBD42: sub rsp, 0x60
0x001EBD46: mov rax, qword ptr [rip + 0x5eaba3]
0x001EBD4D: xor rax, rsp
0x001EBD50: mov qword ptr [rsp + 0x50], rax
0x001EBD55: xor r10d, r10d
0x001EBD58: mov rbx, rdx
0x001EBD5B: mov qword ptr [rsp + 0x20], r10
0x001EBD60: mov rax, qword ptr [rsp + 0x20]
0x001EBD65: mov dword ptr [rsp + 0x2c], r10d
0x001EBD6A: cmp rax, 0x19
0x001EBD6E: jae 0x1401ebdb3
0x001EBD70: mov rax, qword ptr [rsp + 0x20]
0x001EBD75: test rax, rax
0x001EBD78: jne 0x1401ebd7f
0x001EBD7A: mov r9d, dword ptr [rcx]
0x001EBD7D: jmp 0x1401ebd8a
0x001EBD7F: mov rax, qword ptr [rsp + 0x20]
0x001EBD84: movsx r9d, byte ptr [rax + rcx + 3]
0x001EBD8A: mov rax, qword ptr [rsp + 0x20]
0x001EBD8F: movsx edx, byte ptr [rax + rcx + 4]
0x001EBD94: mov rax, qword ptr [rsp + 0x20]
0x001EBD99: sub edx, 3
```

### reg_9A0298_field @ `0x001EBE25`

```asm
0x001EBDFF: int3
0x001EBE00: push rbx
0x001EBE02: sub rsp, 0x60
0x001EBE06: mov rax, qword ptr [rip + 0x5eaae3]
0x001EBE0D: xor rax, rsp
0x001EBE10: mov qword ptr [rsp + 0x50], rax
0x001EBE15: xor r10d, r10d
0x001EBE18: mov rbx, rdx
0x001EBE1B: mov qword ptr [rsp + 0x20], r10
0x001EBE20: mov rax, qword ptr [rsp + 0x20]
0x001EBE25: mov dword ptr [rsp + 0x2c], r10d
0x001EBE2A: cmp rax, 0x1f
0x001EBE2E: jae 0x1401ebe72
0x001EBE30: mov rax, qword ptr [rsp + 0x20]
0x001EBE35: test rax, rax
0x001EBE38: jne 0x1401ebe3f
0x001EBE3A: mov r9d, dword ptr [rcx]
0x001EBE3D: jmp 0x1401ebe4a
0x001EBE3F: mov rax, qword ptr [rsp + 0x20]
0x001EBE44: movsx r9d, byte ptr [rax + rcx + 3]
0x001EBE4A: mov rax, qword ptr [rsp + 0x20]
0x001EBE4F: movsx edx, byte ptr [rax + rcx + 4]
0x001EBE54: mov rax, qword ptr [rsp + 0x20]
0x001EBE59: dec edx
```

### reg_9A0298_field @ `0x001EBEEB`

```asm
0x001EBEBF: int3
0x001EBEC0: push rbx
0x001EBEC2: sub rsp, 0xd0
0x001EBEC9: mov rax, qword ptr [rip + 0x5eaa20]
0x001EBED0: xor rax, rsp
0x001EBED3: mov qword ptr [rsp + 0xc0], rax
0x001EBEDB: xor r10d, r10d
0x001EBEDE: mov rbx, rdx
0x001EBEE1: mov qword ptr [rsp + 0x20], r10
0x001EBEE6: mov rax, qword ptr [rsp + 0x20]
0x001EBEEB: mov dword ptr [rsp + 0x2c], r10d
0x001EBEF0: cmp rax, 0x84
0x001EBEF6: jae 0x1401ebf47
0x001EBEF8: nop dword ptr [rax + rax]
0x001EBF00: mov rax, qword ptr [rsp + 0x20]
0x001EBF05: test rax, rax
0x001EBF08: jne 0x1401ebf0f
0x001EBF0A: mov r9d, dword ptr [rcx]
0x001EBF0D: jmp 0x1401ebf1a
0x001EBF0F: mov rax, qword ptr [rsp + 0x20]
0x001EBF14: movsx r9d, byte ptr [rax + rcx + 3]
0x001EBF1A: mov rax, qword ptr [rsp + 0x20]
0x001EBF1F: movsx r8d, byte ptr [rax + rcx + 4]
0x001EBF25: mov rax, qword ptr [rsp + 0x20]
```

### reg_9A0298_field @ `0x001EBFC5`

```asm
0x001EBF9F: int3
0x001EBFA0: push rbx
0x001EBFA2: sub rsp, 0x50
0x001EBFA6: mov rax, qword ptr [rip + 0x5ea943]
0x001EBFAD: xor rax, rsp
0x001EBFB0: mov qword ptr [rsp + 0x48], rax
0x001EBFB5: xor r10d, r10d
0x001EBFB8: mov rbx, rdx
0x001EBFBB: mov qword ptr [rsp + 0x20], r10
0x001EBFC0: mov rax, qword ptr [rsp + 0x20]
0x001EBFC5: mov dword ptr [rsp + 0x2c], r10d
0x001EBFCA: cmp rax, 0x18
0x001EBFCE: jae 0x1401ec013
0x001EBFD0: mov rax, qword ptr [rsp + 0x20]
0x001EBFD5: test rax, rax
0x001EBFD8: jne 0x1401ebfdf
0x001EBFDA: mov r9d, dword ptr [rcx]
0x001EBFDD: jmp 0x1401ebfea
0x001EBFDF: mov rax, qword ptr [rsp + 0x20]
0x001EBFE4: movsx r9d, byte ptr [rax + rcx + 3]
0x001EBFEA: mov rax, qword ptr [rsp + 0x20]
0x001EBFEF: movsx edx, byte ptr [rax + rcx + 4]
0x001EBFF4: mov rax, qword ptr [rsp + 0x20]
0x001EBFF9: sub edx, 4
```

### reg_9A0298_field @ `0x001EC085`

```asm
0x001EC05F: int3
0x001EC060: push rbx
0x001EC062: sub rsp, 0x60
0x001EC066: mov rax, qword ptr [rip + 0x5ea883]
0x001EC06D: xor rax, rsp
0x001EC070: mov qword ptr [rsp + 0x58], rax
0x001EC075: xor r10d, r10d
0x001EC078: mov rbx, rdx
0x001EC07B: mov qword ptr [rsp + 0x20], r10
0x001EC080: mov rax, qword ptr [rsp + 0x20]
0x001EC085: mov dword ptr [rsp + 0x2c], r10d
0x001EC08A: cmp rax, 0x25
0x001EC08E: jae 0x1401ec0d3
0x001EC090: mov rax, qword ptr [rsp + 0x20]
0x001EC095: test rax, rax
0x001EC098: jne 0x1401ec09f
0x001EC09A: mov r9d, dword ptr [rcx]
0x001EC09D: jmp 0x1401ec0aa
0x001EC09F: mov rax, qword ptr [rsp + 0x20]
0x001EC0A4: movsx r9d, byte ptr [rax + rcx + 3]
0x001EC0AA: mov rax, qword ptr [rsp + 0x20]
0x001EC0AF: movsx edx, byte ptr [rax + rcx + 4]
0x001EC0B4: mov rax, qword ptr [rsp + 0x20]
0x001EC0B9: sub edx, 4
```

### reg_9A0298_field @ `0x001EC145`

```asm
0x001EC11F: int3
0x001EC120: push rbx
0x001EC122: sub rsp, 0x60
0x001EC126: mov rax, qword ptr [rip + 0x5ea7c3]
0x001EC12D: xor rax, rsp
0x001EC130: mov qword ptr [rsp + 0x58], rax
0x001EC135: xor r10d, r10d
0x001EC138: mov rbx, rdx
0x001EC13B: mov qword ptr [rsp + 0x20], r10
0x001EC140: mov rax, qword ptr [rsp + 0x20]
0x001EC145: mov dword ptr [rsp + 0x2c], r10d
0x001EC14A: cmp rax, 0x25
0x001EC14E: jae 0x1401ec193
0x001EC150: mov rax, qword ptr [rsp + 0x20]
0x001EC155: test rax, rax
0x001EC158: jne 0x1401ec15f
0x001EC15A: mov r9d, dword ptr [rcx]
0x001EC15D: jmp 0x1401ec16a
0x001EC15F: mov rax, qword ptr [rsp + 0x20]
0x001EC164: movsx r9d, byte ptr [rax + rcx + 3]
0x001EC16A: mov rax, qword ptr [rsp + 0x20]
0x001EC16F: movsx edx, byte ptr [rax + rcx + 4]
0x001EC174: mov rax, qword ptr [rsp + 0x20]
0x001EC179: sub edx, 0xb
```

### reg_9A0298_field @ `0x001EC205`

```asm
0x001EC1DF: int3
0x001EC1E0: push rbx
0x001EC1E2: sub rsp, 0x60
0x001EC1E6: mov rax, qword ptr [rip + 0x5ea703]
0x001EC1ED: xor rax, rsp
0x001EC1F0: mov qword ptr [rsp + 0x50], rax
0x001EC1F5: xor r10d, r10d
0x001EC1F8: mov rbx, rdx
0x001EC1FB: mov qword ptr [rsp + 0x20], r10
0x001EC200: mov rax, qword ptr [rsp + 0x20]
0x001EC205: mov dword ptr [rsp + 0x2c], r10d
0x001EC20A: cmp rax, 0x1c
0x001EC20E: jae 0x1401ec250
0x001EC210: mov rax, qword ptr [rsp + 0x20]
0x001EC215: test rax, rax
0x001EC218: jne 0x1401ec21f
0x001EC21A: mov r9d, dword ptr [rcx]
0x001EC21D: jmp 0x1401ec22a
0x001EC21F: mov rax, qword ptr [rsp + 0x20]
0x001EC224: movsx r9d, byte ptr [rax + rcx + 3]
0x001EC22A: mov rax, qword ptr [rsp + 0x20]
0x001EC22F: movsx edx, byte ptr [rax + rcx + 4]
0x001EC234: mov rax, qword ptr [rsp + 0x20]
0x001EC239: xor edx, r9d
```

### reg_9A0298_field @ `0x001EC2C5`

```asm
0x001EC29F: int3
0x001EC2A0: push rbx
0x001EC2A2: sub rsp, 0x50
0x001EC2A6: mov rax, qword ptr [rip + 0x5ea643]
0x001EC2AD: xor rax, rsp
0x001EC2B0: mov qword ptr [rsp + 0x40], rax
0x001EC2B5: xor r10d, r10d
0x001EC2B8: mov rbx, rdx
0x001EC2BB: mov qword ptr [rsp + 0x20], r10
0x001EC2C0: mov rax, qword ptr [rsp + 0x20]
0x001EC2C5: mov dword ptr [rsp + 0x2c], r10d
0x001EC2CA: cmp rax, 0xe
0x001EC2CE: jae 0x1401ec313
0x001EC2D0: mov rax, qword ptr [rsp + 0x20]
0x001EC2D5: test rax, rax
0x001EC2D8: jne 0x1401ec2df
0x001EC2DA: mov r9d, dword ptr [rcx]
0x001EC2DD: jmp 0x1401ec2ea
0x001EC2DF: mov rax, qword ptr [rsp + 0x20]
0x001EC2E4: movsx r9d, byte ptr [rax + rcx + 3]
0x001EC2EA: mov rax, qword ptr [rsp + 0x20]
0x001EC2EF: movsx edx, byte ptr [rax + rcx + 4]
0x001EC2F4: mov rax, qword ptr [rsp + 0x20]
0x001EC2F9: sub edx, 3
```

### reg_9A0298_field @ `0x001EC385`

```asm
0x001EC35F: int3
0x001EC360: push rbx
0x001EC362: sub rsp, 0x70
0x001EC366: mov rax, qword ptr [rip + 0x5ea583]
0x001EC36D: xor rax, rsp
0x001EC370: mov qword ptr [rsp + 0x60], rax
0x001EC375: xor r10d, r10d
0x001EC378: mov rbx, rdx
0x001EC37B: mov qword ptr [rsp + 0x20], r10
0x001EC380: mov rax, qword ptr [rsp + 0x20]
0x001EC385: mov dword ptr [rsp + 0x2c], r10d
0x001EC38A: cmp rax, 0x2b
0x001EC38E: jae 0x1401ec3d0
0x001EC390: mov rax, qword ptr [rsp + 0x20]
0x001EC395: test rax, rax
0x001EC398: jne 0x1401ec39f
0x001EC39A: mov r9d, dword ptr [rcx]
0x001EC39D: jmp 0x1401ec3aa
0x001EC39F: mov rax, qword ptr [rsp + 0x20]
0x001EC3A4: movsx r9d, byte ptr [rax + rcx + 3]
0x001EC3AA: mov rax, qword ptr [rsp + 0x20]
0x001EC3AF: movsx edx, byte ptr [rax + rcx + 4]
0x001EC3B4: mov rax, qword ptr [rsp + 0x20]
0x001EC3B9: xor edx, r9d
```

### reg_9A0298_field @ `0x001EC445`

```asm
0x001EC41F: int3
0x001EC420: push rbx
0x001EC422: sub rsp, 0x70
0x001EC426: mov rax, qword ptr [rip + 0x5ea4c3]
0x001EC42D: xor rax, rsp
0x001EC430: mov qword ptr [rsp + 0x68], rax
0x001EC435: xor r11d, r11d
0x001EC438: mov rbx, rdx
0x001EC43B: mov qword ptr [rsp + 0x20], r11
0x001EC440: mov rax, qword ptr [rsp + 0x20]
0x001EC445: mov dword ptr [rsp + 0x2c], r11d
0x001EC44A: cmp rax, 0x37
0x001EC44E: jae 0x1401ec49b
0x001EC450: mov rax, qword ptr [rsp + 0x20]
0x001EC455: test rax, rax
0x001EC458: jne 0x1401ec460
0x001EC45A: mov r10d, dword ptr [rcx + 4]
0x001EC45E: jmp 0x1401ec46b
0x001EC460: mov rax, qword ptr [rsp + 0x20]
0x001EC465: movsx r10d, byte ptr [rax + rcx + 7]
0x001EC46B: mov rax, qword ptr [rsp + 0x20]
0x001EC470: movsx r8d, byte ptr [rax + rcx + 8]
0x001EC476: mov eax, dword ptr [rcx]
0x001EC478: xor r8d, r10d
```

### reg_9A0298_field @ `0x001EC518`

```asm
0x001EC4EF: int3
0x001EC4F0: push rbx
0x001EC4F2: sub rsp, 0x80
0x001EC4F9: mov rax, qword ptr [rip + 0x5ea3f0]
0x001EC500: xor rax, rsp
0x001EC503: mov qword ptr [rsp + 0x70], rax
0x001EC508: xor r11d, r11d
0x001EC50B: mov rbx, rdx
0x001EC50E: mov qword ptr [rsp + 0x20], r11
0x001EC513: mov rax, qword ptr [rsp + 0x20]
0x001EC518: mov dword ptr [rsp + 0x2c], r11d
0x001EC51D: cmp rax, 0x39
0x001EC521: jae 0x1401ec56e
0x001EC523: mov rax, qword ptr [rsp + 0x20]
0x001EC528: test rax, rax
0x001EC52B: jne 0x1401ec533
0x001EC52D: mov r10d, dword ptr [rcx + 4]
0x001EC531: jmp 0x1401ec53e
0x001EC533: mov rax, qword ptr [rsp + 0x20]
0x001EC538: movsx r10d, byte ptr [rax + rcx + 7]
0x001EC53E: mov rax, qword ptr [rsp + 0x20]
0x001EC543: movsx r8d, byte ptr [rax + rcx + 8]
0x001EC549: mov eax, dword ptr [rcx]
0x001EC54B: xor r8d, r10d
```

### reg_9A0298_field @ `0x001EC5E5`

```asm
0x001EC5BF: int3
0x001EC5C0: push rbx
0x001EC5C2: sub rsp, 0x70
0x001EC5C6: mov rax, qword ptr [rip + 0x5ea323]
0x001EC5CD: xor rax, rsp
0x001EC5D0: mov qword ptr [rsp + 0x60], rax
0x001EC5D5: xor r11d, r11d
0x001EC5D8: mov rbx, rdx
0x001EC5DB: mov qword ptr [rsp + 0x20], r11
0x001EC5E0: mov rax, qword ptr [rsp + 0x20]
0x001EC5E5: mov dword ptr [rsp + 0x2c], r11d
0x001EC5EA: cmp rax, 0x2f
0x001EC5EE: jae 0x1401ec63b
0x001EC5F0: mov rax, qword ptr [rsp + 0x20]
0x001EC5F5: test rax, rax
0x001EC5F8: jne 0x1401ec600
0x001EC5FA: mov r10d, dword ptr [rcx + 4]
0x001EC5FE: jmp 0x1401ec60b
0x001EC600: mov rax, qword ptr [rsp + 0x20]
0x001EC605: movsx r10d, byte ptr [rax + rcx + 7]
0x001EC60B: mov rax, qword ptr [rsp + 0x20]
0x001EC610: movsx r8d, byte ptr [rax + rcx + 8]
0x001EC616: mov eax, dword ptr [rcx]
0x001EC618: xor r8d, r10d
```

### reg_9A0298_field @ `0x001EC6BB`

```asm
0x001EC68F: int3
0x001EC690: push rbx
0x001EC692: sub rsp, 0xc0
0x001EC699: mov rax, qword ptr [rip + 0x5ea250]
0x001EC6A0: xor rax, rsp
0x001EC6A3: mov qword ptr [rsp + 0xb0], rax
0x001EC6AB: xor r11d, r11d
0x001EC6AE: mov rbx, rdx
0x001EC6B1: mov qword ptr [rsp + 0x20], r11
0x001EC6B6: mov rax, qword ptr [rsp + 0x20]
0x001EC6BB: mov dword ptr [rsp + 0x2c], r11d
0x001EC6C0: cmp rax, 0x7e
0x001EC6C4: jae 0x1401ec711
0x001EC6C6: mov rax, qword ptr [rsp + 0x20]
0x001EC6CB: test rax, rax
0x001EC6CE: jne 0x1401ec6d6
0x001EC6D0: mov r10d, dword ptr [rcx + 4]
0x001EC6D4: jmp 0x1401ec6e1
0x001EC6D6: mov rax, qword ptr [rsp + 0x20]
0x001EC6DB: movsx r10d, byte ptr [rax + rcx + 7]
0x001EC6E1: mov rax, qword ptr [rsp + 0x20]
0x001EC6E6: movsx r8d, byte ptr [rax + rcx + 8]
0x001EC6EC: mov eax, dword ptr [rcx]
0x001EC6EE: xor r8d, r10d
```

### reg_9A0298_field @ `0x001EC795`

```asm
0x001EC76F: int3
0x001EC770: push rbx
0x001EC772: sub rsp, 0x60
0x001EC776: mov rax, qword ptr [rip + 0x5ea173]
0x001EC77D: xor rax, rsp
0x001EC780: mov qword ptr [rsp + 0x58], rax
0x001EC785: xor r11d, r11d
0x001EC788: mov rbx, rdx
0x001EC78B: mov qword ptr [rsp + 0x20], r11
0x001EC790: mov rax, qword ptr [rsp + 0x20]
0x001EC795: mov dword ptr [rsp + 0x2c], r11d
0x001EC79A: cmp rax, 0x26
0x001EC79E: jae 0x1401ec7eb
0x001EC7A0: mov rax, qword ptr [rsp + 0x20]
0x001EC7A5: test rax, rax
0x001EC7A8: jne 0x1401ec7b0
0x001EC7AA: mov r10d, dword ptr [rcx + 4]
0x001EC7AE: jmp 0x1401ec7bb
0x001EC7B0: mov rax, qword ptr [rsp + 0x20]
0x001EC7B5: movsx r10d, byte ptr [rax + rcx + 7]
0x001EC7BB: mov rax, qword ptr [rsp + 0x20]
0x001EC7C0: movsx r8d, byte ptr [rax + rcx + 8]
0x001EC7C6: mov eax, dword ptr [rcx]
0x001EC7C8: xor r8d, r10d
```

### reg_9A0298_field @ `0x001EC868`

```asm
0x001EC83F: int3
0x001EC840: push rbx
0x001EC842: sub rsp, 0x80
0x001EC849: mov rax, qword ptr [rip + 0x5ea0a0]
0x001EC850: xor rax, rsp
0x001EC853: mov qword ptr [rsp + 0x70], rax
0x001EC858: xor r11d, r11d
0x001EC85B: mov rbx, rdx
0x001EC85E: mov qword ptr [rsp + 0x20], r11
0x001EC863: mov rax, qword ptr [rsp + 0x20]
0x001EC868: mov dword ptr [rsp + 0x2c], r11d
0x001EC86D: cmp rax, 0x3c
0x001EC871: jae 0x1401ec8be
0x001EC873: mov rax, qword ptr [rsp + 0x20]
0x001EC878: test rax, rax
0x001EC87B: jne 0x1401ec883
0x001EC87D: mov r10d, dword ptr [rcx + 4]
0x001EC881: jmp 0x1401ec88e
0x001EC883: mov rax, qword ptr [rsp + 0x20]
0x001EC888: movsx r10d, byte ptr [rax + rcx + 7]
0x001EC88E: mov rax, qword ptr [rsp + 0x20]
0x001EC893: movsx r8d, byte ptr [rax + rcx + 8]
0x001EC899: mov eax, dword ptr [rcx]
0x001EC89B: xor r8d, r10d
```

### reg_9A0298_field @ `0x001EC935`

```asm
0x001EC90F: int3
0x001EC910: push rbx
0x001EC912: sub rsp, 0x60
0x001EC916: mov rax, qword ptr [rip + 0x5e9fd3]
0x001EC91D: xor rax, rsp
0x001EC920: mov qword ptr [rsp + 0x58], rax
0x001EC925: xor r11d, r11d
0x001EC928: mov rbx, rdx
0x001EC92B: mov qword ptr [rsp + 0x20], r11
0x001EC930: mov rax, qword ptr [rsp + 0x20]
0x001EC935: mov dword ptr [rsp + 0x2c], r11d
0x001EC93A: cmp rax, 0x25
0x001EC93E: jae 0x1401ec98b
0x001EC940: mov rax, qword ptr [rsp + 0x20]
0x001EC945: test rax, rax
0x001EC948: jne 0x1401ec950
0x001EC94A: mov r10d, dword ptr [rcx + 4]
0x001EC94E: jmp 0x1401ec95b
0x001EC950: mov rax, qword ptr [rsp + 0x20]
0x001EC955: movsx r10d, byte ptr [rax + rcx + 7]
0x001EC95B: mov rax, qword ptr [rsp + 0x20]
0x001EC960: movsx r8d, byte ptr [rax + rcx + 8]
0x001EC966: mov eax, dword ptr [rcx]
0x001EC968: xor r8d, r10d
```

### reg_9A0298_field @ `0x001ECA05`

```asm
0x001EC9DF: int3
0x001EC9E0: push rbx
0x001EC9E2: sub rsp, 0x50
0x001EC9E6: mov rax, qword ptr [rip + 0x5e9f03]
0x001EC9ED: xor rax, rsp
0x001EC9F0: mov qword ptr [rsp + 0x48], rax
0x001EC9F5: xor r11d, r11d
0x001EC9F8: mov rbx, rdx
0x001EC9FB: mov qword ptr [rsp + 0x20], r11
0x001ECA00: mov rax, qword ptr [rsp + 0x20]
0x001ECA05: mov dword ptr [rsp + 0x2c], r11d
0x001ECA0A: cmp rax, 0x13
0x001ECA0E: jae 0x1401eca5b
0x001ECA10: mov rax, qword ptr [rsp + 0x20]
0x001ECA15: test rax, rax
0x001ECA18: jne 0x1401eca20
0x001ECA1A: mov r10d, dword ptr [rcx + 4]
0x001ECA1E: jmp 0x1401eca2b
0x001ECA20: mov rax, qword ptr [rsp + 0x20]
0x001ECA25: movsx r10d, byte ptr [rax + rcx + 7]
0x001ECA2B: mov rax, qword ptr [rsp + 0x20]
0x001ECA30: movsx r8d, byte ptr [rax + rcx + 8]
0x001ECA36: mov eax, dword ptr [rcx]
0x001ECA38: xor r8d, r10d
```

### reg_9A0298_field @ `0x001ECADB`

```asm
0x001ECAAF: int3
0x001ECAB0: push rbx
0x001ECAB2: sub rsp, 0xc0
0x001ECAB9: mov rax, qword ptr [rip + 0x5e9e30]
0x001ECAC0: xor rax, rsp
0x001ECAC3: mov qword ptr [rsp + 0xb0], rax
0x001ECACB: xor r11d, r11d
0x001ECACE: mov rbx, rdx
0x001ECAD1: mov qword ptr [rsp + 0x20], r11
0x001ECAD6: mov rax, qword ptr [rsp + 0x20]
0x001ECADB: mov dword ptr [rsp + 0x2c], r11d
0x001ECAE0: cmp rax, 0x7c
0x001ECAE4: jae 0x1401ecb31
0x001ECAE6: mov rax, qword ptr [rsp + 0x20]
0x001ECAEB: test rax, rax
0x001ECAEE: jne 0x1401ecaf6
0x001ECAF0: mov r10d, dword ptr [rcx + 4]
0x001ECAF4: jmp 0x1401ecb01
0x001ECAF6: mov rax, qword ptr [rsp + 0x20]
0x001ECAFB: movsx r10d, byte ptr [rax + rcx + 7]
0x001ECB01: mov rax, qword ptr [rsp + 0x20]
0x001ECB06: movsx r8d, byte ptr [rax + rcx + 8]
0x001ECB0C: mov eax, dword ptr [rcx]
0x001ECB0E: xor r8d, r10d
```

### reg_9A029C_field @ `0x001ECE99`

```asm
0x001ECE74: mov dword ptr [rsp + 0x30], 0x22
0x001ECE7C: mov eax, dword ptr [rsp + 0x30]
0x001ECE80: add al, 0x22
0x001ECE82: movsx ecx, al
0x001ECE85: xor ecx, 0x71
0x001ECE88: mov dword ptr [rsp + 0x34], ecx
0x001ECE8C: mov eax, dword ptr [rsp + 0x34]
0x001ECE90: mov ecx, dword ptr [rsp + 0x30]
0x001ECE94: xor ecx, eax
0x001ECE96: xor ecx, 0x7b
0x001ECE99: mov byte ptr [rsp + 0x38], cl
0x001ECE9D: movsx ecx, byte ptr [rsp + 0x38]
0x001ECEA2: mov eax, dword ptr [rsp + 0x30]
0x001ECEA6: inc al
0x001ECEA8: xor eax, ecx
0x001ECEAA: xor eax, 0x7d
0x001ECEAD: mov byte ptr [rsp + 0x39], al
0x001ECEB1: movsx ecx, byte ptr [rsp + 0x39]
0x001ECEB6: mov eax, dword ptr [rsp + 0x30]
0x001ECEBA: add al, 2
0x001ECEBC: xor eax, ecx
0x001ECEBE: xor eax, 0x3a
0x001ECEC1: mov byte ptr [rsp + 0x3a], al
0x001ECEC5: movsx ecx, byte ptr [rsp + 0x3a]
```

### reg_9A02A0_field @ `0x001ECF89`

```asm
0x001ECF6A: mov eax, dword ptr [rsp + 0x30]
0x001ECF6E: add al, 0xb
0x001ECF70: xor eax, ecx
0x001ECF72: xor eax, 0x52
0x001ECF75: mov byte ptr [rsp + 0x43], al
0x001ECF79: movsx ecx, byte ptr [rsp + 0x43]
0x001ECF7E: mov eax, dword ptr [rsp + 0x30]
0x001ECF82: add al, 0xc
0x001ECF84: xor eax, ecx
0x001ECF86: xor eax, 0x41
0x001ECF89: mov byte ptr [rsp + 0x44], al
0x001ECF8D: movsx ecx, byte ptr [rsp + 0x44]
0x001ECF92: mov eax, dword ptr [rsp + 0x30]
0x001ECF96: add al, 0xd
0x001ECF98: xor eax, ecx
0x001ECF9A: xor eax, 0x4d
0x001ECF9D: mov byte ptr [rsp + 0x45], al
0x001ECFA1: movsx ecx, byte ptr [rsp + 0x45]
0x001ECFA6: mov eax, dword ptr [rsp + 0x30]
0x001ECFAA: add al, 0xe
0x001ECFAC: xor eax, ecx
0x001ECFAE: xor eax, 0x20
0x001ECFB1: mov byte ptr [rsp + 0x46], al
0x001ECFB5: movsx ecx, byte ptr [rsp + 0x46]
```

### reg_9A029C_field @ `0x001ED15C`

```asm
0x001ED128: mov rcx, qword ptr [rbx + 0xd0]
0x001ED12F: call rdi
0x001ED131: mov dword ptr [rsp + 0x20], eax
0x001ED135: test eax, eax
0x001ED137: je 0x1401ed39f
0x001ED13D: mov dword ptr [rsp + 0x24], 0x591
0x001ED145: mov dword ptr [rsp + 0x30], 0x76
0x001ED14D: mov dword ptr [rsp + 0x34], 0x71
0x001ED155: mov eax, dword ptr [rsp + 0x34]
0x001ED159: xor eax, 0x38
0x001ED15C: mov byte ptr [rsp + 0x38], al
0x001ED160: movsx ecx, byte ptr [rsp + 0x38]
0x001ED165: xor ecx, 0x20
0x001ED168: mov byte ptr [rsp + 0x39], cl
0x001ED16C: movsx ecx, byte ptr [rsp + 0x39]
0x001ED171: xor ecx, 0x37
0x001ED174: mov byte ptr [rsp + 0x3a], cl
0x001ED178: movsx ecx, byte ptr [rsp + 0x3a]
0x001ED17D: xor ecx, 0x26
0x001ED180: mov byte ptr [rsp + 0x3b], cl
0x001ED184: movsx ecx, byte ptr [rsp + 0x3b]
0x001ED189: xor ecx, 0x3f
0x001ED18C: mov byte ptr [rsp + 0x3c], cl
0x001ED190: movsx ecx, byte ptr [rsp + 0x3c]
```

### reg_9A02A0_field @ `0x001ED1EC`

```asm
0x001ED1C5: xor ecx, 0x19
0x001ED1C8: mov byte ptr [rsp + 0x41], cl
0x001ED1CC: movsx ecx, byte ptr [rsp + 0x41]
0x001ED1D1: xor ecx, 4
0x001ED1D4: mov byte ptr [rsp + 0x42], cl
0x001ED1D8: movsx ecx, byte ptr [rsp + 0x42]
0x001ED1DD: xor ecx, 0x56
0x001ED1E0: mov byte ptr [rsp + 0x43], cl
0x001ED1E4: movsx ecx, byte ptr [rsp + 0x43]
0x001ED1E9: xor ecx, 0x1f
0x001ED1EC: mov byte ptr [rsp + 0x44], cl
0x001ED1F0: movsx ecx, byte ptr [rsp + 0x44]
0x001ED1F5: xor ecx, 0x18
0x001ED1F8: mov byte ptr [rsp + 0x45], cl
0x001ED1FC: movsx ecx, byte ptr [rsp + 0x45]
0x001ED201: xor ecx, 0x56
0x001ED204: mov byte ptr [rsp + 0x46], cl
0x001ED208: movsx ecx, byte ptr [rsp + 0x46]
0x001ED20D: xor ecx, 0x38
0x001ED210: mov byte ptr [rsp + 0x47], cl
0x001ED214: movsx eax, byte ptr [rsp + 0x47]
0x001ED219: mov byte ptr [rsp + 0x48], al
0x001ED21D: movsx ecx, byte ptr [rsp + 0x48]
0x001ED222: xor ecx, 0x17
```

### reg_9A0290_field @ `0x001ED885`

```asm
0x001ED86C: xor rcx, rsp
0x001ED86F: call 0x1403b24c0
0x001ED874: add rsp, 0xb0
0x001ED87B: pop rbp
0x001ED87C: ret
0x001ED87D: int3
0x001ED87E: int3
0x001ED87F: int3
0x001ED880: xor eax, eax
0x001ED882: mov qword ptr [rcx], rdx
0x001ED885: mov dword ptr [rcx + 8], eax
0x001ED888: mov qword ptr [rcx + 0x10], rax
0x001ED88C: mov qword ptr [rcx + 0x18], rax
0x001ED890: mov qword ptr [rcx + 0x20], rax
0x001ED894: mov dword ptr [rcx + 0x2c], 0x3e8
0x001ED89B: mov qword ptr [rcx + 0x30], rax
0x001ED89F: mov rax, rcx
0x001ED8A2: ret
0x001ED8A3: int3
0x001ED8A4: int3
0x001ED8A5: int3
0x001ED8A6: int3
0x001ED8A7: int3
0x001ED8A8: int3
```

### reg_9A0298_field @ `0x001ED894`

```asm
0x001ED87C: ret
0x001ED87D: int3
0x001ED87E: int3
0x001ED87F: int3
0x001ED880: xor eax, eax
0x001ED882: mov qword ptr [rcx], rdx
0x001ED885: mov dword ptr [rcx + 8], eax
0x001ED888: mov qword ptr [rcx + 0x10], rax
0x001ED88C: mov qword ptr [rcx + 0x18], rax
0x001ED890: mov qword ptr [rcx + 0x20], rax
0x001ED894: mov dword ptr [rcx + 0x2c], 0x3e8
0x001ED89B: mov qword ptr [rcx + 0x30], rax
0x001ED89F: mov rax, rcx
0x001ED8A2: ret
0x001ED8A3: int3
0x001ED8A4: int3
0x001ED8A5: int3
0x001ED8A6: int3
0x001ED8A7: int3
0x001ED8A8: int3
0x001ED8A9: int3
0x001ED8AA: int3
0x001ED8AB: int3
0x001ED8AC: int3
```

### reg_9A029C_field @ `0x001EE972`

```asm
0x001EE938: mov qword ptr [rsp + 0x4a0], r14
0x001EE940: mov byte ptr [rsp + 0x490], 0
0x001EE948: lea rdx, [rsi + 0xff]
0x001EE94F: and rdx, 0xffffffffffffff00
0x001EE956: lea rcx, [rbx + 0x18]
0x001EE95A: call 0x14029179e
0x001EE95F: mov dword ptr [rsp + 0x24], eax
0x001EE963: test eax, eax
0x001EE965: je 0x1401eed3e
0x001EE96B: lea rcx, [rip + 0x24508e]
0x001EE972: mov qword ptr [rsp + 0x38], rcx
0x001EE977: lea rdx, [rsp + 0x38]
0x001EE97C: mov ecx, eax
0x001EE97E: call 0x14029177a
0x001EE983: mov dword ptr [rsp + 0x28], 0x188
0x001EE98B: mov dword ptr [rsp + 0x438], 0x77
0x001EE996: mov dword ptr [rsp + 0x43c], 0x27
0x001EE9A1: mov eax, dword ptr [rsp + 0x43c]
0x001EE9A8: xor eax, 0x34
0x001EE9AB: mov byte ptr [rsp + 0x440], al
0x001EE9B2: movsx ecx, byte ptr [rsp + 0x440]
0x001EE9BA: xor ecx, 0x22
0x001EE9BD: mov byte ptr [rsp + 0x441], cl
0x001EE9C4: movsx ecx, byte ptr [rsp + 0x441]
```

### reg_9A0290_field @ `0x001EEDDA`

```asm
0x001EEDB6: mov dword ptr [rip + 0x5f8ba8], edx
0x001EEDBC: ret
0x001EEDBD: int3
0x001EEDBE: int3
0x001EEDBF: int3
0x001EEDC0: mov rax, rsp
0x001EEDC3: push rbp
0x001EEDC4: lea rbp, [rax - 0x9c8]
0x001EEDCB: sub rsp, 0xac0
0x001EEDD2: mov qword ptr [rbp - 0x10], 0xfffffffffffffffe
0x001EEDDA: mov qword ptr [rax + 8], rbx
0x001EEDDE: mov qword ptr [rax + 0x10], rsi
0x001EEDE2: mov qword ptr [rax + 0x18], rdi
0x001EEDE6: mov rax, qword ptr [rip + 0x5e7b03]
0x001EEDED: xor rax, rsp
0x001EEDF0: mov qword ptr [rbp + 0x9b0], rax
0x001EEDF7: cmp dword ptr [rip + 0x5f764a], 0
0x001EEDFE: jg 0x1401ef9b8
0x001EEE04: call 0x140001120
0x001EEE09: mov edi, eax
0x001EEE0B: test eax, eax
0x001EEE0D: je 0x1401ef49f
0x001EEE13: mov ecx, eax
0x001EEE15: call 0x140001480
```

### reg_9A029C_field @ `0x001EF310`

```asm
0x001EF2CB: mov qword ptr [rbp + 0x4f8], rcx
0x001EF2D2: lea rbx, [rip + 0x2449df]
0x001EF2D9: mov qword ptr [rbp + 0x4f0], rbx
0x001EF2E0: lea rcx, [rbp + 0x520]
0x001EF2E7: mov qword ptr [rbp + 0x508], rcx
0x001EF2EE: xor ecx, ecx
0x001EF2F0: mov qword ptr [rbp + 0x510], rcx
0x001EF2F7: mov qword ptr [rbp + 0x518], 0x1f4
0x001EF302: lea rdx, [rip + 0x244907]
0x001EF309: mov qword ptr [rbp + 0x500], rdx
0x001EF310: mov dword ptr [rsp + 0x38], 0xbd
0x001EF318: movups xmm0, xmmword ptr [rsp + 0x38]
0x001EF31D: movups xmmword ptr [rbp + 0x950], xmm0
0x001EF324: mov qword ptr [rsp + 0x38], rsi
0x001EF329: movups xmm0, xmmword ptr [rsp + 0x38]
0x001EF32E: movups xmmword ptr [rbp + 0x960], xmm0
0x001EF335: mov dword ptr [rsp + 0x38], edi
0x001EF339: movups xmm0, xmmword ptr [rsp + 0x38]
0x001EF33E: movups xmmword ptr [rbp + 0x970], xmm0
0x001EF345: mov qword ptr [rsp + 0x60], 0x2a2
0x001EF34E: lea rdx, [rbp + 0x950]
0x001EF355: mov qword ptr [rsp + 0x68], rdx
0x001EF35A: movups xmm0, xmmword ptr [rsp + 0x60]
0x001EF35F: movups xmmword ptr [rbp - 0x80], xmm0
```

### reg_9A029C_field @ `0x001EF324`

```asm
0x001EF2E0: lea rcx, [rbp + 0x520]
0x001EF2E7: mov qword ptr [rbp + 0x508], rcx
0x001EF2EE: xor ecx, ecx
0x001EF2F0: mov qword ptr [rbp + 0x510], rcx
0x001EF2F7: mov qword ptr [rbp + 0x518], 0x1f4
0x001EF302: lea rdx, [rip + 0x244907]
0x001EF309: mov qword ptr [rbp + 0x500], rdx
0x001EF310: mov dword ptr [rsp + 0x38], 0xbd
0x001EF318: movups xmm0, xmmword ptr [rsp + 0x38]
0x001EF31D: movups xmmword ptr [rbp + 0x950], xmm0
0x001EF324: mov qword ptr [rsp + 0x38], rsi
0x001EF329: movups xmm0, xmmword ptr [rsp + 0x38]
0x001EF32E: movups xmmword ptr [rbp + 0x960], xmm0
0x001EF335: mov dword ptr [rsp + 0x38], edi
0x001EF339: movups xmm0, xmmword ptr [rsp + 0x38]
0x001EF33E: movups xmmword ptr [rbp + 0x970], xmm0
0x001EF345: mov qword ptr [rsp + 0x60], 0x2a2
0x001EF34E: lea rdx, [rbp + 0x950]
0x001EF355: mov qword ptr [rsp + 0x68], rdx
0x001EF35A: movups xmm0, xmmword ptr [rsp + 0x60]
0x001EF35F: movups xmmword ptr [rbp - 0x80], xmm0
0x001EF363: mov dword ptr [rbp - 0x70], ecx
0x001EF366: lea rdx, [rbp + 0x4f0]
0x001EF36D: mov qword ptr [rbp - 0x68], rdx
```

### reg_9A029C_field @ `0x001EF335`

```asm
0x001EF2F0: mov qword ptr [rbp + 0x510], rcx
0x001EF2F7: mov qword ptr [rbp + 0x518], 0x1f4
0x001EF302: lea rdx, [rip + 0x244907]
0x001EF309: mov qword ptr [rbp + 0x500], rdx
0x001EF310: mov dword ptr [rsp + 0x38], 0xbd
0x001EF318: movups xmm0, xmmword ptr [rsp + 0x38]
0x001EF31D: movups xmmword ptr [rbp + 0x950], xmm0
0x001EF324: mov qword ptr [rsp + 0x38], rsi
0x001EF329: movups xmm0, xmmword ptr [rsp + 0x38]
0x001EF32E: movups xmmword ptr [rbp + 0x960], xmm0
0x001EF335: mov dword ptr [rsp + 0x38], edi
0x001EF339: movups xmm0, xmmword ptr [rsp + 0x38]
0x001EF33E: movups xmmword ptr [rbp + 0x970], xmm0
0x001EF345: mov qword ptr [rsp + 0x60], 0x2a2
0x001EF34E: lea rdx, [rbp + 0x950]
0x001EF355: mov qword ptr [rsp + 0x68], rdx
0x001EF35A: movups xmm0, xmmword ptr [rsp + 0x60]
0x001EF35F: movups xmmword ptr [rbp - 0x80], xmm0
0x001EF363: mov dword ptr [rbp - 0x70], ecx
0x001EF366: lea rdx, [rbp + 0x4f0]
0x001EF36D: mov qword ptr [rbp - 0x68], rdx
0x001EF371: xorps xmm0, xmm0
0x001EF374: movdqu xmmword ptr [rbp - 0x60], xmm0
0x001EF379: mov qword ptr [rbp - 0x50], rcx
```

### reg_9A029C_field @ `0x001EF970`

```asm
0x001EF93E: call 0x1400328e0
0x001EF943: lea rcx, [rbp + 0x220]
0x001EF94A: call 0x14004afc0
0x001EF94F: nop
0x001EF950: lea rcx, [rbp + 0x730]
0x001EF957: call 0x140032dc0
0x001EF95C: nop
0x001EF95D: lea rcx, [rbp + 0x4d0]
0x001EF964: call 0x140032ef0
0x001EF969: lea rax, [rip + 0x244000]
0x001EF970: mov qword ptr [rsp + 0x38], rax
0x001EF975: xor eax, eax
0x001EF977: mov qword ptr [rsp + 0x40], rax
0x001EF97C: mov qword ptr [rsp + 0x48], rax
0x001EF981: mov qword ptr [rsp + 0x70], rsi
0x001EF986: mov byte ptr [rsp + 0x78], 1
0x001EF98B: lea rdx, [rsp + 0x40]
0x001EF990: lea rcx, [rsp + 0x70]
0x001EF995: call 0x1403d23c8
0x001EF99A: lea rax, [rip + 0x243fe7]
0x001EF9A1: mov qword ptr [rsp + 0x38], rax
0x001EF9A6: lea rdx, [rip + 0x59b5b3]
0x001EF9AD: lea rcx, [rsp + 0x38]
0x001EF9B2: call 0x1403d25d0
```

### reg_9A029C_field @ `0x001EF9A1`

```asm
0x001EF970: mov qword ptr [rsp + 0x38], rax
0x001EF975: xor eax, eax
0x001EF977: mov qword ptr [rsp + 0x40], rax
0x001EF97C: mov qword ptr [rsp + 0x48], rax
0x001EF981: mov qword ptr [rsp + 0x70], rsi
0x001EF986: mov byte ptr [rsp + 0x78], 1
0x001EF98B: lea rdx, [rsp + 0x40]
0x001EF990: lea rcx, [rsp + 0x70]
0x001EF995: call 0x1403d23c8
0x001EF99A: lea rax, [rip + 0x243fe7]
0x001EF9A1: mov qword ptr [rsp + 0x38], rax
0x001EF9A6: lea rdx, [rip + 0x59b5b3]
0x001EF9AD: lea rcx, [rsp + 0x38]
0x001EF9B2: call 0x1403d25d0
0x001EF9B7: int3
0x001EF9B8: mov rcx, qword ptr [rbp + 0x9b0]
0x001EF9BF: xor rcx, rsp
0x001EF9C2: call 0x1403b24c0
0x001EF9C7: lea r11, [rsp + 0xac0]
0x001EF9CF: mov rbx, qword ptr [r11 + 0x10]
0x001EF9D3: mov rsi, qword ptr [r11 + 0x18]
0x001EF9D7: mov rdi, qword ptr [r11 + 0x20]
0x001EF9DB: mov rsp, r11
0x001EF9DE: pop rbp
```

### reg_9A029C_field @ `0x001EFCC7`

```asm
0x001EFCA0: lea rcx, [rbp + 0x50]
0x001EFCA4: call 0x14002ecf0
0x001EFCA9: nop
0x001EFCAA: cmp qword ptr [rax + 0x18], 0x10
0x001EFCAF: jb 0x1401efcb4
0x001EFCB1: mov rax, qword ptr [rax]
0x001EFCB4: lea rcx, [rip + 0x243cb5]
0x001EFCBB: mov qword ptr [rsp + 0x28], rcx
0x001EFCC0: xor ecx, ecx
0x001EFCC2: mov qword ptr [rsp + 0x30], rcx
0x001EFCC7: mov qword ptr [rsp + 0x38], rcx
0x001EFCCC: mov qword ptr [rsp + 0x58], rax
0x001EFCD1: mov byte ptr [rsp + 0x60], 1
0x001EFCD6: lea rdx, [rsp + 0x30]
0x001EFCDB: lea rcx, [rsp + 0x58]
0x001EFCE0: call 0x1403d23c8
0x001EFCE5: lea rax, [rip + 0x243c9c]
0x001EFCEC: mov qword ptr [rsp + 0x28], rax
0x001EFCF1: lea rdx, [rip + 0x59b268]
0x001EFCF8: lea rcx, [rsp + 0x28]
0x001EFCFD: call 0x1403d25d0
0x001EFD02: nop
0x001EFD03: cmp eax, 0x26
0x001EFD06: jne 0x1401efe68
```

### reg_9A0298_field @ `0x001F007E`

```asm
0x001F0051: mov byte ptr [rbp - 0x49], 1
0x001F0055: lea rdx, [rbp - 0x61]
0x001F0059: lea rcx, [rbp - 0x51]
0x001F005D: call 0x1403d23c8
0x001F0062: lea rax, [rip + 0x24391f]
0x001F0069: mov qword ptr [rbp - 0x69], rax
0x001F006D: lea rdx, [rip + 0x59aeec]
0x001F0074: lea rcx, [rbp - 0x69]
0x001F0078: call 0x1403d25d0
0x001F007D: nop
0x001F007E: mov dword ptr [rdi + 0x2c], r14d
0x001F0082: mov dword ptr [rdi + 0x28], esi
0x001F0085: mov eax, dword ptr [rbp + 0x77]
0x001F0088: mov dword ptr [rdi + 8], eax
0x001F008B: lea eax, [rcx - 1]
0x001F008E: cmp eax, ebx
0x001F0090: cmovl ebx, eax
0x001F0093: mov dword ptr [rsp + 0x30], r14d
0x001F0098: mov dword ptr [rsp + 0x28], esi
0x001F009C: mov dword ptr [rsp + 0x20], ebx
0x001F00A0: movzx r9d, r12b
0x001F00A4: mov r8d, r15d
0x001F00A7: mov rdx, rdi
0x001F00AA: lea rcx, [rbp - 0x71]
```

### reg_9A0290_field @ `0x001F0088`

```asm
0x001F005D: call 0x1403d23c8
0x001F0062: lea rax, [rip + 0x24391f]
0x001F0069: mov qword ptr [rbp - 0x69], rax
0x001F006D: lea rdx, [rip + 0x59aeec]
0x001F0074: lea rcx, [rbp - 0x69]
0x001F0078: call 0x1403d25d0
0x001F007D: nop
0x001F007E: mov dword ptr [rdi + 0x2c], r14d
0x001F0082: mov dword ptr [rdi + 0x28], esi
0x001F0085: mov eax, dword ptr [rbp + 0x77]
0x001F0088: mov dword ptr [rdi + 8], eax
0x001F008B: lea eax, [rcx - 1]
0x001F008E: cmp eax, ebx
0x001F0090: cmovl ebx, eax
0x001F0093: mov dword ptr [rsp + 0x30], r14d
0x001F0098: mov dword ptr [rsp + 0x28], esi
0x001F009C: mov dword ptr [rsp + 0x20], ebx
0x001F00A0: movzx r9d, r12b
0x001F00A4: mov r8d, r15d
0x001F00A7: mov rdx, rdi
0x001F00AA: lea rcx, [rbp - 0x71]
0x001F00AE: call 0x1401f21f0
0x001F00B3: add rdi, 0x30
0x001F00B7: cmp rdi, rax
```

### reg_9A029C_field @ `0x001F049A`

```asm
0x001F0471: call 0x140391550
0x001F0476: mov rbx, rax
0x001F0479: call 0x140391534
0x001F047E: cqo
0x001F0480: idiv rbx
0x001F0483: imul rcx, rax, 0x3b9aca00
0x001F048A: imul rax, rdx, 0x3b9aca00
0x001F0491: cqo
0x001F0493: idiv rbx
0x001F0496: lea rbx, [rax + rcx]
0x001F049A: mov qword ptr [rsp + 0x38], rbx
0x001F049F: mov qword ptr [rsp + 0x40], rbx
0x001F04A4: mov rcx, qword ptr [rsi + 0x30]
0x001F04A8: mov rax, qword ptr [rcx]
0x001F04AB: mov r9, qword ptr [r14]
0x001F04AE: mov r8d, r15d
0x001F04B1: mov edx, dword ptr [rsi + 0x28]
0x001F04B4: call qword ptr [rax + 8]
0x001F04B7: test al, al
0x001F04B9: je 0x1401f0199
0x001F04BF: call 0x140391550
0x001F04C4: mov rdi, rax
0x001F04C7: call 0x140391534
0x001F04CC: cqo
```

### reg_9A0298_field @ `0x001F09A5`

```asm
0x001F097F: int3
0x001F0980: push rbx
0x001F0982: sub rsp, 0x70
0x001F0986: mov rax, qword ptr [rip + 0x5e5f63]
0x001F098D: xor rax, rsp
0x001F0990: mov qword ptr [rsp + 0x60], rax
0x001F0995: xor r10d, r10d
0x001F0998: mov rbx, rdx
0x001F099B: mov qword ptr [rsp + 0x20], r10
0x001F09A0: mov rax, qword ptr [rsp + 0x20]
0x001F09A5: mov dword ptr [rsp + 0x2c], r10d
0x001F09AA: cmp rax, 0x2b
0x001F09AE: jae 0x1401f09f3
0x001F09B0: mov rax, qword ptr [rsp + 0x20]
0x001F09B5: test rax, rax
0x001F09B8: jne 0x1401f09bf
0x001F09BA: mov r9d, dword ptr [rcx]
0x001F09BD: jmp 0x1401f09ca
0x001F09BF: mov rax, qword ptr [rsp + 0x20]
0x001F09C4: movsx r9d, byte ptr [rax + rcx + 3]
0x001F09CA: mov rax, qword ptr [rsp + 0x20]
0x001F09CF: movsx edx, byte ptr [rax + rcx + 4]
0x001F09D4: mov rax, qword ptr [rsp + 0x20]
0x001F09D9: sub edx, 9
```

### reg_9A0298_field @ `0x001F0A65`

```asm
0x001F0A3F: int3
0x001F0A40: push rbx
0x001F0A42: sub rsp, 0x70
0x001F0A46: mov rax, qword ptr [rip + 0x5e5ea3]
0x001F0A4D: xor rax, rsp
0x001F0A50: mov qword ptr [rsp + 0x60], rax
0x001F0A55: xor r10d, r10d
0x001F0A58: mov rbx, rdx
0x001F0A5B: mov qword ptr [rsp + 0x20], r10
0x001F0A60: mov rax, qword ptr [rsp + 0x20]
0x001F0A65: mov dword ptr [rsp + 0x2c], r10d
0x001F0A6A: cmp rax, 0x2c
0x001F0A6E: jae 0x1401f0ab3
0x001F0A70: mov rax, qword ptr [rsp + 0x20]
0x001F0A75: test rax, rax
0x001F0A78: jne 0x1401f0a7f
0x001F0A7A: mov r9d, dword ptr [rcx]
0x001F0A7D: jmp 0x1401f0a8a
0x001F0A7F: mov rax, qword ptr [rsp + 0x20]
0x001F0A84: movsx r9d, byte ptr [rax + rcx + 3]
0x001F0A8A: mov rax, qword ptr [rsp + 0x20]
0x001F0A8F: movsx edx, byte ptr [rax + rcx + 4]
0x001F0A94: mov rax, qword ptr [rsp + 0x20]
0x001F0A99: sub edx, 2
```

### reg_9A0298_field @ `0x001F0B25`

```asm
0x001F0AFF: int3
0x001F0B00: push rbx
0x001F0B02: sub rsp, 0x70
0x001F0B06: mov rax, qword ptr [rip + 0x5e5de3]
0x001F0B0D: xor rax, rsp
0x001F0B10: mov qword ptr [rsp + 0x68], rax
0x001F0B15: xor r10d, r10d
0x001F0B18: mov rbx, rdx
0x001F0B1B: mov qword ptr [rsp + 0x20], r10
0x001F0B20: mov rax, qword ptr [rsp + 0x20]
0x001F0B25: mov dword ptr [rsp + 0x2c], r10d
0x001F0B2A: cmp rax, 0x38
0x001F0B2E: jae 0x1401f0b73
0x001F0B30: mov rax, qword ptr [rsp + 0x20]
0x001F0B35: test rax, rax
0x001F0B38: jne 0x1401f0b3f
0x001F0B3A: mov r9d, dword ptr [rcx]
0x001F0B3D: jmp 0x1401f0b4a
0x001F0B3F: mov rax, qword ptr [rsp + 0x20]
0x001F0B44: movsx r9d, byte ptr [rax + rcx + 3]
0x001F0B4A: mov rax, qword ptr [rsp + 0x20]
0x001F0B4F: movsx edx, byte ptr [rax + rcx + 4]
0x001F0B54: mov rax, qword ptr [rsp + 0x20]
0x001F0B59: sub edx, 3
```

### reg_9A0298_field @ `0x001F0BE5`

```asm
0x001F0BBF: int3
0x001F0BC0: push rbx
0x001F0BC2: sub rsp, 0x70
0x001F0BC6: mov rax, qword ptr [rip + 0x5e5d23]
0x001F0BCD: xor rax, rsp
0x001F0BD0: mov qword ptr [rsp + 0x60], rax
0x001F0BD5: xor r10d, r10d
0x001F0BD8: mov rbx, rdx
0x001F0BDB: mov qword ptr [rsp + 0x20], r10
0x001F0BE0: mov rax, qword ptr [rsp + 0x20]
0x001F0BE5: mov dword ptr [rsp + 0x2c], r10d
0x001F0BEA: cmp rax, 0x30
0x001F0BEE: jae 0x1401f0c33
0x001F0BF0: mov rax, qword ptr [rsp + 0x20]
0x001F0BF5: test rax, rax
0x001F0BF8: jne 0x1401f0bff
0x001F0BFA: mov r9d, dword ptr [rcx]
0x001F0BFD: jmp 0x1401f0c0a
0x001F0BFF: mov rax, qword ptr [rsp + 0x20]
0x001F0C04: movsx r9d, byte ptr [rax + rcx + 3]
0x001F0C0A: mov rax, qword ptr [rsp + 0x20]
0x001F0C0F: movsx edx, byte ptr [rax + rcx + 4]
0x001F0C14: mov rax, qword ptr [rsp + 0x20]
0x001F0C19: sub edx, 5
```

### reg_9A029C_field @ `0x001F0C91`

```asm
0x001F0C7F: int3
0x001F0C80: push rbx
0x001F0C82: push rbp
0x001F0C83: push rsi
0x001F0C84: push rdi
0x001F0C85: push r12
0x001F0C87: push r13
0x001F0C89: push r14
0x001F0C8B: push r15
0x001F0C8D: sub rsp, 0x78
0x001F0C91: mov qword ptr [rsp + 0x38], 0xfffffffffffffffe
0x001F0C9A: mov rax, qword ptr [rip + 0x5e5c4f]
0x001F0CA1: xor rax, rsp
0x001F0CA4: mov qword ptr [rsp + 0x68], rax
0x001F0CA9: mov r12, r9
0x001F0CAC: mov r15, r8
0x001F0CAF: mov r14, rdx
0x001F0CB2: mov rsi, rcx
0x001F0CB5: mov r13, qword ptr [rsp + 0xe0]
0x001F0CBD: mov rdi, qword ptr [rsp + 0xe8]
0x001F0CC5: xor ebx, ebx
0x001F0CC7: mov dword ptr [rsp + 0x30], ebx
0x001F0CCB: mov ecx, 0x4e8
0x001F0CD0: call 0x1403b2098
```

### reg_9A029C_field @ `0x001F0ECE`

```asm
0x001F0EA5: lea rcx, [rsp + 0x80]
0x001F0EAD: call 0x1400355e0
0x001F0EB2: nop
0x001F0EB3: mov ebx, 1
0x001F0EB8: mov dword ptr [rsp + 0x50], ebx
0x001F0EBC: mov rax, qword ptr [rsp + 0x58]
0x001F0EC1: mov eax, dword ptr [rax]
0x001F0EC3: mov dword ptr [rsp + 0x40], eax
0x001F0EC7: mov rax, qword ptr [rsp + 0x60]
0x001F0ECC: mov eax, dword ptr [rax]
0x001F0ECE: mov dword ptr [rsp + 0x38], eax
0x001F0ED2: lea rax, [rsp + 0x80]
0x001F0EDA: mov qword ptr [rsp + 0x30], rax
0x001F0EDF: mov rax, qword ptr [rsp + 0x68]
0x001F0EE4: movzx eax, byte ptr [rax]
0x001F0EE7: mov byte ptr [rsp + 0x28], al
0x001F0EEB: mov eax, dword ptr [r13]
0x001F0EEF: mov dword ptr [rsp + 0x20], eax
0x001F0EF3: mov r9d, dword ptr [r12]
0x001F0EF7: mov r8d, dword ptr [r15]
0x001F0EFA: mov rdx, qword ptr [r14]
0x001F0EFD: mov rcx, rbp
0x001F0F00: call 0x140207320
0x001F0F05: jmp 0x1401f0f0a
```
