@echo off
chcp 65001 > nul
powershell -ExecutionPolicy Bypass -File "%~dp0Copy-ExportChatCmd.ps1"
rem pause
