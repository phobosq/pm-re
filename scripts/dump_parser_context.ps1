param(
    [string]$BinPath = 'C:\temp\pm\samples\work\unpacked\PhoenixMiner_6.2c_Windows\PhoenixMiner.exe.bin',
    [string]$OutDir  = 'C:\temp\pm\notes'
)
$ErrorActionPreference = 'Stop'
function Get-U16([byte[]]$b,[int]$o){ [BitConverter]::ToUInt16($b,$o) }
function Get-U32([byte[]]$b,[int]$o){ [BitConverter]::ToUInt32($b,$o) }
function Get-I32([byte[]]$b,[int]$o){ [BitConverter]::ToInt32($b,$o) }
function HexU32([string]$h){ [Convert]::ToUInt32($h.Replace('0x',''),16) }

$bytes = [System.IO.File]::ReadAllBytes($BinPath)
$peOff = Get-U32 $bytes 0x3C
$optOff = $peOff+24
$secCount = Get-U16 $bytes ($peOff+6)
$optSz = Get-U16 $bytes ($peOff+20)
$secOff = $optOff+$optSz
$secs = @()
for($i=0;$i -lt $secCount;$i++){
    $o=$secOff+40*$i; $n=[Text.Encoding]::ASCII.GetString($bytes,$o,8).Trim([char]0)
    $vs=Get-U32 $bytes ($o+8); $va=Get-U32 $bytes ($o+12)
    $rs=Get-U32 $bytes ($o+16); $rp=Get-U32 $bytes ($o+20)
    $secs += [PSCustomObject]@{Name=$n;VirtualSize=$vs;VirtualAddress=$va;RawSize=$rs;RawPtr=$rp}
}

function Rva2Off([uint32]$rva){
    foreach($s in $secs){
        $max=[Math]::Max($s.VirtualSize,$s.RawSize)
        if($rva -ge $s.VirtualAddress -and $rva -lt ($s.VirtualAddress+$max)){
            return [uint32]($s.RawPtr+($rva-$s.VirtualAddress))
        }
    }
    return [uint32]0
}

function HexDumpRange([uint32]$startRva,[uint32]$endRva,[string]$label){
    $off=Rva2Off $startRva
    if($off -eq 0){ Write-Output ($label + ': not found'); return }
    $len=[int]($endRva-$startRva)
    Write-Output ''
    Write-Output ('=== ' + $label + ' @ 0x{0:X8}..0x{1:X8} ===' -f $startRva,$endRva)
    # Hex + offset
    for($i=0;$i -lt $len;$i+=16){
        $row = '{0:X8}: ' -f ($startRva+$i)
        for($j=0;$j -lt 16 -and ($i+$j) -lt $len;$j++){
            $row += '{0:X2} ' -f $bytes[$off+$i+$j]
        }
        Write-Output $row
    }
}

# 1. Dump from PR01 end (0x003E16D5) through the LEA region to see what function follows
HexDumpRange 0x003E16B0 0x003E1760 'PR01_and_after'

# 2. Dump ARGT01 tokenizer in its updated range (session3 found it at 0x003F37E4..0x003F395A)
HexDumpRange 0x003F37E4 0x003F395A 'ARGT01_tokenizer'

# 3. Dump cleanup function 0x003F4464..0x003F44F2
HexDumpRange 0x003F4464 0x003F44F2 'ARGT01_cleanup'
