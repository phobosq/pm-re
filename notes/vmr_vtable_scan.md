# vtable / Function Pointer Scan ??? Session 5
# Scanning all non-code sections for 8-byte VAs pointing to key functions
# imageBase=0x140000000

## All pointer hits: 3
  [.rdata] @0x0043DC30 -> 0x000CA0E0  (PR02_root_A)
  [.rdata] @0x0070CD70 -> 0x003A4D54  (PR02_root_B)
  [.rdata] @0x00718DA0 -> 0x003E16B0  (PR01_parser_cmdline)

## vtable cluster analysis (entries within 32 bytes of each other):
  (no clusters found)
