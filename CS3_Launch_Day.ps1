param (
    [string]$Version = "1.0.0-release"
)

# --- Configuration ---
$GlobalRegions = @("NA-East", "NA-West", "EU-West", "EU-Central", "Asia-East", "SA-Brazil", "Oceania")
$PrimaryCDN = "Akamai"
$SecondaryCDN = "Cloudflare"
$MasterServer = "cs3-master.nexon.net"
$GameClientPath = "C:\Program Files\NEXON Prime\Games\Counter-Strike 3\"

# --- Helper Functions ---
function Write-Log {
    param ([string]$Message, [string]$Color = "White")
    $Timestamp = Get-Date -Format "HH:mm:ss"
    Write-Host "[$Timestamp] $Message" -ForegroundColor $Color
}

function Invoke-Simulated-Deployment {
    param ([string]$Region, [string]$CDN)
    Write-Log "  -> Deploying build $Version to $CDN edge servers in $Region..."
    $steps = 10
    for ($i = 1; $i -le $steps; $i++) {
        $progress = $i * 10
        # Write-Progress -Activity "Deploying to $Region ($CDN)" -Status "$progress% Complete" -PercentComplete $progress
        Start-Sleep -Seconds (Get-Random -Minimum 1 -Maximum 2)
    }
    Write-Log "  -> Deployment to $CDN in $Region complete." -Color Green
}

# --- LAUNCH DAY SEQUENCE ---
Clear-Host
Write-Log "==================================================" -Color Yellow
Write-Log "  COUNTER-STRIKE 3 LAUNCH DAY SIMULATOR v1.0" -Color Yellow
Write-Log "  NEXON Prime Global Operations Center" -Color Yellow
Write-Log "==================================================" -Color Yellow
Write-Log "Launch Time: $(Get-Date)"
Write-Log "Game Version: $Version"

# T-60 Minutes: Final Build Propagation
Write-Log "[T-60 MIN] Initiating final build propagation to global CDNs." -Color Cyan
foreach ($region in $GlobalRegions) {
    Invoke-Simulated-Deployment -Region $region -CDN $PrimaryCDN
    Invoke-Simulated-Deployment -Region $region -CDN $SecondaryCDN # Redundancy
}
Write-Log "[T-50 MIN] Global CDN propagation complete. All edge nodes are hot." -Color Green

# T-30 Minutes: Server Health Checks
Write-Log "[T-30 MIN] Running final health checks on all regional server farms." -Color Cyan
foreach ($region in $GlobalRegions) {
    Write-Log "  -> Pinging server farm in $Region..."
    Start-Sleep -Seconds 1
    Write-Log "  -> Response from ${region}: OK (Latency: $((Get-Random -Minimum 15 -Maximum 80))ms)" -Color Green
}

# T-15 Minutes: Unlock Pre-Loads
Write-Log "[T-15 MIN] Sending decryption keys to NEXON Prime clients for pre-loaded copies." -Color Cyan
Write-Log "  -> Master server ($MasterServer) is now issuing decryption tokens."
Start-Sleep -Seconds 5
Write-Log "  -> Clients are beginning to decrypt game files. Estimated time: 5-10 minutes."

# T-5 Minutes: Final Go/No-Go Poll
Write-Log "[T-5 MIN] Final Go/No-Go poll with regional directors." -Color Cyan
$go = $true
foreach ($region in $GlobalRegions) {
    Write-Log "  -> $region Director: GO" -Color Green
    Start-Sleep -Milliseconds 500
}

if ($go) {
    Write-Log "[T-1 MIN] All systems are GO for launch. Standing by." -Color Green
    Start-Sleep -Seconds 5

    # LAUNCH
    Write-Log "[LAUNCH] EXECUTING LAUNCH!" -Color Magenta
    Write-Log "  -> Enabling public matchmaking on $MasterServer."
    Start-Sleep -Seconds 2
    Write-Log "  -> Store pages on NEXON Prime are now live."
    Start-Sleep -Seconds 2
    Write-Log "  -> Initial player wave is connecting..."

    # Post-Launch Monitoring
    $peakCCU = 0
    for ($i = 1; $i -le 10; $i++) {
        $currentCCU = (Get-Random -Minimum (50000 * $i) -Maximum (150000 * $i))
        if ($currentCCU -gt $peakCCU) { $peakCCU = $currentCCU }
        Write-Log "[LAUNCH + $($i*2) MIN] Concurrent Users (CCU): $($currentCCU.ToString("N0"))" -Color White
        Start-Sleep -Seconds 3
    }

    Write-Log "==================================================" -Color Yellow
    Write-Log "  LAUNCH STATUS: SUCCESSFUL" -Color Green
    Write-Log "  PEAK CONCURRENT USERS (First 20 Mins): $($peakCCU.ToString("N0"))" -Color Green
    Write-Log "  Counter-Strike 3 is LIVE worldwide."
    Write-Log "==================================================" -Color Yellow
} else {
    Write-Log "[ABORT] A 'No-Go' was reported. Aborting launch sequence." -Color Red
}
