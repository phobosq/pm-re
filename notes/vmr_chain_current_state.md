# vmr Chain Current State

status: static-progressed, runtime-blocked-on-host

confirmed links:
1. CLI option presence in docs for -vmr and grouped timing options.
2. Phoenix binary imports parsing/comparison and transport-adjacent APIs.
3. EIO layer includes SCM and DeviceIoControl surface.
4. Helper-driver payload in ZIP includes kernel MMIO mapping primitives.

missing link to reach confirmed full chain:
- runtime correlation from vmr argument value to concrete write path invocation sequence

minimal runtime proof requirements:
1. Controlled run without vmr and with vmr using identical build and environment.
2. Capture call sequence around GetCommandLine/CompareStringW and config store divergence.
3. Capture CreateFile/DeviceIoControl calls, device path, control code, and buffer deltas.
4. Tie resulting transport operation to EIO/helper-driver call path.

wave2 gate:
- Do not start straps/vmt semantic mapping until vmr transport is confirmed or falsified.

