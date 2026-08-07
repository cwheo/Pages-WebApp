# Copy-DateTime_yyyyMMdd_HHmm.ps1
# 현재 시스템 일시를 yyyyMMdd_HHmm 형식으로 클립보드에 복사

$dateTimeString = Get-Date -Format "yyyyMMdd_HHmm"
$dateTimeString | Set-Clipboard

Write-Host "Copied to clipboard: $dateTimeString"
