# Session 6 Findings — M1 falsification and CRT-cluster reclassification

Confidence key: confirmed / strongly_inferred / hypothesis / unknown

## Executive summary

Milestone 1 started from the Session 5 hypothesis that `[0x007EDB70]` contains an encrypted GPU-timing apply callback consumed by the routine around `0x003EA0C4`.

That hypothesis is now **falsified**.

The `0x003EA0xx..0x003EA36x` cluster is runtime startup/termination plumbing, very strongly matching MSVC/UCRT-style process-exit support rather than a PhoenixMiner GPU backend. The evidence is internally consistent:

- `0x003EA230` terminates the process and reaches `ExitProcess`.
- `0x003EA27C` dynamically resolves and calls `CorExitProcess` from `mscoree.dll`.
- `0x003EA31C` encodes/stores a function pointer using the process security cookie and rotation.
- the corresponding consumer decodes the pointer before invoking/registering it.
- `0x003EA2E8` is a second tiny setter for the same storage and is reached from runtime-adjacent code near `0x003F444C`.

There is no direct evidence in this cluster that the stored callback is a VRAM timing callback, and the previous Session 5 statement "Dynamic NVAPI Loading" was not supported by the observed `GetModuleHandleExW`/`GetProcAddress` calls: the resolved module/function pair that is actually proven here is `mscoree.dll!CorExitProcess`.

## Confirmed observations

### C21 — `[0x007EDB70]` belongs to runtime callback/termination state, not proven GPU state

Observed writers/readers:

- `0x003EA2E8`: direct `MOV [0x007EDB70], RCX; RET` style setter.
- `0x003EA31C..0x003EA359`: security-cookie based pointer encoding and store to `[0x007EDB70]`.
- routine around `0x003EA178`: decodes the stored pointer before indirect use.

The encode/decode symmetry is characteristic of protected runtime function-pointer storage. Nothing in the demonstrated chain carries a `-vmr` value, GPU object, PCI identity, timing structure, NVAPI function ID, EIO handle, or IOCTL request.

confidence: confirmed for pointer storage/encoding behavior; strongly_inferred for CRT ownership.

### C22 — `0x003EA230` / `0x003EA27C` anchor the cluster to process termination

`0x003EA230` preserves an exit code and ultimately calls the helper at `0x003EA27C` and imported `ExitProcess`.

`0x003EA27C` resolves:

- module: `mscoree.dll`
- function: `CorExitProcess`

and invokes it before normal process termination handling.

This is strong architectural evidence that the neighboring callback machinery is part of CRT/managed-runtime shutdown handling.

confidence: confirmed.

### C23 — Session 5 NVAPI inference is retracted

Session 5 inferred dynamic NVAPI loading from a generic `GetModuleHandleExW` + `GetProcAddress` pattern. The concrete strings recovered from this path identify `mscoree.dll!CorExitProcess`, not NVAPI.

Therefore:

- `GetProcAddress` in this cluster is not evidence of NVAPI.
- no NVAPI timing function has yet been identified.
- no GPU write path has yet been connected to the parser.

confidence: confirmed correction.

## Falsified architecture

The following Session 5 model must not be used going forward:

```text
opt_handler
  -> store encrypted GPU apply callback in [0x007EDB70]
  -> SETTER_COMMON
  -> decrypt callback
  -> call timing/NVAPI apply method
```

Current status: **falsified**.

## Revised parser-side state

The useful parser work remains valid:

```text
GetCommandLineA/W
  -> PR01 0x003E16B0
  -> ARGT01 0x003F37E4 (tokenization)
  -> argv globals 0x007EDB3C / 0x007EDB40
  -> OPT_DISP 0x003B2714
  -> BIG_PARSER 0x00129A50
  -> indirect/C++ dispatch still unresolved
```

The next unresolved edge is therefore **inside/after BIG_PARSER and its indirect dispatch**, not the CRT cluster at `0x003EA0xx`.

## Revised Milestone 1

### Goal

Find one option-specific object/handler reached from `BIG_PARSER`, and prove a `-vmr`-dependent value store or value flow.

### Static work

1. Classify indirect calls inside `0x00129A50..0x0012DA40`.
2. Recover the table/vtable/object source for each high-value indirect call.
3. Identify handlers that receive an argv token or parsed integer and mutate persistent object state.
4. Exclude CRT/runtime functions by import/context signatures before promoting any handler to GPU relevance.

### Runtime proof target

Use paired runs:

```text
control: no -vmr
active1: -vmr 17
active2: -vmr 31
```

At the first option-dispatch handler after `BIG_PARSER`, capture:

- `this` pointer / object base
- input token/value
- writes to `[this+offset]` or another persistent config object
- indirect call target

A field that tracks `0 -> 17 -> 31` (or equivalent encoded representation) is sufficient to promote the parser→config edge to confirmed.

## Revised Milestone 2

After the `vmr` config field/handler is confirmed, follow **its consumer** downward until it reaches one of:

- EIO export
- DeviceIoControl wrapper
- vendor API / dynamically resolved GPU function
- direct register/MMIO helper

Do not start from generic transport candidates and search upward unless the parser-driven trace stalls.

## Guardrails

1. `0x003EA0xx..0x003EA36x` is now a negative landmark: runtime/termination cluster.
2. Security-cookie encoded function pointers are not evidence of GPU obfuscation by themselves.
3. Generic `GetProcAddress` usage must be tied to the resolved module/function name before assigning a vendor API.
4. No function gets a `VMR_*`, `NVAPI_*`, `VRAM_*`, or timing-specific label without data-flow or runtime evidence.

## Milestone status

- Original M1 (`resolve [0x007EDB70] as GPU apply callback`): **closed / falsified**.
- Revised M1 (`BIG_PARSER -> option-specific config value`): **active**.
- M2 (`confirmed vmr consumer -> hardware transport`): blocked on revised M1.
