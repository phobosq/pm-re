param(
    [string]$BinPath = 'C:\temp\pm\samples\work\unpacked\PhoenixMiner_6.2c_Windows\PhoenixMiner.exe.bin',
    [string]$OutDir  = 'C:\temp\pm\notes'
)
$ErrorActionPreference = 'Stop'

Add-Type @'
using System; using System.Collections.Generic;
public class IndirectWriteScanner {
    // Scan for MOV [reg+disp8/32], reg/imm (register-indirect stores)
    // These are the "config struct field writes" that don't use RIP-relative addressing
    // Catches: MOV [Rm+disp8], Reg (89 /r mod=1, rm!=5)
    //          MOV [Rm+disp32], Reg (89 /r mod=2, rm!=5)
    //          MOV [Rm], Reg (89 /r mod=0, rm!=4/5)
    //          Same with REX prefix (48-4F) for 64-bit
    //          C7 /0 for MOV [mem], imm32
    //          8B for MOV reg, [mem] (reads)
    // Returns: [rva, mod, rm, reg, disp, opcode, rex]
    public static List<long[]> ScanIndirect(byte[] bytes, int beginRva, int endRva, int textOff, int textVA) {
        int off = textOff + (beginRva - textVA);
        int size = endRva - beginRva;
        var results = new List<long[]>();
        for (int i = 0; i < size - 2; i++) {
            byte b0 = bytes[off+i];
            bool hasRex = (b0 >= 0x40 && b0 <= 0x4F);
            int skip = hasRex ? 1 : 0;
            if (i + skip + 1 >= size) continue;
            byte op = bytes[off+i+skip];
            // Only interested in MOV store (89), MOV load (8B), MOVSXD (63), CMP (39, 3B), TEST (85)
            if (op != 0x89 && op != 0x8B && op != 0x39 && op != 0x3B && op != 0x85 && op != 0xC7) continue;
            if (i + skip + 2 >= size) continue;
            byte modrm = bytes[off+i+skip+1];
            int mod = (modrm >> 6) & 3;
            int rm  = modrm & 7;
            int reg = (modrm >> 3) & 7;
            if (mod == 3) continue; // register-only, skip
            if (mod == 0 && rm == 5) continue; // RIP-relative, skip (handled by other scanners)
            // SIB: if rm==4, next byte is SIB, skip for now
            // Calculate instruction length to extract disp
            int dispOffset = 0;
            int dispSize = 0;
            int extraForSib = (rm == 4) ? 1 : 0;
            if (mod == 0) { dispSize = 0; }
            else if (mod == 1) { dispSize = 1; }
            else if (mod == 2) { dispSize = 4; }
            dispOffset = off + i + skip + 2 + extraForSib;
            int disp = 0;
            if (dispSize == 1 && dispOffset < bytes.Length) disp = (sbyte)bytes[dispOffset];
            else if (dispSize == 4 && dispOffset + 3 < bytes.Length) disp = BitConverter.ToInt32(bytes, dispOffset);
            // For op==C7, only report if /0
            if (op == 0xC7 && reg != 0) continue;
            results.Add(new long[] {
                beginRva + i, // instrRva
                mod, rm, reg, disp,
                op == 0x89 ? 0L : (op == 0x8B ? 1L : (op == 0x85 ? 2L : (op == 0xC7 ? 3L : 4L))),
                hasRex ? b0 : 0,
                extraForSib
            });
        }
        return results;
    }
    // Find callers
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

$rm64=@('RAX','RCX','RDX','RBX','RSP','RBP','RSI','RDI','R8','R9','R10','R11','R12','R13','R14','R15')
$opNames=@('STORE','LOAD','TEST','STORE_imm','CMP')

function Scan-IW([int]$b,[int]$e,[string]$lbl){
    $results=[IndirectWriteScanner]::ScanIndirect($bytes,$b,$e,[int]$textSec.RawPtr,[int]$textSec.VirtualAddress)
    Write-Output ('=== ' + $lbl + ' (0x{0:X8}..0x{1:X8}) ===' -f $b,$e)
    $stores=@($results|Where-Object{$_[5] -eq 0 -or $_[5] -eq 3})
    Write-Output ('  STORE instructions: ' + $stores.Count)
    foreach($r in $stores){
        $rva=[int]$r[0]; $mod=[int]$r[1]; $rm=[int]$r[2]; $reg=[int]$r[3]
        $disp=[int]$r[4]; $op=$opNames[[int]$r[5]]; $rex=[int]$r[6]; $sib=[int]$r[7]
        $bits=if($rex -band 8){'64'}else{'32'}
        $regName=if(($rex -band 1) -ne 0){$rm64[$rm+8]}else{$rm64[$rm]}
        $regIdx=if(($rex -band 4) -ne 0){$reg+8}else{$reg}
        $srcName=$rm64[$regIdx]
        $dispStr=if($mod -eq 0){''}elseif($disp -ge 0){'+0x{0:X}' -f $disp}else{'-0x{0:X}' -f (-$disp)}
        $sibStr=if($sib -eq 1){'[sib]'}else{''}
        Write-Output ('  [{0}] {1}  0x{2:X8}  [{3}{4}{5}{6}]  src={7}' -f $bits,$op,$rva,$regName,$sibStr,$dispStr,$dispStr,$srcName)
    }
    Write-Output ''
}

# Focus on DPRB01 and key option handlers
Scan-IW 0x00395CA8 0x00396008 'DPRB01'
Scan-IW 0x003B1C28 0x003B1CCD 'DPRB02'
Scan-IW 0x00393800 0x00396100 'option_handler_block_A'
Scan-IW 0x003B1800 0x003B2200 'option_handler_block_B'

# Also look for where 0x003B2E14 returns to callers and what they do with the result
# Find the first few callers and check bytes after the CALL instruction
Write-Output '=== SAMPLE: bytes after CALL 0x003B2E14 in first 5 callers ==='
$callers=[IndirectWriteScanner]::FindCallers($bytes,[int]$textSec.RawPtr,[int]$textSec.RawSize,[int]$textSec.VirtualAddress,0x003B2E14)
$textOff=[int]$textSec.RawPtr; $textVA=[int]$textSec.VirtualAddress
$count=0
foreach($caller in $callers[0..4]){
    $instrOff=$textOff + ($caller - $textVA)
    $nextOff=$instrOff+5
    $hexBytes=''
    for($xi=0;$xi -lt 20;$xi++){
        if($nextOff+$xi -ge $bytes.Length){ break }
        $hexBytes += '{0:X2} ' -f $bytes[$nextOff+$xi]
    }
    Write-Output ('  caller: 0x{0:X8}  after_call_bytes: {1}  {2}' -f $caller,$hexBytes,(PdataRange $caller))
}
