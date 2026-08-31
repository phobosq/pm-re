# Next Actions (Address-Driven)

## vmr wave1 priorities
1. Inspect parser anchors at RVA 0x003E16B4 and 0x003E16C1 (GetCommandLineA/W).
2. Inspect compare anchors at RVA 0x003B16A7 and 0x003F96DE (CompareStringW).
3. Inspect transport cluster at RVA 0x001C1C37..0x001C1F3E plus 0x001C44A1 and 0x001C6C1C/0x001C6C65.
4. Inspect singleton bridge around RVA 0x0028CB1F with nearby CreateFileW RVAs 0x0028CACC and 0x0028CC24.

## Expected output from this pass
- candidate parser function boundaries
- candidate vmr config destination store
- candidate transport wrapper function(s)
- promotion or falsification of hypothesis H02

## Evidence policy
- no confirmed label without direct code path evidence or runtime trace
- static-only claims stay at strongly_inferred/hypothesis

