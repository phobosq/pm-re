param(
    [string]$BinPath = 'C:\temp\pm\samples\work\unpacked\PhoenixMiner_6.2c_Windows\PhoenixMiner.exe.bin',
    [string]$OutDir  = 'C:\temp\pm\notes'
)
$ErrorActionPreference = 'Stop'

Add-Type @'
using System; using System.Collections.Generic;
public class WriteScanner2 {
    public static List<long[]> ScanWrites(byte[] bytes, int beginRva, int endRva, int textOff, int textVA) {
        int off = textOff + (beginRva - textVA);
        int size = endRva - beginRva;
        var results = new List<long[]>();
        for (int i = 0; i < size - 6; i++) {
            byte rex = bytes[off+i];
            if (rex < 0x48 || rex > 0x4F) continue;
            if (i+6 >= size) break;
            byte op = bytes[off+i+1];
            byte modrm = bytes[off+i+2];
            if ((modrm >> 6) != 0 || (modrm & 7) != 5) continue;
            int disp = BitConverter.ToInt32(bytes, off+i+3);
            int instrRva = beginRva + i;
            long targetRva = instrRva + 7L + disp;
            int opType = -1;
            if (op == 0x89) opType = 0;      // WRITE
            else if (op == 0x8B) opType = 1; // READ
            else if (op == 0x8D) opType = 2; // LEA
            else if (op == 0x3B || op == 0x39) opType = 3; // CMP
            if (opType >= 0)
                results.Add(new long[] { instrRva, targetRva, opType, (modrm >> 3) & 7 });
        }
        return results;
    }
    public static List<int> FindCallers(byte[] bytes, int textOff, int textSize, int textVA, int targetRVA) {
        var callers = new List<int>();
        for (int i = 0; i < textSize - 5; i++) {
            if (bytes[textOff + i] != 0xE8) continue;
            int disp = BitConverter.ToInt32(bytes, textOff + i + 1);
            long tgt = (long)(textVA + i + 5) + disp;
            if ((int)(tgt & 0xFFFFFFFFL) == targetRVA) callers.Add(textVA + i);
        }
        return callers;
    }
    public static int Bsearch(int[] starts, int[] ends, int rva) {
        int lo=0,hi=starts.Length-1;
        while(lo<=hi){int m=(lo+hi)/2;if(rva<starts[m])hi=m-1;else if(rva>=ends[m])lo=m+1;else return m;}
        return -1;
    }
}
'@

function Get-U16([byte[]]$b,[int]$o){ [BitConverter]::ToUInt16($b,$o) }
function Get-U32([byte[]]$b,[int]$o){ [BitConverter]::ToUInt32($b,$o) }

$bytes=[System.IO.File]::ReadAllBytes($BinPath)
$peOff=Get-U32 $bytes 0x3C
$secCount=Get-U16 $bytes ($peOff+6)
$optSz=Get-U16 $bytes ($peOff+20)
$secOff=$peOff+24+$optSz
$secs=@()
for($i=0;$i -lt $secCount;$i++){
    $o=$secOff+40*$i; $n=[Text.Encoding]::ASCII.GetString($bytes,$o,8).Trim([char]0)
    $va=Get-U32 $bytes ($o+12); $rs=Get-U32 $bytes ($o+16); $rp=Get-U32 $bytes ($o+20)
    $secs+=[PSCustomObject]@{Name=$n;VirtualAddress=$va;RawSize=$rs;RawPtr=$rp}
}
$textSec=$secs|Where-Object{$_.Name -eq '.text'}|Select-Object -First 1
$pdataSec=$secs|Where-Object{$_.Name -eq '.pdata'}|Select-Object -First 1
$pdataOff=[int]$pdataSec.RawPtr; $pdataCnt=[int]($pdataSec.RawSize/12)
$pdataStarts=[int[]]::new($pdataCnt); $pdataEnds=[int[]]::new($pdataCnt)
for($i=0;$i -lt $pdataCnt;$i++){
    $pdataStarts[$i]=[BitConverter]::ToInt32($bytes,$pdataOff+12*$i)
    $pdataEnds[$i]=[BitConverter]::ToInt32($bytes,$pdataOff+12*$i+4)
}
function Bsearch([int]$rva){ 
    $lo=0;$hi=$pdataCnt-1
    while($lo -le $hi){$m=[int](($lo+$hi)/2);if($rva -lt $pdataStarts[$m]){$hi=$m-1}elseif($rva -ge $pdataEnds[$m]){$lo=$m+1}else{return $m}}
    return -1
}

$opNames=@('WRITE','READ','LEA','CMP')
$reg64=@('RAX','RCX','RDX','RBX','RSP','RBP','RSI','RDI','R8','R9','R10','R11','R12','R13','R14','R15')

function Scan-Region([int]$b,[int]$e,[string]$lbl){
    $results=[WriteScanner2]::ScanWrites($bytes,$b,$e,[int]$textSec.RawPtr,[int]$textSec.VirtualAddress)
    Write-Output ('--- ' + $lbl + ' (0x{0:X8}..0x{1:X8}) ---' -f $b,$e)
    foreach($r in $results){
        $rva=[int]$r[0]; $tgt=[int]$r[1]; $op=$opNames[[int]$r[2]]; $regIdx=[int]$r[3]
        $fi=Bsearch $rva
        $fn=if($fi -ge 0){'func 0x{0:X8}..0x{1:X8}' -f $pdataStarts[$fi],$pdataEnds[$fi]}else{'no_pdata'}
        $rn=if($regIdx -lt $reg64.Count){$reg64[$regIdx]}else{'Rx'}
        Write-Output ('  ' + $op + '  0x{0:X8}  [0x{1:X8}]  {2}  {3}' -f $rva,$tgt,$rn,$fn)
    }
}

# 1. Code after PR02's CompareStringW JE jump target
Scan-Region 0x003B16C8 0x003B1800 'After_PR02_pdata_boundary'
Write-Output ''

# 2. DPRB01 (0x00395CA8..0x00396008) — direct caller of PR02
Scan-Region 0x00395CA8 0x00396008 'DPRB01_PR02_caller'
Write-Output ''

# 3. DPRB02 (0x003B1C28..0x003B1CCD) — other PR02 caller
Scan-Region 0x003B1C28 0x003B1CCD 'DPRB02_PR02_caller'
Write-Output ''

# 4. 0x003939B8..0x00393A85 — DPRB01's parent
Scan-Region 0x003939B8 0x00393A85 'DPRB01_parent'
Write-Output ''

# 5. 0x003B18EC..0x003B19C7 — DPRB02's parent
Scan-Region 0x003B18EC 0x003B19C7 'DPRB02_parent'
Write-Output ''

# 6. Also scan OPT_DISP itself for writes
Scan-Region 0x003B2714 0x003B288B 'OPT_DISP'
Write-Output ''

# Summary: all unique write-target RVAs found
Write-Output '=== SUMMARY: All unique WRITE targets ==='
$allRegs=@(
    @(0x003B16C8, 0x003B1800),
    @(0x00395CA8, 0x00396008),
    @(0x003B1C28, 0x003B1CCD),
    @(0x003939B8, 0x00393A85),
    @(0x003B18EC, 0x003B19C7),
    @(0x003B2714, 0x003B288B)
)
$allWrites=@()
foreach($rg in $allRegs){
    $r=[WriteScanner2]::ScanWrites($bytes,$rg[0],$rg[1],[int]$textSec.RawPtr,[int]$textSec.VirtualAddress)
    foreach($w in $r){ if([int]$w[2] -eq 0){ $allWrites += '0x{0:X8}' -f [int]$w[1] } }
}
$allWrites | Sort-Object -Unique | ForEach-Object { Write-Output ('  WRITE_TARGET: ' + $_) }
