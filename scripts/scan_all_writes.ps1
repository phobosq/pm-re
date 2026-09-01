param(
    [string]$BinPath = 'C:\temp\pm\samples\work\unpacked\PhoenixMiner_6.2c_Windows\PhoenixMiner.exe.bin',
    [string]$OutDir  = 'C:\temp\pm\notes'
)
$ErrorActionPreference = 'Stop'

Add-Type @'
using System; using System.Collections.Generic;
public class AllRipScanner {
    // Scans for ALL RIP-relative memory operations (both 32- and 64-bit, read/write)
    // Catches: REX.W + 89/8B/3B/39/85/87 (64-bit ops)
    //          89/8B/3B/39/85 without REX (32-bit ops)
    //          C7 /0 (MOV [RIP+d32], imm32)
    //          0F B7/BF (MOVZX/MOVSX 16/8-bit reads)
    //          F7 (TEST r/m32)
    // Returns: [rva, target_rva, op_code, modrm, rex_byte]
    public static List<long[]> ScanAll(byte[] bytes, int beginRva, int endRva, int textOff, int textVA) {
        int off = textOff + (beginRva - textVA);
        int size = endRva - beginRva;
        var results = new List<long[]>();
        for (int i = 0; i < size - 6; i++) {
            byte b0 = bytes[off+i];
            byte b1, modrm;
            int opCode = -1; // 0=WRITE_r/m 1=READ_r/m 2=CMP/TEST/AND 3=WRITE_imm32
            
            // REX prefix 40-4F
            bool hasRex = (b0 >= 0x40 && b0 <= 0x4F);
            int skip = hasRex ? 1 : 0;
            if (i + skip + 5 >= size) continue;
            b1 = bytes[off+i+skip];
            modrm = bytes[off+i+skip+1];
            
            if ((modrm >> 6) != 0 || (modrm & 7) != 5) continue; // must be mod=0, rm=5 (RIP-relative)
            
            int dispOff = off + i + skip + 2;
            if (dispOff + 4 > bytes.Length) continue;
            int disp = BitConverter.ToInt32(bytes, dispOff);
            int instrRva = beginRva + i;
            long nextRva = instrRva + skip + 6;
            long tgt = nextRva + disp;
            
            switch (b1) {
                case 0x89: opCode = 0; break;
                case 0x8B: opCode = 1; break;
                case 0x3B: case 0x39: case 0x85: opCode = 2; break;
                case 0x8D: opCode = 1; break;
                case 0xC7:
                    if (((modrm>>3)&7) != 0) continue;
                    opCode = 3;
                    nextRva = instrRva + skip + 10;
                    tgt = nextRva + disp;
                    break;
            }
            if (opCode < 0) continue;
            results.Add(new long[] { instrRva, (int)(tgt & 0xFFFFFFFFL), opCode, modrm, hasRex ? b0 : 0 });
        }
        return results;
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

$opNames=@('WRITE_r','READ_r','CMP/TEST','WRITE_imm32')

function Scan-Region([int]$b,[int]$e,[string]$lbl){
    $results=[AllRipScanner]::ScanAll($bytes,$b,$e,[int]$textSec.RawPtr,[int]$textSec.VirtualAddress)
    $writes=@($results|Where-Object{$_[2] -eq 0 -or $_[2] -eq 3})
    Write-Output ('--- ' + $lbl + ' (0x{0:X8}..0x{1:X8}) WRITEs only ---' -f $b,$e)
    if($writes.Count -eq 0){ Write-Output '  (none)'; return }
    foreach($r in $writes){
        $rva=[int]$r[0]; $tgt=[int]$r[1]; $op=$opNames[[int]$r[2]]; $rex=[int]$r[4]
        $bits=if($rex -band 8){'64'}else{'32'}
        $fi=Bsearch $rva
        $fn=if($fi -ge 0){'func_0x{0:X8}' -f $pdataStarts[$fi]}else{'no_pdata'}
        Write-Output ('  [{0}bit] {1}  instr=0x{2:X8}  target=[0x{3:X8}]  {4}' -f $bits,$op,$rva,$tgt,$fn)
    }
}

$regions = @(
    @{b=0x003B1600;e=0x003B1800;l='PR02_and_post'},
    @{b=0x003B1800;e=0x003B2200;l='After_PR02_extended'},
    @{b=0x00395CA8;e=0x00396008;l='DPRB01'},
    @{b=0x003B1C28;e=0x003B1CCD;l='DPRB02'},
    @{b=0x003939B8;e=0x00393A85;l='DPRB01_parent'},
    @{b=0x003B18EC;e=0x003B19C7;l='DPRB02_parent'},
    @{b=0x003B2714;e=0x003B288B;l='OPT_DISP'},
    @{b=0x000CA0E0;e=0x000CA127;l='PR02_root_A'},
    @{b=0x003A4D54;e=0x003A4E00;l='PR02_root_B_approx'},
    @{b=0x003EA2F0;e=0x003EA400;l='setters_area'},
    @{b=0x003F9400;e=0x003FA000;l='PR03_and_callers'}
)

foreach($reg in $regions){
    Scan-Region $reg.b $reg.e $reg.l
    Write-Output ''
}
