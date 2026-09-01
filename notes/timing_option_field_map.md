# Timing option -> descriptor -> per-GPU field map

| option | literal anchor | ctor | vtable | setter +0x10 | field |
|---|---|---|---|---|---|
| mt | `0x000E8D60` | `0x000DD7B0` | `0x0043F078` | `0x000E1740` | `+0x98` |
| straps | `0x000E8E2C` | `0x000DD510` | `0x0043F0B0` | `0x000E0F00` | `+0xAC` |
| vmr | `0x000E8F6E` | `0x000DD570` | `0x0043F0E8` | `0x000E10C0` | `+0xB0` |
| rxboost | `0x000E9026` | `0x000DD5F0` | `0x0043F120` | `0x000E1180` | `+0xB0` |
| vmt2 | `0x000E9245` | `0x000DD650` | `0x0043F190` | `0x000E12B0` | `+0xB8` |
| vmt3 | `0x000E931D` | `0x000DD6F0` | `0x0043F1C8` | `0x000E1550` | `+0xBC` |
| vmdag | `0x000E94BD` | `0x000DD730` | `0x0043F238` | `0x000E16B0` | — |
| leavemt | `0x000EEE36` | — | — | — | — |

## Candidate 0xDDxxx calls after each literal anchor

- **mt**: `0x000E8E02->0x000DD7B0`
- **straps**: `0x000E8F36->0x000DD510`
- **vmr**: `0x000E8FFC->0x000DD570`
- **rxboost**: `0x000E914A->0x000DD5F0`
- **vmt2**: `0x000E92E5->0x000DD650`, `0x000E93BD->0x000DD6F0`
- **vmt3**: `0x000E93BD->0x000DD6F0`, `0x000E9493->0x000DD670`
- **vmdag**: `0x000E95AD->0x000DD730`
- **leavemt**: none