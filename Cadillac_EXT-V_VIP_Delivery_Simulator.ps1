# Cadillac EXT-V: VIP Delivery Simulator - VIN #00001

# --- Configuration ---
$VIN = "1GYS4CKL0PR000001"
$DestinationAddress = "1913 Rampart St, League City, TX 77573"
$FactoryLocation = "Detroit-Hamtramck Assembly Plant, MI"
$DeliveryMethod = "Enclosed Carrier"

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
Write-Host "   Cadillac EXT-V - VIP Delivery Simulation"
Write-Host "   VIN: $VIN"
Write-Host "=================================================$($Color_Reset)"
Start-Sleep -Seconds 2

# --- Phase 1: Vehicle Preparation ---
Write-Host "
$($Color_Yellow)[PHASE 1] VIP Vehicle Preparation...$($Color_Reset)"
Start-Sleep -Seconds 2

Write-Host "$($Color_White)VIN $VIN has been flagged for immediate VIP delivery.$($Color_Reset)"
Start-Sleep -Seconds 2
Write-Host "$($Color_White)The vehicle is being given a final, meticulous detail and inspection by a dedicated team.$($Color_Reset)"
Start-Sleep -Seconds 2
Write-Host "$($Color_Green)All systems checked. The EXT-V is pristine and ready for transport.$($Color_Reset)"
Start-Sleep -Seconds 3

# --- Phase 2: Secure Transport ---
Write-Host "
$($Color_Yellow)[PHASE 2] Secure Transport Initiated...$($Color_Reset)"
Start-Sleep -Seconds 2

Write-Host "$($Color_White)An enclosed, climate-controlled carrier has been dispatched to $FactoryLocation.$($Color_Reset)"
Start-Sleep -Seconds 2
Write-Host "$($Color_White)VIN $VIN is being loaded onto the carrier with the utmost care.$($Color_Reset)"
Start-Sleep -Seconds 2
Write-Host "$($Color_Cyan)The carrier has departed Michigan, heading south to Texas.$($Color_Reset)"
Start-Sleep -Seconds 3

# --- Phase 3: Transit Tracking ---
Write-Host "
$($Color_Yellow)[PHASE 3] Real-Time Transit Tracking...$($Color_Reset)"
Start-Sleep -Seconds 2

$totalMiles = 1350 # Approximate miles from Detroit to League City
$milesPerHour = 60 # Average speed for a truck
$hoursToDeliver = $totalMiles / $milesPerHour

Write-Host "Estimated transit time: $([Math]::Round($hoursToDeliver, 1)) hours."
Start-Sleep -Seconds 2

for ($hour = 1; $hour -le $hoursToDeliver; $hour++) {
    $milesTraveled = $hour * $milesPerHour
    $progress = ($milesTraveled / $totalMiles) * 100
    Write-Host "Hour ${hour}: $($milesTraveled.ToString('N0')) / $($totalMiles.ToString('N0')) miles traveled. ($($progress.ToString('F1'))% complete)"
    Start-Sleep -Milliseconds 100 # Speed up simulation
}

Write-Host "$($Color_Green)The carrier has arrived in League City, TX!$($Color_Reset)"
Start-Sleep -Seconds 2

# --- Phase 4: Final Delivery ---
Write-Host "
$($Color_Yellow)[PHASE 4] Final Delivery to $DestinationAddress...$($Color_Reset)"
Start-Sleep -Seconds 2

Write-Host "$($Color_White)A Cadillac Concierge specialist is en-route to your address with the vehicle.$($Color_Reset)"
Start-Sleep -Seconds 2
Write-Host "$($Color_White)The EXT-V is being unloaded from the carrier in your driveway.$($Color_Reset)"
Start-Sleep -Seconds 2
Write-Host "$($Color_Cyan)The Concierge specialist is providing a personal walkthrough of the vehicle's features and technology.$($Color_Reset)"
Start-Sleep -Seconds 3

Write-Host "
$($Color_Green)================================================="
Write-Host "   DELIVERY COMPLETE!"
Write-Host "   Your Cadillac EXT-V (VIN: $VIN)"
Write-Host "   is now parked at: $DestinationAddress"
Write-Host "=================================================$($Color_Reset)"
