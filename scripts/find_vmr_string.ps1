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
$rdataSec=$secs|Where-Object{$_.Name -eq '.rdata'}|Select-Object -First 1
$tOff=[int]$textSec.RawPtr; $tVA=[int]$textSec.VirtualAddress

# Dump raw hex for these RVAs
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

# Setter functions
Hex-Dump 0x003EA2F0 0x10 'setter_0x003EA2F0'
Hex-Dump 0x003EA300 0x10 'setter_0x003EA300'
Hex-Dump 0x003EA310 0x10 'setter_0x003EA310'
Hex-Dump 0x003EA31C 0x50 'setter_0x003EA31C'
Hex-Dump 0x003EA360 0x10 'setter_0x003EA360'

# Also: the 0x007EDB3C area (argv struct) — look at what's at +0x34 (0x007EDB70)
# But that's runtime data... Instead, decode the 0x003EA31C function via the stored file
# Read 0x003EA31C from the notes file
Write-Output ''
Write-Output '--- Reading .rdata string at 0x006C86A8 (used in opt_handler init) ---'
$rva=0x006C86A8; $rSec=$rdataSec; $off=[int]$rSec.RawPtr+($rva-[int]$rSec.VirtualAddress)
if($off -lt $bytes.Length){
    # Try to read as wide string
    $sb=[System.Text.StringBuilder]::new(); $o=$off; $max=100
    while($o+1 -lt $bytes.Length -and $max-- -gt 0){
        $w=[BitConverter]::ToUInt16($bytes,$o)
        if($w -eq 0){break}; if($w -lt 0x20 -or $w -gt 0x7E){break}
        $null=$sb.Append([char]$w); $o+=2
    }
    if($sb.Length -gt 0){ Write-Output ('[W] "'+$sb.ToString()+'"') }
    else{
        $sb=[System.Text.StringBuilder]::new(); $o=$off; $max=100
        while($o -lt $bytes.Length -and $max-- -gt 0){
            $c=$bytes[$o]; if($c -eq 0){break}; if($c -lt 0x20 -or $c -gt 0x7E){break}
            $null=$sb.Append([char]$c); $o++
        }
        if($sb.Length -gt 0){ Write-Output ('[A] "'+$sb.ToString()+'"') }
    }
}

Write-Output ''
Write-Output '--- Checking .rdata area around 0x00432580, 0x00432538 (OPT_DISP LEA targets) ---'
foreach($checkRva in @(0x00432580, 0x00432538, 0x00432530)){
    $rdataVA=[int]$rdataSec.VirtualAddress; $rdataRaw=[int]$rdataSec.RawPtr
    $o=$rdataRaw+($checkRva-$rdataVA)
    $hex=''; for($xi=0;$xi -lt 32;$xi++){ $hex+='{0:X2} ' -f $bytes[$o+$xi] }
    Write-Output ('0x{0:X8}: {1}' -f $checkRva,$hex)
}

Write-Output ''
Write-Output '--- Looking for -vmr string in .rdata ---'
# Search for -vmr as UTF-16LE
$target=[System.Text.Encoding]::Unicode.GetBytes("-vmr`0")
$rdataRaw=[int]$rdataSec.RawPtr; $rdataSz=[int]$rdataSec.RawSize; $rdataVA=[int]$rdataSec.VirtualAddress
for($i=0;$i -lt $rdataSz-10;$i++){
    $match=$true
    for($j=0;$j -lt $target.Length;$j++){ if($bytes[$rdataRaw+$i+$j] -ne $target[$j]){$match=$false;break} }
    if($match){ Write-Output ('  Found "-vmr" UTF16 @ rva=0x{0:X8}' -f ($rdataVA+$i)) }
}
# Also search for -vmr as UTF-16 without null
$target2=[System.Text.Encoding]::Unicode.GetBytes("-vmr")
for($i=0;$i -lt $rdataSz-8;$i++){
    $match=$true
    for($j=0;$j -lt $target2.Length;$j++){ if($bytes[$rdataRaw+$i+$j] -ne $target2[$j]){$match=$false;break} }
    if($match){ Write-Output ('  Found "-vmr" noNULL @ rva=0x{0:X8}' -f ($rdataVA+$i)) }
}
# Search for vmr (without dash, case-insensitive already not, let's also try lowercase)
$target3=[System.Text.Encoding]::Unicode.GetBytes("vmr")
for($i=0;$i -lt $rdataSz-6;$i++){
    $match=$true
    for($j=0;$j -lt $target3.Length;$j++){ if($bytes[$rdataRaw+$i+$j] -ne $target3[$j]){$match=$false;break} }
    if($match){ Write-Output ('  Found "vmr" UTF16 @ rva=0x{0:X8}' -f ($rdataVA+$i)) }
}
