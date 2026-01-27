# Cadillac EXT-V: Supply Chain & Sourcing Simulator

# --- Configuration ---
$TotalUnitsToBuild = 100000
$DailyProductionTarget = 500
$TotalPartsPerVehicle = 30000 # Approximate

# --- ANSI Colors ---
$Color_Cyan = "`e[96m"
$Color_Green = "`e[92m"
$Color_Yellow = "`e[93m"
$Color_Red = "`e[91m"
$Color_White = "`e[97m"
$Color_Reset = "`e[0m"

# --- Simulation Start ---
Clear-Host
Write-Host "$($Color_Cyan)================================================="
Write-Host "   Cadillac EXT-V - Supply Chain & Sourcing Simulation"
Write-Host "=================================================$($Color_Reset)"
Start-Sleep -Seconds 2

# --- Phase 1: Global Sourcing ---
Write-Host "
$($Color_Yellow)[PHASE 1] Initiating Global Supply Chain...$($Color_Reset)"
Start-Sleep -Seconds 2

Write-Host "$($Color_White)Sourcing 6.2L Supercharged V8 engines from GM's Performance Build Center in Bowling Green, KY...$($Color_Reset)"
Start-Sleep -Seconds 2
Write-Host "$($Color_White)Procuring 38-inch OLED displays from LG Display in South Korea...$($Color_Reset)"
Start-Sleep -Seconds 2
Write-Host "$($Color_White)Securing 36-speaker AKG audio systems from Austria...$($Color_Reset)"
Start-Sleep -Seconds 2
Write-Host "$($Color_White)Ordering high-strength aluminum from Alcoa for the bed and body panels...$($Color_Reset)"
Start-Sleep -Seconds 2
Write-Host "$($Color_Green)All critical suppliers are locked in. Supply chain is stable.$($Color_Reset)"
Start-Sleep -Seconds 3

# --- Phase 2: Just-In-Time Logistics ---
Write-Host "
$($Color_Yellow)[PHASE 2] Just-In-Time Logistics...$($Color_Reset)"
Start-Sleep -Seconds 2

Write-Host "$($Color_White)Parts are being shipped to the Detroit-Hamtramck Assembly Plant (Factory ZERO).$($Color_Reset)"
Start-Sleep -Seconds 2
Write-Host "$($Color_White)Automated Guided Vehicles (AGVs) are moving parts to the assembly line as needed.$($Color_Reset)"
Start-Sleep -Seconds 2
Write-Host "$($Color_Green)Inventory management is optimized. No bottlenecks detected.$($Color_Reset)"
Start-Sleep -Seconds 3

# --- Phase 3: Assembly Line Start ---
Write-Host "
$($Color_Yellow)[PHASE 3] Assembly Line Start-Up...$($Color_Reset)"
Start-Sleep -Seconds 2

$totalPartsNeeded = $TotalUnitsToBuild * $TotalPartsPerVehicle
$partsDelivered = 0
$dailyPartsDelivery = $DailyProductionTarget * $TotalPartsPerVehicle

Write-Host "Target Production: $($TotalUnitsToBuild.ToString('N0')) vehicles."
Write-Host "Daily Production Target: $($DailyProductionTarget.ToString('N0')) vehicles."
Write-Host "Total Parts to Deliver: $($totalPartsNeeded.ToString('N0'))."
Start-Sleep -Seconds 2

for ($day = 1; $day -le ($TotalUnitsToBuild / $DailyProductionTarget); $day++) {
    $partsDelivered += $dailyPartsDelivery
    $vehiclesAssembled = $day * $DailyProductionTarget
    $progress = ($vehiclesAssembled / $TotalUnitsToBuild) * 100
    Write-Host "Day ${day}: $($vehiclesAssembled.ToString('N0')) / $($TotalUnitsToBuild.ToString('N0')) vehicles assembled. ($($progress.ToString('F1'))% complete)"
    Start-Sleep -Milliseconds 50 # Speed up simulation
}

Write-Host "
$($Color_Green)Production target achieved! All $($TotalUnitsToBuild.ToString('N0')) units are ready for shipment.$($Color_Reset)"
Start-Sleep -Seconds 2

# --- Phase 4: Quality Control ---
Write-Host "
$($Color_Yellow)[PHASE 4] Quality Control & Final Inspection...$($Color_Reset)"
Start-Sleep -Seconds 2

Write-Host "$($Color_White)Each EXT-V undergoes a 1000-point inspection...$($Color_Reset)"
Start-Sleep -Seconds 2
Write-Host "$($Color_White)Road tests confirm 0-60 mph in 4.2 seconds for the V-Series model.$($Color_Reset)"
Start-Sleep -Seconds 2
Write-Host "$($Color_Green)All vehicles pass final inspection. Quality is flawless.$($Color_Reset)"
