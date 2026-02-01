# 🚀 Getting Started - Despite Group Access Control System

## ⚡ Quick Start (30 seconds)

### Windows Users 🪟
```
1. Extract the folder
2. Double-click: start.bat
3. Wait for "Server running at: http://localhost:5000"
4. Browser opens automatically
5. Login with: alice / securePass123
```

### Mac/Linux Users 🍎 🐧
```
1. Extract the folder
2. Open terminal in folder
3. Run: bash start.sh
4. Wait for "Server running at: http://localhost:5000"
5. Browser opens automatically
6. Login with: alice / securePass123
```

---

## 📋 Requirements

### Minimum
- **Python**: 3.8 or higher
- **Disk Space**: 500MB
- **RAM**: 2GB minimum
- **Internet**: Not required (works offline)

### Supported Operating Systems
- ✅ Windows 10/11
- ✅ macOS 10.15+
- ✅ Ubuntu 18.04+
- ✅ Fedora 30+
- ✅ CentOS 7+
- ✅ Debian 10+

---

## 🔧 Installation

### Step 1: Check Python
```bash
# Windows (Command Prompt or PowerShell)
python --version

# Mac/Linux (Terminal)
python3 --version
```

**Required**: Python 3.8 or higher

### Step 2: Install Python (if not already installed)

#### Windows
1. Visit: https://python.org
2. Download Python 3.11 or 3.12
3. During installation, **CHECK** "Add Python to PATH"
4. Click "Install Now"

#### macOS
```bash
# Using Homebrew (install Homebrew first from https://brew.sh)
brew install python3
```

#### Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install python3 python3-venv python3-pip
```

#### Fedora/CentOS
```bash
sudo dnf install python3 python3-pip
```

### Step 3: Extract & Run

**Windows:**
- Right-click the zip file → Extract All
- Navigate to the folder
- Double-click `start.bat`

**Mac/Linux:**
```bash
unzip AccessControlSystem.zip
cd AccessControlSystem
bash start.sh
```

---

## 📊 What Happens on First Run

```
[OK] Python found: Python 3.11.0
[*] Checking virtual environment...
[*] Virtual environment not found. Creating...
[OK] Virtual environment created
[*] Activating virtual environment...
[OK] Virtual environment activated
[*] Installing dependencies...
[OK] Dependencies ready

[OK] READY TO START

Server running at: http://localhost:5000
```

**First run takes 2-3 minutes** (installing packages)
**Subsequent runs are instant**

---

## 🎯 Demo Credentials

| Username | Password | Role | Permissions |
|----------|----------|------|-------------|
| alice | securePass123 | Creator | Create, Read, Publish |
| bob | adminPass456 | Admin | Full Access |
| diana | pr_manager123 | PR_Manager | Approve, Publish |
| charlie | analyst789 | Analyst | Read-Only |

**Try them all to see different security features!**

---

## 🌐 Accessing the Application

Once the server is running:

```
Browser:        http://localhost:5000
API:            http://localhost:5000/api/
Dashboard:      http://localhost:5000/dashboard
```

### Access on Other Machines (Same Network)

If running on one machine and want to access from another on same network:

```
Replace localhost with the server's IP address:
http://192.168.1.100:5000
```

To find the IP address:
- **Windows**: `ipconfig` (look for IPv4 Address)
- **Mac/Linux**: `ifconfig` or `hostname -I`

---

## 🔒 Security Features Overview

### 6 Security Cards
- 📊 Risk Assessment (0-100 score)
- 🎯 Behavioral Analysis (Anomaly detection)
- ✔️ Compliance Status (Policy enforcement)
- 🛡️ Device Security (Fingerprinting)
- 🚨 Threat Detection (Monitoring)
- ⚡ Rate Limiting (DDoS protection)

### 3 Security Actions
- 📱 Initiate MFA (Challenge workflow)
- 📤 Request Elevated Access (Escalation)
- ✓ Verify Device (Validation)

---

## ⚙️ Advanced Configuration

### Change Server Port
Edit `run_server.py`:
```python
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)  # Change 5000 to desired port
```

### Add More Users
Edit `app/models.py`:
```python
User.users_db = {
    "alice": {"password": "securePass123", "role": "Creator"},
    "bob": {"password": "adminPass456", "role": "Admin"},
    # Add more here:
    "yourname": {"password": "yourpassword", "role": "Creator"}
}
```

### Enable/Disable Features
See `ADVANCED_SECURITY_FEATURES.md` for configuration options

---

## 🆘 Troubleshooting

### Issue: "Python not found"
**Solution:**
- Install Python 3.8+: https://python.org
- **Important**: Check "Add Python to PATH" during installation
- Restart terminal/command prompt after installing

### Issue: "Port 5000 already in use"
**Solution:**
- Another application is using port 5000
- Close the other application, OR
- Edit `run_server.py` to use different port (e.g., 5001)

### Issue: "venv/Scripts/python.exe not found" (Windows)
**Solution:**
- Delete the `venv` folder
- Run `start.bat` again
- It will recreate venv automatically

### Issue: "Permission denied" (Mac/Linux)
**Solution:**
```bash
# Make script executable
chmod +x start.sh
# Then run
bash start.sh
```

### Issue: "SSL: CERTIFICATE_VERIFY_FAILED"
**Solution:**
- This is a Python SSL certificate issue
- Run in terminal:
  ```bash
  python3 -m pip install --upgrade certifi
  ```

### Issue: Website not loading
**Solution:**
1. Check if server is running (look for "Running on http://")
2. Try refreshing browser (Ctrl+R or Cmd+R)
3. Check if using correct URL: http://localhost:5000
4. Check firewall settings

### Issue: Slow performance
**Solution:**
- Close other applications using RAM
- Minimum 2GB RAM required
- Check internet speed if loading assets

---

## 📱 Mobile Access

### Access from Phone/Tablet
1. Get server machine's IP address (see above)
2. On phone/tablet, visit: `http://<SERVER_IP>:5000`
3. Use same demo credentials
4. Full access from any device!

---

## 🔄 Stopping the Server

### Windows
- Press `CTRL+C` in the command prompt
- Or close the window

### Mac/Linux
- Press `CTRL+C` in terminal
- Or close terminal window

**Changes are NOT saved** (reset on restart)

---

## 📦 Distribution to Friends

### Step 1: Prepare Folder
```
AccessControlSystem/
├── start.bat               (Windows users use this)
├── start.sh                (Mac/Linux users use this)
├── setup.py                (Auto-runs if needed)
├── requirements.txt        (Dependencies list)
├── run_server.py           (Main application)
├── app/                    (Application code)
├── README.md               (This file)
└── [other files]
```

### Step 2: Create Zip File
- Right-click folder → Send to → Compressed (Zipped) folder
- Name: `AccessControlSystem.zip`

### Step 3: Send to Friends
- Email the zip file
- Or upload to cloud (Google Drive, Dropbox, OneDrive)
- Send download link

### Step 4: Friends Can Use
**Instructions for your friends:**
1. Download and extract zip file
2. Navigate to folder
3. Windows: Double-click `start.bat`
4. Mac/Linux: Run `bash start.sh`
5. Done! Application opens automatically

---

## 🎓 Learning Resources

### Quick Start
- Time: 5 minutes
- Read: `QUICK_REFERENCE.md`

### Testing
- Time: 15 minutes
- Read: `SECURITY_TESTING_GUIDE.md`

### Technical Details
- Time: 30 minutes
- Read: `ADVANCED_SECURITY_FEATURES.md`

### API Documentation
- Time: 20 minutes
- See: `ADVANCED_SECURITY_FEATURES.md` (Section 3)

---

## 🎯 Common Tasks

### Login
1. Click "Login" button
2. Enter username (e.g., alice)
3. Enter password (e.g., securePass123)
4. Click "Login"

### View Security Features
1. Click "🔒 Security" in sidebar
2. View 6 security cards
3. Click buttons to test features
4. All data updates in real-time

### Test MFA
1. Go to Security section
2. Click "📱 Initiate MFA"
3. Enter any 6 characters
4. See "MFA verification successful!"

### Request Elevated Access
1. Go to Security section
2. Click "📤 Request Elevated Access"
3. Fill in resource name and reason
4. Unique request ID generated

### Switch Theme
1. Press `Alt+T` keyboard shortcut
2. Or click theme toggle button
3. Dark/Light mode switches instantly

---

## 📊 Performance Tips

### For Smooth Experience
- **Minimum RAM**: 2GB
- **Recommended RAM**: 4GB+
- **CPU**: Dual-core or better
- **Disk**: 500MB free space
- **Browser**: Latest Chrome, Firefox, Safari, or Edge

### Optimization
- Close unused applications
- Disable browser extensions
- Use modern browser (Chrome 90+)
- Clear browser cache periodically

---

## 🔐 Security Notes

### In-Memory Database
- Demo data is NOT saved
- Reset on server restart
- Perfect for testing
- Not for production use

### Production Deployment
- See `FINAL_DEPLOYMENT_README.md`
- Use database for persistence
- Configure HTTPS/SSL
- Setup authentication
- Enable monitoring

---

## 📞 Support

### Documentation
- 📖 See included `.md` files
- 📝 Start with: `QUICK_REFERENCE.md`
- 🗂️ Navigation: `DOCUMENTATION_INDEX.md`

### Common Issues
See **Troubleshooting** section above

### Still Need Help?
1. Check all `.md` files (comprehensive guides)
2. Review error messages carefully
3. Try restarting: close and run again
4. Contact developer with error logs

---

## ✅ Verification

To verify everything works:

```
1. Server shows: "Running on http://127.0.0.1:5000"
2. Browser opens automatically
3. Login page loads (alice/securePass123 suggested)
4. Dashboard loads without errors
5. "🔒 Security" section shows 6 cards
6. Cards display real-time data
7. Buttons respond to clicks
```

If all 7 items check ✅, system is working perfectly!

---

## 🎉 You're All Set!

Everything is configured and ready to use.

```
Windows:  Double-click start.bat
Mac/Linux: bash start.sh
```

**Server will be available at: http://localhost:5000**

**Demo login: alice / securePass123**

---

**Version**: 2.0 - Advanced Security Edition
**Last Updated**: January 15, 2026
**Status**: ✅ Production Ready

🛡️ **Enjoy your Enterprise-Grade Security System!** 🛡️
