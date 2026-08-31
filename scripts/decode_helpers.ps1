param(
    [string]$BinPath = 'C:\temp\pm\samples\work\unpacked\PhoenixMiner_6.2c_Windows\PhoenixMiner.exe.bin'
)
$ErrorActionPreference = 'Stop'
function Get-U16([byte[]]$b,[int]$o){ [BitConverter]::ToUInt16($b,$o) }
function Get-U32([byte[]]$b,[int]$o){ [BitConverter]::ToUInt32($b,$o) }

$bytes = [System.IO.File]::ReadAllBytes($BinPath)
$peOff = Get-U32 $bytes 0x3C
$secCount = Get-U16 $bytes ($peOff+6)
$optSz = Get-U16 $bytes ($peOff+20)
$secOff = $peOff+24+$optSz
$secs = @()
for($i=0;$i -lt $secCount;$i++){
    $o=$secOff+40*$i; $n=[Text.Encoding]::ASCII.GetString($bytes,$o,8).Trim([char]0)
    $vs=Get-U32 $bytes ($o+8); $va=Get-U32 $bytes ($o+12)
    $rs=Get-U32 $bytes ($o+16); $rp=Get-U32 $bytes ($o+20)
    $secs += [PSCustomObject]@{n=$n;vs=$vs;va=$va;rs=$rs;rp=$rp}
}

function Rva2Off([uint32]$rva){
    foreach($s in $secs){
        $max=[Math]::Max($s.vs,$s.rs)
        if($rva -ge $s.va -and $rva -lt ($s.va+$max)){ return [uint32]($s.rp+($rva-$s.va)) }
    }
    return [uint32]0
}

function HexDump([uint32]$rva,[int]$len,[string]$label){
    $off=Rva2Off $rva
    if($off -eq 0){ Write-Output ($label + ': offset not found'); return }
    Write-Output ($label + ' @ file 0x' + ('{0:X}' -f $off))
    $hex = ($bytes[$off..([int]$off+$len-1)] | ForEach-Object { '{0:X2}' -f $_ }) -join ' '
    Write-Output $hex
}

# Dump the tiny shared helper candidates
HexDump 0x003B24C0 33 '0x003B24C0 (size=0x21, common helper)'
Write-Output ''
HexDump 0x003B20D4 16 '0x003B20D4 (unknown_pdata, called from DISP01 1x)'
Write-Output ''
HexDump 0x003B20DC 48 '0x003B20DC (unknown_pdata, called from DISP01 4x, TR04 callers)'
Write-Output ''
HexDump 0x003DB020 0x2F '0x003DB020 (called 4x from TR01 and DISP01)'
Write-Output ''
# Decode simple x64 opcode mnemonics for these tiny funcs
function Decode-Simple([uint32]$rva,[int]$len,[string]$label){
    $off=Rva2Off $rva
    if($off -eq 0){ Write-Output ($label + ': not found'); return }
    Write-Output ''; Write-Output ('=== ' + $label + ' naive decode ===')
    $i=0
    while($i -lt $len){
        $b0=$bytes[$off+$i]; $pos='0x{0:X8}' -f ($rva+$i)
        switch($b0){
            0x48 {
                $b1=$bytes[$off+$i+1]
                if($b1 -eq 0x89){ 
                    Write-Output ("  $pos  48 89 xx  MOV r/m64,r64"); $i+=3; break 
                }
                if($b1 -eq 0x8B){ 
                    Write-Output ("  $pos  48 8B xx  MOV r64,r/m64"); $i+=3; break 
                }
                if($b1 -eq 0x83){ 
                    Write-Output ("  $pos  48 83 xx  ADD/SUB/CMP r/m64,imm8"); $i+=4; break 
                }
                if($b1 -eq 0x85){ 
                    Write-Output ("  $pos  48 85 xx  TEST r64,r64"); $i+=3; break 
                }
                if($b1 -eq 0x33){ 
                    Write-Output ("  $pos  48 33 xx  XOR r64,r/m64"); $i+=3; break 
                }
                Write-Output ("  $pos  48 $( '{0:X2}' -f $b1 ) ...  REX.W ..."); $i+=2; break
            }
            0x33 { Write-Output ("  $pos  33 xx  XOR r32,r/m32"); $i+=2; break }
            0x85 { Write-Output ("  $pos  85 xx  TEST r/m32,r32"); $i+=2; break }
            0x39 { Write-Output ("  $pos  39 xx  CMP r/m32,r32"); $i+=2; break }
            0x3B { Write-Output ("  $pos  3B xx  CMP r32,r/m32"); $i+=2; break }
            0x74 { Write-Output ("  $pos  74 xx  JE rel8"); $i+=2; break }
            0x75 { Write-Output ("  $pos  75 xx  JNE rel8"); $i+=2; break }
            0x7E { Write-Output ("  $pos  7E xx  JLE rel8"); $i+=2; break }
            0x7F { Write-Output ("  $pos  7F xx  JG rel8"); $i+=2; break }
            0x72 { Write-Output ("  $pos  72 xx  JB rel8"); $i+=2; break }
            0x73 { Write-Output ("  $pos  73 xx  JAE rel8"); $i+=2; break }
            0x0F {
                $b1=$bytes[$off+$i+1]
                if($b1 -eq 0x84){ Write-Output ("  $pos  0F 84  JE rel32"); $i+=6; break }
                if($b1 -eq 0x85){ Write-Output ("  $pos  0F 85  JNE rel32"); $i+=6; break }
                if($b1 -eq 0x8F){ Write-Output ("  $pos  0F 8F  JG rel32"); $i+=6; break }
                if($b1 -eq 0x8C){ Write-Output ("  $pos  0F 8C  JL rel32"); $i+=6; break }
                Write-Output ("  $pos  0F $( '{0:X2}' -f $b1 )  ..."); $i+=2; break
            }
            0xE8 { 
                $disp=[BitConverter]::ToInt32($bytes,$off+$i+1)
                $tgt=[uint32](([int64]($rva+$i)+5+$disp) -band 0xFFFFFFFF)
                Write-Output ("  $pos  E8  CALL 0x" + ('{0:X8}' -f $tgt)); $i+=5; break 
            }
            0xE9 { 
                $disp=[BitConverter]::ToInt32($bytes,$off+$i+1)
                $tgt=[uint32](([int64]($rva+$i)+5+$disp) -band 0xFFFFFFFF)
                Write-Output ("  $pos  E9  JMP 0x" + ('{0:X8}' -f $tgt)); $i+=5; break 
            }
            0xEB { Write-Output ("  $pos  EB xx  JMP rel8"); $i+=2; break }
            0xC3 { Write-Output ("  $pos  C3  RET"); $i++; break }
            0xC2 { Write-Output ("  $pos  C2 xx xx  RET imm16"); $i+=3; break }
            0x8B { Write-Output ("  $pos  8B xx  MOV r32,r/m32"); $i+=2; break }
            0x89 { Write-Output ("  $pos  89 xx  MOV r/m32,r32"); $i+=2; break }
            0x8D { Write-Output ("  $pos  8D xx  LEA r,m"); $i+=3; break }
            0xB8 { Write-Output ("  $pos  B8  MOV EAX,imm32 " + ('0x{0:X8}' -f (Get-U32 $bytes ($off+$i+1)))); $i+=5; break }
            0x41 { Write-Output ("  $pos  41 xx  REX.B ..."); $i+=2; break }
            0x44 { Write-Output ("  $pos  44 xx  REX.R ..."); $i+=2; break }
            0x45 { Write-Output ("  $pos  45 xx  REX.RB ..."); $i+=2; break }
            0xF7 { Write-Output ("  $pos  F7 xx  TEST/NOT/NEG/MUL ..."); $i+=2; break }
            0xFF { 
                $b1=$bytes[$off+$i+1]
                Write-Output ("  $pos  FF $( '{0:X2}' -f $b1)  CALL/JMP/PUSH/INC indirect"); $i+=2; break 
            }
            0x90 { Write-Output ("  $pos  90  NOP"); $i++; break }
            0x55 { Write-Output ("  $pos  55  PUSH RBP"); $i++; break }
            0x5D { Write-Output ("  $pos  5D  POP RBP"); $i++; break }
            0x53 { Write-Output ("  $pos  53  PUSH RBX"); $i++; break }
            0x5B { Write-Output ("  $pos  5B  POP RBX"); $i++; break }
            0x57 { Write-Output ("  $pos  57  PUSH RDI"); $i++; break }
            0x5F { Write-Output ("  $pos  5F  POP RDI"); $i++; break }
            0x56 { Write-Output ("  $pos  56  PUSH RSI"); $i++; break }
            0x5E { Write-Output ("  $pos  5E  POP RSI"); $i++; break }
            0x50 { Write-Output ("  $pos  50  PUSH RAX"); $i++; break }
            0x58 { Write-Output ("  $pos  58  POP RAX"); $i++; break }
            0x31 { Write-Output ("  $pos  31 xx  XOR r/m32,r32"); $i+=2; break }
            0x83 { 
                $b1=$bytes[$off+$i+1]
                Write-Output ("  $pos  83 $( '{0:X2}' -f $b1) xx  ADD/SUB/CMP r/m32,imm8"); $i+=3; break 
            }
            0x4C { Write-Output ("  $pos  4C xx  REX.WR ..."); $i+=2; break }
            0x4D { Write-Output ("  $pos  4D xx  REX.WRB ..."); $i+=2; break }
            0x4E { Write-Output ("  $pos  4E xx  REX.WX ..."); $i+=2; break }
            0x4F { Write-Object ("  $pos  4F xx  REX.WRXB ..."); $i+=2; break }
            0x49 { Write-Output ("  $pos  49 xx  REX.WB ..."); $i+=2; break }
            0x40 { Write-Output ("  $pos  40 xx  REX ..."); $i+=2; break }
            default {
                Write-Output ("  $pos  " + ('{0:X2}' -f $b0) + "  (unknown/skip)")
                $i++; break
            }
        }
    }
}

Decode-Simple 0x003B24C0 0x21 '0x003B24C0'
Decode-Simple 0x003DB020 0x2F '0x003DB020'
