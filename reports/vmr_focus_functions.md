# vmr Focus Functions (.pdata mapped)

input_callsites_focus: 494
mapped_rows: 494
function_groups: 60

Top function candidates:
- 0x00002750..0x0000535A size=11274 score=500 role=unknown apis=GetProcAddress:250
- 0x00186B8A..0x0019038B size=38913 score=112 role=unknown apis=GetProcAddress:56
- 0x00395004..0x003954D2 size=1230 score=80 role=unknown apis=GetProcAddress:40
- 0x003381A0..0x00338B05 size=2405 score=48 role=unknown apis=GetProcAddress:20; LoadLibraryW:4
- 0x001D123E..0x001D353C size=8958 score=40 role=unknown apis=GetProcAddress:18; LoadLibraryExA:2
- 0x003C50E8..0x003C5799 size=1713 score=34 role=unknown apis=GetProcAddress:17
- 0x001C4010..0x001C44E3 size=1235 score=19 role=transport_wrapper_candidate apis=CreateFileA:2; DeviceIoControl:1
- 0x001C6BB0..0x001C6C93 size=227 score=18 role=ioctl_path_candidate apis=DeviceIoControl:2
- 0x001C1BB0..0x001C1CE0 size=304 score=18 role=ioctl_path_candidate apis=DeviceIoControl:2
- 0x003C5FC8..0x003C60CF size=263 score=16 role=unknown apis=GetProcAddress:6; LoadLibraryExW:1; LoadLibraryW:1
- 0x00404DE8..0x004051D7 size=1007 score=15 role=unknown apis=CreateFileW:3
- 0x0028CA90..0x0028CB6B size=219 score=14 role=transport_wrapper_candidate apis=DeviceIoControl:1; CreateFileW:1
- 0x003E16B0..0x003E16D5 size=37 score=14 role=unknown apis=GetCommandLineW:1; GetCommandLineA:1
- 0x001C1ED0..0x001C1F62 size=146 score=9 role=ioctl_path_candidate apis=DeviceIoControl:1
- 0x001C1E40..0x001C1ECE size=142 score=9 role=ioctl_path_candidate apis=DeviceIoControl:1

Interpretation:
- Functions with CreateFile + DeviceIoControl are top transport wrapper candidates.
- Functions with GetCommandLine + CompareStringW are top parser candidates.
- Keep confidence at strongly_inferred until direct code-flow or runtime evidence.
