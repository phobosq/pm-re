# IOCTL Map (Draft)

status: pre-runtime draft

observed_components:
- PhoenixMiner.exe (from ZIP, preserved as .bin for static analysis)
- EIO.dll (exports multiple MMIO read/write helpers)
- IOMap64.sys (present in ZIP; missing after unpack on host)

known_api_surface:
- user-mode: CreateFileA/W, DeviceIoControl
- helper driver indicators: IoCreateDevice, IoCreateSymbolicLink, MmMapIoSpace, MmUnmapIoSpace

unknowns:
- device path name used for CreateFile
- IOCTL control codes
- input/output buffer structures
- vmr-specific field mapping inside IOCTL payload

plan_to_resolve:
1. Dynamic breakpoint on CreateFile and DeviceIoControl.
2. Log handle->device path and control codes.
3. Diff buffer blobs between vmr control run and active run.
4. Infer candidate struct fields before any semantic claim.

