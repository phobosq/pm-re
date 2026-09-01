# NVIDIA child vtable 0x004BDE70

| slot | target RVA | PDATA |
|---:|---|---|
| `+0x0` | `0x001D5DD0` | `0x001D5DD0..0x001D5E31` |
| `+0x8` | `0x001D7490` | `0x001D7490..0x001D7520` |
| `+0x10` | `0x001E8A10` | `0x001E8A10..0x001E9930` |
| `+0x18` | `0x001E2FE0` | `0x001E2FE0..0x001E3E34` |
| `+0x20` | `0x001E5160` | `0x001E5160..0x001E6C7D` |
| `+0x28` | `0x001E0EC0` | `0x001E0EC0..0x001E1F65` |
| `+0x30` | `0x001E6C80` | `0x001E6C80..0x001E8A0A` |
| `+0x38` | `0x00067840` | none |
| `+0x40` | `0x001E1F70` | `0x001E1F70..0x001E2FD9` |
| `+0x48` | `0x00067840` | none |
| `+0x50` | `0x001DB9E0` | `0x001DB9E0..0x001DBA29` |
| `+0x58` | `0x001DA870` | `0x001DA870..0x001DB9E0` |
| `+0x60` | `0x001D99D0` | `0x001D99D0..0x001DA7A3` |
| `+0x68` | `0x001DBA30` | `0x001DBA30..0x001DC0BF` |
| `+0x70` | `0x001DA7B0` | `0x001DA7B0..0x001DA7FC` |
| `+0x78` | `0x001DE7E0` | `0x001DE7E0..0x001DE7FD` |
| `+0x80` | `0x001DE8B0` | `0x001DE8B0..0x001DF630` |
| `+0x88` | `0x001D9810` | `0x001D9810..0x001D99C7` |

## slot `+0x0` -> `0x001D5DD0`

### Calls

| RVA | target/form |
|---|---|
| `0x001D5DF0` | `call RVA 0x00032EF0` |
| `0x001D5E03` | `call RVA 0x00391A10` |
| `0x001D5E0C` | `call RVA 0x00032EF0` |
| `0x001D5E1E` | `call RVA 0x003B20DC` |

### this-like field accesses

| RVA | instruction |
|---|---|
| `0x001D5DFC` | `lea rcx, [rdi + 0x48]` |
| `0x001D5E08` | `lea rcx, [rdi + 8]` |

## slot `+0x8` -> `0x001D7490`

### Calls

| RVA | target/form |
|---|---|
| `0x001D74F5` | `call RVA 0x0014B790` |
| `0x001D7503` | `call RVA 0x001D6F30` |

### this-like field accesses

| RVA | instruction |
|---|---|
| `0x001D7519` | `mov rcx, qword ptr [rdi + 0xc8]` |

## slot `+0x10` -> `0x001E8A10`

### Calls

| RVA | target/form |
|---|---|
| `0x001E8A5D` | `jmp RVA 0x001E9913` |
| `0x001E8A9F` | `call RVA 0x001ED0B0` |
| `0x001E8B20` | `call qword ptr [rip + 0x5fef9a]` |
| `0x001E8CCD` | `call RVA 0x001EC910` |
| `0x001E8CEA` | `call RVA 0x001D3FC0` |
| `0x001E8D18` | `call RVA 0x003DB020` |
| `0x001E8D27` | `call RVA 0x003DB020` |
| `0x001E8D36` | `call RVA 0x003DB020` |
| `0x001E8D42` | `call RVA 0x003DB020` |
| `0x001E8D4B` | `call RVA 0x003B20D4` |
| `0x001E8D50` | `jmp RVA 0x001E98F8` |
| `0x001E8D8C` | `call qword ptr [rip + 0x5fed36]` |
| `0x001E8F1E` | `call RVA 0x001A4DD0` |
| `0x001E8F3A` | `call RVA 0x0017B170` |
| `0x001E8F47` | `jmp RVA 0x001E98F3` |
| `0x001E9472` | `call RVA 0x001ECAB0` |
| `0x001E9493` | `call RVA 0x0017B330` |
| `0x001E94A0` | `jmp RVA 0x001E98F3` |
| `0x001E98C5` | `call RVA 0x001C5C60` |
| `0x001E98E6` | `call RVA 0x001D43B0` |
| `0x001E98F3` | `call RVA 0x00032EF0` |
| `0x001E9901` | `call RVA 0x001E9930` |
| `0x001E990F` | `jmp RVA 0x001E9913` |
| `0x001E991D` | `call RVA 0x003B24C0` |

### this-like field accesses

| RVA | instruction |
|---|---|
| `0x001E8A46` | `cmp qword ptr [rcx + 0xd0], 0` |
| `0x001E8AA4` | `lea rax, [rdi + 0x13c]` |
| `0x001E8ABC` | `lea rax, [rdi + 0x138]` |
| `0x001E8B19` | `mov rcx, qword ptr [rdi + 0xd0]` |
| `0x001E8D1E` | `mov rax, qword ptr [rcx - 8]` |
| `0x001E8D85` | `mov rcx, qword ptr [rdi + 0xd0]` |
| `0x001E8F2E` | `lea rdx, [rdi + 8]` |
| `0x001E9482` | `lea rdx, [rdi + 8]` |
| `0x001E98D5` | `lea rdx, [rdi + 8]` |

## slot `+0x18` -> `0x001E2FE0`

### Calls

| RVA | target/form |
|---|---|
| `0x001E305B` | `call RVA 0x001ED0B0` |
| `0x001E30B8` | `call qword ptr [rip + 0x604a02]` |
| `0x001E32C9` | `call RVA 0x001EC120` |
| `0x001E32E6` | `call RVA 0x001D3FC0` |
| `0x001E330D` | `call RVA 0x003DB020` |
| `0x001E331C` | `call RVA 0x003DB020` |
| `0x001E332B` | `call RVA 0x003DB020` |
| `0x001E3337` | `call RVA 0x003DB020` |
| `0x001E3340` | `call RVA 0x003B20D4` |
| `0x001E3393` | `call qword ptr [rip + 0x60472f]` |
| `0x001E34F1` | `call RVA 0x001EC1E0` |
| `0x001E350D` | `call RVA 0x0017B170` |
| `0x001E351A` | `jmp RVA 0x001E3DFF` |
| `0x001E3AD1` | `call RVA 0x001EC690` |
| `0x001E3AF2` | `call RVA 0x0017B330` |
| `0x001E3AFF` | `jmp RVA 0x001E3DFF` |
| `0x001E3DD1` | `call RVA 0x001EB8C0` |
| `0x001E3DF2` | `call RVA 0x001D43B0` |
| `0x001E3DFF` | `call RVA 0x00032EF0` |
| `0x001E3E07` | `call RVA 0x001E3E40` |
| `0x001E3E16` | `call RVA 0x003B24C0` |

### this-like field accesses

| RVA | instruction |
|---|---|
| `0x001E301B` | `cmp qword ptr [rcx + 0xd0], 0` |
| `0x001E30B1` | `mov rcx, qword ptr [rbx + 0xd0]` |
| `0x001E3313` | `mov rax, qword ptr [rcx - 8]` |
| `0x001E3379` | `mov eax, dword ptr [rbx + 0x140]` |
| `0x001E338C` | `mov rcx, qword ptr [rbx + 0xd0]` |
| `0x001E33AC` | `imul dword ptr [rbx + 0x140]` |
| `0x001E3501` | `lea rdx, [rbx + 8]` |
| `0x001E351F` | `mov ecx, dword ptr [rbx + 0x140]` |
| `0x001E3AE1` | `lea rdx, [rbx + 8]` |
| `0x001E3DE1` | `lea rdx, [rbx + 8]` |

## slot `+0x20` -> `0x001E5160`

### Calls

| RVA | target/form |
|---|---|
| `0x001E5175` | `call RVA 0x003B2500` |
| `0x001E51D5` | `call RVA 0x003D3050` |
| `0x001E5202` | `call qword ptr [rip + 0x602868]` |
| `0x001E549C` | `call RVA 0x001EC910` |
| `0x001E54B9` | `call RVA 0x001D3FC0` |
| `0x001E54E3` | `call RVA 0x003DB020` |
| `0x001E54F2` | `call RVA 0x003DB020` |
| `0x001E5501` | `call RVA 0x003DB020` |
| `0x001E550D` | `call RVA 0x003DB020` |
| `0x001E5516` | `call RVA 0x003B20D4` |
| `0x001E553C` | `jmp RVA 0x001E5560` |
| `0x001E555B` | `jmp RVA 0x001E59D1` |
| `0x001E594A` | `call RVA 0x001EC840` |
| `0x001E5966` | `call RVA 0x001D4490` |
| `0x001E5994` | `call RVA 0x003DB020` |
| `0x001E59A3` | `call RVA 0x003DB020` |
| `0x001E59B2` | `call RVA 0x003DB020` |
| `0x001E59BE` | `call RVA 0x003DB020` |
| `0x001E59C7` | `call RVA 0x003B20D4` |
| `0x001E59CC` | `jmp RVA 0x001E6C57` |
| `0x001E59E0` | `call RVA 0x003D3050` |
| `0x001E59FD` | `call qword ptr [rip + 0x602095]` |
| `0x001E5A4F` | `jmp RVA 0x001E6627` |
| `0x001E5CA8` | `call qword ptr [rip + 0x601df2]` |
| `0x001E5CC9` | `call qword ptr [rip + 0x601dc9]` |
| `0x001E5D11` | `jmp RVA 0x001E602B` |
| `0x001E5D9E` | `jmp RVA 0x001E5DA8` |
| `0x001E5FFD` | `call RVA 0x0026EBE0` |
| `0x001E6019` | `call RVA 0x0017B170` |
| `0x001E6026` | `jmp RVA 0x001E6C52` |
| `0x001E65F4` | `call RVA 0x001EB300` |
| `0x001E6615` | `call RVA 0x001D43B0` |
| `0x001E6622` | `jmp RVA 0x001E6C52` |
| `0x001E6AC2` | `call RVA 0x001EB660` |
| `0x001E6B2C` | `jmp RVA 0x001E6B31` |
| `0x001E6BD9` | `call RVA 0x00036AD0` |
| `0x001E6C13` | `call RVA 0x0006F540` |
| `0x001E6C2F` | `call RVA 0x000328E0` |
| `0x001E6C38` | `call RVA 0x0004B060` |
| `0x001E6C45` | `call RVA 0x00032DC0` |
| `0x001E6C52` | `call RVA 0x00032EF0` |
| `0x001E6C61` | `call RVA 0x003B24C0` |

### this-like field accesses

| RVA | instruction |
|---|---|
| `0x001E51A6` | `mov rdi, qword ptr [rcx + 0xd0]` |
| `0x001E54E9` | `mov rax, qword ptr [rcx - 8]` |
| `0x001E595A` | `lea rdx, [rsi + 8]` |
| `0x001E599A` | `mov rax, qword ptr [rcx - 8]` |
| `0x001E59F6` | `mov rcx, qword ptr [rsi + 0xd0]` |
| `0x001E5A69` | `cmp dword ptr [rcx + rdx + 8], r15d` |
| `0x001E5BEC` | `movups xmmword ptr [rcx + 0x10], xmm1` |
| `0x001E5BF5` | `movups xmmword ptr [rcx + 0x20], xmm0` |
| `0x001E5BFE` | `movups xmmword ptr [rcx + 0x30], xmm1` |
| `0x001E5C07` | `movups xmmword ptr [rcx + 0x40], xmm0` |
| `0x001E5C10` | `movups xmmword ptr [rcx + 0x50], xmm1` |
| `0x001E5C19` | `movups xmmword ptr [rcx + 0x60], xmm0` |
| `0x001E5C1D` | `lea rcx, [rcx + 0x80]` |
| `0x001E5C29` | `movups xmmword ptr [rcx - 0x10], xmm1` |
| `0x001E5C46` | `movups xmmword ptr [rcx + 0x10], xmm1` |
| `0x001E5C4F` | `movups xmmword ptr [rcx + 0x20], xmm0` |
| `0x001E5C58` | `movups xmmword ptr [rcx + 0x30], xmm1` |
| `0x001E5C60` | `mov qword ptr [rcx + 0x40], rax` |
| `0x001E5CA1` | `mov rcx, qword ptr [rsi + 0xd0]` |
| `0x001E5CC2` | `mov rcx, qword ptr [rsi + 0xd0]` |
| `0x001E5D36` | `cmp dword ptr [rcx + r9 + 8], r15d` |
| `0x001E600D` | `lea rdx, [rsi + 8]` |
| `0x001E6604` | `lea rdx, [rsi + 8]` |
| `0x001E6AD4` | `lea rax, [rsi + 8]` |

## slot `+0x28` -> `0x001E0EC0`

### Calls

| RVA | target/form |
|---|---|
| `0x001E0ED2` | `call RVA 0x003B2500` |
| `0x001E0F26` | `call RVA 0x003D3050` |
| `0x001E0F3F` | `call qword ptr [rip + 0x606b53]` |
| `0x001E0F8F` | `jmp RVA 0x001E1A7A` |
| `0x001E1199` | `call qword ptr [rip + 0x606901]` |
| `0x001E11BA` | `call qword ptr [rip + 0x6068d8]` |
| `0x001E11FF` | `jmp RVA 0x001E1515` |
| `0x001E128D` | `jmp RVA 0x001E1297` |
| `0x001E14E7` | `call RVA 0x001A5360` |
| `0x001E14FE` | `call RVA 0x00063980` |
| `0x001E150B` | `call RVA 0x00032EF0` |
| `0x001E1510` | `jmp RVA 0x001E1F3E` |
| `0x001E1A47` | `call RVA 0x001EB730` |
| `0x001E1A63` | `call RVA 0x001D4490` |
| `0x001E1A70` | `call RVA 0x00032EF0` |
| `0x001E1A75` | `jmp RVA 0x001E1F3E` |
| `0x001E1D54` | `call RVA 0x001EC360` |
| `0x001E1DBC` | `jmp RVA 0x001E1DC1` |
| `0x001E1E6D` | `call RVA 0x00036AD0` |
| `0x001E1EA8` | `call RVA 0x0006F540` |
| `0x001E1EC5` | `call RVA 0x000328E0` |
| `0x001E1ECF` | `call RVA 0x0004B060` |
| `0x001E1EDC` | `call RVA 0x00032DC0` |
| `0x001E1F06` | `call RVA 0x003DB020` |
| `0x001E1F15` | `call RVA 0x003DB020` |
| `0x001E1F24` | `call RVA 0x003DB020` |
| `0x001E1F30` | `call RVA 0x003DB020` |
| `0x001E1F39` | `call RVA 0x003B20D4` |
| `0x001E1F48` | `call RVA 0x003B24C0` |

### this-like field accesses

| RVA | instruction |
|---|---|
| `0x001E0F07` | `mov rbx, qword ptr [rcx + 0xd0]` |
| `0x001E0FA9` | `cmp dword ptr [rcx + rdx + 8], r14d` |
| `0x001E10DC` | `movups xmmword ptr [rcx + 0x10], xmm1` |
| `0x001E10E5` | `movups xmmword ptr [rcx + 0x20], xmm0` |
| `0x001E10EE` | `movups xmmword ptr [rcx + 0x30], xmm1` |
| `0x001E10F7` | `movups xmmword ptr [rcx + 0x40], xmm0` |
| `0x001E1100` | `movups xmmword ptr [rcx + 0x50], xmm1` |
| `0x001E1109` | `movups xmmword ptr [rcx + 0x60], xmm0` |
| `0x001E110D` | `lea rcx, [rcx + 0x80]` |
| `0x001E1119` | `movups xmmword ptr [rcx - 0x10], xmm1` |
| `0x001E1136` | `movups xmmword ptr [rcx + 0x10], xmm1` |
| `0x001E113F` | `movups xmmword ptr [rcx + 0x20], xmm0` |
| `0x001E1148` | `movups xmmword ptr [rcx + 0x30], xmm1` |
| `0x001E1150` | `mov qword ptr [rcx + 0x40], rax` |
| `0x001E1192` | `mov rcx, qword ptr [rsi + 0xd0]` |
| `0x001E11B3` | `mov rcx, qword ptr [rsi + 0xd0]` |
| `0x001E1227` | `cmp dword ptr [rcx + r8 + 8], r14d` |
| `0x001E14F7` | `lea rdx, [rsi + 8]` |
| `0x001E1A57` | `lea rdx, [rsi + 8]` |
| `0x001E1D64` | `lea rcx, [rsi + 8]` |
| `0x001E1DB2` | `cmp qword ptr [rcx + 0x18], 0x10` |
| `0x001E1DC1` | `mov rcx, qword ptr [rcx + 0x10]` |
| `0x001E1F0C` | `mov rax, qword ptr [rcx - 8]` |

## slot `+0x30` -> `0x001E6C80`

### Calls

| RVA | target/form |
|---|---|
| `0x001E6C95` | `call RVA 0x003B2500` |
| `0x001E6CF5` | `call RVA 0x003D3050` |
| `0x001E6D22` | `call qword ptr [rip + 0x600d48]` |
| `0x001E6FBC` | `call RVA 0x001EC910` |
| `0x001E6FD9` | `call RVA 0x001D3FC0` |
| `0x001E7003` | `call RVA 0x003DB020` |
| `0x001E7012` | `call RVA 0x003DB020` |
| `0x001E7021` | `call RVA 0x003DB020` |
| `0x001E702D` | `call RVA 0x003DB020` |
| `0x001E7036` | `call RVA 0x003B20D4` |
| `0x001E705C` | `jmp RVA 0x001E7080` |
| `0x001E707B` | `jmp RVA 0x001E77A5` |
| `0x001E771E` | `call RVA 0x001EB580` |
| `0x001E773A` | `call RVA 0x001D4490` |
| `0x001E7768` | `call RVA 0x003DB020` |
| `0x001E7777` | `call RVA 0x003DB020` |
| `0x001E7786` | `call RVA 0x003DB020` |
| `0x001E7792` | `call RVA 0x003DB020` |
| `0x001E779B` | `call RVA 0x003B20D4` |
| `0x001E77A0` | `jmp RVA 0x001E89E4` |
| `0x001E77C1` | `call RVA 0x003D3050` |
| `0x001E77DE` | `call qword ptr [rip + 0x6002b4]` |
| `0x001E782F` | `jmp RVA 0x001E83B4` |
| `0x001E7A88` | `call qword ptr [rip + 0x600012]` |
| `0x001E7AA9` | `call qword ptr [rip + 0x5fffe9]` |
| `0x001E7AF1` | `jmp RVA 0x001E7FAC` |
| `0x001E7B7F` | `jmp RVA 0x001E7B89` |
| `0x001E7F7E` | `call RVA 0x000DABD0` |
| `0x001E7F9A` | `call RVA 0x0017B170` |
| `0x001E7FA7` | `jmp RVA 0x001E89DF` |
| `0x001E8381` | `call RVA 0x001EC4F0` |
| `0x001E83A2` | `call RVA 0x001D43B0` |
| `0x001E83AF` | `jmp RVA 0x001E89DF` |
| `0x001E884F` | `call RVA 0x001EB660` |
| `0x001E88B9` | `jmp RVA 0x001E88BE` |
| `0x001E8966` | `call RVA 0x00036AD0` |
| `0x001E89A0` | `call RVA 0x0006F540` |
| `0x001E89BC` | `call RVA 0x000328E0` |
| `0x001E89C5` | `call RVA 0x0004B060` |
| `0x001E89D2` | `call RVA 0x00032DC0` |
| `0x001E89DF` | `call RVA 0x00032EF0` |
| `0x001E89EE` | `call RVA 0x003B24C0` |

### this-like field accesses

| RVA | instruction |
|---|---|
| `0x001E6CC6` | `mov rdi, qword ptr [rcx + 0xd0]` |
| `0x001E7009` | `mov rax, qword ptr [rcx - 8]` |
| `0x001E772E` | `lea rdx, [rsi + 8]` |
| `0x001E776E` | `mov rax, qword ptr [rcx - 8]` |
| `0x001E77D7` | `mov rcx, qword ptr [rsi + 0xd0]` |
| `0x001E7849` | `cmp dword ptr [rcx + rdx + 8], 4` |
| `0x001E79CC` | `movups xmmword ptr [rcx + 0x10], xmm1` |
| `0x001E79D5` | `movups xmmword ptr [rcx + 0x20], xmm0` |
| `0x001E79DE` | `movups xmmword ptr [rcx + 0x30], xmm1` |
| `0x001E79E7` | `movups xmmword ptr [rcx + 0x40], xmm0` |
| `0x001E79F0` | `movups xmmword ptr [rcx + 0x50], xmm1` |
| `0x001E79F9` | `movups xmmword ptr [rcx + 0x60], xmm0` |
| `0x001E79FD` | `lea rcx, [rcx + 0x80]` |
| `0x001E7A09` | `movups xmmword ptr [rcx - 0x10], xmm1` |
| `0x001E7A26` | `movups xmmword ptr [rcx + 0x10], xmm1` |
| `0x001E7A2F` | `movups xmmword ptr [rcx + 0x20], xmm0` |
| `0x001E7A38` | `movups xmmword ptr [rcx + 0x30], xmm1` |
| `0x001E7A40` | `mov qword ptr [rcx + 0x40], rax` |
| `0x001E7A81` | `mov rcx, qword ptr [rsi + 0xd0]` |
| `0x001E7AA2` | `mov rcx, qword ptr [rsi + 0xd0]` |
| `0x001E7B16` | `cmp dword ptr [rcx + r9 + 8], 4` |
| `0x001E7F8E` | `lea rdx, [rsi + 8]` |
| `0x001E8391` | `lea rdx, [rsi + 8]` |
| `0x001E8861` | `lea rax, [rsi + 8]` |

## slot `+0x38` -> `0x00067840`

### Calls

| RVA | target/form |
|---|---|
| `0x00067850` | `jmp RVA 0x0006A240` |
| `0x00067899` | `call RVA 0x0006F380` |
| `0x000678DE` | `call RVA 0x0005FA40` |
| `0x0006790B` | `call RVA 0x0006F3F0` |
| `0x0006794E` | `call RVA 0x0005FD40` |
| `0x00067964` | `call RVA 0x0006F460` |
| `0x000679B5` | `call RVA 0x0005FD40` |
| `0x000679CB` | `call RVA 0x0006F460` |
| `0x000679F7` | `call RVA 0x0005FD40` |
| `0x00067A0D` | `call RVA 0x0006F460` |
| `0x00067A2C` | `call RVA 0x00033240` |
| `0x00067A39` | `call RVA 0x003B20DC` |
| `0x00067A45` | `call RVA 0x00391A10` |
| `0x00067A67` | `call RVA 0x0008C100` |
| `0x00067A7E` | `call RVA 0x0006E870` |
| `0x00067A8A` | `call RVA 0x003B20D4` |
| `0x00067AA0` | `call RVA 0x003B20DC` |
| `0x00067AB4` | `call RVA 0x00059280` |
| `0x00067AC1` | `call RVA 0x003B20DC` |
| `0x00067ADF` | `call qword ptr [rax + 0x20]` |
| `0x00067AED` | `call RVA 0x00391E10` |
| `0x00067AF9` | `call RVA 0x00391A10` |
| `0x00067B38` | `call RVA 0x00241B80` |

### this-like field accesses

| RVA | instruction |
|---|---|
| `0x00067994` | `lea rbx, [rcx + 0x1688]` |

## slot `+0x40` -> `0x001E1F70`

### Calls

| RVA | target/form |
|---|---|
| `0x001E1F82` | `call RVA 0x003B2500` |
| `0x001E1FD6` | `call RVA 0x003D3050` |
| `0x001E1FEF` | `call qword ptr [rip + 0x605aa3]` |
| `0x001E203F` | `jmp RVA 0x001E2AE3` |
| `0x001E2249` | `call qword ptr [rip + 0x605851]` |
| `0x001E226A` | `call qword ptr [rip + 0x605828]` |
| `0x001E22AF` | `jmp RVA 0x001E2770` |
| `0x001E233E` | `jmp RVA 0x001E2348` |
| `0x001E2742` | `call RVA 0x001A3280` |
| `0x001E2759` | `call RVA 0x00063980` |
| `0x001E2766` | `call RVA 0x00032EF0` |
| `0x001E276B` | `jmp RVA 0x001E2FB2` |
| `0x001E2AB0` | `call RVA 0x0026ED80` |
| `0x001E2ACC` | `call RVA 0x001D4490` |
| `0x001E2AD9` | `call RVA 0x00032EF0` |
| `0x001E2ADE` | `jmp RVA 0x001E2FB2` |
| `0x001E2DC8` | `call RVA 0x002152F0` |
| `0x001E2E30` | `jmp RVA 0x001E2E35` |
| `0x001E2EE1` | `call RVA 0x00036AD0` |
| `0x001E2F1C` | `call RVA 0x0006F540` |
| `0x001E2F39` | `call RVA 0x000328E0` |
| `0x001E2F43` | `call RVA 0x0004B060` |
| `0x001E2F50` | `call RVA 0x00032DC0` |
| `0x001E2F7A` | `call RVA 0x003DB020` |
| `0x001E2F89` | `call RVA 0x003DB020` |
| `0x001E2F98` | `call RVA 0x003DB020` |
| `0x001E2FA4` | `call RVA 0x003DB020` |
| `0x001E2FAD` | `call RVA 0x003B20D4` |
| `0x001E2FBC` | `call RVA 0x003B24C0` |

### this-like field accesses

| RVA | instruction |
|---|---|
| `0x001E1FB7` | `mov rbx, qword ptr [rcx + 0xd0]` |
| `0x001E2059` | `cmp dword ptr [rcx + rdx + 8], 4` |
| `0x001E218C` | `movups xmmword ptr [rcx + 0x10], xmm1` |
| `0x001E2195` | `movups xmmword ptr [rcx + 0x20], xmm0` |
| `0x001E219E` | `movups xmmword ptr [rcx + 0x30], xmm1` |
| `0x001E21A7` | `movups xmmword ptr [rcx + 0x40], xmm0` |
| `0x001E21B0` | `movups xmmword ptr [rcx + 0x50], xmm1` |
| `0x001E21B9` | `movups xmmword ptr [rcx + 0x60], xmm0` |
| `0x001E21BD` | `lea rcx, [rcx + 0x80]` |
| `0x001E21C9` | `movups xmmword ptr [rcx - 0x10], xmm1` |
| `0x001E21E6` | `movups xmmword ptr [rcx + 0x10], xmm1` |
| `0x001E21EF` | `movups xmmword ptr [rcx + 0x20], xmm0` |
| `0x001E21F8` | `movups xmmword ptr [rcx + 0x30], xmm1` |
| `0x001E2200` | `mov qword ptr [rcx + 0x40], rax` |
| `0x001E2242` | `mov rcx, qword ptr [rsi + 0xd0]` |
| `0x001E2263` | `mov rcx, qword ptr [rsi + 0xd0]` |
| `0x001E22D7` | `cmp dword ptr [rcx + r8 + 8], 4` |
| `0x001E2752` | `lea rdx, [rsi + 8]` |
| `0x001E2AC0` | `lea rdx, [rsi + 8]` |
| `0x001E2DD8` | `lea rcx, [rsi + 8]` |
| `0x001E2E26` | `cmp qword ptr [rcx + 0x18], 0x10` |
| `0x001E2E35` | `mov rcx, qword ptr [rcx + 0x10]` |
| `0x001E2F80` | `mov rax, qword ptr [rcx - 8]` |

## slot `+0x48` -> `0x00067840`

### Calls

| RVA | target/form |
|---|---|
| `0x00067850` | `jmp RVA 0x0006A240` |
| `0x00067899` | `call RVA 0x0006F380` |
| `0x000678DE` | `call RVA 0x0005FA40` |
| `0x0006790B` | `call RVA 0x0006F3F0` |
| `0x0006794E` | `call RVA 0x0005FD40` |
| `0x00067964` | `call RVA 0x0006F460` |
| `0x000679B5` | `call RVA 0x0005FD40` |
| `0x000679CB` | `call RVA 0x0006F460` |
| `0x000679F7` | `call RVA 0x0005FD40` |
| `0x00067A0D` | `call RVA 0x0006F460` |
| `0x00067A2C` | `call RVA 0x00033240` |
| `0x00067A39` | `call RVA 0x003B20DC` |
| `0x00067A45` | `call RVA 0x00391A10` |
| `0x00067A67` | `call RVA 0x0008C100` |
| `0x00067A7E` | `call RVA 0x0006E870` |
| `0x00067A8A` | `call RVA 0x003B20D4` |
| `0x00067AA0` | `call RVA 0x003B20DC` |
| `0x00067AB4` | `call RVA 0x00059280` |
| `0x00067AC1` | `call RVA 0x003B20DC` |
| `0x00067ADF` | `call qword ptr [rax + 0x20]` |
| `0x00067AED` | `call RVA 0x00391E10` |
| `0x00067AF9` | `call RVA 0x00391A10` |
| `0x00067B38` | `call RVA 0x00241B80` |

### this-like field accesses

| RVA | instruction |
|---|---|
| `0x00067994` | `lea rbx, [rcx + 0x1688]` |

## slot `+0x50` -> `0x001DB9E0`

### Calls

| RVA | target/form |
|---|---|
| `0x001DB9FD` | `call RVA 0x001D61A0` |
| `0x001DBA0B` | `call RVA 0x001E9930` |
| `0x001DBA17` | `call RVA 0x00408D10` |

### this-like field accesses

| RVA | instruction |
|---|---|
| `0x001DB9EA` | `cmp qword ptr [rcx + 0xd0], 0` |
| `0x001DBA10` | `lea rcx, [rbx + 0xe8]` |

## slot `+0x58` -> `0x001DA870`

### Calls

| RVA | target/form |
|---|---|
| `0x001DA92B` | `call RVA 0x003D3050` |
| `0x001DA93E` | `call rbx` |
| `0x001DABEF` | `call RVA 0x001A3280` |
| `0x001DAC0C` | `call RVA 0x001D3FC0` |
| `0x001DAC36` | `call RVA 0x003DB020` |
| `0x001DAC45` | `call RVA 0x003DB020` |
| `0x001DAC54` | `call RVA 0x003DB020` |
| `0x001DAC60` | `call RVA 0x003DB020` |
| `0x001DAC69` | `call RVA 0x003B20D4` |
| `0x001DAC8B` | `jmp RVA 0x001DB06D` |
| `0x001DACB1` | `jmp RVA 0x001DB053` |
| `0x001DACC5` | `call RVA 0x003D3050` |
| `0x001DACE7` | `call qword ptr [rip + 0x60cd4b]` |
| `0x001DAF9C` | `call RVA 0x001A3280` |
| `0x001DAFB9` | `call RVA 0x001D3FC0` |
| `0x001DAFE3` | `call RVA 0x003DB020` |
| `0x001DAFF2` | `call RVA 0x003DB020` |
| `0x001DB001` | `call RVA 0x003DB020` |
| `0x001DB00D` | `call RVA 0x003DB020` |
| `0x001DB016` | `call RVA 0x003B20D4` |
| `0x001DB038` | `jmp RVA 0x001DB06D` |
| `0x001DB1E7` | `call RVA 0x001EB800` |
| `0x001DB20B` | `call RVA 0x0002ECF0` |
| `0x001DB217` | `call RVA 0x00043F90` |
| `0x001DB240` | `call RVA 0x003DB020` |
| `0x001DB24F` | `call RVA 0x003DB020` |
| `0x001DB25E` | `call RVA 0x003DB020` |
| `0x001DB26A` | `call RVA 0x003DB020` |
| `0x001DB273` | `call RVA 0x003B20D4` |
| `0x001DB2B5` | `call RVA 0x003DB020` |
| `0x001DB2C4` | `call RVA 0x003DB020` |
| `0x001DB2D3` | `call RVA 0x003DB020` |
| `0x001DB2DF` | `call RVA 0x003DB020` |
| `0x001DB2E8` | `call RVA 0x003B20D4` |
| `0x001DB3E6` | `call RVA 0x0027E5D0` |
| `0x001DB409` | `call RVA 0x0002ECF0` |
| `0x001DB41D` | `call RVA 0x00035230` |
| `0x001DB447` | `call RVA 0x003DB020` |
| `0x001DB456` | `call RVA 0x003DB020` |
| `0x001DB465` | `call RVA 0x003DB020` |
| `0x001DB471` | `call RVA 0x003DB020` |
| `0x001DB47A` | `call RVA 0x003B20D4` |
| `0x001DB49F` | `call RVA 0x00032EF0` |
| `0x001DB57E` | `call RVA 0x001EC2A0` |
| `0x001DB5A1` | `call RVA 0x0002ECF0` |
| `0x001DB5B5` | `call RVA 0x00035230` |
| `0x001DB5C2` | `call RVA 0x00032EF0` |
| `0x001DB5CF` | `call RVA 0x00032EF0` |
| `0x001DB908` | `call RVA 0x000B2C20` |
| `0x001DB932` | `call RVA 0x0017B6F0` |
| `0x001DB93F` | `call RVA 0x00032EF0` |
| `0x001DB949` | `call RVA 0x00032EF0` |
| `0x001DB965` | `call RVA 0x00408CE0` |
| `0x001DB975` | `call RVA 0x00408CF0` |
| `0x001DB985` | `call RVA 0x00408D00` |
| `0x001DB997` | `call RVA 0x00408CD0` |
| `0x001DB9A3` | `call RVA 0x00408D20` |
| `0x001DB9B5` | `call RVA 0x001E9930` |
| `0x001DB9C9` | `call RVA 0x003B24C0` |

### this-like field accesses

| RVA | instruction |
|---|---|
| `0x001DA8EB` | `cmp byte ptr [rdi + 0x28], r12b` |
| `0x001DA8F5` | `cmp byte ptr [rdi + 0xd8], r12b` |
| `0x001DA937` | `mov rcx, qword ptr [rdi + 0xd0]` |
| `0x001DAC3C` | `mov rax, qword ptr [rcx - 8]` |
| `0x001DACE0` | `mov rcx, qword ptr [rdi + 0xd0]` |
| `0x001DAFE9` | `mov rax, qword ptr [rcx - 8]` |
| `0x001DB0B1` | `cmp byte ptr [rdi + 0x108], 0` |
| `0x001DB0BA` | `cmp dword ptr [rdi + 0x114], esi` |
| `0x001DB0C2` | `mov eax, dword ptr [rdi + 0x120]` |
| `0x001DB0CE` | `mov eax, dword ptr [rdi + 0x12c]` |
| `0x001DB0DA` | `cmp dword ptr [rdi + 0x10c], r14d` |
| `0x001DB0E3` | `cmp dword ptr [rdi + 0x110], r15d` |
| `0x001DB246` | `mov rax, qword ptr [rcx - 8]` |
| `0x001DB2BB` | `mov rax, qword ptr [rcx - 8]` |
| `0x001DB44D` | `mov rax, qword ptr [rcx - 8]` |
| `0x001DB918` | `lea rdx, [rdi + 8]` |
| `0x001DB95E` | `lea rcx, [rdi + 0xe8]` |
| `0x001DB96E` | `lea rcx, [rdi + 0xe8]` |
| `0x001DB97E` | `lea rcx, [rdi + 0xe8]` |
| `0x001DB990` | `lea rcx, [rdi + 0xe8]` |
| `0x001DB99C` | `lea rcx, [rdi + 0xe8]` |

## slot `+0x60` -> `0x001D99D0`

### Calls

| RVA | target/form |
|---|---|
| `0x001D9A66` | `call RVA 0x003D3050` |
| `0x001D9A79` | `call rbx` |
| `0x001D9AC6` | `call qword ptr [rip + 0x60e01c]` |
| `0x001D9AD2` | `jmp RVA 0x001DA25A` |
| `0x001D9AE6` | `call RVA 0x003D3050` |
| `0x001D9B08` | `call qword ptr [rip + 0x60df2a]` |
| `0x001D9CF3` | `call RVA 0x001EBC80` |
| `0x001D9D10` | `call RVA 0x001D3FC0` |
| `0x001D9D34` | `call RVA 0x003DB020` |
| `0x001D9D43` | `call RVA 0x003DB020` |
| `0x001D9D52` | `call RVA 0x003DB020` |
| `0x001D9D5E` | `call RVA 0x003DB020` |
| `0x001D9D67` | `call RVA 0x003B20D4` |
| `0x001D9D80` | `jmp RVA 0x001D9FF1` |
| `0x001D9DBA` | `call qword ptr [rip + 0x60dc80]` |
| `0x001D9F5B` | `call RVA 0x0026DE30` |
| `0x001D9F78` | `call RVA 0x001D3FC0` |
| `0x001D9F9F` | `call RVA 0x003DB020` |
| `0x001D9FAE` | `call RVA 0x003DB020` |
| `0x001D9FBD` | `call RVA 0x003DB020` |
| `0x001D9FC9` | `call RVA 0x003DB020` |
| `0x001D9FD2` | `call RVA 0x003B20D4` |
| `0x001DA011` | `call rax` |
| `0x001DA1BA` | `call RVA 0x001EC910` |
| `0x001DA1D7` | `call RVA 0x001D3FC0` |
| `0x001DA201` | `call RVA 0x003DB020` |
| `0x001DA210` | `call RVA 0x003DB020` |
| `0x001DA21F` | `call RVA 0x003DB020` |
| `0x001DA22B` | `call RVA 0x003DB020` |
| `0x001DA234` | `call RVA 0x003B20D4` |
| `0x001DA33B` | `call RVA 0x001EC9E0` |
| `0x001DA352` | `call RVA 0x00063980` |
| `0x001DA380` | `call RVA 0x003DB020` |
| `0x001DA38F` | `call RVA 0x003DB020` |
| `0x001DA39E` | `call RVA 0x003DB020` |
| `0x001DA3AA` | `call RVA 0x003DB020` |
| `0x001DA3B3` | `call RVA 0x003B20D4` |
| `0x001DA3B8` | `jmp RVA 0x001DA773` |
| `0x001DA745` | `call RVA 0x001EB660` |
| `0x001DA761` | `call RVA 0x001D4490` |
| `0x001DA76E` | `call RVA 0x00032EF0` |
| `0x001DA776` | `call RVA 0x001E3E40` |
| `0x001DA785` | `call RVA 0x003B24C0` |

### this-like field accesses

| RVA | instruction |
|---|---|
| `0x001D9A0B` | `cmp qword ptr [rcx + 0xd0], 0` |
| `0x001D9A23` | `cmp byte ptr [rcx + 0xd8], r14b` |
| `0x001D9A72` | `mov rcx, qword ptr [rdi + 0xd0]` |
| `0x001D9ABF` | `mov rcx, qword ptr [rdi + 0xd0]` |
| `0x001D9B01` | `mov rcx, qword ptr [rdi + 0xd0]` |
| `0x001D9D3A` | `mov rax, qword ptr [rcx - 8]` |
| `0x001D9DB3` | `mov rcx, qword ptr [rdi + 0xd0]` |
| `0x001D9FA5` | `mov rax, qword ptr [rcx - 8]` |
| `0x001DA00A` | `mov rcx, qword ptr [rdi + 0xd0]` |
| `0x001DA207` | `mov rax, qword ptr [rcx - 8]` |
| `0x001DA34B` | `lea rdx, [rdi + 8]` |
| `0x001DA386` | `mov rax, qword ptr [rcx - 8]` |
| `0x001DA755` | `lea rdx, [rdi + 8]` |

## slot `+0x68` -> `0x001DBA30`

### Calls

| RVA | target/form |
|---|---|
| `0x001DBA96` | `jmp RVA 0x001DBA9B` |
| `0x001DBAD8` | `jmp RVA 0x001DBADC` |
| `0x001DBB55` | `jmp RVA 0x001DC09A` |
| `0x001DBD2E` | `call RVA 0x000B27F0` |
| `0x001DBD57` | `call RVA 0x0003F680` |
| `0x001DBF55` | `call RVA 0x001C5B90` |
| `0x001DBF6F` | `call RVA 0x00160690` |
| `0x001DBF93` | `call RVA 0x003DB020` |
| `0x001DBFA2` | `call RVA 0x003DB020` |
| `0x001DBFB1` | `call RVA 0x003DB020` |
| `0x001DBFBD` | `call RVA 0x003DB020` |
| `0x001DBFC6` | `call RVA 0x003B20D4` |
| `0x001DBFF9` | `call RVA 0x003DB020` |
| `0x001DC008` | `call RVA 0x003DB020` |
| `0x001DC017` | `call RVA 0x003DB020` |
| `0x001DC023` | `call RVA 0x003DB020` |
| `0x001DC02C` | `call RVA 0x003B20D4` |
| `0x001DC05F` | `call RVA 0x003DB020` |
| `0x001DC06E` | `call RVA 0x003DB020` |
| `0x001DC07D` | `call RVA 0x003DB020` |
| `0x001DC089` | `call RVA 0x003DB020` |
| `0x001DC092` | `call RVA 0x003B20D4` |
| `0x001DC0A1` | `call RVA 0x003B24C0` |

### this-like field accesses

| RVA | instruction |
|---|---|
| `0x001DBA69` | `cmp byte ptr [rcx + 0x26c], sil` |
| `0x001DBA79` | `mov ecx, dword ptr [rcx + 0x39c]` |
| `0x001DBA9B` | `mov dword ptr [rbx + 0x3a0], eax` |
| `0x001DBAA1` | `cmp dword ptr [rbx + 0x3a0], esi` |
| `0x001DBAAD` | `cmp dword ptr [rbx + 0x258], edx` |
| `0x001DBAB5` | `cmp dword ptr [rbx + 0x25c], r8d` |
| `0x001DBABE` | `mov rax, qword ptr [rbx + 0x260]` |
| `0x001DBACA` | `mov eax, dword ptr [rbx + 0x268]` |
| `0x001DBADC` | `mov dword ptr [rbx + 0x258], edx` |
| `0x001DBAE2` | `mov dword ptr [rbx + 0x25c], r8d` |
| `0x001DBAEE` | `movsd qword ptr [rbx + 0x260], xmm0` |
| `0x001DBAFA` | `mov dword ptr [rbx + 0x268], eax` |
| `0x001DBB09` | `mov dword ptr [rbx + 0x258], edx` |
| `0x001DBB13` | `lea rax, [rbx + 0x398]` |
| `0x001DBB5A` | `mov ecx, dword ptr [rbx + 0x278]` |
| `0x001DBB60` | `lea eax, [rcx + 1]` |
| `0x001DBB63` | `mov dword ptr [rbx + 0x278], eax` |
| `0x001DBD49` | `lea r8, [rbx + 0x39c]` |
| `0x001DBF65` | `lea rdx, [rbx + 8]` |
| `0x001DBF99` | `mov rax, qword ptr [rcx - 8]` |
| `0x001DBFFF` | `mov rax, qword ptr [rcx - 8]` |
| `0x001DC065` | `mov rax, qword ptr [rcx - 8]` |

## slot `+0x70` -> `0x001DA7B0`

### Calls

| RVA | target/form |
|---|---|
| `0x001DA7E6` | `jmp RVA 0x001DA7EB` |

### this-like field accesses

| RVA | instruction |
|---|---|
| `0x001DA7B6` | `cmp byte ptr [rcx + 0x26c], 0` |
| `0x001DA7C2` | `mov ecx, dword ptr [rcx + 0x39c]` |
| `0x001DA7EB` | `mov dword ptr [rbx + 0x3a0], eax` |
| `0x001DA7F1` | `cmp dword ptr [rbx + 0x3a0], 0` |

## slot `+0x78` -> `0x001DE7E0`

### Calls

| RVA | target/form |
|---|---|

### this-like field accesses

| RVA | instruction |
|---|---|
| `0x001DE7E6` | `cmp byte ptr [rcx + 0x108], 0` |

## slot `+0x80` -> `0x001DE8B0`

### Calls

| RVA | target/form |
|---|---|
| `0x001DE90E` | `call rax` |
| `0x001DE91C` | `jmp RVA 0x001DE951` |
| `0x001DE943` | `call rax` |
| `0x001DE99E` | `jmp RVA 0x001DF608` |
| `0x001DE9C7` | `call RVA 0x001E0CA0` |
| `0x001DF189` | `call RVA 0x001EB4A0` |
| `0x001DF1A0` | `call RVA 0x00040530` |
| `0x001DF1AA` | `jmp RVA 0x001DF603` |
| `0x001DF223` | `call RVA 0x001D97E0` |
| `0x001DF246` | `call RVA 0x001ECB90` |
| `0x001DF3EA` | `call RVA 0x000DCDD0` |
| `0x001DF401` | `call RVA 0x00040530` |
| `0x001DF40E` | `jmp RVA 0x001DF603` |
| `0x001DF420` | `call RVA 0x001D7930` |
| `0x001DF43E` | `call RVA 0x001ECB90` |
| `0x001DF5DF` | `call RVA 0x000DCDD0` |
| `0x001DF5F6` | `call RVA 0x00040530` |
| `0x001DF603` | `call RVA 0x00032EF0` |
| `0x001DF612` | `call RVA 0x003B24C0` |

### this-like field accesses

| RVA | instruction |
|---|---|
| `0x001DE907` | `mov rcx, qword ptr [rcx + 0xd0]` |
| `0x001DE91E` | `mov rcx, qword ptr [rcx + 0xc8]` |
| `0x001DE95A` | `mov eax, dword ptr [rbx + 0x274]` |
| `0x001DE968` | `mov dword ptr [rbx + 0x274], edi` |
| `0x001DE96E` | `movsxd rax, dword ptr [rbx + 0x270]` |
| `0x001DE987` | `mov dword ptr [rbx + 0x278], ecx` |
| `0x001DE98D` | `mov dword ptr [rbx + 0x270], edi` |
| `0x001DE998` | `mov dword ptr [rbx + 0x27c], ecx` |
| `0x001DE9A8` | `mov ecx, dword ptr [rbx + 0x27c]` |
| `0x001DE9AE` | `lea eax, [rcx + 1]` |
| `0x001DE9B1` | `mov dword ptr [rbx + 0x27c], eax` |
| `0x001DE9D4` | `mov ecx, dword ptr [rbx + 0x278]` |
| `0x001DE9DA` | `lea eax, [rcx + 1]` |
| `0x001DE9DD` | `mov dword ptr [rbx + 0x278], eax` |
| `0x001DF199` | `lea rdx, [rbx + 8]` |
| `0x001DF1B6` | `lea rsi, [rbx + 0x144]` |
| `0x001DF1C5` | `cmp byte ptr [rcx + rbx + 0x280], 0` |
| `0x001DF206` | `cmp dword ptr [rbx + 0x258], 0` |
| `0x001DF213` | `cmp dword ptr [rbx + 0x25c], 0` |
| `0x001DF253` | `mov ecx, dword ptr [rbx + 0x278]` |
| `0x001DF259` | `lea eax, [rcx + 1]` |
| `0x001DF25C` | `mov dword ptr [rbx + 0x278], eax` |
| `0x001DF3FA` | `lea rdx, [rbx + 8]` |
| `0x001DF44B` | `mov ecx, dword ptr [rbx + 0x278]` |
| `0x001DF451` | `lea eax, [rcx + 1]` |
| `0x001DF454` | `mov dword ptr [rbx + 0x278], eax` |
| `0x001DF5EF` | `lea rdx, [rbx + 8]` |

## slot `+0x88` -> `0x001D9810`

### Calls

| RVA | target/form |
|---|---|
| `0x001D9887` | `call RVA 0x003D3050` |
| `0x001D98A8` | `call rsi` |
| `0x001D98C2` | `call qword ptr [rip + 0x60e248]` |
| `0x001D98D6` | `jmp RVA 0x001D98EE` |
| `0x001D98E2` | `jmp RVA 0x001D98EE` |
| `0x001D9905` | `call RVA 0x003D3050` |
| `0x001D9922` | `call qword ptr [rip + 0x60e1e8]` |
| `0x001D9970` | `call RVA 0x001D9490` |
| `0x001D99AA` | `call RVA 0x003B24C0` |

### this-like field accesses

| RVA | instruction |
|---|---|
| `0x001D9857` | `cmp dword ptr [rcx + 0x3a4], -1` |
| `0x001D9870` | `cmp qword ptr [rcx + 0xd0], 0` |
| `0x001D988C` | `mov rcx, qword ptr [rdi + 0xd0]` |
| `0x001D98AE` | `mov rcx, qword ptr [rdi + 0xd0]` |
| `0x001D98CC` | `mov dword ptr [rdi + 0x3a4], 0` |
| `0x001D98DC` | `mov dword ptr [rdi + 0x3a4], eax` |
| `0x001D98E4` | `mov dword ptr [rcx + 0x3a4], 0` |
| `0x001D98EE` | `mov esi, dword ptr [rdi + 0x3a4]` |
| `0x001D990A` | `mov rcx, qword ptr [rdi + 0xd0]` |