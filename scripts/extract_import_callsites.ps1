param(
    [string]$InputPath = 'C:\temp\pm\samples\work\unpacked\PhoenixMiner_6.2c_Windows\PhoenixMiner.exe.bin',
    [string]$OutCsv = 'C:\temp\pm\notes\phoenix_import_callsites_x64.csv',
    [string]$OutHighValueCsv = 'C:\temp\pm\notes\phoenix_import_callsites_high_value.csv'
)

$ErrorActionPreference = 'Stop'

function Get-U16([byte[]]$b, [int]$o) { return [BitConverter]::ToUInt16($b, $o) }
function Get-U32([byte[]]$b, [int]$o) { return [BitConverter]::ToUInt32($b, $o) }
function Get-U64([byte[]]$b, [int]$o) { return [BitConverter]::ToUInt64($b, $o) }
function Get-I32([byte[]]$b, [int]$o) { return [BitConverter]::ToInt32($b, $o) }

function Read-CString([byte[]]$bytes, [int]$offset) {
    if ($offset -lt 0 -or $offset -ge $bytes.Length) { return '' }
    $acc = New-Object System.Collections.Generic.List[byte]
    for ($i = $offset; $i -lt $bytes.Length; $i++) {
        if ($bytes[$i] -eq 0) { break }
        $acc.Add($bytes[$i]) | Out-Null
    }
    return [Text.Encoding]::ASCII.GetString($acc.ToArray())
}

function Rva-To-Off([uint32]$rva, $sections) {
    foreach ($s in $sections) {
        $maxSize = [Math]::Max($s.VirtualSize, $s.RawSize)
        if ($rva -ge $s.VirtualAddress -and $rva -lt ($s.VirtualAddress + $maxSize)) {
            return [uint32]($s.RawPtr + ($rva - $s.VirtualAddress))
        }
    }
    return [uint32]0
}

$bytes = [System.IO.File]::ReadAllBytes($InputPath)
$peOff = Get-U32 $bytes 0x3C
if (-not ($bytes[$peOff] -eq 0x50 -and $bytes[$peOff+1] -eq 0x45)) {
    throw 'Not a PE file'
}

$machine = Get-U16 $bytes ($peOff + 4)
$sectionCount = Get-U16 $bytes ($peOff + 6)
$optSize = Get-U16 $bytes ($peOff + 20)
$optOff = $peOff + 24
$magic = Get-U16 $bytes $optOff
if ($magic -ne 0x20B) {
    throw 'Script expects PE32+ (x64) input'
}

$imageBase = Get-U64 $bytes ($optOff + 24)
$entryRva = Get-U32 $bytes ($optOff + 16)
$dataDirOff = $optOff + 112
$importRva = Get-U32 $bytes ($dataDirOff + 8)

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

$importOff = Rva-To-Off $importRva $sections
if ($importOff -eq 0) {
    throw 'No import table found'
}

$imports = New-Object System.Collections.Generic.List[object]
for ($d = 0; $d -lt 4096; $d++) {
    $descOff = $importOff + 20 * $d
    if (($descOff + 20) -gt $bytes.Length) { break }

    $origFirstThunk = Get-U32 $bytes ($descOff + 0)
    $nameRva = Get-U32 $bytes ($descOff + 12)
    $firstThunk = Get-U32 $bytes ($descOff + 16)

    if ($origFirstThunk -eq 0 -and $nameRva -eq 0 -and $firstThunk -eq 0) {
        break
    }

    $nameOff = Rva-To-Off $nameRva $sections
    $dllName = Read-CString $bytes $nameOff

    $lookupRva = if ($origFirstThunk -ne 0) { $origFirstThunk } else { $firstThunk }
    $lookupOff = Rva-To-Off $lookupRva $sections
    $thunkOff = Rva-To-Off $firstThunk $sections
    if ($lookupOff -eq 0 -or $thunkOff -eq 0) { continue }

    for ($i = 0; $i -lt 20000; $i++) {
        $lo = $lookupOff + 8 * $i
        $to = $thunkOff + 8 * $i
        if (($lo + 8) -gt $bytes.Length -or ($to + 8) -gt $bytes.Length) { break }

        $lookupVal = Get-U64 $bytes $lo
        if ($lookupVal -eq 0) { break }

        $isOrdinal = (($lookupVal -band 0x8000000000000000) -ne 0)
        $importName = ''
        if ($isOrdinal) {
            $ord = [int]($lookupVal -band 0xFFFF)
            $importName = 'ORDINAL_' + $ord
        } else {
            $hintNameRva = [uint32]$lookupVal
            $hintNameOff = Rva-To-Off $hintNameRva $sections
            if ($hintNameOff -gt 0 -and ($hintNameOff + 2) -lt $bytes.Length) {
                $importName = Read-CString $bytes ($hintNameOff + 2)
            }
        }

        $thunkRva = [uint32]($firstThunk + 8 * $i)
        $thunkVa = [uint64]($imageBase + $thunkRva)

        $imports.Add([PSCustomObject]@{
            dll = $dllName
            import_name = $importName
            thunk_rva = ('0x{0:X8}' -f $thunkRva)
            thunk_rva_u32 = $thunkRva
            thunk_va = ('0x{0:X16}' -f $thunkVa)
        }) | Out-Null
    }
}

$importByThunk = @{}
foreach ($imp in $imports) {
    $importByThunk[[string]$imp.thunk_rva_u32] = $imp
}

$text = $sections | Where-Object { $_.Name -eq '.text' } | Select-Object -First 1
if (-not $text) { throw 'No .text section' }

$callsites = New-Object System.Collections.Generic.List[object]
$start = [int]$text.RawPtr
$end = [int]($text.RawPtr + $text.RawSize - 6)
for ($o = $start; $o -le $end; $o++) {
    if ($bytes[$o] -eq 0xFF -and $bytes[$o + 1] -eq 0x15) {
        $disp = Get-I32 $bytes ($o + 2)
        $instrRva = [uint32]($text.VirtualAddress + ($o - $text.RawPtr))
        $nextRva = [uint32]($instrRva + 6)
        $sum = [int64]$nextRva + [int64]$disp
        if ($sum -lt 0) { $sum += 0x100000000 }
        $memRva = [uint32]($sum -band 0xFFFFFFFF)

        $key = [string]$memRva
        if ($importByThunk.ContainsKey($key)) {
            $imp = $importByThunk[$key]
            $callsites.Add([PSCustomObject]@{
                callsite_rva = ('0x{0:X8}' -f $instrRva)
                iat_mem_rva = ('0x{0:X8}' -f $memRva)
                dll = $imp.dll
                import_name = $imp.import_name
            }) | Out-Null
        }
    }
}

$uniq = $callsites | Sort-Object callsite_rva,dll,import_name -Unique
$uniq | Export-Csv -Path $OutCsv -NoTypeInformation -Encoding ascii

$highPattern = '(?i)GetCommandLineA|GetCommandLineW|CompareStringW|CreateFileA|CreateFileW|DeviceIoControl|GetProcAddress|LoadLibraryA|LoadLibraryW|LoadLibraryExA|LoadLibraryExW|CreateServiceA|CreateServiceW|StartServiceA|StartServiceW'
$high = $uniq | Where-Object { $_.import_name -match $highPattern }
$high | Export-Csv -Path $OutHighValueCsv -NoTypeInformation -Encoding ascii

Write-Output ('Input: ' + $InputPath)
Write-Output ('Machine: 0x{0:X4}' -f $machine)
Write-Output ('EntryRva: 0x{0:X8}' -f $entryRva)
Write-Output ('Imports parsed: ' + ($imports.Count))
Write-Output ('Import callsites found: ' + ($uniq.Count))
Write-Output ('High-value callsites: ' + ($high.Count))
