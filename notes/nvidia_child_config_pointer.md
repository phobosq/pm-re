# NVIDIA child ctor: config pointer retention

PDATA `0x001D4A80..0x001D5DC9`

Entry R9 is copied to RSI. This report lists every instruction that explicitly uses RSI as an operand and every store of RSI into memory.

| RVA | kind | instruction |
|---|---|---|
| `0x001D4A83` | RSI-reg | `push rsi` |
| `0x001D4AB6` | RSI-reg | `mov rsi, r9` |
| `0x001D4BA1` | dereference | `cmp dword ptr [rsi + 0xc0], edi` |
| `0x001D4BB0` | dereference | `mov eax, dword ptr [rsi + 0xc0]` |
| `0x001D5DC5` | RSI-reg | `pop rsi` |