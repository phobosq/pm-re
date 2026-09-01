# NVIDIA child ctor config-record accesses

PDATA `0x001D4A80..0x001D5DC9`

Entry `R9` is copied to `RSI`; `RSI` therefore aliases the original per-GPU `0xD8` config record.

| RVA | disp | timing label | instruction |
|---|---:|---|---|
| `0x001D4BA1` | `0xC0` |  | `cmp dword ptr [rsi + 0xc0], edi` |
| `0x001D4BB0` | `0xC0` |  | `mov eax, dword ptr [rsi + 0xc0]` |

## Timing-field contexts
