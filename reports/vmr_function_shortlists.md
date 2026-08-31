# vmr Function Candidate Shortlists

## Transport Candidates
- 0x001C4010..0x001C44E3 score=19 calls=3 role=transport_wrapper_candidate apis=CreateFileA:2; DeviceIoControl:1
- 0x001C1BB0..0x001C1CE0 score=18 calls=2 role=ioctl_path_candidate apis=DeviceIoControl:2
- 0x001C6BB0..0x001C6C93 score=18 calls=2 role=ioctl_path_candidate apis=DeviceIoControl:2
- 0x0028CA90..0x0028CB6B score=14 calls=2 role=transport_wrapper_candidate apis=DeviceIoControl:1; CreateFileW:1
- 0x001C1CE0..0x001C1D98 score=9 calls=1 role=ioctl_path_candidate apis=DeviceIoControl:1
- 0x001C1DA0..0x001C1E31 score=9 calls=1 role=ioctl_path_candidate apis=DeviceIoControl:1
- 0x001C1ED0..0x001C1F62 score=9 calls=1 role=ioctl_path_candidate apis=DeviceIoControl:1
- 0x001C1E40..0x001C1ECE score=9 calls=1 role=ioctl_path_candidate apis=DeviceIoControl:1

## Parser Candidates
- 0x003E16B0..0x003E16D5 score=14 calls=2 role=unknown apis=GetCommandLineW:1; GetCommandLineA:1
- 0x003B160C..0x003B16C8 score=6 calls=1 role=unknown apis=CompareStringW:1
- 0x003F9610..0x003F96FF score=6 calls=1 role=unknown apis=CompareStringW:1

## Interpretation
- Transport-first: inspect top transport candidates to establish vmr write path wrappers.
- Parser-second: bridge cmdline and compare anchors into config-store path.
- Keep evidence at strongly_inferred until direct code-flow confirmation.
