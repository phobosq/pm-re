param(
    [string]$BinPath = 'C:\temp\pm\samples\work\unpacked\PhoenixMiner_6.2c_Windows\PhoenixMiner.exe.bin',
    [string]$OutDir  = 'C:\temp\pm\notes'
)
$ErrorActionPreference = 'Stop'

Add-Type @'
using System; using System.Collections.Generic;
public class BFS {
    public static List<long[]> GetOutbound(byte[] bytes, int rvaStart, int rvaEnd, int textOff, int textVA) {
        int off = textOff + (rvaStart - textVA);
        int size = rvaEnd - rvaStart;
        var calls = new List<long[]>();
        for (int i = 0; i < size - 5; i++) {
            byte b = bytes[off + i];
            if (b == 0xE8 || b == 0xE9) {
                int disp = BitConverter.ToInt32(bytes, off + i + 1);
                long tgt = (long)(rvaStart + i + 5) + disp;
                if (tgt > 0x1000 && tgt < 0x800000)
                    calls.Add(new long[] { b == 0xE8 ? 0 : 1, rvaStart + i, (int)(tgt & 0xFFFFFFFFL) });
                i += 4;
            }
        }
        return calls;
    }
    public static int Bsearch(int[] starts, int[] ends, int rva) {
        int lo=0,hi=starts.Length-1;
        while(lo<=hi){int m=(lo+hi)/2;if(rva<starts[m])hi=m-1;else if(rva>=ends[m])lo=m+1;else return m;}
        return -1;
    }
}
'@

function Get-U16([byte[]]$b,[int]$o){ [BitConverter]::ToUInt16($b,$o) }
function Get-U32([byte[]]$b,[int]$o){ [BitConverter]::ToUInt32($b,$o) }

$bytes = [System.IO.File]::ReadAllBytes($BinPath)
$peOff = Get-U32 $bytes 0x3C
$secCount = Get-U16 $bytes ($peOff+6)
$optSz = Get-U16 $bytes ($peOff+20)
$secOff = $peOff+24+$optSz
$textOff=0; $textVA=0; $textSz=0; $pdOff=0; $pdSz=0
for($i=0;$i -lt $secCount;$i++){
    $o=$secOff+40*$i
    $n=[Text.Encoding]::ASCII.GetString($bytes,$o,8).Trim([char]0)
    $va=Get-U32 $bytes ($o+12); $rs=Get-U32 $bytes ($o+16); $rp=Get-U32 $bytes ($o+20)
    if($n -eq '.text'){ $textOff=[int]$rp; $textVA=[int]$va; $textSz=[int]$rs }
    if($n -eq '.pdata'){ $pdOff=[int]$rp; $pdSz=[int]$rs }
}
$pdCnt=[int]($pdSz/12)
$pdStarts=[int[]]::new($pdCnt); $pdEnds=[int[]]::new($pdCnt)
for($i=0;$i -lt $pdCnt;$i++){
    $pdStarts[$i]=[BitConverter]::ToInt32($bytes,$pdOff+12*$i)
    $pdEnds[$i]  =[BitConverter]::ToInt32($bytes,$pdOff+12*$i+4)
}

function Get-FuncRange([int]$rva){
    $fi=[BFS]::Bsearch($pdStarts,$pdEnds,$rva)
    if($fi -ge 0){ return [PSCustomObject]@{begin=$pdStarts[$fi];end=$pdEnds[$fi]} }
    return $null
}

# Known target functions we want to find reachability to
$targetFuncs = @{
    0x003B160C = 'PR02_compare_A'
    0x003F9610 = 'PR03_compare_B'
    0x001C3A30 = 'DISP01_transport'
    0x003E16B0 = 'PR01_parser_cmdline'
}

# BFS from OPT_DISP to depth 3, tracking which known functions are reachable
$bfsQueue = [System.Collections.Generic.Queue[int]]::new()
$visited = [System.Collections.Generic.HashSet[int]]::new()
$reachable = @{}
$callEdges = @()

# Seed: OPT_DISP and its direct callees
$seedFuncs = @(
    0x003B2714,  # OPT_DISP
    0x003B2238,  # called 2x from OPT_DISP
    0x003B2120,  # first helper
    0x003B20E4,  # third helper
    0x003B22D4,  # another helper
    0x003F463C,  # helper in 3F area
    0x003F45C4,  # helper in 3F area
    0x003EA31C,  # called just before argv getters
    0x003F3F08,  # tiny helper after argv getters
    0x003B2F6C,  # called 2x at end
    0x003EA360,0x003EA300,0x003EA310,0x003EA2F0  # terminal setters
)

foreach($s in $seedFuncs){ [void]$bfsQueue.Enqueue($s) }

$maxDepth = 4
$depthMap = @{}
foreach($s in $seedFuncs){ $depthMap[$s]=0 }

$md = @()
$md += '# BFS Reachability from OPT_DISP chain (depth 4)'
$md += '# Goal: find paths to PR02 (CompareStringW) and transport'
$md += ''

while($bfsQueue.Count -gt 0){
    $funcRva = $bfsQueue.Dequeue()
    if($visited.Contains($funcRva)){ continue }
    [void]$visited.Add($funcRva)
    $depth = if($depthMap.ContainsKey($funcRva)){ $depthMap[$funcRva] } else { 999 }
    if($depth -gt $maxDepth){ continue }
    
    # Mark if this is a target
    if($targetFuncs.ContainsKey($funcRva)){
        $reachable[$funcRva] = $targetFuncs[$funcRva]
    }
    
    $fr = Get-FuncRange $funcRva
    if(-not $fr){ continue }
    
    $outbound = [BFS]::GetOutbound($bytes,$fr.begin,$fr.end,$textOff,$textVA)
    foreach($c in $outbound){
        $tgt=[int]$c[2]
        if(-not $visited.Contains($tgt)){
            if(-not $depthMap.ContainsKey($tgt)){
                $depthMap[$tgt]=$depth+1
                [void]$bfsQueue.Enqueue($tgt)
            }
        }
        if($targetFuncs.ContainsKey($tgt)){
            $callEdges += [PSCustomObject]@{
                from_rva  ='0x{0:X8}' -f $funcRva
                to_rva    ='0x{0:X8}' -f $tgt
                to_label  = $targetFuncs[$tgt]
                from_depth= $depth
            }
        }
    }
}

$md += '## Reachable target functions from OPT_DISP chain:'
if($reachable.Count -eq 0){
    $md += '  (none found within depth ' + $maxDepth + ')'
} else {
    foreach($k in $reachable.Keys){
        $md += ('  REACHABLE: 0x{0:X8}  {1}  (depth={2})' -f $k,$reachable[$k],$depthMap[$k])
    }
}
$md += ''

$md += '## Direct call edges to target functions:'
foreach($e in $callEdges){
    $md += ('  ' + $e.from_rva + ' -> ' + $e.to_rva + '  [' + $e.to_label + ']  (caller depth=' + $e.from_depth + ')')
}
$md += ''

# Also: find callers of OPT_DISP via a wider search (JMP + CALL indirect hint)
# Look at the byte-range callers specifically
$md += '## OPT_DISP area context (what else is in 0x003B2xxx?)'
# List all pdata functions in 0x003B2000..0x003B3000
for($i=0;$i -lt $pdCnt;$i++){
    if($pdStarts[$i] -ge 0x003B2000 -and $pdStarts[$i] -lt 0x003B3000){
        $lbl=''
        $md += ('  func 0x{0:X8}..0x{1:X8} size=0x{2:X}' -f $pdStarts[$i],$pdEnds[$i],($pdEnds[$i]-$pdStarts[$i]))
    }
}

$md -join "`r`n" | Set-Content "$OutDir\vmr_bfs_reachability.md" -Encoding ascii
Get-Content "$OutDir\vmr_bfs_reachability.md"
