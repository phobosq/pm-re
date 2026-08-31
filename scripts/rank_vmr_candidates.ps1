param(
    [string]$CallsCsv = 'C:\temp\pm\notes\phoenix_import_callsites_x64.csv',
    [string]$OutCsv = 'C:\temp\pm\notes\vmr_candidate_blocks.csv',
    [string]$OutMd = 'C:\temp\pm\reports\vmr_candidate_blocks.md',
    [int]$Window = 0x1000
)

$ErrorActionPreference = 'Stop'

function HexToInt([string]$h) {
    return [Convert]::ToInt32($h.Replace('0x',''),16)
}

function IntToHex([int]$v) {
    return ('0x{0:X8}' -f $v)
}

$rows = Import-Csv $CallsCsv
if (-not $rows -or $rows.Count -eq 0) {
    throw 'No callsite rows found'
}

# API weights favor vmr path discovery: parser anchors and transport anchors.
$weights = @{
    'GetCommandLineA' = 7
    'GetCommandLineW' = 7
    'CompareStringW' = 6
    'CreateFileA' = 5
    'CreateFileW' = 5
    'DeviceIoControl' = 9
    'GetProcAddress' = 3
    'LoadLibraryA' = 2
    'LoadLibraryW' = 2
    'LoadLibraryExA' = 2
    'LoadLibraryExW' = 2
    'CreateServiceA' = 4
    'CreateServiceW' = 4
    'StartServiceA' = 4
    'StartServiceW' = 4
}

$high = $rows | Where-Object { $weights.ContainsKey($_.import_name) }
$enriched = $high | ForEach-Object {
    [PSCustomObject]@{
        rva_hex = $_.callsite_rva
        rva = HexToInt $_.callsite_rva
        import_name = $_.import_name
        dll = $_.dll
        weight = $weights[$_.import_name]
    }
} | Sort-Object rva

$blocks = @()
if ($enriched.Count -gt 0) {
    $start = $enriched[0].rva
    $end = $start
    $items = @($enriched[0])

    for ($i = 1; $i -lt $enriched.Count; $i++) {
        $r = $enriched[$i]
        if (($r.rva - $end) -le $Window) {
            $items += $r
            $end = $r.rva
        } else {
            $blocks += [PSCustomObject]@{ start=$start; end=$end; items=@($items) }
            $start = $r.rva
            $end = $r.rva
            $items = @($r)
        }
    }
    $blocks += [PSCustomObject]@{ start=$start; end=$end; items=@($items) }
}

$out = New-Object System.Collections.Generic.List[object]
$idx = 1
foreach ($b in $blocks) {
    $arr = @($b.items)
    $score = ($arr | Measure-Object -Property weight -Sum).Sum
    $count = $arr.Count
    $apis = $arr | Group-Object import_name | Sort-Object Count -Descending

    $hasCmd = ($arr.import_name -contains 'GetCommandLineA' -or $arr.import_name -contains 'GetCommandLineW')
    $hasCmp = ($arr.import_name -contains 'CompareStringW')
    $hasDio = ($arr.import_name -contains 'DeviceIoControl')
    $hasCf = ($arr.import_name -contains 'CreateFileA' -or $arr.import_name -contains 'CreateFileW')

    $role = 'unknown'
    if ($hasDio -and $hasCf) {
        $role = 'transport_wrapper_candidate'
    } elseif ($hasCmd -and $hasCmp) {
        $role = 'cli_parser_candidate'
    } elseif ($hasCmd) {
        $role = 'cli_entry_candidate'
    } elseif ($hasDio) {
        $role = 'ioctl_path_candidate'
    }

    # boost if both parser and transport anchors appear in one block
    if (($hasCmd -or $hasCmp) -and $hasDio) {
        $score += 10
    }

    $out.Add([PSCustomObject]@{
        block_id = ('B{0:D3}' -f $idx)
        start_rva = IntToHex $b.start
        end_rva = IntToHex $b.end
        span_bytes = ($b.end - $b.start)
        callsite_count = $count
        weighted_score = $score
        role_guess = $role
        has_cmdline = $hasCmd
        has_compare = $hasCmp
        has_createfile = $hasCf
        has_deviceiocontrol = $hasDio
        top_apis = (($apis | Select-Object -First 6 | ForEach-Object { $_.Name + ':' + $_.Count }) -join '; ')
    }) | Out-Null

    $idx++
}

$ranked = $out | Sort-Object -Property @{Expression='weighted_score';Descending=$true},@{Expression='callsite_count';Descending=$true}
$ranked | Export-Csv -Path $OutCsv -NoTypeInformation -Encoding ascii

$md = @()
$md += '# vmr Candidate Blocks (Static Heuristic)'
$md += ''
$md += ('window_bytes: 0x{0:X}' -f $Window)
$md += ('input_rows: ' + $rows.Count)
$md += ('high_value_rows: ' + $enriched.Count)
$md += ('blocks: ' + $ranked.Count)
$md += ''
$md += 'Top blocks:'
foreach ($r in ($ranked | Select-Object -First 12)) {
    $md += ('- ' + $r.block_id + ' ' + $r.start_rva + '..' + $r.end_rva + ' score=' + $r.weighted_score + ' role=' + $r.role_guess + ' apis=' + $r.top_apis)
}
$md += ''
$md += 'Interpretation:'
$md += '- Prioritize blocks with DeviceIoControl + CreateFile for vmr transport path.'
$md += '- Prioritize blocks with GetCommandLine + CompareStringW for vmr parser path.'
$md += '- Treat this ranking as strongly_inferred until direct code-flow confirmation.'
$md -join "`r`n" | Set-Content -Path $OutMd -Encoding ascii

Write-Output ('Ranked blocks: ' + $ranked.Count)
Write-Output ('Top block: ' + ($ranked | Select-Object -First 1 -ExpandProperty block_id))
