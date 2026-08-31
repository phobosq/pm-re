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
    $pdataOff = $pdataSec.RawPtr; $count = [int]($pdataSec.RawSize / 12)
    for($i=0;$i -lt $count;$i++){
        $off=$pdataOff+12*$i; $bR=Get-U32 $bytes $off; $eR=Get-U32 $bytes ($off+4)
        if($rva -ge $bR -and $rva -lt $eR){ return [PSCustomObject]@{begin=('0x{0:X8}' -f $bR);end=('0x{0:X8}' -f $eR);size=[int]($eR-$bR)} }
    }
    return $null
}

function Get-Outbound([uint32]$bRva,[uint32]$eRva){
    $off=Rva-To-Off $bRva; if($off -eq 0){ return @() }
    $size=[int]($eRva-$bRva); $calls=@(); $i=0
    while($i -lt $size-5){
        $b0=$bytes[$off+$i]
        if($b0 -eq 0xE8 -or $b0 -eq 0xE9){
            $instrRva=$bRva+$i; $disp=Get-I32 $bytes ($off+$i+1)
            $sum=[int64]$instrRva+5+$disp
            if($sum -lt 0){ $sum+=0x100000000 }
            $tRva=[uint32]($sum -band 0xFFFFFFFF)
            # filter obviously bogus targets (above 0x00800000 likely outside PE)
            if($tRva -lt 0x00800000){
                $calls+=[PSCustomObject]@{type=if($b0 -eq 0xE8){'CALL'}else{'JMP'};from=('0x{0:X8}' -f $instrRva);to=('0x{0:X8}' -f $tRva)}
            }
            $i+=5; continue
        }
        $i++
    }
    return $calls
}

function Find-Callers-Filtered([uint32]$targetRva){
    $tOff=$textSec.RawPtr; $tSize=[int]$textSec.RawSize; $tVA=$textSec.VirtualAddress; $callers=@()
    for($i=0;$i -lt $tSize-5;$i++){
        if($bytes[$tOff+$i] -ne 0xE8){ continue }
        $disp=Get-I32 $bytes ($tOff+$i+1); $instrRva=[uint32]($tVA+$i)
        $sum=[int64]$instrRva+5+$disp
        if($sum -lt 0){ $sum+=0x100000000 }
        if([uint32]($sum -band 0xFFFFFFFF) -eq $targetRva){ $callers+=[uint32]$instrRva }
    }
    return $callers
}

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
    '0x001C55F0' = 'CALLER_DISP01_thunk'
    '0x001C5640' = 'CALLER_DISP01_main'
}

$md = @()
$md += '# Call Chain: Level 2 Callers (above DISP01)'
$md += ''

# Callers of DISP01's two callers + their imports
$level2_targets = @(
    @{id='CALLER_DISP01_thunk'; begin=[uint32]0x001C55F0; end=[uint32]0x001C563E},
    @{id='CALLER_DISP01_main';  begin=[uint32]0x001C5640; end=[uint32]0x001C5985}
)

foreach($lt in $level2_targets){
    $md += ('## ' + $lt.id + ' ' + ('0x{0:X8}' -f $lt.begin) + '..' + ('0x{0:X8}' -f $lt.end) + ' size=0x{0:X}' -f [int]($lt.end-$lt.begin))
    
    # Outbound
    $out = @(Get-Outbound $lt.begin $lt.end)
    $md += ('  Outbound calls: ' + $out.Count)
    foreach($c in $out){
        $lbl = if($knownFuncs.ContainsKey($c.to)){ ' [' + $knownFuncs[$c.to] + ']' } else { '' }
        $pf = Find-Pdata-Func (HexU32 $c.to)
        $fi = if($pf){ ' (func ' + $pf.begin + '..' + $pf.end + ')' } else { '' }
        $md += ('    ' + $c.type + ' ' + $c.from + ' -> ' + $c.to + $lbl + $fi)
    }
    
    # Callers of this function
    Write-Output ('Scanning callers of ' + $lt.id + '...')
    $callers = @(Find-Callers-Filtered $lt.begin)
    $md += ('  Callers: ' + $callers.Count)
    foreach($cv in $callers){
        $pf = Find-Pdata-Func $cv
        $funcInfo = if($pf){ '  func ' + $pf.begin + '..' + $pf.end + ' size=0x{0:X}' -f $pf.size } else { '  unknown_pdata' }
        $lbl = if($pf -and $knownFuncs.ContainsKey($pf.begin)){ ' [' + $knownFuncs[$pf.begin] + ']' } else { '' }
        $md += ('    <- ' + ('0x{0:X8}' -f $cv) + $lbl + $funcInfo)
    }
    $md += ''
}

# Also trace callers of DPRB01 and DPRB04 to see if they connect to the 0x001C chain
$compareCallerTargets = @(
    @{id='DPRB01'; rva=[uint32]0x00395CA8},
    @{id='DPRB04'; rva=[uint32]0x004052CC}
)

$md += '## Callers of Compare-Caller Functions (do they connect to transport chain?)'
foreach($ct in $compareCallerTargets){
    Write-Output ('Scanning callers of ' + $ct.id + '...')
    $callers = @(Find-Callers-Filtered $ct.rva)
    $md += ('### ' + $ct.id + ' (' + ('0x{0:X8}' -f $ct.rva) + ') — ' + $callers.Count + ' callers')
    foreach($cv in $callers){
        $pf = Find-Pdata-Func $cv
        $funcInfo = if($pf){ 'func ' + $pf.begin + '..' + $pf.end + ' size=0x{0:X}' -f $pf.size } else { 'unknown_pdata' }
        $lbl = if($pf -and $knownFuncs.ContainsKey($pf.begin)){ ' [' + $knownFuncs[$pf.begin] + ']' } else { '' }
        $md += ('  <- ' + ('0x{0:X8}' -f $cv) + $lbl + ' ' + $funcInfo)
    }
    $md += ''
}

$md -join "`r`n" | Set-Content "$OutDir\vmr_level2_chain.md" -Encoding ascii
Get-Content "$OutDir\vmr_level2_chain.md"
