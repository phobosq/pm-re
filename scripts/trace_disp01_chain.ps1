param(
    [string]$BinPath = 'C:\temp\pm\samples\work\unpacked\PhoenixMiner_6.2c_Windows\PhoenixMiner.exe.bin',
    [string]$OutDir = 'C:\temp\pm\notes'
)
$ErrorActionPreference = 'Stop'
function Get-U16([byte[]]$b,[int]$o){ [BitConverter]::ToUInt16($b,$o) }
function Get-U32([byte[]]$b,[int]$o){ [BitConverter]::ToUInt32($b,$o) }
function Get-I32([byte[]]$b,[int]$o){ [BitConverter]::ToInt32($b,$o) }
function HexU32([string]$h){ [Convert]::ToUInt32($h.Replace('0x',''),16) }

$bytes = [System.IO.File]::ReadAllBytes($BinPath)
$peOff = Get-U32 $bytes 0x3C
$sectionCount = Get-U16 $bytes ($peOff+6)
$optSize = Get-U16 $bytes ($peOff+20)
$optOff = $peOff+24
$secOff = $optOff+$optSize
$secs = @()
for($i=0;$i -lt $sectionCount;$i++){
    $o=$secOff+40*$i
    $n=[Text.Encoding]::ASCII.GetString($bytes,$o,8).Trim([char]0)
    $vs=Get-U32 $bytes ($o+8); $va=Get-U32 $bytes ($o+12)
    $rs=Get-U32 $bytes ($o+16); $rp=Get-U32 $bytes ($o+20)
    $secs += [PSCustomObject]@{Name=$n;VirtualSize=$vs;VirtualAddress=$va;RawSize=$rs;RawPtr=$rp}
}
$textSec = $secs | Where-Object { $_.Name -eq '.text' } | Select-Object -First 1
$pdataSec = $secs | Where-Object { $_.Name -eq '.pdata' } | Select-Object -First 1

function Rva-To-Off([uint32]$rva){
    foreach($s in $secs){
        $maxSz=[Math]::Max($s.VirtualSize,$s.RawSize)
        if($rva -ge $s.VirtualAddress -and $rva -lt ($s.VirtualAddress+$maxSz)){
            return [uint32]($s.RawPtr+($rva-$s.VirtualAddress))
        }
    }
    return [uint32]0
}

function Find-Pdata-Func([uint32]$rva){
    $pdataOff = $pdataSec.RawPtr
    $count = [int]($pdataSec.RawSize / 12)
    for($i=0;$i -lt $count;$i++){
        $off = $pdataOff + 12*$i
        $bRva = Get-U32 $bytes $off
        $eRva = Get-U32 $bytes ($off+4)
        if($rva -ge $bRva -and $rva -lt $eRva){
            return [PSCustomObject]@{begin=('0x{0:X8}' -f $bRva); end=('0x{0:X8}' -f $eRva); size=[int]($eRva-$bRva)}
        }
    }
    return $null
}

# Get outbound calls from a function range
function Get-Outbound([uint32]$beginRva,[uint32]$endRva){
    $off = Rva-To-Off $beginRva
    if($off -eq 0){ return @() }
    $size = [int]($endRva - $beginRva)
    $calls = @()
    $i=0
    while($i -lt $size-5){
        $b0 = $bytes[$off+$i]
        if($b0 -eq 0xE8 -or $b0 -eq 0xE9){
            $instrRva = $beginRva + $i
            $disp = Get-I32 $bytes ($off+$i+1)
            $sum = [int64]$instrRva + 5 + $disp
            if($sum -lt 0){ $sum += 0x100000000 }
            $targetRva = [uint32]($sum -band 0xFFFFFFFF)
            $calls += [PSCustomObject]@{type=if($b0 -eq 0xE8){'CALL'}else{'JMP'};from=('0x{0:X8}' -f $instrRva);to=('0x{0:X8}' -f $targetRva)}
            $i+=5; continue
        }
        $i++
    }
    return $calls
}

# Scan .text for callers of a given RVA
function Find-Callers([uint32]$targetRva){
    $tOff = $textSec.RawPtr
    $tSize = [int]$textSec.RawSize
    $tVA = $textSec.VirtualAddress
    $callers = @()
    for($i=0; $i -lt $tSize-5; $i++){
        if($bytes[$tOff+$i] -ne 0xE8){ continue }
        $disp = Get-I32 $bytes ($tOff+$i+1)
        $instrRva = [uint32]($tVA + $i)
        $sum = [int64]$instrRva + 5 + $disp
        if($sum -lt 0){ $sum += 0x100000000 }
        if([uint32]($sum -band 0xFFFFFFFF) -eq $targetRva){
            $callers += [uint32]$instrRva
        }
    }
    return $callers
}

# Known function set with labels for cross-reference
$knownFuncs = @{
    '0x001C4010' = 'TR01_transport_wrapper_A'
    '0x0028CA90' = 'TR04_transport_wrapper_B'
    '0x001C1BB0' = 'TR02_ioctl_cluster_A1'
    '0x001C6BB0' = 'TR03_ioctl_cluster_B'
    '0x003E16B0' = 'PR01_parser_cmdline'
    '0x003B160C' = 'PR02_parser_compare_A'
    '0x003F9610' = 'PR03_parser_compare_B'
    '0x001C3A30' = 'DISP01_transport_dispatcher_AB'
    '0x0028CF90' = 'DISP04B_transport_dispatcher_B'
    '0x00395CA8' = 'DPRB01_compare_A_caller_L'
    '0x003B1C28' = 'DPRB02_compare_A_caller_S'
    '0x0040520C' = 'DPRB03_compare_B_caller_S'
    '0x004052CC' = 'DPRB04_compare_B_caller_L'
}

function Label-Func([string]$rvaHex){
    $r = $rvaHex.ToUpper()
    if($knownFuncs.ContainsKey($rvaHex)){ return $knownFuncs[$rvaHex] }
    return ''
}

$md = @()
$md += '# DISP01 Deep Dive and Caller Chain'
$md += ''

# 1. Outbound calls from DISP01
$disp01_begin = [uint32]0x001C3A30
$disp01_end   = [uint32]0x001C400E
$outbound = @(Get-Outbound $disp01_begin $disp01_end)
$md += ('## DISP01 Outbound Calls/Jmps (' + $outbound.Count + ' total)')
foreach($c in $outbound){
    $pf = Find-Pdata-Func (HexU32 $c.to)
    $label = Label-Func $c.to
    $funcInfo = if($pf){ 'in_func ' + $pf.begin + '..' + $pf.end + ' size=0x{0:X}' -f $pf.size } else { 'unknown_pdata' }
    $labelPart = if($label){ ' [' + $label + ']' } else { '' }
    $md += ('  ' + $c.type + ' ' + $c.from + ' -> ' + $c.to + $labelPart + '  (' + $funcInfo + ')')
}
$md += ''

# 2. Callers of DISP01 (0x001C3A30)
Write-Output 'Scanning for callers of DISP01...'
$callers_disp01 = @(Find-Callers $disp01_begin)
$md += ('## Callers of DISP01 (0x001C3A30) — ' + $callers_disp01.Count + ' found')
foreach($cv in $callers_disp01){
    $pf = Find-Pdata-Func $cv
    $funcInfo = if($pf){ 'in_func ' + $pf.begin + '..' + $pf.end + ' size=0x{0:X}' -f $pf.size } else { 'unknown_pdata' }
    $label = if($pf){ Label-Func $pf.begin } else { '' }
    $labelPart = if($label){ ' [' + $label + ']' } else { '' }
    $md += ('  <- ' + ('0x{0:X8}' -f $cv) + $labelPart + '  (' + $funcInfo + ')')
}
$md += ''

# 3. Outbound calls from compare callers to check cross-range links
$compareCallers = @(
    @{id='DPRB01'; begin=[uint32]0x00395CA8; end=[uint32]0x00396008},
    @{id='DPRB04'; begin=[uint32]0x004052CC; end=[uint32]0x0040565E}
)
foreach($cc in $compareCallers){
    $outb = @(Get-Outbound $cc.begin $cc.end)
    $md += ('## ' + $cc.id + ' Outbound Calls (' + $outb.Count + ' total)')
    foreach($c in $outb){
        $label = Label-Func $c.to
        $pf = Find-Pdata-Func (HexU32 $c.to)
        $funcInfo = if($pf){ 'in_func ' + $pf.begin + '..' + $pf.end } else { 'unknown_pdata' }
        $labelPart = if($label){ ' [' + $label + ']' } else { '' }
        $md += ('  ' + $c.type + ' ' + $c.from + ' -> ' + $c.to + $labelPart + '  (' + $funcInfo + ')')
    }
    $md += ''
}

$md -join "`r`n" | Set-Content "$OutDir\vmr_disp01_chain.md" -Encoding ascii
Get-Content "$OutDir\vmr_disp01_chain.md"
