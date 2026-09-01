# Hypothesis register

Confidence key: confirmed / strongly_inferred / hypothesis / unknown

## H01 — vmr_parser_path_exists
status: closed / confirmed
evidence:
- recovered literal `-vmr` at RVA `0x000E8F6E`
- descriptor ctor `0x000DD570`, vtable `0x0043F0E8`
- setter slot `+0x10 -> 0x000E10C0`
- `0x000E10D8` stores VMR to per-GPU record `+0xB0`
- per-GPU stride `0xD8`
confidence: confirmed

## H02 — vmr_uses_nvidia_registerop_transport
status: closed / confirmed
evidence:
- NVIDIA child `+0x25C` is the VMR scalar
- strap apply reaches `0x001ECB90`
- PhoenixMiner resolves private `NvAPI_GPU_RegisterOp` with QueryInterface ID `0x2EB3C140`
- confirmed timing RegisterOp writes include `0x9A0290`, `0x9A0298`, `0x9A029C`, `0x9A02A0`
confidence: confirmed

## H03 — timing options share one per-GPU config record
status: closed / confirmed
evidence:
- `-mt -> +0x98`
- `-straps -> +0xAC`
- `-vmr/-rxboost -> +0xB0`
- `-vmt2 -> +0xB8`
- `-vmt3 -> +0xBC`
confidence: confirmed

## H04 — vmr_and_rxboost_share_storage
status: closed / confirmed
evidence:
- both descriptor setters write per-GPU `+0xB0`
- Type2 runtime is NVIDIA, where `+0xB0` is interpreted as VMR
confidence: confirmed

## H05 — five-field consumer_0x3053C0_is_backend
status: falsified
conclusion: arithmetic transform/fingerprint, not timing application
confidence: confirmed falsification

## H06 — multifield_0x3C397C_is_backend
status: falsified
conclusion: unrelated mutable object / offset collision
confidence: strongly_inferred falsification

## H07 — generic_transport_candidates_are_vmr_backend
status: falsified for NVIDIA VMR
conclusion: NVIDIA VMR reaches private NVAPI RegisterOp instead
confidence: confirmed falsification

## H08 — derived_slot50_is_vmr_apply
status: falsified
conclusion: Type2 slot `+0x50` consumes non-VMR config; earlier snapshot hits were stack displacement collisions
confidence: confirmed falsification

## H09 — derived_type2_is_nvidia
status: closed / confirmed
evidence:
- Type2 ctor `0x001CDCC0` creates NVIDIA child `0x001D4A80`
- child stored at Type2 `+0x840`
- Type2 vtable slot `+0x90 -> 0x001CF880` returns `[this+0x840]`
- NVML names independently identify NVIDIA runtime
confidence: confirmed

## H10 — child_25c_is_vmr
status: closed / confirmed
evidence:
- `0x001D8B1F` reads `[child+0x25C]`
- same branch reconstructs `unable to set VRAM refresh rate -vmr {}`
- child vtable slot `+0x68 -> 0x001DBA30` writes R8D to `[child+0x25C]`
confidence: confirmed

## H11 — child_258_is_straps_preset
status: closed / confirmed
evidence:
- `0x001D7B43` reads `[child+0x258]` as preset ID
- `0x001D78B0` selects predefined 0x5C strap profile
- upper bridge forwards persistent `-straps +0xAC` as EDX to child setter
confidence: confirmed

## H12 — persistent_vmr_to_child_vmr_bridge
status: closed / confirmed
evidence:
- `0x00130628` Type2 slot `+0x90` obtains NVIDIA child into RDI
- `0x06A320` fills local snapshot rooted at `RBP+0x20`
- `0x00130687: mov edx,[rbp+0xCC]` = snapshot `+0xAC` (`-straps`)
- `0x0013068D: mov r8d,[rbp+0xD0]` = snapshot `+0xB0` (`-vmr`)
- `0x001306F9 -> 0x0014BA60 -> [child_vtable+0x68]`
- setter stores R8D to child `+0x25C`
confidence: confirmed

## H13 — vmr_maps_to_register_9a0290_field
status: closed / confirmed
evidence:
- VMR interpolation writes local profile `+0x08`
- `0x001D8F6E..0x001D8FAA` copies full profile to output
- RegisterOp maps profile `+0x08` to register `0x9A0290`, mask `0x1FF00`, shift 8
conclusion: VMR hardware field is `0x9A0290[16:8]`
confidence: confirmed

## H14 — registerop_handle_is_physical_gpu_handle
status: closed / confirmed
evidence:
- NVIDIA child handle is stored at `+0xD0`
- same handle is passed to `NvAPI_GPU_GetRamType` (`0x57F7CAAC`), `NvAPI_GPU_GetRamMaker` (`0x42AEA16A`), `NvAPI_GPU_GetPCIIdentifiers` (`0x2DDFB66E`), and RegisterOp
confidence: confirmed

## H15 — exact_vmr_numeric_transform
status: closed / confirmed
evidence:
- interpolation block `0x001D8B2D..0x001D8B57`
- divisor loaded at `0x001D8500` from RVA `0x004386B8`; extracted double is exactly `100.0`
- exact equation is `trunc(base - (base - target) * vmr / 100.0)`
- current cached/hardware profile `+0x08` replaces type-8 base when nonzero
- if no current value is available, type-8 table value is fallback base
- type-9 table value is target
confidence: confirmed

## H16 — vmr_family_table
status: closed / confirmed
evidence:
- family map RVA `0x004BD620..0x004BD6D0`
- keys are packed NVIDIA PCI IDs, e.g. `0x1B8010DE`
- profile table RVA `0x004BD6D0`, 16 records
- family 0 VMR endpoints: type8 `220`, type9 `130`
- family 1 VMR endpoints: type8 `152`, type9 `120`
- family 1 entries correspond to Pascal GDDR5X devices; family 0 entries correspond to Pascal GDDR5 devices
confidence: confirmed for table/dataflow; memory-type names strongly inferred from device IDs

## Milestones
M1 `-vmr -> persistent per-GPU config +0xB0`: CLOSED / CONFIRMED.
M2 `persistent VMR -> NVIDIA child +0x25C`: CLOSED / CONFIRMED.
M3 `child VMR -> profile+0x08 -> RegisterOp 0x9A0290[16:8]`: CLOSED / CONFIRMED.
M4 exact numeric transform and Pascal family endpoints: CLOSED / CONFIRMED.

Full static NVIDIA Pascal VMR path is CLOSED.

## MVP status
`tools/nvramtiming/` now implements:
- NVIDIA enumeration and PCI identification
- private RegisterOp read (`opcode 0x15`)
- `--read-reg`
- exact PhoenixMiner-compatible `--vmr-preview`
- transactional `--vmr-test <gpu> <0..100> --confirm-write`

`--vmr-test` uses masked RegisterOp write opcode `0x16` only on `0x9A0290 / mask 0x1FF00`, verifies the desired field, then always attempts to restore and verify the original field. No persistent VMR apply mode exists yet.

Next milestone M5: validate read/preview and then the transactional write/readback/restore path on a real supported Pascal GPU before exposing persistent apply or broadening to VMT/straps.
