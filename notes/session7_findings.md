# Session 7 Findings — argv chain reclassification and true main entry

Confidence key: confirmed / strongly_inferred / hypothesis / unknown

## Executive summary

Session 6 removed the false GPU interpretation of the `0x003EA0xx..0x003EA36x` cluster. Re-reading the surrounding argv flow changes the interpretation of `0x003B2714` as well.

The function previously labeled `OPT_DISP` is very strongly consistent with a CRT/C++ runtime wrapper that prepares `argc/argv`, calls the program's real `main`, and then performs exit/cleanup handling.

The important consequence is:

```text
0x003B2714 = runtime main-invocation wrapper (strongly_inferred)
0x00129A50 = PhoenixMiner application main(argc, argv, ...), or equivalent top-level app entry (strongly_inferred)
```

The real PhoenixMiner option analysis should therefore start inside `0x00129A50`, not in the CRT argv construction and termination code around `0x003Bxxxx/0x003Exxxx`.

## Evidence

### C24 — argv creation is runtime infrastructure

Previously established facts:

- `0x003E16B0` snapshots `GetCommandLineA/W`.
- `0x003F37E4` tokenizes the ANSI command line into globals:
  - `0x007EDB3C` count-like value
  - `0x007EDB40` argv pointer table
  - `0x007EDB60` fallback/source buffer
- `0x003E16D8` returns the address of the argc-like global.
- `0x003E16E0` returns the address of the argv-like global.
- cleanup at `0x003F4464..0x003F44F2` frees/clears argv state.

This lifecycle is characteristic of CRT command-line construction rather than an application-specific option parser.

confidence: strongly_inferred.

### C25 — `0x003B2714` calls argc/argv accessors immediately before `0x00129A50`

Relevant call sequence from the existing static call census:

```text
0x003B280F -> 0x003E16E0  get_argv_ptr_table
0x003B2817 -> 0x003E16D8  get_argv_count
0x003B281F -> 0x003F3F08
0x003B282C -> 0x00129A50
```

The same function then enters the previously misclassified termination cluster:

```text
0x003B283E -> 0x003EA360
0x003B2848 -> 0x003EA300
...
0x003B2867 -> 0x003EA310
0x003B2874 -> 0x003EA2F0
```

Session 6 established that the `0x003EA...` targets are process-exit/runtime helpers, not timing setters.

Therefore the structural interpretation is now:

```text
CRT argv preparation
    -> obtain argv
    -> obtain argc
    -> obtain third startup argument / environment-like state
    -> call 0x00129A50
    -> runtime exit/cleanup
```

confidence: strongly_inferred.

### C26 — old `OPT_DISP` label is retired

The label `OPT_DISP` implied application option dispatch. There is no longer sufficient evidence for that meaning.

New working label:

```text
PM62C_CRT_MAIN_WRAPPER = 0x003B2714..0x003B288B
```

The absence of normal direct callers is no longer evidence of C++ vtable dispatch; runtime entry wrappers are commonly reached through startup indirection.

confidence: strongly_inferred.

### C27 — `0x00129A50` becomes the highest-priority application entry

Existing analysis already shows:

- range `0x00129A50..0x0012DA40`
- size about 16 KB
- receives argv from the CRT wrapper
- contains references interpreted as `System.Object[]` and `"-"`

The current `bigparser_analysis.md` is incomplete because its indirect-call scanner only catches RIP-relative `CALL [rip+disp32]`. It misses the forms most important for object dispatch:

- `CALL RAX/RBX/...`
- `CALL [RAX+disp]`
- `CALL [RAX+RCX*scale+disp]`
- other ModRM/SIB memory-indirect forms

This explains why the prior static pass could not meaningfully classify the interior of `0x00129A50`.

confidence: confirmed limitation of the scanner; strongly_inferred application-entry interpretation.

## Corrections to earlier sessions

### Session 3

`PR01` / `ARGT01` remain valid technical landmarks, but they should be treated as CRT command-line/argv construction, not as PhoenixMiner-specific parsing.

### Session 4

`OPT_DISP` is retired and should not be used as an option-dispatch label.

The conclusion that missing edges imply C++ vtable dispatch was premature. The immediate `0x003B2714 -> 0x00129A50` edge is a normal direct call and appears to be the transition from runtime into application code.

### Session 5

The timing/NVAPI interpretation of the termination cluster remains retracted per Session 6.

## Revised architecture

```text
Windows command line
    |
    v
CRT command-line snapshot / argv builder
0x003E16B0 / 0x003F37E4
    |
    v
PM62C_CRT_MAIN_WRAPPER
0x003B2714
    |
    | argc / argv / startup state
    v
PM62C_MAIN
0x00129A50..0x0012DA40
    |
    +--> application option/config logic   <-- CURRENT TARGET
    |
    +--> GPU enumeration / initialization
    |
    +--> mining/application setup
    |
    +--> timing/backend consumers
```

## Revised Milestone 1

### Goal

Identify the first application-level option processing inside `PM62C_MAIN`, with emphasis on discovering how argv entries are compared/decoded and where their values are stored.

### Immediate static tasks

1. Disassemble all of `0x00129A50..0x0012DA40` with a real x86-64 decoder.
2. Enumerate every direct and indirect `CALL`, including register and arbitrary memory-indirect forms.
3. Track the incoming Windows x64 argument registers at entry:
   - `RCX` — likely argc
   - `RDX` — likely argv
   - `R8` — likely env/startup third argument
4. Identify which nonvolatile registers / stack slots receive those arguments.
5. Find loops indexing the argv pointer array.
6. From those loops, identify string comparison/decryption/hash functions and value conversion functions.
7. Only then search for a `-vmr`-specific path.

## Success criterion for next pass

A result such as:

```text
PM62C_MAIN 0x00129A50
  RDX(argv) -> R14
  argc -> EBX
  loop @ 0x00xxxxxx
      argv[i] -> helper 0x00yyyyyy
      token discriminator -> handler 0x00zzzzzz
```

is sufficient to establish the first true application parser anchor.

No GPU/timing label is required yet.

## Tooling change

The old `analyze_bigparser.ps1` scanner is useful for RIP-relative references but is insufficient for this milestone because its indirect-call detector only recognizes `FF /2` with RIP-relative addressing.

A new Capstone-based call census should be used to cover all x86-64 call forms and retain surrounding instruction context.

## Milestone status

- Session 6 CRT termination reclassification: closed / retained.
- `0x003B2714` as Phoenix option dispatcher: **falsified**.
- `0x003B2714` as CRT main wrapper: **strongly_inferred**.
- `0x00129A50` as application main/top-level entry: **strongly_inferred**.
- Revised M1: locate argv/token handling inside `0x00129A50`: **active**.
