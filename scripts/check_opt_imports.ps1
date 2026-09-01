param(
    [string]$ImportCsv = 'C:\temp\pm\notes\phoenix_import_callsites_x64.csv',
    [string]$OutDir = 'C:\temp\pm\notes'
)
$ErrorActionPreference = 'Stop'

$imp = Import-Csv $ImportCsv

function Show-Imports([int]$beginRva,[int]$endRva,[string]$label){
    $hits = @($imp | Where-Object {
        $rv=[Convert]::ToInt32($_.callsite_rva.Replace('0x',''),16)
        $rv -ge $beginRva -and $rv -lt $endRva
    })
    Write-Output ('=== ' + $label + ' (0x{0:X8}..0x{1:X8}) — {2} import callsites ===' -f $beginRva,$endRva,$hits.Count)
    foreach($h in $hits | Sort-Object callsite_rva){
        Write-Output ('  ' + $h.callsite_rva + '  ' + $h.dll + '!' + $h.import_name)
    }
}

# 1. Huge option parser candidate
Show-Imports 0x00129A50 0x0012DA40 'BIG_FUNC (option_parser_candidate?)'

# 2. Setter area
Show-Imports 0x003EA2F0 0x003EA380 '0x003EA2F0-area (option setters?)'

# 3. OPT_DISP helper functions called before getters
Show-Imports 0x003B2120 0x003B2170 '0x003B2120 (first helper in OPT_DISP)'
Show-Imports 0x003B2E24 0x003B2F70 '0x003B2E24 (called 2x from OPT_DISP)'
Show-Imports 0x003B2238 0x003B22D2 '0x003B2238 (called 2x from OPT_DISP)'

# 4. Callers via CompareStringW — find ALL CompareStringW callsites, check their functions
Write-Output ''
Write-Output '=== All CompareStringW callsites ==='
$cmpSites = @($imp | Where-Object { $_.import_name -like 'Compare*' -or $_.import_name -like '*String*' })
foreach($s in $cmpSites){ Write-Output ('  ' + $s.callsite_rva + '  ' + $s.dll + '!' + $s.import_name) }
