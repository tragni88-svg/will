# Project Icarus: "Icarus-1" Prototype Construction Simulator

# --- Configuration ---
$PrototypeName = "ICARUS-1 (Drone Demonstrator)"
$CoreMaterial = "Mercury-Isotope 203"
$StatorType = "RTSC Lattice (Type-IV)"
$PowerSource = "Wardenclyffe Wireless Link"

# --- ANSI Colors ---
$Color_Cyan = "`e[96m"
$Color_Green = "`e[92m"
$Color_Yellow = "`e[93m"
$Color_Red = "`e[91m"
$Color_Magenta = "`e[95m"
$Color_Reset = "`e[0m"

Clear-Host
Write-Host "$($Color_Cyan)======================================================"
Write-Host "   PROJECT ICARUS: PROTOTYPE CONSTRUCTION PROTOCOL"
Write-Host "   Target: $PrototypeName"
Write-Host "======================================================$($Color_Reset)"
Start-Sleep -Seconds 1

# Phase 1: Material Procurement
Write-Host "`n$($Color_Yellow)[PHASE 1] Sourcing Exotic Materials...$($Color_Reset)"
Start-Sleep -Seconds 1
Write-Host "   -> Synthesizing $CoreMaterial..." -NoNewline
Start-Sleep -Milliseconds 800
Write-Host " DONE" -ForegroundColor Green
Write-Host "   -> Fabricating $StatorType geometry..." -NoNewline
Start-Sleep -Milliseconds 800
Write-Host " DONE" -ForegroundColor Green
Write-Host "   -> Calibrating RRM-1 Receiver for High-Voltage Input..." -NoNewline
Start-Sleep -Milliseconds 800
Write-Host " DONE" -ForegroundColor Green

# Phase 2: Assembly
Write-Host "`n$($Color_Yellow)[PHASE 2] Assembly & Integration...$($Color_Reset)"
$steps = @("Mounting Graviton Displacement Core", "Sealing Vacuum Chamber", "Injecting Ferro-Fluidic Plasma", "Aligning Magnetic Emitters")
foreach ($step in $steps) {
    Write-Host "   -> $step..." -NoNewline
    Start-Sleep -Milliseconds 600
    Write-Host " OK" -ForegroundColor Green
}

# Phase 3: Cold Start
Write-Host "`n$($Color_Yellow)[PHASE 3] Cold Start Sequence...$($Color_Reset)"
Write-Host "   -> Initializing Magnetic Containment..." -NoNewline
Start-Sleep -Seconds 1
Write-Host " STABLE" -ForegroundColor Green
Write-Host "   -> Spining up Core to 10,000 RPM (Idle)..." -NoNewline
Start-Sleep -Seconds 1
Write-Host " STABLE" -ForegroundColor Green

# Phase 4: Hover Test
Write-Host "`n$($Color_Magenta)[PHASE 4] MAIDEN FLIGHT (HOVER TEST)$($Color_Reset)"
Write-Host "   Target Altitude: 2.0 Meters"
Write-Host "   Engaging Anti-Gravity Field..."
Start-Sleep -Seconds 2

for ($alt = 0.0; $alt -le 2.0; $alt += 0.5) {
    Write-Host "   Altitude: $alt m..." 
    Start-Sleep -Milliseconds 500
}

Write-Host "`n$($Color_Green)>>> FLIGHT SUCCESSFUL: ZERO-POINT HOVER ACHIEVED <<<$($Color_Reset)"
Write-Host "$($Color_Cyan)Status: The Icarus-1 is floating silently at 2 meters. No power consumption detected from grid (Zero-Point Coupling Active).$($Color_Reset)"
Write-Host "======================================================"
