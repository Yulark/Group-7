#!/usr/bin/env python3
"""
Despite Group Access Control System - Universal Launcher
Works on Windows, macOS, Linux
Automatically detects OS and starts the application
"""

import os
import sys
import subprocess
import webbrowser
import platform
import time
from pathlib import Path

class Launcher:
    def __init__(self):
        self.os_type = platform.system()
        self.base_dir = Path(__file__).parent
        self.venv_dir = self.base_dir / "venv"
        self.is_windows = self.os_type == "Windows"
        
    def print_header(self):
        """Print header"""
        print("\n" + "="*70)
        print("  DESPITE GROUP ACCESS CONTROL SYSTEM v2.0")
        print("  Universal Launcher")
        print("="*70)
        print(f"  OS: {self.os_type}")
        print(f"  Python: {platform.python_version()}")
        print("="*70 + "\n")
    
    def check_python(self):
        """Check if Python is available"""
        print("[*] Checking Python installation...")
        
        version = sys.version_info
        if version.major < 3 or (version.major == 3 and version.minor < 8):
            print(f"[ERROR] Python 3.8+ required (current: {version.major}.{version.minor})")
            print("\nInstall from: https://python.org")
            sys.exit(1)
        
        print(f"[OK] Python {version.major}.{version.minor} found\n")
    
    def get_venv_python(self):
        """Get Python executable from venv"""
        if self.is_windows:
            return self.venv_dir / "Scripts" / "python.exe"
        else:
            return self.venv_dir / "bin" / "python"
    
    def venv_exists(self):
        """Check if venv exists"""
        return (self.venv_dir / ("Scripts" if self.is_windows else "bin")).exists()
    
    def check_venv(self):
        """Check and create venv if needed"""
        print("[*] Checking virtual environment...")
        
        if self.venv_exists():
            print("[OK] Virtual environment found\n")
            return True
        
        print("[*] Creating virtual environment...")
        try:
            subprocess.run(
                [sys.executable, "-m", "venv", str(self.venv_dir)],
                check=True,
                capture_output=True
            )
            print("[OK] Virtual environment created\n")
            return True
        except Exception as e:
            print(f"[ERROR] Failed to create venv: {e}")
            return False
    
    def install_deps(self):
        """Install dependencies"""
        print("[*] Installing dependencies...")
        
        req_file = self.base_dir / "requirements.txt"
        if not req_file.exists():
            print("[ERROR] requirements.txt not found")
            return False
        
        venv_python = str(self.get_venv_python())
        
        try:
            # Upgrade pip
            subprocess.run(
                [venv_python, "-m", "pip", "install", "--quiet", "--upgrade", "pip"],
                check=False,
                capture_output=True,
                timeout=60
            )
            
            # Install requirements
            subprocess.run(
                [venv_python, "-m", "pip", "install", "--quiet", "-r", str(req_file)],
                check=True,
                timeout=120
            )
            
            print("[OK] Dependencies installed\n")
            return True
        except subprocess.TimeoutExpired:
            print("[WARNING] Installation timed out (may still work)")
            return True
        except Exception as e:
            print(f"[ERROR] Failed to install dependencies: {e}")
            return False
    
    def start_server(self):
        """Start Flask server"""
        print("="*70)
        print("  [OK] READY TO START")
        print("="*70)
        print("\n  Server Details:")
        print("    URL: http://localhost:5000")
        print("    Status: Starting...")
        print("\n  Demo Credentials:")
        print("    - alice / securePass123 (Creator)")
        print("    - bob / adminPass456 (Admin)")
        print("    - diana / pr_manager123 (PR_Manager)")
        print("    - charlie / analyst789 (Analyst)")
        print("\n  [!] Press CTRL+C to stop server")
        print("="*70 + "\n")
        
        venv_python = str(self.get_venv_python())
        
        try:
            # Try to open browser
            try:
                # Open in 2 seconds
                time.sleep(2)
                webbrowser.open('http://localhost:5000')
            except:
                pass
            
            # Run server
            subprocess.run(
                [venv_python, str(self.base_dir / "run_server.py")],
                check=False
            )
        except KeyboardInterrupt:
            print("\n\n[*] Server stopped by user")
        except Exception as e:
            print(f"\n[ERROR] Failed to start server: {e}")
            return False
        
        return True
    
    def run(self):
        """Run complete launcher"""
        try:
            self.print_header()
            self.check_python()
            
            if not self.check_venv():
                return False
            
            if not self.install_deps():
                print("[WARNING] Continuing despite dependency issues...")
            
            self.start_server()
            return True
        except KeyboardInterrupt:
            print("\n[*] Launcher interrupted")
            return False
        except Exception as e:
            print(f"\n[ERROR] Launcher failed: {e}")
            return False

if __name__ == "__main__":
    launcher = Launcher()
    success = launcher.run()
    sys.exit(0 if success else 1)
