param(
    [string]$BinPath = 'C:\temp\pm\samples\work\unpacked\PhoenixMiner_6.2c_Windows\PhoenixMiner.exe.bin',
    [string]$ImportCsv = 'C:\temp\pm\notes\phoenix_import_callsites_high_value.csv',
    [string]$OutDir = 'C:\temp\pm\notes'
)
$ErrorActionPreference = 'Stop'
function Get-U16([byte[]]$b,[int]$o){ [BitConverter]::ToUInt16($b,$o) }
function Get-U32([byte[]]$b,[int]$o){ [BitConverter]::ToUInt32($b,$o) }
function Get-I32([byte[]]$b,[int]$o){ [BitConverter]::ToInt32($b,$o) }
function HexU32([string]$h){ [Convert]::ToUInt32($h.Replace('0x',''),16) }

# New functions discovered
$newFuncs = @(
    @{id='DISP01'; label='transport_dispatcher_AB'; begin='0x001C3A30'; end='0x001C400E'; size=0x5DE},
    @{id='DISP04B'; label='transport_dispatcher_B'; begin='0x0028CF90'; end='0x0028D054'; size=0xC4},
    @{id='DPRB01'; label='compare_A_caller_L'; begin='0x00395CA8'; end='0x00396008'; size=0x360},
    @{id='DPRB02'; label='compare_A_caller_S'; begin='0x003B1C28'; end='0x003B1CCD'; size=0xA5},
    @{id='DPRB03'; label='compare_B_caller_S'; begin='0x0040520C'; end='0x004052C9'; size=0xBD},
    @{id='DPRB04'; label='compare_B_caller_L'; begin='0x004052CC'; end='0x0040565E'; size=0x392}
)

# Load import callsites to find which functions appear inside our new ranges
$imports = @(Import-Csv $ImportCsv)

$md = @()
$md += '# Dispatch/Caller Function Analysis'
$md += 'confidence: strongly_inferred (static analysis)'
$md += ''

foreach($f in $newFuncs){
    $bRva = HexU32 $f.begin
    $eRva = HexU32 $f.end
    $hits = @($imports | Where-Object {
        $rv = HexU32 $_.callsite_rva
        $rv -ge $bRva -and $rv -lt $eRva
    })
    $md += ('## ' + $f.id + ' ' + $f.label)
    $md += ('   range: ' + $f.begin + '..' + $f.end + ' size=0x{0:X}' -f $f.size)
    $md += ('   import callsites inside: ' + $hits.Count)
    if($hits.Count -gt 0){
        foreach($h in $hits | Sort-Object callsite_rva){
            $md += ('   ' + $h.callsite_rva + ' -> ' + $h.dll + '!' + $h.function)
        }
    } else {
        $md += '   (no import callsites from high-value list — relies on internal calls only)'
    }
    $md += ''
}

# Build import lookup for DISP01 specifically (all imports, not just high-value)
$allImports = @(Import-Csv 'C:\temp\pm\notes\phoenix_import_callsites_x64.csv')
$disp01b = HexU32 '0x001C3A30'
$disp01e = HexU32 '0x001C400E'
$disp01Imports = @($allImports | Where-Object {
    $rv = HexU32 $_.callsite_rva
    $rv -ge $disp01b -and $rv -lt $disp01e
})
$md += '## DISP01 Full Import Callsites (all imports, not just high-value)'
$md += ('   count: ' + $disp01Imports.Count)
foreach($h in $disp01Imports | Sort-Object callsite_rva){
    $md += ('   ' + $h.callsite_rva + ' -> ' + $h.dll + '!' + $h.function)
}
$md += ''
$md += 'Evidence classification:'
$md += '  - If DISP01 contains CompareString*/GetCommandLine: parser+transport in one function -> confirmed_bridge'
$md += '  - If DISP01 has only transport APIs: dispatcher is below parser -> need higher caller'
$md += '  - If compare_B_callers share any RVA ranges with transport callers: cross-link found'

$md -join "`r`n" | Set-Content "$OutDir\vmr_dispatch_analysis.md" -Encoding ascii
Get-Content "$OutDir\vmr_dispatch_analysis.md"
