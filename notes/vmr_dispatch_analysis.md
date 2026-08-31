# Dispatch/Caller Function Analysis
confidence: strongly_inferred (static analysis)

## DISP01 transport_dispatcher_AB
   range: 0x001C3A30..0x001C400E size=0x5DE
   import callsites inside: 0
   (no import callsites from high-value list ??? relies on internal calls only)

## DISP04B transport_dispatcher_B
   range: 0x0028CF90..0x0028D054 size=0xC4
   import callsites inside: 0
   (no import callsites from high-value list ??? relies on internal calls only)

## DPRB01 compare_A_caller_L
   range: 0x00395CA8..0x00396008 size=0x360
   import callsites inside: 0
   (no import callsites from high-value list ??? relies on internal calls only)

## DPRB02 compare_A_caller_S
   range: 0x003B1C28..0x003B1CCD size=0xA5
   import callsites inside: 0
   (no import callsites from high-value list ??? relies on internal calls only)

## DPRB03 compare_B_caller_S
   range: 0x0040520C..0x004052C9 size=0xBD
   import callsites inside: 0
   (no import callsites from high-value list ??? relies on internal calls only)

## DPRB04 compare_B_caller_L
   range: 0x004052CC..0x0040565E size=0x392
   import callsites inside: 0
   (no import callsites from high-value list ??? relies on internal calls only)

## DISP01 Full Import Callsites (all imports, not just high-value)
   count: 0

Evidence classification:
  - If DISP01 contains CompareString*/GetCommandLine: parser+transport in one function -> confirmed_bridge
  - If DISP01 has only transport APIs: dispatcher is below parser -> need higher caller
  - If compare_B_callers share any RVA ranges with transport callers: cross-link found
