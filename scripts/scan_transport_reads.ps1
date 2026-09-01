param(
    [string]$BinPath = 'C:\temp\pm\samples\work\unpacked\PhoenixMiner_6.2c_Windows\PhoenixMiner.exe.bin',
    [string]$OutDir  = 'C:\temp\pm\notes'
)
$ErrorActionPreference = 'Stop'

Add-Type @'
using System; using System.Collections.Generic;
public class TransportScanner {
    public static List<long[]> ScanRipOps(byte[] bytes, int beginRva, int endRva, int textOff, int textVA) {
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
            long tgt; int opCode = -1;
            switch (b1) {
                case 0x89: opCode = 0; tgt = nextRva + disp; break;
                case 0x8B: opCode = 1; tgt = nextRva + disp; break;
                case 0x8D: opCode = 2; tgt = nextRva + disp; break;
                case 0x3B: case 0x39: case 0x85: opCode = 3; tgt = nextRva + disp; break;
                case 0xC7:
                    if (((modrm>>3)&7) != 0) { opCode=-1; tgt=0; break; }
                    opCode = 4; nextRva = instrRva + skip + 10; tgt = nextRva + disp; break;
                default: opCode=-1; tgt=0; break;
            }
            if (opCode < 0) continue;
            results.Add(new long[] { instrRva, (int)(tgt & 0xFFFFFFFFL), opCode, (modrm>>3)&7, hasRex ? b0 : 0 });
        }
        return results;
    }
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
    public static List<int> FindCallers(byte[] bytes, int textOff, int textSize, int textVA, int targetRVA) {
        var callers = new List<int>();
        for (int i = 0; i < textSize - 5; i++) {
            if (bytes[textOff+i] != 0xE8) continue;
            int disp = BitConverter.ToInt32(bytes, textOff+i+1);
            long tgt = (long)(textVA+i+5) + disp;
            if ((int)(tgt & 0xFFFFFFFFL) == targetRVA) callers.Add(textVA+i);
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
    $fi=Bsearch $rva; if($fi -ge 0){return ('0x{0:X8}..0x{1:X8}' -f $pdataStarts[$fi],$pdataEnds[$fi])} else{ return 'no_pdata'}
}

$opNames=@('WRITE_r','READ_r','LEA','CMP/TEST','WRITE_imm32')
$reg64=@('RAX','RCX','RDX','RBX','RSP','RBP','RSI','RDI','R8','R9','R10','R11','R12','R13','R14','R15')

function Scan-Region([int]$b,[int]$e,[string]$lbl){
    $results=[TransportScanner]::ScanRipOps($bytes,$b,$e,[int]$textSec.RawPtr,[int]$textSec.VirtualAddress)
    $reads=@($results|Where-Object{$_[2] -eq 1})
    Write-Output ('--- ' + $lbl + ' (0x{0:X8}..0x{1:X8}) READs ---' -f $b,$e)
    foreach($r in $reads){
        $rva=[int]$r[0]; $tgt=[int]$r[1]; $rex=[int]$r[4]; $regIdx=[int]$r[3]
        $bits=if($rex -band 8){'64'}else{'32'}
        $rn=if($regIdx -lt $reg64.Count){$reg64[$regIdx]}else{'Rx'}
        # Skip if target looks like .rdata (0x430000..0x780000 = likely string or function pointer)
        $skip=($tgt -ge 0x430000 -and $tgt -lt 0x780000)
        if(-not $skip){
            Write-Output ('  [{0}] READ  0x{1:X8}  <- [{2:X8}]  -> {3}' -f $bits,$rva,$tgt,$rn)
        }
    }
    $writes=@($results|Where-Object{$_[2] -eq 0 -or $_[2] -eq 4})
    if($writes.Count -gt 0){
        Write-Output ('  WRITEs:')
        foreach($w in $writes){
            $rva=[int]$w[0]; $tgt=[int]$w[1]; $rex=[int]$w[4]; $regIdx=[int]$w[3]
            $bits=if($rex -band 8){'64'}else{'32'}
            $rn=if($regIdx -lt $reg64.Count){$reg64[$regIdx]}else{'Rx'}
            Write-Output ('  [{0}] WRITE  0x{1:X8}  -> [{2:X8}]  src={3}' -f $bits,$rva,$tgt,$rn)
        }
    }
    Write-Output ''
}

# TR02 root: 0x003A4D54 (vtable hit)
$tr2fi=Bsearch 0x003A4D54
$tr2b=[int]$pdataStarts[$tr2fi]; $tr2e=[int]$pdataEnds[$tr2fi]
Scan-Region $tr2b $tr2e ('TR02_root vtable@0x003A4D54')

# DISP01: called from TR01/TR02 — find by looking what TR02 calls
Write-Output '=== TR02 CALL graph ==='
$tr2calls=[TransportScanner]::FindCalls($bytes,$tr2b,$tr2e,[int]$textSec.RawPtr,[int]$textSec.VirtualAddress)
foreach($c in $tr2calls){ $f=[int]($c[0]);$t=[int]($c[1]); Write-Output ('  CALL  0x{0:X8}  -> 0x{1:X8}  {2}' -f $f,$t,(PdataRange $t)) }
Write-Output ''

# Scan TR01 area (known: 0x001C44B5 is in TR01)
$tr1fi=Bsearch 0x001C44B5
$tr1b=[int]$pdataStarts[$tr1fi]; $tr1e=[int]$pdataEnds[$tr1fi]
Scan-Region $tr1b $tr1e ('TR01_area @0x001C44B5')
Write-Output ('TR01 function: 0x{0:X8}..0x{1:X8} (size 0x{2:X})' -f $tr1b,$tr1e,($tr1e-$tr1b))

# PR02_root_A at 0x000CA0E0 (vtable entry) 
$prcall_fi=Bsearch 0x000CA0E0
$prcall_b=[int]$pdataStarts[$prcall_fi]; $prcall_e=[int]$pdataEnds[$prcall_fi]
Scan-Region $prcall_b $prcall_e ('PR02_root_A @0x000CA0E0')
Write-Output ''
Write-Output '=== PR02_root_A CALL graph ==='
$prcalls=[TransportScanner]::FindCalls($bytes,$prcall_b,$prcall_e,[int]$textSec.RawPtr,[int]$textSec.VirtualAddress)
foreach($c in $prcalls[0..19]){ $f=[int]($c[0]);$t=[int]($c[1]); Write-Output ('  CALL  0x{0:X8}  -> 0x{1:X8}  {2}' -f $f,$t,(PdataRange $t)) }
Write-Output ''

# Also look at VMR-related globals 0x007EC638/630/668 — who ELSE reads them?
Write-Output '=== Callers/readers of config globals 0x007EC638, 0x007EC630, 0x007EC668 ==='
$tVA=[int]$textSec.VirtualAddress; $tOff=[int]$textSec.RawPtr; $tSz=[int]$textSec.RawSize
$targets=@(0x007EC638, 0x007EC630, 0x007EC668)
foreach($tgt in $targets){
    $hits=@()
    Add-Type -AssemblyName System.Runtime.InteropServices 2>$null
    $tgtRva=$tgt
    for($i=0;$i -lt $tSz-6;$i++){
        $b0=$bytes[$tOff+$i]
        $hasRex=($b0 -ge 0x40 -and $b0 -le 0x4F)
        $skip=if($hasRex){1}else{0}
        if($i+$skip+5 -ge $tSz){ continue }
        $b1=$bytes[$tOff+$i+$skip]
        $modrm=$bytes[$tOff+$i+$skip+1]
        if((($modrm -shr 6) -ne 0) -or (($modrm -band 7) -ne 5)){ continue }
        $disp=[BitConverter]::ToInt32($bytes,$tOff+$i+$skip+2)
        $instrRva=$tVA+$i
        $nextRva=[long]($instrRva+$skip+6)
        $calcTgt=[int](($nextRva+$disp) -band 0xFFFFFFFFL)
        if($calcTgt -eq $tgtRva){
            $op=if($b1 -eq 0x89 -or $b1 -eq 0xC7){'WRITE'}elseif($b1 -eq 0x8B){'READ'}else{'OTHER'}
            $hits+=[PSCustomObject]@{instr='0x{0:X8}'-f$instrRva;op=$op;func=(PdataRange $instrRva)}
        }
    }
    Write-Output ('--- [0x{0:X8}]: {1} hits ---' -f $tgt,$hits.Count)
    foreach($h in $hits){ Write-Output ('  '+$h.op+'  '+$h.instr+'  '+$h.func) }
}
