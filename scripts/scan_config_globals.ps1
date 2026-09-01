param(
    [string]$BinPath = 'C:\temp\pm\samples\work\unpacked\PhoenixMiner_6.2c_Windows\PhoenixMiner.exe.bin'
)
$ErrorActionPreference = 'Stop'

$bytes=[System.IO.File]::ReadAllBytes($BinPath)
function Get-U16([byte[]]$b,[int]$o){ [BitConverter]::ToUInt16($b,$o) }
function Get-U32([byte[]]$b,[int]$o){ [BitConverter]::ToUInt32($b,$o) }

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
    while($lo -le $hi){$m=[int](($lo+$hi)/2);if($rva -lt $pdataStarts[$m]){$hi=$m-1}elseif($rva -ge $pdataEnds[$m]){$lo=$m+1}else{return $m}}; return -1
}
$tOff=[int]$textSec.RawPtr; $tVA=[int]$textSec.VirtualAddress

Add-Type @'
using System; using System.Collections.Generic;
public class TargetScan {
    public static List<long[]> ScanWrites(byte[] bytes, int textOff, int textVA, int textSize, long[] targets) {
        var results = new List<long[]>();
        for (int i = 0; i < textSize - 6; i++) {
            byte b0 = bytes[textOff+i];
            bool rex = (b0 >= 0x40 && b0 <= 0x4F);
            int sk = rex ? 1 : 0;
            if (i + sk + 5 >= textSize) continue;
            byte op = bytes[textOff+i+sk];
            byte mr = bytes[textOff+i+sk+1];
            if ((mr >> 6) != 0 || (mr & 7) != 5) continue;
            // MOV [rip+d32], reg/imm
            bool isWrite = false; bool isImm = false;
            if (op == 0x89) { isWrite = true; }
            else if (op == 0xC7 && ((mr>>3)&7)==0) { isWrite = true; isImm = true; }
            if (!isWrite) continue;
            int dOff = textOff+i+sk+2;
            if (dOff+4 > bytes.Length) continue;
            int disp = BitConverter.ToInt32(bytes, dOff);
            int instrRva = textVA + i;
            long nextRva = instrRva + sk + (isImm ? 10 : 6);
            long tgt = nextRva + disp;
            foreach (long t in targets) {
                if (tgt == t) {
                    results.Add(new long[] { instrRva, tgt, isImm?1:0, (mr>>3)&7 });
                }
            }
        }
        return results;
    }
    public static List<long[]> ScanReads(byte[] bytes, int textOff, int textVA, int textSize, long[] targets) {
        var results = new List<long[]>();
        for (int i = 0; i < textSize - 6; i++) {
            byte b0 = bytes[textOff+i];
            bool rex = (b0 >= 0x40 && b0 <= 0x4F);
            int sk = rex ? 1 : 0;
            if (i + sk + 5 >= textSize) continue;
            byte op = bytes[textOff+i+sk];
            byte mr = bytes[textOff+i+sk+1];
            if ((mr >> 6) != 0 || (mr & 7) != 5) continue;
            if (op != 0x8B) continue;
            int dOff = textOff+i+sk+2;
            if (dOff+4 > bytes.Length) continue;
            int disp = BitConverter.ToInt32(bytes, dOff);
            int instrRva = textVA + i;
            long nextRva = instrRva + sk + 6;
            long tgt = nextRva + disp;
            foreach (long t in targets) {
                if (tgt == t) {
                    results.Add(new long[] { instrRva, tgt, 0, (mr>>3)&7 });
                }
            }
        }
        return results;
    }
}
'@

$tSize=[int]$textSec.RawSize

# Targets to scan for writes (the globals we saw reads from in SETTER area)
$writeTargets=[long[]]@(
    0x00717190, 0x00717194, 0x00717198, 0x007171A0,  # possible config value globals
    0x007EDB70, 0x007EDB66                            # known setter targets
)
$readTargets=[long[]]@(
    0x00717190, 0x00717194, 0x00717198, 0x007171A0
)

$reg64=@('RAX','RCX','RDX','RBX','RSP','RBP','RSI','RDI','R8','R9','R10','R11','R12','R13','R14','R15')

Write-Output '=== WRITES to config-candidate globals ==='
$writes=[TargetScan]::ScanWrites($bytes,$tOff,$tVA,$tSize,$writeTargets)
foreach($r in $writes){
    $rva=[int]$r[0]; $tgt=[int]$r[1]; $isImm=[int]$r[2]; $regN=$reg64[[int]$r[3]]
    $fi=Bsearch $rva; $fn=if($fi -ge 0){'func_0x{0:X8}'-f$pdataStarts[$fi]}else{'no_pdata'}
    $src=if($isImm){'IMM'}else{$regN}
    Write-Output ('  WRITE [0x{0:X8}] <- {1} at 0x{2:X8}  {3}' -f $tgt,$src,$rva,$fn)
}

Write-Output ''
Write-Output '=== READS from 0x00717190..0x007171A0 ==='
$reads=[TargetScan]::ScanReads($bytes,$tOff,$tVA,$tSize,$readTargets)
foreach($r in $reads){
    $rva=[int]$r[0]; $tgt=[int]$r[1]; $regN=$reg64[[int]$r[3]]
    $fi=Bsearch $rva; $fn=if($fi -ge 0){'func_0x{0:X8}'-f$pdataStarts[$fi]}else{'no_pdata'}
    Write-Output ('  READ  [0x{0:X8}] -> {1} at 0x{2:X8}  {3}' -f $tgt,$regN,$rva,$fn)
}

Write-Output ''
Write-Output '=== Hex around 0x003EA2E0 (where WRITE to 0x007EDB70 happens) ==='
$off=$tOff+(0x003EA2E0-$tVA)
for($i=0;$i -lt 64;$i+=16){
    $addr=0x003EA2E0+$i; $line='0x{0:X8}  ' -f $addr
    for($j=0;$j -lt 16;$j++){ $line+='{0:X2} ' -f $bytes[$off+$i+$j] }
    Write-Output $line
}

Write-Output ''
Write-Output '=== Pdata function containing 0x003EA2E8 ==='
$fi=Bsearch 0x003EA2E8
Write-Output ('  pdata idx={0}  start=0x{1:X8}  end=0x{2:X8}' -f $fi,$(if($fi -ge 0){$pdataStarts[$fi]}else{0}),$(if($fi -ge 0){$pdataEnds[$fi]}else{0}))

Write-Output ''
Write-Output '=== What pdata entry covers 0x003E91F0 (func reading 0x00717190)? ==='
$fi=Bsearch 0x003EA011
Write-Output ('  0x003EA011 -> pdata idx={0}  start=0x{1:X8}  end=0x{2:X8}' -f $fi,$(if($fi -ge 0){$pdataStarts[$fi]}else{0}),$(if($fi -ge 0){$pdataEnds[$fi]}else{0}))
$fi=Bsearch 0x003E91F0
Write-Output ('  0x003E91F0 -> pdata idx={0}  start=0x{1:X8}  end=0x{2:X8}' -f $fi,$(if($fi -ge 0){$pdataStarts[$fi]}else{0}),$(if($fi -ge 0){$pdataEnds[$fi]}else{0}))

# Look at hex around OPT_DISP setter call area 0x003B2800..0x003B2880
Write-Output ''
Write-Output '=== OPT_DISP setter call area (0x003B2800..0x003B2880) ==='
$off=$tOff+(0x003B2800-$tVA)
for($i=0;$i -lt 0x80;$i+=16){
    $addr=0x003B2800+$i; $line='0x{0:X8}  ' -f $addr
    for($j=0;$j -lt 16;$j++){ $line+='{0:X2} ' -f $bytes[$off+$i+$j] }
    Write-Output $line
}
