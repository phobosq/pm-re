param(
    [string]$BinPath = 'C:\temp\pm\samples\work\unpacked\PhoenixMiner_6.2c_Windows\PhoenixMiner.exe.bin',
    [string]$OutDir  = 'C:\temp\pm\notes'
)
$ErrorActionPreference = 'Stop'

Add-Type @'
using System; using System.Collections.Generic;
public class UpTrace {
    public static List<int> FindCallers(byte[] bytes, int textOff, int textSize, int textVA, int targetRVA) {
        var callers = new List<int>();
        for (int i = 0; i < textSize - 5; i++) {
            if (bytes[textOff + i] != 0xE8) continue;
            int disp = BitConverter.ToInt32(bytes, textOff + i + 1);
            long tgt = (long)(textVA + i + 5) + disp;
            if ((int)(tgt & 0xFFFFFFFFL) == targetRVA) callers.Add(textVA + i);
        }
        return callers;
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

function Resolve-Func([int]$rva){
    $fi=[UpTrace]::Bsearch($pdStarts,$pdEnds,$rva)
    if($fi -ge 0){ return [PSCustomObject]@{begin=$pdStarts[$fi];end=$pdEnds[$fi];size=$pdEnds[$fi]-$pdStarts[$fi]} }
    return $null
}

# Trace callers up to 4 levels
function Trace-Up([int]$startRva,[string]$label,[int]$maxDepth){
    $current = @($startRva)
    $seen = [System.Collections.Generic.HashSet[int]]::new()
    Write-Output ('=== Upward trace from ' + $label + ' (0x{0:X8}) ===' -f $startRva)
    for($depth=0; $depth -lt $maxDepth; $depth++){
        $next = @()
        foreach($rva in $current){
            if($seen.Contains($rva)){ continue }
            [void]$seen.Add($rva)
            $callers = @([UpTrace]::FindCallers($bytes,$textOff,$textSz,$textVA,$rva))
            Write-Output ('  depth ' + $depth + ': 0x{0:X8} has {1} CALL rel32 callers' -f $rva,$callers.Count)
            foreach($c in $callers){
                $f = Resolve-Func $c
                $fi=''; if($f){ $fi = 'in_func 0x{0:X8}..0x{1:X8} size=0x{2:X}' -f $f.begin,$f.end,$f.size }
                Write-Output ('    <- 0x{0:X8}  {1}' -f $c,$fi)
                if($f){ $next += [int]$f.begin }
            }
        }
        if($next.Count -eq 0){ Write-Output ('  (no more CALL rel32 callers at depth ' + ($depth+1) + ')'); break }
        $current = @($next | Sort-Object -Unique)
    }
    Write-Output ''
}

Trace-Up 0x003B160C 'PR02_compare_A' 4
Trace-Up 0x003F9610 'PR03_compare_B' 4
Trace-Up 0x00395CA8 'DPRB01_compare_A_caller' 4
