# vmr Parser Hunt Plan (NVIDIA wave1)

Static leads:
- GetCommandLineA/GetCommandLineW imports present (confirmed)
- CompareStringW import present (confirmed)
- DeviceIoControl and CreateFileA/W imports present (confirmed)
- GetProcAddress and LoadLibrary* imports present (confirmed)

Dynamic breakpoints priority:
1. kernel32!GetCommandLineW
2. kernel32!GetCommandLineA
3. kernel32!CompareStringW
4. kernel32!GetProcAddress
5. kernel32!LoadLibraryA/LoadLibraryW/LoadLibraryExA/LoadLibraryExW
6. kernel32!CreateFileW/CreateFileA
7. kernel32!DeviceIoControl
8. ntdll!NtDeviceIoControlFile

Procedure:
1. Run control args (without vmr) and collect call sequence digest.
2. Run active args (with vmr value) keeping all else identical.
3. Compare first divergence after command-line parsing.
4. Mark store-to-config site for vmr and propagate to first consumer.
5. Correlate consumer with CreateFile/DeviceIoControl or EIO exported calls.

Stop criteria:
- No parser divergence observed in both runs -> hypothesis stays open and move to deeper compare/token normalization tracing.
- Consumer found but no transport relation -> strongly_inferred only, not confirmed.

