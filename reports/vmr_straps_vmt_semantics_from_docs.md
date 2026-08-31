# vmr/straps/vmt Semantics Seed (Readme)

## line 52
  PhoenixMiner is fast (arguably the fastest) **Ethash** (Ethereum, ETC,
> etc.) miner that supports both AMD and Nvidia cards (including in
  mixed mining rigs). It runs under Windows x64 and Linux x64 and has a
  developer fee of 0.65% (the lowest in the industry). This means that

## line 212
  
> * Supports Nvidia 30x0, 20x0, 16x0, 10x0 and 9x0 series as well as
    older cards with enough VRAM
  

## line 215
  
> * Partial unlocking of Nvidia LHR cards (applied automatically)
  
  * Nvidia LHR lock detection and real-time adjustment of the unlock

## line 217
  
> * Nvidia LHR lock detection and real-time adjustment of the unlock
    intensity
  

## line 549
  
> -nvidia
     Use only Nvidia cards
  

## line 550
  -nvidia
>    Use only Nvidia cards
  
  -nvmalt

## line 608
  -nvKernel <n>
>    Type of Nvidia kernel: 0 auto (default), 1 old (v1), 2 newer (v2),
     3 latest (v3). Note that v3 kernels are only supported on GTX10x0
     GPUs. Also note that dual mining is supported only by v2 kernels.

## line 614
  -nvdo <n>
>    Enable Nvidia driver-specific optimizations (0 - no, the default; 1
     - yes). Try "-nvdo 1" if your are unstable. You may specify this
     option per-GPU.

## line 619
  -nvNew <n>
>    Use new Nvidia kernels if supported (0: no, 1: yes; default: 1).
     You may specify this option per-GPU.
  

## line 623
  -nvf <n>
>    Nvidia kernel sync (0: never, 1: periodic; 2: always; 3: forced;
     default: 1). You may specify this option per-GPU.
  

## line 627
  -lhr <n>
>    Nvidia LHR unlock (0: no, -1: automatic, 100-1000: unlock
     intensity; default: -1). If this option is not specified (or
     specified as -1), the default LHR unlock intensity is 520. You may

## line 812
  -ttmem <n>
>    Set fan control target video memory temperature (can be used only
     on GPUs that report the VRAM temperature). Example: "-ttmem 83"
     will keep the GPU memory temperature at or bellow 83C by increasing

## line 814
     on GPUs that report the VRAM temperature). Example: "-ttmem 83"
>    will keep the GPU memory temperature at or bellow 83C by increasing
     the fan speed as necessary. This parameter can be combined with
     "-tt", and "-ttj"

## line 820
     Level of hardware monitoring: 0 - temperature and fan speed only; 1
>    - temperature, fan speed, and power; 2 - full (include core/memory
     clocks, voltages, P-states). The default is 1.
  

## line 874
  -cclock <n>
>    Set GPU core clock in MHz (0 for default). For Nvidia cards use
     relative values (e.g. -300 or +400)
  

## line 881
  -mclock <n>
>    Set GPU memory clock in MHz (0 for default). For Nvidia cards use
     relative values (e.g. -300 or +400)
  

## line 885
  -mvddc <n>
>    Set GPU memory voltage in mV (0 for default)
  
  -tstop <n>

## line 894
  -mt <n>
>    VRAM timings (AMD under Windows only): 0 - default VBIOS values; 1
     - faster timings; 2 - fastest timings. The default is 0. This is
     useful for mining with AMD cards without modding the VBIOS.

## line 895
     VRAM timings (AMD under Windows only): 0 - default VBIOS values; 1
>    - faster timings; 2 - fastest timings. The default is 0. This is
     useful for mining with AMD cards without modding the VBIOS.
  

## line 899
  -leavemt
>    Do not reset memory timing level ("-mt") to 0 when closing
  
  -ttli <n>

## line 921
     Lower GPU usage when VRAM temperature is above n deg C (can be used
>    only on GPUs that report the memory temperature). The default value
     is 0, which means do not lower the usage regardless of the GPU
     memory temperature. If you are using both "-ttmem" and "-tmaxmem"

## line 923
     is 0, which means do not lower the usage regardless of the GPU
>    memory temperature. If you are using both "-ttmem" and "-tmaxmem"
     options, the temperature in "-ttmem" should be lower than the
     "-tmaxmem" to avoid throttling the GPUs without using the fans to

## line 928
  
> -straps <n>
     Memory strap level (Nvidia cards 10x0 and P10x series only). The
     possible values are 0 to 6. 0 is the default value and uses the

## line 929
  -straps <n>
>    Memory strap level (Nvidia cards 10x0 and P10x series only). The
     possible values are 0 to 6. 0 is the default value and uses the
     default timings from the VBIOS. Each strap level corresponds to a

## line 931
     possible values are 0 to 6. 0 is the default value and uses the
>    default timings from the VBIOS. Each strap level corresponds to a
     predefined combination of memory timings ("-vmt1", "-vmt2",
     "-vmt3", "-vmr"). Strap level 3 is the fastest predefined level and

## line 932
     default timings from the VBIOS. Each strap level corresponds to a
>    predefined combination of memory timings ("-vmt1", "-vmt2",
     "-vmt3", "-vmr"). Strap level 3 is the fastest predefined level and
     may not work on most cards, 1 is the slowest (but still faster than

## line 935
     may not work on most cards, 1 is the slowest (but still faster than
>    the default timings). Strap levels 4 to 6 are the same as 1 to 3
     but with less aggressive refresh rates (i.e. lower "-vmr" values).
  

## line 936
     the default timings). Strap levels 4 to 6 are the same as 1 to 3
>    but with less aggressive refresh rates (i.e. lower "-vmr" values).
  
  -straps <n>

## line 938
  
> -straps <n>
     Memory strap level (AMD Vega cards only). The possible values are 0
     to 5. 0 is the default value and uses the default timings from the

## line 939
  -straps <n>
>    Memory strap level (AMD Vega cards only). The possible values are 0
     to 5. 0 is the default value and uses the default timings from the
     VBIOS. Each strap level corresponds to a predefined combination of

## line 940
     Memory strap level (AMD Vega cards only). The possible values are 0
>    to 5. 0 is the default value and uses the default timings from the
     VBIOS. Each strap level corresponds to a predefined combination of
     memory timings. Strap level 5 is the fastest level and may not work

## line 942
     VBIOS. Each strap level corresponds to a predefined combination of
>    memory timings. Strap level 5 is the fastest level and may not work
     on most cards, 1 is the slowest (but still faster than the default
     timings). Note that straps for AMD cards are experimental and may

## line 944
     on most cards, 1 is the slowest (but still faster than the default
>    timings). Note that straps for AMD cards are experimental and may
     lead to crashes or instability. "-vmt1", "-vmt2", and "-vmt3"
     parameters have no effect on AMD cards

## line 948
  
> -vmt1 <n>
     Memory timing parameter 1 (0 to 100, default 0)
  

## line 949
  -vmt1 <n>
>    Memory timing parameter 1 (0 to 100, default 0)
  
  -vmt2 <n>

## line 951
  
> -vmt2 <n>
     Memory timing parameter 2 (0 to 100, default 0)
  

## line 952
  -vmt2 <n>
>    Memory timing parameter 2 (0 to 100, default 0)
  
  -vmt3 <n>

## line 954
  
> -vmt3 <n>
     Memory timing parameter 3 (0 to 100, default 0)
  

## line 955
  -vmt3 <n>
>    Memory timing parameter 3 (0 to 100, default 0)
  
  -vmr <n>

## line 957
  
> -vmr <n>
     Memory refresh rate (0 to 100, default 0). For AMD cards you may
     also use "-rxboost"

## line 958
  -vmr <n>
>    Memory refresh rate (0 to 100, default 0). For AMD cards you may
     also use "-rxboost"
  

## line 962
  -nvmem <n>
>    Force using straps on unsupported Nvidia GPUs (0 - do not force, 1
     - GDDR5, 2 - GDDR5X). Make sure that the parameter matches your GPU
     memory type. You can try this if your card is Pascal-based but when

## line 964
     - GDDR5, 2 - GDDR5X). Make sure that the parameter matches your GPU
>    memory type. You can try this if your card is Pascal-based but when
     you try to use "-straps" or any other memory timing option, the
     card is shown as ?unsupported?.

## line 965
     memory type. You can try this if your card is Pascal-based but when
>    you try to use "-straps" or any other memory timing option, the
     card is shown as ?unsupported?.
  

## line 969
  -rxboost <n>
>    Memory refresh rate on AMD cards (0 - default value, 1 - predefined
     value that should work on most cards, 2 to 100 - increasingly
     aggressive settings). If you want to fine tune the value, you may

## line 980
  -mcdag <n>
>    Reset GPU memory clock to default during DAG generation. Nvidia
     only, default: 0 (turned off). This may allow you to set higher
     memory overclock on your Nvidia cards without risking corrupt DAG

## line 982
     only, default: 0 (turned off). This may allow you to set higher
>    memory overclock on your Nvidia cards without risking corrupt DAG
     buffer, which can lead to excessive number of stale shares.
  

## line 991
     seconds. This allows you to do all the following in the
>    "daggen.sh": turn off the overclocking of Nvidia GPUs, sleep for
     30-60 seconds, and then  re-apply the overclocking of the Nvidia
     GPUs.

## line 992
     "daggen.sh": turn off the overclocking of Nvidia GPUs, sleep for
>    30-60 seconds, and then  re-apply the overclocking of the Nvidia
     GPUs.
  

## line 1040
  
> * label "amd" or "nvidia": e.g. "amd:1090" sets the value to 1090
    for all AMD cards
  

## line 1047
    all cards which contain ?gtx? and ?1070? in their names with
>   anything between them. This will match ?Nvidia GeForce GTX 1070? but
    not ?Nvidia GeForce 1070?.
  

## line 1048
    anything between them. This will match ?Nvidia GeForce GTX 1070? but
>   not ?Nvidia GeForce 1070?.
  
  Note that if more than one selector matches given card, than only the

## line 1165
  
> * Most recent Nvidia drivers require running as administrator (or as
    root under Linux) to allow hardware control, so you must run
    PhoenixMiner as administrator for the VRAM timing options to work.

## line 1167
    root under Linux) to allow hardware control, so you must run
>   PhoenixMiner as administrator for the VRAM timing options to work.
  
  * The AMD memory timing options ("-rxboost", "-vmr", "-straps"),

## line 1169
  
> * The AMD memory timing options ("-rxboost", "-vmr", "-straps"),
    with the notable exception of "-mt", also require running as
    administrator (or as root under Linux)

## line 1173
  
> * When using the VRAM timing options ("-straps", "-vmt1", "-vmt2",
    "-vmt3", "-vmr"), start with lower values and make sure that the
    cards are stable before trying higher and more aggressive settings.

## line 1177
    You can use "-straps" along with the other options. For example
>   "-straps 1" "-vmt1 60" will use the timings from 1st strap level but
    -vmt1 will be set to 60 instead of whatever value is specified by
    the 1st strap level. In such case the "-straps" option must be

## line 1185
  
> * The VRAM timing options can be quite different between the GPUs,
    even when the GPUs are the same model. Therefore, you can (and
    probably should) specify the VRAM timing options per-GPU.

## line 1187
    even when the GPUs are the same model. Therefore, you can (and
>   probably should) specify the VRAM timing options per-GPU.
  
  * If you specify a single value (e.g. "-cvddc 1150"), it will be

## line 1210
    voltages, etc. MSI Afterburner also seems to behave OK (so you can
>   use it to control the Nvidia cards while AMD cards are controller by
    PhoenixMiner).
  

## line 1254
     A: Yes, but make sure that each GPU is used by a single miner (use
>    the -gpus, -amd, or -nvidia command-line options to limit the GPUs
     that given instance of PhoenixMiner actually uses).
  

## line 1335
  
> P002: My Nvidia GTX9x0 card is showing very low hashrate under Windows
  10!
     S: While there is a (convoluted) workaround, the best solution is

## line 1340
  
> P003: I'm using Nvidia GTX970 (or similar) card and my hashrate
  dropped dramatically for Ethereum or Ethereum classic!
     S: GTX970 has enough VRAM for larger DAGs but its hashate drops

## line 1362
  last message is "debugger detected"
>    S: If you have only Nvidia cards, add the option -nvidia to the
     PhoenixMiner.exe command line. If you have only AMD cards, add the
     option -amd to the command line.

