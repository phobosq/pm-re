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
- VMR value is tied to persistent per-GPU config field `+0xB0`
- runtime config lifecycle is type-safe through getter `0x084A60` / setter `0x1362D0`
- derived Type2 runtime is confirmed NVIDIA via dynamically resolved NVML functions
- generic EIO/DeviceIoControl candidates remain unlinked
falsification_test: confirmed NVIDIA `+0xB0` consumer terminates in a non-hardware path and no timing apply path exists
next_experiment: restrict M2 to NVIDIA Type2 and identify its non-NVML hardware-facing dynamic/virtual API layer
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
evidence:
- both descriptor setters write per-GPU field `+0xB0`
- Type2 runtime is confirmed NVIDIA, so Type2 interpretation of `+0xB0` is `-vmr`
interpretation: storage is shared across vendor semantics; NVIDIA VMR and the other vendor's rxboost must diverge below the common config layer
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
falsification_test: confirmed NVIDIA timing-field consumer reaches a different vendor/MMIO path
next_experiment: do not search upward from generic transport candidates; follow NVIDIA Type2 virtual/dynamic API path downward
confidence: unknown

## H08 — derived_slot50_is_vmr_apply
status: falsified
evidence:
- Type1 slot `+0x50` (`0x1688D0`) uses type-safe snapshot getter but does not consume snapshot `+0xB0`
- Type2 slot `+0x50` (`0x1CF8B0`) likewise uses type-safe snapshot getter but consumes only non-VMR fields
- apparent `+0x368/+0x440` hits inside derived methods were stack-frame displacement collisions, not `this+snapshot` materialization
conclusion: derived slot `+0x50` is runtime/config work, not the VMR timing apply edge
confidence: confirmed falsification

## H09 — derived_type2_is_nvidia
status: closed / confirmed
evidence:
- Type2 ctor `0x001CDCC0` creates helper object `0x001D4A80`
- Type2 dynamic loader writes GetProcAddress results to slots `0x007E7840`, `0x007E7848`, `0x007E7858`
- statically decoded names are:
  - `nvmlDeviceGetHandleByIndex_v2`
  - `nvmlDeviceGetHandleByPciBusId_v2`
  - `nvmlErrorString`
conclusion: derived Type2 runtime is NVIDIA; this NVML layer appears to be enumeration/monitoring, not yet the timing backend
confidence: confirmed

## Active milestone
M1 `-vmr -> persistent per-GPU config`: CLOSED / CONFIRMED.
M2 `NVIDIA Type2 +0xB0 (VMR) -> first hardware-facing consumer`: ACTIVE.
