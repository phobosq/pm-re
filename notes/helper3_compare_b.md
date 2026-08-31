# Helper 3 Compare Path B

status: static handoff only
confidence: strongly_inferred

primary function:
- PM62C_PR_03 -> 0x003F9610..0x003F96FF

anchor callsite:
- 0x003F96DE -> CompareStringW

nearby block:
- B030 -> 0x003F94C0..0x003F96DE score=13 role=unknown
- block-local imports before the compare: 0x003F94C0/0x003F94E1 -> LoadLibraryExW; 0x003F9546 -> GetProcAddress

working interpretation:
- compare path B is lower priority than compare path A because it is bundled with dynamic loader activity before the compare
- this may represent token normalization through a helper module, or it may be unrelated late-stage text handling
- only keep it on the vmr path if it is observed after parser entry or if the compared strings match CLI/config tokens

next debugger actions:
1. break on 0x003F96DE only after classifying whether path A is parser-relevant
2. capture module/function names resolved by the preceding loader calls
3. record the compared wide strings and whether the compare result feeds config mutation or transport selection

guardrail:
- do not assume parser relevance merely because CompareStringW is present; the loader-heavy block shape makes false positives plausible
