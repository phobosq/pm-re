# vmr Callers (Who Calls Our Target Functions)
confidence: strongly_inferred (static CALL rel32 scan of .text)

## TR01 transport_wrapper_A -> 0x001C4010 (1 callers)
  <- 0x001C3C79 in unknown_func

## TR04 transport_wrapper_B -> 0x0028CA90 (2 callers)
  <- 0x0028CFFB in unknown_func
  <- 0x0028D493 in 0x0028D350..0x0028D530 role=unknown

## TR02 ioctl_cluster_A1 -> 0x001C1BB0 (1 callers)
  <- 0x001C3CCE in unknown_func

## TR03 ioctl_cluster_B -> 0x001C6BB0 (1 callers)
  <- 0x001C44B5 in 0x001C4010..0x001C44E3 role=transport_wrapper_candidate

## PR01 parser_cmdline -> 0x003E16B0 (0 callers)
  (no CALL rel32 callers found ??? function may be called only indirectly)

## PR02 parser_compare_A -> 0x003B160C (2 callers)
  <- 0x00395FB0 in unknown_func
  <- 0x003B1C94 in unknown_func

## PR03 parser_compare_B -> 0x003F9610 (2 callers)
  <- 0x00405290 in unknown_func
  <- 0x00405604 in unknown_func

