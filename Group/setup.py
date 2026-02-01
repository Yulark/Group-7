#!/usr/bin/env python3
"""
Despite Group Access Control System - Cross-Platform Setup
Detects OS, installs dependencies, and prepares the application
"""

import os
import sys
import subprocess
import platform
import json
from pathlib import Path

class Setup:
    def __init__(self):
        self.os_type = platform.system()
        self.python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
        self.base_dir = Path(__file__).parent
        self.venv_dir = self.base_dir / "venv"
        
    def print_header(self):
        """Print setup header"""
        print("\n" + "="*60)
        print("  DESPITE GROUP ACCESS CONTROL SYSTEM")
        print("  Cross-Platform Setup & Installation")
        print("="*60)
        print(f"Operating System: {self.os_type}")
        print(f"Python Version: {self.python_version}")
        print(f"Installation Path: {self.base_dir}")
        print("="*60 + "\n")
    
    def check_python(self):
        """Check if Python 3.8+ is available"""
        print("✓ Checking Python installation...")
        major, minor = sys.version_info.major, sys.version_info.minor
        
        if major < 3 or (major == 3 and minor < 8):
            print("✗ Python 3.8+ required!")
            print(f"  Current: Python {major}.{minor}")
            sys.exit(1)
        
        print(f"✓ Python {major}.{minor} detected\n")
        return True
    
    def create_venv(self):
        """Create virtual environment"""
        print("✓ Setting up virtual environment...")
        
        if self.venv_dir.exists():
            print(f"  Virtual environment already exists at {self.venv_dir}")
            return True
        
        try:
            subprocess.run(
                [sys.executable, "-m", "venv", str(self.venv_dir)],
                check=True,
                capture_output=True
            )
            print(f"✓ Virtual environment created\n")
            return True
        except subprocess.CalledProcessError as e:
            print(f"✗ Failed to create virtual environment: {e}")
            return False
    
    def get_pip_command(self):
        """Get pip executable path for current OS"""
        if self.os_type == "Windows":
            return self.venv_dir / "Scripts" / "pip.exe"
        else:
            return self.venv_dir / "bin" / "pip"
    
    def get_python_command(self):
        """Get python executable path for current OS"""
        if self.os_type == "Windows":
            return self.venv_dir / "Scripts" / "python.exe"
        else:
            return self.venv_dir / "bin" / "python"
    
    def install_dependencies(self):
        """Install required packages"""
        print("✓ Installing dependencies...")
        
        pip_cmd = str(self.get_pip_command())
        requirements_file = self.base_dir / "requirements.txt"
        
        if not requirements_file.exists():
            print(f"✗ requirements.txt not found at {requirements_file}")
            return False
        
        try:
            subprocess.run(
                [pip_cmd, "install", "--upgrade", "pip"],
                check=True,
                capture_output=True
            )
            
            subprocess.run(
                [pip_cmd, "install", "-r", str(requirements_file)],
                check=True,
                capture_output=False
            )
            
            print("✓ Dependencies installed successfully\n")
            return True
        except subprocess.CalledProcessError as e:
            print(f"✗ Failed to install dependencies: {e}")
            return False
    
    def create_startup_scripts(self):
        """Create OS-specific startup scripts"""
        print("✓ Creating startup scripts...")
        
        python_cmd = str(self.get_python_command())
        
        if self.os_type == "Windows":
            self.create_batch_script(python_cmd)
        else:
            self.create_shell_script(python_cmd)
        
        print("✓ Startup scripts created\n")
    
    def create_batch_script(self, python_cmd):
        """Create Windows batch script"""
        batch_content = f"""@echo off
REM Despite Group Access Control System - Windows Launcher
REM Run this file to start the application

cd /d "%~dp0"

REM Check if venv exists
if not exist venv (
    echo Virtual environment not found. Running setup...
    python setup.py
    echo.
    echo Setup complete! Run this script again to start the application.
    pause
    exit /b
)

REM Activate virtual environment and run Flask
echo Starting Despite Group Access Control System...
echo.
echo Server running at: http://localhost:5000
echo.
echo Demo Credentials:
echo   - alice / securePass123 (Creator)
echo   - bob / adminPass456 (Admin)
echo   - diana / pr_manager123 (PR_Manager)
echo   - charlie / analyst789 (Analyst)
echo.
echo Press CTRL+C to stop the server
echo.

call venv\\Scripts\\activate.bat
python run_server.py

pause
"""
        
        script_path = self.base_dir / "start.bat"
        with open(script_path, "w") as f:
            f.write(batch_content)
        print(f"  Created: {script_path}")
    
    def create_shell_script(self, python_cmd):
        """Create Unix/Linux/Mac shell script"""
        shell_content = """#!/bin/bash
# Despite Group Access Control System - Unix Launcher
# Run this file to start the application

cd "$(dirname "$0")"

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Running setup..."
    python3 setup.py
    echo ""
    echo "Setup complete! Run this script again to start the application."
    exit 1
fi

# Activate virtual environment and run Flask
echo "Starting Despite Group Access Control System..."
echo ""
echo "Server running at: http://localhost:5000"
echo ""
echo "Demo Credentials:"
echo "  - alice / securePass123 (Creator)"
echo "  - bob / adminPass456 (Admin)"
echo "  - diana / pr_manager123 (PR_Manager)"
echo "  - charlie / analyst789 (Analyst)"
echo ""
echo "Press CTRL+C to stop the server"
echo ""

source venv/bin/activate
python run_server.py
"""
        
        script_path = self.base_dir / "start.sh"
        with open(script_path, "w") as f:
            f.write(shell_content)
        
        # Make executable
        os.chmod(script_path, 0o755)
        print(f"  Created: {script_path}")
    
    def create_config(self):
        """Create configuration file"""
        config = {
            "app_name": "Despite Group Access Control System",
            "version": "2.0",
            "python_version": self.python_version,
            "os": self.os_type,
            "venv_created": True,
            "setup_date": str(Path.cwd())
        }
        
        config_path = self.base_dir / ".setup_config.json"
        with open(config_path, "w") as f:
            json.dump(config, f, indent=2)
        
        return True
    
    def print_next_steps(self):
        """Print next steps"""
        print("\n" + "="*60)
        print("  ✓ SETUP COMPLETE!")
        print("="*60)
        print("\nNext Steps:")
        print("")
        
        if self.os_type == "Windows":
            print("  1. Double-click: start.bat")
            print("  2. Or run in terminal: start.bat")
            print("")
            print("Distribution to friends (Windows):")
            print("  1. Zip the entire folder")
            print("  2. They extract it")
            print("  3. They double-click start.bat")
            print("  4. Browser opens automatically")
        else:
            print("  1. Run: ./start.sh")
            print("  2. Or: bash start.sh")
            print("")
            print("Distribution to friends (Mac/Linux):")
            print("  1. Zip the entire folder")
            print("  2. They extract it")
            print("  3. They run: bash start.sh")
            print("  4. Browser opens automatically")
        
        print("")
        print("  Server URL: http://localhost:5000")
        print("  Default user: alice / securePass123")
        print("")
        print("="*60 + "\n")
    
    def run(self):
        """Run complete setup"""
        try:
            self.print_header()
            self.check_python()
            self.create_venv()
            self.install_dependencies()
            self.create_startup_scripts()
            self.create_config()
            self.print_next_steps()
            return True
        except Exception as e:
            print(f"\n✗ Setup failed: {e}")
            return False

if __name__ == "__main__":
    setup = Setup()
    success = setup.run()
    sys.exit(0 if success else 1)
