# argv Getter Function Callers
# Getters: 0x003E16D8=get_argv_count  0x003E16E0=get_argv_ptr_table  0x003E16E8=get_fallback_buf
# These tiny LEA+RET accessors are called instead of RIP-relative direct access
# confidence: confirmed (CALL rel32 exhaustive scan of .text, getter byte patterns verified)

## get_argv_count (1 callers)
  <- 0x003B2817  in 0x003B2714..0x003B288B size=0x177

## get_argv_ptr_table (1 callers)
  <- 0x003B280F  in 0x003B2714..0x003B288B size=0x177

## get_fallback_buf (1 callers)
  <- 0x0006D29E  in 0x0006A930..0x0006E7E8 size=0x3EB8

## Multi-getter callers (option dispatch candidates)
  func 0x003B2714..0x003B288B size=0x177  calls: get_argv_count, get_argv_ptr_table (2x)
