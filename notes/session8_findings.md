# Session 8 Findings — confirmed `-vmr` parser-to-config store

Confidence key: confirmed / strongly_inferred / hypothesis / unknown

## Executive summary

Revised M1 is now closed successfully.

The obfuscated CLI literal `-vmr` is statically recovered at RVA `0x000E8F6E..0x000E8FA4` inside the central option parser `0x000E6870..0x000E9DDF`.

On a match, the parser constructs a VMR-specific descriptor via `0x000DD570`, supplies bounds `0..100`, and jumps into the common numeric option handler at `0x000E9D89 -> 0x00090AB0`.

The VMR descriptor vtable resolves to RVA `0x0043F0E8`. Its slot `+0x10` points to `0x000E10C0`, which performs the actual config write:

```asm
0x000E10C0: movsxd rax, dword ptr [rdx]
0x000E10C3: imul   rdx, rax, 0xd8
0x000E10CA: mov    rax, qword ptr [rcx + 8]
0x000E10CE: mov    rcx, qword ptr [rax + 0x2c0]
0x000E10D5: mov    eax, dword ptr [r8]
0x000E10D8: mov    dword ptr [rdx + rcx + 0xb0], eax
```

Therefore the parsed VMR value is stored in a per-GPU structure with:

- element stride: `0xD8`
- VMR field offset: `+0xB0`
- index source: `*(int32_t *)RDX`
- value source: `*(uint32_t *)R8`
- array/base pointer source: `*([descriptor+8] + 0x2C0)`

This is the first confirmed option-specific persistent config field in the project.

## Confirmed chain

```text
central option parser 0x000E6870..0x000E9DDF
    |
    | recovered literal -vmr @ 0x000E8F6E..0x000E8FA4
    v
string compare
    |
    | match @ 0x000E8FEE
    v
0x000DD570 descriptor constructor
    |
    | vtable = 0x0043F0E8
    | descriptor+8 = parser owner/context (RDI)
    v
common numeric option handler 0x00090AB0
    |
    | min = 0
    | max = 100
    v
virtual setter slot +0x10
    |
    v
0x000E10C0
    |
    v
per_gpu[index].field_0xB0 = parsed_vmr
```

## Neighboring timing options

The same parser block confirms the timing-family architecture:

- `-straps` -> constructor `0x000DD510`, max `6`
- `-vmr` -> constructor `0x000DD570`, max `100`
- `-rxboost` -> constructor `0x000DD5F0`, max `100`
- `-mt`, `-vmt2`, `-vmt3`, `-vmdag`, `-leavemt` are also statically recovered in the same option parser region.

This supports a family of small polymorphic field descriptors feeding one shared numeric parser.

## M1 status

Revised M1 goal was: `BIG_PARSER/application parser -> option-specific config value`.

Status: **CONFIRMED / CLOSED**.

No runtime experiment is required to prove the parser-to-config edge anymore.

## M2 active goal

Find consumers of:

```text
per_gpu_base + gpu_index * 0xD8 + 0xB0
```

and follow the first confirmed VMR-dependent consumer to:

- an AMD/NVIDIA timing transformation,
- vendor API,
- EIO/MMIO path,
- DeviceIoControl wrapper,
- or another hardware-facing register helper.

## Immediate static experiment

Scan executable code for memory accesses involving:

- displacement `0xB0`
- nearby `IMUL ..., 0xD8`
- loads from an object-derived base equivalent to `[owner+0x2C0]`

Rank exact stride+offset matches above generic `+0xB0` accesses.

A read of this field followed by timing/register logic is sufficient to promote the first M2 edge.
