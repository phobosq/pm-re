# vmr Static Call Graph (Selected Ranges)

## TR01 transport_wrapper_A 0x001C4010..0x001C44E3 (18 edges)
  direct CALL: 14  direct JMP: 0  indirect: 4
  CALL 0x001C40BC -> 0x00178BB0
  CALL 0x001C411C -> 0x003DB020
  CALL 0x001C412B -> 0x003DB020
  CALL 0x001C413A -> 0x003DB020
  CALL 0x001C4146 -> 0x003DB020
  CALL 0x001C414F -> 0x003B20D4
  CALL 0x001C4174 -> 0x001C0670
  CALL 0x001C425E -> 0x00178720
  CALL 0x001C42A1 -> 0x00032EF0
  CALL 0x001C4434 -> 0x001A5430
  CALL 0x001C444C -> 0x001C01D0
  CALL 0x001C4456 -> 0x00032EF0
  CALL 0x001C44B5 -> 0x001C6BB0 -> func 0x001C6BB0..0x001C6C93 role=ioctl_path_candidate
  CALL 0x001C44C9 -> 0x003B24C0
  CALL_IND: 4 indirect dispatch(es)

## TR04 transport_wrapper_B 0x0028CA90..0x0028CB6B (5 edges)
  direct CALL: 2  direct JMP: 0  indirect: 3
  CALL 0x0028CAE5 -> 0x003B2624
  CALL 0x0028CB49 -> 0x003B20DC
  CALL_IND: 3 indirect dispatch(es)

## TR02 ioctl_cluster_A1 0x001C1BB0..0x001C1CE0 (6 edges)
  direct CALL: 3  direct JMP: 0  indirect: 2
  CALL 0x001C1C42 -> 0x001C1DA0 -> func 0x001C1DA0..0x001C1E31 role=ioctl_path_candidate
  CALL 0x001C1CAA -> 0x001C1DA0 -> func 0x001C1DA0..0x001C1E31 role=ioctl_path_candidate
  CALL 0x001C1CC6 -> 0x003B24C0
  CALL_IND: 2 indirect dispatch(es)

## TR03 ioctl_cluster_B 0x001C6BB0..0x001C6C93 (3 edges)
  direct CALL: 1  direct JMP: 0  indirect: 2
  CALL 0x001C6C85 -> 0x003B24C0
  CALL_IND: 2 indirect dispatch(es)

## PR01 parser_cmdline 0x003E16B0..0x003E16D5 (2 edges)
  direct CALL: 0  direct JMP: 0  indirect: 2
  CALL_IND: 2 indirect dispatch(es)

## PR02 parser_compare_A 0x003B160C..0x003B16C8 (4 edges)
  direct CALL: 2  direct JMP: 0  indirect: 2
  CALL 0x003B1643 -> 0x003B2E14
  CALL 0x003B1680 -> 0x003B16C8
  CALL_IND: 2 indirect dispatch(es)

## PR03 parser_compare_B 0x003F9610..0x003F96FF (5 edges)
  direct CALL: 2  direct JMP: 0  indirect: 3
  CALL 0x003F964E -> 0x003F9424 -> func 0x003F9424..0x003F95C4 role=unknown
  CALL 0x003F96B7 -> 0x003F9EEC
  CALL_IND: 3 indirect dispatch(es)

Interpretation:
- Direct CALL edges within this set indicate callee relationships.
- Calls INTO known transport/ioctl functions from parser or compare ranges would link parser -> transport.
- confidence: strongly_inferred (static only; no runtime confirmation)
