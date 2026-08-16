@echo off
chcp 65001 >nul
echo ==========================================
echo   WinApt Build Script
echo   Building apt.exe and apt-get.exe
echo ==========================================
echo.

REM Check for Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    exit /b 1
)

REM Check for PyInstaller
pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo Installing PyInstaller...
    pip install pyinstaller
)

echo [1/4] Building apt.exe...
pyinstaller --onefile --name apt --console apt.py
if errorlevel 1 (
    echo ERROR: Failed to build apt.exe
    exit /b 1
)

echo [2/4] Building apt-get.exe...
pyinstaller --onefile --name apt-get --console apt-get.py
if errorlevel 1 (
    echo ERROR: Failed to build apt-get.exe
    exit /b 1
)

echo [3/4] Creating distribution directory...
if not exist "dist\winapt" mkdir "dist\winapt"
copy "dist\apt.exe" "dist\winapt\" >nul
copy "dist\apt-get.exe" "dist\winapt\" >nul
copy "README.md" "dist\winapt\" >nul

REM Copy source code
xcopy /E /I /Y "core" "dist\winapt\core" >nul
xcopy /E /I /Y "backends" "dist\winapt\backends" >nul
copy "easter_eggs.py" "dist\winapt\" >nul
copy "utils.py" "dist\winapt\" >nul
copy "apt.py" "dist\winapt\" >nul
copy "apt-get.py" "dist\winapt\" >nul
copy "setup.py" "dist\winapt\" >nul
copy "requirements.txt" "dist\winapt\" >nul

echo [4/4] Creating ZIP archive...
powershell -Command "Compress-Archive -Path 'dist\winapt\*' -DestinationPath 'dist\winapt.zip' -Force"

echo.
echo ==========================================
echo   Build Complete!
echo   Executables: dist\winapt\
echo   Archive:     dist\winapt.zip
echo ==========================================
pause
