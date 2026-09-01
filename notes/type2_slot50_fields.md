# Type2 slot +0x50 snapshot field accesses

snapshot local: `rsp+0xB0` size `0xD8`

| RVA | snapshot off | label | instruction |
|---|---:|---|---|
| `0x001CF949` | `+0x0` |  | `lea rdx, [rsp + 0xb0]` |
| `0x001CF99E` | `+0x2C` |  | `cmp dword ptr [rsp + 0xdc], 0` |
| `0x001CFAD4` | `+0x30` |  | `mov r9d, dword ptr [rsp + 0xe0]` |
| `0x001CFADC` | `+0x2C` |  | `cmp dword ptr [rsp + 0xdc], 0` |
| `0x001CFAFA` | `+0x25` |  | `movzx r9d, byte ptr [rsp + 0xd5]` |
| `0x001CFB03` | `+0x20` |  | `mov r8d, dword ptr [rsp + 0xd0]` |
| `0x001CFB1B` | `+0x34` |  | `mov r8d, dword ptr [rsp + 0xe4]` |

## Contexts for timing-related or late-record fields
