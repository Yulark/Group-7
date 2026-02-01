# 🎯 Despite Group Access Control System v2.0

## 🚀 Quick Start (Choose Your OS)

### Windows 🪟
```
1. Extract this folder
2. Double-click: start.bat
3. Wait for browser to open
4. Login: alice / securePass123
5. Done!
```

### Mac 🍎
```
1. Extract this folder
2. Open Terminal
3. Type: cd [folder path]
4. Type: bash start.sh
5. Wait for browser to open
6. Login: alice / securePass123
7. Done!
```

### Linux 🐧
```
1. Extract this folder
2. Open Terminal
3. Type: cd [folder path]
4. Type: bash start.sh
5. Wait for browser to open
6. Login: alice / securePass123
7. Done!
```

---

## ❓ Requirements

- **Python 3.8+** (Install from https://python.org)
- **Browser** (Chrome, Firefox, Safari, Edge)
- **2GB RAM minimum**
- **Internet**: Not required (works offline)

---

## 🎓 First Time Setup

1. **Install Python** (if not already)
   - https://python.org
   - **Important**: Check "Add Python to PATH"
   - Restart computer after installing

2. **Extract this folder**
   - Right-click → Extract All (Windows)
   - Double-click to extract (Mac/Linux)

3. **Run the application**
   - **Windows**: Double-click `start.bat`
   - **Mac/Linux**: Run `bash start.sh` in Terminal

4. **First run takes 2-3 minutes**
   - It's installing packages (only happens once)
   - Wait for "Running on http://localhost:5000"
   - Browser opens automatically

5. **Login with demo account**
   - Username: `alice`
   - Password: `securePass123`

---

## 👤 Demo Accounts

| User | Password | Role |
|------|----------|------|
| alice | securePass123 | Creator |
| bob | adminPass456 | Admin |
| diana | pr_manager123 | PR Manager |
| charlie | analyst789 | Analyst |

Try different users to see different features!

---

## 🌐 Access Addresses

- **Local machine**: http://localhost:5000
- **Same network**: http://[machine-ip]:5000
- **Get IP**:
  - Windows: Run `ipconfig` in Command Prompt
  - Mac/Linux: Run `hostname -I` in Terminal

---

## 🔒 Security Features

### View These on Security Page (Click "🔒 Security" in sidebar):

1. **Risk Assessment** - Real-time risk score (0-100)
2. **Behavioral Analysis** - Detect unusual activity
3. **Compliance Status** - Policy enforcement
4. **Device Security** - Device fingerprinting
5. **Threat Detection** - Active monitoring
6. **Rate Limiting** - DDoS protection

### Try These Buttons:
- **📱 Initiate MFA** - Multi-factor authentication
- **📤 Request Elevated Access** - Permission escalation
- **✓ Verify Device** - Device validation

---

## 🆘 Troubleshooting

### Problem: "Python not found"
**Solution**: Install Python from https://python.org
- Check "Add Python to PATH"
- Restart computer

### Problem: Script won't run
**Solution**:
- Windows: Make sure `start.bat` exists
- Mac/Linux: Make sure `start.sh` exists
- Try running in Administrator/sudo mode

### Problem: Port 5000 already in use
**Solution**: Edit `run_server.py` line 55, change 5000 to 5001

### Problem: Very slow first run
**Solution**: This is normal (installing packages)
- Can take 2-5 minutes
- Wait until you see "Running on http://localhost:5000"

### Problem: Browser doesn't open automatically
**Solution**: Open manually
- Type in browser: `http://localhost:5000`
- Server will still be running

---

## ⏹️ Stopping the Application

**Press CTRL+C** in the terminal/command prompt

Changes are NOT saved (resets on restart)

---

## 📁 Folder Contents

```
AccessControlSystem/
├── start.bat ..................... (Windows launcher - double-click)
├── start.sh ....................... (Mac/Linux launcher - bash start.sh)
├── launcher.py .................... (Universal launcher - python3 launcher.py)
├── setup.py ....................... (Setup script - auto-runs if needed)
├── run_server.py .................. (Main application file)
├── requirements.txt ............... (Python dependencies)
├── app/ ........................... (Application code)
├── README.md ...................... (Project overview)
├── GETTING_STARTED.md ............ (Detailed guide)
├── INSTANT_START.md .............. (Super quick start)
└── [other documentation files]
```

---

## 🚀 Advanced Usage

### Run with Custom Port
Edit `run_server.py`:
```python
app.run(debug=True, host='0.0.0.0', port=3000)  # Change port here
```

### Access from Specific IP Only
Edit `run_server.py`:
```python
app.run(debug=True, host='192.168.1.100', port=5000)  # Set IP here
```

### Disable Auto-Browser Open
Edit `run_server.py`, comment out:
```python
# timer = Timer(2, open_browser)
# timer.daemon = True
# timer.start()
```

---

## 📚 Documentation

- **INSTANT_START.md** - Ultra quick (1 min read)
- **GETTING_STARTED.md** - Full guide (10 min read)
- **QUICK_REFERENCE.md** - Feature overview (5 min read)
- **SECURITY_TESTING_GUIDE.md** - Testing guide (15 min read)
- **ADVANCED_SECURITY_FEATURES.md** - Technical docs (30 min read)

---

## 🎯 Common Tasks

### Change Demo User Password
Edit `app/models.py`:
```python
"alice": {"password": "newpassword", "role": "Creator"}
```

### Add New User
Edit `app/models.py`:
```python
"yourname": {"password": "yourpassword", "role": "Creator"}
```

### Access on Mobile Device
1. Run app on computer
2. Find computer IP (see Troubleshooting)
3. On phone: `http://<COMPUTER_IP>:5000`
4. Use same login

---

## ✅ Verification Checklist

Everything working if you see:
- ✅ Terminal shows: "Running on http://127.0.0.1:5000"
- ✅ Browser opens automatically
- ✅ Login page displays
- ✅ Can login with alice/securePass123
- ✅ Dashboard loads
- ✅ All menu items clickable
- ✅ Security section shows 6 cards
- ✅ Dark/light theme toggle works

---

## 📞 Support

1. Check documentation files (*.md)
2. Review error messages carefully
3. Try restarting (close and run again)
4. Delete `venv` folder and retry

---

## 🎉 Ready to Start?

### Windows 🪟
**Double-click:** `start.bat`

### Mac/Linux 🍎🐧
**Run:** `bash start.sh`

---

## 📊 System Information

- **Version**: 2.0 - Advanced Security Edition
- **Framework**: Flask 3.1.2
- **Python**: 3.8 - 3.12 (recommended 3.11)
- **Database**: In-memory (demo)
- **License**: Open Source

---

## 🛡️ Security Note

This is a **demo/testing version**:
- Data resets on restart
- No persistent database
- Perfect for learning & testing
- See docs for production setup

---

**Have fun!** 🎉

Questions? Check the documentation files included!
