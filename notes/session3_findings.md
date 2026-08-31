# vmr Static Parser Bridge — Session 3 Findings
# Confidence key: confirmed / strongly_inferred / hypothesis / unknown

## Executive Summary

Static continuation of the parser path found a concrete read-side consumer of the `GetCommandLineA` pointer captured by `PR01`.
The new bridge is:

`PR01 (0x003E16B0)` -> stores `GetCommandLineA/W` into globals `0x1407EDB50/0x1407EDB58`

`ARGT01 (0x003F37E4..0x003F3947)` -> reads `0x1407EDB50`, falls back to a local buffer when empty, tokenizes the ANSI command line, and stores argv-like globals at `0x1407EDB3C`, `0x1407EDB40`, and `0x1407EDB60`

This upgrades the parser-entry story from "tiny cmdline snapshot" to "snapshot plus concrete downstream tokenization bridge".

## Confirmed / Strongly Inferred Facts

1. `PR01` performs only two import calls and two global stores:
   - `0x003E16B4 -> GetCommandLineA`, stored to `0x1407EDB50`
   - `0x003E16C1 -> GetCommandLineW`, stored to `0x1407EDB58`
2. `ARGT01` reads `0x1407EDB50` at `0x003F3835`.
3. If that pointer is null or points to an empty string, `ARGT01` substitutes a local buffer rooted near `0x1407EDDA0`.
4. `ARGT01` then passes the chosen string through internal splitter/allocation helpers and writes parser-state globals:
   - `0x003F38CA -> [0x1407EDB40] = token pointer table`
   - `0x003F38D1 / 0x003F3923 -> [0x1407EDB3C] = count-like value`
   - `0x003F383E -> [0x1407EDB60] = fallback/source buffer`
5. A later cleanup path near `0x003F44BD..0x003F44E5` frees and clears `0x1407EDB40` (and adjacent parser-state storage), consistent with argc/argv lifecycle handling.

## Negative / Still-Missing Results

- No static xref to `0x1407EDB58` beyond the initial `GetCommandLineW` store was found in this pass.
- No `-vmr`-specific compare/store consumer was confirmed from the argv-like globals in this pass.
- No parser -> transport direct call edge was introduced by this result; the shared-global hypothesis remains intact.

## Implications

- `PR01` should now be treated as a real parser seed, not just an isolated CLI-adjacent stub.
- The best runtime choke point moves from the raw `GetCommandLine*` entry alone to the tokenizer bridge around `0x003F3835` and the first consumer of `0x1407EDB40`.
- Compare-path A/B may still matter, but both now look more like later string/locale helpers than the earliest parser ingress.

## Recommended Next Steps

1. Runtime: break on `0x003F3835` and log whether execution uses `[0x1407EDB50]` or the fallback buffer.
2. Runtime: after `0x003F38CA/0x003F392F`, dump the token table at `0x1407EDB40` and count at `0x1407EDB3C`.
3. Static: find all read-side xrefs to `0x1407EDB40`/`0x1407EDB3C` and classify the first option-dispatch consumer.
4. Only after locating the first argv consumer, resume prioritization between compare-path A and compare-path B for `-vmr` token confirmation.
