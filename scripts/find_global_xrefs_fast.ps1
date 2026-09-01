param(
    [string]$BinPath = 'C:\temp\pm\samples\work\unpacked\PhoenixMiner_6.2c_Windows\PhoenixMiner.exe.bin',
    [string]$OutDir  = 'C:\temp\pm\notes'
)
$ErrorActionPreference = 'Stop'

# Fast RIP-relative scanner using compiled C#
Add-Type @'
using System;
using System.Collections.Generic;
public class RipScanner {
    public static List<long[]> Scan(byte[] bytes, int textOff, int textSize, int textVA, int[] targetRVAs) {
        var hits = new List<long[]>();
        int end = textSize - 4;
        for (int p = 0; p < end; p++) {
            int disp32 = BitConverter.ToInt32(bytes, textOff + p);
            long targetRVA = (long)(textVA + p + 4) + disp32;
            for (int t = 0; t < targetRVAs.Length; t++) {
                if (targetRVA == targetRVAs[t]) {
                    byte bm3 = (p >= 3) ? bytes[textOff + p - 3] : (byte)0xFF;
                    byte bm2 = (p >= 2) ? bytes[textOff + p - 2] : (byte)0xFF;
                    byte bm1 = (p >= 1) ? bytes[textOff + p - 1] : (byte)0xFF;
                    hits.Add(new long[] { t, textVA + p - 3, bm3, bm2, bm1 });
                    break;
                }
            }
        }
        return hits;
    }
    public static int BsearchPdata(int[] starts, int[] ends, int rva) {
        int lo = 0, hi = starts.Length - 1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (rva < starts[mid]) hi = mid - 1;
            else if (rva >= ends[mid]) lo = mid + 1;
            else return mid;
        }
        return -1;
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
    $o=$secOff+40*$i; $n=[Text.Encoding]::ASCII.GetString($bytes,$o,8).Trim([char]0)
    $vs=Get-U32 $bytes ($o+8); $va=Get-U32 $bytes ($o+12)
    $rs=Get-U32 $bytes ($o+16); $rp=Get-U32 $bytes ($o+20)
    $secs += [PSCustomObject]@{Name=$n;VirtualSize=$vs;VirtualAddress=$va;RawSize=$rs;RawPtr=$rp}
}
$textSec  = $secs | Where-Object { $_.Name -eq '.text' }  | Select-Object -First 1
$pdataSec = $secs | Where-Object { $_.Name -eq '.pdata' } | Select-Object -First 1

Write-Output ('ImageBase: 0x{0:X}  text: VA=0x{1:X} size=0x{2:X}' -f $imageBase,$textSec.VirtualAddress,$textSec.RawSize)

# Build sorted pdata arrays for binary search
$pdataOff=[int]$pdataSec.RawPtr; $pdataCnt=[int]($pdataSec.RawSize/12)
$pdataStarts=[int[]]::new($pdataCnt)
$pdataEnds  =[int[]]::new($pdataCnt)
for($i=0;$i -lt $pdataCnt;$i++){
    $o=$pdataOff+12*$i
    $pdataStarts[$i]=[BitConverter]::ToInt32($bytes,$o)
    $pdataEnds[$i]  =[BitConverter]::ToInt32($bytes,$o+4)
}

# Target globals (RVA = VA - imageBase)
$targets = [ordered]@{
    'argv_count'    = [int]0x007EDB3C
    'argv_ptr_table'= [int]0x007EDB40
    'cmdlineA_ptr'  = [int]0x007EDB50
    'cmdlineW_ptr'  = [int]0x007EDB58
    'fallback_buf'  = [int]0x007EDB60
}
$targetLabels = @($targets.Keys)
$targetRVAs   = [int[]]($targets.Values)

$knownFuncs = @{
    0x001C3A30 = 'DISP01_transport_dispatcher'
    0x001C4010 = 'TR01_transport_wrapper_A'
    0x001C1BB0 = 'TR02_ioctl_cluster_A1'
    0x001C6BB0 = 'TR03_ioctl_cluster_B'
    0x003E16B0 = 'PR01_parser_cmdline'
    0x003B160C = 'PR02_parser_compare_A'
    0x003F9610 = 'PR03_parser_compare_B'
    0x003F37E4 = 'ARGT01_tokenizer'
    0x00395CA8 = 'DPRB01_compare_A_caller'
    0x004052CC = 'DPRB04_compare_B_caller'
}

Write-Output 'Running fast C# RIP-relative scan...'
$sw = [System.Diagnostics.Stopwatch]::StartNew()
$hits = [RipScanner]::Scan($bytes,[int]$textSec.RawPtr,[int]$textSec.RawSize,[int]$textSec.VirtualAddress,$targetRVAs)
$sw.Stop()
Write-Output ('Scan complete in {0:F1}s — {1} hits' -f $sw.Elapsed.TotalSeconds,$hits.Count)

$rows = @()
foreach($h in $hits){
    $tIdx   = [int]$h[0]
    $instrRVA=[int]$h[1]
    $bm3    = [byte]$h[2]; $bm2=[byte]$h[3]; $bm1=[byte]$h[4]

    # Classify access type from the bytes before the disp32
    $accessType = 'unknown'
    $instrStart = $instrRVA
    if($bm2 -eq 0xFF -and $bm1 -eq 0x15){ $instrStart=$instrRVA+1; $accessType='CALL_IND' }
    elseif($bm3 -in @(0x48,0x4C,0x4D,0x44) -and $bm2 -eq 0x8B){ $accessType='READ_64' }
    elseif($bm3 -in @(0x48,0x4C,0x4D,0x44) -and $bm2 -eq 0x89){ $accessType='WRITE_64' }
    elseif($bm3 -in @(0x48,0x4C) -and $bm2 -eq 0x8D){ $accessType='LEA' }
    elseif($bm3 -in @(0x48,0x4C) -and $bm2 -eq 0x3B){ $accessType='CMP_64' }
    elseif($bm3 -in @(0x48,0x4C) -and $bm2 -eq 0x85){ $accessType='TEST_64' }
    elseif($bm3 -in @(0x40,0x41,0x42,0x43,0x44,0x45,0x46,0x47) -and $bm2 -eq 0x8B){ $accessType='READ_32x' }
    elseif($bm1 -eq 0x15 -and $bm2 -ne 0xFF){ $accessType='maybe_CS' }

    # Binary search pdata
    $fi = [RipScanner]::BsearchPdata($pdataStarts,$pdataEnds,$instrStart)
    $funcBegin=''; $funcEnd=''; $funcSize=0; $funcLabel=''
    if($fi -ge 0){
        $funcBegin='0x{0:X8}' -f $pdataStarts[$fi]
        $funcEnd  ='0x{0:X8}' -f $pdataEnds[$fi]
        $funcSize = $pdataEnds[$fi]-$pdataStarts[$fi]
        if($knownFuncs.ContainsKey($pdataStarts[$fi])){ $funcLabel=$knownFuncs[$pdataStarts[$fi]] }
    }

    $rows += [PSCustomObject]@{
        global_label = $targetLabels[$tIdx]
        global_rva   = '0x{0:X8}' -f $targetRVAs[$tIdx]
        access_type  = $accessType
        instr_rva    = '0x{0:X8}' -f $instrStart
        op_bytes     = '{0:X2} {1:X2} {2:X2}' -f $bm3,$bm2,$bm1
        func_begin   = $funcBegin
        func_end     = $funcEnd
        func_size    = $funcSize
        func_label   = $funcLabel
    }
}

$rows | Sort-Object global_label,instr_rva | Export-Csv "$OutDir\vmr_global_xrefs.csv" -NoTypeInformation -Encoding ascii

# Render markdown
$md = @()
$md += '# vmr Global Variable Cross-References (Session 4)'
$md += '# Globals from ARGT01 (session3): argv table written by tokenizer, read by option dispatcher'
$md += '# confidence: strongly_inferred (exhaustive RIP-relative .text scan)'
$md += ''
foreach($lbl in $targetLabels){
    $tRows  = @($rows | Where-Object { $_.global_label -eq $lbl })
    $rva    = '0x{0:X8}' -f $targets[$lbl]
    $writes = @($tRows | Where-Object { $_.access_type -like 'WRITE*' })
    $reads  = @($tRows | Where-Object { $_.access_type -in @('READ_64','READ_32x','CMP_64','TEST_64') })
    $other  = @($tRows | Where-Object { $_.access_type -notin @('WRITE_64','READ_64','READ_32x','CMP_64','TEST_64') })
    $md += ('## ' + $lbl + ' @ ' + $rva + '  (' + $tRows.Count + ' total: ' + $writes.Count + ' writes, ' + $reads.Count + ' reads, ' + $other.Count + ' other)')
    if($writes.Count -gt 0){
        $md += '  WRITES:'
        foreach($r in $writes){
            $lbl2=if($r.func_label){'  ['+$r.func_label+']'}else{''}
            $md += ('    W ' + $r.instr_rva + $lbl2 + '  ' + $r.func_begin + '..' + $r.func_end + ' size=0x{0:X}' -f $r.func_size)
        }
    }
    if($reads.Count -gt 0){
        $md += '  READS:'
        foreach($r in $reads){
            $lbl2=if($r.func_label){'  ['+$r.func_label+']'}else{''}
            $md += ('    R ' + $r.instr_rva + '  ' + $r.access_type + $lbl2 + '  ' + $r.func_begin + '..' + $r.func_end + ' size=0x{0:X}' -f $r.func_size)
        }
    }
    if($other.Count -gt 0){
        $md += '  OTHER (call-indirect / unknown / LEA):'
        foreach($r in $other){
            $lbl2=if($r.func_label){'  ['+$r.func_label+']'}else{''}
            $md += ('    ? ' + $r.instr_rva + '  ' + $r.access_type + $lbl2 + '  ' + $r.func_begin + '..' + $r.func_end + ' size=0x{0:X}' -f $r.func_size)
        }
    }
    $md += ''
}

# Cross-reference: which read-functions also appear in parser/transport chain?
$md += '## Key: read-side consumers NOT already in known-function list'
$readFuncs = @($rows | Where-Object { $_.access_type -in @('READ_64','READ_32x','CMP_64','TEST_64') } |
    Where-Object { $_.func_label -eq '' } |
    Select-Object func_begin,func_end,func_size -Unique |
    Sort-Object func_begin)
foreach($rf in $readFuncs){
    if($rf.func_begin -ne ''){
        $md += ('  UNKNOWN_READER ' + $rf.func_begin + '..' + $rf.func_end + ' size=0x{0:X}' -f [int]$rf.func_size)
    }
}

$md -join "`r`n" | Set-Content "$OutDir\vmr_global_xrefs.md" -Encoding ascii
Write-Output ('Total xrefs: ' + $rows.Count)
Get-Content "$OutDir\vmr_global_xrefs.md"
