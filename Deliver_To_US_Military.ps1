# Project Icarus: Military Handover Simulation

# --- Configuration ---
$DeliveryTarget = "Wright-Patterson AFB (Hangar 18)"
$Payload = "Icarus-V 'Vanguard' Prototype (Unit #002)"
$Escort = "2x F-22 Raptor (USAF)"

# --- ANSI Colors ---
$Color_Cyan = "`e[96m"
$Color_Green = "`e[92m"
$Color_Yellow = "`e[93m"
$Color_Red = "`e[91m"
$Color_Magenta = "`e[95m"
$Color_Reset = "`e[0m"

Clear-Host
Write-Host "$($Color_Cyan)======================================================"
Write-Host "   OPERATION: PROMETHEUS (Technology Transfer)"
Write-Host "   Payload: $Payload"
Write-Host "======================================================$($Color_Reset)"
Start-Sleep -Seconds 1

# 1. Departure
Write-Host "`n$($Color_Yellow)[DEPARTURE] Wardenclyffe Pad A...$($Color_Reset)"
Write-Host "   Vanguard Unit Spooling Up..." -NoNewline
Start-Sleep -Milliseconds 500
Write-Host " ONLINE" -ForegroundColor Green
Write-Host "   Stealth Mode: ENGAGED (Radar Cross Section: 0.00)"
Write-Host "   Pilot: Test Pilot 'Maverick'"

# 2. Transit
Write-Host "`n$($Color_Magenta)[TRANSIT] En Route to Ohio Sector...$($Color_Reset)"
Write-Host "   Altitude: 80,000 ft"
Write-Host "   Speed: Mach 5 (Cruising)"
Start-Sleep -Seconds 1
Write-Host "   Intercept Detected: $Escort"
Write-Host "   IFF Transponder: 'FRIENDLY' - Signal Sent." -ForegroundColor Green
Write-Host "   Escort Status: FORMATION LOCKED."

# 3. Arrival
Write-Host "`n$($Color_Yellow)[ARRIVAL] Wright-Patterson Airspace...$($Color_Reset)"
Write-Host "   ATC: 'Unidentified craft, you are cleared for landing on Runway 22L. Welcome to Earth, over.'"
Write-Host "   Vanguard: 'Solid copy. Engaging VTOL mode.'"
Start-Sleep -Seconds 1
Write-Host "   Descent Rate: 50 m/s..." -NoNewline
Start-Sleep -Milliseconds 500
Write-Host " TOUCHDOWN" -ForegroundColor Green

# 4. Handover
Write-Host "`n$($Color_Cyan)[HANDOVER] Hangar 18 Secure Facility...$($Color_Reset)"
Write-Host "   General [REDACTED] approaching."
Write-Host "   Boeing Engineering Team standing by."
Start-Sleep -Seconds 1
Write-Host "   Transferring Control Codes..." -NoNewline
Start-Sleep -Milliseconds 800
Write-Host " COMPLETE" -ForegroundColor Green

Write-Host "`n======================================================"
Write-Host "   MISSION SUCCESS: ASSET DELIVERED TO US MILITARY"
Write-Host "======================================================"
