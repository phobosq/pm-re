param(
    [string]$InputPath = 'C:\temp\pm\samples\work\unpacked\PhoenixMiner_6.2c_Windows\PhoenixMiner.exe.bin',
    [string]$CallsitesCsv = 'C:\temp\pm\notes\phoenix_import_callsites_x64.csv',
    [string]$OutCsv = 'C:\temp\pm\notes\vmr_focus_functions.csv',
    [string]$OutMd = 'C:\temp\pm\reports\vmr_focus_functions.md'
)

$ErrorActionPreference = 'Stop'

function Get-U16([byte[]]$b, [int]$o) { [BitConverter]::ToUInt16($b, $o) }
function Get-U32([byte[]]$b, [int]$o) { [BitConverter]::ToUInt32($b, $o) }

function Rva-To-Off([uint32]$rva, $sections) {
    foreach ($s in $sections) {
        $maxSize = [Math]::Max($s.VirtualSize, $s.RawSize)
        if ($rva -ge $s.VirtualAddress -and $rva -lt ($s.VirtualAddress + $maxSize)) {
            return [uint32]($s.RawPtr + ($rva - $s.VirtualAddress))
        }
    }
    return [uint32]0
}

function HexToInt([string]$h) {
    return [Convert]::ToInt32($h.Replace('0x',''), 16)
}

$bytes = [System.IO.File]::ReadAllBytes($InputPath)
$peOff = Get-U32 $bytes 0x3C
if (-not ($bytes[$peOff] -eq 0x50 -and $bytes[$peOff+1] -eq 0x45)) {
    throw 'Invalid PE signature'
}

$sectionCount = Get-U16 $bytes ($peOff + 6)
$optSize = Get-U16 $bytes ($peOff + 20)
$optOff = $peOff + 24
$magic = Get-U16 $bytes $optOff
if ($magic -ne 0x20B) {
    throw 'Expected PE32+ (x64)'
}

$dataDirOff = $optOff + 112
# Exception directory = index 3
$excRva = Get-U32 $bytes ($dataDirOff + 8 * 3)
$excSize = Get-U32 $bytes ($dataDirOff + 8 * 3 + 4)

$secOff = $optOff + $optSize
$sections = @()
for ($i = 0; $i -lt $sectionCount; $i++) {
    $o = $secOff + 40 * $i
    $name = [Text.Encoding]::ASCII.GetString($bytes, $o, 8).Trim([char]0)
    $vsize = Get-U32 $bytes ($o + 8)
    $vaddr = Get-U32 $bytes ($o + 12)
    $rsize = Get-U32 $bytes ($o + 16)
    $rptr = Get-U32 $bytes ($o + 20)
    $sections += [PSCustomObject]@{
        Name = $name
        VirtualSize = $vsize
        VirtualAddress = $vaddr
        RawSize = $rsize
        RawPtr = $rptr
    }
}

$excOff = Rva-To-Off $excRva $sections
if ($excOff -eq 0 -or $excSize -lt 12) {
    throw 'No valid .pdata / exception directory'
}

$funcs = New-Object System.Collections.Generic.List[object]
$entryCount = [int]($excSize / 12)
for ($i = 0; $i -lt $entryCount; $i++) {
    $o = $excOff + 12 * $i
    if (($o + 12) -gt $bytes.Length) { break }
    $begin = Get-U32 $bytes $o
    $end = Get-U32 $bytes ($o + 4)
    $unwind = Get-U32 $bytes ($o + 8)
    if ($begin -eq 0 -and $end -eq 0) { continue }
    if ($end -le $begin) { continue }
    $funcs.Add([PSCustomObject]@{
        begin_rva_u32 = $begin
        end_rva_u32 = $end
        unwind_rva_u32 = $unwind
        begin_rva = ('0x{0:X8}' -f $begin)
        end_rva = ('0x{0:X8}' -f $end)
        size = ($end - $begin)
    }) | Out-Null
}

$funcArr = @($funcs | Sort-Object begin_rva_u32, end_rva_u32)
if ($funcArr.Count -eq 0) {
    throw 'No runtime function entries parsed'
}

$calls = Import-Csv $CallsitesCsv
$focusPattern = '(?i)GetCommandLineA|GetCommandLineW|CompareStringW|CreateFileA|CreateFileW|DeviceIoControl|GetProcAddress|LoadLibraryA|LoadLibraryW|LoadLibraryExA|LoadLibraryExW|CreateServiceA|CreateServiceW|StartServiceA|StartServiceW'
$focusCalls = $calls | Where-Object { $_.import_name -match $focusPattern }

# Map callsite to containing function by linear scan (sufficient for this scale)
$mapped = New-Object System.Collections.Generic.List[object]
foreach ($c in $focusCalls) {
    $rva = HexToInt $c.callsite_rva
    $hit = $null
    foreach ($f in $funcArr) {
        if ($rva -ge $f.begin_rva_u32 -and $rva -lt $f.end_rva_u32) {
            $hit = $f
            break
        }
        if ($f.begin_rva_u32 -gt $rva) { break }
    }

    if ($null -ne $hit) {
        $mapped.Add([PSCustomObject]@{
            function_begin = $hit.begin_rva
            function_end = $hit.end_rva
            function_size = $hit.size
            callsite_rva = $c.callsite_rva
            import_name = $c.import_name
            dll = $c.dll
        }) | Out-Null
    } else {
        $mapped.Add([PSCustomObject]@{
            function_begin = 'unmapped'
            function_end = 'unmapped'
            function_size = 0
            callsite_rva = $c.callsite_rva
            import_name = $c.import_name
            dll = $c.dll
        }) | Out-Null
    }
}

$grouped = $mapped | Group-Object function_begin,function_end,function_size | ForEach-Object {
    $g = $_.Group
    $apiCounts = $g | Group-Object import_name | Sort-Object Count -Descending

    $hasCmd = ($g.import_name -contains 'GetCommandLineA' -or $g.import_name -contains 'GetCommandLineW')
    $hasCmp = ($g.import_name -contains 'CompareStringW')
    $hasDio = ($g.import_name -contains 'DeviceIoControl')
    $hasCf = ($g.import_name -contains 'CreateFileA' -or $g.import_name -contains 'CreateFileW')

    $role = 'unknown'
    if ($hasCmd -and $hasCmp) {
        $role = 'cli_parser_candidate'
    }
    if ($hasDio -and $hasCf) {
        $role = 'transport_wrapper_candidate'
    } elseif ($hasDio) {
        $role = 'ioctl_path_candidate'
    }

    $score = 0
    foreach ($r in $g) {
        switch ($r.import_name) {
            'DeviceIoControl' { $score += 9 }
            'CreateFileA' { $score += 5 }
            'CreateFileW' { $score += 5 }
            'GetCommandLineA' { $score += 7 }
            'GetCommandLineW' { $score += 7 }
            'CompareStringW' { $score += 6 }
            default { if ($r.import_name -match '(?i)GetProcAddress|LoadLibrary') { $score += 2 } }
        }
    }

    [PSCustomObject]@{
        function_begin = ($g[0].function_begin)
        function_end = ($g[0].function_end)
        function_size = ($g[0].function_size)
        callsite_count = $g.Count
        weighted_score = $score
        role_guess = $role
        has_cmdline = $hasCmd
        has_compare = $hasCmp
        has_createfile = $hasCf
        has_deviceiocontrol = $hasDio
        apis = (($apiCounts | Select-Object -First 8 | ForEach-Object { $_.Name + ':' + $_.Count }) -join '; ')
    }
}

$ranked = $grouped | Sort-Object -Property @{Expression='weighted_score';Descending=$true},@{Expression='callsite_count';Descending=$true}
$ranked | Export-Csv -Path $OutCsv -NoTypeInformation -Encoding ascii

$md = @()
$md += '# vmr Focus Functions (.pdata mapped)'
$md += ''
$md += ('input_callsites_focus: ' + $focusCalls.Count)
$md += ('mapped_rows: ' + $mapped.Count)
$md += ('function_groups: ' + $ranked.Count)
$md += ''
$md += 'Top function candidates:'
foreach ($r in ($ranked | Select-Object -First 15)) {
    $md += ('- ' + $r.function_begin + '..' + $r.function_end + ' size=' + $r.function_size + ' score=' + $r.weighted_score + ' role=' + $r.role_guess + ' apis=' + $r.apis)
}
$md += ''
$md += 'Interpretation:'
$md += '- Functions with CreateFile + DeviceIoControl are top transport wrapper candidates.'
$md += '- Functions with GetCommandLine + CompareStringW are top parser candidates.'
$md += '- Keep confidence at strongly_inferred until direct code-flow or runtime evidence.'
$md -join "`r`n" | Set-Content -Path $OutMd -Encoding ascii

Write-Output ('Runtime functions parsed: ' + $funcArr.Count)
Write-Output ('Focus callsites mapped: ' + $mapped.Count)
Write-Output ('Candidate functions: ' + $ranked.Count)
