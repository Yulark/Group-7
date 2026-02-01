# SETUP & RUN GUIDE - Modern UI Version

## System Requirements

- Windows 10 or later
- Python 3.7+ installed and added to PATH
- Modern web browser (Chrome, Firefox, Safari, or Edge)

## Installation Steps

### Step 1: Verify Python Installation

Open Command Prompt or PowerShell and run:

```bash
python --version
```

You should see: `Python 3.x.x` (version 3.7 or higher)

**If Python is not found:**
1. Download from https://www.python.org/downloads/
2. During installation, check ✅ "Add Python to PATH"
3. Restart your computer
4. Verify with `python --version` again

### Step 2: Install Dependencies

Navigate to the project directory and install required packages:

```bash
cd "c:\Users\Yulark\OneDrive\Desktop\Group"
pip install -r requirements.txt
```

**Expected packages installed:**
- Flask 3.0.0
- Werkzeug 3.0.1
- Jinja2 3.1.2

### Step 3: Run the Server

Choose one of these methods:

#### Method 1: Using Python (Recommended)
```bash
python run_server.py
```

#### Method 2: Using Flask CLI
```bash
python -m flask run --host=0.0.0.0 --port=5000
```

#### Method 3: Using Batch File (Windows)
```bash
run.bat
```

**Expected output:**
```
 * Serving Flask app 'app'
 * Debug mode: off
 * Running on http://0.0.0.0:5000
```

### Step 4: Access the Application

Open your web browser and navigate to:

1. **Homepage**: http://localhost:5000
2. **Login Page**: http://localhost:5000/login
3. **Dashboard**: http://localhost:5000/dashboard (after login)

## Using the Dark/Light Mode Theme

### Automatic Theme Toggle Button
- **Location**: Bottom-right corner of every page
- **Size**: 50x50 pixels
- **Appearance**: 
  - 🌙 Moon icon = Light mode active (click to switch to dark)
  - ☀️ Sun icon = Dark mode active (click to switch to light)

### Keyboard Shortcut
- Press **Alt + T** on any page to toggle theme

### Theme Persistence
- Your theme choice is saved in browser's localStorage
- Theme automatically loads on next visit
- Works across all pages in the application

### System Preference
- If no saved preference, system dark/light mode is used
- This can be changed in your OS settings or by clicking the toggle button

## Demo Credentials

Login with any of these demo accounts:

### Admin Account
- **Username**: `admin`
- **Password**: `admin@123`
- **Role**: Administrator
- **Access**: Full system access, all permissions

### Regular User
- **Username**: `user`
- **Password**: `user@123`
- **Role**: User
- **Access**: Standard permissions, read-only access to reports

### HR Manager
- **Username**: `hr`
- **Password**: `hr@123`
- **Role**: HR Manager
- **Access**: Employee management, access requests

### Department Manager
- **Username**: `manager`
- **Password**: `manager@123`
- **Role**: Department Manager
- **Access**: Department-specific access control

## Features to Test

### 1. Theme Switching
- [ ] Click the theme toggle button in bottom-right
- [ ] Observe smooth transition to dark/light mode
- [ ] Verify all colors adapt correctly
- [ ] Check that text remains readable

### 2. Login Page
- [ ] Login page uses modern design
- [ ] Try entering a demo credential
- [ ] Click "Login" button
- [ ] Observe smooth theme in login form
- [ ] Test theme toggle during login

### 3. Dashboard
- [ ] Dashboard displays your user information
- [ ] Theme toggle works on dashboard
- [ ] All sections visible in both themes:
  - Overview with stats
  - Permissions section
  - Access control test scenarios
  - System reports
- [ ] Menu items navigate between sections

### 4. Access Control Testing
- [ ] Navigate to "Access Control Test" section
- [ ] Select a test scenario
- [ ] Execute the test
- [ ] View results in both themes
- [ ] Verify theme toggle doesn't break functionality

### 5. Parallax Scrolling
- [ ] Return to homepage (/index)
- [ ] Scroll down to see parallax effects
- [ ] Toggle theme while scrolling
- [ ] Verify parallax works in both light and dark modes

### 6. Form Submissions
- [ ] Test access requests
- [ ] Submit forms in both themes
- [ ] Verify form validation works
- [ ] Check API responses in both modes

## Troubleshooting

### Issue: "Python was not found"
**Solution**: 
1. Install Python from https://www.python.org/downloads/
2. Select "Add Python to PATH" during installation
3. Restart your computer
4. Run `python --version` to verify

### Issue: "ModuleNotFoundError: No module named 'flask'"
**Solution**:
```bash
pip install flask werkzeug jinja2
```

### Issue: "Port 5000 already in use"
**Solution**: Use a different port
```bash
python -m flask run --host=0.0.0.0 --port=5001
```

### Issue: "Theme not switching"
**Solution**:
1. Clear browser cache (Ctrl+Shift+Delete)
2. Close and reopen browser
3. Try a different browser
4. Check browser console (F12) for errors

### Issue: "Theme not persisting after refresh"
**Solution**:
1. Verify localStorage is enabled in browser settings
2. Check browser console for errors (F12)
3. Try incognito/private mode (won't persist by design)

### Issue: "Dark mode colors incorrect"
**Solution**:
1. Hard refresh: Ctrl+F5 (or Cmd+Shift+R on Mac)
2. Clear browser cache
3. Check that theme.css loaded (F12 → Network → theme.css)

## File Structure Overview

```
Group/
├── app/
│   ├── __init__.py              - Flask app factory
│   ├── models.py                - Business logic, access control
│   ├── routes.py                - API endpoints and routes
│   ├── templates/
│   │   ├── index.html          - Modern homepage
│   │   ├── login.html          - Modern login page
│   │   └── dashboard.html      - Modern dashboard
│   └── static/
│       ├── css/
│       │   ├── theme.css       - Theme system (NEW)
│       │   ├── style.css       - Main styles (UPDATED)
│       │   ├── dashboard.css   - Dashboard styles (UPDATED)
│       │   ├── login.css       - Login styles (UPDATED)
│       │   └── parallax.css    - Parallax effects
│       └── js/
│           ├── theme.js        - Theme manager (NEW)
│           ├── dashboard.js    - Dashboard interactions
│           ├── login.js        - Login form handling
│           └── parallax.js     - Parallax scrolling
├── requirements.txt             - Python dependencies
├── run_server.py               - Server launcher
├── run.bat                     - Windows batch launcher
├── README.md                   - Project documentation
├── MODERN_UI_IMPLEMENTATION.md - UI implementation details
└── SETUP_RUN_GUIDE.md          - This file
```

## Next Steps

1. **Install Python** (if not already installed)
2. **Install dependencies**: `pip install -r requirements.txt`
3. **Run the server**: `python run_server.py`
4. **Open browser**: http://localhost:5000
5. **Test theme toggle**: Click the moon/sun button
6. **Login**: Use admin/admin@123
7. **Explore dashboard**: Try different sections
8. **Enjoy the modern UI!**

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the MODERN_UI_IMPLEMENTATION.md for detailed technical info
3. Check browser console (F12) for error messages
4. Verify all dependencies are installed: `pip list`

## What's New in This Version

✨ **Modern UI Features:**
- Dark mode and light mode theme system
- Smooth theme transitions (300ms)
- Persistent user preferences (localStorage)
- System preference detection
- Keyboard shortcut (Alt+T) for theme toggle
- Responsive design for all screen sizes
- Modern card-based layouts
- Enhanced visual hierarchy
- Accessible color contrasts

🔒 **Security Features Preserved:**
- Zero Trust Architecture
- Role-based access control
- Device security validation
- Audit logging system (5 log types)
- Session management (15-minute timeout)
- DRM content protection
- All 6+ API endpoints functional

## Happy Exploring! 🚀

The Despite Group Access Control System now features a modern, professional UI with full dark/light mode support while maintaining complete security and functionality.
