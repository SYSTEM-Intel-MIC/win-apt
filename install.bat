@echo off
chcp 65001 >nul 2>&1
title WinApt Installer

echo.
echo  ========================================
echo       WinApt - apt for Windows
echo  ========================================
echo.

:: Check if Python is installed
echo  [1/5] Checking Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo  [ERROR] Python is not installed or not in PATH.
    echo  Please install Python 3.8+ from: https://www.python.org/downloads/
    echo  Make sure to check "Add Python to PATH" during installation.
    echo.
    pause
    exit /b 1
)

for /f "tokens=2 delims= " %%v in ('python --version 2^>^&1') do set PYVER=%%v
echo  [OK] Python %PYVER%

:: Check Python version >= 3.8
python -c "import sys; exit(0 if sys.version_info >= (3, 8) else 1)" >nul 2>&1
if %errorlevel% neq 0 (
    echo  [ERROR] Python 3.8+ required. Current: %PYVER%
    pause
    exit /b 1
)

:: Install the package
echo.
echo  [2/5] Installing WinApt...
cd /d "%~dp0"
pip install . --quiet 2>nul
if %errorlevel% neq 0 (
    pip install . --user --quiet 2>nul
    if %errorlevel% neq 0 (
        echo  [ERROR] Installation failed.
        pause
        exit /b 1
    )
)
echo  [OK] Package installed

:: Find Scripts directory
echo.
echo  [3/5] Configuring PATH...
for /f "tokens=*" %%i in ('python -c "import sys,os; p=os.path.dirname(sys.executable); s=os.path.join(p,'Scripts') if os.path.exists(os.path.join(p,'Scripts')) else os.path.join(os.path.dirname(p),'Scripts'); print(s)"') do set SCRIPTS_DIR=%%i

:: Copy apt.exe and apt-get.exe to a local bin directory for reliability
set "LOCAL_BIN=%~dp0bin"
if not exist "%LOCAL_BIN%" mkdir "%LOCAL_BIN%"
if exist "%SCRIPTS_DIR%\apt.exe" copy /y "%SCRIPTS_DIR%\apt.exe" "%LOCAL_BIN%\apt.exe" >nul 2>&1
if exist "%SCRIPTS_DIR%\apt-get.exe" copy /y "%SCRIPTS_DIR%\apt-get.exe" "%LOCAL_BIN%\apt-get.exe" >nul 2>&1
echo  [OK] Executables ready: %LOCAL_BIN%

:: Add to user PATH permanently using PowerShell (no char limit)
echo.
echo  [4/5] Adding to PATH...
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
    "$currentPath = [Environment]::GetEnvironmentVariable('Path', 'User'); ^
     $toAdd = @('%LOCAL_BIN%', '%SCRIPTS_DIR%'); ^
     foreach ($dir in $toAdd) { ^
       if ($dir -and (Test-Path $dir) -and $currentPath -notlike [regex]::Escape($dir) + ';*') { ^
         $currentPath = $currentPath.TrimEnd(';') + ';' + $dir; ^
       } ^
     }; ^
     [Environment]::SetEnvironmentVariable('Path', $currentPath, 'User'); ^
     Write-Host '[OK] PATH updated'"

:: Update current session PATH
set "PATH=%PATH%;%LOCAL_BIN%;%SCRIPTS_DIR%"

:: Verify
echo.
echo  [5/5] Verifying...
apt --version >nul 2>&1
if %errorlevel% neq 0 (
    echo  [WARN] apt not available in this session yet.
    echo  Please open a NEW terminal and run: apt --version
) else (
    echo  [OK] apt is working!
)

echo.
echo  ========================================
echo           Installation Complete
echo  ========================================
echo.
echo  Open a NEW terminal and try:
echo.
echo    apt --version
echo    apt update
echo    apt install firefox
echo    apt moo
echo.
echo  Requires: winget and/or Chocolatey
echo  ========================================
echo.
pause
