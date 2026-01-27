# Cadillac EXT-V: Marketing & Launch Simulator

# --- Configuration ---
$RevealEvent = "North American International Auto Show (Detroit)"
$LaunchDate = (Get-Date).AddDays(120)

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
Write-Host "   Cadillac EXT-V - Marketing & Launch Simulation"
Write-Host "=================================================$($Color_Reset)"
Start-Sleep -Seconds 2

# --- Phase 1: Teaser Campaign (T-Minus 30 Days) ---
Write-Host "
$($Color_Yellow)[PHASE 1] Teaser Campaign Initiated...$($Color_Reset)"
Start-Sleep -Seconds 2

Write-Host "$($Color_White)Mysterious, shadowy videos appear on social media, showing a glimpse of a vertical headlight and the roar of a supercharged V8.$($Color_Reset)"
Start-Sleep -Seconds 2
Write-Host "$($Color_White)Hashtag #DareGreatly trends as automotive journalists speculate about a new Cadillac V-Series vehicle.$($Color_Reset)"
Start-Sleep -Seconds 2
Write-Host "$($Color_Cyan)Cadillac officially confirms a major reveal at the $($RevealEvent).$($Color_Reset)"
Start-Sleep -Seconds 3

# --- Phase 2: The Reveal (Detroit Auto Show) ---
Write-Host "
$($Color_Yellow)[PHASE 2] World Premiere at the $($RevealEvent)...$($Color_Reset)"
Start-Sleep -Seconds 2

Write-Host "$($Color_White)The stage is dark. The sound of a heartbeat fills the room, followed by the thunderous ignition of the 6.2L V8.$($Color_Reset)"
Start-Sleep -Seconds 3
Write-Host "$($Color_Red)Lights flash, and the Cadillac EXT-V is revealed.$($Color_Reset)"
Start-Sleep -Seconds 2
Write-Host "$($Color_White)The press is in a frenzy. The 700hp figure is announced, sending shockwaves through the industry.$($Color_Reset)"
Start-Sleep -Seconds 2
Write-Host "$($Color_Green)'Best in Show' awards from multiple publications are given to the EXT-V.$($Color_Reset)"
Start-Sleep -Seconds 3

# --- Phase 3: Pre-Orders & Launch ---
Write-Host "
$($Color_Yellow)[PHASE 3] Launch Day - $($LaunchDate.ToString('D'))$($Color_Reset)"
Start-Sleep -Seconds 2

Write-Host "$($Color_Cyan)The online configurator and pre-order system goes live.$($Color_Reset)"
Start-Sleep -Seconds 1
Write-Host "$($Color_Red)The first year's allocation of the EXT-V model sells out in under 10 minutes.$($Color_Reset)"
Start-Sleep -Seconds 2
Write-Host "$($Color_White)The first trucks are delivered to VIP clients and brand ambassadors.$($Color_Reset)"
Start-Sleep -Seconds 2

# --- Phase 4: Market Impact ---
Write-Host "
$($Color_Yellow)[PHASE 4] Redefining the Segment...$($Color_Reset)"
Start-Sleep -Seconds 1
Write-Host "$($Color_Cyan)First-drive reviews are published...$($Color_Reset)"
Start-Sleep -Seconds 2
Write-Host "$($Color_White)MotorTrend: 'An Escalade with a bed and the heart of a Corvette Z06. A new king is crowned.'"
Write-Host "$($Color_White)Car and Driver: 'The 700hp V8 is brutally effective, but the real story is the interior. Unmatched luxury.'"
Write-Host "$($Color_White)The a href='http://Truck.com'>Truck.com</a>: 'It hauls, it tows, and it's faster than most sports cars. The supertruck segment has been put on notice.'"
Start-Sleep -Seconds 4

Write-Host "
$($Color_Green)================================================="
Write-Host "   Cadillac EXT-V Launch: A Decisive Victory"
Write-Host "=================================================$($Color_Reset)"
