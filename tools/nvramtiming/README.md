# nvramtiming

Standalone NVIDIA VRAM-timing research tool extracted from the PhoenixMiner 6.2c reverse-engineering work in this repository.

## Current MVP stage

Implemented:
- Windows x64 only
- dynamic `nvapi64.dll` loading
- `nvapi_QueryInterface`
- `NvAPI_Initialize`
- `NvAPI_EnumPhysicalGPUs`
- GPU-name enumeration
- private `NvAPI_GPU_RegisterOp` discovery (`0x2EB3C140`)
- read-only RegisterOp request ABI (`version 0x11808`, opcode `0x15`)
- arbitrary single-register read via `--read-reg`

Intentionally **not implemented yet**:
- RegisterOp write opcode / active register writes
- `set_vmr` / `set_vmt*`
- strap application

Writes remain disabled until the high-level timing controls are fully reproduced and a read/verify/restore transaction is in place.

## Build

```powershell
cmake -S tools/nvramtiming -B build/nvramtiming -A x64
cmake --build build/nvramtiming --config Release
```

The GitHub Actions build also publishes a `nvramtiming-win64` executable artifact.

## Usage

List NVIDIA GPUs and check private RegisterOp availability:

```powershell
build\nvramtiming\Release\nvramtiming.exe --list
```

Read one register (no write operation is issued):

```powershell
build\nvramtiming\Release\nvramtiming.exe --read-reg 0 0x9A0290
```

The current executable is strictly read-only.

## Confirmed RE anchors

- private NVAPI ID `0x2EB3C140` resolves to the RegisterOp interface used by PhoenixMiner's NVIDIA timing path
- RegisterOp receives a normal `NvPhysicalGpuHandle`; PhoenixMiner uses the same handle with `NvAPI_GPU_GetRamType`, `NvAPI_GPU_GetRamMaker`, and `NvAPI_GPU_GetPCIIdentifiers`
- request header is `version=0x11808`, followed by count and 0x18-byte entries
- entry opcode `0x15` performs a register read; result is returned in the entry value field
- entry opcode `0x16` is the masked-write form observed in PhoenixMiner, but it is intentionally not exposed by this tool
- NVIDIA VMR is stored in child field `+0x25C`
- VMR changes profile field `+0x08`, which maps to register `0x9A0290` with mask `0x1FF00` / shift 8
- the remaining static RE edge is the upper bridge from persistent per-GPU config `+0xB0` to the NVIDIA child VMR setter

See `notes/` for the evidence trail.
