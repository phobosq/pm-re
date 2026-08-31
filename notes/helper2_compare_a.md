# Helper 2 Compare Path A

status: static handoff only
confidence: strongly_inferred

primary function:
- PM62C_PR_02 -> 0x003B160C..0x003B16C8

anchor callsite:
- 0x003B16A7 -> CompareStringW

nearby block:
- B023 -> 0x003B16A7..0x003B1DA4 score=15 role=unknown
- additional block-local imports after the compare: 0x003B1D7E/0x003B1D91/0x003B1DA4 -> GetProcAddress

working interpretation:
- compare path A looks parser-adjacent because it carries the earliest CompareStringW anchor
- the trailing GetProcAddress activity means this block may sit in a wider initialization/dispatch routine rather than a pure token comparator
- treat it as the first compare target to classify after the cmdline entry anchor

next debugger actions:
1. if execution reaches 0x003B16A7 after 0x003E16B4/0x003E16C1, dump the compared wide strings
2. capture the destination basic block taken on equal vs non-equal results
3. note whether the later GetProcAddress calls are unconditional init noise or vmr-dependent follow-on behavior

guardrail:
- if the compared strings are locale/UI text instead of option tokens, demote this path and move focus to compare path B
