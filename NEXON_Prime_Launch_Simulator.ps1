# NEXON Prime: Manufacturing & Launch Day Simulator

# --- Configuration ---
$TotalUnitsForLaunch = 2000000
$ManufacturingRatePerDay = 50000
$ReleaseDate = (Get-Date).AddDays(90) # Set release date 90 days from today

# --- ANSI Colors for Readability ---
$Color_Cyan = "`e[96m"
$Color_Green = "`e[92m"
$Color_Yellow = "`e[93m"
$Color_Red = "`e[91m"
$Color_White = "`e[97m"
$Color_Reset = "`e[0m"

# --- Simulation Start ---
Clear-Host
Write-Host "$($Color_Cyan)================================================="
Write-Host "   NEXON Prime - Manufacturing & Launch Simulation"
Write-Host "=================================================$($Color_Reset)"
Start-Sleep -Seconds 2

# --- Phase 1: Manufacturing ---
Write-Host "
$($Color_Yellow)[PHASE 1] Mass Production Initiated...$($Color_Reset)"
Start-Sleep -Seconds 1

$daysToProduce = $TotalUnitsForLaunch / $ManufacturingRatePerDay
$currentUnits = 0

Write-Host "Manufacturing Target: $($TotalUnitsForLaunch.ToString('N0')) units."
Write-Host "Production Rate: $($ManufacturingRatePerDay.ToString('N0')) units/day."
Write-Host "Estimated Production Time: $daysToProduce days."
Start-Sleep -Seconds 2

for ($day = 1; $day -le $daysToProduce; $day++) {
    $currentUnits += $ManufacturingRatePerDay
    $progress = ($currentUnits / $TotalUnitsForLaunch) * 100
    Write-Host "Day ${day}: $($currentUnits.ToString('N0')) / $($TotalUnitsForLaunch.ToString('N0')) units assembled. ($($progress.ToString('F1'))% complete)"
    Start-Sleep -Milliseconds 100 # Speed up simulation
}

Write-Host "$($Color_Green)Manufacturing complete. All launch units are ready for distribution.$($Color_Reset)"
Start-Sleep -Seconds 2

# --- Phase 2: Pre-Launch Hype ---
Write-Host "
$($Color_Yellow)[PHASE 2] Pre-Launch Sequence...$($Color_Reset)"
Start-Sleep -Seconds 1

Write-Host "$($Color_Cyan)NEXON announces official release date: $($ReleaseDate.ToString('D'))$($Color_Reset)"
Start-Sleep -Seconds 2
Write-Host "$($Color_White)Pre-orders go live worldwide... and sell out in 15 minutes.$($Color_Reset)"
Start-Sleep -Seconds 2
Write-Host "$($Color_White)Logistics network activated. Units shipping to distribution centers globally.$($Color_Reset)"
Start-Sleep -Seconds 3

# --- Phase 3: Launch Day ---
Write-Host "
$($Color_Yellow)[PHASE 3] LAUNCH DAY - $($ReleaseDate.ToString('D'))$($Color_Reset)"
Start-Sleep -Seconds 2

Write-Host "$($Color_White)Midnight launches begin in Australia and Japan...$($Color_Reset)"
Start-Sleep -Seconds 2

$initialSales = 0
$launchDayTarget = $TotalUnitsForLaunch * 0.75 # Simulate 75% sell-through on day 1

while ($initialSales -lt $launchDayTarget) {
    $burst = Get-Random -Minimum 50000 -Maximum 150000
    $initialSales += $burst
    if ($initialSales -gt $launchDayTarget) { $initialSales = $launchDayTarget }
    $percentageSold = ($initialSales / $launchDayTarget) * 100
    Write-Host "$($Color_Green)Sales Update: $($initialSales.ToString('N0')) units sold... ($($percentageSold.ToString('F1'))% of Day 1 stock)"
    Start-Sleep -Milliseconds 200
}

Write-Host "
$($Color_Green)Initial Launch Day Allocation SOLD OUT!$($Color_Reset)"
Start-Sleep -Seconds 1
Write-Host "$($Color_White)Players are logging into PrimeOS for the first time...$($Color_Reset)"
Start-Sleep -Seconds 1
Write-Host "$($Color_White)Servers for 'Counter-Strike 3' are at maximum capacity.$($Color_Reset)"
Start-Sleep -Seconds 2

# --- Phase 4: Post-Launch ---
Write-Host "
$($Color_Yellow)[PHASE 4] The First 24 Hours...$($Color_Reset)"
Start-Sleep -Seconds 1
Write-Host "$($Color_Cyan)Review Embargo Lifts...$($Color_Reset)"
Start-Sleep -Seconds 2
Write-Host "$($Color_White)IGN: 'A true generational leap. 9.8/10'"
Write-Host "$($Color_White)GameSpot: 'The 10K promise is real. NEXON has a winner. 9.5/10'"
Write-Host "$($Color_White)Digital Foundry: 'The most powerful console ever made. A new benchmark.'"
Start-Sleep -Seconds 4

Write-Host "
$($Color_Green)================================================="
Write-Host "   NEXON Prime Launch: A Resounding Success"
Write-Host "=================================================$($Color_Reset)"
