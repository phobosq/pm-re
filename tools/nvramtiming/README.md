# nvramtiming

Standalone NVIDIA Pascal VRAM-timing research tool extracted from the PhoenixMiner 6.2c reverse-engineering work in this repository.

## Current MVP

Implemented:
- Windows x64
- dynamic `nvapi64.dll` loading and `nvapi_QueryInterface`
- NVIDIA GPU enumeration / names / PCI identifiers
- private `NvAPI_GPU_RegisterOp` discovery (`0x2EB3C140`)
- RegisterOp read ABI: request `0x11808`, opcode `0x15`
- arbitrary register read via `--read-reg`
- exact PhoenixMiner-compatible VMR preview for supported Pascal PCI IDs
- transactional VMR write/readback/restore test using masked-write opcode `0x16`

Not implemented:
- persistent VMR apply mode
- VMT1/VMT2/VMT3
- complete strap application
- non-Pascal NVIDIA families

## Build

```powershell
cmake -S tools/nvramtiming -B build/nvramtiming -A x64
cmake --build build/nvramtiming --config Release
```

GitHub Actions publishes the executable as artifact `nvramtiming-win64`.

## Usage

### 1. Enumerate GPUs

```powershell
nvramtiming.exe --list
```

### 2. Read the confirmed VMR register

```powershell
nvramtiming.exe --read-reg 0 0x9A0290
```

This is read-only.

### 3. Preview a VMR value

```powershell
nvramtiming.exe --vmr-preview 0 1
```

Preview reads the current `0x9A0290` value, extracts bits `[16:8]`, identifies the PhoenixMiner Pascal family from the PCI ID, and computes the field that PhoenixMiner 6.2c would use. It performs no write.

The exact recovered equation is:

```text
desired = trunc(base - (base - target) * vmr / 100.0)
```

If the current hardware field is nonzero it is used as `base`; otherwise the family type-8 fallback is used.

Recovered endpoints:
- family 0 / Pascal GDDR5: fallback base `220`, target `130`
- family 1 / Pascal GDDR5X: fallback base `152`, target `120`

### 4. Transactional hardware test

Only after `--list`, `--read-reg`, and `--vmr-preview` all return sensible values:

```powershell
nvramtiming.exe --vmr-test 0 1 --confirm-write
```

This command performs a real register write. It is intentionally not a persistent apply command.

Transaction sequence:
1. read and save the original `0x9A0290` field
2. masked write only bits covered by `0x1FF00`
3. read back and verify the requested field
4. attempt to restore the original field regardless of apply/readback result
5. read back and verify restore

Exit code `3` means the original field was **not verified restored**. Stop further writes and reset the NVIDIA driver/GPU before doing anything else.

For the first real test use a small VMR value such as `1`; do not start with `100`.

There is deliberately no `--vmr-apply` yet. Persistent apply should only be added after the transactional path has been validated on real hardware.

## Confirmed RE anchors

- `-vmr` persistent per-GPU config: `+0xB0`
- Type2 runtime is NVIDIA
- Type2 `+0x840` holds the real NVIDIA child; vtable slot `+0x90` returns it
- child setter vtable slot `+0x68 -> 0x001DBA30`
- setter argument R8D is stored to `child+0x25C`, confirmed VMR
- upper bridge `0x001305F0` forwards snapshot `+0xB0` as R8D into that setter
- VMR interpolation: `0x001D8B2D..0x001D8B57`
- divisor is exactly `100.0` at RVA `0x004386B8`
- VMR output is profile `+0x08`
- hardware mapping is register `0x9A0290`, mask `0x1FF00`, shift `8`
- private RegisterOp read opcode `0x15`; masked-write opcode `0x16`
- RegisterOp takes a normal `NvPhysicalGpuHandle`
- family map: RVA `0x004BD620..0x004BD6D0`
- profile table: RVA `0x004BD6D0`, 16 records

See `notes/` and `hypotheses/hypothesis_register.md` for the complete evidence trail.
