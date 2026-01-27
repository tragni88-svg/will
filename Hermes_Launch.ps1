# Project Icarus: "Hermes X-1" Maiden Voyage Simulation

# --- Configuration ---
$MissionName = "ICARUS-FLIGHT-01"
$Crew = @("Cmdr. Shepard", "Lt. Ripley", "Dr. Freeman", "Eng. Stark")
$TargetOrbit = "LEO (400km)"

# --- ANSI Colors ---
$Color_Cyan = "`e[96m"
$Color_Green = "`e[92m"
$Color_Yellow = "`e[93m"
$Color_Red = "`e[91m"
$Color_Magenta = "`e[95m"
$Color_Reset = "`e[0m"

Clear-Host
Write-Host "$($Color_Cyan)======================================================"
Write-Host "   MISSION CONTROL: HERMES X-1 LAUNCH SEQUENCE"
Write-Host "   Commander: $($Crew[0])"
Write-Host "======================================================$($Color_Reset)"
Start-Sleep -Seconds 1

# 1. Pre-Flight
Write-Host "`n$($Color_Yellow)[PRE-FLIGHT] System Check...$($Color_Reset)"
Write-Host "   -> Fusion Reactor Ignition..." -NoNewline
Start-Sleep -Seconds 1
Write-Host " ONLINE (3.5 GW)" -ForegroundColor Green
Write-Host "   -> Graviton Core 1 (Port)..." -NoNewline
Start-Sleep -Milliseconds 500
Write-Host " SYNCED" -ForegroundColor Green
Write-Host "   -> Graviton Core 2 (Starboard)..." -NoNewline
Start-Sleep -Milliseconds 500
Write-Host " SYNCED" -ForegroundColor Green
Write-Host "   -> Inertial Dampeners..." -NoNewline
Start-Sleep -Milliseconds 500
Write-Host " ACTIVE (1.0 G)" -ForegroundColor Green

# 2. Launch
Write-Host "`n$($Color_Magenta)[LAUNCH] Initiating Vertical Takeoff...$($Color_Reset)"
Start-Sleep -Seconds 1
Write-Host "   3... 2... 1... ENGAGE." -ForegroundColor White
Start-Sleep -Milliseconds 500

for ($alt = 0; $alt -le 10000; $alt += 2000) {
    Write-Host "   Altitude: $alt meters | Vel: 0 m/s (Hovering)" 
    Start-Sleep -Milliseconds 200
}
Write-Host "$($Color_Green)>>> CLEAR OF TOWER. TRANSITIONING TO ASCENT MODE. <<<$($Color_Reset)"

# 3. Ascent
Write-Host "`n$($Color_Yellow)[ASCENT] Punching it...$($Color_Reset)"
$velocity = 0
for ($i = 0; $i -le 10; $i++) {
    $velocity += 500
    Write-Host "   Velocity: $velocity m/s | G-Force (Hull): $(($i+1))G | G-Force (Crew): 1.0G"
    Start-Sleep -Milliseconds 300
}

Write-Host "`n$($Color_Cyan)[STATUS] PASSING KARMAN LINE (100km). ENTRIES SPACE.$($Color_Reset)"
Start-Sleep -Seconds 1
Write-Host "   Atmospheric Friction: NONE (Field Active)" -ForegroundColor DarkGray
Write-Host "   Sonic Boom: NONE (Suppressed)" -ForegroundColor DarkGray

# 4. Orbit
Write-Host "`n$($Color_Green)[ORBIT] Orbit Achieved: 400km Stable.$($Color_Reset)"
Write-Host "   Crew Status: GREEN"
Write-Host "   Hull Integrity: 100%"
Write-Host "   Fuel Remaining: 99.8%"

# 5. Lunar Flyby Simulation
Write-Host "`n$($Color_Magenta)[COURSE PLOT] Setting course for Lunar Flyby...$($Color_Reset)"
Write-Host "   Accelerating to 0.1c..."
Start-Sleep -Seconds 2
Write-Host "   ... [TIME DILATION SKIPPED] ..."
Write-Host "   Lunar Orbit Established." -ForegroundColor Green
Write-Host "   Capturing High-Res Surface Data..." -NoNewline
Start-Sleep -Seconds 1
Write-Host " DONE" -ForegroundColor Green

# 6. Return
Write-Host "`n$($Color_Yellow)[RETURN] De-orbiting...$($Color_Reset)"
Write-Host "   Engaging Gravity Braking..."
Start-Sleep -Seconds 1
Write-Host "   Touchdown at Wardenclyffe Pad A." -ForegroundColor Green

Write-Host "`n======================================================"
Write-Host "   MISSION SUCCESSFUL: MANNED ANTI-GRAVITY FLIGHT"
Write-Host "======================================================"
