# Triage Report (Updated)

timestamp_utc: 2026-08-31T22:56:47.8447919Z
scope: NVIDIA vmr wave1; straps/vmt wave2

confirmed:
- sample SHA-256 matches expected reference
- PhoenixMiner.exe and IOMap64.sys exist in ZIP entries
- PhoenixMiner.exe and IOMap64.sys are missing after unpack on this host (environment interference)
- PhoenixMiner imports CreateFileA/W, DeviceIoControl, GetProcAddress, LoadLibrary*
- IOMap64.sys in-memory strings include MmMapIoSpace/MmUnmapIoSpace and IoCreateDevice

strongly_inferred:
- vmr likely routes through helper-driver/MMIO-related path via EIO.dll + IOMap64.sys
- runtime import resolution behavior is likely relevant due GetProcAddress/LoadLibrary usage

hypothesis:
- vmr parser path requires dynamic compare tracing because direct option tokens are not plainly visible in binary strings

next_actions:
1. Resolve vmr parser comparator/store path in debugger/disassembler.
2. Correlate vmr consumer with CreateFile/DeviceIoControl transitions.
3. Capture A/B vmr traces and promote transport to confirmed.

