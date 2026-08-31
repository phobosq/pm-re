# Helper 1 Parser Entry

status: static handoff only
confidence: strongly_inferred

primary function:
- PM62C_PR_01 -> 0x003E16B0..0x003E16D5

anchor callsites:
- 0x003E16B4 -> GetCommandLineA
- 0x003E16C1 -> GetCommandLineW

nearby block:
- B027 -> 0x003E16B4..0x003E16C1 score=14 role=cli_entry_candidate

working interpretation:
- this is a compact CLI entry/dispatch point rather than a transport routine
- dual ANSI/Unicode command-line fetch suggests early normalization or argv selection
- no compare or transport APIs appear in the same function, so follow-on control flow must leave this range quickly
- the function stores the raw command-line pointers into globals:
  - 0x003E16BA -> [0x1407EDB50] = GetCommandLineA()
  - 0x003E16C7 -> [0x1407EDB58] = GetCommandLineW()
- a downstream ANSI-side consumer at 0x003F37E4..0x003F3947 reads [0x1407EDB50], falls back to a local buffer when empty, tokenizes the string, and materializes argv-like globals at:
  - 0x1407EDB3C (count-like)
  - 0x1407EDB40 (pointer-table-like)
  - 0x1407EDB60 (fallback/source buffer pointer)

next debugger actions:
1. break on 0x003E16B4 and 0x003E16C1 in paired control/active vmr runs
2. break on 0x003F3835 and confirm whether [0x1407EDB50] or the fallback buffer is used
3. record the tokenized argv-like outputs written at 0x1407EDB3C/0x1407EDB40 before the first vmr-dependent compare/store divergence

guardrail:
- do not mark vmr parser confirmed from this range alone; it is only the entry anchor into later tokenization/compare/store logic
