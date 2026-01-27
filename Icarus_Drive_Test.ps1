# Project Icarus: Graviton Displacement Drive Test Protocol

# --- Configuration ---
$TargetRPM = 60000
$RequiredPowerGW = 1.21
$CoreTempLimit = 2500 # Kelvin

# --- ANSI Colors ---
$Color_Cyan = "`e[96m"
$Color_Green = "`e[92m"
$Color_Yellow = "`e[93m"
$Color_Red = "`e[91m"
$Color_Magenta = "`e[95m"
$Color_Reset = "`e[0m"

Clear-Host
Write-Host "$($Color_Cyan)======================================================"
Write-Host "   PROJECT ICARUS: GRAVITON DRIVE DIAGNOSTICS"
Write-Host "======================================================$($Color_Reset)"
Start-Sleep -Seconds 1

# 1. Power Injection
Write-Host "`n$($Color_Yellow)[SYSTEM] Connecting to Wardenclyffe Grid...$($Color_Reset)"
for ($i = 0; $i -le 100; $i+=20) {
    Write-Host "      Power Level: $i%..." -NoNewline
    Start-Sleep -Milliseconds 400
    Write-Host " OK" -ForegroundColor Green
}
Write-Host "$($Color_Green)>>> POWER STABLE at $RequiredPowerGW GW <<<$($Color_Reset)"

# 2. Spin Up
Write-Host "`n$($Color_Yellow)[SYSTEM] Spun-up Mercury Plasma Torus...$($Color_Reset)"
$rpm = 0
while ($rpm -lt $TargetRPM) {
    $rpm += 5000
    Write-Host "      RPM: $rpm..." 
    Start-Sleep -Milliseconds 200
}
Write-Host "$($Color_Green)>>> CORE SYNCHRONIZED ($TargetRPM RPM) <<<$($Color_Reset)"

# 3. Field Generation
Write-Host "`n$($Color_Magenta)[PHYSICS] Initiating Higgs Field Displacement...$($Color_Reset)"
Start-Sleep -Seconds 1
Write-Host "      Distortion: 5%..." -ForegroundColor DarkGray
Start-Sleep -Milliseconds 500
Write-Host "      Distortion: 25%..." -ForegroundColor DarkGray
Start-Sleep -Milliseconds 500
Write-Host "      Distortion: 50%..." -ForegroundColor DarkGray
Start-Sleep -Milliseconds 500
Write-Host "      Distortion: 85%..." -ForegroundColor White
Start-Sleep -Milliseconds 500
Write-Host "      Distortion: 100%..." -ForegroundColor White

# 4. Levitation Check
Write-Host "`n$($Color_Cyan)[STATUS] ENGAGING ANTI-GRAVITY CLAMPS$($Color_Reset)"
Start-Sleep -Seconds 1
Write-Host "$($Color_Green)      WEIGHT: 0.00 KG (MASS NULLIFIED)"
Write-Host "      LIFT: POSITIVE"
Write-Host "      STABILITY: 100%$($Color_Reset)"

Write-Host "`n======================================================"
Write-Host "   TEST SUCCESSFUL: OBJECT IS FLOATING"
Write-Host "======================================================"
