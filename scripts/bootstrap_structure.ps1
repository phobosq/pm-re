param([string]$Root='C:\temp\pm')
$ErrorActionPreference='Stop'
New-Item -ItemType Directory -Force -Path "$Root\samples\original","$Root\samples\work","$Root\hashes","$Root\inventory","$Root\strings","$Root\imports","$Root\ghidra","$Root\ida","$Root\traces\api","$Root\traces\ioctls","$Root\traces\mmio","$Root\registers","$Root\notes","$Root\hypotheses","$Root\scripts","$Root\reports" | Out-Null
Write-Host 'Project structure ensured at' $Root

