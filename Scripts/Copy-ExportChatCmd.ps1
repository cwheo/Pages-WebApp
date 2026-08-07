# Copy-ExportChatCmd.ps1
# Export Chat 명령어를 클립보드에 복사
# Usage: .\Scripts\Copy-ExportChatCmd.ps1

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

# Create directory path
$docPath = ".\AiCollabDocs\$year\$month"

# Generate export path
$exportPath = "$docPath\${timestamp}_${ProjectName}_Chat.txt"

# Output the command to execute in Claude Code
Write-Host ""
Write-Host "Run this command in Claude Code:" -ForegroundColor Cyan
Write-Host "/export $exportPath" -ForegroundColor Yellow
Write-Host ""

# Copy to clipboard
$command = "/export $exportPath"
$command | Set-Clipboard
Write-Host "Command copied to clipboard!" -ForegroundColor Green
