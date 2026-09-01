# vmr Static Analysis — Session 4 Findings
# Confidence key: confirmed / strongly_inferred / hypothesis / unknown

## Executive Summary

Session 4 completed the static parser-chain analysis, discovering the option dispatcher
and confirming that all call-chain roots rely on C++ virtual dispatch (function pointers/vtable),
not direct CALL rel32. This explains why prior BFS could not close the parser→transport gap.

## New Confirmed / Strongly Inferred Facts

C16: OPT_DISP (0x003B2714..0x003B288B, 375B) is the argv consumer.
     Calls get_argv_ptr_table (0x003E16E0) and get_argv_count (0x003E16D8) at consecutive
     instruction addresses 0x003B280F and 0x003B2817.
     confidence: confirmed

C17: get_argv_count (0x003E16D8..0x003E16DF) and get_argv_ptr_table (0x003E16E0..0x003E16E7)
     are 2-instruction LEA RAX,[global]; RET accessors immediately after PR01 in the binary.
     get_fallback_buf (0x003E16E8..0x003E16EF) is a third adjacent accessor.
     These are the only ways to read argv_count (0x007EDB3C) and argv_ptr_table (0x007EDB40).
     confidence: confirmed (byte-level decode verified)

C18: All roots of the compare chains have 0 CALL rel32 callers:
     - PR02 root path: 0x000CA0E0 (71B) and 0x003A4D54 (66B) — no callers
     - PR03 root path: 0x003FE2BC (305B) and 0x003FE408 (256B) — no callers
     - OPT_DISP (0x003B2714, 375B) — no callers
     All are called via function pointer / C++ vtable dispatch.
     confidence: confirmed (exhaustive CALL rel32 scan of .text)

C19: 0x003B2E24 (called 2x from OPT_DISP) is a C++ SEH helper.
     Uses: RtlCaptureContext, RtlLookupFunctionEntry, RtlVirtualUnwind, IsDebuggerPresent,
     SetUnhandledExceptionFilter, UnhandledExceptionFilter.
     OPT_DISP has 2 try-catch blocks around option-processing logic.
     confidence: confirmed

C20: CompareStringW appears at exactly 2 callsites:
     - 0x003B16A7 in PR02 (0x003B160C..0x003B16C8)
     - 0x003F96DE in PR03 (0x003F9610..0x003F96FF)
     No other CompareStringW callsites exist in PhoenixMiner.exe.
     confidence: confirmed

## Full Parser Chain (Static, Confirmed)

```
GetCommandLineA (IAT)
  -> PR01 (0x003E16B0): stores to argv_cmdlineA_ptr (0x1407EDB50)
       |
ARGT01 (0x003F37E4): reads 0x1407EDB50, tokenizes command line, writes:
   - 0x1407EDB3C (argv_count)
   - 0x1407EDB40 (argv_ptr_table)
   - 0x1407EDB60 (fallback_buf)
       |
get_argv_count (0x003E16D8): LEA RAX, [argv_count]; RET
get_argv_ptr_table (0x003E16E0): LEA RAX, [argv_ptr_table]; RET
       |
OPT_DISP (0x003B2714): calls both getters, then calls 0x00129A50 (huge, 16kB) with argv
       |
  [VTABLE DISPATCH — not traceable via CALL rel32]
       |
DPRB01/02 (0x00395CA8, 0x003B1C28): callers of PR02
DPRB03/04 (0x0040520C, 0x004052CC): callers of PR03
       |
PR02 (0x003B160C): CompareStringW @ 0x003B16A7
PR03 (0x003F9610): CompareStringW @ 0x003F96DE
       |
  [store parsed vmr value to global — NOT YET LOCATED]
       |
OPT_DISP terminal calls: 0x003EA2F0, 0x003EA300, 0x003EA310, 0x003EA360
  (4 setter-like functions with no import callsites — strong setter candidates)
       |
  [shared global data — hypothesis H08 still active]
       |
DISP01 (0x001C3A30) -> TR01 -> TR03 (IOCTL chain)
```

## Key Missing Links

1. vtable address containing 0x003B2714 — find which C++ object's vtable points here
2. Where PR02/PR03 store the parsed value after CompareStringW confirms the match
3. Whether 0x003EA2F0-0x003EA360 are the setters for vmr-related config globals

## Hypotheses Updated

H09: OPT_DISP and the DPRB01/DPRB02 callers are methods of the same C++ class.
     Evidence: both are in 0x003B area, both have 0 CALL rel32 callers.
     confidence: hypothesis

H10: The 4 terminal calls in OPT_DISP (0x003EA2F0-0x003EA360) write parsed option
     values to config globals that DISP01/TR01 later read before IOCTL dispatch.
     confidence: hypothesis

## Recommended Next Steps

Static:
1. Scan .rdata/.data for 8-byte VA values (0x14003B2714) pointing to OPT_DISP — find the vtable
2. Dump bytes of PR02 (0x003B160C..0x003B16C8) to find MOV [global], reg after CompareStringW
3. Dump bytes of 0x003EA2F0-0x003EA360 to identify what global each small function writes

Runtime (if environment available):
1. Break at ARGT01 entry (0x003F37E4) — dump argv_count and argv_ptr_table after return
2. Break at OPT_DISP entry (0x003B2714) — log RCX/RDX (this pointer, first arg)
3. Break on CompareStringW (0x003B16A7) — log lpString1/lpString2 for vmr match
4. On vmr match: note next MOV [global], reg instruction for value store RVA

## Session 4 New Artifacts

notes/vmr_global_xrefs.csv/md  — RIP-relative access scan of 5 argv globals
notes/vmr_getter_callers.csv/md — callers of get_argv_* accessors
notes/vmr_opt_disp_analysis.md  — OPT_DISP outbound calls, imports, callers
notes/vmr_bfs_reachability.md   — BFS depth-4 from OPT_DISP (no targets reached)
scripts/find_global_xrefs_fast.ps1
scripts/find_getter_callers.ps1
scripts/analyze_opt_disp.ps1
scripts/bfs_reachability.ps1
scripts/trace_up_from_compare.ps1
scripts/dump_parser_context.ps1
scripts/check_opt_imports.ps1
