# Session 5 Findings

## Key Discoveries

### 1. Option Strings Are Encrypted
No plaintext strings for `-vmr`, `-straps`, `-vmt1`, `-vmt2`, `-vmt3` found anywhere in binary. All option names are encrypted/obfuscated and decrypted to BSS at runtime.

The string at `0x006C86A8` (used in opt_handler init) decodes only to `"C"` — confirming runtime string decryption.

### 2. SETTER_COMMON Architecture (0x003EA0C4..0x003EA0B6)
This is a large function that orchestrates GPU timing setup.

**Prologue:**
- `ESI = R8D` (arg3: 0 or 1)
- `EBX = EDX` (arg2: 0 or 2)
- `R14D = ECX` (arg1: parsed option value or 0)
- `JNZ 0x003EA133` if arg3≠0 (skip DLL loading phase)

**arg3=0 path** (DLL loading):
- `CALL [0x00430160]` = `GetModuleHandleExW` (loads some DLL)
- Validates PE header ('MZ', 'PE' checks)
- Atomically sets flag at `[0x007EDB66]` via `XCHG`

**Function pointer stored at [0x007EDB70]:**
- Written by `0x003EA31C`: stores `ROR(arg1, 64-(cookie&63)) XOR security_cookie`
- Read by SETTER_COMMON at `0x003EA178`
- Decryption in SETTER_COMMON:
  ```
  RDI = cookie XOR [0x007EDB70] = ROR(original_arg1, rot)
  ROR RDI, cookie&63  → RDI = original_arg1 (recovered!)
  CALL [0x00430900](RDI)  ← register with dispatch
  CALL RDI(0,0,0)         ← call the recovered function
  ```
- `[0x007EDB70]` stores an **encrypted FUNCTION POINTER** (not an integer)

### 3. Setter Stubs Classification

| Stub | ECX | EDX (arg2) | R8D (arg3) | Path |
|------|-----|-----------|-----------|------|
| 0x003EA31C | caller's | n/a | n/a | Init [0x007EDB70] — stores encrypted func ptr |
| 0x003EA360 | caller's | 0 | 0 | → ExitProcess path (help/version options?) |
| 0x003EA310 | caller's | 2 | 0 | → ExitProcess path |
| 0x003EA300 | 0 | 0 | 1 | → Normal return path (INIT mode) |
| 0x003EA2F0 | 0 | 2 | 1 | → Normal return path (INIT mode) |

**KEY INSIGHT**: Stubs with `arg3=0` (R8D=0) lead SETTER_COMMON to call `func_0x003EA230` which calls `ExitProcess(arg1)`. These are likely for options that exit the process (help, version, etc.).

Stubs with `arg3=1` (R8D=1) return normally — these are the INITIALIZATION stubs.

### 4. func_0x003EA230 = Process Exit Function
```
PUSH RBX; SUB RSP, 0x20
MOV EBX, ECX  ; save exit_code
CALL func_0x003FA0AC  ; check some condition
JZ → skip_peb_check
MOV RAX, GS:[0x60]  ; PEB
MOV EDX, [RAX+0xBC]  ; PEB.NtGlobalFlag or similar
SHR EDX, 8; TEST DL, 1; JNZ +0x11
→ ...some kernel path...
; final:
MOV ECX, EBX; CALL func_0x003EA27C  ; CorExitProcess(exit_code) if .NET
MOV ECX, EBX; CALL [0x00430158]     ; ExitProcess(exit_code)
```

### 5. func_0x003EA27C = CorExitProcess Helper
- Calls `GetModuleHandleExW(0, L"mscoree.dll", &handle)`
- Calls `GetProcAddress(handle, "CorExitProcess")`  
- Calls `[0x00430900](CorExitProcess_ptr)` — dispatch registration
- Calls `CorExitProcess(arg1)`
- Module name at `0x00717A78` in `.rdata` = `"mscoree.dll"` (UTF-16LE)
- Function name at `0x00717A90` in `.rdata` = `"CorExitProcess"` (ASCII)

### 6. Dynamic NVAPI Loading
- `func_0x003EA27C` uses `GetModuleHandleExW` + `GetProcAddress` pattern
- No NVAPI in static IAT — loaded dynamically at runtime
- Module name strings are NOT encrypted in .rdata (mscoree.dll, CorExitProcess visible)
- GPU timing API module name encrypted/runtime-decrypted at BSS

### 7. IAT Entries Confirmed
| IAT Address | Function |
|-------------|----------|
| 0x00430160 | KERNEL32.dll!GetModuleHandleExW |
| 0x004301E8 | KERNEL32.dll!GetProcAddress |
| 0x00430278 | KERNEL32.dll!CreateFileA |
| 0x00430158 | KERNEL32.dll!ExitProcess |
| 0x00430900 | Runtime-filled dispatch pointer (→ func at RVA 0x00067840) |

### 8. Globals 0x00717190..0x007171A0
- Read exclusively by `func_0x003E91F0` (pdata: 0x003E91F0..0x003EA0B6, size ~3.8KB)
- **ZERO RIP-relative writes** anywhere in binary
- Likely: NVAPI read-back buffers (GPU fills these) or runtime-set by NVAPI initialization
- Values: 32-bit each, read into RCX
- Gap: 0x00717190, 0x00717194, 0x00717198, 0x007171A0 (4-byte stride, except last gap is 8)

### 9. func_0x003E91F0 — Large Function (3.8KB)
- Spans 0x003E91F0..0x003EA0B6
- Contains all the reads from 0x00717190-0x007171A0
- ALSO contains SETTER_COMMON at 0x003EA0C4 WITHIN its pdata range!
  - Actually: pdata 0x003E91F0..0x003EA0B6, and SETTER_COMMON at 0x003EA0C4 is AFTER this range
  - Correction: SETTER_COMMON at 0x003EA0C4 is in a SEPARATE pdata range

Wait: from scan output:
```
pdata idx=12178  start=0x003E91F0  end=0x003EA0B6
```
And SETTER_COMMON starts at 0x003EA0C4 (which is AFTER 0x003EA0B6).
So func_0x003E91F0 ends at 0x003EA0B6, and SETTER_COMMON is a separate function at 0x003EA0C4.

### 10. Globals Near 0x007EDB70
| Address | Size | Content |
|---------|------|---------|
| 0x007EDB3C | 4 | argv_count |
| 0x007EDB40 | 8 | argv_ptr_table ptr |
| 0x007EDB50 | 8 | cmdlineA_ptr |
| 0x007EDB58 | 8 | cmdlineW_ptr |
| 0x007EDB60 | 8 | fallback_buf |
| 0x007EDB66 | 1? | atomic lock flag (XCHG via SETTER_COMMON) |
| 0x007EDB70 | 8 | encrypted function pointer (set by 0x003EA31C) |
| 0x007EDB78 | 1 | status byte (CMP to 0 in SETTER_COMMON) |
| 0x007EDB79 | 1 | status byte (CMP to 0 in SETTER_COMMON) |
| 0x007EDB7A | 1 | read by SETTER_COMMON (MOVZX EAX, byte []) |
| 0x007EDB7C | 1 | written by SETTER_COMMON (CMOVZ/MOV byte) |

## Still Unknown

1. **vmr INTEGER storage** — the parsed vmr value may only exist transiently in registers (R14D in SETTER_COMMON) and be applied to the GPU via the recovered function pointer (CALL RDI). No named BSS global found.

2. **What is the function stored encrypted at [0x007EDB70]?** — This is the key function called by SETTER_COMMON. It receives (0,0,0) as args. Likely it reads the current option value from the C++ object and applies to NVAPI.

3. **C++ option object structure** — vmr value likely stored at `[*[0x007EC638] + offset]` (heap). The vtable setter writes it there when parsing.

4. **wave2 (-straps, -vmt1/2/3)** — not yet investigated.

## Architecture Hypothesis

```
Startup flow:
1. opt_handler registers callback encrypted at [0x007EDB70] via CALL 0x003EA31C
2. BIG_PARSER parses argv, returns success/failure
3. Stubs 0x003EA300/0x003EA2F0 (init mode, arg3=1) initialize NVAPI session
4. The encrypted callback at [0x007EDB70] IS the option's "apply" method
5. SETTER_COMMON: decrypts → CALL RDI(0,0,0) where RDI is the apply method

Apply method (called as CALL RDI):
- Reads current vmr value from C++ option object
- Calls NVAPI timing function with that value
- The vmr integer lives in C++ object at heap+offset

The C++ object singleton pointer: [0x007EC638]
The vmr integer offset in object: TBD (likely +0x30 or similar)
```

## func_0x003F444C Calls 0x003EA2E8
- `0x003EA2E8`: tiny function `MOV [0x007EDB70], RCX; RET`
- Called from `func_0x003F444C` (1 time)
- Stores RCX directly to [0x007EDB70] (unencrypted!)
- This might be the RESET/CLEAR function for the timing handle
