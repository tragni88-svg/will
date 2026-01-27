# Project Icarus: Manufacturing & Production Log

# --- Configuration ---
$TargetUnits = 500 # Initial Production Run
$FactoryLocation = "Wardenclyffe Gigafactory (Nevada Sector)"

# --- ANSI Colors ---
$Color_Cyan = "`e[96m"
$Color_Green = "`e[92m"
$Color_Yellow = "`e[93m"
$Color_Red = "`e[91m"
$Color_Magenta = "`e[95m"
$Color_Reset = "`e[0m"

Clear-Host
Write-Host "$($Color_Cyan)======================================================"
Write-Host "   PROJECT ICARUS: INDUSTRIAL PRODUCTION PROTOCOL"
Write-Host "   Facility: $FactoryLocation"
Write-Host "======================================================$($Color_Reset)"
Start-Sleep -Seconds 1

# 1. Procurement (Global Supply Chain)
Write-Host "`n$($Color_Yellow)[PHASE 1] GLOBAL PROCUREMENT INITIATED...$($Color_Reset)"
$materials = @(
    "Mercury-Isotope 203 (Liquid Plasma)",
    "Yttrium-Barium-Copper-Oxide (Superconductors)",
    "Carbon-Tri-Titanium Weave (Hull)",
    "Quantum Control Chips (NVIDIA Custom)"
)

foreach ($mat in $materials) {
    Write-Host "   -> Sourcing $mat..." -NoNewline
    Start-Sleep -Milliseconds 400
    Write-Host " SECURED" -ForegroundColor Green
}

# 2. Prototype Assembly (Verification)
Write-Host "`n$($Color_Magenta)[PHASE 2] FINAL PROTOTYPE ASSEMBLY (VERIFICATION UNIT)...$($Color_Reset)"
Write-Host "   -> Assembling Core Geometry..." -NoNewline
Start-Sleep -Milliseconds 500
Write-Host " OK" -ForegroundColor Green
Write-Host "   -> Injecting Plasma..." -NoNewline
Start-Sleep -Milliseconds 500
Write-Host " OK" -ForegroundColor Green
Write-Host "   -> Quality Control Check..." -NoNewline
Start-Sleep -Milliseconds 500
Write-Host " PASSED (99.99% Tolerance)" -ForegroundColor Green

# 3. Mass Production Spin-Up
Write-Host "`n$($Color_Yellow)[PHASE 3] SPINNING UP PRODUCTION LINES...$($Color_Reset)"
Start-Sleep -Seconds 1
Write-Host "   -> Activating Robotic Assembly Cells..." -NoNewline
Start-Sleep -Milliseconds 600
Write-Host " ONLINE" -ForegroundColor Green
Write-Host "   -> Synchronizing Conveyor Systems..." -NoNewline
Start-Sleep -Milliseconds 600
Write-Host " ONLINE" -ForegroundColor Green

# 4. Production Run
Write-Host "`n$($Color_Green)[PHASE 4] EXECUTING BATCH RUN ($TargetUnits UNITS)...$($Color_Reset)"
for ($i = 0; $i -le $TargetUnits; $i+=50) {
    Write-Host "   Units Completed: $i / $TargetUnits" 
    Start-Sleep -Milliseconds 100
}

# 5. Deployment
Write-Host "`n$($Color_Cyan)[STATUS] PRODUCTION COMPLETE.$($Color_Reset)"
Write-Host "   Inventory: $TargetUnits Graviton Displacement Drives ready for hull integration."
Write-Host "   Logistics: Loading onto Wardenclyffe Transport Rail."
Write-Host "======================================================"
