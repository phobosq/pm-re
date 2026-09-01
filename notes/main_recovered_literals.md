# Recovered obfuscated literals from PM62C_MAIN

Method: group printable low-byte immediates from repeated `xor reg, imm` literal-builder sequences.

| begin RVA | end RVA | chars | recovered literal |
|---|---|---:|---|
| `0x00129B24` | `0x00129B78` | 4 | `L-vs` |
| `0x00129E3F` | `0x0012A063` | 20 | `DGPU_FORCE_64BIT_PTR` |
| `0x0012A1C2` | `0x0012A216` | 4 | `:100` |
| `0x0012A27A` | `0x0012A44A` | 17 | `GPU_MAX_HEAP_SIZE` |
| `0x0012A571` | `0x0012A75F` | 22 | `\1GPU_USE_SYNC_OBJECTS` |
| `0x0012A7ED` | `0x0012A811` | 3 | `899` |
| `0x0012A85B` | `0x0012AAB9` | 22 | `hGPU_MAX_ALLOC_PERCENT` |
| `0x0012AB3A` | `0x0012AB64` | 3 | `100` |
| `0x0012ABB0` | `0x0012AE65` | 25 | `nGPU_SINGLE_ALLOC_PERCENT` |
| `0x0012AF05` | `0x0012B0AF` | 19 | `1CUDA_CACHE_DISABLE` |
| `0x0012B2E5` | `0x0012B3CA` | 9 | `B-restart` |
| `0x0012B536` | `0x0012B776` | 33 | `!r!gns!qsdwhntr!horu\`obd!un!bmnrd` |
| `0x0012B7D8` | `0x0012B844` | 7 | `91,16?x` |
| `0x0012B9E4` | `0x0012BA72` | 6 | `'-help` |
| `0x0012BAFA` | `0x0012BB63` | 6 | `--help` |
| `0x0012BC37` | `0x0012BD1C` | 9 | `J-version` |
| `0x0012BD82` | `0x0012BE2A` | 9 | `--version` |
| `0x0012C036` | `0x0012C5A3` | 49 | `--config must be followed by the config file name` |
| `0x0012C827` | `0x0012C8E4` | 10 | `config.txt` |
| `0x0012CEFE` | `0x0012CF58` | 4 | `ECEC` |
| `0x0012CFEB` | `0x0012D640` | 57 | `yThe following options are not supported and are ignored:` |
| `0x0012D871` | `0x0012D949` | 10 | `mPA\KGLMSU` |

## High-value timing-related matches

- none in this pass