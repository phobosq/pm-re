# vmr Static Call Graph — Session 2 Findings
# Confidence key: confirmed / strongly_inferred / hypothesis / unknown

## Executive Summary

Static call-graph analysis (session 2) mapped 7 key function ranges across parser and transport regions.
No direct parser→transport call chain found. Connection is via shared global data (hypothesis).

## Confirmed Call Chain: Transport Stack

```
CALLER_THUNK  0x001C55F0..0x001C563E (78B)   <- 0x001833F0..0x00183453 (L3, 99B)
CALLER_MAIN   0x001C5640..0x001C5985 (837B)  <- 0x00186880..0x00186921 (L3, 161B)
     |
     | CALL (rel32)
     v
DISP01        0x001C3A30..0x001C400E (1502B)  [transport_dispatcher_AB]
     |            |
     | CALL         | CALL
     v              v
TR01          TR02  0x001C1BB0 (ioctl_cluster_A1)
0x001C4010..0x001C44E3
     |
     | CALL @ 0x001C44B5
     v
TR03  0x001C6BB0..0x001C6C93 (ioctl_cluster_B)
```

Evidence: confirmed (pdata exhaustive parse + CALL rel32 scan)

## Parser Region Call Topology

```
DPRB01  0x00395CA8..0x00396008 (864B)   <- 0x003939B8..0x00393A85 (205B)
  calls: PR02 (parser_compare_A @ 0x003B160C), string helpers 0x003F0A60, 0x003B2500, 0x003F0948

DPRB04  0x004052CC..0x0040565E (914B)   <- 0x00405660..0x004056E9 (137B)
  calls: PR03 (parser_compare_B @ 0x003F9610), string helpers 0x003F0A60, 0x003B2500, 0x003F0948

PR02  0x003B160C..0x003B16C8 (188B)  <- DPRB01, DPRB02
PR03  0x003F9610..0x003F96FF (239B)  <- DPRB03, DPRB04
PR01  0x003E16B0..0x003E16D5 (37B)   <- no direct CALL callers (called via func-ptr / vtable)
```

Evidence: confirmed (pdata + CALL scan)

## Key Negative Result: No Direct Parser→Transport Link

The parser region (0x003B–0x0040) has no direct CALL rel32 edges into the transport region (0x001C).
The two regions operate independently in terms of direct call flow.

Implication: vmr value is passed through shared global data (heap struct or global variable),
NOT through a direct function call from parser to transport.

## Disproven Hypothesis: 0x003B24C0 as Config Accessor

0x003B24C0 is __security_check_cookie (MSVC stack canary).
Bytes: 48 3B 0D ... (CMP RCX, [RIP+disp]) → rotate → REPNZ RET → JMP __report_gsfailure
Appears everywhere because MSVC emits it at every function epilog with a stack frame.
Evidence: strongly_inferred (byte-level decode matches known pattern)

## New Targets: String Helper Functions Called by Both Parser Callers

These appear in BOTH DPRB01 and DPRB04, suggesting they are the compare infrastructure:
- 0x003F0A60 (called 2x in each) — compare/classify helper
- 0x003B2500 (called 2x in each) — compare/classify helper
- 0x003F0948 (called 2x in each) — compare/classify helper
- 0x003F0B44 (called 2x in each, unknown_pdata) — inner compare primitive

These likely implement string comparison chains (strcmp-style wrappers around CompareStringW).

## Recommended Next Steps

1. Dump 40+ bytes from 0x003F0A60 and 0x003B2500 to check for CompareStringW indirect call
2. Find callers of L3 functions (0x001833F0, 0x00186880) to reach L4 — possible app-level dispatcher
3. For runtime: set breakpoints at DISP01 entry (0x001C3A30) and log RCX/RDX args;
   if vmr value is an arg, it was passed from L3 caller
4. For global-data hypothesis: scan for LEA RIP+disp / MOV patterns in PR02/PR03 that write to
   a specific global address, then check if DISP01 reads from the same address

## Evidence Classification Updates

C12: DISP01 (0x001C3A30) is the single transport dispatcher for TR01+TR02 — confirmed
C13: TR01 calls TR03 directly (0x001C44B5) — confirmed
C14: Parser and transport have no direct call chain — confirmed (negative result)
C15: 0x003B24C0 is __security_check_cookie, not config accessor — strongly_inferred
H08: vmr config stored in shared global struct accessed by both parser and transport — hypothesis

## Artifacts Produced This Session

notes/vmr_call_graph.csv        — 43 outbound edges from 7 ranges
notes/vmr_call_graph.md         — call graph summary
notes/vmr_callers.csv           — 9 caller edges to target functions
notes/vmr_callers.md            — callers summary
notes/vmr_caller_funcs.csv/md   — pdata resolution of caller functions
notes/vmr_dispatch_analysis.md  — import-API check for dispatcher functions
notes/vmr_disp01_chain.md       — DISP01 outbound + its callers
notes/vmr_level2_chain.md       — level-2 caller analysis
scripts/extract_call_graph.ps1
scripts/find_callers.ps1
scripts/find_caller_funcs.ps1
scripts/analyze_dispatch_funcs.ps1
scripts/trace_disp01_chain.ps1
scripts/trace_level2_chain.ps1
scripts/decode_helpers.ps1
