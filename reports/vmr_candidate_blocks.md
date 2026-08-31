# vmr Candidate Blocks (Static Heuristic)

window_bytes: 0x1000
input_rows: 1785
high_value_rows: 494
blocks: 32

Top blocks:
- B001 0x0000276D..0x00005332 score=750 role=unknown apis=GetProcAddress:250
- B007 0x00186AE8..0x00190316 score=170 role=unknown apis=GetProcAddress:56; LoadLibraryA:1
- B022 0x00395024..0x003954B6 score=120 role=unknown apis=GetProcAddress:40
- B025 0x003C5117..0x003C60AF score=81 role=unknown apis=GetProcAddress:25; LoadLibraryExW:2; LoadLibraryW:1
- B017 0x003381FB..0x00338653 score=68 role=unknown apis=GetProcAddress:20; LoadLibraryW:4
- B012 0x001D1279..0x001D34ED score=58 role=unknown apis=GetProcAddress:18; LoadLibraryExA:2
- B009 0x001C1C37..0x001C1F3E score=54 role=ioctl_path_candidate apis=DeviceIoControl:6
- B018 0x003483D9..0x00348F48 score=33 role=unknown apis=GetProcAddress:9; LoadLibraryW:2; LoadLibraryA:1
- B015 0x0028CACC..0x0028D43A score=24 role=transport_wrapper_candidate apis=CreateFileW:3; DeviceIoControl:1
- B032 0x00404EE9..0x00405C79 score=20 role=unknown apis=CreateFileW:4
- B010 0x001C40F0..0x001C44A1 score=19 role=transport_wrapper_candidate apis=CreateFileA:2; DeviceIoControl:1
- B011 0x001C6C1C..0x001C6C65 score=18 role=ioctl_path_candidate apis=DeviceIoControl:2

Interpretation:
- Prioritize blocks with DeviceIoControl + CreateFile for vmr transport path.
- Prioritize blocks with GetCommandLine + CompareStringW for vmr parser path.
- Treat this ranking as strongly_inferred until direct code-flow confirmation.
