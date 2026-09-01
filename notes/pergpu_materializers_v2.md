# per-GPU materializers v2

Fingerprint: owner `+0x2C0`, stride `0xD8`, timing offsets `{0x98,0xAC,0xB0,0xB8,0xBC}`.

| exact stride | timing offsets in same fn | PDATA | +0x2C0 | calls |
|---|---:|---|---:|---:|
| True | 0 | `0x000E07F0..0x000E0876` | 1 | 2 |
| True | 0 | `0x000E15A0..0x000E1605` | 1 | 2 |
| False | 5 | `0x000100F0..0x00025D56` | 2 | 37 |
| False | 5 | `0x00036DE0..0x00037E31` | 2 | 97 |
| False | 5 | `0x00059FE0..0x0005C50C` | 3 | 156 |
| False | 5 | `0x0008F720..0x0009001B` | 2 | 24 |
| False | 5 | `0x000E9DE0..0x000EF85E` | 2 | 369 |
| False | 5 | `0x00186B8A..0x0019038B` | 2 | 171 |
| False | 5 | `0x00192870..0x0019453B` | 3 | 46 |
| False | 5 | `0x0019B3E0..0x0019DD83` | 2 | 57 |
| False | 4 | `0x00053B50..0x00054A28` | 1 | 49 |
| False | 4 | `0x0007F0F0..0x000831BB` | 2 | 147 |
| False | 4 | `0x000AB450..0x000ACD15` | 1 | 56 |
| False | 4 | `0x001B22D0..0x001B5154` | 2 | 149 |
| False | 3 | `0x0004B100..0x0004D5EC` | 3 | 154 |
| False | 3 | `0x000710F0..0x00071A4E` | 1 | 61 |
| False | 3 | `0x00074AB0..0x00079CAC` | 1 | 243 |
| False | 3 | `0x000A2870..0x000A459E` | 2 | 104 |
| False | 3 | `0x000A45A0..0x000A71B9` | 2 | 123 |
| False | 3 | `0x000B4A20..0x000B5D82` | 2 | 88 |
| False | 3 | `0x000CAAD0..0x000D9A27` | 2 | 364 |
| False | 3 | `0x000E2100..0x000E2F25` | 3 | 76 |
| False | 3 | `0x00129A50..0x0012DA40` | 1 | 203 |
| False | 3 | `0x001AB9B0..0x001AD581` | 1 | 78 |
| False | 3 | `0x001AD600..0x001AD930` | 1 | 15 |
| False | 3 | `0x001B9E60..0x001BBB38` | 1 | 125 |
| False | 3 | `0x001BE210..0x001BF98F` | 1 | 111 |
| False | 3 | `0x001F3A60..0x001F72AD` | 1 | 92 |
| False | 3 | `0x001F7F40..0x001FB9C1` | 2 | 144 |
| False | 3 | `0x00211460..0x002148C7` | 1 | 132 |
| False | 3 | `0x0026A150..0x0026AEB8` | 1 | 90 |
| False | 3 | `0x00277170..0x00279741` | 1 | 161 |
| False | 2 | `0x000B20D0..0x000B251B` | 2 | 16 |
| False | 2 | `0x000BE420..0x000C6E75` | 2 | 376 |
| False | 2 | `0x000C70E0..0x000CA069` | 3 | 105 |
| False | 2 | `0x000E00C0..0x000E04FD` | 1 | 2 |
| False | 2 | `0x00174750..0x0017765C` | 2 | 95 |
| False | 2 | `0x001A76C0..0x001A7973` | 1 | 10 |
| False | 2 | `0x001B6B20..0x001B74AD` | 1 | 41 |
| False | 2 | `0x001B8F10..0x001B918F` | 1 | 8 |
| False | 2 | `0x00269770..0x0026A149` | 2 | 53 |
| False | 2 | `0x00283B10..0x0028560C` | 2 | 78 |
| False | 2 | `0x0029ED60..0x0029FB8B` | 2 | 102 |
| False | 2 | `0x003BB090..0x003BB497` | 1 | 36 |
| False | 1 | `0x000667B0..0x00066CD1` | 2 | 11 |
| False | 1 | `0x00067D70..0x00067F28` | 1 | 13 |
| False | 1 | `0x00091D10..0x000924B1` | 1 | 38 |
| False | 1 | `0x0012F250..0x0012F86D` | 1 | 27 |
| False | 1 | `0x0013BFD0..0x0013C0F3` | 1 | 3 |
| False | 1 | `0x001621A0..0x00163854` | 1 | 63 |
| False | 1 | `0x001AF830..0x001B2010` | 3 | 109 |
| False | 1 | `0x001BC490..0x001BDADF` | 2 | 113 |
| False | 1 | `0x00200150..0x00201A76` | 46 | 50 |
| False | 1 | `0x0020D030..0x0020E8E3` | 46 | 50 |
| False | 1 | `0x00217690..0x00219A53` | 2 | 106 |
| False | 1 | `0x00241EA0..0x00243CD4` | 3 | 172 |
| False | 1 | `0x0024D370..0x0024E3DE` | 2 | 36 |
| False | 1 | `0x003BD3A4..0x003BD4F4` | 2 | 13 |
| False | 0 | `0x00005E52..0x000068FD` | 1 | 93 |
| False | 0 | `0x0003B320..0x0003C830` | 4 | 112 |
| False | 0 | `0x00065DB0..0x00066524` | 1 | 40 |
| False | 0 | `0x000B3A80..0x000B4740` | 1 | 37 |
| False | 0 | `0x000E2040..0x000E20FA` | 2 | 3 |
| False | 0 | `0x000E6870..0x000E9DDF` | 1 | 200 |
| False | 0 | `0x000EFDC0..0x00122EDF` | 2 | 158 |
| False | 0 | `0x00134FE0..0x00135326` | 2 | 14 |
| False | 0 | `0x001438F0..0x00144E2B` | 2 | 48 |
| False | 0 | `0x0017AE80..0x0017AFA2` | 1 | 5 |
| False | 0 | `0x0017E730..0x00180AFD` | 2 | 40 |
| False | 0 | `0x00181C80..0x00181E4C` | 1 | 7 |
| False | 0 | `0x00182AE0..0x001833E3` | 1 | 30 |
| False | 0 | `0x00183460..0x001862DE` | 2 | 62 |
| False | 0 | `0x00196DE0..0x0019B06D` | 2 | 68 |
| False | 0 | `0x0019F220..0x001A2564` | 2 | 57 |
| False | 0 | `0x001A8290..0x001A84A5` | 1 | 20 |
| False | 0 | `0x001B65F0..0x001B6745` | 1 | 5 |
| False | 0 | `0x001E0EC0..0x001E1F65` | 1 | 23 |
| False | 0 | `0x001E1F70..0x001E2FD9` | 4 | 23 |
| False | 0 | `0x001E5160..0x001E6C7D` | 2 | 33 |
| False | 0 | `0x001E6C80..0x001E8A0A` | 1 | 33 |
| False | 0 | `0x001F1160..0x001F143E` | 1 | 3 |
| False | 0 | `0x002077E0..0x00207F51` | 1 | 16 |
| False | 0 | `0x002157F0..0x00217688` | 1 | 116 |
| False | 0 | `0x002710E0..0x00271E67` | 2 | 88 |
| False | 0 | `0x00292D90..0x00292F2C` | 1 | 22 |
| False | 0 | `0x00293538..0x00293646` | 2 | 7 |
| False | 0 | `0x00299A30..0x0029A6E2` | 1 | 68 |
| False | 0 | `0x0029C674..0x0029DA4C` | 1 | 96 |
| False | 0 | `0x002A2860..0x002A2995` | 1 | 18 |
| False | 0 | `0x002A5580..0x002A563A` | 1 | 7 |
| False | 0 | `0x002A5660..0x002A5731` | 1 | 5 |
| False | 0 | `0x002A5B10..0x002A5C15` | 2 | 10 |
| False | 0 | `0x002A5C20..0x002A5EC9` | 3 | 20 |
| False | 0 | `0x002A5ED0..0x002A5FE4` | 2 | 7 |
| False | 0 | `0x002A5FF0..0x002A60C6` | 2 | 6 |
| False | 0 | `0x002AAFE0..0x002AB100` | 2 | 6 |
| False | 0 | `0x002AC860..0x002AC971` | 3 | 4 |
| False | 0 | `0x002AC980..0x002ACAA4` | 1 | 5 |
| False | 0 | `0x002BB6B0..0x002BB7DE` | 1 | 5 |
| False | 0 | `0x002BB961..0x002BB9B0` | 1 | 1 |
| False | 0 | `0x002BBB53..0x002BBB8D` | 1 | 0 |
| False | 0 | `0x00370C80..0x003728CC` | 1 | 94 |
| False | 0 | `0x0037EF20..0x0037F043` | 1 | 7 |
| False | 0 | `0x003BF988..0x003BFAE3` | 1 | 8 |
| False | 0 | `0x003BFAF4..0x003BFB3A` | 1 | 4 |
| False | 0 | `0x004189C5..0x00418CDB` | 2 | 4 |
| False | 0 | `0x0042576D..0x00425796` | 1 | 1 |

## Exact-stride details

### `0x000E07F0..0x000E0876` — offsets none

```asm
0x000E0819: call 0x1403e69f8
0x000E0825: imul rbx, rbx, 0xd8
0x000E082C: add rbx, qword ptr [rax + 0x2c0]
0x000E0833: call 0x1403e6d3c
```

### `0x000E15A0..0x000E1605` — offsets none

```asm
0x000E15CC: call 0x1403e69f8
0x000E15D9: imul rbx, rbx, 0xd8
0x000E15E0: add rbx, qword ptr [rax + 0x2c0]
0x000E15E7: call 0x1403e6d3c
```
