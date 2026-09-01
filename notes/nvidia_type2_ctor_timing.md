# NVIDIA Type2 ctor timing-flow trace

PDATA `0x001CDCC0..0x001CDDAC`

Entry `R9` is the original per-GPU config-record pointer.

Observed aliases: `r9, rsi`

| RVA | base | disp | label | instruction |
|---|---|---:|---|---|

## Timing-field contexts


## All calls

| RVA | target/form | nearby config aliases in arg registers |
|---|---|---|
| `0x001CDCEB` | `0x14012f250` |  |
| `0x001CDD07` | `0x140391a94` | rcx<=[rbx + 0x7c0] |
| `0x001CDD53` | `0x1403b2098` |  |
| `0x001CDD6E` | `0x1401d4a80` | r8<=[rbx + 8]; r9<=rsi; rcx<=rax |
| `0x001CDD91` | `qword ptr [rax]` | rcx<=qword ptr [rbx + 0x840] |