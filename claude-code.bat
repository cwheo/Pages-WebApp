@echo off
:: claude-code.bat - Claude Code 실행
::   사용법 1) 이 배치를 원하는 폴더에 복사 후 더블클릭  -> 배치가 있는 폴더에서 실행
::   사용법 2) claude-code.bat "C:\실행할\폴더경로"  -> 지정한 폴더에서 실행

setlocal
set "CLAUDE_EXE=%USERPROFILE%\.local\bin\claude.exe"

:: 대상 폴더 결정: 인자가 있으면 그 경로, 없으면 배치 파일이 있는 폴더
if not "%~1"=="" (set "TARGET_DIR=%~1") else (set "TARGET_DIR=%~dp0")

:: 경로 끝에 백슬래시 보장 (wt -d 인자 처리 및 존재 검사용)
if not "%TARGET_DIR:~-1%"=="\" set "TARGET_DIR=%TARGET_DIR%\"

:: 대상 폴더 존재 확인
if not exist "%TARGET_DIR%" goto :baddir

:: Windows Terminal에서 대상 폴더로 열고 Claude Code 실행
:: (경로 끝 백슬래시+따옴표가 이스케이프로 오인되지 않도록 "%TARGET_DIR%." 형태 사용)
start "" "%LOCALAPPDATA%\Microsoft\WindowsApps\wt.exe" -d "%TARGET_DIR%." -- cmd /c "%CLAUDE_EXE%" --dangerously-skip-permissions
goto :eof

:baddir
echo [ERROR] Target folder not found: "%TARGET_DIR%"
echo   Usage: claude-code.bat [folder-path]
pause
