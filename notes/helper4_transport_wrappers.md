# Helper 4 Transport Wrappers

status: static handoff only
confidence: strongly_inferred

wrapper candidate A:
- PM62C_TR_01 -> 0x001C4010..0x001C44E3
- block B010 -> 0x001C40F0..0x001C44A1 score=19 role=transport_wrapper_candidate
- callsites: 0x001C40F0 CreateFileA; 0x001C4290 CreateFileA; 0x001C44A1 DeviceIoControl

wrapper candidate B:
- PM62C_TR_04 -> 0x0028CA90..0x0028CB6B
- block B015 -> 0x0028CACC..0x0028D43A score=24 role=transport_wrapper_candidate
- block-local callsites: 0x0028CACC CreateFileW; 0x0028CB1F DeviceIoControl; 0x0028CC24 CreateFileW; 0x0028D43A CreateFileW

working interpretation:
- wrapper A is the cleanest ANSI open/open/ioctl shape and is the best first target for handle-flow tracing
- wrapper B looks like a Unicode open + ioctl path with nearby reopen/fallback behavior in the wider block
- both wrappers are static transport candidates only; neither is vmr-linked until a parser/config path reaches them

next debugger actions:
1. record device path strings, desired access flags, and returned handles at each CreateFile* callsite
2. test whether the same handle reaches the paired DeviceIoControl call
3. diff control code and input/output buffer pointers between control and active vmr runs

guardrail:
- keep claims at strongly_inferred unless the wrapper is observed on a vmr-dependent execution path
