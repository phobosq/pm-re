param(
    [string]$BinPath = 'C:\temp\pm\samples\work\unpacked\PhoenixMiner_6.2c_Windows\PhoenixMiner.exe.bin',
    [string]$OutDir  = 'C:\temp\pm\notes'
)
$ErrorActionPreference = 'Stop'

Add-Type @'
using System; using System.Text;
public class ByteDumper {
    static string[] reg64 = { "RAX","RCX","RDX","RBX","RSP","RBP","RSI","RDI","R8","R9","R10","R11","R12","R13","R14","R15" };
    static string[] reg32 = { "EAX","ECX","EDX","EBX","ESP","EBP","ESI","EDI","R8D","R9D","R10D","R11D","R12D","R13D","R14D","R15D" };
    static string RegName(int idx, bool wide) { return wide ? reg64[idx] : reg32[idx]; }

    // Very basic x64 decoder - handles MOV, CALL, JCC, RET, LEA, TEST, CMP, ADD, SUB, XOR
    public static string DecodeAt(byte[] bytes, int rawOff, int rva, out int len) {
        len = 1;
        if (rawOff >= bytes.Length) return "???";
        byte b0 = bytes[rawOff];
        bool hasRex = b0 >= 0x40 && b0 <= 0x4F;
        bool rexW = hasRex && (b0 & 8) != 0;
        bool rexR = hasRex && (b0 & 4) != 0;
        bool rexX = hasRex && (b0 & 2) != 0;
        bool rexB = hasRex && (b0 & 1) != 0;
        int skip = hasRex ? 1 : 0;
        if (rawOff + skip >= bytes.Length) return hasRex ? string.Format("REX.{0:X}",b0&0xF) : "DB {0:X2}";
        byte op = bytes[rawOff + skip];
        
        // Helper for ModRM decode
        Func<int, int, bool, bool, Tuple<string,int>> decodeModrm = (moOff, dispOff, wide, regExt) => {
            byte modrm = bytes[moOff];
            int mod = (modrm >> 6) & 3;
            int rm = modrm & 7;
            int reg = (modrm >> 3) & 7;
            if (rexR) reg += 8;
            if (rexB) rm += 8;
            int dispSize = 0;
            string rmStr;
            if (mod == 3) { rmStr = RegName(rm, wide); dispSize = 0; }
            else if (mod == 0 && (rm & 7) == 5) {
                // RIP-relative
                int d = BitConverter.ToInt32(bytes, dispOff);
                long tgt = rva + skip + 1 + 1 + 4 + d; // rough
                rmStr = string.Format("[RIP+0x{0:X8}=0x{1:X8}]", d, tgt & 0xFFFFFFFFL);
                dispSize = 4;
            }
            else if ((rm & 7) == 4) {
                // SIB
                byte sib = bytes[moOff+1];
                int scale = 1 << ((sib>>6)&3);
                int idx = (sib>>3)&7; if (rexX) idx+=8;
                int ba = sib&7; if (rexB) ba+=8;
                string sibStr = (ba==5&&mod==0) ? string.Format("[0x{0:X8}]",BitConverter.ToInt32(bytes,moOff+2)) :
                    (idx==4) ? string.Format("[{0}]",RegName(ba,true)) :
                    string.Format("[{0}+{1}*{2}]", RegName(ba,true), RegName(idx,true), scale);
                if (mod == 1) { sbyte d8 = (sbyte)bytes[moOff+2]; sibStr = sibStr.TrimEnd(']') + (d8>=0?"+":"")+d8+"]"; dispSize = 1; }
                else if (mod == 2) { int d32 = BitConverter.ToInt32(bytes,moOff+2); sibStr = sibStr.TrimEnd(']') + (d32>=0?"+0x":"-0x")+Math.Abs(d32).ToString("X")+"]"; dispSize = 4; }
                rmStr = sibStr;
                dispSize += 1; // extra SIB byte
            }
            else {
                rmStr = "[" + RegName(rm, true) + "]";
                if (mod == 1) { sbyte d8 = (sbyte)bytes[moOff + 1]; rmStr = "[" + RegName(rm, true) + (d8>=0?"+0x":"-0x")+Math.Abs((int)d8).ToString("X")+"]"; dispSize = 1; }
                else if (mod == 2) { int d32 = BitConverter.ToInt32(bytes, moOff+1); rmStr = "[" + RegName(rm, true) + (d32>=0?"+0x":"-0x")+Math.Abs(d32).ToString("X")+"]"; dispSize = 4; }
            }
            return Tuple.Create(rmStr + "|" + reg, dispSize);
        };

        // CALL rel32
        if (op == 0xE8 && rawOff + skip + 5 <= bytes.Length) {
            int d = BitConverter.ToInt32(bytes, rawOff + skip + 1);
            long tgt = rva + skip + 5 + d;
            len = skip + 5;
            return string.Format("CALL 0x{0:X8}", tgt & 0xFFFFFFFFL);
        }
        // JMP rel32
        if (op == 0xE9 && rawOff + skip + 5 <= bytes.Length) {
            int d = BitConverter.ToInt32(bytes, rawOff + skip + 1);
            long tgt = rva + skip + 5 + d;
            len = skip + 5;
            return string.Format("JMP 0x{0:X8}", tgt & 0xFFFFFFFFL);
        }
        // JMP rel8
        if (op == 0xEB && rawOff + skip + 2 <= bytes.Length) {
            int d = (sbyte)bytes[rawOff + skip + 1];
            long tgt = rva + skip + 2 + d;
            len = skip + 2;
            return string.Format("JMP.S 0x{0:X8}", tgt & 0xFFFFFFFFL);
        }
        // Jcc rel8
        if (op >= 0x70 && op <= 0x7F && rawOff + skip + 2 <= bytes.Length) {
            string[] jcc = {"JO","JNO","JB","JAE","JZ","JNZ","JBE","JA","JS","JNS","JP","JNP","JL","JGE","JLE","JG"};
            int d = (sbyte)bytes[rawOff + skip + 1];
            long tgt = rva + skip + 2 + d;
            len = skip + 2;
            return string.Format("{0} 0x{1:X8}", jcc[op&0xF], tgt & 0xFFFFFFFFL);
        }
        // Jcc rel32 (0F 8x)
        if (op == 0x0F && rawOff + skip + 6 <= bytes.Length) {
            byte op2 = bytes[rawOff + skip + 1];
            if (op2 >= 0x80 && op2 <= 0x8F) {
                string[] jcc = {"JO","JNO","JB","JAE","JZ","JNZ","JBE","JA","JS","JNS","JP","JNP","JL","JGE","JLE","JG"};
                int d = BitConverter.ToInt32(bytes, rawOff + skip + 2);
                long tgt = rva + skip + 6 + d;
                len = skip + 6;
                return string.Format("{0} 0x{1:X8}", jcc[op2&0xF], tgt & 0xFFFFFFFFL);
            }
        }
        // RET
        if (op == 0xC3) { len = skip + 1; return "RET"; }
        if (op == 0xC2 && rawOff + skip + 3 <= bytes.Length) {
            int imm = BitConverter.ToUInt16(bytes, rawOff + skip + 1);
            len = skip + 3;
            return string.Format("RET {0}", imm);
        }
        // NOP
        if (op == 0x90) { len = skip + 1; return "NOP"; }
        // PUSH/POP reg (50-5F)
        if (op >= 0x50 && op <= 0x57) { len = skip + 1; return "PUSH " + RegName((op-0x50)+(rexB?8:0), true); }
        if (op >= 0x58 && op <= 0x5F) { len = skip + 1; return "POP " + RegName((op-0x58)+(rexB?8:0), true); }
        // XOR r, r  (33 /r)
        // ADD/SUB/CMP imm8 (83 /x) 
        // MOV r/m, r (89) and MOV r, r/m (8B)
        if ((op == 0x89 || op == 0x8B || op == 0x8D || op == 0x3B || op == 0x39 || op == 0x85 || op == 0x33 || op == 0x03 || op == 0x2B || op == 0x23 || op == 0x0B || op == 0x63) && rawOff + skip + 2 < bytes.Length) {
            byte modrm = bytes[rawOff + skip + 1];
            int mod = (modrm >> 6) & 3;
            int rm_orig = modrm & 7;
            int reg_orig = (modrm >> 3) & 7;
            int regFull = reg_orig + (rexR ? 8 : 0);
            int rmFull = rm_orig + (rexB ? 8 : 0);
            var dec = decodeModrm(rawOff + skip + 1, rawOff + skip + 2, rexW, rexR);
            string[] parts = dec.Item1.Split('|');
            string memStr = parts[0]; int regIdx = int.Parse(parts[1]);
            int dispSz = dec.Item2;
            // SIB adds 1 already in dispSz
            len = skip + 1 + 1 + dispSz + (mod == 3 ? 0 : 0);
            // fixup: if SIB, modrm+sib+disp
            if ((rm_orig == 4) && mod != 3) len++; // extra SIB was included in dispSz for SIB base case, but not always
            string name = rexW ? "Q" : "D";
            if (op == 0x89) return string.Format("MOV{0} {1}, {2}", name, memStr, RegName(regIdx, rexW));
            if (op == 0x8B) return string.Format("MOV{0} {1}, {2}", name, RegName(regIdx, rexW), memStr);
            if (op == 0x8D) return string.Format("LEA {0}, {1}", RegName(regIdx, rexW), memStr);
            if (op == 0x3B) return string.Format("CMP {0}, {1}", RegName(regIdx, rexW), memStr);
            if (op == 0x39) return string.Format("CMP {0}, {1}", memStr, RegName(regIdx, rexW));
            if (op == 0x85) return string.Format("TEST {0}, {1}", memStr, RegName(regIdx, rexW));
            if (op == 0x33) return string.Format("XOR {0}, {1}", RegName(regIdx, rexW), memStr);
            if (op == 0x03) return string.Format("ADD {0}, {1}", RegName(regIdx, rexW), memStr);
            if (op == 0x2B) return string.Format("SUB {0}, {1}", RegName(regIdx, rexW), memStr);
            if (op == 0x23) return string.Format("AND {0}, {1}", RegName(regIdx, rexW), memStr);
            if (op == 0x0B) return string.Format("OR {0}, {1}", RegName(regIdx, rexW), memStr);
            if (op == 0x63) return string.Format("MOVSXD {0}, {1}", RegName(regIdx, true), memStr);
        }
        // MOV r/m, imm (C7 /0)
        if (op == 0xC7 && rawOff + skip + 2 < bytes.Length) {
            byte modrm = bytes[rawOff + skip + 1];
            int mod = (modrm >> 6) & 3;
            int rm_orig = modrm & 7;
            if (((modrm >> 3) & 7) == 0) {
                var dec = decodeModrm(rawOff + skip + 1, rawOff + skip + 2, rexW, false);
                string[] parts = dec.Item1.Split('|');
                string memStr = parts[0];
                int dispSz = dec.Item2;
                int immOff = rawOff + skip + 2 + dispSz + (rm_orig == 4 && mod != 3 ? 1 : 0);
                if (immOff + 3 < bytes.Length) {
                    int imm = BitConverter.ToInt32(bytes, immOff);
                    len = immOff - rawOff + 4;
                    return string.Format("MOV {0}, {1}(0x{2:X8})", memStr, rexW?"QWORD":"",(uint)imm);
                }
            }
        }
        // CALL r/m (FF /2)
        if (op == 0xFF && rawOff + skip + 2 < bytes.Length) {
            byte modrm = bytes[rawOff + skip + 1];
            if (((modrm >> 3) & 7) == 2) {
                int mod = (modrm >> 6) & 3; int rm = modrm & 7 + (rexB?8:0);
                if (mod == 3) { len = skip + 2; return "CALL " + RegName(rm, true); }
                var dec = decodeModrm(rawOff + skip + 1, rawOff + skip + 2, true, false);
                string[] parts = dec.Item1.Split('|');
                len = skip + 2 + dec.Item2 + (rm == 4 && mod != 3 ? 1 : 0);
                return "CALL [" + parts[0].Trim('[',']') + "]";
            }
        }
        // TEST r/m8, imm8 (F6 /0) or TEST r/m32, imm32 (F7 /0)
        if ((op == 0xF6 || op == 0xF7) && rawOff + skip + 2 < bytes.Length) {
            byte modrm = bytes[rawOff + skip + 1];
            if (((modrm >> 3) & 7) == 0) {
                int mod = (modrm >> 6) & 3; int rm = (modrm & 7) + (rexB?8:0);
                if (mod == 3) {
                    int immSz = (op == 0xF6) ? 1 : 4;
                    if (rawOff + skip + 2 + immSz <= bytes.Length) {
                        string imm = op == 0xF6 ? bytes[rawOff+skip+2].ToString("X2") : BitConverter.ToUInt32(bytes,rawOff+skip+2).ToString("X8");
                        string rn = op == 0xF6 ? (rm < 4 ? new[]{"AL","CL","DL","BL"}[rm] : "r8h") : RegName(rm, rexW);
                        len = skip + 2 + immSz; return string.Format("TEST {0}, 0x{1}", rn, imm);
                    }
                }
            }
        }
        // MOV r, imm64 (B8+r for 64-bit)
        if (op >= 0xB8 && op <= 0xBF) {
            int reg = (op - 0xB8) + (rexB ? 8 : 0);
            if (rexW && rawOff + skip + 9 <= bytes.Length) {
                long imm = BitConverter.ToInt64(bytes, rawOff + skip + 1);
                len = skip + 9; return string.Format("MOVABS {0}, 0x{1:X16}", RegName(reg, true), (ulong)imm);
            }
            if (!rexW && rawOff + skip + 5 <= bytes.Length) {
                uint imm = BitConverter.ToUInt32(bytes, rawOff + skip + 1);
                len = skip + 5; return string.Format("MOV {0}, 0x{1:X8}", RegName(reg, false), imm);
            }
        }
        // SUB RSP, imm8 (83 EC xx)
        if (op == 0x83 && rawOff + skip + 3 <= bytes.Length) {
            byte modrm = bytes[rawOff + skip + 1];
            int r = (modrm >> 3) & 7;
            int rm = modrm & 7;
            if ((modrm >> 6) == 3) {
                sbyte imm8 = (sbyte)bytes[rawOff + skip + 2];
                string[] ops83 = {"ADD","OR","ADC","SBB","AND","SUB","XOR","CMP"};
                len = skip + 3; return string.Format("{0} {1}, {2}", ops83[r], RegName(rm+(rexB?8:0), rexW), imm8);
            }
        }
        // SUB/ADD RSP, imm32 (81 /5 or /0)
        if (op == 0x81 && rawOff + skip + 6 <= bytes.Length) {
            byte modrm = bytes[rawOff + skip + 1];
            if ((modrm >> 6) == 3) {
                int r = (modrm >> 3) & 7; int rm = modrm & 7 + (rexB?8:0);
                int imm = BitConverter.ToInt32(bytes, rawOff + skip + 2);
                string[] ops81 = {"ADD","OR","ADC","SBB","AND","SUB","XOR","CMP"};
                len = skip + 6; return string.Format("{0} {1}, 0x{2:X8}", ops81[r], RegName(rm, rexW), (uint)imm);
            }
        }
        // XOR r8, r8 (32)
        if (op == 0x32 && rawOff + skip + 2 <= bytes.Length) {
            byte modrm = bytes[rawOff + skip + 1];
            if ((modrm >> 6) == 3) {
                int r = (modrm >> 3) & 7; int rm = modrm & 7;
                len = skip + 2; return string.Format("XOR8 {0}l, {1}l", RegName(r, false), RegName(rm, false));
            }
        }
        // TEST AL, imm8
        if (op == 0xA8) { len = skip + 2; return string.Format("TEST AL, 0x{0:X2}", bytes[rawOff+skip+1]); }
        // Handle no-op prefix overlap
        len = skip + 1;
        return string.Format("DB 0x{0:X2}", op);
    }

    public static string DumpFunc(byte[] bytes, int funcRva, int funcEnd, int textOff, int textVA, int maxInstr = 200) {
        var sb = new StringBuilder();
        int rva = funcRva;
        int count = 0;
        while (rva < funcEnd && count < maxInstr) {
            int rawOff = textOff + (rva - textVA);
            if (rawOff >= bytes.Length) break;
            int len;
            string decoded = DecodeAt(bytes, rawOff, rva, out len);
            sb.AppendLine(string.Format("  0x{0:X8}  {1}", rva, decoded));
            rva += len;
            count++;
        }
        return sb.ToString();
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
$tOff=[int]$textSec.RawPtr; $tVA=[int]$textSec.VirtualAddress

function Dump-Func([int]$begin,[int]$end,[string]$label,[int]$max=200){
    Write-Output ('=== ' + $label + ' (0x{0:X8}..0x{1:X8}) ===' -f $begin,$end)
    Write-Output ([ByteDumper]::DumpFunc($bytes,$begin,$end,$tOff,$tVA,$max))
}

# Option handler calling 0x003B2E14 twice (BIG_PARSER calls this 2x)
Dump-Func 0x00390FE8 0x003910A4 'opt_handler_0x00390FE8 (calls 0x003B2E14 at 0x00391055, 0x0039107C)'

Write-Output ''
# 0x003B2E14 - the value parser
Dump-Func 0x003B2E14 0x003B2F69 '0x003B2E14_val_parser'

Write-Output ''
# First option handler (0x00390EB0)
Dump-Func 0x00390EB0 0x00390F39 'opt_handler_0x00390EB0'

# Also check function 0x00032EF0 (called 44x by BIG_PARSER — likely string compare)
Write-Output ''
Dump-Func 0x00032EF0 0x00032F71 'str_compare_0x00032EF0 (44 calls from BIG_PARSER)'

# Save results
$out=''; $fns=@(
    @{b=0x00390FE8;e=0x003910A4;l='opt_handler_0x00390FE8'},
    @{b=0x003B2E14;e=0x003B2F69;l='val_parser_0x003B2E14'},
    @{b=0x00390EB0;e=0x00390F39;l='opt_handler_0x00390EB0'},
    @{b=0x00032EF0;e=0x00032F71;l='str_compare_0x00032EF0'}
)
foreach($fn in $fns){
    $out+='=== '+$fn.l+' ==='+"`n"
    $out+=[ByteDumper]::DumpFunc($bytes,$fn.b,$fn.e,$tOff,$tVA)+"`n"
}
$out | Set-Content "$OutDir\disasm_key_funcs.md" -Encoding ascii
Write-Output 'Saved to notes/disasm_key_funcs.md'
