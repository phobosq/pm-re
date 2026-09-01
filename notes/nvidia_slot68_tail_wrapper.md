# NVIDIA child mode-setter tail wrapper 0x16E0B0

`0x16E0B0` replaces RCX with `[wrapper+0x80]` and tail-jumps to child vtable slot +0x68, preserving RDX/R8/R9.

direct callers: `0`

## Data refs
