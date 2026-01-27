# Cadillac EXT-V Mule Build Simulator
# Real-time prototype validation program simulation

param(
    [int]$SimulationSpeed = 1,  # 1=normal, 2=2x speed, 5=5x speed
    [int]$StartWeek = 1,
    [int]$EndWeek = 32,
    [switch]$AutoShowMode = $false
)

# ANSI color codes for enhanced output
$Colors = @{
    Header = "`e[1;34m"    # Blue
    Success = "`e[1;32m"   # Green
    Warning = "`e[1;33m"   # Yellow
    Error = "`e[1;31m"     # Red
    Info = "`e[1;36m"      # Cyan
    Reset = "`e[0m"        # Reset
    Bold = "`e[1m"          # Bold
}

function Write-ColoredOutput {
    param([string]$Text, [string]$Color = "Reset")
    Write-Host "$($Colors[$Color])$Text$($Colors.Reset)"
}

function Show-ProgressBar {
    param([int]$Current, [int]$Total, [string]$Label)
    $percent = [math]::Round(($Current / $Total) * 100, 1)
    $barLength = 40
    $filled = [math]::Round(($percent / 100) * $barLength)
    $empty = $barLength - $filled
    
    $bar = "█" * $filled + "░" * $empty
    Write-Host "$Label [$bar] $percent%" -NoNewline
    Write-Host "`r" -NoNewline
}

function Get-RandomOutcome {
    param([int]$SuccessRate = 85)
    $random = Get-Random -Minimum 1 -Maximum 100
    return $random -le $SuccessRate
}

function Simulate-ComponentDelivery {
    param([string]$Supplier, [string]$Component, [int]$Week)
    
    $deliveryOutcomes = @{
        "LG Display" = @{ SuccessRate = 90; LeadTime = 6 }
        "Plasan" = @{ SuccessRate = 85; LeadTime = 8 }
        "Tonawanda" = @{ SuccessRate = 95; LeadTime = 4 }
        "Magna" = @{ SuccessRate = 88; LeadTime = 5 }
        "Bosch" = @{ SuccessRate = 92; LeadTime = 3 }
    }
    
    $supplierData = $deliveryOutcomes[$Supplier]
    $onTime = Get-RandomOutcome -SuccessRate $supplierData.SuccessRate
    
    if ($onTime) {
        Write-ColoredOutput "✓ $Supplier delivered $Component on schedule (Week $Week)" "Success"
        return @{ Status = "OnTime"; Delay = 0; Quality = "Good" }
    } else {
        $delay = Get-Random -Minimum 1 -Maximum 3
        Write-ColoredOutput "⚠ $Supplier delayed $Component by $delay weeks" "Warning"
        return @{ Status = "Delayed"; Delay = $delay; Quality = "Acceptable" }
    }
}

function Simulate-TestingOutcome {
    param([string]$TestType, [int]$Week)
    
    $testOutcomes = @{
        "LT4_Powertrain" = @{ SuccessRate = 88; Critical = $true }
        "OLED_Thermal" = @{ SuccessRate = 82; Critical = $true }
        "Carbon_Fiber" = @{ SuccessRate = 85; Critical = $true }
        "MRC_Calibration" = @{ SuccessRate = 90; Critical = $false }
        "NVH_Testing" = @{ SuccessRate = 85; Critical = $false }
        "Crash_Simulation" = @{ SuccessRate = 95; Critical = $true }
    }
    
    $testData = $testOutcomes[$TestType]
    $passed = Get-RandomOutcome -SuccessRate $testData.SuccessRate
    
    if ($passed) {
        Write-ColoredOutput "✓ $TestType testing passed (Week $Week)" "Success"
        return @{ Status = "Passed"; ReworkRequired = $false; Critical = $testData.Critical }
    } else {
        Write-ColoredOutput "✗ $TestType testing failed - rework required (Week $Week)" "Error"
        return @{ Status = "Failed"; ReworkRequired = $true; Critical = $testData.Critical }
    }
}

function Update-ProgramMetrics {
    param([hashtable]$Metrics, [int]$Week)
    
    # Simulate progress based on week and random outcomes
    $baseProgress = ($Week / 32) * 100
    $randomFactor = Get-Random -Minimum -5 -Maximum 5
    $progress = [math]::Max(0, [math]::Min(100, $baseProgress + $randomFactor))
    
    $metrics.OverallProgress = [math]::Round($progress, 1)
    $metrics.VehiclesBuilt = [math]::Floor(($Week / 32) * 13)  # 13 total mules
    $metrics.TestsCompleted = [math]::Floor(($Week / 32) * 45)  # ~45 major tests
    
    # Simulate budget burn
    $weeklyBurn = Get-Random -Minimum 1.0 -Maximum 1.5
    $metrics.BudgetSpent = [math]::Round($metrics.BudgetSpent + $weeklyBurn, 1)
    
    return $metrics
}

# Initialize program metrics
$programMetrics = @{
    OverallProgress = 0.0
    VehiclesBuilt = 0
    TestsCompleted = 0
    BudgetSpent = 0.0
    CriticalIssues = 0
    SupplierDelays = 0
}

# Main simulation loop
Write-ColoredOutput "`n╔══════════════════════════════════════════════════════════════════════╗" "Header"
Write-ColoredOutput "║    CADILLAC EXT-V MULE VEHICLE BUILD PROGRAM - LIVE SIMULATION     ║" "Header"
Write-ColoredOutput "╚══════════════════════════════════════════════════════════════════════╝" "Header"
Write-ColoredOutput "Program: `$39.5M prototype validation - 13 mule vehicles - 32-week timeline`n" "Info"

# Phase definitions
$phases = @(
    @{ Name = "Alpha Phase"; StartWeek = 1; EndWeek = 12; Vehicles = 4; Budget = 12.5 },
    @{ Name = "Beta Phase"; StartWeek = 13; EndWeek = 24; Vehicles = 6; Budget = 18.7 },
    @{ Name = "Release Candidate"; StartWeek = 25; EndWeek = 32; Vehicles = 3; Budget = 8.3 }
)

for ($week = $StartWeek; $week -le $EndWeek; $week++) {
    
    # Determine current phase
    $currentPhase = $phases | Where-Object { $week -ge $_.StartWeek -and $week -le $_.EndWeek }
    
    Write-ColoredOutput "`n📅 WEEK $week - $($currentPhase.Name.ToUpper())" "Bold"
    Write-ColoredOutput "═══════════════════════════════════════════════════════════════════════" "Header"
    
    # Update metrics
    $programMetrics = Update-ProgramMetrics -Metrics $programMetrics -Week $week
    
    # Show progress bars
    Show-ProgressBar -Current $week -Total 32 -Label "Program Progress"
    Write-Host ""
    Show-ProgressBar -Current $programMetrics.BudgetSpent -Total 39.5 -Label "Budget Spent (`$`$($programMetrics.BudgetSpent)M / `$39.5M)"
    Write-Host ""
    
    # Weekly activities based on phase
    switch ($currentPhase.Name) {
        "Alpha Phase" {
            if ($week -eq 1) {
                Write-ColoredOutput "🔧 INITIATING ALPHA BUILD" "Bold"
                Write-ColoredOutput "→ Securing Silverado chassis for modification" "Info"
                Write-ColoredOutput "→ LT4 crate engine procurement initiated" "Info"
            }
            elseif ($week -eq 4) {
                Write-ColoredOutput "🚗 ALPHA MULE 1: Chassis modification complete" "Success"
                $delivery = Simulate-ComponentDelivery -Supplier "Tonawanda" -Component "LT4 V8 Engine" -Week $week
            }
            elseif ($week -eq 8) {
                Write-ColoredOutput "⚙️ POWERTRAIN INTEGRATION" "Bold"
                $test = Simulate-TestingOutcome -TestType "LT4_Powertrain" -Week $week
                if ($test.ReworkRequired) { $programMetrics.CriticalIssues++ }
            }
            elseif ($week -eq 12) {
                Write-ColoredOutput "✅ ALPHA PHASE COMPLETE" "Success"
                Write-ColoredOutput "→ 4 Alpha mules operational" "Info"
                Write-ColoredOutput "→ Beta build authorization granted" "Info"
            }
        }
        
        "Beta Phase" {
            if ($week -eq 13) {
                Write-ColoredOutput "🔨 BETA BUILD INITIATION" "Bold"
                Write-ColoredOutput "→ Production-intent chassis preparation" "Info"
                Write-ColoredOutput "→ Carbon fiber bed prototype development" "Info"
            }
            elseif ($week -eq 16) {
                Write-ColoredOutput "🛻 CARBON FIBER BED PROTOTYPE" "Bold"
                $delivery = Simulate-ComponentDelivery -Supplier "Plasan" -Component "Carbon Fiber Bed" -Week $week
                if ($delivery.Status -eq "Delayed") { $programMetrics.SupplierDelays++ }
            }
            elseif ($week -eq 17) {
                Write-ColoredOutput "📺 OLED DISPLAY INTEGRATION" "Bold"
                $delivery = Simulate-ComponentDelivery -Supplier "LG Display" -Component "38-inch OLED" -Week $week
                if ($delivery.Status -eq "Delayed") { $programMetrics.SupplierDelays++ }
            }
            elseif ($week -eq 18) {
                Write-ColoredOutput "🌡️ OLED THERMAL TESTING" "Bold"
                $test = Simulate-TestingOutcome -TestType "OLED_Thermal" -Week $week
                if ($test.ReworkRequired) { $programMetrics.CriticalIssues++ }
            }
            elseif ($week -eq 20) {
                Write-ColoredOutput "🔬 CARBON FIBER STRUCTURAL TESTING" "Bold"
                $test = Simulate-TestingOutcome -TestType "Carbon_Fiber" -Week $week
                if ($test.ReworkRequired) { $programMetrics.CriticalIssues++ }
            }
            elseif ($week -eq 24) {
                Write-ColoredOutput "✅ BETA PHASE COMPLETE" "Success"
                Write-ColoredOutput "→ 6 Beta mules with key technologies" "Info"
                Write-ColoredOutput "→ RC authorization pending review" "Info"
            }
        }
        
        "Release Candidate" {
            if ($week -eq 25) {
                Write-ColoredOutput "🏁 RELEASE CANDIDATE BUILD" "Bold"
                Write-ColoredOutput "→ Production tooling components" "Info"
                Write-ColoredOutput "→ Final supplier integration" "Info"
            }
            elseif ($week -eq 28) {
                Write-ColoredOutput "⚡ FINAL VALIDATION TESTING" "Bold"
                $test = Simulate-TestingOutcome -TestType "Crash_Simulation" -Week $week
                if ($test.ReworkRequired) { $programMetrics.CriticalIssues++ }
            }
            elseif ($week -eq 30) {
                Write-ColoredOutput "🏭 PRODUCTION READINESS ASSESSMENT" "Bold"
                Write-ColoredOutput "→ Assembly process validation" "Info"
                Write-ColoredOutput "→ Supplier quality verification" "Info"
            }
            elseif ($week -eq 32) {
                Write-ColoredOutput "🎯 PROGRAM COMPLETE" "Success"
                Write-ColoredOutput "→ Production authorization (Job #1)" "Success"
                Write-ColoredOutput "→ 3 RC vehicles validated" "Success"
            }
        }
    }
    
    # Show weekly metrics
    Write-ColoredOutput "`n📊 WEEKLY METRICS:" "Bold"
    Write-ColoredOutput "→ Vehicles Built: $($programMetrics.VehiclesBuilt)/13" "Info"
    Write-ColoredOutput "→ Tests Completed: $($programMetrics.TestsCompleted)/45" "Info"
    Write-ColoredOutput "→ Critical Issues: $($programMetrics.CriticalIssues)" $(if($programMetrics.CriticalIssues -gt 3){"Error"} else {"Info"})
    Write-ColoredOutput "→ Supplier Delays: $($programMetrics.SupplierDelays)" $(if($programMetrics.SupplierDelays -gt 5){"Warning"} else {"Info"})
    
    # Auto-show integration
    if ($AutoShowMode -and $week -eq 28) {
        Write-ColoredOutput "`n🏆 DETROIT AUTO SHOW REVEAL PREPARATION" "Bold"
        Write-ColoredOutput "→ Concept vehicle final detailing" "Info"
        Write-ColoredOutput "→ Press conference setup" "Info"
        Write-ColoredOutput "→ Media preview scheduling" "Info"
    }
    
    # Simulation delay
    Start-Sleep -Milliseconds (500 / $SimulationSpeed)
}

# Final program summary
Write-ColoredOutput "`n╔══════════════════════════════════════════════════════════════════════╗" "Header"
Write-ColoredOutput "║                    PROGRAM COMPLETION SUMMARY                       ║" "Header"
Write-ColoredOutput "╚══════════════════════════════════════════════════════════════════════╝" "Header"

Write-ColoredOutput "📈 FINAL METRICS:" "Bold"
Write-ColoredOutput "→ Overall Progress: $($programMetrics.OverallProgress)%" $(if($programMetrics.OverallProgress -ge 95){"Success"} else {"Warning"})
Write-ColoredOutput "→ Total Vehicles Built: $($programMetrics.VehiclesBuilt)/13" "Info"
Write-ColoredOutput "→ Total Tests Completed: $($programMetrics.TestsCompleted)/45" "Info"
Write-ColoredOutput "→ Budget Utilization: $$($programMetrics.BudgetSpent)M / $39.5M" "Info"
Write-ColoredOutput "→ Critical Issues Resolved: $($programMetrics.CriticalIssues)" $(if($programMetrics.CriticalIssues -le 5){"Success"} else {"Error"})
Write-ColoredOutput "→ Supplier Performance: $($programMetrics.SupplierDelays) delays" $(if($programMetrics.SupplierDelays -le 3){"Success"} else {"Warning"})

Write-ColoredOutput "`n🎯 PRODUCTION READINESS STATUS:" "Bold"
$readinessScore = [math]::Round(100 - ($programMetrics.CriticalIssues * 3) - ($programMetrics.SupplierDelays * 2), 0)
Write-ColoredOutput "→ Production Readiness Score: $readinessScore%" $(if($readinessScore -ge 85){"Success"} elseif($readinessScore -ge 70){"Warning"} else {"Error"})

if ($readinessScore -ge 85) {
    Write-ColoredOutput "✅ PROGRAM READY FOR PRODUCTION AUTHORIZATION" "Success"
} else {
    Write-ColoredOutput "WARNING: ADDITIONAL VALIDATION REQUIRED BEFORE PRODUCTION" "Warning"
}