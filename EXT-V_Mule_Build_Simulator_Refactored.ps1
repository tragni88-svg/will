# Cadillac EXT-V Mule Build Simulator - Refactored Version
# Real-time prototype validation program simulation

param(
    [int]$SimulationSpeed = 2,
    [int]$StartWeek = 1,
    [int]$EndWeek = 32
)

Write-Host "╔══════════════════════════════════════════════════════════════════════╗" -ForegroundColor Blue
Write-Host "║    CADILLAC EXT-V MULE VEHICLE BUILD PROGRAM - LIVE SIMULATION     ║" -ForegroundColor Blue
Write-Host "╚══════════════════════════════════════════════════════════════════════╝" -ForegroundColor Blue
Write-Host "Program: `$39.5M prototype validation - 13 mule vehicles - 32-week timeline" -ForegroundColor Cyan

# Initialize program metrics
$vehiclesBuilt = 0
$testsCompleted = 0
$budgetSpent = 0.0
$criticalIssues = 0
$supplierDelays = 0

for ($week = $StartWeek; $week -le $EndWeek; $week++) {
    
    Write-Host "`n📅 WEEK $week" -ForegroundColor Yellow
    Write-Host "═══════════════════════════════════════════════════════════════════════" -ForegroundColor Blue
    
    # Update metrics
    $progress = [math]::Round(($week / 32) * 100, 1)
    $vehiclesBuilt = [math]::Floor(($week / 32) * 13)
    $testsCompleted = [math]::Floor(($week / 32) * 45)
    
    # Simulate budget burn
    $weeklyBurn = Get-Random -Minimum 1.0 -Maximum 1.5
    $budgetSpent = [math]::Round($budgetSpent + $weeklyBurn, 1)
    
    # Show progress
    Write-Host "Program Progress: $progress%" -ForegroundColor Green
    Write-Host "Budget Spent: `$budgetSpent / `$39.5M" -ForegroundColor Green
    
    # Weekly activities based on week number using a switch statement
    switch ($week) {
        1 {
            Write-Host "🔧 INITIATING ALPHA BUILD" -ForegroundColor Green
            Write-Host "→ Securing Silverado chassis for modification" -ForegroundColor Cyan
            Write-Host "→ LT4 crate engine procurement initiated" -ForegroundColor Cyan
        }
        4 {
            Write-Host "🚗 ALPHA MULE 1: Chassis modification complete" -ForegroundColor Green
            Write-Host "✓ Tonawanda delivered LT4 V8 Engine on schedule" -ForegroundColor Green
        }
        8 {
            Write-Host "⚙️ POWERTRAIN INTEGRATION" -ForegroundColor Green
            $testPassed = (Get-Random -Minimum 1 -Maximum 100) -le 88
            if ($testPassed) {
                Write-Host "✓ LT4_Powertrain testing passed" -ForegroundColor Green
            } else {
                Write-Host "✗ LT4_Powertrain testing failed - rework required" -ForegroundColor Red
                $criticalIssues++
            }
        }
        12 {
            Write-Host "✅ ALPHA PHASE COMPLETE" -ForegroundColor Green
            Write-Host "→ 4 Alpha mules operational" -ForegroundColor Cyan
            Write-Host "→ Beta build authorization granted" -ForegroundColor Cyan
        }
        13 {
            Write-Host "🔨 BETA BUILD INITIATION" -ForegroundColor Green
            Write-Host "→ Production-intent chassis preparation" -ForegroundColor Cyan
            Write-Host "→ Carbon fiber bed prototype development" -ForegroundColor Cyan
        }
        16 {
            Write-Host "🛻 CARBON FIBER BED PROTOTYPE" -ForegroundColor Green
            $deliverySuccess = (Get-Random -Minimum 1 -Maximum 100) -le 85
            if ($deliverySuccess) {
                Write-Host "✓ Plasan delivered Carbon Fiber Bed on schedule" -ForegroundColor Green
            } else {
                Write-Host "⚠ Plasan delayed Carbon Fiber Bed by 1 week" -ForegroundColor Yellow
                $supplierDelays++
            }
        }
        17 {
            Write-Host "📺 OLED DISPLAY INTEGRATION" -ForegroundColor Green
            $deliverySuccess = (Get-Random -Minimum 1 -Maximum 100) -le 90
            if ($deliverySuccess) {
                Write-Host "✓ LG Display delivered 38-inch OLED on schedule" -ForegroundColor Green
            } else {
                Write-Host "⚠ LG Display delayed 38-inch OLED by 1 week" -ForegroundColor Yellow
                $supplierDelays++
            }
        }
        18 {
            Write-Host "🌡️ OLED THERMAL TESTING" -ForegroundColor Green
            $testPassed = (Get-Random -Minimum 1 -Maximum 100) -le 82
            if ($testPassed) {
                Write-Host "✓ OLED_Thermal testing passed" -ForegroundColor Green
            } else {
                Write-Host "✗ OLED_Thermal testing failed - rework required" -ForegroundColor Red
                $criticalIssues++
            }
        }
        20 {
            Write-Host "🔬 CARBON FIBER STRUCTURAL TESTING" -ForegroundColor Green
            $testPassed = (Get-Random -Minimum 1 -Maximum 100) -le 85
            if ($testPassed) {
                Write-Host "✓ Carbon_Fiber testing passed" -ForegroundColor Green
            } else {
                Write-Host "✗ Carbon_Fiber testing failed - rework required" -ForegroundColor Red
                $criticalIssues++
            }
        }
        24 {
            Write-Host "✅ BETA PHASE COMPLETE" -ForegroundColor Green
            Write-Host "→ 6 Beta mules with key technologies" -ForegroundColor Cyan
            Write-Host "→ RC authorization pending review" -ForegroundColor Cyan
        }
        25 {
            Write-Host "🏁 RELEASE CANDIDATE BUILD" -ForegroundColor Green
            Write-Host "→ Production tooling components" -ForegroundColor Cyan
            Write-Host "→ Final supplier integration" -ForegroundColor Cyan
        }
        28 {
            Write-Host "⚡ FINAL VALIDATION TESTING" -ForegroundColor Green
            $testPassed = (Get-Random -Minimum 1 -Maximum 100) -le 95
            if ($testPassed) {
                Write-Host "✓ Crash_Simulation testing passed" -ForegroundColor Green
            } else {
                Write-Host "✗ Crash_Simulation testing failed - rework required" -ForegroundColor Red
                $criticalIssues++
            }
        }
        30 {
            Write-Host "🏭 PRODUCTION READINESS ASSESSMENT" -ForegroundColor Green
            Write-Host "→ Assembly process validation" -ForegroundColor Cyan
            Write-Host "→ Supplier quality verification" -ForegroundColor Cyan
        }
        32 {
            Write-Host "🎯 PROGRAM COMPLETE" -ForegroundColor Green
            Write-Host "→ Production authorization (Job #1)" -ForegroundColor Green
            Write-Host "→ 3 RC vehicles validated" -ForegroundColor Green
        }
    }
    
    # Show weekly metrics
    Write-Host "`n📊 WEEKLY METRICS:" -ForegroundColor Yellow
    Write-Host "→ Vehicles Built: $vehiclesBuilt/13" -ForegroundColor Cyan
    Write-Host "→ Tests Completed: $testsCompleted/45" -ForegroundColor Cyan
    Write-Host "→ Critical Issues: $criticalIssues" -ForegroundColor $(if($criticalIssues -gt 3){"Red"} else {"Cyan"})
    Write-Host "→ Supplier Delays: $supplierDelays" -ForegroundColor $(if($supplierDelays -gt 5){"Yellow"} else {"Cyan"})
    
    # Simulation delay
    Start-Sleep -Milliseconds (500 / $SimulationSpeed)
}

# Final program summary
Write-Host "`n╔══════════════════════════════════════════════════════════════════════╗" -ForegroundColor Blue
Write-Host "║                    PROGRAM COMPLETION SUMMARY                       ║" -ForegroundColor Blue
Write-Host "╚══════════════════════════════════════════════════════════════════════╝" -ForegroundColor Blue

Write-Host "📈 FINAL METRICS:" -ForegroundColor Yellow
Write-Host "→ Overall Progress: 100%" -ForegroundColor Green
Write-Host "→ Total Vehicles Built: $vehiclesBuilt/13" -ForegroundColor Cyan
Write-Host "→ Total Tests Completed: $testsCompleted/45" -ForegroundColor Cyan
Write-Host "→ Budget Utilization: `$budgetSpent / `$39.5M" -ForegroundColor Cyan
Write-Host "→ Critical Issues Resolved: $criticalIssues" -ForegroundColor $(if($criticalIssues -le 5){"Green"} else {"Red"})
Write-Host "→ Supplier Performance: $supplierDelays delays" -ForegroundColor $(if($supplierDelays -le 3){"Green"} else {"Yellow"})

Write-Host "`n🎯 PRODUCTION READINESS STATUS:" -ForegroundColor Yellow
$readinessScore = [math]::Round(100 - ($criticalIssues * 3) - ($supplierDelays * 2), 0)
Write-Host "→ Production Readiness Score: $readinessScore%" -ForegroundColor $(if($readinessScore -ge 85){"Green"} elseif($readinessScore -ge 70){"Yellow"} else {"Red"})

if ($readinessScore -ge 85) {
    Write-Host "✅ PROGRAM READY FOR PRODUCTION AUTHORIZATION" -ForegroundColor Green
} else {
    Write-Host "WARNING: ADDITIONAL VALIDATION REQUIRED BEFORE PRODUCTION" -ForegroundColor Yellow
}
