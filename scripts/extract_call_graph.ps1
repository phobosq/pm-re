param(
    [string]$BinPath = 'C:\temp\pm\samples\work\unpacked\PhoenixMiner_6.2c_Windows\PhoenixMiner.exe.bin',
    [string]$PdataCsv = 'C:\temp\pm\notes\vmr_focus_functions.csv',
    [string]$OutDir = 'C:\temp\pm\notes'
)

$ErrorActionPreference = 'Stop'

function Get-U16([byte[]]$b,[int]$o){ [BitConverter]::ToUInt16($b,$o) }
function Get-U32([byte[]]$b,[int]$o){ [BitConverter]::ToUInt32($b,$o) }
function Get-I8([byte[]]$b,[int]$o){ [sbyte]$b[$o] }
function Get-I32([byte[]]$b,[int]$o){ [BitConverter]::ToInt32($b,$o) }

function Rva-To-Off([uint32]$rva,$secs){
    foreach($s in $secs){
        $maxSz=[Math]::Max($s.VirtualSize,$s.RawSize)
        if($rva -ge $s.VirtualAddress -and $rva -lt ($s.VirtualAddress+$maxSz)){
            return [uint32]($s.RawPtr+($rva-$s.VirtualAddress))
        }
    }
    return [uint32]0
}

function HexToU32([string]$h){ [Convert]::ToUInt32($h.Replace('0x',''),16) }

$bytes = [System.IO.File]::ReadAllBytes($BinPath)
$peOff = Get-U32 $bytes 0x3C
$sectionCount = Get-U16 $bytes ($peOff+6)
$optSize = Get-U16 $bytes ($peOff+20)
$optOff = $peOff+24
$magic = Get-U16 $bytes $optOff
if($magic -ne 0x20B){ throw 'Expected PE32+' }
$imageBase = [BitConverter]::ToUInt64($bytes,$optOff+24)

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
if(-not $textSec){ throw 'No .text section' }

# Decode CALL and JMP instructions in a byte range, return target RVAs
function Get-Calls([byte[]]$bytes,[uint32]$beginRva,[uint32]$endRva,$secs){
    $off = Rva-To-Off $beginRva $secs
    if($off -eq 0){ return @() }
    $size = [int]($endRva - $beginRva)
    $calls = @()
    $i = 0
    while($i -lt $size-5){
        $b0 = $bytes[$off+$i]
        if($b0 -eq 0xE8 -or $b0 -eq 0xE9){
            # CALL rel32 or JMP rel32
            $instrRva = $beginRva + $i
            $disp = [BitConverter]::ToInt32($bytes, $off+$i+1)
            $sum = [int64]$instrRva + 5 + $disp
            if($sum -lt 0){ $sum += 0x100000000 }
            $targetRva = [uint32]($sum -band 0xFFFFFFFF)
            $calls += [PSCustomObject]@{
                caller_rva = ('0x{0:X8}' -f $instrRva)
                target_rva = ('0x{0:X8}' -f $targetRva)
                type = if($b0 -eq 0xE8){'CALL'}else{'JMP'}
            }
            $i += 5
            continue
        }
        if($b0 -eq 0xFF){
            $b1 = $bytes[$off+$i+1]
            if(($b1 -band 0x38) -eq 0x10 -or ($b1 -band 0x38) -eq 0x20){
                # CALL/JMP [mem] - log as indirect (cannot resolve statically)
                $instrRva = $beginRva + $i
                $calls += [PSCustomObject]@{
                    caller_rva = ('0x{0:X8}' -f $instrRva)
                    target_rva = 'indirect'
                    type = if(($b1 -band 0x38) -eq 0x10){'CALL_IND'}else{'JMP_IND'}
                }
            }
        }
        $i++
    }
    return $calls
}

# Load function table from pdata CSV
$funcs = Import-Csv $PdataCsv

# Build quick lookup: for each RVA -> function
function Find-Func([uint32]$rva,$funcArr){
    foreach($f in $funcArr){
        $b = HexToU32 $f.function_begin
        $e = HexToU32 $f.function_end
        if($rva -ge $b -and $rva -lt $e){ return $f }
    }
    return $null
}

# Target ranges: transport candidates and parser candidates
$targets = @(
    @{id='TR01'; label='transport_wrapper_A'; begin='0x001C4010'; end='0x001C44E3'},
    @{id='TR04'; label='transport_wrapper_B'; begin='0x0028CA90'; end='0x0028CB6B'},
    @{id='TR02'; label='ioctl_cluster_A1';   begin='0x001C1BB0'; end='0x001C1CE0'},
    @{id='TR03'; label='ioctl_cluster_B';    begin='0x001C6BB0'; end='0x001C6C93'},
    @{id='PR01'; label='parser_cmdline';     begin='0x003E16B0'; end='0x003E16D5'},
    @{id='PR02'; label='parser_compare_A';   begin='0x003B160C'; end='0x003B16C8'},
    @{id='PR03'; label='parser_compare_B';   begin='0x003F9610'; end='0x003F96FF'}
)

$allRows = @()
$funcArr = @($funcs | Sort-Object -Property @{Expression={[Convert]::ToUInt32($_.function_begin.Replace('0x',''),16)};Descending=$false})

foreach($t in $targets){
    $bRva = HexToU32 $t.begin
    $eRva = HexToU32 $t.end
    $calls = @(Get-Calls $bytes $bRva $eRva $secs)
    foreach($c in $calls){
        # Resolve target to known function if possible
        $tgtF = $null
        if($c.target_rva -ne 'indirect'){
            $tRva = HexToU32 $c.target_rva
            $tgtF = Find-Func $tRva $funcArr
        }
        $allRows += [PSCustomObject]@{
            range_id    = $t.id
            range_label = $t.label
            range_begin = $t.begin
            range_end   = $t.end
            caller_rva  = $c.caller_rva
            target_rva  = $c.target_rva
            type        = $c.type
            target_func_begin = if($tgtF){ $tgtF.function_begin } else { '' }
            target_func_end   = if($tgtF){ $tgtF.function_end }   else { '' }
            target_func_role  = if($tgtF){ $tgtF.role_guess }     else { '' }
            target_func_score = if($tgtF){ $tgtF.weighted_score } else { '' }
            target_func_apis  = if($tgtF){ $tgtF.apis }           else { '' }
        }
    }
}

$allRows | Export-Csv "$OutDir\vmr_call_graph.csv" -NoTypeInformation -Encoding ascii

# Build call-graph summary markdown
$md = @()
$md += '# vmr Static Call Graph (Selected Ranges)'
$md += ''
foreach($t in $targets){
    $rows = @($allRows | Where-Object { $_.range_id -eq $t.id })
    $md += ('## ' + $t.id + ' ' + $t.label + ' ' + $t.begin + '..' + $t.end + ' (' + $rows.Count + ' edges)')
    $dirCalls  = @($rows | Where-Object { $_.type -eq 'CALL' })
    $dirJmps   = @($rows | Where-Object { $_.type -eq 'JMP' })
    $indCalls  = @($rows | Where-Object { $_.type -eq 'CALL_IND' })
    $md += ('  direct CALL: ' + $dirCalls.Count + '  direct JMP: ' + $dirJmps.Count + '  indirect: ' + $indCalls.Count)
    foreach($r in ($dirCalls | Select-Object -First 20)){
        $tinfo = if($r.target_func_begin){ ' -> func ' + $r.target_func_begin + '..' + $r.target_func_end + ' role=' + $r.target_func_role } else { '' }
        $md += ('  CALL ' + $r.caller_rva + ' -> ' + $r.target_rva + $tinfo)
    }
    foreach($r in ($dirJmps | Select-Object -First 8)){
        $tinfo = if($r.target_func_begin){ ' -> func ' + $r.target_func_begin + '..' + $r.target_func_end + ' role=' + $r.target_func_role } else { '' }
        $md += ('  JMP  ' + $r.caller_rva + ' -> ' + $r.target_rva + $tinfo)
    }
    if($indCalls.Count -gt 0){
        $md += ('  CALL_IND: ' + $indCalls.Count + ' indirect dispatch(es)')
    }
    $md += ''
}

$md += 'Interpretation:'
$md += '- Direct CALL edges within this set indicate callee relationships.'
$md += '- Calls INTO known transport/ioctl functions from parser or compare ranges would link parser -> transport.'
$md += '- confidence: strongly_inferred (static only; no runtime confirmation)'
$md -join "`r`n" | Set-Content "$OutDir\vmr_call_graph.md" -Encoding ascii

Write-Output ('Total edges: ' + $allRows.Count)
Write-Output ('Targets covered: ' + $targets.Count)
