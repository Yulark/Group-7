# 📖 Complete Installation & Distribution Manual

## Table of Contents
1. [Quick Start](#quick-start)
2. [Detailed Installation](#detailed-installation)
3. [Running the Application](#running-the-application)
4. [Distributing to Friends](#distributing-to-friends)
5. [Troubleshooting](#troubleshooting)
6. [Advanced Configuration](#advanced-configuration)

---

## Quick Start

### Windows 🪟
```
1. Extract folder
2. Double-click: start.bat
3. Wait for server message
4. Browser opens automatically
5. Login: alice / securePass123
```

### macOS 🍎
```
1. Extract folder
2. Open Terminal, cd to folder
3. Run: bash start.sh
4. Wait for server message
5. Browser opens automatically
6. Login: alice / securePass123
```

### Linux 🐧
```
1. Extract folder
2. Open Terminal, cd to folder
3. Run: bash start.sh
4. Wait for server message
5. Browser opens automatically
6. Login: alice / securePass123
```

---

## Detailed Installation

### Prerequisites

#### Windows 🪟
1. **Python 3.8+**
   - Download from: https://python.org/downloads
   - Click "Windows installer" for your version (64-bit recommended)
   - During installation:
     - ✅ Check "Add Python to PATH"
     - ✅ Check "Install for all users"
     - Click "Install Now"
   - Verify: Open Command Prompt, type `python --version`

2. **Git (Optional)**
   - Download from: https://git-scm.com
   - Default settings OK
   - For cloning repository

3. **Text Editor (Optional)**
   - VS Code: https://code.visualstudio.com
   - Sublime Text: https://sublimetext.com
   - For editing configuration

#### macOS 🍎
1. **Python 3.8+**
   ```bash
   # Using Homebrew (recommended)
   brew install python3
   
   # Or download from https://python.org
   ```
   - Verify: Open Terminal, type `python3 --version`

2. **Homebrew (if not installed)**
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

3. **Git (Optional)**
   ```bash
   brew install git
   ```

#### Linux (Ubuntu/Debian) 🐧
```bash
# Update package list
sudo apt-get update

# Install Python and dependencies
sudo apt-get install python3 python3-venv python3-pip python3-dev

# Verify
python3 --version
```

#### Linux (Fedora/CentOS) 🔴
```bash
# Install Python
sudo dnf install python3 python3-pip

# Verify
python3 --version
```

---

## Running the Application

### Method 1: Easiest (Recommended)

#### Windows 🪟
```
1. Extract folder
2. Double-click: start.bat
3. Done!
```

#### Mac/Linux 🍎🐧
```bash
cd /path/to/folder
bash start.sh
# Or
chmod +x start.sh
./start.sh
```

### Method 2: Python Launcher

#### Windows/Mac/Linux
```bash
cd /path/to/folder
python3 launcher.py
# Or
python launcher.py
```

### Method 3: Manual Setup

#### Windows
```batch
cd C:\path\to\folder
python -m venv venv
call venv\Scripts\activate.bat
pip install -r requirements.txt
python run_server.py
```

#### Mac/Linux
```bash
cd /path/to/folder
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 run_server.py
```

### What You Should See

```
========================================================
DESPITE GROUP ACCESS CONTROL SYSTEM v2.0
========================================================
[OK] Python found: Python 3.11.0
[*] Checking virtual environment...
[OK] Virtual environment found
[*] Installing dependencies...
[OK] Dependencies installed

[OK] READY TO START
========================================================

 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
```

### Access Application

**Automatic**: Browser opens at http://localhost:5000

**Manual**: Type in browser: `http://localhost:5000`

---

## Distributing to Friends

### Step 1: Prepare the Folder

The folder should contain:
```
AccessControlSystem/
├── start.bat                 ← Windows users run this
├── start.sh                  ← Mac/Linux users run this
├── launcher.py               ← Or this (works on all OS)
├── setup.py                  ← Auto-setup
├── run_server.py             ← Main app
├── requirements.txt          ← Dependencies
├── app/                      ← Application code
├── README.md                 ← Overview
├── README_DISTRIBUTION.md    ← For friends
├── GETTING_STARTED.md        ← Installation guide
├── INSTANT_START.md          ← Quick start
└── [other documentation]
```

### Step 2: Create Distribution Package

#### Windows 🪟
```
1. Right-click folder → Send to → Compressed (Zipped) folder
2. Name: AccessControlSystem.zip
3. Send via email or file sharing
```

#### Mac 🍎
```bash
# In Terminal
zip -r AccessControlSystem.zip AccessControlSystem/
# File "AccessControlSystem.zip" created
# Drag to email or upload to cloud storage
```

#### Linux 🐧
```bash
# In Terminal
tar -czf AccessControlSystem.tar.gz AccessControlSystem/
# File "AccessControlSystem.tar.gz" created
# Send via email or file sharing
```

### Step 3: Share with Friends

**Option A: Email**
- Attach: AccessControlSystem.zip
- Include message from "README_DISTRIBUTION.md"

**Option B: Cloud Storage**
- Upload to Google Drive
- Upload to Dropbox
- Upload to OneDrive
- Share link with friends

**Option C: File Sharing**
- Use WeTransfer: https://wetransfer.com
- Use Mega: https://mega.nz
- Use File sharing service

### Step 4: Friends Can Run

#### Friends on Windows 🪟
```
1. Download and extract zip
2. Double-click: start.bat
3. Done! Server starts automatically
```

#### Friends on Mac/Linux 🍎🐧
```bash
1. Download and extract zip
2. cd to folder
3. bash start.sh
4. Done! Server starts automatically
```

---

## Troubleshooting

### Issue: "Python not found"

**Problem**: Getting error "python not found" or "python is not recognized"

**Solution**:
1. Install Python from https://python.org
2. **Important**: During installation, check "Add Python to PATH"
3. Restart computer
4. Try again

**Verify**:
- Windows: Open Command Prompt, type `python --version`
- Mac/Linux: Open Terminal, type `python3 --version`

---

### Issue: Port 5000 Already in Use

**Problem**: Error "Address already in use"

**Solution Option 1**: Stop other application using port 5000
- Close other applications
- Restart your computer

**Solution Option 2**: Use different port
1. Edit: `run_server.py`
2. Find line ~55: `app.run(..., port=5000)`
3. Change 5000 to another number (e.g., 5001, 8000, 3000)
4. Restart application
5. Access at: `http://localhost:5001`

---

### Issue: Virtual Environment Error

**Problem**: "venv/Scripts/python.exe not found" or "venv permission denied"

**Solution**:
1. Delete the `venv` folder completely
2. Run the script again
3. It will recreate `venv` automatically

**For Windows**:
```batch
rmdir /s /q venv
start.bat
```

**For Mac/Linux**:
```bash
rm -rf venv
bash start.sh
```

---

### Issue: Slow First Run

**Problem**: Script takes 2-5 minutes first time

**Solution**: This is normal!
- First run installs packages (~300MB)
- Subsequent runs are instant
- Just wait for "Running on http://127.0.0.1:5000"

---

### Issue: Browser Doesn't Open

**Problem**: Server starts but browser doesn't open

**Solution**:
1. Manually open browser
2. Type: `http://localhost:5000`
3. Server is still running (you can see it in terminal)

---

### Issue: "SSL: CERTIFICATE_VERIFY_FAILED"

**Problem**: Error about SSL certificates

**Solution**:
```bash
# Mac/Linux
python3 -m pip install --upgrade certifi

# Or run this if available
/Applications/Python\ 3.x/Install\ Certificates.command

# Windows
python -m pip install --upgrade certifi
```

---

### Issue: Permission Denied (Mac/Linux)

**Problem**: Error "Permission denied" when running .sh file

**Solution**:
```bash
# Make file executable
chmod +x start.sh

# Then run
bash start.sh
```

---

### Issue: Firewall Blocking

**Problem**: Can't access from another computer

**Solution**:
1. Windows: Check Windows Defender Firewall
   - Settings → Firewall → Allow an app
   - Add Python
2. Mac: Security & Privacy → Firewall Options
3. Linux: Check iptables or ufw settings

---

### Issue: "Module Not Found"

**Problem**: Error about missing module (Flask, werkzeug, etc.)

**Solution**:
```bash
# Windows
python -m pip install -r requirements.txt

# Mac/Linux
python3 -m pip install -r requirements.txt
```

---

### Issue: Can't Access from Other Machine

**Problem**: Other computer can't reach http://localhost:5000

**Solution**:
1. Find server's IP address
   - **Windows**: `ipconfig` (look for "IPv4 Address")
   - **Mac/Linux**: `hostname -I` or `ifconfig`
   
2. Access from other machine:
   - `http://<SERVER_IP>:5000`
   - Example: `http://192.168.1.100:5000`

---

## Advanced Configuration

### Change Default Port

Edit `run_server.py`:
```python
if __name__ == '__main__':
    # ... code ...
    app.run(
        debug=True,
        host='0.0.0.0',
        port=8000  # Change 5000 to desired port
    )
```

### Bind to Specific IP

Edit `run_server.py`:
```python
app.run(
    debug=True,
    host='192.168.1.100',  # Only this IP
    port=5000
)
```

### Disable Auto-Browser Open

Edit `run_server.py`, comment out:
```python
# timer = Timer(2, open_browser)
# timer.daemon = True
# timer.start()
```

### Add Custom Users

Edit `app/models.py`:
```python
User.users_db = {
    "alice": {"password": "securePass123", "role": "Creator"},
    "bob": {"password": "adminPass456", "role": "Admin"},
    # Add new users:
    "john": {"password": "johnpass123", "role": "Creator"},
    "jane": {"password": "janepass456", "role": "Analyst"}
}
```

### Change Security Settings

Edit `app/models.py`, find configuration section:
```python
# Rate Limiting
RATE_LIMIT = 100  # requests per hour

# MFA Configuration
MFA_EXPIRY_MINUTES = 5
MFA_MAX_ATTEMPTS = 3

# Session timeout
SESSION_TIMEOUT_MINUTES = 30
```

### Enable Detailed Logging

Edit `run_server.py`:
```python
if __name__ == '__main__':
    app.run(
        debug=True,  # Set to True for detailed errors
        host='0.0.0.0',
        port=5000
    )
```

---

## Performance Optimization

### Minimum Requirements
- Python: 3.8+
- RAM: 2GB
- Disk: 500MB
- Browser: Latest version

### Recommended Specs
- Python: 3.11+
- RAM: 4GB+
- Disk: 1GB
- SSD recommended
- Multi-core processor

### Speed Tips
- Use SSD instead of HDD
- Close other applications
- Use latest Python version (3.11+)
- Disable browser extensions
- Clear browser cache periodically

---

## Deployment Checklist

Before distributing to friends, verify:

- ✅ Python installed and working
- ✅ All files present and readable
- ✅ requirements.txt has all dependencies
- ✅ start.bat works on Windows
- ✅ start.sh works on Mac/Linux
- ✅ launcher.py works universally
- ✅ Application starts without errors
- ✅ Can login with demo credentials
- ✅ All pages load correctly
- ✅ Dark/light theme works
- ✅ Security features accessible
- ✅ No error messages
- ✅ Documentation is complete
- ✅ README files are clear

---

## Support Documentation

Include these files when distributing:

1. **README_DISTRIBUTION.md** - For friends (START HERE)
2. **INSTANT_START.md** - Ultra quick 1-minute setup
3. **GETTING_STARTED.md** - Detailed installation
4. **QUICK_REFERENCE.md** - Feature overview
5. **SECURITY_TESTING_GUIDE.md** - Testing procedures
6. **ADVANCED_SECURITY_FEATURES.md** - Technical details

---

## Version Information

- **Project**: Despite Group Access Control System
- **Version**: 2.0 - Advanced Security Edition
- **Python**: 3.8 - 3.12 (3.11 recommended)
- **Framework**: Flask 3.1.2
- **Last Updated**: January 15, 2026
- **Status**: Production Ready

---

## Summary

### To Run Locally:
1. Install Python 3.8+
2. Extract folder
3. Run: `start.bat` (Windows) or `bash start.sh` (Mac/Linux)
4. Done!

### To Send to Friends:
1. Zip the entire folder
2. Email or upload to cloud
3. Friends extract and run
4. They're done!

### For Help:
- Check included documentation
- Review troubleshooting section
- Verify Python installation
- Check file permissions

---

## Contact & Support

For issues or questions:
1. Check documentation files
2. Review error messages carefully
3. Try restarting application
4. Delete `venv` and retry
5. Verify Python installation

---

**Happy Deploying!** 🎉

The application is designed to work across all platforms with minimal setup.
Share it freely with your friends!
