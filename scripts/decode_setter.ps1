param(
    [string]$BinPath = 'C:\temp\pm\samples\work\unpacked\PhoenixMiner_6.2c_Windows\PhoenixMiner.exe.bin',
    [string]$OutDir = 'C:\temp\pm\notes'
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

# Hex dump of area containing 0x003EA0B9..0x003EA2F0
function Hex-Dump([int]$rva,[int]$size,[string]$label){
    $off=$tOff+($rva-$tVA)
    Write-Output ('=== ' + $label + ' @ 0x{0:X8} ({1} bytes) ===' -f $rva,$size)
    for($row=0;$row -lt [Math]::Ceiling($size/16);$row++){
        $addr=$rva+$row*16
        $line='0x{0:X8}  ' -f $addr
        $asc=''
        for($col=0;$col -lt 16;$col++){
            $bi=$row*16+$col
            if($bi -lt $size -and $off+$bi -lt $bytes.Length){
                $b=$bytes[$off+$bi]
                $line+='{0:X2} ' -f $b
                $asc+=if($b -ge 0x20 -and $b -le 0x7E){[char]$b}else{'.'}
            }else{$line+='   '; $asc+=' '}
        }
        Write-Output ($line + ' ' + $asc)
    }
}

# Find pdata range for 0x003EA0B9
$fi=Bsearch 0x003EA0B9
if($fi -ge 0){
    $b=$pdataStarts[$fi]; $e=$pdataEnds[$fi]
    Write-Output ('SETTER_COMMON pdata: 0x{0:X8}..0x{1:X8} (size=0x{2:X})' -f $b,$e,($e-$b))
    Hex-Dump $b ($e-$b) 'SETTER_COMMON'
}else{
    Write-Output 'No pdata for 0x003EA0B9 — dumping 512 bytes around it'
    Hex-Dump (0x003EA0B9-0x50) 0x200 'SETTER_COMMON_area'
}

Write-Output ''

# Also scan for ALL RIP-relative ops in the 0x003EA000..0x003EA2F0 range
Add-Type @'
using System; using System.Collections.Generic;
public class RipScan3 {
    public static List<long[]> Scan(byte[] bytes, int beginRva, int endRva, int textOff, int textVA) {
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
                case 0x3B: case 0x39: case 0x85: case 0x3A: opCode = 3; tgt = nextRva + disp; break;
                case 0xC7: if (((modrm>>3)&7)!=0){opCode=-1;tgt=0;break;} opCode=4; nextRva=instrRva+skip+10; tgt=nextRva+disp; break;
                default: opCode = -1; tgt = 0; break;
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
}
'@

Write-Output '=== RIP-relative ops in SETTER_COMMON area (0x003EA000..0x003EA2F0) ==='
$results=[RipScan3]::Scan($bytes,0x003EA000,0x003EA2F0,$tOff,$tVA)
$reg64=@('RAX','RCX','RDX','RBX','RSP','RBP','RSI','RDI','R8','R9','R10','R11','R12','R13','R14','R15')
$opNames=@('WRITE_r','READ_r','LEA','CMP/TEST','WRITE_imm')
foreach($r in $results){
    $rva=[int]$r[0];$tgt=[int]$r[1];$op=$opNames[[int]$r[2]];$rex=[int]$r[4];$rn=$reg64[[int]$r[3]]
    $bits=if($rex -band 8){'64'}else{'32'}
    $fi=Bsearch $rva
    $fn=if($fi -ge 0){'0x{0:X8}'-f$pdataStarts[$fi]}else{'no_pdata'}
    # Only show writes to BSS area (high RVAs > 0x700000)
    if([int]$r[2] -eq 0 -and $tgt -gt 0x700000){
        Write-Output ('  WRITE [{0}] {1} 0x{2:X8} -> [0x{3:X8}] {4}' -f $bits,$op,$rva,$tgt,$fn)
    }
    elseif([int]$r[2] -eq 1 -and $tgt -gt 0x700000){
        Write-Output ('  READ  [{0}] {1} 0x{2:X8} <- [0x{3:X8}] {4}' -f $bits,$op,$rva,$tgt,$fn)
    }
}

Write-Output ''
Write-Output '=== Calls in SETTER_COMMON area ==='
$calls=[RipScan3]::FindCalls($bytes,0x003EA000,0x003EA2F0,$tOff,$tVA)
$callTgts=@{}
foreach($c in $calls){$t=[int]($c[1]); if(-not $callTgts[$t]){$callTgts[$t]=0}; $callTgts[$t]++}
foreach($kv in ($callTgts.GetEnumerator()|Sort-Object{-$_.Value}|Select-Object -First 20)){
    $fi=Bsearch $kv.Key; $fn=if($fi -ge 0){'func_0x{0:X8}'-f$pdataStarts[$fi]}else{'no_pdata'}
    Write-Output ('  count={0,-4} tgt=0x{1:X8} {2}' -f $kv.Value,$kv.Key,$fn)
}

# Search for option name strings in entire binary (not just .rdata)
Write-Output ''
Write-Output '=== Searching for -vmr, -straps, -vmt strings in entire binary ==='
$searches=@('-vmr','-straps','-vmt1','-vmt2','-vmt3')
foreach($s in $searches){
    $targetW=[System.Text.Encoding]::Unicode.GetBytes($s)
    $targetA=[System.Text.Encoding]::ASCII.GetBytes($s)
    for($i=0;$i -lt $bytes.Length-$targetW.Length;$i++){
        $m=$true; for($j=0;$j -lt $targetW.Length;$j++){if($bytes[$i+$j]-ne$targetW[$j]){$m=$false;break}}
        if($m){ Write-Output ('  UTF16 "{0}" @ file_off=0x{1:X8}' -f $s,$i) }
    }
    for($i=0;$i -lt $bytes.Length-$targetA.Length;$i++){
        $m=$true; for($j=0;$j -lt $targetA.Length;$j++){if($bytes[$i+$j]-ne$targetA[$j]){$m=$false;break}}
        if($m){ Write-Output ('  ASCII "{0}" @ file_off=0x{1:X8}' -f $s,$i) }
    }
}
