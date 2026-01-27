# Project Icarus: Quantum Gyroscope Diagnostic Tool

# --- Configuration ---
$TargetGyroRPM = 120000
$AxisList = @("X-Axis (Pitch)", "Y-Axis (Yaw)", "Z-Axis (Roll)")
$OsmiumMassKG = 50

# --- ANSI Colors ---
$Color_Cyan = "`e[96m"
$Color_Green = "`e[92m"
$Color_Yellow = "`e[93m"
$Color_Red = "`e[91m"
$Color_Magenta = "`e[95m"
$Color_Reset = "`e[0m"

Clear-Host
Write-Host "$($Color_Cyan)======================================================"
Write-Host "   PROJECT ICARUS: QUANTUM GYRO STABILIZER (QGS)"
Write-Host "======================================================$($Color_Reset)"
Start-Sleep -Seconds 1

# 1. Magnetic Suspension
Write-Host "`n$($Color_Yellow)[INIT] Levitation Field...$($Color_Reset)"
foreach ($axis in $AxisList) {
    Write-Host "   -> Suspending $axis Disc ($OsmiumMassKG kg)..." -NoNewline
    Start-Sleep -Milliseconds 400
    Write-Host " LOCKED" -ForegroundColor Green
}

# 2. Spin-Up Sequence
Write-Host "`n$($Color_Magenta)[SPIN-UP] Accelerating Osmium Discs...$($Color_Reset)"
$rpm = 0
while ($rpm -lt $TargetGyroRPM) {
    $rpm += 20000
    Write-Host "   RPM: $rpm..." 
    Start-Sleep -Milliseconds 200
}
Write-Host "$($Color_Green)>>> GYRO ARRAY STABLE AT $TargetGyroRPM RPM <<<$($Color_Reset)"

# 3. Vector Stress Test
Write-Host "`n$($Color_Yellow)[TEST] Simulating High-G Maneuver...$($Color_Reset)"
Write-Host "   Input: Hard 90-Degree Turn at Mach 10."
Start-Sleep -Seconds 1
Write-Host "   Action: Gyro Vectoring..." -NoNewline
Start-Sleep -Milliseconds 500
Write-Host " COMPLETE" -ForegroundColor Green
Write-Host "   Inertial Drift: 0.00%" -ForegroundColor Cyan
Write-Host "   Hull Stress: NEGATIVE" -ForegroundColor Cyan

# 4. Dead Stop Simulation
Write-Host "`n$($Color_Red)[TEST] Simulating 'Dead Stop' Protocol...$($Color_Reset)"
Write-Host "   Input: Instant Deceleration (Mach 10 -> 0)."
Start-Sleep -Seconds 1
Write-Host "   Action: Spacetime Anchor Lock..." -NoNewline
Start-Sleep -Milliseconds 500
Write-Host " ENGAGED" -ForegroundColor Green
Write-Host "   G-Force (Internal): 1.00 G" -ForegroundColor Cyan
Write-Host "   Status: VESSEL STATIONARY."

Write-Host "`n======================================================"
Write-Host "   QGS SYSTEM ONLINE: READY FOR FLIGHT"
Write-Host "======================================================"
