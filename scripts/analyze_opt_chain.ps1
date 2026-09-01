param(
    [string]$BinPath = 'C:\temp\pm\samples\work\unpacked\PhoenixMiner_6.2c_Windows\PhoenixMiner.exe.bin',
    [string]$OutDir  = 'C:\temp\pm\notes'
)
$ErrorActionPreference = 'Stop'

Add-Type @'
using System; using System.Collections.Generic;
public class ByteReader {
    // Scan for all RIP-relative ops (read/write/lea/cmp) in a region
    public static List<long[]> ScanAll(byte[] bytes, int beginRva, int endRva, int textOff, int textVA) {
        int off = textOff + (beginRva - textVA);
        int size = endRva - beginRva;
        var results = new List<long[]>();
        for (int i = 0; i < size - 6; i++) {
            byte b0 = bytes[off+i];
            bool hasRex = (b0 >= 0x40 && b0 <= 0x4F);
            int skip = hasRex ? 1 : 0;
            if (i + skip + 5 >= size) continue;
            byte b1 = bytes[off+i+skip];
            byte modrm = bytes[off+i+skip+1];
            if ((modrm >> 6) != 0 || (modrm & 7) != 5) continue;
            int dispOff = off + i + skip + 2;
            if (dispOff + 4 > bytes.Length) continue;
            int disp = BitConverter.ToInt32(bytes, dispOff);
            int instrRva = beginRva + i;
            long nextRva = instrRva + skip + 6;
            long tgt;
            int opCode = -1;
            switch (b1) {
                case 0x89: opCode = 0; tgt = nextRva + disp; break; // WRITE
                case 0x8B: opCode = 1; tgt = nextRva + disp; break; // READ
                case 0x8D: opCode = 2; tgt = nextRva + disp; break; // LEA
                case 0x3B: case 0x39: case 0x85: opCode = 3; tgt = nextRva + disp; break;
                case 0xC7:
                    if (((modrm>>3)&7) != 0) { opCode = -1; tgt = 0; break; }
                    opCode = 4;
                    nextRva = instrRva + skip + 10;
                    tgt = nextRva + disp;
                    break;
                default: opCode = -1; tgt = 0; break;
            }
            if (opCode < 0) continue;
            results.Add(new long[] { instrRva, (int)(tgt & 0xFFFFFFFFL), opCode, (modrm>>3)&7, hasRex ? b0 : 0 });
        }
        return results;
    }
    // Find all CALL rel32 targets from a region
    public static List<long[]> FindCalls(byte[] bytes, int beginRva, int endRva, int textOff, int textVA) {
        int off = textOff + (beginRva - textVA);
        int size = endRva - beginRva;
        var results = new List<long[]>();
        for (int i = 0; i < size - 4; i++) {
            if (bytes[off+i] != 0xE8) continue;
            int disp = BitConverter.ToInt32(bytes, off+i+1);
            long tgt = (beginRva + i + 5) + disp;
            results.Add(new long[] { beginRva + i, (int)(tgt & 0xFFFFFFFFL) });
        }
        return results;
    }
    // Find CALL [mem] (indirect calls via IAT)
    public static List<long[]> FindIndirectCalls(byte[] bytes, int beginRva, int endRva, int textOff, int textVA) {
        int off = textOff + (beginRva - textVA);
        int size = endRva - beginRva;
        var results = new List<long[]>();
        for (int i = 0; i < size - 5; i++) {
            if (bytes[off+i] != 0xFF) continue;
            byte modrm = bytes[off+i+1];
            if ((modrm & 0x38) != 0x10) continue; // /2
            if ((modrm >> 6) != 0 || (modrm & 7) != 5) continue; // mod=0 rm=5 RIP-rel
            int disp = BitConverter.ToInt32(bytes, off+i+2);
            long tgt = (beginRva + i + 6) + disp;
            results.Add(new long[] { beginRva + i, (int)(tgt & 0xFFFFFFFFL) });
        }
        return results;
    }
    // Read bytes at a given raw offset
    public static byte[] ReadAt(byte[] bytes, int offset, int count) {
        var result = new byte[Math.Min(count, bytes.Length - offset)];
        Array.Copy(bytes, offset, result, 0, result.Length);
        return result;
    }
    // Find callers of a given RVA
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
$rdataSec=$secs|Where-Object{$_.Name -eq '.rdata'}|Select-Object -First 1
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
function PdataRange([int]$rva){
    $fi=Bsearch $rva
    if($fi -ge 0){ return ('func_0x{0:X8}..0x{1:X8}' -f $pdataStarts[$fi],$pdataEnds[$fi]) }
    return 'no_pdata'
}

function Read-RdataString([int]$rva){
    if($rva -lt [int]$rdataSec.VirtualAddress){ return '(not in .rdata)' }
    $rawOff=[int]$rdataSec.RawPtr + ($rva - [int]$rdataSec.VirtualAddress)
    if($rawOff -ge $bytes.Length){ return '(out of file)' }
    # try UTF-16LE first
    $sb=[System.Text.StringBuilder]::new()
    $o=$rawOff; $max=200
    while($o+1 -lt $bytes.Length -and $max -gt 0){
        $w=[BitConverter]::ToUInt16($bytes,$o)
        if($w -eq 0){ break }
        if($w -gt 0x7E -or $w -lt 0x20){ break }
        $null=$sb.Append([char]$w); $o+=2; $max--
    }
    if($sb.Length -gt 2){ return ('[UTF16] "' + $sb.ToString() + '"') }
    # try ASCII
    $sb=[System.Text.StringBuilder]::new(); $o=$rawOff; $max=200
    while($o -lt $bytes.Length -and $max -gt 0){
        $c=$bytes[$o]
        if($c -eq 0){ break }
        if($c -gt 0x7E -or $c -lt 0x20){ break }
        $null=$sb.Append([char]$c); $o++; $max--
    }
    if($sb.Length -gt 0){ return ('[ASCII] "' + $sb.ToString() + '"') }
    return ('[bytes] ' + ($bytes[$rawOff..($rawOff+15)] -join ' '))
}

$opNames=@('WRITE_r','READ_r','LEA','CMP/TEST','WRITE_imm32')
$reg64=@('RAX','RCX','RDX','RBX','RSP','RBP','RSI','RDI')

function Scan-Full([int]$b,[int]$e,[string]$lbl){
    Write-Output ('=== ' + $lbl + ' (0x{0:X8}..0x{1:X8}) ===' -f $b,$e)
    $results=[ByteReader]::ScanAll($bytes,$b,$e,[int]$textSec.RawPtr,[int]$textSec.VirtualAddress)
    $calls=[ByteReader]::FindCalls($bytes,$b,$e,[int]$textSec.RawPtr,[int]$textSec.VirtualAddress)
    $icalls=[ByteReader]::FindIndirectCalls($bytes,$b,$e,[int]$textSec.RawPtr,[int]$textSec.VirtualAddress)
    foreach($r in $results){
        $rva=[int]$r[0];$tgt=[int]$r[1];$op=$opNames[[int]$r[2]];$regIdx=[int]$r[3];$rex=[int]$r[4]
        $bits=if($rex -band 8){'64'}else{'32'}
        $rn=if($regIdx -lt $reg64.Count){$reg64[$regIdx]}else{'Rx'}
        $extra=''
        if($op -eq 'LEA' -or $op -eq 'READ_r' -or $op -eq 'WRITE_r'){
            $s=Read-RdataString $tgt
            if($s -ne '(not in .rdata)'){ $extra=' STR='+$s }
        }
        Write-Output ('  [{0}] {1}  0x{2:X8}  [{3:X8}]  {4}{5}' -f $bits,$op,$rva,$tgt,$rn,$extra)
    }
    foreach($c in $calls){
        $from=[int]($c[0]); $to=[int]($c[1])
        Write-Output ('  CALL  0x{0:X8}  -> 0x{1:X8}  {2}' -f $from,$to,(PdataRange $to))
    }
    foreach($c in $icalls){
        $from=[int]($c[0]); $to=[int]($c[1])
        Write-Output ('  CALL_I  0x{0:X8}  -> [0x{1:X8}]' -f $from,$to)
    }
    Write-Output ''
}

# 1. Function 0x003B2E14 — called from PR02 at 0x003B1643, key candidate for vmr parser+store
$fi=Bsearch 0x003B2E14
if($fi -ge 0){
    Scan-Full $pdataStarts[$fi] $pdataEnds[$fi] ('PR02_callee_0x003B2E14 pdata=' + ('0x{0:X8}..0x{1:X8}' -f $pdataStarts[$fi],$pdataEnds[$fi]))
}else{
    # Try manual range  
    Scan-Full 0x003B2E14 0x003B2F00 'PR02_callee_0x003B2E14_manual'
}

# 2. OPT_DISP detailed (all ops with string resolution)
Scan-Full 0x003B2714 0x003B288B 'OPT_DISP_detailed'

# 3. Function 0x003B1D38..0x003B1E56 (writes to 0x007ED148/150/158)
Scan-Full 0x003B1D38 0x003B1E56 'func_003B1D38_writes_ED148'

# 4. Find callers of 0x003B160C (PR02) to understand who drives the comparison
$callers=[ByteReader]::FindCallers($bytes,[int]$textSec.RawPtr,[int]$textSec.RawSize,[int]$textSec.VirtualAddress,0x003B160C)
Write-Output '=== Callers of PR02 (0x003B160C) ==='
foreach($c in $callers){ Write-Output ('  caller: 0x{0:X8}  {1}' -f $c,(PdataRange $c)) }
Write-Output ''

# 5. Find callers of 0x003B2E14
$callers2=[ByteReader]::FindCallers($bytes,[int]$textSec.RawPtr,[int]$textSec.RawSize,[int]$textSec.VirtualAddress,0x003B2E14)
Write-Output '=== Callers of 0x003B2E14 ==='
foreach($c in $callers2){ Write-Output ('  caller: 0x{0:X8}  {1}' -f $c,(PdataRange $c)) }
Write-Output ''

# 6. Strings at OPT_DISP LEA targets
Write-Output '=== Strings at OPT_DISP LEA targets ==='
foreach($rva in @(0x00432580, 0x00432538, 0x00430910, 0x004306F0)){
    $s=Read-RdataString $rva
    Write-Output ('  0x{0:X8}: {1}' -f $rva,$s)
}

# 7. Find callers of 0x003B1D38 (writes to 0x007ED148 area)
Write-Output ''
Write-Output '=== Callers of func_0x003B1D38 ==='
$callers3=[ByteReader]::FindCallers($bytes,[int]$textSec.RawPtr,[int]$textSec.RawSize,[int]$textSec.VirtualAddress,0x003B1D38)
foreach($c in $callers3){ Write-Output ('  caller: 0x{0:X8}  {1}' -f $c,(PdataRange $c)) }
