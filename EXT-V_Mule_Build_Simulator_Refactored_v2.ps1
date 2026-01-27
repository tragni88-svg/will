param(
    [int]$SimulationSpeed = 2,
    [int]$StartWeek = 1,
    [int]$EndWeek = 32
)

# Cadillac EXT-V Mule Build Simulator - Refactored Version
# Real-time prototype validation program simulation

#region Weekly Event Functions

function Invoke-Week1 {
    param($Metrics)
    Write-Host '[BUILD] INITIATING ALPHA BUILD' -ForegroundColor Green
    Write-Host '-> Securing Silverado chassis for modification' -ForegroundColor Cyan
    Write-Host '-> LT4 crate engine procurement initiated' -ForegroundColor Cyan
}

function Invoke-Week4 {
    param($Metrics)
    Write-Host '[ALPHA MULE 1] Chassis modification complete' -ForegroundColor Green
    Write-Host '[OK] Tonawanda delivered LT4 V8 Engine on schedule' -ForegroundColor Green
}

function Invoke-Week8 {
    param($Metrics)
    Write-Host '[SYSTEM] POWERTRAIN INTEGRATION' -ForegroundColor Green
    $testPassed = (Get-Random -Minimum 1 -Maximum 100) -le 88
    if ($testPassed) {
        Write-Host '[OK] LT4_Powertrain testing passed' -ForegroundColor Green
    } else {
        Write-Host '[FAIL] LT4_Powertrain testing failed - rework required' -ForegroundColor Red
        $Metrics.criticalIssues++
    }
}

function Invoke-Week12 {
    param($Metrics)
    Write-Host '[COMPLETE] ALPHA PHASE COMPLETE' -ForegroundColor Green
    Write-Host '-> 4 Alpha mules operational' -ForegroundColor Cyan
    Write-Host '-> Beta build authorization granted' -ForegroundColor Cyan
}

function Invoke-Week13 {
    param($Metrics)
    Write-Host '[BETA] BETA BUILD INITIATION' -ForegroundColor Green
    Write-Host '-> Production-intent chassis preparation' -ForegroundColor Cyan
    Write-Host '-> Carbon fiber bed prototype development' -ForegroundColor Cyan
}

function Invoke-Week16 {
    param($Metrics)
    Write-Host '[PROTOTYPE] CARBON FIBER BED PROTOTYPE' -ForegroundColor Green
    $deliverySuccess = (Get-Random -Minimum 1 -Maximum 100) -le 85
    if ($deliverySuccess) {
        Write-Host '[OK] Plasan delivered Carbon Fiber Bed on schedule' -ForegroundColor Green
    } else {
        Write-Host '[WARN] Plasan delayed Carbon Fiber Bed by 1 week' -ForegroundColor Yellow
        $Metrics.supplierDelays++
    }
}

function Invoke-Week17 {
    param($Metrics)
    Write-Host '[DISPLAY] OLED DISPLAY INTEGRATION' -ForegroundColor Green
    $deliverySuccess = (Get-Random -Minimum 1 -Maximum 100) -le 90
    if ($deliverySuccess) {
        Write-Host '[OK] LG Display delivered 38-inch OLED on schedule' -ForegroundColor Green
    } else {
        Write-Host '[WARN] LG Display delayed 38-inch OLED by 1 week' -ForegroundColor Yellow
        $Metrics.supplierDelays++
    }
}

function Invoke-Week18 {
    param($Metrics)
    Write-Host '[TEST] OLED THERMAL TESTING' -ForegroundColor Green
    $testPassed = (Get-Random -Minimum 1 -Maximum 100) -le 82
    if ($testPassed) {
        Write-Host '[OK] OLED_Thermal testing passed' -ForegroundColor Green
    } else {
        Write-Host '[FAIL] OLED_Thermal testing failed - rework required' -ForegroundColor Red
        $Metrics.criticalIssues++
    }
}

function Invoke-Week20 {
    param($Metrics)
    Write-Host '[TEST] CARBON FIBER STRUCTURAL TESTING' -ForegroundColor Green
    $testPassed = (Get-Random -Minimum 1 -Maximum 100) -le 85
    if ($testPassed) {
        Write-Host '[OK] Carbon_Fiber testing passed' -ForegroundColor Green
    } else {
        Write-Host '[FAIL] Carbon_Fiber testing failed - rework required' -ForegroundColor Red
        $Metrics.criticalIssues++
    }
}

function Invoke-Week24 {
    param($Metrics)
    Write-Host '[COMPLETE] BETA PHASE COMPLETE' -ForegroundColor Green
    Write-Host '-> 6 Beta mules with key technologies' -ForegroundColor Cyan
    Write-Host '-> RC authorization pending review' -ForegroundColor Cyan
}

function Invoke-Week25 {
    param($Metrics)
    Write-Host '[RC] RELEASE CANDIDATE BUILD' -ForegroundColor Green
    Write-Host '-> Production tooling components' -ForegroundColor Cyan
    Write-Host '-> Final supplier integration' -ForegroundColor Cyan
}

function Invoke-Week28 {
    param($Metrics)
    Write-Host '[VALIDATION] FINAL VALIDATION TESTING' -ForegroundColor Green
    $testPassed = (Get-Random -Minimum 1 -Maximum 100) -le 95
    if ($testPassed) {
        Write-Host '[OK] Crash_Simulation testing passed' -ForegroundColor Green
    } else {
        Write-Host '[FAIL] Crash_Simulation testing failed - rework required' -ForegroundColor Red
        $Metrics.criticalIssues++
    }
}

function Invoke-Week30 {
    param($Metrics)
    Write-Host '[PROD] PRODUCTION READINESS ASSESSMENT' -ForegroundColor Green
    Write-Host '-> Assembly process validation' -ForegroundColor Cyan
    Write-Host '-> Supplier quality verification' -ForegroundColor Cyan
}

function Invoke-Week32 {
    param($Metrics)
    Write-Host '[TARGET] PROGRAM COMPLETE' -ForegroundColor Green
    Write-Host '-> Production authorization (Job #1)' -ForegroundColor Green
    Write-Host '-> 3 RC vehicles validated' -ForegroundColor Green
}

#endregion

#region Main Simulation Logic

Write-Host '+--------------------------------------------------------------------+' -ForegroundColor Blue
Write-Host '|    CADILLAC EXT-V MULE VEHICLE BUILD PROGRAM - LIVE SIMULATION     |' -ForegroundColor Blue
Write-Host '+--------------------------------------------------------------------+' -ForegroundColor Blue
Write-Host "Program: `$39.5M prototype validation - 13 mule vehicles - 32-week timeline" -ForegroundColor Cyan

# Initialize program metrics
$Metrics = @{
    vehiclesBuilt = 0
    testsCompleted = 0
    budgetSpent = 0.0
    criticalIssues = 0
    supplierDelays = 0
}

for ($week = $StartWeek; $week -le $EndWeek; $week++) {
    
    Write-Host "`n[WEEK $week]" -ForegroundColor Yellow
    Write-Host '-----------------------------------------------------------------------' -ForegroundColor Blue
    
    # Update metrics
    $Metrics.progress = [math]::Round(($week / 32) * 100, 1)
    $Metrics.vehiclesBuilt = [math]::Floor(($week / 32) * 13)
    $Metrics.testsCompleted = [math]::Floor(($week / 32) * 45)
    
    # Simulate budget burn
    $weeklyBurn = Get-Random -Minimum 1.0 -Maximum 1.5
    $Metrics.budgetSpent = [math]::Round($Metrics.budgetSpent + $weeklyBurn, 1)
    
    # Show progress
    Write-Host "Program Progress: $($Metrics.progress)%" -ForegroundColor Green
    Write-Host "Budget Spent: `$($Metrics.budgetSpent)M / `$39.5M" -ForegroundColor Green
    
    # Weekly activities based on week number
    $functionName = "Invoke-Week$week"
    if (Get-Command $functionName -ErrorAction SilentlyContinue) {
        & $functionName -Metrics $Metrics
    }
    
    # Show weekly metrics
    Write-Host "`n[STATUS] PROGRAM STATUS:" -ForegroundColor Yellow
    Write-Host "-> Vehicles Built: $($Metrics.vehiclesBuilt)/13" -ForegroundColor Cyan
    Write-Host "-> Tests Completed: $($Metrics.testsCompleted)/45" -ForegroundColor Cyan
    Write-Host "-> Critical Issues: $($Metrics.criticalIssues)" -ForegroundColor $(if($Metrics.criticalIssues -gt 3){"Red"} else {"Cyan"})
    Write-Host "-> Supplier Delays: $($Metrics.supplierDelays)" -ForegroundColor $(if($Metrics.supplierDelays -gt 5){"Yellow"} else {"Cyan"})
    
    # Simulation delay
    Start-Sleep -Milliseconds (500 / $SimulationSpeed)
}

# Final program summary
Write-Host "`n+--------------------------------------------------------------------+" -ForegroundColor Blue
Write-Host '|                    PROGRAM COMPLETION SUMMARY                      |' -ForegroundColor Blue
Write-Host '+--------------------------------------------------------------------+' -ForegroundColor Blue

Write-Host "[METRICS] FINAL METRICS:" -ForegroundColor Yellow
Write-Host "-> Overall Progress: 100%" -ForegroundColor Green
Write-Host "-> Total Vehicles Built: $($Metrics.vehiclesBuilt)/13" -ForegroundColor Cyan
Write-Host "-> Total Tests Completed: $($Metrics.testsCompleted)/45" -ForegroundColor Cyan
Write-Host "-> Budget Utilization: `$($Metrics.budgetSpent)M / `$39.5M" -ForegroundColor Cyan
Write-Host "-> Critical Issues Resolved: $($Metrics.criticalIssues)" -ForegroundColor $(if($Metrics.criticalIssues -le 5){"Green"} else {"Red"})
Write-Host "-> Supplier Performance: $($Metrics.supplierDelays) delays" -ForegroundColor $(if($Metrics.supplierDelays -le 3){"Green"} else {"Yellow"})

Write-Host "`n[TARGET] PRODUCTION READINESS STATUS:" -ForegroundColor Yellow
$readinessScore = [math]::Round(100 - ($Metrics.criticalIssues * 3) - ($Metrics.supplierDelays * 2), 0)
Write-Host "-> Production Readiness Score: $readinessScore%" -ForegroundColor $(if($readinessScore -ge 85){"Green"} elseif($readinessScore -ge 70){"Yellow"} else {"Red"})

if ($readinessScore -ge 85)
{
    Write-Host '[OK] PROGRAM READY FOR PRODUCTION AUTHORIZATION' -ForegroundColor Green
}
else
{
    Write-Host 'WARNING: ADDITIONAL VALIDATION REQUIRED BEFORE PRODUCTION' -ForegroundColor Yellow
}

#endregion
