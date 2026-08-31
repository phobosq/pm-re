param(
    [string]$BinPath = 'C:\temp\pm\samples\work\unpacked\PhoenixMiner_6.2c_Windows\PhoenixMiner.exe.bin',
    [string]$PdataCsv = 'C:\temp\pm\notes\vmr_focus_functions.csv',
    [string]$OutDir  = 'C:\temp\pm\notes'
)

$ErrorActionPreference = 'Stop'
function Get-U16([byte[]]$b,[int]$o){ [BitConverter]::ToUInt16($b,$o) }
function Get-U32([byte[]]$b,[int]$o){ [BitConverter]::ToUInt32($b,$o) }
function HexU32([string]$h){ [Convert]::ToUInt32($h.Replace('0x',''),16) }

function Rva-To-Off([uint32]$rva,$secs){
    foreach($s in $secs){
        $maxSz=[Math]::Max($s.VirtualSize,$s.RawSize)
        if($rva -ge $s.VirtualAddress -and $rva -lt ($s.VirtualAddress+$maxSz)){
            return [uint32]($s.RawPtr+($rva-$s.VirtualAddress))
        }
    }
    return [uint32]0
}

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

# Scan the whole .text section for CALL rel32 instructions pointing to one of our targets
# Returns: [caller_rva, target_rva]
$targetRvas = @(
    @{id='TR01'; rva=[uint32]0x001C4010; label='transport_wrapper_A'},
    @{id='TR04'; rva=[uint32]0x0028CA90; label='transport_wrapper_B'},
    @{id='TR02'; rva=[uint32]0x001C1BB0; label='ioctl_cluster_A1'},
    @{id='TR03'; rva=[uint32]0x001C6BB0; label='ioctl_cluster_B'},
    @{id='PR01'; rva=[uint32]0x003E16B0; label='parser_cmdline'},
    @{id='PR02'; rva=[uint32]0x003B160C; label='parser_compare_A'},
    @{id='PR03'; rva=[uint32]0x003F9610; label='parser_compare_B'}
)

Write-Output 'Scanning .text for callers of target functions...'
$tOff = $textSec.RawPtr
$tSize = [int]$textSec.RawSize
$tVA = $textSec.VirtualAddress

$callerRows = @()
for($i=0; $i -lt $tSize-5; $i++){
    $b0 = $bytes[$tOff+$i]
    if($b0 -ne 0xE8){ continue }
    $disp = [BitConverter]::ToInt32($bytes, $tOff+$i+1)
    $instrRva = [uint32]($tVA + $i)
    $sum = [int64]$instrRva + 5 + $disp
    if($sum -lt 0){ $sum += 0x100000000 }
    $targetRva = [uint32]($sum -band 0xFFFFFFFF)
    foreach($t in $targetRvas){
        if($targetRva -eq $t.rva){
            $callerRows += [PSCustomObject]@{
                target_id    = $t.id
                target_label = $t.label
                target_rva   = ('0x{0:X8}' -f $t.rva)
                caller_rva   = ('0x{0:X8}' -f $instrRva)
            }
        }
    }
}

# Now load pdata functions to assign caller_rva to a containing function
$funcs = @(Import-Csv $PdataCsv | Sort-Object -Property @{Expression={[Convert]::ToUInt32($_.function_begin.Replace('0x',''),16)};Descending=$false})

function Find-Func([uint32]$rva){
    foreach($f in $funcs){
        $b = HexU32 $f.function_begin
        $e = HexU32 $f.function_end
        if($rva -ge $b -and $rva -lt $e){ return $f }
    }
    return $null
}

$result = @()
foreach($row in $callerRows){
    $cRva = HexU32 $row.caller_rva
    $cf = Find-Func $cRva
    $result += [PSCustomObject]@{
        target_id          = $row.target_id
        target_label       = $row.target_label
        target_rva         = $row.target_rva
        caller_rva         = $row.caller_rva
        caller_func_begin  = if($cf){ $cf.function_begin } else { '' }
        caller_func_end    = if($cf){ $cf.function_end } else { '' }
        caller_func_role   = if($cf){ $cf.role_guess } else { 'not_in_pdata_candidates' }
        caller_func_score  = if($cf){ $cf.weighted_score } else { '' }
        caller_func_apis   = if($cf){ $cf.apis } else { '' }
    }
}

$result | Export-Csv "$OutDir\vmr_callers.csv" -NoTypeInformation -Encoding ascii
Write-Output ('Total caller edges: ' + $result.Count)

# Print summary grouped by target
$md = @()
$md += '# vmr Callers (Who Calls Our Target Functions)'
$md += 'confidence: strongly_inferred (static CALL rel32 scan of .text)'
$md += ''
foreach($t in $targetRvas){
    $rows = @($result | Where-Object { $_.target_id -eq $t.id })
    $md += ('## ' + $t.id + ' ' + $t.label + ' -> ' + ('0x{0:X8}' -f $t.rva) + ' (' + $rows.Count + ' callers)')
    if($rows.Count -eq 0){
        $md += '  (no CALL rel32 callers found — function may be called only indirectly)'
    }
    foreach($r in ($rows | Select-Object -First 15)){
        $loc = if($r.caller_func_begin){ $r.caller_func_begin + '..' + $r.caller_func_end + ' role=' + $r.caller_func_role } else { 'unknown_func' }
        $md += ('  <- ' + $r.caller_rva + ' in ' + $loc)
    }
    $md += ''
}

$md -join "`r`n" | Set-Content "$OutDir\vmr_callers.md" -Encoding ascii
Get-Content "$OutDir\vmr_callers.md"
