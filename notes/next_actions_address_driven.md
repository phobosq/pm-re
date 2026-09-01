# Next Actions (Address-Driven)

## Scope lock — NVIDIA only
This project phase is **NVIDIA-only**.

Do not spend analysis time on AMD/ADL/IOMap/rxboost paths. AMD timing control already has satisfactory external tooling and is out of scope for this reverse-engineering effort.

Treat the following as negative landmarks for the current mission:
- ADL-owned runtime branches
- AMD `\\.\IOMap` transport
- AMD `set straps` path around `0x001C44F0`
- AMD IOMap primitives around `0x001C1E40` / `0x001C1ED0`
- AMD register maps recovered from those helpers

These findings may remain documented as classification evidence, but they must not drive further experiments unless the user explicitly reopens AMD scope.

## Active milestone
M1 `-vmr -> persistent per-GPU config +0xB0`: CLOSED / CONFIRMED.

M2 `NVIDIA Type2 +0xB0 (VMR) -> first NVIDIA hardware-facing consumer`: ACTIVE.

## NVIDIA priorities
1. Stay on confirmed NVIDIA Type2 runtime (`0x001CDCC0` lineage; NVML-loaded class).
2. Classify all Type2 child-object virtual methods from vtable `0x004BDE70` and all wrappers that call them.
3. Search for Type2/child methods that consume either:
   - the original `0xD8` config record,
   - a copied/aliased snapshot containing `+0xB0`, or
   - a derived scalar that can be proven to originate from `+0xB0`.
4. For any confirmed `+0xB0` consumer, follow only its NVIDIA-facing callees downward:
   - dynamically resolved NVIDIA APIs other than monitoring-only NVML,
   - NVIDIA driver/device handles,
   - DeviceIoControl paths linked by data flow from the Type2 consumer,
   - direct register/MMIO helpers if present.
5. Do not promote generic transport candidates without a Type2/config data-flow edge.

## Immediate experiment
Re-run/extend NVIDIA child and Type2 provenance analysis, starting from:
- Type2 ctor `0x001CDCC0`
- child ctor `0x001D4A80`
- child vtable `0x004BDE70`
- known Type2 wrappers around `0x001EED90`, `0x001F0120`, `0x001F0960`

The next useful artifact should rank child-vtable methods by evidence of receiving config/snapshot-derived values and show their direct/indirect callees.

## Evidence policy
- no confirmed label without direct code path evidence or runtime trace
- static-only claims stay at strongly_inferred/hypothesis
- AMD evidence cannot be used to infer NVIDIA transport semantics
