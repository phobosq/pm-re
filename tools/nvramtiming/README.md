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
- probes availability of private `NvAPI_GPU_RegisterOp` (`0x2EB3C140`)

Intentionally **not implemented yet**:
- active register reads/writes through the private interface
- `-vmr`/`-vmt*` transformations
- strap application

Those remain disabled until the exact PhoenixMiner request ABI and the high-level timing-value -> register-field mapping are fully verified statically.

## Build

```powershell
cmake -S tools/nvramtiming -B build/nvramtiming -A x64
cmake --build build/nvramtiming --config Release
```

Run:

```powershell
build\nvramtiming\Release\nvramtiming.exe --list
```

The current executable is read-only.

## Confirmed RE anchors

- private NVAPI ID `0x2EB3C140` resolves to the RegisterOp interface used by PhoenixMiner's NVIDIA strap path
- downstream strap application performs masked operations against registers including `0x9A0290`, `0x9A0298`, `0x9A029C`, and `0x9A02A0`
- active writes remain out of this tool until their request structure and timing-value mapping are completely reproduced

See `notes/` for the evidence trail.
