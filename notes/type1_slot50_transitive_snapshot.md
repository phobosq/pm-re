# AMD Type1 slot +0x50 transitive snapshot trace

PDATA `0x001688D0..0x001694C0`

## Getter calls

| call | output local |
|---|---|
| `0x001689B0` | `rsp+0x1a0` |
| `0x001690C2` | `rsp+0x280` |

## Timing-shaped accesses to plausible snapshot locals

| RVA | base | record offset | label | instruction |
|---|---|---:|---|---|
| `0x00168C63` | `rsp+0x2c8` (inferred) | `+0x98` | mt | `mov dword ptr [rsp + 0x360], 0x34` |
| `0x00168C6E` | `rsp+0x2c8` (inferred) | `+0x98` | mt | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168C8B` | `rsp+0x2c8` (inferred) | `+0x98` | mt | `mov ecx, dword ptr [rsp + 0x360]` |
| `0x00168CA6` | `rsp+0x2c8` (inferred) | `+0x98` | mt | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168CC3` | `rsp+0x2c8` (inferred) | `+0x98` | mt | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168CE0` | `rsp+0x2c8` (inferred) | `+0x98` | mt | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168CFD` | `rsp+0x2c8` (inferred) | `+0x98` | mt | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168D1A` | `rsp+0x2c8` (inferred) | `+0x98` | mt | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168D37` | `rsp+0x2c8` (inferred) | `+0x98` | mt | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168D54` | `rsp+0x2c8` (inferred) | `+0x98` | mt | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168D71` | `rsp+0x2c8` (inferred) | `+0x98` | mt | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168D8E` | `rsp+0x2c8` (inferred) | `+0x98` | mt | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168DAB` | `rsp+0x2c8` (inferred) | `+0x98` | mt | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168DC8` | `rsp+0x2c8` (inferred) | `+0x98` | mt | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168DE5` | `rsp+0x2c8` (inferred) | `+0x98` | mt | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168DF3` | `rsp+0x2c8` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x374], al` |
| `0x00168DFA` | `rsp+0x2c8` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x374]` |
| `0x00168E02` | `rsp+0x2c8` (inferred) | `+0x98` | mt | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168E1F` | `rsp+0x2c8` (inferred) | `+0x98` | mt | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168E3C` | `rsp+0x2c8` (inferred) | `+0x98` | mt | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168E59` | `rsp+0x2c8` (inferred) | `+0x98` | mt | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168E67` | `rsp+0x2c8` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x378], al` |
| `0x00168E6E` | `rsp+0x2c8` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x378]` |
| `0x00168E76` | `rsp+0x2c8` (inferred) | `+0x98` | mt | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168E93` | `rsp+0x2c8` (inferred) | `+0x98` | mt | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168EB0` | `rsp+0x2c8` (inferred) | `+0x98` | mt | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168ECD` | `rsp+0x2c8` (inferred) | `+0x98` | mt | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168EEA` | `rsp+0x2c8` (inferred) | `+0x98` | mt | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168F07` | `rsp+0x2c8` (inferred) | `+0x98` | mt | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168F24` | `rsp+0x2c8` (inferred) | `+0x98` | mt | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168F41` | `rsp+0x2c8` (inferred) | `+0x98` | mt | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168F4F` | `rsp+0x2c8` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x380], al` |
| `0x00168F56` | `rsp+0x2c8` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x380]` |
| `0x00168F5E` | `rsp+0x2c8` (inferred) | `+0x98` | mt | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168F7B` | `rsp+0x2c8` (inferred) | `+0x98` | mt | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168F98` | `rsp+0x2c8` (inferred) | `+0x98` | mt | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168FB5` | `rsp+0x2c8` (inferred) | `+0x98` | mt | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168FC3` | `rsp+0x2c8` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x384], al` |
| `0x00168FE3` | `rsp+0x2c8` (inferred) | `+0x98` | mt | `lea rcx, [rsp + 0x360]` |
| `0x00168C63` | `rsp+0x2b4` (inferred) | `+0xAC` | straps | `mov dword ptr [rsp + 0x360], 0x34` |
| `0x00168C6E` | `rsp+0x2b4` (inferred) | `+0xAC` | straps | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168C7D` | `rsp+0x2b4` (inferred) | `+0xB0` | vmr/rxboost | `mov dword ptr [rsp + 0x364], ecx` |
| `0x00168C84` | `rsp+0x2b4` (inferred) | `+0xB0` | vmr/rxboost | `mov eax, dword ptr [rsp + 0x364]` |
| `0x00168C8B` | `rsp+0x2b4` (inferred) | `+0xAC` | straps | `mov ecx, dword ptr [rsp + 0x360]` |
| `0x00168CA6` | `rsp+0x2b4` (inferred) | `+0xAC` | straps | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168CC3` | `rsp+0x2b4` (inferred) | `+0xAC` | straps | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168CE0` | `rsp+0x2b4` (inferred) | `+0xAC` | straps | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168CFD` | `rsp+0x2b4` (inferred) | `+0xAC` | straps | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168D0B` | `rsp+0x2b4` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x36c], al` |
| `0x00168D12` | `rsp+0x2b4` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x36c]` |
| `0x00168D1A` | `rsp+0x2b4` (inferred) | `+0xAC` | straps | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168D37` | `rsp+0x2b4` (inferred) | `+0xAC` | straps | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168D54` | `rsp+0x2b4` (inferred) | `+0xAC` | straps | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168D71` | `rsp+0x2b4` (inferred) | `+0xAC` | straps | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168D7F` | `rsp+0x2b4` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x370], al` |
| `0x00168D86` | `rsp+0x2b4` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x370]` |
| `0x00168D8E` | `rsp+0x2b4` (inferred) | `+0xAC` | straps | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168DAB` | `rsp+0x2b4` (inferred) | `+0xAC` | straps | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168DC8` | `rsp+0x2b4` (inferred) | `+0xAC` | straps | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168DE5` | `rsp+0x2b4` (inferred) | `+0xAC` | straps | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168E02` | `rsp+0x2b4` (inferred) | `+0xAC` | straps | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168E1F` | `rsp+0x2b4` (inferred) | `+0xAC` | straps | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168E3C` | `rsp+0x2b4` (inferred) | `+0xAC` | straps | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168E59` | `rsp+0x2b4` (inferred) | `+0xAC` | straps | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168E76` | `rsp+0x2b4` (inferred) | `+0xAC` | straps | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168E93` | `rsp+0x2b4` (inferred) | `+0xAC` | straps | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168EB0` | `rsp+0x2b4` (inferred) | `+0xAC` | straps | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168ECD` | `rsp+0x2b4` (inferred) | `+0xAC` | straps | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168EEA` | `rsp+0x2b4` (inferred) | `+0xAC` | straps | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168F07` | `rsp+0x2b4` (inferred) | `+0xAC` | straps | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168F24` | `rsp+0x2b4` (inferred) | `+0xAC` | straps | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168F41` | `rsp+0x2b4` (inferred) | `+0xAC` | straps | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168F5E` | `rsp+0x2b4` (inferred) | `+0xAC` | straps | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168F7B` | `rsp+0x2b4` (inferred) | `+0xAC` | straps | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168F98` | `rsp+0x2b4` (inferred) | `+0xAC` | straps | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168FB5` | `rsp+0x2b4` (inferred) | `+0xAC` | straps | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168FE3` | `rsp+0x2b4` (inferred) | `+0xAC` | straps | `lea rcx, [rsp + 0x360]` |
| `0x00168C63` | `rsp+0x2b0` (inferred) | `+0xB0` | vmr/rxboost | `mov dword ptr [rsp + 0x360], 0x34` |
| `0x00168C6E` | `rsp+0x2b0` (inferred) | `+0xB0` | vmr/rxboost | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168C8B` | `rsp+0x2b0` (inferred) | `+0xB0` | vmr/rxboost | `mov ecx, dword ptr [rsp + 0x360]` |
| `0x00168C97` | `rsp+0x2b0` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x368], cl` |
| `0x00168C9E` | `rsp+0x2b0` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x368]` |
| `0x00168CA6` | `rsp+0x2b0` (inferred) | `+0xB0` | vmr/rxboost | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168CC3` | `rsp+0x2b0` (inferred) | `+0xB0` | vmr/rxboost | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168CE0` | `rsp+0x2b0` (inferred) | `+0xB0` | vmr/rxboost | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168CFD` | `rsp+0x2b0` (inferred) | `+0xB0` | vmr/rxboost | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168D0B` | `rsp+0x2b0` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x36c], al` |
| `0x00168D12` | `rsp+0x2b0` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x36c]` |
| `0x00168D1A` | `rsp+0x2b0` (inferred) | `+0xB0` | vmr/rxboost | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168D37` | `rsp+0x2b0` (inferred) | `+0xB0` | vmr/rxboost | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168D54` | `rsp+0x2b0` (inferred) | `+0xB0` | vmr/rxboost | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168D71` | `rsp+0x2b0` (inferred) | `+0xB0` | vmr/rxboost | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168D8E` | `rsp+0x2b0` (inferred) | `+0xB0` | vmr/rxboost | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168DAB` | `rsp+0x2b0` (inferred) | `+0xB0` | vmr/rxboost | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168DC8` | `rsp+0x2b0` (inferred) | `+0xB0` | vmr/rxboost | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168DE5` | `rsp+0x2b0` (inferred) | `+0xB0` | vmr/rxboost | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168E02` | `rsp+0x2b0` (inferred) | `+0xB0` | vmr/rxboost | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168E1F` | `rsp+0x2b0` (inferred) | `+0xB0` | vmr/rxboost | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168E3C` | `rsp+0x2b0` (inferred) | `+0xB0` | vmr/rxboost | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168E59` | `rsp+0x2b0` (inferred) | `+0xB0` | vmr/rxboost | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168E76` | `rsp+0x2b0` (inferred) | `+0xB0` | vmr/rxboost | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168E93` | `rsp+0x2b0` (inferred) | `+0xB0` | vmr/rxboost | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168EB0` | `rsp+0x2b0` (inferred) | `+0xB0` | vmr/rxboost | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168ECD` | `rsp+0x2b0` (inferred) | `+0xB0` | vmr/rxboost | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168EEA` | `rsp+0x2b0` (inferred) | `+0xB0` | vmr/rxboost | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168F07` | `rsp+0x2b0` (inferred) | `+0xB0` | vmr/rxboost | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168F24` | `rsp+0x2b0` (inferred) | `+0xB0` | vmr/rxboost | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168F41` | `rsp+0x2b0` (inferred) | `+0xB0` | vmr/rxboost | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168F5E` | `rsp+0x2b0` (inferred) | `+0xB0` | vmr/rxboost | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168F7B` | `rsp+0x2b0` (inferred) | `+0xB0` | vmr/rxboost | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168F98` | `rsp+0x2b0` (inferred) | `+0xB0` | vmr/rxboost | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168FB5` | `rsp+0x2b0` (inferred) | `+0xB0` | vmr/rxboost | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168FD3` | `rsp+0x2b0` (inferred) | `+0xB8` | vmt2 | `movzx eax, byte ptr [rsp + 0x368]` |
| `0x00168FE3` | `rsp+0x2b0` (inferred) | `+0xB0` | vmr/rxboost | `lea rcx, [rsp + 0x360]` |
| `0x00168C63` | `rsp+0x2a8` (inferred) | `+0xB8` | vmt2 | `mov dword ptr [rsp + 0x360], 0x34` |
| `0x00168C6E` | `rsp+0x2a8` (inferred) | `+0xB8` | vmt2 | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168C7D` | `rsp+0x2a8` (inferred) | `+0xBC` | vmt3 | `mov dword ptr [rsp + 0x364], ecx` |
| `0x00168C84` | `rsp+0x2a8` (inferred) | `+0xBC` | vmt3 | `mov eax, dword ptr [rsp + 0x364]` |
| `0x00168C8B` | `rsp+0x2a8` (inferred) | `+0xB8` | vmt2 | `mov ecx, dword ptr [rsp + 0x360]` |
| `0x00168CA6` | `rsp+0x2a8` (inferred) | `+0xB8` | vmt2 | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168CC3` | `rsp+0x2a8` (inferred) | `+0xB8` | vmt2 | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168CE0` | `rsp+0x2a8` (inferred) | `+0xB8` | vmt2 | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168CFD` | `rsp+0x2a8` (inferred) | `+0xB8` | vmt2 | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168D1A` | `rsp+0x2a8` (inferred) | `+0xB8` | vmt2 | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168D37` | `rsp+0x2a8` (inferred) | `+0xB8` | vmt2 | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168D54` | `rsp+0x2a8` (inferred) | `+0xB8` | vmt2 | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168D71` | `rsp+0x2a8` (inferred) | `+0xB8` | vmt2 | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168D8E` | `rsp+0x2a8` (inferred) | `+0xB8` | vmt2 | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168DAB` | `rsp+0x2a8` (inferred) | `+0xB8` | vmt2 | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168DC8` | `rsp+0x2a8` (inferred) | `+0xB8` | vmt2 | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168DE5` | `rsp+0x2a8` (inferred) | `+0xB8` | vmt2 | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168E02` | `rsp+0x2a8` (inferred) | `+0xB8` | vmt2 | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168E1F` | `rsp+0x2a8` (inferred) | `+0xB8` | vmt2 | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168E3C` | `rsp+0x2a8` (inferred) | `+0xB8` | vmt2 | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168E59` | `rsp+0x2a8` (inferred) | `+0xB8` | vmt2 | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168E76` | `rsp+0x2a8` (inferred) | `+0xB8` | vmt2 | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168E93` | `rsp+0x2a8` (inferred) | `+0xB8` | vmt2 | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168EB0` | `rsp+0x2a8` (inferred) | `+0xB8` | vmt2 | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168ECD` | `rsp+0x2a8` (inferred) | `+0xB8` | vmt2 | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168EEA` | `rsp+0x2a8` (inferred) | `+0xB8` | vmt2 | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168F07` | `rsp+0x2a8` (inferred) | `+0xB8` | vmt2 | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168F24` | `rsp+0x2a8` (inferred) | `+0xB8` | vmt2 | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168F41` | `rsp+0x2a8` (inferred) | `+0xB8` | vmt2 | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168F5E` | `rsp+0x2a8` (inferred) | `+0xB8` | vmt2 | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168F7B` | `rsp+0x2a8` (inferred) | `+0xB8` | vmt2 | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168F98` | `rsp+0x2a8` (inferred) | `+0xB8` | vmt2 | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168FB5` | `rsp+0x2a8` (inferred) | `+0xB8` | vmt2 | `mov eax, dword ptr [rsp + 0x360]` |
| `0x00168FE3` | `rsp+0x2a8` (inferred) | `+0xB8` | vmt2 | `lea rcx, [rsp + 0x360]` |
| `0x00168C7D` | `rsp+0x2b8` (inferred) | `+0xAC` | straps | `mov dword ptr [rsp + 0x364], ecx` |
| `0x00168C84` | `rsp+0x2b8` (inferred) | `+0xAC` | straps | `mov eax, dword ptr [rsp + 0x364]` |
| `0x00168C97` | `rsp+0x2b8` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x368], cl` |
| `0x00168C9E` | `rsp+0x2b8` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x368]` |
| `0x00168D7F` | `rsp+0x2b8` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x370], al` |
| `0x00168D86` | `rsp+0x2b8` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x370]` |
| `0x00168DF3` | `rsp+0x2b8` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x374], al` |
| `0x00168DFA` | `rsp+0x2b8` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x374]` |
| `0x00168FD3` | `rsp+0x2b8` (inferred) | `+0xB0` | vmr/rxboost | `movzx eax, byte ptr [rsp + 0x368]` |
| `0x00168C97` | `rsp+0x2bc` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x368], cl` |
| `0x00168C9E` | `rsp+0x2bc` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x368]` |
| `0x00168D0B` | `rsp+0x2bc` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x36c], al` |
| `0x00168D12` | `rsp+0x2bc` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x36c]` |
| `0x00168DF3` | `rsp+0x2bc` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x374], al` |
| `0x00168DFA` | `rsp+0x2bc` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x374]` |
| `0x00168E67` | `rsp+0x2bc` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x378], al` |
| `0x00168E6E` | `rsp+0x2bc` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x378]` |
| `0x00168FD3` | `rsp+0x2bc` (inferred) | `+0xAC` | straps | `movzx eax, byte ptr [rsp + 0x368]` |
| `0x001691AC` | `rsp+0x308` (inferred) | `+0xAC` | straps | `mov dword ptr [rsp + 0x3b4], 0x2a` |
| `0x001691B7` | `rsp+0x308` (inferred) | `+0xAC` | straps | `mov eax, dword ptr [rsp + 0x3b4]` |
| `0x001691C1` | `rsp+0x308` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x3b8], al` |
| `0x001691C8` | `rsp+0x308` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x3b8]` |
| `0x00169251` | `rsp+0x308` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x3c0], cl` |
| `0x00169258` | `rsp+0x308` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x3c0]` |
| `0x00169299` | `rsp+0x308` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x3c4], cl` |
| `0x001692A0` | `rsp+0x308` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x3c4]` |
| `0x00169393` | `rsp+0x308` (inferred) | `+0xB0` | vmr/rxboost | `movzx eax, byte ptr [rsp + 0x3b8]` |
| `0x001691C1` | `rsp+0x30c` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x3b8], al` |
| `0x001691C8` | `rsp+0x30c` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x3b8]` |
| `0x00169209` | `rsp+0x30c` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x3bc], cl` |
| `0x00169210` | `rsp+0x30c` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x3bc]` |
| `0x00169299` | `rsp+0x30c` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x3c4], cl` |
| `0x001692A0` | `rsp+0x30c` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x3c4]` |
| `0x001692E1` | `rsp+0x30c` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x3c8], cl` |
| `0x001692E8` | `rsp+0x30c` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x3c8]` |
| `0x00169393` | `rsp+0x30c` (inferred) | `+0xAC` | straps | `movzx eax, byte ptr [rsp + 0x3b8]` |
| `0x00168CB4` | `rsp+0x2bd` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x369], al` |
| `0x00168CBB` | `rsp+0x2bd` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x369]` |
| `0x00168D28` | `rsp+0x2bd` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x36d], al` |
| `0x00168D2F` | `rsp+0x2bd` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x36d]` |
| `0x00168E10` | `rsp+0x2bd` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x375], al` |
| `0x00168E17` | `rsp+0x2bd` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x375]` |
| `0x00168E84` | `rsp+0x2bd` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x379], al` |
| `0x00168E8B` | `rsp+0x2bd` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x379]` |
| `0x00168CD1` | `rsp+0x2be` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x36a], al` |
| `0x00168CD8` | `rsp+0x2be` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x36a]` |
| `0x00168D45` | `rsp+0x2be` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x36e], al` |
| `0x00168D4C` | `rsp+0x2be` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x36e]` |
| `0x00168E2D` | `rsp+0x2be` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x376], al` |
| `0x00168E34` | `rsp+0x2be` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x376]` |
| `0x00168EA1` | `rsp+0x2be` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x37a], al` |
| `0x00168EA8` | `rsp+0x2be` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x37a]` |
| `0x00168CEE` | `rsp+0x2bf` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x36b], al` |
| `0x00168CF5` | `rsp+0x2bf` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x36b]` |
| `0x00168D62` | `rsp+0x2bf` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x36f], al` |
| `0x00168D69` | `rsp+0x2bf` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x36f]` |
| `0x00168E4A` | `rsp+0x2bf` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x377], al` |
| `0x00168E51` | `rsp+0x2bf` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x377]` |
| `0x00168EBE` | `rsp+0x2bf` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x37b], al` |
| `0x00168EC5` | `rsp+0x2bf` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x37b]` |
| `0x00168D0B` | `rsp+0x2c0` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x36c], al` |
| `0x00168D12` | `rsp+0x2c0` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x36c]` |
| `0x00168D7F` | `rsp+0x2c0` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x370], al` |
| `0x00168D86` | `rsp+0x2c0` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x370]` |
| `0x00168E67` | `rsp+0x2c0` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x378], al` |
| `0x00168E6E` | `rsp+0x2c0` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x378]` |
| `0x00168EDB` | `rsp+0x2c0` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x37c], al` |
| `0x00168EE2` | `rsp+0x2c0` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x37c]` |
| `0x00168D28` | `rsp+0x2c1` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x36d], al` |
| `0x00168D2F` | `rsp+0x2c1` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x36d]` |
| `0x00168D9C` | `rsp+0x2c1` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x371], al` |
| `0x00168DA3` | `rsp+0x2c1` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x371]` |
| `0x00168E84` | `rsp+0x2c1` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x379], al` |
| `0x00168E8B` | `rsp+0x2c1` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x379]` |
| `0x00168EF8` | `rsp+0x2c1` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x37d], al` |
| `0x00168EFF` | `rsp+0x2c1` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x37d]` |
| `0x00168D45` | `rsp+0x2c2` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x36e], al` |
| `0x00168D4C` | `rsp+0x2c2` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x36e]` |
| `0x00168DB9` | `rsp+0x2c2` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x372], al` |
| `0x00168DC0` | `rsp+0x2c2` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x372]` |
| `0x00168EA1` | `rsp+0x2c2` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x37a], al` |
| `0x00168EA8` | `rsp+0x2c2` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x37a]` |
| `0x00168F15` | `rsp+0x2c2` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x37e], al` |
| `0x00168F1C` | `rsp+0x2c2` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x37e]` |
| `0x00168D62` | `rsp+0x2c3` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x36f], al` |
| `0x00168D69` | `rsp+0x2c3` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x36f]` |
| `0x00168DD6` | `rsp+0x2c3` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x373], al` |
| `0x00168DDD` | `rsp+0x2c3` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x373]` |
| `0x00168EBE` | `rsp+0x2c3` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x37b], al` |
| `0x00168EC5` | `rsp+0x2c3` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x37b]` |
| `0x00168F32` | `rsp+0x2c3` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x37f], al` |
| `0x00168F39` | `rsp+0x2c3` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x37f]` |
| `0x00168D7F` | `rsp+0x2c4` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x370], al` |
| `0x00168D86` | `rsp+0x2c4` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x370]` |
| `0x00168DF3` | `rsp+0x2c4` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x374], al` |
| `0x00168DFA` | `rsp+0x2c4` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x374]` |
| `0x00168EDB` | `rsp+0x2c4` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x37c], al` |
| `0x00168EE2` | `rsp+0x2c4` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x37c]` |
| `0x00168F4F` | `rsp+0x2c4` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x380], al` |
| `0x00168F56` | `rsp+0x2c4` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x380]` |
| `0x00168D9C` | `rsp+0x2c5` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x371], al` |
| `0x00168DA3` | `rsp+0x2c5` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x371]` |
| `0x00168E10` | `rsp+0x2c5` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x375], al` |
| `0x00168E17` | `rsp+0x2c5` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x375]` |
| `0x00168EF8` | `rsp+0x2c5` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x37d], al` |
| `0x00168EFF` | `rsp+0x2c5` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x37d]` |
| `0x00168F6C` | `rsp+0x2c5` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x381], al` |
| `0x00168F73` | `rsp+0x2c5` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x381]` |
| `0x00168DB9` | `rsp+0x2c6` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x372], al` |
| `0x00168DC0` | `rsp+0x2c6` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x372]` |
| `0x00168E2D` | `rsp+0x2c6` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x376], al` |
| `0x00168E34` | `rsp+0x2c6` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x376]` |
| `0x00168F15` | `rsp+0x2c6` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x37e], al` |
| `0x00168F1C` | `rsp+0x2c6` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x37e]` |
| `0x00168F89` | `rsp+0x2c6` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x382], al` |
| `0x00168F90` | `rsp+0x2c6` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x382]` |
| `0x00168DD6` | `rsp+0x2c7` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x373], al` |
| `0x00168DDD` | `rsp+0x2c7` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x373]` |
| `0x00168E4A` | `rsp+0x2c7` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x377], al` |
| `0x00168E51` | `rsp+0x2c7` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x377]` |
| `0x00168F32` | `rsp+0x2c7` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x37f], al` |
| `0x00168F39` | `rsp+0x2c7` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x37f]` |
| `0x00168FA6` | `rsp+0x2c7` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x383], al` |
| `0x00168FAD` | `rsp+0x2c7` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x383]` |
| `0x00169002` | `rsp+0x10` (inferred) | `+0xB0` | vmr/rxboost | `mov qword ptr [rsp + 0xc0], rcx` |
| `0x0016900C` | `rsp+0x10` (inferred) | `+0xB8` | vmt2 | `mov qword ptr [rsp + 0xc8], rcx` |
| `0x0016902C` | `rsp+0x10` (inferred) | `+0xB8` | vmt2 | `lea rdx, [rsp + 0xc8]` |
| `0x00169048` | `rsp+0x10` (inferred) | `+0xB0` | vmr/rxboost | `mov qword ptr [rsp + 0xc0], rax` |
| `0x00169057` | `rsp+0x10` (inferred) | `+0xB0` | vmr/rxboost | `lea rcx, [rsp + 0xc0]` |
| `0x001693C2` | `rsp+0x10` (inferred) | `+0x98` | mt | `mov qword ptr [rsp + 0xa8], rcx` |
| `0x00169408` | `rsp+0x10` (inferred) | `+0x98` | mt | `mov qword ptr [rsp + 0xa8], rax` |
| `0x00169417` | `rsp+0x10` (inferred) | `+0x98` | mt | `lea rcx, [rsp + 0xa8]` |
| `0x001691A1` | `rsp+0x318` (inferred) | `+0x98` | mt | `mov dword ptr [rsp + 0x3b0], 0x14` |
| `0x00169299` | `rsp+0x318` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x3c4], cl` |
| `0x001692A0` | `rsp+0x318` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x3c4]` |
| `0x001692E1` | `rsp+0x318` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x3c8], cl` |
| `0x001692E8` | `rsp+0x318` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x3c8]` |
| `0x00169371` | `rsp+0x318` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x3d0], cl` |
| `0x00169378` | `rsp+0x318` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x3d0]` |
| `0x001693A3` | `rsp+0x318` (inferred) | `+0x98` | mt | `lea rcx, [rsp + 0x3b0]` |
| `0x001691A1` | `rsp+0x304` (inferred) | `+0xAC` | straps | `mov dword ptr [rsp + 0x3b0], 0x14` |
| `0x001691AC` | `rsp+0x304` (inferred) | `+0xB0` | vmr/rxboost | `mov dword ptr [rsp + 0x3b4], 0x2a` |
| `0x001691B7` | `rsp+0x304` (inferred) | `+0xB0` | vmr/rxboost | `mov eax, dword ptr [rsp + 0x3b4]` |
| `0x00169209` | `rsp+0x304` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x3bc], cl` |
| `0x00169210` | `rsp+0x304` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x3bc]` |
| `0x00169251` | `rsp+0x304` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x3c0], cl` |
| `0x00169258` | `rsp+0x304` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x3c0]` |
| `0x001693A3` | `rsp+0x304` (inferred) | `+0xAC` | straps | `lea rcx, [rsp + 0x3b0]` |
| `0x001691D3` | `rsp+0x30d` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x3b9], cl` |
| `0x001691DA` | `rsp+0x30d` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x3b9]` |
| `0x0016921B` | `rsp+0x30d` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x3bd], cl` |
| `0x00169222` | `rsp+0x30d` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x3bd]` |
| `0x001692AB` | `rsp+0x30d` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x3c5], cl` |
| `0x001692B2` | `rsp+0x30d` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x3c5]` |
| `0x001692F3` | `rsp+0x30d` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x3c9], cl` |
| `0x001692FA` | `rsp+0x30d` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x3c9]` |
| `0x001691E5` | `rsp+0x30e` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x3ba], cl` |
| `0x001691EC` | `rsp+0x30e` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x3ba]` |
| `0x0016922D` | `rsp+0x30e` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x3be], cl` |
| `0x00169234` | `rsp+0x30e` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x3be]` |
| `0x001692BD` | `rsp+0x30e` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x3c6], cl` |
| `0x001692C4` | `rsp+0x30e` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x3c6]` |
| `0x00169305` | `rsp+0x30e` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x3ca], cl` |
| `0x0016930C` | `rsp+0x30e` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x3ca]` |
| `0x001691F7` | `rsp+0x30f` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x3bb], cl` |
| `0x001691FE` | `rsp+0x30f` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x3bb]` |
| `0x0016923F` | `rsp+0x30f` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x3bf], cl` |
| `0x00169246` | `rsp+0x30f` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x3bf]` |
| `0x001692CF` | `rsp+0x30f` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x3c7], cl` |
| `0x001692D6` | `rsp+0x30f` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x3c7]` |
| `0x00169317` | `rsp+0x30f` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x3cb], cl` |
| `0x0016931E` | `rsp+0x30f` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x3cb]` |
| `0x00169209` | `rsp+0x310` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x3bc], cl` |
| `0x00169210` | `rsp+0x310` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x3bc]` |
| `0x00169251` | `rsp+0x310` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x3c0], cl` |
| `0x00169258` | `rsp+0x310` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x3c0]` |
| `0x001692E1` | `rsp+0x310` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x3c8], cl` |
| `0x001692E8` | `rsp+0x310` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x3c8]` |
| `0x00169329` | `rsp+0x310` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x3cc], cl` |
| `0x00169330` | `rsp+0x310` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x3cc]` |
| `0x0016921B` | `rsp+0x311` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x3bd], cl` |
| `0x00169222` | `rsp+0x311` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x3bd]` |
| `0x00169263` | `rsp+0x311` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x3c1], cl` |
| `0x0016926A` | `rsp+0x311` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x3c1]` |
| `0x001692F3` | `rsp+0x311` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x3c9], cl` |
| `0x001692FA` | `rsp+0x311` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x3c9]` |
| `0x0016933B` | `rsp+0x311` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x3cd], cl` |
| `0x00169342` | `rsp+0x311` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x3cd]` |
| `0x0016922D` | `rsp+0x312` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x3be], cl` |
| `0x00169234` | `rsp+0x312` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x3be]` |
| `0x00169275` | `rsp+0x312` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x3c2], cl` |
| `0x0016927C` | `rsp+0x312` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x3c2]` |
| `0x00169305` | `rsp+0x312` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x3ca], cl` |
| `0x0016930C` | `rsp+0x312` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x3ca]` |
| `0x0016934D` | `rsp+0x312` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x3ce], cl` |
| `0x00169354` | `rsp+0x312` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x3ce]` |
| `0x0016923F` | `rsp+0x313` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x3bf], cl` |
| `0x00169246` | `rsp+0x313` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x3bf]` |
| `0x00169287` | `rsp+0x313` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x3c3], cl` |
| `0x0016928E` | `rsp+0x313` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x3c3]` |
| `0x00169317` | `rsp+0x313` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x3cb], cl` |
| `0x0016931E` | `rsp+0x313` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x3cb]` |
| `0x0016935F` | `rsp+0x313` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x3cf], cl` |
| `0x00169366` | `rsp+0x313` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x3cf]` |
| `0x00169251` | `rsp+0x314` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x3c0], cl` |
| `0x00169258` | `rsp+0x314` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x3c0]` |
| `0x00169299` | `rsp+0x314` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x3c4], cl` |
| `0x001692A0` | `rsp+0x314` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x3c4]` |
| `0x00169329` | `rsp+0x314` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x3cc], cl` |
| `0x00169330` | `rsp+0x314` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x3cc]` |
| `0x00169371` | `rsp+0x314` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x3d0], cl` |
| `0x00169378` | `rsp+0x314` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x3d0]` |
| `0x0016892C` | `rsp-0x48` (inferred) | `+0x98` | mt | `mov byte ptr [rsp + 0x50], al` |
| `0x00168AE1` | `rsp-0x48` (inferred) | `+0xB8` | vmt2 | `mov qword ptr [rsp + 0x70], rax` |
| `0x00168B47` | `rsp-0x48` (inferred) | `+0xB0` | vmr/rxboost | `mov qword ptr [rsp + 0x68], rdx` |
| `0x00168BB7` | `rsp-0x48` (inferred) | `+0xB0` | vmr/rxboost | `lea rax, [rsp + 0x68]` |
| `0x00168BF0` | `rsp-0x48` (inferred) | `+0xB8` | vmt2 | `lea rdx, [rsp + 0x70]` |
| `0x00168C01` | `rsp-0x48` (inferred) | `+0xB8` | vmt2 | `mov rdi, qword ptr [rsp + 0x70]` |
| `0x00168C06` | `rsp-0x48` (inferred) | `+0xB0` | vmr/rxboost | `mov rdx, qword ptr [rsp + 0x68]` |
| `0x00168AA5` | `rsp-0x40` (inferred) | `+0x98` | mt | `mov dword ptr [rsp + 0x58], eax` |
| `0x00168AE1` | `rsp-0x40` (inferred) | `+0xB0` | vmr/rxboost | `mov qword ptr [rsp + 0x70], rax` |
| `0x00168BF0` | `rsp-0x40` (inferred) | `+0xB0` | vmr/rxboost | `lea rdx, [rsp + 0x70]` |
| `0x00168C01` | `rsp-0x40` (inferred) | `+0xB0` | vmr/rxboost | `mov rdi, qword ptr [rsp + 0x70]` |
| `0x00168C32` | `rsp-0x40` (inferred) | `+0x98` | mt | `mov eax, dword ptr [rsp + 0x58]` |
| `0x0016918B` | `rsp-0x40` (inferred) | `+0xB8` | vmt2 | `mov qword ptr [rsp + 0x78], rax` |
| `0x00169197` | `rsp-0x40` (inferred) | `+0xB8` | vmt2 | `lea rcx, [rsp + 0x78]` |
| `0x00168AB7` | `rsp+0x28` (inferred) | `+0xB0` | vmr/rxboost | `mov qword ptr [rsp + 0xd8], rbx` |
| `0x00168ABF` | `rsp+0x28` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0xe0], 0` |
| `0x00168ACF` | `rsp+0x28` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0xe0], 1` |
| `0x00168B3B` | `rsp+0x28` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0xe0], 0` |
| `0x00169002` | `rsp+0x28` (inferred) | `+0x98` | mt | `mov qword ptr [rsp + 0xc0], rcx` |
| `0x00169048` | `rsp+0x28` (inferred) | `+0x98` | mt | `mov qword ptr [rsp + 0xc0], rax` |
| `0x00169057` | `rsp+0x28` (inferred) | `+0x98` | mt | `lea rcx, [rsp + 0xc0]` |
| `0x00168BBC` | `rsp-0x8` (inferred) | `+0x98` | mt | `mov qword ptr [rsp + 0x90], rax` |
| `0x00168BC9` | `rsp-0x8` (inferred) | `+0x98` | mt | `lea r8, [rsp + 0x90]` |
| `0x001693C2` | `rsp-0x8` (inferred) | `+0xB0` | vmr/rxboost | `mov qword ptr [rsp + 0xa8], rcx` |
| `0x001693CC` | `rsp-0x8` (inferred) | `+0xB8` | vmt2 | `mov qword ptr [rsp + 0xb0], rcx` |
| `0x001693EC` | `rsp-0x8` (inferred) | `+0xB8` | vmt2 | `lea rdx, [rsp + 0xb0]` |
| `0x00169408` | `rsp-0x8` (inferred) | `+0xB0` | vmr/rxboost | `mov qword ptr [rsp + 0xa8], rax` |
| `0x00169417` | `rsp-0x8` (inferred) | `+0xB0` | vmr/rxboost | `lea rcx, [rsp + 0xa8]` |
| `0x00168C7D` | `rsp+0x2cc` (inferred) | `+0x98` | mt | `mov dword ptr [rsp + 0x364], ecx` |
| `0x00168C84` | `rsp+0x2cc` (inferred) | `+0x98` | mt | `mov eax, dword ptr [rsp + 0x364]` |
| `0x00168E67` | `rsp+0x2cc` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x378], al` |
| `0x00168E6E` | `rsp+0x2cc` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x378]` |
| `0x00168EDB` | `rsp+0x2cc` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x37c], al` |
| `0x00168EE2` | `rsp+0x2cc` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x37c]` |
| `0x00168FC3` | `rsp+0x2cc` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x384], al` |
| `0x00168C97` | `rsp+0x2d0` (inferred) | `+0x98` | mt | `mov byte ptr [rsp + 0x368], cl` |
| `0x00168C9E` | `rsp+0x2d0` (inferred) | `+0x98` | mt | `movsx ecx, byte ptr [rsp + 0x368]` |
| `0x00168EDB` | `rsp+0x2d0` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x37c], al` |
| `0x00168EE2` | `rsp+0x2d0` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x37c]` |
| `0x00168F4F` | `rsp+0x2d0` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x380], al` |
| `0x00168F56` | `rsp+0x2d0` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x380]` |
| `0x00168FD3` | `rsp+0x2d0` (inferred) | `+0x98` | mt | `movzx eax, byte ptr [rsp + 0x368]` |
| `0x00168E10` | `rsp+0x2c9` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x375], al` |
| `0x00168E17` | `rsp+0x2c9` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x375]` |
| `0x00168E84` | `rsp+0x2c9` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x379], al` |
| `0x00168E8B` | `rsp+0x2c9` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x379]` |
| `0x00168F6C` | `rsp+0x2c9` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x381], al` |
| `0x00168F73` | `rsp+0x2c9` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x381]` |
| `0x00168FCC` | `rsp+0x2c9` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x385], al` |
| `0x001691A1` | `rsp+0x300` (inferred) | `+0xB0` | vmr/rxboost | `mov dword ptr [rsp + 0x3b0], 0x14` |
| `0x001691C1` | `rsp+0x300` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x3b8], al` |
| `0x001691C8` | `rsp+0x300` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x3b8]` |
| `0x00169209` | `rsp+0x300` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x3bc], cl` |
| `0x00169210` | `rsp+0x300` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x3bc]` |
| `0x00169393` | `rsp+0x300` (inferred) | `+0xB8` | vmt2 | `movzx eax, byte ptr [rsp + 0x3b8]` |
| `0x001693A3` | `rsp+0x300` (inferred) | `+0xB0` | vmr/rxboost | `lea rcx, [rsp + 0x3b0]` |
| `0x001691C1` | `rsp+0x320` (inferred) | `+0x98` | mt | `mov byte ptr [rsp + 0x3b8], al` |
| `0x001691C8` | `rsp+0x320` (inferred) | `+0x98` | mt | `movsx ecx, byte ptr [rsp + 0x3b8]` |
| `0x00169329` | `rsp+0x320` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x3cc], cl` |
| `0x00169330` | `rsp+0x320` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x3cc]` |
| `0x00169371` | `rsp+0x320` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x3d0], cl` |
| `0x00169378` | `rsp+0x320` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x3d0]` |
| `0x00169393` | `rsp+0x320` (inferred) | `+0x98` | mt | `movzx eax, byte ptr [rsp + 0x3b8]` |
| `0x00169263` | `rsp+0x315` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x3c1], cl` |
| `0x0016926A` | `rsp+0x315` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x3c1]` |
| `0x001692AB` | `rsp+0x315` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x3c5], cl` |
| `0x001692B2` | `rsp+0x315` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x3c5]` |
| `0x0016933B` | `rsp+0x315` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x3cd], cl` |
| `0x00169342` | `rsp+0x315` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x3cd]` |
| `0x00169383` | `rsp+0x315` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x3d1], cl` |
| `0x00169275` | `rsp+0x316` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x3c2], cl` |
| `0x0016927C` | `rsp+0x316` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x3c2]` |
| `0x001692BD` | `rsp+0x316` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x3c6], cl` |
| `0x001692C4` | `rsp+0x316` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x3c6]` |
| `0x0016934D` | `rsp+0x316` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x3ce], cl` |
| `0x00169354` | `rsp+0x316` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x3ce]` |
| `0x0016938C` | `rsp+0x316` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x3d2], al` |
| `0x0016890B` | `rsp-0x58` (inferred) | `+0xB8` | vmt2 | `mov qword ptr [rsp + 0x60], rdx` |
| `0x00168AA5` | `rsp-0x58` (inferred) | `+0xB0` | vmr/rxboost | `mov dword ptr [rsp + 0x58], eax` |
| `0x00168BC4` | `rsp-0x58` (inferred) | `+0xAC` | straps | `lea r9, [rsp + 0x54]` |
| `0x00168C29` | `rsp-0x58` (inferred) | `+0x98` | mt | `mov dword ptr [rsp + 0x40], eax` |
| `0x00168C32` | `rsp-0x58` (inferred) | `+0xB0` | vmr/rxboost | `mov eax, dword ptr [rsp + 0x58]` |
| `0x0016942D` | `rsp-0x58` (inferred) | `+0xB8` | vmt2 | `mov rax, qword ptr [rsp + 0x60]` |
| `0x00168AE1` | `rsp-0x28` (inferred) | `+0x98` | mt | `mov qword ptr [rsp + 0x70], rax` |
| `0x00168BBC` | `rsp-0x28` (inferred) | `+0xB8` | vmt2 | `mov qword ptr [rsp + 0x90], rax` |
| `0x00168BC9` | `rsp-0x28` (inferred) | `+0xB8` | vmt2 | `lea r8, [rsp + 0x90]` |
| `0x00168BF0` | `rsp-0x28` (inferred) | `+0x98` | mt | `lea rdx, [rsp + 0x70]` |
| `0x00168C01` | `rsp-0x28` (inferred) | `+0x98` | mt | `mov rdi, qword ptr [rsp + 0x70]` |
| `0x0016917C` | `rsp-0x28` (inferred) | `+0xB0` | vmr/rxboost | `mov qword ptr [rsp + 0x88], rax` |
| `0x00168B47` | `rsp-0x44` (inferred) | `+0xAC` | straps | `mov qword ptr [rsp + 0x68], rdx` |
| `0x00168BB7` | `rsp-0x44` (inferred) | `+0xAC` | straps | `lea rax, [rsp + 0x68]` |
| `0x00168BC4` | `rsp-0x44` (inferred) | `+0x98` | mt | `lea r9, [rsp + 0x54]` |
| `0x00168C06` | `rsp-0x44` (inferred) | `+0xAC` | straps | `mov rdx, qword ptr [rsp + 0x68]` |
| `0x0016918B` | `rsp-0x44` (inferred) | `+0xBC` | vmt3 | `mov qword ptr [rsp + 0x78], rax` |
| `0x00169197` | `rsp-0x44` (inferred) | `+0xBC` | vmt3 | `lea rcx, [rsp + 0x78]` |
| `0x00168CB4` | `rsp+0x2d1` (inferred) | `+0x98` | mt | `mov byte ptr [rsp + 0x369], al` |
| `0x00168CBB` | `rsp+0x2d1` (inferred) | `+0x98` | mt | `movsx ecx, byte ptr [rsp + 0x369]` |
| `0x00168EF8` | `rsp+0x2d1` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x37d], al` |
| `0x00168EFF` | `rsp+0x2d1` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x37d]` |
| `0x00168F6C` | `rsp+0x2d1` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x381], al` |
| `0x00168F73` | `rsp+0x2d1` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x381]` |
| `0x00168CB4` | `rsp+0x2b9` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x369], al` |
| `0x00168CBB` | `rsp+0x2b9` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x369]` |
| `0x00168D9C` | `rsp+0x2b9` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x371], al` |
| `0x00168DA3` | `rsp+0x2b9` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x371]` |
| `0x00168E10` | `rsp+0x2b9` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x375], al` |
| `0x00168E17` | `rsp+0x2b9` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x375]` |
| `0x00168CD1` | `rsp+0x2d2` (inferred) | `+0x98` | mt | `mov byte ptr [rsp + 0x36a], al` |
| `0x00168CD8` | `rsp+0x2d2` (inferred) | `+0x98` | mt | `movsx ecx, byte ptr [rsp + 0x36a]` |
| `0x00168F15` | `rsp+0x2d2` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x37e], al` |
| `0x00168F1C` | `rsp+0x2d2` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x37e]` |
| `0x00168F89` | `rsp+0x2d2` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x382], al` |
| `0x00168F90` | `rsp+0x2d2` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x382]` |
| `0x00168CD1` | `rsp+0x2ba` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x36a], al` |
| `0x00168CD8` | `rsp+0x2ba` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x36a]` |
| `0x00168DB9` | `rsp+0x2ba` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x372], al` |
| `0x00168DC0` | `rsp+0x2ba` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x372]` |
| `0x00168E2D` | `rsp+0x2ba` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x376], al` |
| `0x00168E34` | `rsp+0x2ba` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x376]` |
| `0x00168CEE` | `rsp+0x2d3` (inferred) | `+0x98` | mt | `mov byte ptr [rsp + 0x36b], al` |
| `0x00168CF5` | `rsp+0x2d3` (inferred) | `+0x98` | mt | `movsx ecx, byte ptr [rsp + 0x36b]` |
| `0x00168F32` | `rsp+0x2d3` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x37f], al` |
| `0x00168F39` | `rsp+0x2d3` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x37f]` |
| `0x00168FA6` | `rsp+0x2d3` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x383], al` |
| `0x00168FAD` | `rsp+0x2d3` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x383]` |
| `0x00168CEE` | `rsp+0x2bb` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x36b], al` |
| `0x00168CF5` | `rsp+0x2bb` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x36b]` |
| `0x00168DD6` | `rsp+0x2bb` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x373], al` |
| `0x00168DDD` | `rsp+0x2bb` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x373]` |
| `0x00168E4A` | `rsp+0x2bb` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x377], al` |
| `0x00168E51` | `rsp+0x2bb` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x377]` |
| `0x00168E2D` | `rsp+0x2ca` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x376], al` |
| `0x00168E34` | `rsp+0x2ca` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x376]` |
| `0x00168EA1` | `rsp+0x2ca` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x37a], al` |
| `0x00168EA8` | `rsp+0x2ca` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x37a]` |
| `0x00168F89` | `rsp+0x2ca` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x382], al` |
| `0x00168F90` | `rsp+0x2ca` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x382]` |
| `0x00168E4A` | `rsp+0x2cb` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x377], al` |
| `0x00168E51` | `rsp+0x2cb` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x377]` |
| `0x00168EBE` | `rsp+0x2cb` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x37b], al` |
| `0x00168EC5` | `rsp+0x2cb` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x37b]` |
| `0x00168FA6` | `rsp+0x2cb` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x383], al` |
| `0x00168FAD` | `rsp+0x2cb` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x383]` |
| `0x001691AC` | `rsp+0x31c` (inferred) | `+0x98` | mt | `mov dword ptr [rsp + 0x3b4], 0x2a` |
| `0x001691B7` | `rsp+0x31c` (inferred) | `+0x98` | mt | `mov eax, dword ptr [rsp + 0x3b4]` |
| `0x001692E1` | `rsp+0x31c` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x3c8], cl` |
| `0x001692E8` | `rsp+0x31c` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x3c8]` |
| `0x00169329` | `rsp+0x31c` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x3cc], cl` |
| `0x00169330` | `rsp+0x31c` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x3cc]` |
| `0x001691D3` | `rsp+0x309` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x3b9], cl` |
| `0x001691DA` | `rsp+0x309` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x3b9]` |
| `0x00169263` | `rsp+0x309` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x3c1], cl` |
| `0x0016926A` | `rsp+0x309` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x3c1]` |
| `0x001692AB` | `rsp+0x309` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x3c5], cl` |
| `0x001692B2` | `rsp+0x309` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x3c5]` |
| `0x001691E5` | `rsp+0x30a` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x3ba], cl` |
| `0x001691EC` | `rsp+0x30a` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x3ba]` |
| `0x00169275` | `rsp+0x30a` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x3c2], cl` |
| `0x0016927C` | `rsp+0x30a` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x3c2]` |
| `0x001692BD` | `rsp+0x30a` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x3c6], cl` |
| `0x001692C4` | `rsp+0x30a` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x3c6]` |
| `0x001691F7` | `rsp+0x30b` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x3bb], cl` |
| `0x001691FE` | `rsp+0x30b` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x3bb]` |
| `0x00169287` | `rsp+0x30b` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x3c3], cl` |
| `0x0016928E` | `rsp+0x30b` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x3c3]` |
| `0x001692CF` | `rsp+0x30b` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x3c7], cl` |
| `0x001692D6` | `rsp+0x30b` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x3c7]` |
| `0x00169287` | `rsp+0x317` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x3c3], cl` |
| `0x0016928E` | `rsp+0x317` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x3c3]` |
| `0x001692CF` | `rsp+0x317` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x3c7], cl` |
| `0x001692D6` | `rsp+0x317` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x3c7]` |
| `0x0016935F` | `rsp+0x317` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x3cf], cl` |
| `0x00169366` | `rsp+0x317` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x3cf]` |
| `0x0016890B` | `rsp-0x38` (inferred) | `+0x98` | mt | `mov qword ptr [rsp + 0x60], rdx` |
| `0x00169174` | `rsp-0x38` (inferred) | `+0xB8` | vmt2 | `mov qword ptr [rsp + 0x80], rax` |
| `0x0016918B` | `rsp-0x38` (inferred) | `+0xB0` | vmr/rxboost | `mov qword ptr [rsp + 0x78], rax` |
| `0x00169197` | `rsp-0x38` (inferred) | `+0xB0` | vmr/rxboost | `lea rcx, [rsp + 0x78]` |
| `0x0016942D` | `rsp-0x38` (inferred) | `+0x98` | mt | `mov rax, qword ptr [rsp + 0x60]` |
| `0x0016890B` | `rsp-0x4c` (inferred) | `+0xAC` | straps | `mov qword ptr [rsp + 0x60], rdx` |
| `0x00168AE1` | `rsp-0x4c` (inferred) | `+0xBC` | vmt3 | `mov qword ptr [rsp + 0x70], rax` |
| `0x00168BF0` | `rsp-0x4c` (inferred) | `+0xBC` | vmt3 | `lea rdx, [rsp + 0x70]` |
| `0x00168C01` | `rsp-0x4c` (inferred) | `+0xBC` | vmt3 | `mov rdi, qword ptr [rsp + 0x70]` |
| `0x0016942D` | `rsp-0x4c` (inferred) | `+0xAC` | straps | `mov rax, qword ptr [rsp + 0x60]` |
| `0x0016890B` | `rsp-0x50` (inferred) | `+0xB0` | vmr/rxboost | `mov qword ptr [rsp + 0x60], rdx` |
| `0x00168B47` | `rsp-0x50` (inferred) | `+0xB8` | vmt2 | `mov qword ptr [rsp + 0x68], rdx` |
| `0x00168BB7` | `rsp-0x50` (inferred) | `+0xB8` | vmt2 | `lea rax, [rsp + 0x68]` |
| `0x00168C06` | `rsp-0x50` (inferred) | `+0xB8` | vmt2 | `mov rdx, qword ptr [rsp + 0x68]` |
| `0x0016942D` | `rsp-0x50` (inferred) | `+0xB0` | vmr/rxboost | `mov rax, qword ptr [rsp + 0x60]` |
| `0x00168913` | `rsp-0x20` (inferred) | `+0xB8` | vmt2 | `mov qword ptr [rsp + 0x98], rcx` |
| `0x00168BBC` | `rsp-0x20` (inferred) | `+0xB0` | vmr/rxboost | `mov qword ptr [rsp + 0x90], rax` |
| `0x00168BC9` | `rsp-0x20` (inferred) | `+0xB0` | vmr/rxboost | `lea r8, [rsp + 0x90]` |
| `0x0016918B` | `rsp-0x20` (inferred) | `+0x98` | mt | `mov qword ptr [rsp + 0x78], rax` |
| `0x00169197` | `rsp-0x20` (inferred) | `+0x98` | mt | `lea rcx, [rsp + 0x78]` |
| `0x00168AA5` | `rsp-0x54` (inferred) | `+0xAC` | straps | `mov dword ptr [rsp + 0x58], eax` |
| `0x00168B47` | `rsp-0x54` (inferred) | `+0xBC` | vmt3 | `mov qword ptr [rsp + 0x68], rdx` |
| `0x00168BB7` | `rsp-0x54` (inferred) | `+0xBC` | vmt3 | `lea rax, [rsp + 0x68]` |
| `0x00168C06` | `rsp-0x54` (inferred) | `+0xBC` | vmt3 | `mov rdx, qword ptr [rsp + 0x68]` |
| `0x00168C32` | `rsp-0x54` (inferred) | `+0xAC` | straps | `mov eax, dword ptr [rsp + 0x58]` |
| `0x00168ABF` | `rsp+0x48` (inferred) | `+0x98` | mt | `mov byte ptr [rsp + 0xe0], 0` |
| `0x00168ACF` | `rsp+0x48` (inferred) | `+0x98` | mt | `mov byte ptr [rsp + 0xe0], 1` |
| `0x00168B3B` | `rsp+0x48` (inferred) | `+0x98` | mt | `mov byte ptr [rsp + 0xe0], 0` |
| `0x0016906C` | `rsp+0x48` (inferred) | `+0xB8` | vmt2 | `mov dword ptr [rsp + 0x100], r12d` |
| `0x0016907C` | `rsp+0x48` (inferred) | `+0xB8` | vmt2 | `movaps xmm0, xmmword ptr [rsp + 0x100]` |
| `0x00168ABF` | `rsp+0x30` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0xe0], 0` |
| `0x00168ACF` | `rsp+0x30` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0xe0], 1` |
| `0x00168B3B` | `rsp+0x30` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0xe0], 0` |
| `0x0016900C` | `rsp+0x30` (inferred) | `+0x98` | mt | `mov qword ptr [rsp + 0xc8], rcx` |
| `0x0016902C` | `rsp+0x30` (inferred) | `+0x98` | mt | `lea rdx, [rsp + 0xc8]` |
| `0x00168B47` | `rsp-0x30` (inferred) | `+0x98` | mt | `mov qword ptr [rsp + 0x68], rdx` |
| `0x00168BB7` | `rsp-0x30` (inferred) | `+0x98` | mt | `lea rax, [rsp + 0x68]` |
| `0x00168C06` | `rsp-0x30` (inferred) | `+0x98` | mt | `mov rdx, qword ptr [rsp + 0x68]` |
| `0x00169174` | `rsp-0x30` (inferred) | `+0xB0` | vmr/rxboost | `mov qword ptr [rsp + 0x80], rax` |
| `0x0016917C` | `rsp-0x30` (inferred) | `+0xB8` | vmt2 | `mov qword ptr [rsp + 0x88], rax` |
| `0x00168C7D` | `rsp+0x2ac` (inferred) | `+0xB8` | vmt2 | `mov dword ptr [rsp + 0x364], ecx` |
| `0x00168C84` | `rsp+0x2ac` (inferred) | `+0xB8` | vmt2 | `mov eax, dword ptr [rsp + 0x364]` |
| `0x00168C97` | `rsp+0x2ac` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x368], cl` |
| `0x00168C9E` | `rsp+0x2ac` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x368]` |
| `0x00168FD3` | `rsp+0x2ac` (inferred) | `+0xBC` | vmt3 | `movzx eax, byte ptr [rsp + 0x368]` |
| `0x00168D0B` | `rsp+0x2d4` (inferred) | `+0x98` | mt | `mov byte ptr [rsp + 0x36c], al` |
| `0x00168D12` | `rsp+0x2d4` (inferred) | `+0x98` | mt | `movsx ecx, byte ptr [rsp + 0x36c]` |
| `0x00168F4F` | `rsp+0x2d4` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x380], al` |
| `0x00168F56` | `rsp+0x2d4` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x380]` |
| `0x00168FC3` | `rsp+0x2d4` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x384], al` |
| `0x00168D28` | `rsp+0x2d5` (inferred) | `+0x98` | mt | `mov byte ptr [rsp + 0x36d], al` |
| `0x00168D2F` | `rsp+0x2d5` (inferred) | `+0x98` | mt | `movsx ecx, byte ptr [rsp + 0x36d]` |
| `0x00168F6C` | `rsp+0x2d5` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x381], al` |
| `0x00168F73` | `rsp+0x2d5` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x381]` |
| `0x00168FCC` | `rsp+0x2d5` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x385], al` |
| `0x00168E84` | `rsp+0x2cd` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x379], al` |
| `0x00168E8B` | `rsp+0x2cd` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x379]` |
| `0x00168EF8` | `rsp+0x2cd` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x37d], al` |
| `0x00168EFF` | `rsp+0x2cd` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x37d]` |
| `0x00168FCC` | `rsp+0x2cd` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x385], al` |
| `0x00169002` | `rsp+0x4` (inferred) | `+0xBC` | vmt3 | `mov qword ptr [rsp + 0xc0], rcx` |
| `0x00169048` | `rsp+0x4` (inferred) | `+0xBC` | vmt3 | `mov qword ptr [rsp + 0xc0], rax` |
| `0x00169057` | `rsp+0x4` (inferred) | `+0xBC` | vmt3 | `lea rcx, [rsp + 0xc0]` |
| `0x001693CC` | `rsp+0x4` (inferred) | `+0xAC` | straps | `mov qword ptr [rsp + 0xb0], rcx` |
| `0x001693EC` | `rsp+0x4` (inferred) | `+0xAC` | straps | `lea rdx, [rsp + 0xb0]` |
| `0x0016900C` | `rsp+0x18` (inferred) | `+0xB0` | vmr/rxboost | `mov qword ptr [rsp + 0xc8], rcx` |
| `0x00169014` | `rsp+0x18` (inferred) | `+0xB8` | vmt2 | `mov qword ptr [rsp + 0xd0], rcx` |
| `0x0016902C` | `rsp+0x18` (inferred) | `+0xB0` | vmr/rxboost | `lea rdx, [rsp + 0xc8]` |
| `0x001693CC` | `rsp+0x18` (inferred) | `+0x98` | mt | `mov qword ptr [rsp + 0xb0], rcx` |
| `0x001693EC` | `rsp+0x18` (inferred) | `+0x98` | mt | `lea rdx, [rsp + 0xb0]` |
| `0x001691AC` | `rsp+0x2fc` (inferred) | `+0xB8` | vmt2 | `mov dword ptr [rsp + 0x3b4], 0x2a` |
| `0x001691B7` | `rsp+0x2fc` (inferred) | `+0xB8` | vmt2 | `mov eax, dword ptr [rsp + 0x3b4]` |
| `0x001691C1` | `rsp+0x2fc` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x3b8], al` |
| `0x001691C8` | `rsp+0x2fc` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x3b8]` |
| `0x00169393` | `rsp+0x2fc` (inferred) | `+0xBC` | vmt3 | `movzx eax, byte ptr [rsp + 0x3b8]` |
| `0x001691D3` | `rsp+0x321` (inferred) | `+0x98` | mt | `mov byte ptr [rsp + 0x3b9], cl` |
| `0x001691DA` | `rsp+0x321` (inferred) | `+0x98` | mt | `movsx ecx, byte ptr [rsp + 0x3b9]` |
| `0x0016933B` | `rsp+0x321` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x3cd], cl` |
| `0x00169342` | `rsp+0x321` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x3cd]` |
| `0x00169383` | `rsp+0x321` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x3d1], cl` |
| `0x001691E5` | `rsp+0x322` (inferred) | `+0x98` | mt | `mov byte ptr [rsp + 0x3ba], cl` |
| `0x001691EC` | `rsp+0x322` (inferred) | `+0x98` | mt | `movsx ecx, byte ptr [rsp + 0x3ba]` |
| `0x0016934D` | `rsp+0x322` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x3ce], cl` |
| `0x00169354` | `rsp+0x322` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x3ce]` |
| `0x0016938C` | `rsp+0x322` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x3d2], al` |
| `0x001692AB` | `rsp+0x319` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x3c5], cl` |
| `0x001692B2` | `rsp+0x319` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x3c5]` |
| `0x001692F3` | `rsp+0x319` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x3c9], cl` |
| `0x001692FA` | `rsp+0x319` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x3c9]` |
| `0x00169383` | `rsp+0x319` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x3d1], cl` |
| `0x001692BD` | `rsp+0x31a` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x3c6], cl` |
| `0x001692C4` | `rsp+0x31a` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x3c6]` |
| `0x00169305` | `rsp+0x31a` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x3ca], cl` |
| `0x0016930C` | `rsp+0x31a` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x3ca]` |
| `0x0016938C` | `rsp+0x31a` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x3d2], al` |
| `0x0016890B` | `rsp-0x5c` (inferred) | `+0xBC` | vmt3 | `mov qword ptr [rsp + 0x60], rdx` |
| `0x0016892C` | `rsp-0x5c` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x50], al` |
| `0x00168BC4` | `rsp-0x5c` (inferred) | `+0xB0` | vmr/rxboost | `lea r9, [rsp + 0x54]` |
| `0x0016942D` | `rsp-0x5c` (inferred) | `+0xBC` | vmt3 | `mov rax, qword ptr [rsp + 0x60]` |
| `0x00168913` | `rsp+0x0` (inferred) | `+0x98` | mt | `mov qword ptr [rsp + 0x98], rcx` |
| `0x001693CC` | `rsp+0x0` (inferred) | `+0xB0` | vmr/rxboost | `mov qword ptr [rsp + 0xb0], rcx` |
| `0x001693D4` | `rsp+0x0` (inferred) | `+0xB8` | vmt2 | `mov qword ptr [rsp + 0xb8], rcx` |
| `0x001693EC` | `rsp+0x0` (inferred) | `+0xB0` | vmr/rxboost | `lea rdx, [rsp + 0xb0]` |
| `0x00168913` | `rsp-0x14` (inferred) | `+0xAC` | straps | `mov qword ptr [rsp + 0x98], rcx` |
| `0x001693C2` | `rsp-0x14` (inferred) | `+0xBC` | vmt3 | `mov qword ptr [rsp + 0xa8], rcx` |
| `0x00169408` | `rsp-0x14` (inferred) | `+0xBC` | vmt3 | `mov qword ptr [rsp + 0xa8], rax` |
| `0x00169417` | `rsp-0x14` (inferred) | `+0xBC` | vmt3 | `lea rcx, [rsp + 0xa8]` |
| `0x0016892C` | `rsp-0x60` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x50], al` |
| `0x00168AA5` | `rsp-0x60` (inferred) | `+0xB8` | vmt2 | `mov dword ptr [rsp + 0x58], eax` |
| `0x00168C2D` | `rsp-0x60` (inferred) | `+0x98` | mt | `mov dword ptr [rsp + 0x38], r10d` |
| `0x00168C32` | `rsp-0x60` (inferred) | `+0xB8` | vmt2 | `mov eax, dword ptr [rsp + 0x58]` |
| `0x00168A04` | `rsp+0x11c` (inferred) | `+0x98` | mt | `mov r13d, dword ptr [rsp + 0x1b4]` |
| `0x00168A0C` | `rsp+0x11c` (inferred) | `+0xB0` | vmr/rxboost | `cmp dword ptr [rsp + 0x1cc], 0` |
| `0x00168C19` | `rsp+0x11c` (inferred) | `+0xB0` | vmr/rxboost | `cmp dword ptr [rsp + 0x1cc], 0` |
| `0x0016914E` | `rsp+0x11c` (inferred) | `+0xB8` | vmt2 | `mov r8d, dword ptr [rsp + 0x1d4]` |
| `0x00168ABF` | `rsp+0x24` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0xe0], 0` |
| `0x00168ACF` | `rsp+0x24` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0xe0], 1` |
| `0x00168B3B` | `rsp+0x24` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0xe0], 0` |
| `0x00169014` | `rsp+0x24` (inferred) | `+0xAC` | straps | `mov qword ptr [rsp + 0xd0], rcx` |
| `0x00168AE1` | `rsp-0x3c` (inferred) | `+0xAC` | straps | `mov qword ptr [rsp + 0x70], rax` |
| `0x00168BF0` | `rsp-0x3c` (inferred) | `+0xAC` | straps | `lea rdx, [rsp + 0x70]` |
| `0x00168C01` | `rsp-0x3c` (inferred) | `+0xAC` | straps | `mov rdi, qword ptr [rsp + 0x70]` |
| `0x00169174` | `rsp-0x3c` (inferred) | `+0xBC` | vmt3 | `mov qword ptr [rsp + 0x80], rax` |
| `0x00168BE8` | `rsp-0x78` (inferred) | `+0x98` | mt | `mov qword ptr [rsp + 0x20], rax` |
| `0x00168C29` | `rsp-0x78` (inferred) | `+0xB8` | vmt2 | `mov dword ptr [rsp + 0x40], eax` |
| `0x00168C2D` | `rsp-0x78` (inferred) | `+0xB0` | vmr/rxboost | `mov dword ptr [rsp + 0x38], r10d` |
| `0x00168C46` | `rsp-0x78` (inferred) | `+0x98` | mt | `mov dword ptr [rsp + 0x20], r13d` |
| `0x00168CB4` | `rsp+0x2b1` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x369], al` |
| `0x00168CBB` | `rsp+0x2b1` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x369]` |
| `0x00168D28` | `rsp+0x2b1` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x36d], al` |
| `0x00168D2F` | `rsp+0x2b1` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x36d]` |
| `0x00168CD1` | `rsp+0x2b2` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x36a], al` |
| `0x00168CD8` | `rsp+0x2b2` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x36a]` |
| `0x00168D45` | `rsp+0x2b2` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x36e], al` |
| `0x00168D4C` | `rsp+0x2b2` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x36e]` |
| `0x00168CEE` | `rsp+0x2b3` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x36b], al` |
| `0x00168CF5` | `rsp+0x2b3` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x36b]` |
| `0x00168D62` | `rsp+0x2b3` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x36f], al` |
| `0x00168D69` | `rsp+0x2b3` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x36f]` |
| `0x00168D28` | `rsp+0x2b5` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x36d], al` |
| `0x00168D2F` | `rsp+0x2b5` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x36d]` |
| `0x00168D9C` | `rsp+0x2b5` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x371], al` |
| `0x00168DA3` | `rsp+0x2b5` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x371]` |
| `0x00168D45` | `rsp+0x2d6` (inferred) | `+0x98` | mt | `mov byte ptr [rsp + 0x36e], al` |
| `0x00168D4C` | `rsp+0x2d6` (inferred) | `+0x98` | mt | `movsx ecx, byte ptr [rsp + 0x36e]` |
| `0x00168F89` | `rsp+0x2d6` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x382], al` |
| `0x00168F90` | `rsp+0x2d6` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x382]` |
| `0x00168D45` | `rsp+0x2b6` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x36e], al` |
| `0x00168D4C` | `rsp+0x2b6` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x36e]` |
| `0x00168DB9` | `rsp+0x2b6` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x372], al` |
| `0x00168DC0` | `rsp+0x2b6` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x372]` |
| `0x00168D62` | `rsp+0x2d7` (inferred) | `+0x98` | mt | `mov byte ptr [rsp + 0x36f], al` |
| `0x00168D69` | `rsp+0x2d7` (inferred) | `+0x98` | mt | `movsx ecx, byte ptr [rsp + 0x36f]` |
| `0x00168FA6` | `rsp+0x2d7` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x383], al` |
| `0x00168FAD` | `rsp+0x2d7` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x383]` |
| `0x00168D62` | `rsp+0x2b7` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x36f], al` |
| `0x00168D69` | `rsp+0x2b7` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x36f]` |
| `0x00168DD6` | `rsp+0x2b7` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x373], al` |
| `0x00168DDD` | `rsp+0x2b7` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x373]` |
| `0x00168EA1` | `rsp+0x2ce` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x37a], al` |
| `0x00168EA8` | `rsp+0x2ce` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x37a]` |
| `0x00168F15` | `rsp+0x2ce` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x37e], al` |
| `0x00168F1C` | `rsp+0x2ce` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x37e]` |
| `0x00168EBE` | `rsp+0x2cf` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x37b], al` |
| `0x00168EC5` | `rsp+0x2cf` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x37b]` |
| `0x00168F32` | `rsp+0x2cf` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x37f], al` |
| `0x00168F39` | `rsp+0x2cf` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x37f]` |
| `0x00169002` | `rsp+0x14` (inferred) | `+0xAC` | straps | `mov qword ptr [rsp + 0xc0], rcx` |
| `0x00169014` | `rsp+0x14` (inferred) | `+0xBC` | vmt3 | `mov qword ptr [rsp + 0xd0], rcx` |
| `0x00169048` | `rsp+0x14` (inferred) | `+0xAC` | straps | `mov qword ptr [rsp + 0xc0], rax` |
| `0x00169057` | `rsp+0x14` (inferred) | `+0xAC` | straps | `lea rcx, [rsp + 0xc0]` |
| `0x00169002` | `rsp+0x8` (inferred) | `+0xB8` | vmt2 | `mov qword ptr [rsp + 0xc0], rcx` |
| `0x00169048` | `rsp+0x8` (inferred) | `+0xB8` | vmt2 | `mov qword ptr [rsp + 0xc0], rax` |
| `0x00169057` | `rsp+0x8` (inferred) | `+0xB8` | vmt2 | `lea rcx, [rsp + 0xc0]` |
| `0x001693D4` | `rsp+0x8` (inferred) | `+0xB0` | vmr/rxboost | `mov qword ptr [rsp + 0xb8], rcx` |
| `0x0016901C` | `rsp+0x80` (inferred) | `+0xB0` | vmr/rxboost | `mov qword ptr [rsp + 0x130], rax` |
| `0x00169024` | `rsp+0x80` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x138], 1` |
| `0x00169034` | `rsp+0x80` (inferred) | `+0xB0` | vmr/rxboost | `lea rcx, [rsp + 0x130]` |
| `0x001693E4` | `rsp+0x80` (inferred) | `+0x98` | mt | `mov byte ptr [rsp + 0x118], 1` |
| `0x0016901C` | `rsp+0x78` (inferred) | `+0xB8` | vmt2 | `mov qword ptr [rsp + 0x130], rax` |
| `0x00169034` | `rsp+0x78` (inferred) | `+0xB8` | vmt2 | `lea rcx, [rsp + 0x130]` |
| `0x001693DC` | `rsp+0x78` (inferred) | `+0x98` | mt | `mov qword ptr [rsp + 0x110], rax` |
| `0x001693F4` | `rsp+0x78` (inferred) | `+0x98` | mt | `lea rcx, [rsp + 0x110]` |
| `0x0016906C` | `rsp+0x54` (inferred) | `+0xAC` | straps | `mov dword ptr [rsp + 0x100], r12d` |
| `0x0016907C` | `rsp+0x54` (inferred) | `+0xAC` | straps | `movaps xmm0, xmmword ptr [rsp + 0x100]` |
| `0x001693DC` | `rsp+0x54` (inferred) | `+0xBC` | vmt3 | `mov qword ptr [rsp + 0x110], rax` |
| `0x001693F4` | `rsp+0x54` (inferred) | `+0xBC` | vmt3 | `lea rcx, [rsp + 0x110]` |
| `0x00169084` | `rsp+0xb4` (inferred) | `+0xAC` | straps | `movdqa xmmword ptr [rsp + 0x160], xmm0` |
| `0x0016908D` | `rsp+0xb4` (inferred) | `+0xAC` | straps | `lea rdx, [rsp + 0x160]` |
| `0x00169095` | `rsp+0xb4` (inferred) | `+0xBC` | vmt3 | `lea rcx, [rsp + 0x170]` |
| `0x001690A9` | `rsp+0xb4` (inferred) | `+0xBC` | vmt3 | `lea rcx, [rsp + 0x170]` |
| `0x0016917C` | `rsp-0x10` (inferred) | `+0x98` | mt | `mov qword ptr [rsp + 0x88], rax` |
| `0x001693C2` | `rsp-0x10` (inferred) | `+0xB8` | vmt2 | `mov qword ptr [rsp + 0xa8], rcx` |
| `0x00169408` | `rsp-0x10` (inferred) | `+0xB8` | vmt2 | `mov qword ptr [rsp + 0xa8], rax` |
| `0x00169417` | `rsp-0x10` (inferred) | `+0xB8` | vmt2 | `lea rcx, [rsp + 0xa8]` |
| `0x001691A1` | `rsp+0x2f8` (inferred) | `+0xB8` | vmt2 | `mov dword ptr [rsp + 0x3b0], 0x14` |
| `0x001691AC` | `rsp+0x2f8` (inferred) | `+0xBC` | vmt3 | `mov dword ptr [rsp + 0x3b4], 0x2a` |
| `0x001691B7` | `rsp+0x2f8` (inferred) | `+0xBC` | vmt3 | `mov eax, dword ptr [rsp + 0x3b4]` |
| `0x001693A3` | `rsp+0x2f8` (inferred) | `+0xB8` | vmt2 | `lea rcx, [rsp + 0x3b0]` |
| `0x001691D3` | `rsp+0x301` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x3b9], cl` |
| `0x001691DA` | `rsp+0x301` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x3b9]` |
| `0x0016921B` | `rsp+0x301` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x3bd], cl` |
| `0x00169222` | `rsp+0x301` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x3bd]` |
| `0x001691E5` | `rsp+0x302` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x3ba], cl` |
| `0x001691EC` | `rsp+0x302` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x3ba]` |
| `0x0016922D` | `rsp+0x302` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x3be], cl` |
| `0x00169234` | `rsp+0x302` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x3be]` |
| `0x001691F7` | `rsp+0x323` (inferred) | `+0x98` | mt | `mov byte ptr [rsp + 0x3bb], cl` |
| `0x001691FE` | `rsp+0x323` (inferred) | `+0x98` | mt | `movsx ecx, byte ptr [rsp + 0x3bb]` |
| `0x0016935F` | `rsp+0x323` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x3cf], cl` |
| `0x00169366` | `rsp+0x323` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x3cf]` |
| `0x001691F7` | `rsp+0x303` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x3bb], cl` |
| `0x001691FE` | `rsp+0x303` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x3bb]` |
| `0x0016923F` | `rsp+0x303` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x3bf], cl` |
| `0x00169246` | `rsp+0x303` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x3bf]` |
| `0x00169209` | `rsp+0x324` (inferred) | `+0x98` | mt | `mov byte ptr [rsp + 0x3bc], cl` |
| `0x00169210` | `rsp+0x324` (inferred) | `+0x98` | mt | `movsx ecx, byte ptr [rsp + 0x3bc]` |
| `0x00169371` | `rsp+0x324` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x3d0], cl` |
| `0x00169378` | `rsp+0x324` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x3d0]` |
| `0x0016921B` | `rsp+0x305` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x3bd], cl` |
| `0x00169222` | `rsp+0x305` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x3bd]` |
| `0x00169263` | `rsp+0x305` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x3c1], cl` |
| `0x0016926A` | `rsp+0x305` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x3c1]` |
| `0x0016922D` | `rsp+0x306` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x3be], cl` |
| `0x00169234` | `rsp+0x306` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x3be]` |
| `0x00169275` | `rsp+0x306` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x3c2], cl` |
| `0x0016927C` | `rsp+0x306` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x3c2]` |
| `0x0016923F` | `rsp+0x307` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x3bf], cl` |
| `0x00169246` | `rsp+0x307` (inferred) | `+0xB8` | vmt2 | `movsx ecx, byte ptr [rsp + 0x3bf]` |
| `0x00169287` | `rsp+0x307` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x3c3], cl` |
| `0x0016928E` | `rsp+0x307` (inferred) | `+0xBC` | vmt3 | `movsx ecx, byte ptr [rsp + 0x3c3]` |
| `0x001692CF` | `rsp+0x31b` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x3c7], cl` |
| `0x001692D6` | `rsp+0x31b` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x3c7]` |
| `0x00169317` | `rsp+0x31b` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x3cb], cl` |
| `0x0016931E` | `rsp+0x31b` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x3cb]` |
| `0x001692F3` | `rsp+0x31d` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x3c9], cl` |
| `0x001692FA` | `rsp+0x31d` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x3c9]` |
| `0x0016933B` | `rsp+0x31d` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x3cd], cl` |
| `0x00169342` | `rsp+0x31d` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x3cd]` |
| `0x00169305` | `rsp+0x31e` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x3ca], cl` |
| `0x0016930C` | `rsp+0x31e` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x3ca]` |
| `0x0016934D` | `rsp+0x31e` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x3ce], cl` |
| `0x00169354` | `rsp+0x31e` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x3ce]` |
| `0x00169317` | `rsp+0x31f` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x3cb], cl` |
| `0x0016931E` | `rsp+0x31f` (inferred) | `+0xAC` | straps | `movsx ecx, byte ptr [rsp + 0x3cb]` |
| `0x0016935F` | `rsp+0x31f` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x3cf], cl` |
| `0x00169366` | `rsp+0x31f` (inferred) | `+0xB0` | vmr/rxboost | `movsx ecx, byte ptr [rsp + 0x3cf]` |
| `0x001693C2` | `rsp-0x4` (inferred) | `+0xAC` | straps | `mov qword ptr [rsp + 0xa8], rcx` |
| `0x001693D4` | `rsp-0x4` (inferred) | `+0xBC` | vmt3 | `mov qword ptr [rsp + 0xb8], rcx` |
| `0x00169408` | `rsp-0x4` (inferred) | `+0xAC` | straps | `mov qword ptr [rsp + 0xa8], rax` |
| `0x00169417` | `rsp-0x4` (inferred) | `+0xAC` | straps | `lea rcx, [rsp + 0xa8]` |
| `0x00168900` | `rsp+0x388` (inferred) | `+0xB0` | vmr/rxboost | `mov qword ptr [rsp + 0x438], rax` |
| `0x00169493` | `rsp+0x388` (inferred) | `+0xB0` | vmr/rxboost | `mov rcx, qword ptr [rsp + 0x438]` |
| `0x001694A3` | `rsp+0x388` (inferred) | `+0xB8` | vmt2 | `lea r11, [rsp + 0x440]` |
| `0x00168900` | `rsp+0x380` (inferred) | `+0xB8` | vmt2 | `mov qword ptr [rsp + 0x438], rax` |
| `0x0016939B` | `rsp+0x380` (inferred) | `+0x98` | mt | `lea rdx, [rsp + 0x418]` |
| `0x00169493` | `rsp+0x380` (inferred) | `+0xB8` | vmt2 | `mov rcx, qword ptr [rsp + 0x438]` |
| `0x0016892C` | `rsp-0x68` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x50], al` |
| `0x00168BC4` | `rsp-0x68` (inferred) | `+0xBC` | vmt3 | `lea r9, [rsp + 0x54]` |
| `0x00168C36` | `rsp-0x68` (inferred) | `+0x98` | mt | `mov dword ptr [rsp + 0x30], eax` |
| `0x001689A5` | `rsp+0x108` (inferred) | `+0x98` | mt | `lea rdx, [rsp + 0x1a0]` |
| `0x00168A04` | `rsp+0x108` (inferred) | `+0xAC` | straps | `mov r13d, dword ptr [rsp + 0x1b4]` |
| `0x001690C7` | `rsp+0x108` (inferred) | `+0x98` | mt | `lea rcx, [rsp + 0x1a0]` |
| `0x00168A0C` | `rsp+0x120` (inferred) | `+0xAC` | straps | `cmp dword ptr [rsp + 0x1cc], 0` |
| `0x00168C11` | `rsp+0x120` (inferred) | `+0xB0` | vmr/rxboost | `mov r10d, dword ptr [rsp + 0x1d0]` |
| `0x00168C19` | `rsp+0x120` (inferred) | `+0xAC` | straps | `cmp dword ptr [rsp + 0x1cc], 0` |
| `0x00168A0C` | `rsp+0x114` (inferred) | `+0xB8` | vmt2 | `cmp dword ptr [rsp + 0x1cc], 0` |
| `0x00168C11` | `rsp+0x114` (inferred) | `+0xBC` | vmt3 | `mov r10d, dword ptr [rsp + 0x1d0]` |
| `0x00168C19` | `rsp+0x114` (inferred) | `+0xB8` | vmt2 | `cmp dword ptr [rsp + 0x1cc], 0` |
| `0x00168AA5` | `rsp-0x64` (inferred) | `+0xBC` | vmt3 | `mov dword ptr [rsp + 0x58], eax` |
| `0x00168BC4` | `rsp-0x64` (inferred) | `+0xB8` | vmt2 | `lea r9, [rsp + 0x54]` |
| `0x00168C32` | `rsp-0x64` (inferred) | `+0xBC` | vmt3 | `mov eax, dword ptr [rsp + 0x58]` |
| `0x00168AB7` | `rsp+0x20` (inferred) | `+0xB8` | vmt2 | `mov qword ptr [rsp + 0xd8], rbx` |
| `0x00169014` | `rsp+0x20` (inferred) | `+0xB0` | vmr/rxboost | `mov qword ptr [rsp + 0xd0], rcx` |
| `0x001693D4` | `rsp+0x20` (inferred) | `+0x98` | mt | `mov qword ptr [rsp + 0xb8], rcx` |
| `0x00168AB7` | `rsp+0x1c` (inferred) | `+0xBC` | vmt3 | `mov qword ptr [rsp + 0xd8], rbx` |
| `0x0016900C` | `rsp+0x1c` (inferred) | `+0xAC` | straps | `mov qword ptr [rsp + 0xc8], rcx` |
| `0x0016902C` | `rsp+0x1c` (inferred) | `+0xAC` | straps | `lea rdx, [rsp + 0xc8]` |
| `0x00168B8A` | `rsp+0xb0` (inferred) | `+0x98` | mt | `mov qword ptr [rsp + 0x148], rdi` |
| `0x00169084` | `rsp+0xb0` (inferred) | `+0xB0` | vmr/rxboost | `movdqa xmmword ptr [rsp + 0x160], xmm0` |
| `0x0016908D` | `rsp+0xb0` (inferred) | `+0xB0` | vmr/rxboost | `lea rdx, [rsp + 0x160]` |
| `0x00168B8A` | `rsp+0x98` (inferred) | `+0xB0` | vmr/rxboost | `mov qword ptr [rsp + 0x148], rdi` |
| `0x0016901C` | `rsp+0x98` (inferred) | `+0x98` | mt | `mov qword ptr [rsp + 0x130], rax` |
| `0x00169034` | `rsp+0x98` (inferred) | `+0x98` | mt | `lea rcx, [rsp + 0x130]` |
| `0x00168B92` | `rsp+0xa8` (inferred) | `+0x98` | mt | `mov qword ptr [rsp + 0x140], rcx` |
| `0x00169084` | `rsp+0xa8` (inferred) | `+0xB8` | vmt2 | `movdqa xmmword ptr [rsp + 0x160], xmm0` |
| `0x0016908D` | `rsp+0xa8` (inferred) | `+0xB8` | vmt2 | `lea rdx, [rsp + 0x160]` |
| `0x00168B92` | `rsp+0x84` (inferred) | `+0xBC` | vmt3 | `mov qword ptr [rsp + 0x140], rcx` |
| `0x0016901C` | `rsp+0x84` (inferred) | `+0xAC` | straps | `mov qword ptr [rsp + 0x130], rax` |
| `0x00169034` | `rsp+0x84` (inferred) | `+0xAC` | straps | `lea rcx, [rsp + 0x130]` |
| `0x00168BBC` | `rsp-0x2c` (inferred) | `+0xBC` | vmt3 | `mov qword ptr [rsp + 0x90], rax` |
| `0x00168BC9` | `rsp-0x2c` (inferred) | `+0xBC` | vmt3 | `lea r8, [rsp + 0x90]` |
| `0x00169174` | `rsp-0x2c` (inferred) | `+0xAC` | straps | `mov qword ptr [rsp + 0x80], rax` |
| `0x00168BE8` | `rsp-0x8c` (inferred) | `+0xAC` | straps | `mov qword ptr [rsp + 0x20], rax` |
| `0x00168C36` | `rsp-0x8c` (inferred) | `+0xBC` | vmt3 | `mov dword ptr [rsp + 0x30], eax` |
| `0x00168C46` | `rsp-0x8c` (inferred) | `+0xAC` | straps | `mov dword ptr [rsp + 0x20], r13d` |
| `0x00168BE8` | `rsp-0x90` (inferred) | `+0xB0` | vmr/rxboost | `mov qword ptr [rsp + 0x20], rax` |
| `0x00168C42` | `rsp-0x90` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x28], al` |
| `0x00168C46` | `rsp-0x90` (inferred) | `+0xB0` | vmr/rxboost | `mov dword ptr [rsp + 0x20], r13d` |
| `0x00168D7F` | `rsp+0x2d8` (inferred) | `+0x98` | mt | `mov byte ptr [rsp + 0x370], al` |
| `0x00168D86` | `rsp+0x2d8` (inferred) | `+0x98` | mt | `movsx ecx, byte ptr [rsp + 0x370]` |
| `0x00168FC3` | `rsp+0x2d8` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x384], al` |
| `0x00168D9C` | `rsp+0x2d9` (inferred) | `+0x98` | mt | `mov byte ptr [rsp + 0x371], al` |
| `0x00168DA3` | `rsp+0x2d9` (inferred) | `+0x98` | mt | `movsx ecx, byte ptr [rsp + 0x371]` |
| `0x00168FCC` | `rsp+0x2d9` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x385], al` |
| `0x0016900C` | `rsp+0xc` (inferred) | `+0xBC` | vmt3 | `mov qword ptr [rsp + 0xc8], rcx` |
| `0x0016902C` | `rsp+0xc` (inferred) | `+0xBC` | vmt3 | `lea rdx, [rsp + 0xc8]` |
| `0x001693D4` | `rsp+0xc` (inferred) | `+0xAC` | straps | `mov qword ptr [rsp + 0xb8], rcx` |
| `0x0016906C` | `rsp+0x68` (inferred) | `+0x98` | mt | `mov dword ptr [rsp + 0x100], r12d` |
| `0x0016907C` | `rsp+0x68` (inferred) | `+0x98` | mt | `movaps xmm0, xmmword ptr [rsp + 0x100]` |
| `0x001693E4` | `rsp+0x68` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x118], 1` |
| `0x0016906C` | `rsp+0x50` (inferred) | `+0xB0` | vmr/rxboost | `mov dword ptr [rsp + 0x100], r12d` |
| `0x00169074` | `rsp+0x50` (inferred) | `+0xB8` | vmt2 | `mov qword ptr [rsp + 0x108], rax` |
| `0x0016907C` | `rsp+0x50` (inferred) | `+0xB0` | vmr/rxboost | `movaps xmm0, xmmword ptr [rsp + 0x100]` |
| `0x00169074` | `rsp+0x58` (inferred) | `+0xB0` | vmr/rxboost | `mov qword ptr [rsp + 0x108], rax` |
| `0x001693DC` | `rsp+0x58` (inferred) | `+0xB8` | vmt2 | `mov qword ptr [rsp + 0x110], rax` |
| `0x001693F4` | `rsp+0x58` (inferred) | `+0xB8` | vmt2 | `lea rcx, [rsp + 0x110]` |
| `0x0016917C` | `rsp-0x34` (inferred) | `+0xBC` | vmt3 | `mov qword ptr [rsp + 0x88], rax` |
| `0x0016918B` | `rsp-0x34` (inferred) | `+0xAC` | straps | `mov qword ptr [rsp + 0x78], rax` |
| `0x00169197` | `rsp-0x34` (inferred) | `+0xAC` | straps | `lea rcx, [rsp + 0x78]` |
| `0x0016921B` | `rsp+0x325` (inferred) | `+0x98` | mt | `mov byte ptr [rsp + 0x3bd], cl` |
| `0x00169222` | `rsp+0x325` (inferred) | `+0x98` | mt | `movsx ecx, byte ptr [rsp + 0x3bd]` |
| `0x00169383` | `rsp+0x325` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x3d1], cl` |
| `0x0016922D` | `rsp+0x326` (inferred) | `+0x98` | mt | `mov byte ptr [rsp + 0x3be], cl` |
| `0x00169234` | `rsp+0x326` (inferred) | `+0x98` | mt | `movsx ecx, byte ptr [rsp + 0x3be]` |
| `0x0016938C` | `rsp+0x326` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x3d2], al` |
| `0x001693DC` | `rsp+0x60` (inferred) | `+0xB0` | vmr/rxboost | `mov qword ptr [rsp + 0x110], rax` |
| `0x001693E4` | `rsp+0x60` (inferred) | `+0xB8` | vmt2 | `mov byte ptr [rsp + 0x118], 1` |
| `0x001693F4` | `rsp+0x60` (inferred) | `+0xB0` | vmr/rxboost | `lea rcx, [rsp + 0x110]` |
| `0x00168913` | `rsp-0x18` (inferred) | `+0xB0` | vmr/rxboost | `mov qword ptr [rsp + 0x98], rcx` |
| `0x00169174` | `rsp-0x18` (inferred) | `+0x98` | mt | `mov qword ptr [rsp + 0x80], rax` |
| `0x00168913` | `rsp-0x24` (inferred) | `+0xBC` | vmt3 | `mov qword ptr [rsp + 0x98], rcx` |
| `0x0016917C` | `rsp-0x24` (inferred) | `+0xAC` | straps | `mov qword ptr [rsp + 0x88], rax` |
| `0x0016892C` | `rsp-0x6c` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x50], al` |
| `0x00168C29` | `rsp-0x6c` (inferred) | `+0xAC` | straps | `mov dword ptr [rsp + 0x40], eax` |
| `0x00168B8A` | `rsp+0x90` (inferred) | `+0xB8` | vmt2 | `mov qword ptr [rsp + 0x148], rdi` |
| `0x00168B92` | `rsp+0x90` (inferred) | `+0xB0` | vmr/rxboost | `mov qword ptr [rsp + 0x140], rcx` |
| `0x00168B8A` | `rsp+0x8c` (inferred) | `+0xBC` | vmt3 | `mov qword ptr [rsp + 0x148], rdi` |
| `0x00169024` | `rsp+0x8c` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x138], 1` |
| `0x00168B92` | `rsp+0x88` (inferred) | `+0xB8` | vmt2 | `mov qword ptr [rsp + 0x140], rcx` |
| `0x00169024` | `rsp+0x88` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x138], 1` |
| `0x00168C11` | `rsp+0x124` (inferred) | `+0xAC` | straps | `mov r10d, dword ptr [rsp + 0x1d0]` |
| `0x0016914E` | `rsp+0x124` (inferred) | `+0xB0` | vmr/rxboost | `mov r8d, dword ptr [rsp + 0x1d4]` |
| `0x00168C11` | `rsp+0x118` (inferred) | `+0xB8` | vmt2 | `mov r10d, dword ptr [rsp + 0x1d0]` |
| `0x0016914E` | `rsp+0x118` (inferred) | `+0xBC` | vmt3 | `mov r8d, dword ptr [rsp + 0x1d4]` |
| `0x00168C29` | `rsp-0x70` (inferred) | `+0xB0` | vmr/rxboost | `mov dword ptr [rsp + 0x40], eax` |
| `0x00168C42` | `rsp-0x70` (inferred) | `+0x98` | mt | `mov byte ptr [rsp + 0x28], al` |
| `0x00168C29` | `rsp-0x7c` (inferred) | `+0xBC` | vmt3 | `mov dword ptr [rsp + 0x40], eax` |
| `0x00168C36` | `rsp-0x7c` (inferred) | `+0xAC` | straps | `mov dword ptr [rsp + 0x30], eax` |
| `0x00168C2D` | `rsp-0x80` (inferred) | `+0xB8` | vmt2 | `mov dword ptr [rsp + 0x38], r10d` |
| `0x00168C36` | `rsp-0x80` (inferred) | `+0xB0` | vmr/rxboost | `mov dword ptr [rsp + 0x30], eax` |
| `0x00168C2D` | `rsp-0x84` (inferred) | `+0xBC` | vmt3 | `mov dword ptr [rsp + 0x38], r10d` |
| `0x00168C42` | `rsp-0x84` (inferred) | `+0xAC` | straps | `mov byte ptr [rsp + 0x28], al` |
| `0x00168C36` | `rsp-0x88` (inferred) | `+0xB8` | vmt2 | `mov dword ptr [rsp + 0x30], eax` |
| `0x00168C42` | `rsp-0x88` (inferred) | `+0xB0` | vmr/rxboost | `mov byte ptr [rsp + 0x28], al` |
| `0x00168FDB` | `rsp+0x360` (inferred) | `+0x98` | mt | `lea rdx, [rsp + 0x3f8]` |
| `0x0016939B` | `rsp+0x360` (inferred) | `+0xB8` | vmt2 | `lea rdx, [rsp + 0x418]` |
| `0x00169074` | `rsp+0x5c` (inferred) | `+0xAC` | straps | `mov qword ptr [rsp + 0x108], rax` |
| `0x001693E4` | `rsp+0x5c` (inferred) | `+0xBC` | vmt3 | `mov byte ptr [rsp + 0x118], 1` |

## Calls near snapshot/timing materialization

| call | target | preceding window |
|---|---|---|
| `0x00168925` | `RVA 0x00169520` | `push r15; sub rsp, 0x440; mov qword ptr [rax - 0x318], 0xfffffffffffffffe; mov qword ptr [rax + 0x10], rbx; mov qword ptr [rax + 0x20], rsi; mov rax, qword ptr [rip + 0x66dff3]; xor rax, rsp; mov qword ptr [rsp + 0x438], rax; mov r14, r8; mov qword ptr [rsp + 0x60], rdx; mov rsi, rcx; mov qword ptr [rsp + 0x98], rcx; lea rbx, [rcx + 0x7c0]; mov rcx, rbx` |
| `0x0016894F` | `RVA 0x00391AC4` | `mov r14, r8; mov qword ptr [rsp + 0x60], rdx; mov rsi, rcx; mov qword ptr [rsp + 0x98], rcx; lea rbx, [rcx + 0x7c0]; mov rcx, rbx; call 0x140169520; xor eax, eax; mov byte ptr [rsp + 0x50], al; mov qword ptr [rsi + 0x860], rax; mov qword ptr [rsi + 0x868], rax; mov qword ptr [rsi + 0x870], rax; mov qword ptr [rsi + 0x878], rax; mov rcx, rbx` |
| `0x0016895A` | `RVA 0x0039219C` | `lea rbx, [rcx + 0x7c0]; mov rcx, rbx; call 0x140169520; xor eax, eax; mov byte ptr [rsp + 0x50], al; mov qword ptr [rsi + 0x860], rax; mov qword ptr [rsi + 0x868], rax; mov qword ptr [rsi + 0x870], rax; mov qword ptr [rsi + 0x878], rax; mov rcx, rbx; call 0x140391ac4; test eax, eax; je 0x14016895f; mov ecx, eax` |
| `0x0016896A` | `RVA 0x00391B24` | `mov byte ptr [rsp + 0x50], al; mov qword ptr [rsi + 0x860], rax; mov qword ptr [rsi + 0x868], rax; mov qword ptr [rsi + 0x870], rax; mov qword ptr [rsi + 0x878], rax; mov rcx, rbx; call 0x140391ac4; test eax, eax; je 0x14016895f; mov ecx, eax; call 0x14039219c; xor edi, edi; mov dword ptr [rbx + 0x98], edi; mov rcx, rbx` |
| `0x001689B0` | `RVA 0x00084A60` | `call 0x14039219c; nop ; lea rcx, [rbx + 0x50]; call 0x140391e8c; test eax, eax; je 0x140168990; mov ecx, eax; call 0x14039219c; nop ; movsxd rax, dword ptr [rsi + 0x98]; imul r15, rax, 0xa8; add r15, qword ptr [rip + 0x67da63]; lea rdx, [rsp + 0x1a0]; mov rcx, rsi` |
| `0x00168A22` | `RVA 0x00169520` | `movzx edx, al; mov r12d, 1; cmp ecx, 0x3e8; cmove edx, r12d; jmp 0x140168a04; mov r12d, 1; mov r13d, dword ptr [rsp + 0x1b4]; cmp dword ptr [rsp + 0x1cc], 0; jg 0x140168a1f; test r13d, r13d; je 0x140168a1f; test dl, dl; je 0x140168a98; mov rcx, rbx` |
| `0x00168A41` | `RVA 0x0016B960` | `mov r13d, dword ptr [rsp + 0x1b4]; cmp dword ptr [rsp + 0x1cc], 0; jg 0x140168a1f; test r13d, r13d; je 0x140168a1f; test dl, dl; je 0x140168a98; mov rcx, rbx; call 0x140169520; mov rdi, qword ptr [rsi + 0x888]; mov qword ptr [rsi + 0x888], 0; test rdi, rdi; je 0x140168a54; mov rcx, rdi` |
| `0x00168ACA` | `RVA 0x00169520` | `test eax, eax; je 0x140168a98; mov ecx, eax; call 0x14039219c; nop ; mov edx, dword ptr [r14 + 0x18]; mov rcx, qword ptr [r14 + 0x10]; call 0x140159b40; mov dword ptr [rsp + 0x58], eax; cmp qword ptr [rsi + 0x888], 0; jne 0x1401690b7; mov qword ptr [rsp + 0xd8], rbx; mov byte ptr [rsp + 0xe0], 0; mov rcx, rbx` |
| `0x00168ADC` | `RVA 0x003B2098` | `call 0x14039219c; nop ; mov edx, dword ptr [r14 + 0x18]; mov rcx, qword ptr [r14 + 0x10]; call 0x140159b40; mov dword ptr [rsp + 0x58], eax; cmp qword ptr [rsi + 0x888], 0; jne 0x1401690b7; mov qword ptr [rsp + 0xd8], rbx; mov byte ptr [rsp + 0xe0], 0; mov rcx, rbx; call 0x140169520; mov byte ptr [rsp + 0xe0], 1; mov ecx, 0x88` |
| `0x00168AF8` | `RVA 0x0016B6E0` | `jne 0x1401690b7; mov qword ptr [rsp + 0xd8], rbx; mov byte ptr [rsp + 0xe0], 0; mov rcx, rbx; call 0x140169520; mov byte ptr [rsp + 0xe0], 1; mov ecx, 0x88; call 0x1403b2098; mov qword ptr [rsp + 0x70], rax; test rax, rax; je 0x140168aff; mov r8d, dword ptr [rsi + 0x98]; mov rdx, rsi; mov rcx, rax` |
| `0x00168B18` | `RVA 0x0016B960` | `mov qword ptr [rsp + 0x70], rax; test rax, rax; je 0x140168aff; mov r8d, dword ptr [rsi + 0x98]; mov rdx, rsi; mov rcx, rax; call 0x14016b6e0; jmp 0x140168b02; mov rax, rdi; mov rdi, qword ptr [rsi + 0x888]; mov qword ptr [rsi + 0x888], rax; test rdi, rdi; je 0x140168b2a; mov rcx, rdi` |
| `0x00168BDF` | `RVA 0x0015ED70` | `je 0x140168bac; cmp rdx, qword ptr [rdi + 0x20]; jb 0x140168bac; mov byte ptr [rsp + 0x51], r8b; jmp 0x140168c0b; mov byte ptr [rsp + 0x52], 1; xor eax, eax; mov byte ptr [rsp + 0x53], al; lea rax, [rsp + 0x68]; mov qword ptr [rsp + 0x90], rax; lea r9, [rsp + 0x54]; lea r8, [rsp + 0x90]; lea rdx, [rip + 0x2e1f30]; lea rcx, [rip + 0x67dc49]` |
| `0x00168BFC` | `RVA 0x0015F0B0` | `xor eax, eax; mov byte ptr [rsp + 0x53], al; lea rax, [rsp + 0x68]; mov qword ptr [rsp + 0x90], rax; lea r9, [rsp + 0x54]; lea r8, [rsp + 0x90]; lea rdx, [rip + 0x2e1f30]; lea rcx, [rip + 0x67dc49]; call 0x14015ed70; lea r9, [rax + 0x20]; mov qword ptr [rsp + 0x20], rax; mov r8, rdi; lea rdx, [rsp + 0x70]; lea rcx, [rip + 0x67dc2c]` |
| `0x00168C56` | `RVA 0x0016E0D0` | `xor edi, edi; mov r10d, dword ptr [rsp + 0x1d0]; cmp dword ptr [rsp + 0x1cc], 0; cmovg r10d, edi; mov eax, dword ptr [r14 + 0x18]; mov dword ptr [rsp + 0x40], eax; mov dword ptr [rsp + 0x38], r10d; mov eax, dword ptr [rsp + 0x58]; mov dword ptr [rsp + 0x30], eax; movzx eax, byte ptr [rsp + 0x1b9]; mov byte ptr [rsp + 0x28], al; mov dword ptr [rsp + 0x20], r13d; mov r9, qword ptr [r15 + 0x10]; mov rcx, qword ptr [rsi + 0x888]` |
| `0x00168FEB` | `RVA 0x00093190` | `xor eax, ecx; xor eax, 0x65; mov byte ptr [rsp + 0x383], al; movsx ecx, byte ptr [rsp + 0x383]; mov eax, dword ptr [rsp + 0x360]; add al, 0x1c; xor eax, ecx; xor eax, 0x72; mov byte ptr [rsp + 0x384], al; xor eax, eax; mov byte ptr [rsp + 0x385], al; movzx eax, byte ptr [rsp + 0x368]; lea rdx, [rsp + 0x3f8]; lea rcx, [rsp + 0x360]` |
| `0x0016903C` | `RVA 0x003D23C8` | `call 0x140093190; nop ; cmp qword ptr [rax + 0x18], 0x10; jb 0x140168ffb; mov rax, qword ptr [rax]; lea rcx, [rip + 0x2ca96e]; mov qword ptr [rsp + 0xc0], rcx; xor ecx, ecx; mov qword ptr [rsp + 0xc8], rcx; mov qword ptr [rsp + 0xd0], rcx; mov qword ptr [rsp + 0x130], rax; mov byte ptr [rsp + 0x138], 1; lea rdx, [rsp + 0xc8]; lea rcx, [rsp + 0x130]` |
| `0x0016905F` | `RVA 0x003D25D0` | `lea rcx, [rip + 0x2ca96e]; mov qword ptr [rsp + 0xc0], rcx; xor ecx, ecx; mov qword ptr [rsp + 0xc8], rcx; mov qword ptr [rsp + 0xd0], rcx; mov qword ptr [rsp + 0x130], rax; mov byte ptr [rsp + 0x138], 1; lea rdx, [rsp + 0xc8]; lea rcx, [rsp + 0x130]; call 0x1403d23c8; lea rax, [rip + 0x2ca940]; mov qword ptr [rsp + 0xc0], rax; lea rdx, [rip + 0x621f09]; lea rcx, [rsp + 0xc0]` |
| `0x00169067` | `RVA 0x00058850` | `mov qword ptr [rsp + 0xc8], rcx; mov qword ptr [rsp + 0xd0], rcx; mov qword ptr [rsp + 0x130], rax; mov byte ptr [rsp + 0x138], 1; lea rdx, [rsp + 0xc8]; lea rcx, [rsp + 0x130]; call 0x1403d23c8; lea rax, [rip + 0x2ca940]; mov qword ptr [rsp + 0xc0], rax; lea rdx, [rip + 0x621f09]; lea rcx, [rsp + 0xc0]; call 0x1403d25d0; nop ; jmp 0x1401690b7` |
| `0x0016909D` | `RVA 0x00059100` | `lea rax, [rip + 0x2ca940]; mov qword ptr [rsp + 0xc0], rax; lea rdx, [rip + 0x621f09]; lea rcx, [rsp + 0xc0]; call 0x1403d25d0; nop ; jmp 0x1401690b7; call 0x140058850; mov dword ptr [rsp + 0x100], r12d; mov qword ptr [rsp + 0x108], rax; movaps xmm0, xmmword ptr [rsp + 0x100]; movdqa xmmword ptr [rsp + 0x160], xmm0; lea rdx, [rsp + 0x160]; lea rcx, [rsp + 0x170]` |
| `0x001690B1` | `RVA 0x003D25D0` | `lea rcx, [rsp + 0xc0]; call 0x1403d25d0; nop ; jmp 0x1401690b7; call 0x140058850; mov dword ptr [rsp + 0x100], r12d; mov qword ptr [rsp + 0x108], rax; movaps xmm0, xmmword ptr [rsp + 0x100]; movdqa xmmword ptr [rsp + 0x160], xmm0; lea rdx, [rsp + 0x160]; lea rcx, [rsp + 0x170]; call 0x140059100; lea rdx, [rip + 0x6221af]; lea rcx, [rsp + 0x170]` |
| `0x001690C2` | `RVA 0x00084A60` | `call 0x140058850; mov dword ptr [rsp + 0x100], r12d; mov qword ptr [rsp + 0x108], rax; movaps xmm0, xmmword ptr [rsp + 0x100]; movdqa xmmword ptr [rsp + 0x160], xmm0; lea rdx, [rsp + 0x160]; lea rcx, [rsp + 0x170]; call 0x140059100; lea rdx, [rip + 0x6221af]; lea rcx, [rsp + 0x170]; call 0x1403d25d0; nop ; lea rdx, [rsp + 0x280]; mov rcx, rsi` |
| `0x00169160` | `RVA 0x0016ED70` | `movups xmm0, xmmword ptr [rax + 0x10]; movups xmmword ptr [rcx + 0x10], xmm0; movups xmm1, xmmword ptr [rax + 0x20]; movups xmmword ptr [rcx + 0x20], xmm1; movups xmm0, xmmword ptr [rax + 0x30]; movups xmmword ptr [rcx + 0x30], xmm0; movups xmm1, xmmword ptr [rax + 0x40]; movups xmmword ptr [rcx + 0x40], xmm1; mov rax, qword ptr [rax + 0x50]; mov qword ptr [rcx + 0x50], rax; mov r9d, dword ptr [rsp + 0x248]; mov r8d, dword ptr [rsp + 0x1d4]; mov rdx, r14; mov rcx, qword ptr [rsi + 0x888]` |
| `0x0016919C` | `RVA 0x003D25D0` | `mov rdx, r14; mov rcx, qword ptr [rsi + 0x888]; call 0x14016ed70; test eax, eax; je 0x140169425; cmp eax, 2; jne 0x1401691a1; xor eax, eax; mov qword ptr [rsp + 0x80], rax; mov qword ptr [rsp + 0x88], rax; lea rax, [rip + 0x2e2235]; mov qword ptr [rsp + 0x78], rax; lea rdx, [rip + 0x622879]; lea rcx, [rsp + 0x78]` |
| `0x001693AB` | `RVA 0x0021D330` | `movsx ecx, byte ptr [rsp + 0x3ce]; xor ecx, 0x7a; mov byte ptr [rsp + 0x3cf], cl; movsx ecx, byte ptr [rsp + 0x3cf]; xor ecx, 0x71; mov byte ptr [rsp + 0x3d0], cl; movsx ecx, byte ptr [rsp + 0x3d0]; xor ecx, 0x66; mov byte ptr [rsp + 0x3d1], cl; xor eax, eax; mov byte ptr [rsp + 0x3d2], al; movzx eax, byte ptr [rsp + 0x3b8]; lea rdx, [rsp + 0x418]; lea rcx, [rsp + 0x3b0]` |
| `0x001693FC` | `RVA 0x003D23C8` | `call 0x14021d330; nop ; cmp qword ptr [rax + 0x18], 0x10; jb 0x1401693bb; mov rax, qword ptr [rax]; lea rcx, [rip + 0x2ca5ae]; mov qword ptr [rsp + 0xa8], rcx; xor ecx, ecx; mov qword ptr [rsp + 0xb0], rcx; mov qword ptr [rsp + 0xb8], rcx; mov qword ptr [rsp + 0x110], rax; mov byte ptr [rsp + 0x118], 1; lea rdx, [rsp + 0xb0]; lea rcx, [rsp + 0x110]` |
| `0x0016941F` | `RVA 0x003D25D0` | `lea rcx, [rip + 0x2ca5ae]; mov qword ptr [rsp + 0xa8], rcx; xor ecx, ecx; mov qword ptr [rsp + 0xb0], rcx; mov qword ptr [rsp + 0xb8], rcx; mov qword ptr [rsp + 0x110], rax; mov byte ptr [rsp + 0x118], 1; lea rdx, [rsp + 0xb0]; lea rcx, [rsp + 0x110]; call 0x1403d23c8; lea rax, [rip + 0x2ca580]; mov qword ptr [rsp + 0xa8], rax; lea rdx, [rip + 0x621b49]; lea rcx, [rsp + 0xa8]` |
| `0x00169428` | `RVA 0x00169520` | `mov qword ptr [rsp + 0xb0], rcx; mov qword ptr [rsp + 0xb8], rcx; mov qword ptr [rsp + 0x110], rax; mov byte ptr [rsp + 0x118], 1; lea rdx, [rsp + 0xb0]; lea rcx, [rsp + 0x110]; call 0x1403d23c8; lea rax, [rip + 0x2ca580]; mov qword ptr [rsp + 0xa8], rax; lea rdx, [rip + 0x621b49]; lea rcx, [rsp + 0xa8]; call 0x1403d25d0; nop ; mov rcx, rbx` |
| `0x00169454` | `RVA 0x00391AC4` | `lea rdx, [rip + 0x621b49]; lea rcx, [rsp + 0xa8]; call 0x1403d25d0; nop ; mov rcx, rbx; call 0x140169520; mov rax, qword ptr [rsp + 0x60]; movups xmm0, xmmword ptr [rax]; movups xmmword ptr [rsi + 0x860], xmm0; movups xmm1, xmmword ptr [rax + 0x10]; movups xmmword ptr [rsi + 0x870], xmm1; mov eax, dword ptr [r14 + 0x18]; mov dword ptr [rsi + 0x880], eax; mov rcx, rbx` |
| `0x0016945F` | `RVA 0x0039219C` | `mov rcx, rbx; call 0x140169520; mov rax, qword ptr [rsp + 0x60]; movups xmm0, xmmword ptr [rax]; movups xmmword ptr [rsi + 0x860], xmm0; movups xmm1, xmmword ptr [rax + 0x10]; movups xmmword ptr [rsi + 0x870], xmm1; mov eax, dword ptr [r14 + 0x18]; mov dword ptr [rsi + 0x880], eax; mov rcx, rbx; call 0x140391ac4; test eax, eax; je 0x140169464; mov ecx, eax` |
| `0x0016949E` | `RVA 0x003B24C0` | `test eax, eax; je 0x14016947e; mov ecx, eax; call 0x14039219c; nop ; lea rcx, [rbx + 0x50]; call 0x140391e8c; test eax, eax; je 0x140169493; mov ecx, eax; call 0x14039219c; nop ; mov rcx, qword ptr [rsp + 0x438]; xor rcx, rsp` |

## Full body

```asm
0x001688D0: mov rax, rsp
0x001688D3: push rdi
0x001688D4: push r12
0x001688D6: push r13
0x001688D8: push r14
0x001688DA: push r15
0x001688DC: sub rsp, 0x440
0x001688E3: mov qword ptr [rax - 0x318], 0xfffffffffffffffe
0x001688EE: mov qword ptr [rax + 0x10], rbx
0x001688F2: mov qword ptr [rax + 0x20], rsi
0x001688F6: mov rax, qword ptr [rip + 0x66dff3]
0x001688FD: xor rax, rsp
0x00168900: mov qword ptr [rsp + 0x438], rax
0x00168908: mov r14, r8
0x0016890B: mov qword ptr [rsp + 0x60], rdx
0x00168910: mov rsi, rcx
0x00168913: mov qword ptr [rsp + 0x98], rcx
0x0016891B: lea rbx, [rcx + 0x7c0]
0x00168922: mov rcx, rbx
0x00168925: call 0x140169520
0x0016892A: xor eax, eax
0x0016892C: mov byte ptr [rsp + 0x50], al
0x00168930: mov qword ptr [rsi + 0x860], rax
0x00168937: mov qword ptr [rsi + 0x868], rax
0x0016893E: mov qword ptr [rsi + 0x870], rax
0x00168945: mov qword ptr [rsi + 0x878], rax
0x0016894C: mov rcx, rbx
0x0016894F: call 0x140391ac4
0x00168954: test eax, eax
0x00168956: je 0x14016895f
0x00168958: mov ecx, eax
0x0016895A: call 0x14039219c
0x0016895F: xor edi, edi
0x00168961: mov dword ptr [rbx + 0x98], edi
0x00168967: mov rcx, rbx
0x0016896A: call 0x140391b24
0x0016896F: test eax, eax
0x00168971: je 0x14016897b
0x00168973: mov ecx, eax
0x00168975: call 0x14039219c
0x0016897A: nop
0x0016897B: lea rcx, [rbx + 0x50]
0x0016897F: call 0x140391e8c
0x00168984: test eax, eax
0x00168986: je 0x140168990
0x00168988: mov ecx, eax
0x0016898A: call 0x14039219c
0x0016898F: nop
0x00168990: movsxd rax, dword ptr [rsi + 0x98]
0x00168997: imul r15, rax, 0xa8
0x0016899E: add r15, qword ptr [rip + 0x67da63]
0x001689A5: lea rdx, [rsp + 0x1a0]
0x001689AD: mov rcx, rsi
0x001689B0: call 0x140084a60
0x001689B5: xor dl, dl
0x001689B7: mov eax, dword ptr [r14 + 0x18]
0x001689BB: mov ecx, dword ptr [rsi + 0x880]
0x001689C1: cmp eax, ecx
0x001689C3: je 0x1401689fe
0x001689C5: test eax, eax
0x001689C7: js 0x1401689e7
0x001689C9: cmp eax, 1
0x001689CC: jle 0x1401689df
0x001689CE: cmp eax, 3
0x001689D1: jle 0x1401689e7
0x001689D3: cmp eax, 4
0x001689D6: jne 0x1401689e7
0x001689D8: cmp ecx, eax
0x001689DA: setne al
0x001689DD: jmp 0x1401689e9
0x001689DF: cmp ecx, 1
0x001689E2: seta al
0x001689E5: jmp 0x1401689e9
0x001689E7: mov al, 1
0x001689E9: movzx edx, al
0x001689EC: mov r12d, 1
0x001689F2: cmp ecx, 0x3e8
0x001689F8: cmove edx, r12d
0x001689FC: jmp 0x140168a04
0x001689FE: mov r12d, 1
0x00168A04: mov r13d, dword ptr [rsp + 0x1b4]
0x00168A0C: cmp dword ptr [rsp + 0x1cc], 0
0x00168A14: jg 0x140168a1f
0x00168A16: test r13d, r13d
0x00168A19: je 0x140168a1f
0x00168A1B: test dl, dl
0x00168A1D: je 0x140168a98
0x00168A1F: mov rcx, rbx
0x00168A22: call 0x140169520
0x00168A27: mov rdi, qword ptr [rsi + 0x888]
0x00168A2E: mov qword ptr [rsi + 0x888], 0
0x00168A39: test rdi, rdi
0x00168A3C: je 0x140168a54
0x00168A3E: mov rcx, rdi
0x00168A41: call 0x14016b960
0x00168A46: mov edx, 0x88
0x00168A4B: mov rcx, rdi
0x00168A4E: call 0x1403b20dc
0x00168A53: nop
0x00168A54: mov rcx, rbx
0x00168A57: call 0x140391ac4
0x00168A5C: test eax, eax
0x00168A5E: je 0x140168a67
0x00168A60: mov ecx, eax
0x00168A62: call 0x14039219c
0x00168A67: xor edi, edi
0x00168A69: mov dword ptr [rbx + 0x98], edi
0x00168A6F: mov rcx, rbx
0x00168A72: call 0x140391b24
0x00168A77: test eax, eax
0x00168A79: je 0x140168a83
0x00168A7B: mov ecx, eax
0x00168A7D: call 0x14039219c
0x00168A82: nop
0x00168A83: lea rcx, [rbx + 0x50]
0x00168A87: call 0x140391e8c
0x00168A8C: test eax, eax
0x00168A8E: je 0x140168a98
0x00168A90: mov ecx, eax
0x00168A92: call 0x14039219c
0x00168A97: nop
0x00168A98: mov edx, dword ptr [r14 + 0x18]
0x00168A9C: mov rcx, qword ptr [r14 + 0x10]
0x00168AA0: call 0x140159b40
0x00168AA5: mov dword ptr [rsp + 0x58], eax
0x00168AA9: cmp qword ptr [rsi + 0x888], 0
0x00168AB1: jne 0x1401690b7
0x00168AB7: mov qword ptr [rsp + 0xd8], rbx
0x00168ABF: mov byte ptr [rsp + 0xe0], 0
0x00168AC7: mov rcx, rbx
0x00168ACA: call 0x140169520
0x00168ACF: mov byte ptr [rsp + 0xe0], 1
0x00168AD7: mov ecx, 0x88
0x00168ADC: call 0x1403b2098
0x00168AE1: mov qword ptr [rsp + 0x70], rax
0x00168AE6: test rax, rax
0x00168AE9: je 0x140168aff
0x00168AEB: mov r8d, dword ptr [rsi + 0x98]
0x00168AF2: mov rdx, rsi
0x00168AF5: mov rcx, rax
0x00168AF8: call 0x14016b6e0
0x00168AFD: jmp 0x140168b02
0x00168AFF: mov rax, rdi
0x00168B02: mov rdi, qword ptr [rsi + 0x888]
0x00168B09: mov qword ptr [rsi + 0x888], rax
0x00168B10: test rdi, rdi
0x00168B13: je 0x140168b2a
0x00168B15: mov rcx, rdi
0x00168B18: call 0x14016b960
0x00168B1D: mov edx, 0x88
0x00168B22: mov rcx, rdi
0x00168B25: call 0x1403b20dc
0x00168B2A: test rbx, rbx
0x00168B2D: je 0x140169067
0x00168B33: mov rcx, rbx
0x00168B36: call 0x14016aaf0
0x00168B3B: mov byte ptr [rsp + 0xe0], 0
0x00168B43: mov rdx, qword ptr [r15 + 0x18]
0x00168B47: mov qword ptr [rsp + 0x68], rdx
0x00168B4C: xor edi, edi
0x00168B4E: mov r8d, edi
0x00168B51: cmp qword ptr [rip + 0x67dcd8], rdi
0x00168B58: je 0x140168c11
0x00168B5E: mov rcx, qword ptr [rip + 0x67dcc3]
0x00168B65: mov rax, qword ptr [rcx + 8]
0x00168B69: mov rdi, rcx
0x00168B6C: cmp byte ptr [rax + 0x19], r8b
0x00168B70: jne 0x140168b8a
0x00168B72: cmp qword ptr [rax + 0x20], rdx
0x00168B76: jae 0x140168b7e
0x00168B78: mov rax, qword ptr [rax + 0x10]
0x00168B7C: jmp 0x140168b84
0x00168B7E: mov rdi, rax
0x00168B81: mov rax, qword ptr [rax]
0x00168B84: cmp byte ptr [rax + 0x19], r8b
0x00168B88: je 0x140168b72
0x00168B8A: mov qword ptr [rsp + 0x148], rdi
0x00168B92: mov qword ptr [rsp + 0x140], rcx
0x00168B9A: cmp rdi, rcx
0x00168B9D: je 0x140168bac
0x00168B9F: cmp rdx, qword ptr [rdi + 0x20]
0x00168BA3: jb 0x140168bac
0x00168BA5: mov byte ptr [rsp + 0x51], r8b
0x00168BAA: jmp 0x140168c0b
0x00168BAC: mov byte ptr [rsp + 0x52], 1
0x00168BB1: xor eax, eax
0x00168BB3: mov byte ptr [rsp + 0x53], al
0x00168BB7: lea rax, [rsp + 0x68]
0x00168BBC: mov qword ptr [rsp + 0x90], rax
0x00168BC4: lea r9, [rsp + 0x54]
0x00168BC9: lea r8, [rsp + 0x90]
0x00168BD1: lea rdx, [rip + 0x2e1f30]
0x00168BD8: lea rcx, [rip + 0x67dc49]
0x00168BDF: call 0x14015ed70
0x00168BE4: lea r9, [rax + 0x20]
0x00168BE8: mov qword ptr [rsp + 0x20], rax
0x00168BED: mov r8, rdi
0x00168BF0: lea rdx, [rsp + 0x70]
0x00168BF5: lea rcx, [rip + 0x67dc2c]
0x00168BFC: call 0x14015f0b0
0x00168C01: mov rdi, qword ptr [rsp + 0x70]
0x00168C06: mov rdx, qword ptr [rsp + 0x68]
0x00168C0B: mov r8, qword ptr [rdi + 0x28]
0x00168C0F: xor edi, edi
0x00168C11: mov r10d, dword ptr [rsp + 0x1d0]
0x00168C19: cmp dword ptr [rsp + 0x1cc], 0
0x00168C21: cmovg r10d, edi
0x00168C25: mov eax, dword ptr [r14 + 0x18]
0x00168C29: mov dword ptr [rsp + 0x40], eax
0x00168C2D: mov dword ptr [rsp + 0x38], r10d
0x00168C32: mov eax, dword ptr [rsp + 0x58]
0x00168C36: mov dword ptr [rsp + 0x30], eax
0x00168C3A: movzx eax, byte ptr [rsp + 0x1b9]
0x00168C42: mov byte ptr [rsp + 0x28], al
0x00168C46: mov dword ptr [rsp + 0x20], r13d
0x00168C4B: mov r9, qword ptr [r15 + 0x10]
0x00168C4F: mov rcx, qword ptr [rsi + 0x888]
0x00168C56: call 0x14016e0d0
0x00168C5B: test al, al
0x00168C5D: jne 0x140169065
0x00168C63: mov dword ptr [rsp + 0x360], 0x34
0x00168C6E: mov eax, dword ptr [rsp + 0x360]
0x00168C75: add al, 0x34
0x00168C77: movsx ecx, al
0x00168C7A: xor ecx, 0x53
0x00168C7D: mov dword ptr [rsp + 0x364], ecx
0x00168C84: mov eax, dword ptr [rsp + 0x364]
0x00168C8B: mov ecx, dword ptr [rsp + 0x360]
0x00168C92: xor ecx, eax
0x00168C94: xor ecx, 0x55
0x00168C97: mov byte ptr [rsp + 0x368], cl
0x00168C9E: movsx ecx, byte ptr [rsp + 0x368]
0x00168CA6: mov eax, dword ptr [rsp + 0x360]
0x00168CAD: inc al
0x00168CAF: xor eax, ecx
0x00168CB1: xor eax, 0x6e
0x00168CB4: mov byte ptr [rsp + 0x369], al
0x00168CBB: movsx ecx, byte ptr [rsp + 0x369]
0x00168CC3: mov eax, dword ptr [rsp + 0x360]
0x00168CCA: add al, 2
0x00168CCC: xor eax, ecx
0x00168CCE: xor eax, 0x61
0x00168CD1: mov byte ptr [rsp + 0x36a], al
0x00168CD8: movsx ecx, byte ptr [rsp + 0x36a]
0x00168CE0: mov eax, dword ptr [rsp + 0x360]
0x00168CE7: add al, 3
0x00168CE9: xor eax, ecx
0x00168CEB: xor eax, 0x62
0x00168CEE: mov byte ptr [rsp + 0x36b], al
0x00168CF5: movsx ecx, byte ptr [rsp + 0x36b]
0x00168CFD: mov eax, dword ptr [rsp + 0x360]
0x00168D04: add al, 4
0x00168D06: xor eax, ecx
0x00168D08: xor eax, 0x6c
0x00168D0B: mov byte ptr [rsp + 0x36c], al
0x00168D12: movsx ecx, byte ptr [rsp + 0x36c]
0x00168D1A: mov eax, dword ptr [rsp + 0x360]
0x00168D21: add al, 5
0x00168D23: xor eax, ecx
0x00168D25: xor eax, 0x65
0x00168D28: mov byte ptr [rsp + 0x36d], al
0x00168D2F: movsx ecx, byte ptr [rsp + 0x36d]
0x00168D37: mov eax, dword ptr [rsp + 0x360]
0x00168D3E: add al, 6
0x00168D40: xor eax, ecx
0x00168D42: xor eax, 0x20
0x00168D45: mov byte ptr [rsp + 0x36e], al
0x00168D4C: movsx ecx, byte ptr [rsp + 0x36e]
0x00168D54: mov eax, dword ptr [rsp + 0x360]
0x00168D5B: add al, 7
0x00168D5D: xor eax, ecx
0x00168D5F: xor eax, 0x74
0x00168D62: mov byte ptr [rsp + 0x36f], al
0x00168D69: movsx ecx, byte ptr [rsp + 0x36f]
0x00168D71: mov eax, dword ptr [rsp + 0x360]
0x00168D78: add al, 8
0x00168D7A: xor eax, ecx
0x00168D7C: xor eax, 0x6f
0x00168D7F: mov byte ptr [rsp + 0x370], al
0x00168D86: movsx ecx, byte ptr [rsp + 0x370]
0x00168D8E: mov eax, dword ptr [rsp + 0x360]
0x00168D95: add al, 9
0x00168D97: xor eax, ecx
0x00168D99: xor eax, 0x20
0x00168D9C: mov byte ptr [rsp + 0x371], al
0x00168DA3: movsx ecx, byte ptr [rsp + 0x371]
0x00168DAB: mov eax, dword ptr [rsp + 0x360]
0x00168DB2: add al, 0xa
0x00168DB4: xor eax, ecx
0x00168DB6: xor eax, 0x63
0x00168DB9: mov byte ptr [rsp + 0x372], al
0x00168DC0: movsx ecx, byte ptr [rsp + 0x372]
0x00168DC8: mov eax, dword ptr [rsp + 0x360]
0x00168DCF: add al, 0xb
0x00168DD1: xor eax, ecx
0x00168DD3: xor eax, 0x72
0x00168DD6: mov byte ptr [rsp + 0x373], al
0x00168DDD: movsx ecx, byte ptr [rsp + 0x373]
0x00168DE5: mov eax, dword ptr [rsp + 0x360]
0x00168DEC: add al, 0xc
0x00168DEE: xor eax, ecx
0x00168DF0: xor eax, 0x65
0x00168DF3: mov byte ptr [rsp + 0x374], al
0x00168DFA: movsx ecx, byte ptr [rsp + 0x374]
0x00168E02: mov eax, dword ptr [rsp + 0x360]
0x00168E09: add al, 0xd
0x00168E0B: xor eax, ecx
0x00168E0D: xor eax, 0x61
0x00168E10: mov byte ptr [rsp + 0x375], al
0x00168E17: movsx ecx, byte ptr [rsp + 0x375]
0x00168E1F: mov eax, dword ptr [rsp + 0x360]
0x00168E26: add al, 0xe
0x00168E28: xor eax, ecx
0x00168E2A: xor eax, 0x74
0x00168E2D: mov byte ptr [rsp + 0x376], al
0x00168E34: movsx ecx, byte ptr [rsp + 0x376]
0x00168E3C: mov eax, dword ptr [rsp + 0x360]
0x00168E43: add al, 0xf
0x00168E45: xor eax, ecx
0x00168E47: xor eax, 0x65
0x00168E4A: mov byte ptr [rsp + 0x377], al
0x00168E51: movsx ecx, byte ptr [rsp + 0x377]
0x00168E59: mov eax, dword ptr [rsp + 0x360]
0x00168E60: add al, 0x10
0x00168E62: xor eax, ecx
0x00168E64: xor eax, 0x20
0x00168E67: mov byte ptr [rsp + 0x378], al
0x00168E6E: movsx ecx, byte ptr [rsp + 0x378]
0x00168E76: mov eax, dword ptr [rsp + 0x360]
0x00168E7D: add al, 0x11
0x00168E7F: xor eax, ecx
0x00168E81: xor eax, 0x4f
0x00168E84: mov byte ptr [rsp + 0x379], al
0x00168E8B: movsx ecx, byte ptr [rsp + 0x379]
0x00168E93: mov eax, dword ptr [rsp + 0x360]
0x00168E9A: add al, 0x12
0x00168E9C: xor eax, ecx
0x00168E9E: xor eax, 0x70
0x00168EA1: mov byte ptr [rsp + 0x37a], al
0x00168EA8: movsx ecx, byte ptr [rsp + 0x37a]
0x00168EB0: mov eax, dword ptr [rsp + 0x360]
0x00168EB7: add al, 0x13
0x00168EB9: xor eax, ecx
0x00168EBB: xor eax, 0x65
0x00168EBE: mov byte ptr [rsp + 0x37b], al
0x00168EC5: movsx ecx, byte ptr [rsp + 0x37b]
0x00168ECD: mov eax, dword ptr [rsp + 0x360]
0x00168ED4: add al, 0x14
0x00168ED6: xor eax, ecx
0x00168ED8: xor eax, 0x6e
0x00168EDB: mov byte ptr [rsp + 0x37c], al
0x00168EE2: movsx ecx, byte ptr [rsp + 0x37c]
0x00168EEA: mov eax, dword ptr [rsp + 0x360]
0x00168EF1: add al, 0x15
0x00168EF3: xor eax, ecx
0x00168EF5: xor eax, 0x43
0x00168EF8: mov byte ptr [rsp + 0x37d], al
0x00168EFF: movsx ecx, byte ptr [rsp + 0x37d]
0x00168F07: mov eax, dword ptr [rsp + 0x360]
0x00168F0E: add al, 0x16
0x00168F10: xor eax, ecx
0x00168F12: xor eax, 0x4c
0x00168F15: mov byte ptr [rsp + 0x37e], al
0x00168F1C: movsx ecx, byte ptr [rsp + 0x37e]
0x00168F24: mov eax, dword ptr [rsp + 0x360]
0x00168F2B: add al, 0x17
0x00168F2D: xor eax, ecx
0x00168F2F: xor eax, 0x20
0x00168F32: mov byte ptr [rsp + 0x37f], al
0x00168F39: movsx ecx, byte ptr [rsp + 0x37f]
0x00168F41: mov eax, dword ptr [rsp + 0x360]
0x00168F48: add al, 0x18
0x00168F4A: xor eax, ecx
0x00168F4C: xor eax, 0x6d
0x00168F4F: mov byte ptr [rsp + 0x380], al
0x00168F56: movsx ecx, byte ptr [rsp + 0x380]
0x00168F5E: mov eax, dword ptr [rsp + 0x360]
0x00168F65: add al, 0x19
0x00168F67: xor eax, ecx
0x00168F69: xor eax, 0x69
0x00168F6C: mov byte ptr [rsp + 0x381], al
0x00168F73: movsx ecx, byte ptr [rsp + 0x381]
0x00168F7B: mov eax, dword ptr [rsp + 0x360]
0x00168F82: add al, 0x1a
0x00168F84: xor eax, ecx
0x00168F86: xor eax, 0x6e
0x00168F89: mov byte ptr [rsp + 0x382], al
0x00168F90: movsx ecx, byte ptr [rsp + 0x382]
0x00168F98: mov eax, dword ptr [rsp + 0x360]
0x00168F9F: add al, 0x1b
0x00168FA1: xor eax, ecx
0x00168FA3: xor eax, 0x65
0x00168FA6: mov byte ptr [rsp + 0x383], al
0x00168FAD: movsx ecx, byte ptr [rsp + 0x383]
0x00168FB5: mov eax, dword ptr [rsp + 0x360]
0x00168FBC: add al, 0x1c
0x00168FBE: xor eax, ecx
0x00168FC0: xor eax, 0x72
0x00168FC3: mov byte ptr [rsp + 0x384], al
0x00168FCA: xor eax, eax
0x00168FCC: mov byte ptr [rsp + 0x385], al
0x00168FD3: movzx eax, byte ptr [rsp + 0x368]
0x00168FDB: lea rdx, [rsp + 0x3f8]
0x00168FE3: lea rcx, [rsp + 0x360]
0x00168FEB: call 0x140093190
0x00168FF0: nop
0x00168FF1: cmp qword ptr [rax + 0x18], 0x10
0x00168FF6: jb 0x140168ffb
0x00168FF8: mov rax, qword ptr [rax]
0x00168FFB: lea rcx, [rip + 0x2ca96e]
0x00169002: mov qword ptr [rsp + 0xc0], rcx
0x0016900A: xor ecx, ecx
0x0016900C: mov qword ptr [rsp + 0xc8], rcx
0x00169014: mov qword ptr [rsp + 0xd0], rcx
0x0016901C: mov qword ptr [rsp + 0x130], rax
0x00169024: mov byte ptr [rsp + 0x138], 1
0x0016902C: lea rdx, [rsp + 0xc8]
0x00169034: lea rcx, [rsp + 0x130]
0x0016903C: call 0x1403d23c8
0x00169041: lea rax, [rip + 0x2ca940]
0x00169048: mov qword ptr [rsp + 0xc0], rax
0x00169050: lea rdx, [rip + 0x621f09]
0x00169057: lea rcx, [rsp + 0xc0]
0x0016905F: call 0x1403d25d0
0x00169064: nop
0x00169065: jmp 0x1401690b7
0x00169067: call 0x140058850
0x0016906C: mov dword ptr [rsp + 0x100], r12d
0x00169074: mov qword ptr [rsp + 0x108], rax
0x0016907C: movaps xmm0, xmmword ptr [rsp + 0x100]
0x00169084: movdqa xmmword ptr [rsp + 0x160], xmm0
0x0016908D: lea rdx, [rsp + 0x160]
0x00169095: lea rcx, [rsp + 0x170]
0x0016909D: call 0x140059100
0x001690A2: lea rdx, [rip + 0x6221af]
0x001690A9: lea rcx, [rsp + 0x170]
0x001690B1: call 0x1403d25d0
0x001690B6: nop
0x001690B7: lea rdx, [rsp + 0x280]
0x001690BF: mov rcx, rsi
0x001690C2: call 0x140084a60
0x001690C7: lea rcx, [rsp + 0x1a0]
0x001690CF: movups xmm0, xmmword ptr [rax]
0x001690D2: movups xmmword ptr [rcx], xmm0
0x001690D5: movups xmm1, xmmword ptr [rax + 0x10]
0x001690D9: movups xmmword ptr [rcx + 0x10], xmm1
0x001690DD: movups xmm0, xmmword ptr [rax + 0x20]
0x001690E1: movups xmmword ptr [rcx + 0x20], xmm0
0x001690E5: movups xmm1, xmmword ptr [rax + 0x30]
0x001690E9: movups xmmword ptr [rcx + 0x30], xmm1
0x001690ED: movups xmm0, xmmword ptr [rax + 0x40]
0x001690F1: movups xmmword ptr [rcx + 0x40], xmm0
0x001690F5: movups xmm1, xmmword ptr [rax + 0x50]
0x001690F9: movups xmmword ptr [rcx + 0x50], xmm1
0x001690FD: movups xmm0, xmmword ptr [rax + 0x60]
0x00169101: movups xmmword ptr [rcx + 0x60], xmm0
0x00169105: lea rcx, [rcx + 0x80]
0x0016910C: movups xmm0, xmmword ptr [rax + 0x70]
0x00169110: movups xmmword ptr [rcx - 0x10], xmm0
0x00169114: sub rax, -0x80
0x00169118: movups xmm1, xmmword ptr [rax]
0x0016911B: movups xmmword ptr [rcx], xmm1
0x0016911E: movups xmm0, xmmword ptr [rax + 0x10]
0x00169122: movups xmmword ptr [rcx + 0x10], xmm0
0x00169126: movups xmm1, xmmword ptr [rax + 0x20]
0x0016912A: movups xmmword ptr [rcx + 0x20], xmm1
0x0016912E: movups xmm0, xmmword ptr [rax + 0x30]
0x00169132: movups xmmword ptr [rcx + 0x30], xmm0
0x00169136: movups xmm1, xmmword ptr [rax + 0x40]
0x0016913A: movups xmmword ptr [rcx + 0x40], xmm1
0x0016913E: mov rax, qword ptr [rax + 0x50]
0x00169142: mov qword ptr [rcx + 0x50], rax
0x00169146: mov r9d, dword ptr [rsp + 0x248]
0x0016914E: mov r8d, dword ptr [rsp + 0x1d4]
0x00169156: mov rdx, r14
0x00169159: mov rcx, qword ptr [rsi + 0x888]
0x00169160: call 0x14016ed70
0x00169165: test eax, eax
0x00169167: je 0x140169425
0x0016916D: cmp eax, 2
0x00169170: jne 0x1401691a1
0x00169172: xor eax, eax
0x00169174: mov qword ptr [rsp + 0x80], rax
0x0016917C: mov qword ptr [rsp + 0x88], rax
0x00169184: lea rax, [rip + 0x2e2235]
0x0016918B: mov qword ptr [rsp + 0x78], rax
0x00169190: lea rdx, [rip + 0x622879]
0x00169197: lea rcx, [rsp + 0x78]
0x0016919C: call 0x1403d25d0
0x001691A1: mov dword ptr [rsp + 0x3b0], 0x14
0x001691AC: mov dword ptr [rsp + 0x3b4], 0x2a
0x001691B7: mov eax, dword ptr [rsp + 0x3b4]
0x001691BE: xor eax, 0x41
0x001691C1: mov byte ptr [rsp + 0x3b8], al
0x001691C8: movsx ecx, byte ptr [rsp + 0x3b8]
0x001691D0: xor ecx, 0x7a
0x001691D3: mov byte ptr [rsp + 0x3b9], cl
0x001691DA: movsx ecx, byte ptr [rsp + 0x3b9]
0x001691E2: xor ecx, 0x75
0x001691E5: mov byte ptr [rsp + 0x3ba], cl
0x001691EC: movsx ecx, byte ptr [rsp + 0x3ba]
0x001691F4: xor ecx, 0x76
0x001691F7: mov byte ptr [rsp + 0x3bb], cl
0x001691FE: movsx ecx, byte ptr [rsp + 0x3bb]
0x00169206: xor ecx, 0x78
0x00169209: mov byte ptr [rsp + 0x3bc], cl
0x00169210: movsx ecx, byte ptr [rsp + 0x3bc]
0x00169218: xor ecx, 0x71
0x0016921B: mov byte ptr [rsp + 0x3bd], cl
0x00169222: movsx ecx, byte ptr [rsp + 0x3bd]
0x0016922A: xor ecx, 0x34
0x0016922D: mov byte ptr [rsp + 0x3be], cl
0x00169234: movsx ecx, byte ptr [rsp + 0x3be]
0x0016923C: xor ecx, 0x60
0x0016923F: mov byte ptr [rsp + 0x3bf], cl
0x00169246: movsx ecx, byte ptr [rsp + 0x3bf]
0x0016924E: xor ecx, 0x7b
0x00169251: mov byte ptr [rsp + 0x3c0], cl
0x00169258: movsx ecx, byte ptr [rsp + 0x3c0]
0x00169260: xor ecx, 0x34
0x00169263: mov byte ptr [rsp + 0x3c1], cl
0x0016926A: movsx ecx, byte ptr [rsp + 0x3c1]
0x00169272: xor ecx, 0x7d
0x00169275: mov byte ptr [rsp + 0x3c2], cl
0x0016927C: movsx ecx, byte ptr [rsp + 0x3c2]
0x00169284: xor ecx, 0x7a
0x00169287: mov byte ptr [rsp + 0x3c3], cl
0x0016928E: movsx ecx, byte ptr [rsp + 0x3c3]
0x00169296: xor ecx, 0x7d
0x00169299: mov byte ptr [rsp + 0x3c4], cl
0x001692A0: movsx ecx, byte ptr [rsp + 0x3c4]
0x001692A8: xor ecx, 0x60
0x001692AB: mov byte ptr [rsp + 0x3c5], cl
0x001692B2: movsx ecx, byte ptr [rsp + 0x3c5]
0x001692BA: xor ecx, 0x7d
0x001692BD: mov byte ptr [rsp + 0x3c6], cl
0x001692C4: movsx ecx, byte ptr [rsp + 0x3c6]
0x001692CC: xor ecx, 0x75
0x001692CF: mov byte ptr [rsp + 0x3c7], cl
0x001692D6: movsx ecx, byte ptr [rsp + 0x3c7]
0x001692DE: xor ecx, 0x78
0x001692E1: mov byte ptr [rsp + 0x3c8], cl
0x001692E8: movsx ecx, byte ptr [rsp + 0x3c8]
0x001692F0: xor ecx, 0x7d
0x001692F3: mov byte ptr [rsp + 0x3c9], cl
0x001692FA: movsx ecx, byte ptr [rsp + 0x3c9]
0x00169302: xor ecx, 0x6e
0x00169305: mov byte ptr [rsp + 0x3ca], cl
0x0016930C: movsx ecx, byte ptr [rsp + 0x3ca]
0x00169314: xor ecx, 0x71
0x00169317: mov byte ptr [rsp + 0x3cb], cl
0x0016931E: movsx ecx, byte ptr [rsp + 0x3cb]
0x00169326: xor ecx, 0x34
0x00169329: mov byte ptr [rsp + 0x3cc], cl
0x00169330: movsx ecx, byte ptr [rsp + 0x3cc]
0x00169338: xor ecx, 0x79
0x0016933B: mov byte ptr [rsp + 0x3cd], cl
0x00169342: movsx ecx, byte ptr [rsp + 0x3cd]
0x0016934A: xor ecx, 0x7d
0x0016934D: mov byte ptr [rsp + 0x3ce], cl
0x00169354: movsx ecx, byte ptr [rsp + 0x3ce]
0x0016935C: xor ecx, 0x7a
0x0016935F: mov byte ptr [rsp + 0x3cf], cl
0x00169366: movsx ecx, byte ptr [rsp + 0x3cf]
0x0016936E: xor ecx, 0x71
0x00169371: mov byte ptr [rsp + 0x3d0], cl
0x00169378: movsx ecx, byte ptr [rsp + 0x3d0]
0x00169380: xor ecx, 0x66
0x00169383: mov byte ptr [rsp + 0x3d1], cl
0x0016938A: xor eax, eax
0x0016938C: mov byte ptr [rsp + 0x3d2], al
0x00169393: movzx eax, byte ptr [rsp + 0x3b8]
0x0016939B: lea rdx, [rsp + 0x418]
0x001693A3: lea rcx, [rsp + 0x3b0]
0x001693AB: call 0x14021d330
0x001693B0: nop
0x001693B1: cmp qword ptr [rax + 0x18], 0x10
0x001693B6: jb 0x1401693bb
0x001693B8: mov rax, qword ptr [rax]
0x001693BB: lea rcx, [rip + 0x2ca5ae]
0x001693C2: mov qword ptr [rsp + 0xa8], rcx
0x001693CA: xor ecx, ecx
0x001693CC: mov qword ptr [rsp + 0xb0], rcx
0x001693D4: mov qword ptr [rsp + 0xb8], rcx
0x001693DC: mov qword ptr [rsp + 0x110], rax
0x001693E4: mov byte ptr [rsp + 0x118], 1
0x001693EC: lea rdx, [rsp + 0xb0]
0x001693F4: lea rcx, [rsp + 0x110]
0x001693FC: call 0x1403d23c8
0x00169401: lea rax, [rip + 0x2ca580]
0x00169408: mov qword ptr [rsp + 0xa8], rax
0x00169410: lea rdx, [rip + 0x621b49]
0x00169417: lea rcx, [rsp + 0xa8]
0x0016941F: call 0x1403d25d0
0x00169424: nop
0x00169425: mov rcx, rbx
0x00169428: call 0x140169520
0x0016942D: mov rax, qword ptr [rsp + 0x60]
0x00169432: movups xmm0, xmmword ptr [rax]
0x00169435: movups xmmword ptr [rsi + 0x860], xmm0
0x0016943C: movups xmm1, xmmword ptr [rax + 0x10]
0x00169440: movups xmmword ptr [rsi + 0x870], xmm1
0x00169447: mov eax, dword ptr [r14 + 0x18]
0x0016944B: mov dword ptr [rsi + 0x880], eax
0x00169451: mov rcx, rbx
0x00169454: call 0x140391ac4
0x00169459: test eax, eax
0x0016945B: je 0x140169464
0x0016945D: mov ecx, eax
0x0016945F: call 0x14039219c
0x00169464: mov dword ptr [rbx + 0x98], edi
0x0016946A: mov rcx, rbx
0x0016946D: call 0x140391b24
0x00169472: test eax, eax
0x00169474: je 0x14016947e
0x00169476: mov ecx, eax
0x00169478: call 0x14039219c
0x0016947D: nop
0x0016947E: lea rcx, [rbx + 0x50]
0x00169482: call 0x140391e8c
0x00169487: test eax, eax
0x00169489: je 0x140169493
0x0016948B: mov ecx, eax
0x0016948D: call 0x14039219c
0x00169492: nop
0x00169493: mov rcx, qword ptr [rsp + 0x438]
0x0016949B: xor rcx, rsp
0x0016949E: call 0x1403b24c0
0x001694A3: lea r11, [rsp + 0x440]
0x001694AB: mov rbx, qword ptr [r11 + 0x38]
0x001694AF: mov rsi, qword ptr [r11 + 0x48]
0x001694B3: mov rsp, r11
0x001694B6: pop r15
0x001694B8: pop r14
0x001694BA: pop r13
0x001694BC: pop r12
0x001694BE: pop rdi
0x001694BF: ret
```