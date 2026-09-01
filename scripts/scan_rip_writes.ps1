param(
    [string]$BinPath = 'C:\temp\pm\samples\work\unpacked\PhoenixMiner_6.2c_Windows\PhoenixMiner.exe.bin',
    [string]$OutDir  = 'C:\temp\pm\notes'
)
$ErrorActionPreference = 'Stop'

Add-Type @'
using System;
using System.Collections.Generic;
public class WriteScanner {
    // Scan for MOV [RIP+d32], reg64 patterns (REX.W + 89 /r where mod=0, rm=5)
    // and LEA reg, [RIP+d32] patterns
    // Returns: [rva, target_rva, op_type, reg]
    // op_type: 0=MOV_WRITE 1=MOV_READ 2=LEA 3=CMP 4=TEST 5=XCHG
    public static List<long[]> ScanWrites(byte[] bytes, int beginRva, int endRva, int textOff, int textVA) {
        int off = textOff + (beginRva - textVA);
        int size = endRva - beginRva;
        var results = new List<long[]>();
        for (int i = 0; i < size - 6; i++) {
            byte rex = bytes[off+i];
            // REX.W prefix (48-4F)
            if (rex < 0x48 || rex > 0x4F) continue;
            if (i+6 >= size) break;
            byte op = bytes[off+i+1];
            byte modrm = bytes[off+i+2];
            byte mod = (byte)((modrm >> 6) & 3);
            byte rm  = (byte)(modrm & 7);
            byte reg = (byte)((modrm >> 3) & 7);
            if (mod != 0 || rm != 5) continue; // must be RIP-relative
            int disp = BitConverter.ToInt32(bytes, off+i+3);
            int instrRva = beginRva + i;
            long nextRva = instrRva + 7;
            long targetRva = nextRva + disp;
            int opType = -1;
            if (op == 0x89) opType = 0; // MOV [RIP+d32], reg
            else if (op == 0x8B) opType = 1; // MOV reg, [RIP+d32]
            else if (op == 0x8D) opType = 2; // LEA reg, [RIP+d32]
            else if (op == 0x3B || op == 0x39) opType = 3; // CMP
            else if (op == 0x85) opType = 4; // TEST
            else if (op == 0x87) opType = 5; // XCHG
            if (opType >= 0) {
                results.Add(new long[] { instrRva, targetRva, opType, reg, rex });
            }
        }
        return results;
    }
}
'@

function Get-U16([byte[]]$b,[int]$o){ [BitConverter]::ToUInt16($b,$o) }
function Get-U32([byte[]]$b,[int]$o){ [BitConverter]::ToUInt32($b,$o) }

$bytes = [System.IO.File]::ReadAllBytes($BinPath)
$peOff = Get-U32 $bytes 0x3C
$optOff=$peOff+24
$imageBase=[BitConverter]::ToUInt64($bytes,$optOff+24)
$secCount=Get-U16 $bytes ($peOff+6)
$optSz=Get-U16 $bytes ($peOff+20)
$secOff=$optOff+$optSz
$secs=@()
for($i=0;$i -lt $secCount;$i++){
    $o=$secOff+40*$i; $n=[Text.Encoding]::ASCII.GetString($bytes,$o,8).Trim([char]0)
    $va=Get-U32 $bytes ($o+12); $rs=Get-U32 $bytes ($o+16); $rp=Get-U32 $bytes ($o+20)
    $secs += [PSCustomObject]@{Name=$n;VirtualAddress=$va;RawSize=$rs;RawPtr=$rp}
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
    while($lo -le $hi){ $m=[int](($lo+$hi)/2); if($rva -lt $pdataStarts[$m]){$hi=$m-1} elseif($rva -ge $pdataEnds[$m]){$lo=$m+1} else{return $m} }
    return -1
}

$opNames = @('WRITE','READ','LEA','CMP','TEST','XCHG')
$regs64  = @('RAX','RCX','RDX','RBX','RSP','RBP','RSI','RDI')

# Key analysis regions
$regions = @(
    @{label='PR02_and_extend';  begin=[int]0x003B1400; end=[int]0x003B1800},
    @{label='PR02_callers';     begin=[int]0x003B1800; end=[int]0x003B2000},
    @{label='DPRB01_area';      begin=[int]0x00393800; end=[int]0x00396100},
    @{label='PR03_and_callers'; begin=[int]0x003F9400; end=[int]0x003FA000},
    @{label='OPT_DISP_area';    begin=[int]0x003B2700; end=[int]0x003B2900},
    @{label='setters_area';     begin=[int]0x003EA200; end=[int]0x003EA400}
)

$allRows = @()
foreach($reg in $regions){
    $writes = [WriteScanner]::ScanWrites($bytes,$reg.begin,$reg.end,[int]$textSec.RawPtr,[int]$textSec.VirtualAddress)
    foreach($w in $writes){
        $instrRva=[int]$w[0]; $targetRva=[int]$w[1]; $opType=[int]$w[2]
        $regIdx=[int]$w[3]; $rexByte=[int]$w[4]
        $fi=Bsearch $instrRva
        $funcBegin=''; $funcEnd=''; $funcSize=0
        if($fi -ge 0){ $funcBegin='0x{0:X8}' -f $pdataStarts[$fi]; $funcEnd='0x{0:X8}' -f $pdataEnds[$fi]; $funcSize=$pdataEnds[$fi]-$pdataStarts[$fi] }
        $allRows += [PSCustomObject]@{
            region     = $reg.label
            instr_rva  = '0x{0:X8}' -f $instrRva
            op         = $opNames[$opType]
            target_rva = '0x{0:X8}' -f $targetRva
            func_begin = $funcBegin
            func_end   = $funcEnd
            func_size  = $funcSize
        }
    }
}

$allRows | Export-Csv "$OutDir\vmr_rip_writes.csv" -NoTypeInformation -Encoding ascii

# Show only WRITEs (potential vmr-store candidates) and sort by target_rva
$writes = @($allRows | Where-Object { $_.op -eq 'WRITE' } | Sort-Object target_rva)
Write-Output ('Total RIP-relative writes in regions: ' + $writes.Count)
Write-Output ''
Write-Output 'WRITE targets (sorted by target RVA — look for repeating stores to same global):'
foreach($w in $writes){
    Write-Output ('  ' + $w.instr_rva + '  -> [' + $w.target_rva + ']  in ' + $w.func_begin + '..' + $w.func_end)
}

# Also show writes from the CompareStringW-containing functions specifically
Write-Output ''
Write-Output 'WRITES from PR02 (0x003B160C) and its extended range:'
foreach($w in ($allRows | Where-Object { $_.op -eq 'WRITE' -and $_.region -eq 'PR02_and_extend' })){
    Write-Output ('  ' + $w.instr_rva + '  -> [' + $w.target_rva + ']  in ' + $w.func_begin + '..' + $w.func_end)
}
Write-Output ''
Write-Output 'WRITES from PR03 area:'
foreach($w in ($allRows | Where-Object { $_.op -eq 'WRITE' -and $_.region -eq 'PR03_and_callers' })){
    Write-Output ('  ' + $w.instr_rva + '  -> [' + $w.target_rva + ']  in ' + $w.func_begin + '..' + $w.func_end)
}
