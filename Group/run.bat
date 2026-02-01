@echo off
REM Despite Group Access Control System - Installation and Run Script

echo ========================================================
echo DESPITE GROUP ACCESS CONTROL SYSTEM
echo Zero Trust Architecture Implementation
echo ========================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo.
    echo Please install Python from: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

cd /d "c:\Users\Yulark\OneDrive\Desktop\Group"

echo Python found! Installing dependencies...
pip install -r requirements.txt

echo.
echo Starting Despite Group Access Control System...
echo Server will run at: http://localhost:5000
echo.
echo Demo Credentials:
echo   - alice (Creator): securePass123
echo   - bob (Admin): adminPass456
echo   - diana (PR Manager): pr_manager123
echo   - charlie (Analyst): analyst789
echo.
echo Press CTRL+C to stop the server
echo ========================================================
echo.

REM Run the Flask server
python run_server.py

pause
