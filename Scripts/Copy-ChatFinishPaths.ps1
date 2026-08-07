# Copy-ChatFinishPaths.ps1
# Chat 마무리용 - Work List 경로 + Export 명령어 생성
# Usage: .\Scripts\Copy-ChatFinishPaths.ps1

# ============================================
# Configuration - Modify this for your project
# ============================================
$ProjectName = "Template"
# ============================================

# Get current timestamp
$now = Get-Date
$year = $now.ToString("yyyy")
$month = $now.ToString("MM")
$timestamp = $now.ToString("yyyyMMdd_HHmm")

# Generate paths
$docPath = ".\AiCollabDocs\$year\$month"
$workListPath = "$docPath\${timestamp}_${ProjectName}_Work_List.md"
$exportCmd = "/export $docPath\${timestamp}_${ProjectName}_Chat.txt"

# Output
Write-Host ""
Write-Host "=== Chat Finish Paths ===" -ForegroundColor Cyan
Write-Host ""
Write-Host "[1] Work List path:" -ForegroundColor Yellow
Write-Host "    $workListPath" -ForegroundColor White
Write-Host ""
Write-Host "[2] Chat Export command:" -ForegroundColor Yellow
Write-Host "    $exportCmd" -ForegroundColor White
Write-Host ""

# Copy export command to clipboard
$exportCmd | Set-Clipboard
Write-Host "Export command copied to clipboard!" -ForegroundColor Green
