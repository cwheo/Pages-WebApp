# Copy-DateTime_yyyyMMdd_HHmmss.ps1
# 현재 시스템 일시를 yyyyMMdd_HHmmss 형식으로 클립보드에 복사

$dateTimeString = Get-Date -Format "yyyyMMdd_HHmmss"
$dateTimeString | Set-Clipboard

Write-Host "Copied to clipboard: $dateTimeString"
