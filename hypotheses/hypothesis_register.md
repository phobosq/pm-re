# Hypothesis register

Confidence key: confirmed / strongly_inferred / hypothesis / unknown

## H01 — vmr_parser_path_exists
status: closed / confirmed
evidence:
- recovered literal `-vmr` at RVA `0x000E8F6E`
- descriptor ctor `0x000DD570`
- descriptor vtable `0x0043F0E8`
- setter slot `+0x10 -> 0x000E10C0`
- confirmed store `0x000E10D8: mov dword ptr [rdx + rcx + 0xB0], eax`
- per-GPU stride confirmed as `0xD8`; array base is reached through owner `+0x2C0`
conclusion: parser->persistent-config edge is closed statically
confidence: confirmed

## H02 — vmr_uses_low_level_transport
status: active
evidence:
- VMR value is now tied to persistent per-GPU config field `+0xB0`
- generic EIO/DeviceIoControl candidates exist but are not yet linked to this field
falsification_test: confirmed `+0xB0` consumer terminates in a non-hardware path and no timing apply path exists
next_experiment: enumerate genuine materializers/consumers of owner `+0x2C0` + stride `0xD8`, then follow the first downstream call boundary
confidence: hypothesis

## H03 — timing options share one per-GPU config record
status: closed / confirmed
evidence:
- record stride `0xD8`
- `-mt -> +0x98`
- `-straps -> +0xAC`
- `-vmr/-rxboost -> +0xB0`
- `-vmt2 -> +0xB8`
- `-vmt3 -> +0xBC`
confidence: confirmed

## H04 — vmr_and_rxboost_share_storage
status: closed / confirmed
evidence: both descriptor setters write per-GPU field `+0xB0`
interpretation: storage is shared; semantic/backend distinction remains unresolved
confidence: confirmed

## H05 — five-field consumer_0x3053C0_is_backend
status: falsified
evidence:
- function `0x003053C0..0x00305BB6` reads all five timing offsets but performs a self-contained arithmetic transform
- no calls in the timing-field tail
- final output is only two DWORD stores to `[r14]` and `[r14+4]`
conclusion: likely generic hash/fingerprint/transform over a record, not timing application
confidence: confirmed falsification

## H06 — multifield_0x3C397C_is_backend
status: falsified
evidence:
- function mutates offsets such as `+0xB0` and `+0xAC`
- performs normalization/division rather than consuming immutable PM timing config
conclusion: structurally similar unrelated object; offset collision
confidence: strongly_inferred falsification

## H07 — generic_transport_candidates_are_vmr_backend
status: blocked / unproven
evidence: DeviceIoControl/CreateFile clusters exist, but no parser/config data-flow edge reaches them yet
falsification_test: confirmed timing-field consumer reaches a different vendor/MMIO path
next_experiment: do not search upward from transport candidates; first close `per_gpu +0xB0 -> consumer`
confidence: unknown

## Active milestone
M1 `-vmr -> persistent per-GPU config`: CLOSED / CONFIRMED.
M2 `per-GPU +0xB0 -> first hardware-facing consumer`: ACTIVE.
