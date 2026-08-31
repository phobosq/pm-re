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

# Find .pdata section
$pdata = $secs | Where-Object { $_.Name -eq '.pdata' } | Select-Object -First 1
if(-not $pdata){ throw 'No .pdata' }

# Parse all RUNTIME_FUNCTION entries (each 12 bytes: begin_rva, end_rva, unwind_rva)
$pdataOff = $pdata.RawPtr
$pdataSize = [int]$pdata.RawSize
$funcCount = [int]($pdataSize / 12)

# Probe RVAs: callers of TR01/TR02 that were in unknown_func
$probeRvas = @(
    [uint32]0x001C3C79,  # caller of TR01 (transport_wrapper_A)
    [uint32]0x001C3CCE,  # caller of TR02 (ioctl_cluster_A1)
    [uint32]0x0028CFFB,  # caller of TR04 (transport_wrapper_B)
    [uint32]0x00395FB0,  # caller of PR02 (parser_compare_A)
    [uint32]0x003B1C94,  # caller of PR02 (parser_compare_A)
    [uint32]0x00405290,  # caller of PR03 (parser_compare_B)
    [uint32]0x00405604   # caller of PR03 (parser_compare_B)
)

$results = @()
for($i=0; $i -lt $funcCount; $i++){
    $off = $pdataOff + 12*$i
    $begRva = Get-U32 $bytes $off
    $endRva = Get-U32 $bytes ($off+4)
    foreach($prv in $probeRvas){
        if($prv -ge $begRva -and $prv -lt $endRva){
            $results += [PSCustomObject]@{
                probe = ('0x{0:X8}' -f $prv)
                func_begin = ('0x{0:X8}' -f $begRva)
                func_end   = ('0x{0:X8}' -f $endRva)
                func_size  = [int]($endRva - $begRva)
            }
        }
    }
}

$md = @()
$md += '# Unknown Caller Functions — PDATA Lookup'
$md += 'Probing which pdata entries contain the caller RVAs identified in vmr_callers.md'
$md += ''
if($results.Count -eq 0){
    $md += '## No pdata entries found for any probed RVAs'
    $md += 'This means the caller functions are either:'
    $md += '  a) Inside the .pdata range but using frames not in .pdata candidates (unlikely at this scale)'
    $md += '  b) Tail calls / indirect dispatches where pdata begin != what we tracked'
    $md += '  c) Located outside pdata coverage (rare for x64 Windows)'
} else {
    $seen = @{}
    foreach($r in $results){
        $key = $r.func_begin + '_' + $r.func_end
        if(-not $seen.ContainsKey($key)){
            $seen[$key] = @()
        }
        $seen[$key] += $r.probe
    }
    foreach($k in $seen.Keys | Sort-Object){
        $r0 = $results | Where-Object { ($_.func_begin + '_' + $_.func_end) -eq $k } | Select-Object -First 1
        $probeList = $seen[$k] -join ', '
        $md += ('## func ' + $r0.func_begin + '..' + $r0.func_end + ' size=0x{0:X}' -f $r0.func_size)
        $md += ('   contains: ' + $probeList)
    }
}
$md += ''
$md += 'confidence: confirmed (pdata exhaustive parse)'

$md -join "`r`n" | Set-Content "$OutDir\vmr_caller_funcs.md" -Encoding ascii
$results | Export-Csv "$OutDir\vmr_caller_funcs.csv" -NoTypeInformation -Encoding ascii
Get-Content "$OutDir\vmr_caller_funcs.md"
Write-Output ('Probe hits: ' + $results.Count)
