# 🚀 Ultra Quick Start - Despite Group Access Control System

## ⚡ One-Click Start

### Windows 🪟
```
Double-click: start.bat
```

### macOS 🍎
```
bash start.sh
```

### Linux 🐧
```
bash start.sh
```

---

## 📝 Or Step-by-Step

### Windows (Command Prompt)
```batch
REM 1. Extract folder
cd C:\Path\To\Folder

REM 2. Run launcher
python launcher.py

REM That's it! Server starts automatically
```

### macOS/Linux (Terminal)
```bash
# 1. Extract folder
cd /path/to/folder

# 2. Run launcher
python3 launcher.py

# That's it! Server starts automatically
```

---

## 🌐 Access Application

Once you see:
```
Running on http://127.0.0.1:5000
```

**Browser opens automatically!**

If not, go to: **http://localhost:5000**

---

## 👤 Login

```
Username: alice
Password: securePass123
```

(Try bob/adminPass456 for admin access)

---

## ⏹️ Stop Server

Press: **CTRL+C** in terminal

---

## 📱 Access from Other Device (Same Network)

Find server IP address:
- **Windows**: `ipconfig` (look for IPv4 Address)
- **Mac/Linux**: `hostname -I`

Then visit: `http://<IP_ADDRESS>:5000`

Example: `http://192.168.1.100:5000`

---

## 🆘 Troubleshooting

### "Python not found"
- Install Python 3.8+: https://python.org
- Make sure "Add to PATH" is checked
- Restart terminal after install

### "Port 5000 in use"
- Edit `run_server.py` line 55, change 5000 to 5001
- Retry

### "venv not found"
- Delete `venv` folder
- Run script again
- It recreates automatically

---

## ✅ That's All!

Everything else happens automatically:
- ✅ Virtual environment created
- ✅ Dependencies installed
- ✅ Server started
- ✅ Browser opened
- ✅ Ready to use!

---

## 📦 Send to Friends

1. Zip the entire folder
2. Email to friend
3. Friend extracts
4. Friend runs `start.bat` (Windows) or `bash start.sh` (Mac/Linux)
5. Done!

---

**Ready? Start now!** 🎉
