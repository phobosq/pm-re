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

## H02 — vmr_uses_nvidia_registerop_transport
status: closed / confirmed
evidence:
- NVIDIA child field `+0x25C` is consumed as a 0..100 interpolation scalar in the strap profile builder
- the same branch reconstructs the diagnostic text `unable to set VRAM refresh rate -vmr {}`
- NVIDIA child strap apply is vtable slot `+0x80 -> 0x001DE8B0`
- apply calls `0x001ECB90(current5C, desired5C, gpu_index)`
- PhoenixMiner resolves private `NvAPI_GPU_RegisterOp` with QueryInterface ID `0x2EB3C140`
- `0x001ECB90` actively calls RegisterOp for changed timing fields
- confirmed register operations include `0x9A0290`, `0x9A0298`, `0x9A029C`, `0x9A02A0`
conclusion: VMR is implemented through the NVIDIA strap-profile path and private NVAPI RegisterOp, not the generic DeviceIoControl candidates
confidence: confirmed

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
interpretation: storage is shared across vendor semantics; NVIDIA VMR and the other vendor's rxboost diverge below the common config layer
confidence: confirmed

## H05 — five-field consumer_0x3053C0_is_backend
status: falsified
evidence:
- function `0x003053C0..0x00305BB6` reads all five timing offsets but performs a self-contained arithmetic transform
- no calls in the timing-field tail
- final output is only two DWORD stores to `[r14]` and `[r14+4]`
conclusion: generic transform, not timing application
confidence: confirmed falsification

## H06 — multifield_0x3C397C_is_backend
status: falsified
evidence:
- function mutates offsets such as `+0xB0` and `+0xAC`
- performs normalization/division rather than consuming immutable PM timing config
conclusion: structurally similar unrelated object; offset collision
confidence: strongly_inferred falsification

## H07 — generic_transport_candidates_are_vmr_backend
status: falsified for NVIDIA VMR
evidence:
- the confirmed NVIDIA strap path reaches private `NvAPI_GPU_RegisterOp` instead
- no parser/config data-flow proof was ever established to the generic DeviceIoControl candidates
conclusion: generic transport candidates are not the current NVIDIA VMR backend
confidence: confirmed falsification for the NVIDIA scope

## H08 — derived_slot50_is_vmr_apply
status: falsified
evidence:
- Type2 slot `+0x50` (`0x1CF8B0`) consumes only non-VMR snapshot fields
- apparent `+0x368/+0x440` hits were stack-frame collisions
confidence: confirmed falsification

## H09 — derived_type2_is_nvidia
status: closed / confirmed
evidence:
- Type2 ctor `0x001CDCC0` creates helper object `0x001D4A80`
- statically decoded dynamic API names include `nvmlDeviceGetHandleByIndex_v2`, `nvmlDeviceGetHandleByPciBusId_v2`, and `nvmlErrorString`
- the real NVIDIA child returned by `0x001D4A80` is stored at Type2 `+0x840`
- Type2 vtable slot `+0x90 -> 0x001CF880` returns `[this+0x840]`
confidence: confirmed

## H10 — child_25c_is_vmr
status: closed / confirmed
evidence:
- `0x001D8B1F: mov edx,[child+0x25C]`
- value is normalized as a percentage and used in interpolation between current and target timing values
- diagnostic string in the same branch decodes to `unable to set VRAM refresh rate -vmr {}`
- child vtable slot `+0x68 -> 0x001DBA30` writes its R8D argument to `[child+0x25C]`
conclusion: child field `+0x25C` is the runtime VMR scalar and slot `+0x68` is its setter path
confidence: confirmed

## H11 — child_258_is_straps_preset
status: active / strongly_inferred
evidence:
- `0x001D7B43` reads `[child+0x258]` as profile/preset ID and passes it to `0x001D78B0`
- `0x001D78B0` chooses a predefined 0x5C strap profile
- slot `+0x68 -> 0x001DBA30` writes EDX to `[child+0x258]`
- values 8/9 are specially normalized back to zero in the setter, indicating internal sentinel/special modes
falsification_test: caller provenance shows EDX comes from another non-straps control
next_experiment: trace slot +0x68 caller ABI and map EDX to persistent config `+0xAC`
confidence: strongly_inferred

## H12 — persistent_vmr_to_child_vmr_bridge
status: active
known endpoints:
- source: persistent per-GPU `+0xB0` (`-vmr`)
- sink: NVIDIA child slot `+0x68 -> 0x001DBA30`, argument `R8D`, stored at child `+0x25C`
next_experiment:
- filter indirect `call [vptr+0x68]` callsites by the confirmed setter ABI `{EDX,R8D,R9}`
- prove R8D originates from runtime/persistent VMR
success_criterion: direct static dataflow `config +0xB0 -> R8D -> child+0x25C`
confidence: hypothesis

## Active milestone
M1 `-vmr -> persistent per-GPU config +0xB0`: CLOSED / CONFIRMED.
M2 lower half `child VMR -> NVIDIA hardware RegisterOp`: CLOSED / CONFIRMED.
Remaining RE edge for full VMR chain: `persistent +0xB0 -> child +0x25C`.
MVP scaffold under `tools/nvramtiming/`: active; read-only NVAPI enumeration build is passing on Windows CI.
