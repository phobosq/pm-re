# CLI Entrypoints Seed (Updated)

status: static docs seed ready; direct binary token visibility is weak.

confirmed_from_docs:
- -vmr
- -straps
- -vmt1
- -vmt2
- -vmt3
- -mt

binary_visibility:
- ASCII token extraction from PhoenixMiner.exe: no direct hits for vmr/straps/vmt (strongly_inferred)
- UTF-16 token extraction from PhoenixMiner.exe: weak artifact mt-MT only (strongly_inferred)

implication:
- prioritize xref from parser comparators and dynamic compare tracing rather than raw string xrefs.

next_steps:
1. Set breakpoints on strcmp/wcsicmp equivalents and argv traversal.
2. Track store to config structure for vmr first.
3. Follow vmr consumer into transport candidate path.
