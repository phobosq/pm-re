# Helper 5 IOCTL Clusters

status: static handoff only
confidence: strongly_inferred

cluster A:
- B009 -> 0x001C1C37..0x001C1F3E score=54 role=ioctl_path_candidate
- anchored functions in range: PM62C_TR_02 0x001C1BB0..0x001C1CE0; PM62C_TR_05 0x001C1CE0..0x001C1D98; PM62C_TR_06 0x001C1DA0..0x001C1E31; PM62C_TR_08 0x001C1E40..0x001C1ECE; PM62C_TR_07 0x001C1ED0..0x001C1F62
- callsites: 0x001C1C37; 0x001C1CA0; 0x001C1D58; 0x001C1E0E; 0x001C1EAC; 0x001C1F3E -> DeviceIoControl

cluster B:
- B011 -> 0x001C6C1C..0x001C6C65 score=18 role=ioctl_path_candidate
- anchored function: PM62C_TR_03 -> 0x001C6BB0..0x001C6C93
- callsites: 0x001C6C1C; 0x001C6C65 -> DeviceIoControl

working interpretation:
- cluster A looks like a family of adjacent DeviceIoControl leaf routines, possibly probe/read/write variants sharing one transport layer
- cluster B is compact enough to be a single specialized ioctl helper or retry branch
- these clusters are valuable even without visible CreateFile* calls because they may sit below the wrapper candidates

next debugger actions:
1. break on all B009 and B011 callsites after confirming which wrapper opened the device handle
2. log control codes, buffer sizes, and whether the input buffer mutates with vmr value changes
3. use repeated-hit patterns to separate setup/probe ioctls from value-carrying write ioctls

guardrail:
- repeated DeviceIoControl use alone does not prove vmr writes; require vmr-dependent payload or call-stack linkage first
