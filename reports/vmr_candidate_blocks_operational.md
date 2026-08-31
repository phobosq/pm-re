# vmr Candidate Blocks (Operational Filter)

filter: has_deviceiocontrol OR has_createfile OR has_cmdline OR has_compare

Top operational blocks:
- B009 0x001C1C37..0x001C1F3E score=54 role=ioctl_path_candidate flags(cmd=False,cmp=False,cf=False,dio=True) apis=DeviceIoControl:6
- B015 0x0028CACC..0x0028D43A score=24 role=transport_wrapper_candidate flags(cmd=False,cmp=False,cf=True,dio=True) apis=CreateFileW:3; DeviceIoControl:1
- B032 0x00404EE9..0x00405C79 score=20 role=unknown flags(cmd=False,cmp=False,cf=True,dio=False) apis=CreateFileW:4
- B010 0x001C40F0..0x001C44A1 score=19 role=transport_wrapper_candidate flags(cmd=False,cmp=False,cf=True,dio=True) apis=CreateFileA:2; DeviceIoControl:1
- B011 0x001C6C1C..0x001C6C65 score=18 role=ioctl_path_candidate flags(cmd=False,cmp=False,cf=False,dio=True) apis=DeviceIoControl:2
- B023 0x003B16A7..0x003B1DA4 score=15 role=unknown flags(cmd=False,cmp=True,cf=False,dio=False) apis=GetProcAddress:3; CompareStringW:1
- B027 0x003E16B4..0x003E16C1 score=14 role=cli_entry_candidate flags(cmd=True,cmp=False,cf=False,dio=False) apis=GetCommandLineW:1; GetCommandLineA:1
- B030 0x003F94C0..0x003F96DE score=13 role=unknown flags(cmd=False,cmp=True,cf=False,dio=False) apis=LoadLibraryExW:2; CompareStringW:1; GetProcAddress:1
- B031 0x003FF82D..0x003FF82D score=5 role=unknown flags(cmd=False,cmp=False,cf=True,dio=False) apis=CreateFileW:1
- B006 0x0006F818..0x0006F818 score=5 role=unknown flags(cmd=False,cmp=False,cf=True,dio=False) apis=CreateFileA:1
- B014 0x0022487C..0x0022487C score=5 role=unknown flags(cmd=False,cmp=False,cf=True,dio=False) apis=CreateFileW:1
- B029 0x003EEE65..0x003EEE65 score=5 role=unknown flags(cmd=False,cmp=False,cf=True,dio=False) apis=CreateFileW:1

priority:
1. transport wrappers with CreateFile+DeviceIoControl
2. pure DeviceIoControl clusters
3. parser entry and compare anchors
