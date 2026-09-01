# Dispatcher 0x584A0 address-taken scan

containing PDATA: `0x000584A0..0x00058581`

data refs: 2; code refs: 6

## Data refs

| RVA | section | kind | target |
|---|---|---|---|
| `0x00734A70` | `.rdata` | rva32 | `0x000584A0` |
| `0x007F2D50` | `.pdata` | rva32 | `0x000584A0` |

## Code refs

| RVA | kind | target | instruction |
|---|---|---|---|
| `0x00080066` | rip-mem | `0x000584A0` | `lea rcx, [rip - 0x27bcd]` |
| `0x00080066` | rip-lea | `0x000584A0` | `lea rcx, [rip - 0x27bcd]` |
| `0x000A2F31` | rip-mem | `0x000584A0` | `lea rcx, [rip - 0x4aa98]` |
| `0x000A2F31` | rip-lea | `0x000584A0` | `lea rcx, [rip - 0x4aa98]` |
| `0x000A4DCC` | rip-mem | `0x000584A0` | `lea rcx, [rip - 0x4c933]` |
| `0x000A4DCC` | rip-lea | `0x000584A0` | `lea rcx, [rip - 0x4c933]` |