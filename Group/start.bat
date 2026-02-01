@echo off
REM =========================================================
REM Despite Group Access Control System - Windows Launcher
REM =========================================================
REM This script sets up and starts the application on Windows
REM Simply double-click this file or run it from cmd

setlocal enabledelayedexpansion

cd /d "%~dp0"

REM Colors for output (Windows 10+)
color 0A

title Despite Group Access Control System

echo.
echo =========================================================
echo   DESPITE GROUP ACCESS CONTROL SYSTEM v2.0
echo   Windows Launcher
echo =========================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo.
    echo Please install Python 3.8+ from: https://python.org
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

echo [OK] Python found
python --version

echo.
echo [*] Checking virtual environment...

REM Check if venv exists
if not exist "venv" (
    echo [*] Virtual environment not found. Creating...
    python -m venv venv
    if errorlevel 1 (
        echo [ERROR] Failed to create virtual environment
        pause
        exit /b 1
    )
    echo [OK] Virtual environment created
)

echo.
echo [*] Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo [ERROR] Failed to activate virtual environment
    pause
    exit /b 1
)
echo [OK] Virtual environment activated

echo.
echo [*] Installing dependencies...
pip install -q --upgrade pip
if errorlevel 1 (
    echo [WARNING] Some dependencies may not be installed
)
pip install -q -r requirements.txt
if errorlevel 1 (
    echo [WARNING] Failed to install all dependencies
    echo [*] Attempting to continue anyway...
)
echo [OK] Dependencies ready

echo.
echo =========================================================
echo   [OK] READY TO START
echo =========================================================
echo.
echo Server Details:
echo   URL: http://localhost:5000
echo   Status: Starting...
echo.
echo Demo Credentials:
echo   - alice / securePass123 (Creator)
echo   - bob / adminPass456 (Admin)
echo   - diana / pr_manager123 (PR_Manager)
echo   - charlie / analyst789 (Analyst)
echo.
echo [!] Press CTRL+C in terminal to stop the server
echo.
echo =========================================================
echo.

REM Start the application
python run_server.py

REM If we get here, server stopped
echo.
echo =========================================================
echo Server stopped.
echo =========================================================
pause
