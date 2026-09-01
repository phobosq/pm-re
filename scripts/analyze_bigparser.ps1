param(
    [string]$BinPath = 'C:\temp\pm\samples\work\unpacked\PhoenixMiner_6.2c_Windows\PhoenixMiner.exe.bin',
    [string]$OutDir  = 'C:\temp\pm\notes'
)
$ErrorActionPreference = 'Stop'

Add-Type @'
using System; using System.Collections.Generic;
public class BigParserScanner {
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
                    opCode = 4; nextRva = instrRva + skip + 10; tgt = nextRva + disp; break;
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
    public static List<long[]> FindIndirectCalls(byte[] bytes, int beginRva, int endRva, int textOff, int textVA) {
        int off = textOff + (beginRva - textVA);
        int size = endRva - beginRva;
        var results = new List<long[]>();
        for (int i = 0; i < size - 5; i++) {
            if (bytes[off+i] != 0xFF) continue;
            byte modrm = bytes[off+i+1];
            if ((modrm & 0x38) != 0x10) continue;
            if ((modrm >> 6) != 0 || (modrm & 7) != 5) continue;
            int disp = BitConverter.ToInt32(bytes, off+i+2);
            long tgt = (beginRva + i + 6) + disp;
            results.Add(new long[] { beginRva + i, (int)(tgt & 0xFFFFFFFFL) });
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

function Read-String([int]$rva){
    $sec=$null
    foreach($s in $secs){ 
        if($rva -ge [int]$s.VirtualAddress -and $rva -lt [int]$s.VirtualAddress+[int]$s.RawSize){ $sec=$s; break }
    }
    if(-not $sec){ return '(oor)' }
    $rawOff=[int]$sec.RawPtr + ($rva - [int]$sec.VirtualAddress)
    if($rawOff+2 -ge $bytes.Length){ return '(eof)' }
    # UTF-16LE
    $sb=[System.Text.StringBuilder]::new(); $o=$rawOff; $max=80
    while($o+1 -lt $bytes.Length -and $max-- -gt 0){
        $w=[BitConverter]::ToUInt16($bytes,$o)
        if($w -eq 0){ break }
        if($w -lt 32 -or $w -gt 126){ $sb.Clear(); break }
        $null=$sb.Append([char]$w); $o+=2
    }
    if($sb.Length -gt 1){ return ('"' + $sb.ToString() + '"') }
    # ASCII
    $sb=[System.Text.StringBuilder]::new(); $o=$rawOff; $max=80
    while($o -lt $bytes.Length -and $max-- -gt 0){
        $c=$bytes[$o]
        if($c -eq 0){ break }
        if($c -lt 32 -or $c -gt 126){ $sb.Clear(); break }
        $null=$sb.Append([char]$c); $o++
    }
    if($sb.Length -gt 0){ return ('"' + $sb.ToString() + '"') }
    $hex=''
    for($xi=0;$xi -lt [Math]::Min(8,$bytes.Length-$rawOff);$xi++){ $hex+='{0:X2} ' -f $bytes[$rawOff+$xi] }
    return ('['+$hex.Trim()+']')
}

$opNames=@('WRITE_r','READ_r','LEA','CMP/TEST','WRITE_imm32')
$reg64=@('RAX','RCX','RDX','RBX','RSP','RBP','RSI','RDI')

# BIG_PARSER = 0x00129A50..0x0012DA40 (size 0x3FF0 = 16368 bytes)
$begin=0x00129A50; $end=0x0012DA40
Write-Output ('=== BIG_PARSER 0x{0:X8}..0x{1:X8} (size 0x{2:X} = {3} bytes) ===' -f $begin,$end,($end-$begin),($end-$begin))
Write-Output ''

# RIP-relative ops
$allOps=[BigParserScanner]::ScanAll($bytes,$begin,$end,[int]$textSec.RawPtr,[int]$textSec.VirtualAddress)
$writes=@($allOps|Where-Object{$_[2] -eq 0 -or $_[2] -eq 4})
$reads=@($allOps|Where-Object{$_[2] -eq 1})
$leas=@($allOps|Where-Object{$_[2] -eq 2})

Write-Output ('RIP-relative WRITEs: ' + $writes.Count)
Write-Output ('RIP-relative READs: ' + $reads.Count)
Write-Output ('RIP-relative LEAs: ' + $leas.Count)
Write-Output ''

Write-Output '--- All WRITE targets (sorted) ---'
$wtgts=@()
foreach($w in $writes){
    $rva=[int]($w[0]); $tgt=[int]($w[1]); $op=$opNames[[int]($w[2])]; $rex=[int]($w[4])
    $bits=if($rex -band 8){'64'}else{'32'}
    $wtgts+=[PSCustomObject]@{instr='0x{0:X8}'-f$rva;target='0x{0:X8}'-f$tgt;op=$op;bits=$bits}
}
$wtgts|Sort-Object target|Format-Table -AutoSize|Out-String|Write-Output

Write-Output ''
Write-Output '--- All LEA targets with strings (sorted) ---'
$prevTgt=-1
foreach($l in ($leas|Sort-Object{[int]$_[1]})){
    $rva=[int]($l[0]); $tgt=[int]($l[1])
    if($tgt -eq $prevTgt+7 -or $tgt -eq $prevTgt+6){ continue } # skip overlapping false hits
    $prevTgt=$tgt
    $str=Read-String $tgt
    if($str -ne '(oor)' -and $str -ne '(eof)'){
        Write-Output ('  LEA  0x{0:X8}  -> 0x{1:X8}  {2}' -f $rva,$tgt,$str)
    }
}

Write-Output ''
Write-Output '--- Unique CALL targets (sorted) ---'
$calls=[BigParserScanner]::FindCalls($bytes,$begin,$end,[int]$textSec.RawPtr,[int]$textSec.VirtualAddress)
$icalls=[BigParserScanner]::FindIndirectCalls($bytes,$begin,$end,[int]$textSec.RawPtr,[int]$textSec.VirtualAddress)
$callTgts=@{}
foreach($c in $calls){
    $t=[int]($c[1])
    if(-not $callTgts.ContainsKey($t)){ $callTgts[$t]=0 }
    $callTgts[$t]++
}
Write-Output 'Direct CALL targets (freq, sorted):'
foreach($kv in ($callTgts.GetEnumerator()|Sort-Object {-$_.Value}|Select-Object -First 30)){
    $fn=PdataRange $kv.Key
    Write-Output ('  count={0,-4} tgt=0x{1:X8}  {2}' -f $kv.Value,$kv.Key,$fn)
}
Write-Output ''
Write-Output 'Indirect CALL targets:'
$iatTgts=@{}
foreach($c in $icalls){ $t=[int]($c[1]); if(-not $iatTgts.ContainsKey($t)){$iatTgts[$t]=0}; $iatTgts[$t]++ }
foreach($kv in ($iatTgts.GetEnumerator()|Sort-Object{$_.Key})){
    Write-Output ('  IAT=[0x{0:X8}]  count={1}' -f $kv.Key,$kv.Value)
}

# Also scan callers of BIG_PARSER
Write-Output ''
Write-Output '--- Callers of BIG_PARSER (0x00129A50) ---'
$crs=[BigParserScanner]::FindCallers($bytes,[int]$textSec.RawPtr,[int]$textSec.RawSize,[int]$textSec.VirtualAddress,0x00129A50)
foreach($c in $crs){ Write-Output ('  0x{0:X8}  {1}' -f $c,(PdataRange $c)) }

# Save to file
$out=@()
$out+='# BIG_PARSER Analysis 0x00129A50..0x0012DA40'
$out+=''; $out+='## WRITE targets (unique, sorted):'
foreach($w in ($wtgts|Sort-Object target -Unique)){ $out+=('  '+$w.bits+' '+$w.op+'  '+$w.instr+'  -> ['+$w.target+']') }
$out+=''; $out+='## LEA string targets:'
foreach($l in ($leas|Sort-Object{[int]$_[1]})){
    $tgt=[int]($l[1])
    $str=Read-String $tgt
    if($str -ne '(oor)' -and $str -ne '(eof)'){ $out+=('  LEA  0x{0:X8}  {1}' -f $tgt,$str) }
}
$out | Set-Content "$OutDir\bigparser_analysis.md" -Encoding ascii
Write-Output ''
Write-Output 'Saved to notes/bigparser_analysis.md'
