# vmr Global Variable Cross-References (Session 4)
# Globals from ARGT01 (session3): argv table written by tokenizer, read by option dispatcher
# confidence: strongly_inferred (exhaustive RIP-relative .text scan)

## argv_count @ 0x007EDB3C  (3 total: 0 writes, 0 reads, 3 other)
  OTHER (call-indirect / unknown / LEA):
    ? 0x003E16D8  LEA  .. size=0x0
    ? 0x003F38D0  unknown  [ARGT01_tokenizer]  0x003F37E4..0x003F395A size=0x176
    ? 0x003F3922  unknown  [ARGT01_tokenizer]  0x003F37E4..0x003F395A size=0x176

## argv_ptr_table @ 0x007EDB40  (5 total: 3 writes, 1 reads, 1 other)
  WRITES:
    W 0x003F38CA  [ARGT01_tokenizer]  0x003F37E4..0x003F395A size=0x176
    W 0x003F392F  [ARGT01_tokenizer]  0x003F37E4..0x003F395A size=0x176
    W 0x003F44D7  0x003F4464..0x003F44F2 size=0x8E
  READS:
    R 0x003F44BD  READ_64  0x003F4464..0x003F44F2 size=0x8E
  OTHER (call-indirect / unknown / LEA):
    ? 0x003E16E0  LEA  .. size=0x0

## cmdlineA_ptr @ 0x007EDB50  (2 total: 1 writes, 1 reads, 0 other)
  WRITES:
    W 0x003E16BA  [PR01_parser_cmdline]  0x003E16B0..0x003E16D5 size=0x25
  READS:
    R 0x003F3835  READ_64  [ARGT01_tokenizer]  0x003F37E4..0x003F395A size=0x176

## cmdlineW_ptr @ 0x007EDB58  (1 total: 1 writes, 0 reads, 0 other)
  WRITES:
    W 0x003E16C7  [PR01_parser_cmdline]  0x003E16B0..0x003E16D5 size=0x25

## fallback_buf @ 0x007EDB60  (2 total: 1 writes, 0 reads, 1 other)
  WRITES:
    W 0x003F383E  [ARGT01_tokenizer]  0x003F37E4..0x003F395A size=0x176
  OTHER (call-indirect / unknown / LEA):
    ? 0x003E16E8  LEA  .. size=0x0

## Key: read-side consumers NOT already in known-function list
  UNKNOWN_READER 0x003F4464..0x003F44F2 size=0x8E
