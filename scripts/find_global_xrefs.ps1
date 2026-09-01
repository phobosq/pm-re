param(
    [string]$BinPath = 'C:\temp\pm\samples\work\unpacked\PhoenixMiner_6.2c_Windows\PhoenixMiner.exe.bin',
    [string]$OutDir  = 'C:\temp\pm\notes'
)
$ErrorActionPreference = 'Stop'
function Get-U16([byte[]]$b,[int]$o){ [BitConverter]::ToUInt16($b,$o) }
function Get-U32([byte[]]$b,[int]$o){ [BitConverter]::ToUInt32($b,$o) }
function Get-I32([byte[]]$b,[int]$o){ [BitConverter]::ToInt32($b,$o) }

$bytes = [System.IO.File]::ReadAllBytes($BinPath)
$peOff = Get-U32 $bytes 0x3C
$optOff = $peOff+24
$imageBase = [BitConverter]::ToUInt64($bytes,$optOff+24)
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
$textSec = $secs | Where-Object { $_.Name -eq '.text' } | Select-Object -First 1
$pdataSec = $secs | Where-Object { $_.Name -eq '.pdata' } | Select-Object -First 1

Write-Output ('ImageBase: 0x{0:X}' -f $imageBase)

# Target globals (VA with imagebase)
$targets = @(
    @{va=[uint64]0x1407EDB3C; rva=[uint32]0x007EDB3C; label='argv_count'},
    @{va=[uint64]0x1407EDB40; rva=[uint32]0x007EDB40; label='argv_ptr_table'},
    @{va=[uint64]0x1407EDB50; rva=[uint32]0x007EDB50; label='cmdlineA_ptr'},
    @{va=[uint64]0x1407EDB58; rva=[uint32]0x007EDB58; label='cmdlineW_ptr'},
    @{va=[uint64]0x1407EDB60; rva=[uint32]0x007EDB60; label='fallback_buf'}
)

function Find-Pdata-Func([uint32]$rva){
    $pdataOff=$pdataSec.RawPtr; $cnt=[int]($pdataSec.RawSize/12)
    for($i=0;$i -lt $cnt;$i++){
        $off=$pdataOff+12*$i
        $bR=Get-U32 $bytes $off; $eR=Get-U32 $bytes ($off+4)
        if($rva -ge $bR -and $rva -lt $eR){
            return [PSCustomObject]@{begin=('0x{0:X8}' -f $bR);end=('0x{0:X8}' -f $eR);size=[int]($eR-$bR)}
        }
    }
    return $null
}

$knownFuncs = @{
    '0x001C3A30' = 'DISP01_transport_dispatcher'
    '0x001C4010' = 'TR01_transport_wrapper_A'
    '0x001C1BB0' = 'TR02_ioctl_cluster_A1'
    '0x001C6BB0' = 'TR03_ioctl_cluster_B'
    '0x003E16B0' = 'PR01_parser_cmdline'
    '0x003B160C' = 'PR02_parser_compare_A'
    '0x003F9610' = 'PR03_parser_compare_B'
    '0x003F37E4' = 'ARGT01_tokenizer'
    '0x00395CA8' = 'DPRB01_compare_A_caller'
    '0x004052CC' = 'DPRB04_compare_B_caller'
}

# Scan the entire .text for RIP-relative accesses to the target globals.
# For a RIP-relative access, the disp32 is relative to the END of the instruction.
# We scan all 4-byte windows: for each pos, compute the target RVA and see if it matches any global.
# Strategy: for each byte position p in .text, treat bytes[p..p+3] as int32 disp32,
# the instruction's end is at textVA + p + 4 (assuming disp is the last 4 bytes of instr),
# so target_RVA = (textVA + p + 4 + disp32). Check against each target.

Write-Output 'Scanning .text for RIP-relative global accesses...'
$tOff = $textSec.RawPtr
$tSize = [int]$textSec.RawSize
$tVA   = $textSec.VirtualAddress

$rows = @()
for($p=0; $p -lt $tSize-4; $p++){
    $disp32 = Get-I32 $bytes ($tOff+$p)
    $afterInstr = [int64]$tVA + [int64]$p + 4
    $sum64 = $afterInstr + [int64]$disp32
    if($sum64 -lt 0){ $sum64 += 0x100000000L }
    $targetRVA = [uint32]($sum64 -band 0xFFFFFFFFL)
    foreach($t in $targets){
        if($targetRVA -eq $t.rva){
            # Get the byte before to classify: read/write/call
            $b_minus1 = if($p -ge 1){ $bytes[$tOff+$p-1] } else { 0xFF }
            $b_minus2 = if($p -ge 2){ $bytes[$tOff+$p-2] } else { 0xFF }
            $b_minus3 = if($p -ge 3){ $bytes[$tOff+$p-3] } else { 0xFF }
            # Classify likely instruction type
            $instrRVA = [uint32]($tVA + $p - 2)  # most likely starts 2-3 bytes before disp32
            $op = '{0:X2} {1:X2} {2:X2}' -f $b_minus3,$b_minus2,$b_minus1
            # Common RIP-relative patterns ending just before disp32:
            # FF 15 -> CALL [RIP+disp32]  (import call) — disp ends instr, so disp at -2 from end
            # 48 8B 05/0D/15/1D/25/2D/35/3D -> MOV r64,[RIP+disp32]  (read) — disp at -3 from end (REX+opcode+modrm)
            # 48 89 05/0D -> MOV [RIP+disp32],r64  (write)
            # 48 8D 05/0D -> LEA r64,[RIP+disp32]
            # 4C 8B 05/0D -> MOV r8/r9,[RIP+disp32]
            $accessType = 'unknown'
            if($b_minus2 -eq 0xFF -and $b_minus1 -eq 0x15){ $instrRVA=[uint32]($tVA+$p-2); $accessType='CALL_IND' }
            elseif($b_minus3 -in @(0x48,0x4C,0x4D,0x44) -and $b_minus2 -eq 0x8B){ $instrRVA=[uint32]($tVA+$p-3); $accessType='READ_64' }
            elseif($b_minus3 -in @(0x48,0x4C,0x4D,0x44) -and $b_minus2 -eq 0x89){ $instrRVA=[uint32]($tVA+$p-3); $accessType='WRITE_64' }
            elseif($b_minus3 -in @(0x48,0x4C) -and $b_minus2 -eq 0x8D){ $instrRVA=[uint32]($tVA+$p-3); $accessType='LEA' }
            elseif($b_minus3 -in @(0x48,0x4C) -and $b_minus2 -eq 0x3B){ $instrRVA=[uint32]($tVA+$p-3); $accessType='CMP' }
            elseif($b_minus3 -in @(0x48,0x4C) -and $b_minus2 -eq 0x85){ $instrRVA=[uint32]($tVA+$p-3); $accessType='TEST' }
            elseif($b_minus3 -eq 0x48 -and $b_minus2 -eq 0x83){ $instrRVA=[uint32]($tVA+$p-3); $accessType='CMP_IMM8' }

            $pf = Find-Pdata-Func $instrRVA
            $funcLabel = if($pf -and $knownFuncs.ContainsKey($pf.begin)){ $knownFuncs[$pf.begin] } else { '' }
            $rows += [PSCustomObject]@{
                global_label = $t.label
                global_rva   = ('0x{0:X8}' -f $t.rva)
                access_type  = $accessType
                instr_rva    = ('0x{0:X8}' -f $instrRVA)
                op_bytes     = $op
                func_begin   = if($pf){ $pf.begin } else { '' }
                func_end     = if($pf){ $pf.end } else { '' }
                func_size    = if($pf){ $pf.size } else { 0 }
                func_label   = $funcLabel
            }
            break
        }
    }
}

$rows | Export-Csv "$OutDir\vmr_global_xrefs.csv" -NoTypeInformation -Encoding ascii
Write-Output ('Total xrefs: ' + $rows.Count)

$md = @()
$md += '# vmr Global Variable Cross-References'
$md += 'Globals from session3: PR01 stores cmdline, ARGT01 tokenizes into argv table'
$md += 'confidence: strongly_inferred (RIP-relative scan of .text)'
$md += ''
foreach($t in $targets){
    $tRows = @($rows | Where-Object { $_.global_label -eq $t.label })
    $md += ('## ' + $t.label + ' @ 0x{0:X8}  ({1} xrefs)' -f $t.rva,$tRows.Count)
    $reads  = @($tRows | Where-Object { $_.access_type -like 'READ*' -or $_.access_type -eq 'CMP' -or $_.access_type -eq 'TEST' })
    $writes = @($tRows | Where-Object { $_.access_type -like 'WRITE*' })
    $other  = @($tRows | Where-Object { $_.access_type -notin @('READ_64','WRITE_64','CMP','TEST') })
    if($writes.Count -gt 0){
        $md += ('  WRITES (' + $writes.Count + '):')
        foreach($r in $writes){ 
            $lbl=if($r.func_label){'  ['+$r.func_label+']'}else{''}
            $md += ('    ' + $r.instr_rva + $lbl + ' in ' + $r.func_begin + '..' + $r.func_end)
        }
    }
    if($reads.Count -gt 0){
        $md += ('  READS (' + $reads.Count + '):')
        foreach($r in $reads){ 
            $lbl=if($r.func_label){'  ['+$r.func_label+']'}else{''}
            $md += ('    ' + $r.instr_rva + '  ' + $r.access_type + $lbl + ' in ' + $r.func_begin + '..' + $r.func_end)
        }
    }
    if($other.Count -gt 0){
        $md += ('  OTHER (' + $other.Count + '):')
        foreach($r in $other){
            $lbl=if($r.func_label){'  ['+$r.func_label+']'}else{''}
            $md += ('    ' + $r.instr_rva + '  ' + $r.access_type + $lbl + ' in ' + $r.func_begin + '..' + $r.func_end)
        }
    }
    $md += ''
}

$md -join "`r`n" | Set-Content "$OutDir\vmr_global_xrefs.md" -Encoding ascii
Get-Content "$OutDir\vmr_global_xrefs.md"
