param(
    [string]$BinPath = 'C:\temp\pm\samples\work\unpacked\PhoenixMiner_6.2c_Windows\PhoenixMiner.exe.bin',
    [string]$OutDir  = 'C:\temp\pm\notes'
)
$ErrorActionPreference = 'Stop'

Add-Type @'
using System;
using System.Collections.Generic;
public class CallerScan2 {
    public static List<long[]> FindCallers(byte[] bytes, int textOff, int textSize, int textVA, int[] targetRVAs) {
        var hits = new List<long[]>();
        for (int i = 0; i < textSize - 5; i++) {
            if (bytes[textOff + i] != 0xE8) continue;
            int disp = BitConverter.ToInt32(bytes, textOff + i + 1);
            long target = (long)(textVA + i + 5) + disp;
            for (int t = 0; t < targetRVAs.Length; t++) {
                if (target == targetRVAs[t]) {
                    hits.Add(new long[] { t, textVA + i });
                    break;
                }
            }
        }
        return hits;
    }
    public static int BsearchPdata(int[] starts, int[] ends, int rva) {
        int lo=0, hi=starts.Length-1;
        while(lo<=hi){ int m=(lo+hi)/2; if(rva<starts[m]) hi=m-1; else if(rva>=ends[m]) lo=m+1; else return m; }
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

# The 3 getter RVAs confirmed from byte analysis
$getterRVAs = [int[]](0x003E16D8, 0x003E16E0, 0x003E16E8)
$getterLabels = @('get_argv_count', 'get_argv_ptr_table', 'get_fallback_buf')

$knownFuncs = @{
    0x001C3A30 = 'DISP01_transport_dispatcher'
    0x001C4010 = 'TR01_transport_wrapper_A'
    0x001C1BB0 = 'TR02_ioctl_cluster_A1'
    0x003E16B0 = 'PR01_parser_cmdline'
    0x003F37E4 = 'ARGT01_tokenizer'
    0x00395CA8 = 'DPRB01_compare_A_caller'
    0x004052CC = 'DPRB04_compare_B_caller'
    0x003F3610 = 'ARGT01_cleanup'
}

Write-Output 'Scanning for getter callers...'
$hits = [CallerScan2]::FindCallers($bytes,$textOff,$textSz,$textVA,$getterRVAs)
Write-Output ('Total getter call sites: ' + $hits.Count)

$rows = @()
foreach($h in $hits){
    $ti=[int]$h[0]; $callerRva=[int]$h[1]
    $fi=[CallerScan2]::BsearchPdata($pdStarts,$pdEnds,$callerRva)
    $funcBegin=''; $funcEnd=''; $funcSize=0; $funcLabel=''
    if($fi -ge 0){
        $funcBegin='0x{0:X8}' -f $pdStarts[$fi]
        $funcEnd  ='0x{0:X8}' -f $pdEnds[$fi]
        $funcSize = $pdEnds[$fi]-$pdStarts[$fi]
        if($knownFuncs.ContainsKey($pdStarts[$fi])){ $funcLabel=$knownFuncs[$pdStarts[$fi]] }
    }
    $rows += [PSCustomObject]@{
        getter_label = $getterLabels[$ti]
        getter_rva   = '0x{0:X8}' -f $getterRVAs[$ti]
        caller_rva   = '0x{0:X8}' -f $callerRva
        func_begin   = $funcBegin
        func_end     = $funcEnd
        func_size    = $funcSize
        func_label   = $funcLabel
    }
}

$rows | Export-Csv "$OutDir\vmr_getter_callers.csv" -NoTypeInformation -Encoding ascii

# Build markdown report
$md = @()
$md += '# argv Getter Function Callers'
$md += '# Getters: 0x003E16D8=get_argv_count  0x003E16E0=get_argv_ptr_table  0x003E16E8=get_fallback_buf'
$md += '# These tiny LEA+RET accessors are called instead of RIP-relative direct access'
$md += '# confidence: confirmed (CALL rel32 exhaustive scan of .text, getter byte patterns verified)'
$md += ''
foreach($lbl in $getterLabels){
    $gRows = @($rows | Where-Object { $_.getter_label -eq $lbl })
    $md += ('## ' + $lbl + ' (' + $gRows.Count + ' callers)')
    foreach($r in $gRows | Sort-Object caller_rva){
        $lbl2=if($r.func_label){'  ['+$r.func_label+']'}else{''}
        $md += ('  <- ' + $r.caller_rva + $lbl2 + '  in ' + $r.func_begin + '..' + $r.func_end + ' size=0x{0:X}' -f [int]$r.func_size)
    }
    $md += ''
}

# Cross-reference: functions that call MULTIPLE getters (option dispatch candidates)
$md += '## Multi-getter callers (option dispatch candidates)'
$funcCallCount = @{}
foreach($r in $rows){
    $key = $r.func_begin
    if(-not $funcCallCount.ContainsKey($key)){ $funcCallCount[$key]=@{count=0;end=$r.func_end;size=$r.func_size;label=$r.func_label;getters=@()} }
    $funcCallCount[$key].count++
    $funcCallCount[$key].getters += $r.getter_label
}
foreach($k in ($funcCallCount.Keys | Sort-Object)){
    $v = $funcCallCount[$k]
    if($v.count -ge 2 -or $v.label -ne ''){
        $getterList = ($v.getters | Sort-Object -Unique) -join ', '
        $lbl2=if($v.label){'  ['+$v.label+']'}else{''}
        $md += ('  func ' + $k + '..' + $v.end + ' size=0x{0:X}' -f [int]$v.size + $lbl2 + '  calls: ' + $getterList + ' ('+$v.count+'x)')
    }
}

$md -join "`r`n" | Set-Content "$OutDir\vmr_getter_callers.md" -Encoding ascii
Get-Content "$OutDir\vmr_getter_callers.md"
