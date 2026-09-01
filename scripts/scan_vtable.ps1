param(
    [string]$BinPath = 'C:\temp\pm\samples\work\unpacked\PhoenixMiner_6.2c_Windows\PhoenixMiner.exe.bin',
    [string]$OutDir  = 'C:\temp\pm\notes'
)
$ErrorActionPreference = 'Stop'

Add-Type @'
using System; using System.Collections.Generic;
public class VtableScan {
    public static List<long[]> ScanData(byte[] bytes, int dataOff, int dataSize, int dataVA,
                                         long imageBase, long[] targetVAs) {
        var hits = new List<long[]>();
        for (int i = 0; i <= dataSize - 8; i++) {
            long v = BitConverter.ToInt64(bytes, dataOff + i);
            for (int t = 0; t < targetVAs.Length; t++) {
                if (v == targetVAs[t]) {
                    hits.Add(new long[] { t, dataVA + i, v });
                    break;
                }
            }
        }
        return hits;
    }
}
'@

function Get-U16([byte[]]$b,[int]$o){ [BitConverter]::ToUInt16($b,$o) }
function Get-U32([byte[]]$b,[int]$o){ [BitConverter]::ToUInt32($b,$o) }

$bytes = [System.IO.File]::ReadAllBytes($BinPath)
$peOff = Get-U32 $bytes 0x3C
$optOff = $peOff+24
$imageBase = [BitConverter]::ToUInt64($bytes,$optOff+24)
$secCount = Get-U16 $bytes ($peOff+6)
$optSz = Get-U16 $bytes ($peOff+20)
$secOff = $optOff+$optSz
$secs = @()
for($i=0;$i -lt $secCount;$i++){
    $o=$secOff+40*$i
    $n=[Text.Encoding]::ASCII.GetString($bytes,$o,8).Trim([char]0)
    $vs=Get-U32 $bytes ($o+8); $va=Get-U32 $bytes ($o+12)
    $rs=Get-U32 $bytes ($o+16); $rp=Get-U32 $bytes ($o+20)
    $secs += [PSCustomObject]@{Name=$n;VirtualSize=$vs;VirtualAddress=$va;RawSize=$rs;RawPtr=$rp}
}

Write-Output ('ImageBase: 0x{0:X}' -f $imageBase)
Write-Output ('Sections: ' + ($secs | ForEach-Object { $_.Name }) -join ', ')

# All no-caller functions identified in sessions 3-4
# These are candidates for vtable entries
$noCallerRVAs = @(
    0x003B2714,  # OPT_DISP
    0x000CA0E0,  # PR02 root path A
    0x003A4D54,  # PR02 root path B
    0x003FE2BC,  # PR03 root path A
    0x003FE408,  # PR03 root path B
    # Also include direct entry points
    0x003E16B0,  # PR01_parser_cmdline
    0x003F37E4,  # ARGT01_tokenizer
    0x003B160C,  # PR02_compare_A
    0x003F9610,  # PR03_compare_B
    0x001C3A30,  # DISP01_transport
    0x001C4010,  # TR01_transport_wrapper_A
    0x001C6BB0,  # TR03_ioctl_cluster_B
    0x003E16D8,  # get_argv_count
    0x003E16E0,  # get_argv_ptr_table
    0x003E16E8   # get_fallback_buf
)

$targetLabels = @{
    0x003B2714 = 'OPT_DISP'
    0x000CA0E0 = 'PR02_root_A'
    0x003A4D54 = 'PR02_root_B'
    0x003FE2BC = 'PR03_root_A'
    0x003FE408 = 'PR03_root_B'
    0x003E16B0 = 'PR01_parser_cmdline'
    0x003F37E4 = 'ARGT01_tokenizer'
    0x003B160C = 'PR02_compare_A'
    0x003F9610 = 'PR03_compare_B'
    0x001C3A30 = 'DISP01_transport'
    0x001C4010 = 'TR01_transport_wrapper_A'
    0x001C6BB0 = 'TR03_ioctl_cluster_B'
    0x003E16D8 = 'get_argv_count'
    0x003E16E0 = 'get_argv_ptr_table'
    0x003E16E8 = 'get_fallback_buf'
}

# Compute virtual addresses (imageBase + RVA)
$targetVAs = [long[]]($noCallerRVAs | ForEach-Object { [long]$imageBase + [long]$_ })

$md = @()
$md += '# vtable / Function Pointer Scan — Session 5'
$md += '# Scanning all non-code sections for 8-byte VAs pointing to key functions'
$md += '# imageBase=0x{0:X}' -f $imageBase
$md += ''

$allHits = @()
foreach($sec in $secs){
    if($sec.Name -in @('.text','.pdata','INIT','.reloc')){ continue }  # skip code and reloc
    if($sec.RawSize -lt 8){ continue }
    $secOff2=[int]$sec.RawPtr; $secSize=[int]$sec.RawSize; $secVA=[int]$sec.VirtualAddress
    Write-Output ('Scanning section ' + $sec.Name + ' VA=0x{0:X} size=0x{1:X}' -f $secVA,$secSize)
    $hits = [VtableScan]::ScanData($bytes,$secOff2,$secSize,$secVA,$imageBase,$targetVAs)
    foreach($h in $hits){
        $tIdx=[int]$h[0]; $hitRVA=[int]$h[1]; $funcRVA=$noCallerRVAs[$tIdx]
        $lbl=$targetLabels[$funcRVA]
        $allHits += [PSCustomObject]@{
            section   = $sec.Name
            ptr_rva   = '0x{0:X8}' -f $hitRVA
            func_rva  = '0x{0:X8}' -f $funcRVA
            func_label= $lbl
        }
    }
}

# Group by pointer_rva to see vtable candidates (consecutive hits at aligned addresses)
$md += ('## All pointer hits: ' + $allHits.Count)
$allHits | Sort-Object section,ptr_rva | ForEach-Object {
    $md += ('  [' + $_.section + '] @' + $_.ptr_rva + ' -> ' + $_.func_rva + '  (' + $_.func_label + ')')
}
$md += ''

# Find vtable clusters: groups of consecutive 8-byte entries (within 32 bytes of each other)
$md += '## vtable cluster analysis (entries within 32 bytes of each other):'
$sorted = @($allHits | Sort-Object { [Convert]::ToInt32($_.ptr_rva.Replace('0x',''),16) })
$clusters = @()
$currentCluster = @()
for($i=0;$i -lt $sorted.Count;$i++){
    $rva=[Convert]::ToInt32($sorted[$i].ptr_rva.Replace('0x',''),16)
    if($currentCluster.Count -eq 0){
        $currentCluster += $sorted[$i]
    } else {
        $prevRva=[Convert]::ToInt32($currentCluster[-1].ptr_rva.Replace('0x',''),16)
        if(($rva - $prevRva) -le 64){
            $currentCluster += $sorted[$i]
        } else {
            if($currentCluster.Count -ge 2){ $clusters += ,$currentCluster }
            $currentCluster = @($sorted[$i])
        }
    }
}
if($currentCluster.Count -ge 2){ $clusters += ,$currentCluster }

foreach($cl in $clusters){
    $firstRva=[Convert]::ToInt32($cl[0].ptr_rva.Replace('0x',''),16)
    $lastRva =[Convert]::ToInt32($cl[-1].ptr_rva.Replace('0x',''),16)
    $md += ('  CLUSTER @ 0x{0:X8}..0x{1:X8} ({2} entries):' -f $firstRva,$lastRva,$cl.Count)
    foreach($e in $cl){
        $md += ('    ' + $e.ptr_rva + ' -> ' + $e.func_rva + '  (' + $e.func_label + ')')
    }
}
if($clusters.Count -eq 0){ $md += '  (no clusters found)' }

$allHits | Export-Csv "$OutDir\vmr_vtable_scan.csv" -NoTypeInformation -Encoding ascii
$md -join "`r`n" | Set-Content "$OutDir\vmr_vtable_scan.md" -Encoding ascii
Write-Output ('Total hits: ' + $allHits.Count)
Get-Content "$OutDir\vmr_vtable_scan.md"
