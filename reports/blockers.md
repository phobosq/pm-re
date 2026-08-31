# Blockers and Mitigations

## B1: Host-side removal after unpack
status: active
impact: blocks direct runtime trace on current host
observed: PhoenixMiner.exe and IOMap64.sys present in ZIP but missing after unpack
mitigation: use isolated VM workflow that preserves sample; keep ZIP immutable source; perform static analysis via zip-stream/in-memory extraction

## B2: Weak direct CLI token visibility in binary strings
status: active
impact: slows parser xref seeding for vmr/straps/vmt
mitigation: comparator tracing path (GetCommandLine*/CompareStringW + store tracking)

## B3: Transport not yet runtime-confirmed
status: active
impact: blocks semantically safe analysis of straps/vmt fields
mitigation: finish vmr wave1 A/B trace first; then unlock straps/vmt wave2

## Exit criteria for blockers
1. vmr parser->consumer path mapped.
2. device path + IOCTL/control surface captured at runtime.
3. first vmr argument->write chain reaches confirmed level.

