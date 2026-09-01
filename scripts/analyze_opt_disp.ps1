param(
    [string]$BinPath = 'C:\temp\pm\samples\work\unpacked\PhoenixMiner_6.2c_Windows\PhoenixMiner.exe.bin',
    [string]$ImportCsv = 'C:\temp\pm\notes\phoenix_import_callsites_x64.csv',
    [string]$OutDir  = 'C:\temp\pm\notes'
)
$ErrorActionPreference = 'Stop'

Add-Type @'
using System; using System.Collections.Generic;
public class Scan3 {
    public static List<long[]> FindCallers(byte[] bytes, int textOff, int textSize, int textVA, int[] targetRVAs) {
        var hits = new List<long[]>();
        for (int i = 0; i < textSize - 5; i++) {
            if (bytes[textOff + i] != 0xE8) continue;
            int disp = BitConverter.ToInt32(bytes, textOff + i + 1);
            long target = (long)(textVA + i + 5) + disp;
            for (int t = 0; t < targetRVAs.Length; t++) {
                if (target == targetRVAs[t]) { hits.Add(new long[] { t, textVA + i }); break; }
            }
        }
        return hits;
    }
    public static int Bsearch(int[] starts, int[] ends, int rva) {
        int lo=0, hi=starts.Length-1;
        while(lo<=hi){ int m=(lo+hi)/2; if(rva<starts[m]) hi=m-1; else if(rva>=ends[m]) lo=m+1; else return m; }
        return -1;
    }
    public static List<long[]> GetOutboundCalls(byte[] bytes, int rvaStart, int rvaEnd, int textOff, int textVA) {
        int off = textOff + (rvaStart - textVA);
        int size = rvaEnd - rvaStart;
        var calls = new List<long[]>();
        for (int i = 0; i < size - 5; i++) {
            byte b = bytes[off + i];
            if (b == 0xE8 || b == 0xE9) {
                int disp = BitConverter.ToInt32(bytes, off + i + 1);
                long tgt = (long)(rvaStart + i + 5) + disp;
                if (tgt > 0x1000 && tgt < 0x800000)
                    calls.Add(new long[] { b == 0xE8 ? 0 : 1, rvaStart + i, (int)(tgt & 0xFFFFFFFFL) });
                i += 4;
            }
        }
        return calls;
    }
}
'@

function Get-U16([byte[]]$b,[int]$o){ [BitConverter]::ToUInt16($b,$o) }
function Get-U32([byte[]]$b,[int]$o){ [BitConverter]::ToUInt32($b,$o) }

$bytes = [System.IO.File]::ReadAllBytes($BinPath)
$peOff = Get-U32 $bytes 0x3C
$secCount = Get-U16 $bytes ($peOff+6)
$optSz = Get-U16 $bytes ($peOff+20)
$secOff = $peOff+24+$optSz
$textOff=0; $textVA=0; $textSz=0; $pdOff=0; $pdSz=0
for($i=0;$i -lt $secCount;$i++){
    $o=$secOff+40*$i
    $n=[Text.Encoding]::ASCII.GetString($bytes,$o,8).Trim([char]0)
    $va=Get-U32 $bytes ($o+12); $rs=Get-U32 $bytes ($o+16); $rp=Get-U32 $bytes ($o+20)
    if($n -eq '.text'){ $textOff=[int]$rp; $textVA=[int]$va; $textSz=[int]$rs }
    if($n -eq '.pdata'){ $pdOff=[int]$rp; $pdSz=[int]$rs }
}
$pdCnt=[int]($pdSz/12)
$pdStarts=[int[]]::new($pdCnt); $pdEnds=[int[]]::new($pdCnt)
for($i=0;$i -lt $pdCnt;$i++){
    $pdStarts[$i]=[BitConverter]::ToInt32($bytes,$pdOff+12*$i)
    $pdEnds[$i]  =[BitConverter]::ToInt32($bytes,$pdOff+12*$i+4)
}

$knownFuncs = @{
    0x001C3A30 = 'DISP01_transport_dispatcher'
    0x001C4010 = 'TR01_transport_wrapper_A'
    0x001C1BB0 = 'TR02_ioctl_cluster_A1'
    0x001C6BB0 = 'TR03_ioctl_cluster_B'
    0x003E16B0 = 'PR01_parser_cmdline'
    0x003F37E4 = 'ARGT01_tokenizer'
    0x003E16D8 = 'get_argv_count'
    0x003E16E0 = 'get_argv_ptr_table'
    0x003E16E8 = 'get_fallback_buf'
    0x003B160C = 'PR02_parser_compare_A'
    0x003F9610 = 'PR03_parser_compare_B'
    0x003B2714 = 'OPT_DISP_candidate'
    0x00395CA8 = 'DPRB01_compare_A_caller'
    0x004052CC = 'DPRB04_compare_B_caller'
}

# Load import callsites for annotation
$importsByRva = @{}
foreach($row in (Import-Csv $ImportCsv)){
    $rva=[Convert]::ToInt32($row.callsite_rva.Replace('0x',''),16)
    $importsByRva[$rva] = $row.dll + '!' + $row.import_name
}

$optDispBegin = [int]0x003B2714
$optDispEnd   = [int]0x003B288B

$md = @()
$md += '# Option Dispatcher (OPT_DISP) Deep Analysis'
$md += '# 0x003B2714..0x003B288B — calls get_argv_count and get_argv_ptr_table'
$md += ''

# 1. Outbound calls from OPT_DISP
$outCalls = [Scan3]::GetOutboundCalls($bytes,$optDispBegin,$optDispEnd,$textOff,$textVA)
$md += ('## OPT_DISP Outbound Calls (' + $outCalls.Count + ' total)')
foreach($c in $outCalls){
    $type=if($c[0] -eq 0){'CALL'}else{'JMP'}
    $from='0x{0:X8}' -f [int]$c[1]
    $to  ='0x{0:X8}' -f [int]$c[2]
    $toRva=[int]$c[2]
    $lbl=if($knownFuncs.ContainsKey($toRva)){'  ['+$knownFuncs[$toRva]+']'}else{''}
    $imp=if($importsByRva.ContainsKey($toRva)){' (IAT: '+$importsByRva[$toRva]+')'}else{''}
    $fi=[Scan3]::Bsearch($pdStarts,$pdEnds,$toRva)
    $fi2=''; if($fi -ge 0){ $fi2=' in_func 0x{0:X8}..0x{1:X8}' -f $pdStarts[$fi],$pdEnds[$fi] }
    $md += ('  ' + $type + ' ' + $from + ' -> ' + $to + $lbl + $imp + $fi2)
}
$md += ''

# 2. Import callsites inside OPT_DISP
$importsInRange = @()
foreach($row in (Import-Csv $ImportCsv)){
    $rva=[Convert]::ToInt32($row.callsite_rva.Replace('0x',''),16)
    if($rva -ge $optDispBegin -and $rva -lt $optDispEnd){
        $importsInRange += $row
    }
}
$md += ('## OPT_DISP Import Callsites (' + $importsInRange.Count + ')')
foreach($r in $importsInRange){ $md += ('  ' + $r.callsite_rva + ' -> ' + $r.dll + '!' + $r.import_name) }
$md += ''

# 3. Callers of OPT_DISP
Write-Output 'Scanning for OPT_DISP callers...'
$callerHits = [Scan3]::FindCallers($bytes,$textOff,$textSz,$textVA,[int[]]($optDispBegin))
$md += ('## OPT_DISP Callers (' + $callerHits.Count + ')')
foreach($h in $callerHits){
    $callerRva=[int]$h[1]
    $fi=[Scan3]::Bsearch($pdStarts,$pdEnds,$callerRva)
    $lbl=if($fi -ge 0 -and $knownFuncs.ContainsKey($pdStarts[$fi])){'  ['+$knownFuncs[$pdStarts[$fi]]+']'}else{''}
    $funcInfo=if($fi -ge 0){'func 0x{0:X8}..0x{1:X8} size=0x{2:X}' -f $pdStarts[$fi],$pdEnds[$fi],($pdEnds[$fi]-$pdStarts[$fi])}else{'no_pdata'}
    $md += ('  <- 0x{0:X8}' -f $callerRva + $lbl + '  ' + $funcInfo)
}
$md += ''

# 4. Import callsites inside the large caller (0x0006A930..0x0006E7E8) — checking overlap with OPT path
$md += '## Large caller (0x0006A930) — import callsites sample'
$largeBegin=[int]0x0006A930; $largeEnd=[int]0x0006E7E8
$largeImports = @($importsInRange = (Import-Csv $ImportCsv) | Where-Object {
    $rv=[Convert]::ToInt32($_.callsite_rva.Replace('0x',''),16)
    $rv -ge $largeBegin -and $rv -lt $largeEnd
} | Select-Object -First 20)
$md += ('  (first 20 of ' + ($largeImports.Count) + ' import callsites in 0x6A930..0x6E7E8)')
foreach($r in $largeImports){ $md += ('  ' + $r.callsite_rva + ' -> ' + $r.dll + '!' + $r.function) }

$md -join "`r`n" | Set-Content "$OutDir\vmr_opt_disp_analysis.md" -Encoding ascii
Get-Content "$OutDir\vmr_opt_disp_analysis.md"
