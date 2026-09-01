param(
    [string]$BinPath = 'C:\temp\pm\samples\work\unpacked\PhoenixMiner_6.2c_Windows\PhoenixMiner.exe.bin',
    [string]$OutDir  = 'C:\temp\pm\notes'
)
$ErrorActionPreference = 'Stop'

Add-Type @'
using System; using System.Text;
public class MiniDisasm2 {
    static string[] r64 = { "RAX","RCX","RDX","RBX","RSP","RBP","RSI","RDI","R8","R9","R10","R11","R12","R13","R14","R15" };
    static string[] r32 = { "EAX","ECX","EDX","EBX","ESP","EBP","ESI","EDI","R8D","R9D","R10D","R11D","R12D","R13D","R14D","R15D" };
    
    static string Reg(int i, bool w) { return w ? r64[i & 15] : r32[i & 15]; }

    static int SibExtra(byte modrm, int mod) {
        return ((modrm & 7) == 4 && mod != 3) ? 1 : 0;
    }
    static int DispSize(int mod, byte modrm_rm5) {
        if (mod == 0 && (modrm_rm5 == 5)) return 4; // RIP-relative
        if (mod == 1) return 1;
        if (mod == 2) return 4;
        return 0;
    }

    public static Tuple<string,int> Decode(byte[] b, int off, int rva) {
        if (off >= b.Length) return Tuple.Create("???",1);
        byte b0 = b[off];
        bool rex = b0 >= 0x40 && b0 <= 0x4F;
        bool W = rex && (b0 & 8) != 0, R = rex && (b0 & 4) != 0, X = rex && (b0 & 2) != 0, B = rex && (b0 & 1) != 0;
        int sk = rex ? 1 : 0;
        if (off + sk >= b.Length) return Tuple.Create("REX_ONLY",1+sk);
        byte op = b[off + sk];

        // CALL rel32
        if (op == 0xE8 && off+sk+4 < b.Length) {
            int d = BitConverter.ToInt32(b, off+sk+1);
            long t = rva + sk + 5 + d;
            return Tuple.Create(string.Format("CALL 0x{0:X8}", (uint)t), sk+5);
        }
        // JMP rel32/8
        if (op == 0xE9 && off+sk+4 < b.Length) {
            int d = BitConverter.ToInt32(b, off+sk+1);
            return Tuple.Create(string.Format("JMP 0x{0:X8}", (uint)(rva+sk+5+d)), sk+5);
        }
        if (op == 0xEB && off+sk+1 < b.Length) {
            int d = (sbyte)b[off+sk+1];
            return Tuple.Create(string.Format("JMP8 0x{0:X8}", (uint)(rva+sk+2+d)), sk+2);
        }
        // Jcc rel8
        if ((op >= 0x70 && op <= 0x7F) && off+sk+1 < b.Length) {
            string[] jn = {"JO","JNO","JB","JAE","JZ","JNZ","JBE","JA","JS","JNS","JP","JNP","JL","JGE","JLE","JG"};
            int d = (sbyte)b[off+sk+1];
            return Tuple.Create(string.Format("{0} 0x{1:X8}", jn[op&0xF], (uint)(rva+sk+2+d)), sk+2);
        }
        // 0F 8x Jcc rel32
        if (op == 0x0F && off+sk+5 < b.Length) {
            byte op2 = b[off+sk+1];
            if (op2 >= 0x80 && op2 <= 0x8F) {
                string[] jn = {"JO","JNO","JB","JAE","JZ","JNZ","JBE","JA","JS","JNS","JP","JNP","JL","JGE","JLE","JG"};
                int d = BitConverter.ToInt32(b, off+sk+2);
                return Tuple.Create(string.Format("{0} 0x{1:X8}", jn[op2&0xF], (uint)(rva+sk+6+d)), sk+6);
            }
            // MOVZX / MOVSX
            if ((op2 == 0xB6 || op2 == 0xB7 || op2 == 0xBE || op2 == 0xBF) && off+sk+2 < b.Length) {
                byte mr = b[off+sk+2]; int mod=(mr>>6)&3, rm=mr&7+(B?8:0), reg=(mr>>3)&7+(R?8:0);
                int sib=SibExtra(mr,mod); int dz=DispSize(mod,b[off+sk+2+sib+1<b.Length?(mr):(5)]);
                string mnem = op2 == 0xB6 ? "MOVZX8" : op2 == 0xB7 ? "MOVZX16" : op2 == 0xBE ? "MOVSX8" : "MOVSX16";
                return Tuple.Create(string.Format("{0} {1}, ...", mnem, Reg(reg, W)), sk+2+1+sib+dz);
            }
        }
        // RET
        if (op == 0xC3) return Tuple.Create("RET", sk+1);
        if (op == 0xC2 && off+sk+2 < b.Length) return Tuple.Create("RET "+BitConverter.ToUInt16(b,off+sk+1), sk+3);
        // NOP
        if (op == 0x90) return Tuple.Create("NOP", sk+1);
        // PUSH/POP
        if (op >= 0x50 && op <= 0x57) return Tuple.Create("PUSH "+Reg(op-0x50+(B?8:0),true), sk+1);
        if (op >= 0x58 && op <= 0x5F) return Tuple.Create("POP "+Reg(op-0x58+(B?8:0),true), sk+1);
        // MOV r, imm (B8+r)
        if (op >= 0xB8 && op <= 0xBF) {
            int reg = (op-0xB8)+(B?8:0);
            if (W && off+sk+8 < b.Length) {
                long imm = BitConverter.ToInt64(b,off+sk+1);
                return Tuple.Create(string.Format("MOVABS {0},0x{1:X16}",Reg(reg,true),(ulong)imm), sk+9);
            }
            if (off+sk+4 < b.Length) {
                uint imm = BitConverter.ToUInt32(b,off+sk+1);
                return Tuple.Create(string.Format("MOV {0},0x{1:X8}",Reg(reg,false),imm), sk+5);
            }
        }
        // Helpers for ModRM instructions
        if ((op == 0x89 || op == 0x8B || op == 0x8D || op == 0x8A || op == 0x3B || op == 0x39 || op == 0x85 || 
             op == 0x33 || op == 0x03 || op == 0x2B || op == 0x23 || op == 0x63 || op == 0x0B || op == 0x1B ||
             op == 0x69 || op == 0x6B || op == 0x87) && off+sk+1 < b.Length) {
            byte mr = b[off+sk+1];
            int mod=(mr>>6)&3, rm_raw=mr&7, reg_raw=(mr>>3)&7;
            int rm = rm_raw + (B?8:0), reg = reg_raw + (R?8:0);
            bool hasSib = (rm_raw == 4) && mod != 3;
            int sibOff = off+sk+1+1;
            byte sib = hasSib && sibOff < b.Length ? b[sibOff] : (byte)0;
            int dz = (mod==0 && (rm_raw==5)) ? 4 : (mod==1?1:(mod==2?4:0));
            int sibDz = hasSib ? (((sib&7)==5 && mod==0)?4:0) : 0;
            int totalExtra = 1 + (hasSib?1:0) + dz + sibDz; // modrm + sib? + disp?
            string memStr;
            if (mod == 3) { memStr = Reg(rm, W); }
            else if (mod == 0 && rm_raw == 5) {
                int d = off+sk+totalExtra-4 < b.Length ? BitConverter.ToInt32(b, off+sk+totalExtra-4) : 0;
                long t = rva + sk + 1 + totalExtra + d;
                memStr = string.Format("[RIP+0x{0:X}=>{1:X8}]", d, (uint)t);
            }
            else if (hasSib) {
                int sidx=(sib>>3)&7+(X?8:0), sba=sib&7+(B?8:0), ssc=1<<((sib>>6)&3);
                string sb_s = sba==5&&mod==0 ? string.Format("[0x{0:X}]",BitConverter.ToInt32(b,sibOff+1)) :
                    sidx==4 ? string.Format("[{0}]",Reg(sba,true)) : string.Format("[{0}+{1}*{2}]",Reg(sba,true),Reg(sidx,true),ssc);
                if (mod==1){sbyte d8=(sbyte)b[sibOff+1+sibDz];sb_s=sb_s.TrimEnd(']')+(d8>=0?"+0x":"-0x")+Math.Abs((int)d8).ToString("X")+"]";}
                else if (mod==2){int d32=BitConverter.ToInt32(b,sibOff+1+sibDz);sb_s=sb_s.TrimEnd(']')+(d32>=0?"+0x":"-0x")+Math.Abs(d32).ToString("X")+"]";}
                memStr = sb_s;
            }
            else {
                memStr = "["+Reg(rm,true)+"]";
                if (mod==1){sbyte d8=off+sk+2<b.Length?(sbyte)b[off+sk+2]:(sbyte)0; memStr="["+Reg(rm,true)+(d8>=0?"+0x":"-0x")+Math.Abs((int)d8).ToString("X")+"]";}
                else if (mod==2){int d32=off+sk+5<b.Length?BitConverter.ToInt32(b,off+sk+2):0; memStr="["+Reg(rm,true)+(d32>=0?"+0x":"-0x")+Math.Abs(d32).ToString("X")+"]";}
            }
            string[] ops = { "MOV?","MOV?","MOV?","MOV?","","","","","","" };
            string mnem;
            if (op==0x89) mnem="MOV "+memStr+","+Reg(reg,W);
            else if (op==0x8B) mnem="MOV "+Reg(reg,W)+","+memStr;
            else if (op==0x8D) mnem="LEA "+Reg(reg,W)+","+memStr;
            else if (op==0x3B) mnem="CMP "+Reg(reg,W)+","+memStr;
            else if (op==0x39) mnem="CMP "+memStr+","+Reg(reg,W);
            else if (op==0x85) mnem="TEST "+memStr+","+Reg(reg,W);
            else if (op==0x33) mnem="XOR "+Reg(reg,W)+","+memStr;
            else if (op==0x03) mnem="ADD "+Reg(reg,W)+","+memStr;
            else if (op==0x2B) mnem="SUB "+Reg(reg,W)+","+memStr;
            else if (op==0x23) mnem="AND "+Reg(reg,W)+","+memStr;
            else if (op==0x63) mnem="MOVSXD "+Reg(reg,true)+","+memStr;
            else mnem="OP_"+op.ToString("X2")+" "+memStr+","+Reg(reg,W);
            return Tuple.Create(mnem, sk+1+totalExtra);
        }
        // MOV r/m, imm32 (C7)
        if (op == 0xC7 && off+sk+1 < b.Length) {
            byte mr = b[off+sk+1]; int mod=(mr>>6)&3, rm_raw=mr&7, regf=(mr>>3)&7;
            if (regf == 0) {
                bool hasSib=(rm_raw==4)&&mod!=3;
                int dz=(mod==0&&rm_raw==5)?4:(mod==1?1:(mod==2?4:0));
                int tOff=off+sk+2+(hasSib?1:0)+dz;
                if (tOff+3 < b.Length) {
                    int imm=BitConverter.ToInt32(b,tOff);
                    string memStr; 
                    if (mod==3) memStr=Reg(rm_raw+(B?8:0),W);
                    else if (mod==0&&rm_raw==5){int d=BitConverter.ToInt32(b,off+sk+2);long t=rva+sk+1+1+4+4+d;memStr=string.Format("[RIP=>{0:X8}]",(uint)t);}
                    else if (mod==1){sbyte d8=(sbyte)b[off+sk+2];memStr="["+Reg(rm_raw+(B?8:0),true)+(d8>=0?"+0x":"-0x")+Math.Abs((int)d8).ToString("X")+"]";}
                    else if (mod==2){int d32=BitConverter.ToInt32(b,off+sk+2);memStr="["+Reg(rm_raw+(B?8:0),true)+(d32>=0?"+0x":"-0x")+Math.Abs(d32).ToString("X")+"]";}
                    else memStr="["+Reg(rm_raw+(B?8:0),true)+"]";
                    return Tuple.Create(string.Format("MOV {0},0x{1:X8}",memStr,(uint)imm), tOff-off+4);
                }
            }
        }
        // ADD/SUB/CMP/AND/OR/XOR r/m, imm8/32 (83/81)
        if ((op == 0x83 || op == 0x81) && off+sk+1 < b.Length) {
            byte mr = b[off+sk+1]; int mod=(mr>>6)&3,rm=mr&7+(B?8:0),regf=(mr>>3)&7;
            string[] on83 = {"ADD","OR","ADC","SBB","AND","SUB","XOR","CMP"};
            if (mod == 3) {
                if (op==0x83 && off+sk+2 < b.Length) {
                    sbyte imm=(sbyte)b[off+sk+2];
                    return Tuple.Create(string.Format("{0} {1},{2}",on83[regf],Reg(rm,W),imm), sk+3);
                }
                if (op==0x81 && off+sk+5 < b.Length) {
                    int imm=BitConverter.ToInt32(b,off+sk+2);
                    return Tuple.Create(string.Format("{0} {1},0x{2:X}",on83[regf],Reg(rm,W),(uint)imm), sk+6);
                }
            }
        }
        // CALL/JMP r/m (FF /2 /4)
        if (op == 0xFF && off+sk+1 < b.Length) {
            byte mr = b[off+sk+1]; int mod=(mr>>6)&3,rm=mr&7+(B?8:0),regf=(mr>>3)&7;
            if (mod == 3 && (regf==2||regf==4)) {
                string m = regf==2?"CALL":"JMP";
                return Tuple.Create(m+" "+Reg(rm,true), sk+2);
            }
            if (mod==0 && (mr&7)==5 && off+sk+5 < b.Length) {
                int d=BitConverter.ToInt32(b,off+sk+2); long t=rva+sk+6+d;
                string m = regf==2?"CALL":"JMP";
                return Tuple.Create(string.Format("{0} [RIP=>{1:X8}]",m,(uint)t), sk+6);
            }
            if ((regf==2||regf==4) && off+sk+1 < b.Length) {
                int hasSib=((mr&7)==4&&mod!=3)?1:0;
                int dz=(mod==0&&(mr&7)==5)?4:(mod==1?1:(mod==2?4:0));
                string m=regf==2?"CALL":"JMP";
                if (mod==1){sbyte d8=off+sk+2+hasSib<b.Length?(sbyte)b[off+sk+2+hasSib]:(sbyte)0;return Tuple.Create(string.Format("{0} [{1}+0x{2:X}]",m,Reg(rm,true),d8>=0?(int)d8:-(int)d8),sk+2+hasSib+1);}
                return Tuple.Create(string.Format("{0} [{1}]",m,Reg(rm,true)), sk+2+hasSib+dz);
            }
        }
        // XOR/TEST reg (32/85)
        if ((op == 0x32 || op == 0x30) && off+sk+1 < b.Length) {
            byte mr = b[off+sk+1]; if ((mr>>6)==3) { int r=(mr>>3)&7+(R?8:0),rm=mr&7+(B?8:0); return Tuple.Create(string.Format("XOR {0},{1}",Reg(r,W),Reg(rm,W)),sk+2); }
        }
        // TEST AL/AX/EAX/RAX, imm (A8/A9)
        if (op == 0xA8) return Tuple.Create(string.Format("TEST AL,0x{0:X2}",b[off+sk+1]), sk+2);
        if (op == 0xA9 && off+sk+4 < b.Length) {
            uint imm = BitConverter.ToUInt32(b,off+sk+1);
            return Tuple.Create(string.Format("TEST {0},0x{1:X8}",Reg(0,W),imm), sk+5);
        }
        // IMUL r, r/m, imm
        if (op == 0x6B && off+sk+2 < b.Length) {
            byte mr=b[off+sk+1]; int mod=(mr>>6)&3,rm=mr&7+(B?8:0),reg=(mr>>3)&7+(R?8:0);
            if (mod==3 && off+sk+2 < b.Length) {
                sbyte imm=(sbyte)b[off+sk+2];
                return Tuple.Create(string.Format("IMUL {0},{1},{2}",Reg(reg,W),Reg(rm,W),imm), sk+3);
            }
        }
        // DEC/INC/NEG/NOT (FE/FF/F6/F7 /0-/3) 
        if ((op == 0xFE || op == 0xF6 || op == 0xF7) && off+sk+1 < b.Length) {
            byte mr=b[off+sk+1]; int regf=(mr>>3)&7,rm=mr&7+(B?8:0),mod=(mr>>6)&3;
            string[] fn={"TEST","","NOT","NEG","MUL","IMUL","DIV","IDIV"};
            if (mod==3 && (regf==2||regf==3||regf>=5)) return Tuple.Create(fn[regf]+" "+Reg(rm,W), sk+2);
            if (mod==3 && regf==0 && (op==0xF6||op==0xF7)) {
                if (op==0xF6&&off+sk+2<b.Length) return Tuple.Create(string.Format("TEST {0},0x{1:X2}",Reg(rm,false),b[off+sk+2]),sk+3);
                if (op==0xF7&&off+sk+5<b.Length) return Tuple.Create(string.Format("TEST {0},0x{1:X8}",Reg(rm,W),BitConverter.ToUInt32(b,off+sk+2)),sk+6);
            }
        }
        // SAR/SHR/SHL r, imm8 (C0/C1) or 1 (D0/D1) or CL (D2/D3)
        if ((op == 0xC1 || op == 0xD1 || op == 0xD3) && off+sk+1 < b.Length) {
            byte mr=b[off+sk+1]; int regf=(mr>>3)&7,rm=mr&7+(B?8:0),mod=(mr>>6)&3;
            string[] sn={"ROL","ROR","RCL","RCR","SHL","SHR","SAL","SAR"};
            if (mod==3) {
                if (op==0xC1&&off+sk+2<b.Length) return Tuple.Create(string.Format("{0} {1},{2}",sn[regf],Reg(rm,W),b[off+sk+2]),sk+3);
                if (op==0xD1) return Tuple.Create(string.Format("{0} {1},1",sn[regf],Reg(rm,W)),sk+2);
                if (op==0xD3) return Tuple.Create(string.Format("{0} {1},CL",sn[regf],Reg(rm,W)),sk+2);
            }
        }
        // LEA/MOV rsp-rel prologues (48 8D xx)
        // CDQE/CBW 
        if (op == 0x98) return Tuple.Create(W?"CDQE":"CWDE", sk+1);
        if (op == 0x99) return Tuple.Create(W?"CQO":"CDQ", sk+1);
        // XCHG
        if (op >= 0x91 && op <= 0x97) return Tuple.Create("XCHG "+Reg(0,W)+","+Reg(op-0x90+(B?8:0),W), sk+1);
        // Default
        return Tuple.Create(string.Format("DB 0x{0:X2}{1}", b0, rex?(" /op=0x"+op.ToString("X2")):""), sk==0?1:sk+1);
    }

    public static string Dump(byte[] b, int funcRva, int funcEnd, int textOff, int textVA, int maxInstr=300) {
        var sb = new StringBuilder();
        int rva = funcRva;
        for (int i=0; rva<funcEnd && i<maxInstr; i++) {
            int rawOff = textOff + (rva - textVA);
            var r = Decode(b, rawOff, rva);
            sb.AppendLine(string.Format("  0x{0:X8}  {1}", rva, r.Item1));
            rva += r.Item2;
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

function Dump-Func([int]$b,[int]$e,[string]$lbl,[int]$max=200){
    Write-Output ('=== ' + $lbl + ' (0x{0:X8}..0x{1:X8}) ===' -f $b,$e)
    Write-Output ([MiniDisasm2]::Dump($bytes,$b,$e,$tOff,$tVA,$max))
}

# TR01: 0x001C4010..0x001C44E3 — focus on first ~200 instructions around the [0x007D68F0] read
Dump-Func 0x001C4010 0x001C41A0 'TR01_head_part1'

Write-Output ''
# Also dump the 0x003939B8 function (called by PR02_root_A)
Dump-Func 0x003939B8 0x00393A85 '0x003939B8 (PR02_root_A callee)'

Write-Output ''
# And func 0x003B18EC (called by TR02)
Dump-Func 0x003B18EC 0x003B19C7 'TR02_callee_0x003B18EC'

# Save
$out=''; $fns=@(
    @{b=0x001C4010;e=0x001C41A0;l='TR01_head'},
    @{b=0x003939B8;e=0x00393A85;l='0x003939B8_PR02rootA_callee'},
    @{b=0x003B18EC;e=0x003B19C7;l='TR02_callee'}
)
foreach($fn in $fns){
    $out+='=== '+$fn.l+' ==='+"`n"
    $out+=[MiniDisasm2]::Dump($bytes,$fn.b,$fn.e,$tOff,$tVA)+"`n"
}
$out | Set-Content "$OutDir\tr01_decode.md" -Encoding ascii
Write-Output 'Saved to notes/tr01_decode.md'
