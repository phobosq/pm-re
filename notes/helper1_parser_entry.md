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

next debugger actions:
1. break on 0x003E16B4 and 0x003E16C1 in paired control/active vmr runs
2. record the immediate branch/call targets reached after each cmdline fetch
3. stop at the first downstream compare or config-store divergence before promoting any parser claim

guardrail:
- do not mark vmr parser confirmed from this range alone; it is only the entry anchor into later compare/store logic
