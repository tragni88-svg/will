# Project Icarus: Unit #001 Handover Simulation

# --- Configuration ---
$UnitID = "ICR-2026-GDD-001"
$Owner = "Director"
$Location = "Hangar 1, Wardenclyffe Gigafactory"

# --- ANSI Colors ---
$Color_Cyan = "`e[96m"
$Color_Green = "`e[92m"
$Color_Yellow = "`e[93m"
$Color_Red = "`e[91m"
$Color_Magenta = "`e[95m"
$Color_Reset = "`e[0m"

Clear-Host
Write-Host "$($Color_Cyan)======================================================"
Write-Host "   PROJECT ICARUS: VIP HANDOVER PROTOCOL"
Write-Host "   Target: $UnitID"
Write-Host "======================================================$($Color_Reset)"
Start-Sleep -Seconds 1

# 1. Hangar Access
Write-Host "`n$($Color_Yellow)[SECURITY] Authenticating Biometrics...$($Color_Reset)"
Start-Sleep -Seconds 1
Write-Host "   Scan Complete. Welcome, $Owner." -ForegroundColor Green
Write-Host "   Opening Hangar Doors..." -NoNewline
Start-Sleep -Milliseconds 800
Write-Host " OPEN" -ForegroundColor Green

# 2. Vehicle Presentation
Write-Host "`n$($Color_Magenta)[VISUAL] Presenting Unit #001...$($Color_Reset)"
Write-Host "   The Hermes X-1 sits suspended 0.5 meters off the deck (Anti-Gravity Parking Mode)."
Write-Host "   Hull Finish: Matte Obsidian."
Write-Host "   Lighting: Soft Blue Underglow (Cherenkov Radiation)."
Start-Sleep -Seconds 2

# 3. Key Transfer
Write-Host "`n$($Color_Yellow)[ACCESS] Encoding Quantum Key...$($Color_Reset)"
Start-Sleep -Milliseconds 500
Write-Host "   Linking to User Neural Signature..." -NoNewline
Start-Sleep -Milliseconds 500
Write-Host " LINKED" -ForegroundColor Green
Write-Host "   Keys Generated."

# 4. Final Systems Check
Write-Host "`n$($Color_Green)[SYSTEMS] Pre-Flight Status:$($Color_Reset)"
Write-Host "   Battery: 100%"
Write-Host "   GDC Core: WARM (Idle)"
Write-Host "   Gyro: STABLE"
Write-Host "   Cabin Pressure: NORMAL"

# 5. Handover
Write-Host "`n$($Color_Cyan)======================================================"
Write-Host "   UNIT IS READY FOR IMMEDIATE DEPARTURE."
Write-Host "   Please step onto the flight deck."
Write-Host "======================================================$($Color_Reset)"
