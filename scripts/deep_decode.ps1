param(
    [string]$BinPath = 'C:\temp\pm\samples\work\unpacked\PhoenixMiner_6.2c_Windows\PhoenixMiner.exe.bin',
    [string]$OutDir  = 'C:\temp\pm\notes'
)
$ErrorActionPreference = 'Stop'

Add-Type @'
using System; using System.Collections.Generic;
public class DeepDecode {
    // Returns list of [rva, opcode_class, target_rva_or_imm, modrm, sib, has_rip_rel, rip_target]
    // opcode_class: 0=other 1=CALL_rel32 2=JMP_rel32 3=MOV_rip_read 4=MOV_rip_write 5=LEA_rip 6=CMP_rip 7=TEST_rip 8=CALL_rip_ind 9=RET 10=JCC_rel8 11=JCC_rel32
    public static List<object[]> Decode(byte[] bytes, int rvaStart, int rvaEnd, int textOff, int textVA) {
        int off = textOff + (rvaStart - textVA);
        int size = rvaEnd - rvaStart;
        var result = new List<object[]>();
        int i = 0;
        while (i < size) {
            int rva = rvaStart + i;
            // Collect REX prefix
            byte rex = 0;
            if (bytes[off+i] >= 0x40 && bytes[off+i] <= 0x4F) { rex = bytes[off+i]; i++; if (i >= size) break; }
            byte b0 = bytes[off+i];
            // CALL rel32
            if (b0 == 0xE8 && i + 4 < size) {
                int disp = BitConverter.ToInt32(bytes, off+i+1);
                long tgt = (long)(rva + 5) + disp;
                result.Add(new object[] { rva, 1, (long)tgt, (byte)0, (byte)0, false, (long)0, "CALL 0x" + tgt.ToString("X8") });
                i += 5; continue;
            }
            // JMP rel32
            if (b0 == 0xE9 && i + 4 < size) {
                int disp = BitConverter.ToInt32(bytes, off+i+1);
                long tgt = (long)(rva + 5) + disp;
                result.Add(new object[] { rva, 2, (long)tgt, (byte)0, (byte)0, false, (long)0, "JMP 0x" + tgt.ToString("X8") });
                i += 5; continue;
            }
            // JCC rel8
            if ((b0 >= 0x70 && b0 <= 0x7F) && i + 1 < size) {
                sbyte disp = (sbyte)bytes[off+i+1];
                long tgt = (long)(rva + 2) + disp;
                result.Add(new object[] { rva, 10, (long)tgt, b0, (byte)0, false, (long)0, "J" + b0.ToString("X2") + " 0x" + tgt.ToString("X8") });
                i += 2; continue;
            }
            // JCC rel32 (0F 8x)
            if (b0 == 0x0F && i + 5 < size) {
                byte b1 = bytes[off+i+1];
                if (b1 >= 0x80 && b1 <= 0x8F) {
                    int disp = BitConverter.ToInt32(bytes, off+i+2);
                    long tgt = (long)(rva + 6) + disp;
                    result.Add(new object[] { rva, 11, (long)tgt, b1, (byte)0, false, (long)0, "J" + b1.ToString("X2") + " 0x" + tgt.ToString("X8") });
                    i += 6; continue;
                }
            }
            // RET
            if (b0 == 0xC3 || b0 == 0xC2) {
                result.Add(new object[] { rva, 9, (long)0, b0, (byte)0, false, (long)0, "RET" });
                i += (b0 == 0xC3 ? 1 : 3); continue;
            }
            // RIP-relative patterns (with or without REX)
            // Need to look at actual op+modrm combo
            // MOV r64, [RIP+d32]: REX.W + 8B /r (mod=0 rm=5)
            // MOV [RIP+d32], r64: REX.W + 89 /r
            // LEA r64, [RIP+d32]: REX.W + 8D /r
            // CMP r64, [RIP+d32]: REX.W + 3B /r or 39 /r
            // CALL [RIP+d32]: FF /2 (mod=0 rm=5)
            if (rex != 0 && i + 5 < size) {
                byte op = b0;
                byte modrm = bytes[off+i+1];
                byte mod = (byte)((modrm >> 6) & 3);
                byte rm  = (byte)(modrm & 7);
                if (mod == 0 && rm == 5 && i + 5 < size) { // RIP-relative ModRM
                    int disp = BitConverter.ToInt32(bytes, off+i+2);
                    long tgt = (long)(rva + 7) + disp; // REX(1) + op(1) + modrm(1) + disp(4) = 7 bytes
                    int cls = 0; string desc = "RIP?";
                    if (op == 0x8B) { cls = 3; desc = "MOV reg,[0x" + tgt.ToString("X8") + "]"; }
                    else if (op == 0x89) { cls = 4; desc = "MOV [0x" + tgt.ToString("X8") + "],reg"; }
                    else if (op == 0x8D) { cls = 5; desc = "LEA reg,[0x" + tgt.ToString("X8") + "]"; }
                    else if (op == 0x3B || op == 0x39) { cls = 6; desc = "CMP [0x" + tgt.ToString("X8") + "]"; }
                    else if (op == 0x85) { cls = 7; desc = "TEST [0x" + tgt.ToString("X8") + "]"; }
                    if (cls != 0) {
                        result.Add(new object[] { rva, cls, tgt, op, modrm, true, tgt, desc });
                        i += 7; continue;
                    }
                }
            }
            // CALL [RIP+d32] = FF 15 disp32 (no REX)
            if (b0 == 0xFF && i + 5 < size) {
                byte b1 = bytes[off+i+1];
                if (b1 == 0x15) { // CALL [RIP+d32]
                    int disp = BitConverter.ToInt32(bytes, off+i+2);
                    long tgt = (long)(rva + 6) + disp;
                    result.Add(new object[] { rva, 8, tgt, b1, (byte)0, true, tgt, "CALL [0x" + tgt.ToString("X8") + "]" });
                    i += 6; continue;
                }
            }
            // Default: emit as raw with first 2 bytes
            string raw = (rex != 0 ? rex.ToString("X2")+" " : "") + b0.ToString("X2");
            if (i+1 < size) raw += " " + bytes[off+i+1].ToString("X2");
            result.Add(new object[] { rva, 0, (long)0, b0, (byte)0, false, (long)0, raw });
            i++;
        }
        return result;
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
$textSec = $secs | Where-Object { $_.Name -eq '.text' } | Select-Object -First 1

function Rva2Off([uint32]$rva){
    foreach($s in $secs){
        $max=[Math]::Max($s.VirtualSize,$s.RawSize)
        if($rva -ge $s.VirtualAddress -and $rva -lt ($s.VirtualAddress+$max)){
            return [uint32]($s.RawPtr+($rva-$s.VirtualAddress))
        }
    }
    return [uint32]0
}

function Decode-And-Print([int]$beginRva,[int]$endRva,[string]$label){
    $instrs = [DeepDecode]::Decode($bytes,$beginRva,$endRva,[int]$textSec.RawPtr,[int]$textSec.VirtualAddress)
    $lines = @()
    $lines += ('=== ' + $label + ' @ 0x{0:X8}..0x{1:X8} ({2} bytes) ===' -f $beginRva,$endRva,($endRva-$beginRva))
    foreach($ins in $instrs){
        $rva='0x{0:X8}' -f [int]$ins[0]
        $desc=[string]$ins[7]
        $cls=[int]$ins[1]
        $marker = switch($cls){
            1 { 'CALL   ' } 2 { 'JMP    ' } 3 { 'READ   ' } 4 { 'WRITE  ' } 5 { 'LEA    ' }
            6 { 'CMP    ' } 7 { 'TEST   ' } 8 { 'CALL_I ' } 9 { 'RET    ' } 10 { 'JCC    ' }
            11 { 'JCC32  ' } default { '       ' }
        }
        $lines += ('  ' + $rva + '  ' + $marker + $desc)
    }
    return $lines
}

$md = @()
$md += '# Deep Decode: PR02, PR03, Setter area, vtable contexts'
$md += ''

# PR02
$pr02Lines = Decode-And-Print 0x003B160C 0x003B16C8 'PR02_compare_A'
$md += $pr02Lines
$md += ''

# PR03
$pr03Lines = Decode-And-Print 0x003F9610 0x003F96FF 'PR03_compare_B'
$md += $pr03Lines
$md += ''

# Setter candidates (4 terminal calls from OPT_DISP)
$setterRanges = @(
    @{begin=0x003EA2F0; end=0x003EA2FF + 0x10; label='setter_0x003EA2F0'}
    @{begin=0x003EA300; end=0x003EA310; label='setter_0x003EA300'}
    @{begin=0x003EA310; end=0x003EA320; label='setter_0x003EA310'}
    @{begin=0x003EA360; end=0x003EA380; label='setter_0x003EA360'}
    @{begin=0x003EA31C; end=0x003EA360; label='setter_0x003EA31C'}
)

# First, find proper pdata boundaries for these
$pdataSec = $secs | Where-Object { $_.Name -eq '.pdata' } | Select-Object -First 1
$pdataOff=[int]$pdataSec.RawPtr; $pdataCnt=[int]($pdataSec.RawSize/12)

function Find-PdataFunc([int]$rva){
    for($i=0;$i -lt $pdataCnt;$i++){
        $bR=[BitConverter]::ToInt32($bytes,$pdataOff+12*$i)
        $eR=[BitConverter]::ToInt32($bytes,$pdataOff+12*$i+4)
        if($rva -ge $bR -and $rva -lt $eR){ return [PSCustomObject]@{begin=$bR;end=$eR} }
    }
    return $null
}

$setterRVAs = @(0x003EA2F0, 0x003EA300, 0x003EA310, 0x003EA360, 0x003EA31C)
foreach($srva in $setterRVAs){
    $pf=Find-PdataFunc $srva
    if($pf){
        $lines=Decode-And-Print $pf.begin $pf.end ('setter_0x{0:X8}' -f $srva)
        $md += $lines; $md += ''
    } else {
        $md += ('setter_0x{0:X8}: not in pdata' -f $srva)
        $md += ''
    }
}

# vtable hit context — dump 128 bytes around each hit
$vtableHits = @(
    @{rva=0x0043DC30; label='vtable_hit_PR02_root_A'},
    @{rva=0x0070CD70; label='vtable_hit_PR02_root_B'},
    @{rva=0x00718DA0; label='vtable_hit_PR01'}
)
foreach($vh in $vtableHits){
    $off=Rva2Off $vh.rva
    if($off -gt 0){
        $md += ('=== ' + $vh.label + ' context @ 0x{0:X8} (64 bytes before/after) ===' -f $vh.rva)
        # Show as 8-byte entries
        for($i=-5;$i -le 5;$i++){
            $pos=$vh.rva+$i*8
            $fOff=Rva2Off $pos
            if($fOff -eq 0){ continue }
            $v=[BitConverter]::ToInt64($bytes,[int]$fOff)
            $rvaV=[long]$v - [long]$imageBase
            $marker=if($i -eq 0){'<<<'}else{'   '}
            $rvaU = [long]($rvaV -band 0xFFFFFFFFL)
            $md += ('  ' + ('0x{0:X8}' -f $pos) + '  =  0x{0:X16}  (RVA=0x{1:X8}) {2}' -f [long]$v,[long]$rvaU,$marker)
        }
        $md += ''
    }
}

$md -join "`r`n" | Set-Content "$OutDir\vmr_deep_decode.md" -Encoding ascii
Write-Output 'Done.'
# Print just the important parts
Write-Output ''; Write-Output '=== PR02 key instructions ==='
$pr02Lines | Where-Object { $_ -match 'WRITE|READ|CMP|CALL|RET|JCC' } | ForEach-Object { Write-Output $_ }
Write-Output ''; Write-Output '=== PR03 key instructions ==='
$pr03Lines | Where-Object { $_ -match 'WRITE|READ|CMP|CALL|RET|JCC' } | ForEach-Object { Write-Output $_ }
