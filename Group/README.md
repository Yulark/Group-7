# Despite Group Access Control System

Zero Trust Architecture & Digital Rights Management Implementation

## Project Overview

This is a complete web-based access control system implementing Zero Trust Architecture and Digital Rights Management for Despite Group of Companies' Social Media & Public Relations Department. The application demonstrates secure content management, role-based access control, and comprehensive audit logging.

## Features

### Core Security Features
- ✓ **Zero Trust Architecture** - No device or user is trusted by default
- ✓ **Role-Based Access Control (RBAC)** - Admin, Creator, PR Manager, Analyst roles
- ✓ **Digital Rights Management (DRM)** - Content watermarking and protection
- ✓ **Multi-Factor Authentication** - Enhanced security protocols
- ✓ **Device Security Verification** - Only secure devices allowed access
- ✓ **Comprehensive Audit Logging** - All access attempts recorded

### Frontend Features
- ✓ **Parallax Scrolling** - Smooth, modern UI with parallax effects
- ✓ **Responsive Design** - Works on desktop, tablet, and mobile
- ✓ **Interactive Dashboard** - Real-time access control testing
- ✓ **Secure Authentication** - Password hashing with SHA-256
- ✓ **Session Management** - 15-minute automatic timeout

### Backend Features
- ✓ **Flask Web Framework** - Lightweight and efficient
- ✓ **RESTful API** - Clean API endpoints for frontend communication
- ✓ **Access Control Module** - Implements Zero Trust validation
- ✓ **Alert System** - Real-time notifications for security events
- ✓ **Logging System** - Security events, access logs, audit trails

## Project Structure

```
Group/
├── app/
│   ├── __init__.py              # Flask app factory
│   ├── models.py                # Access control and DRM models
│   ├── routes.py                # Flask routes and API endpoints
│   ├── templates/
│   │   ├── index.html           # Home page with parallax
│   │   ├── login.html           # Login page
│   │   └── dashboard.html       # User dashboard
│   ├── static/
│   │   ├── css/
│   │   │   ├── style.css        # Main styles
│   │   │   ├── parallax.css     # Parallax effects
│   │   │   ├── login.css        # Login page styles
│   │   │   └── dashboard.css    # Dashboard styles
│   │   └── js/
│   │       ├── parallax.js      # Parallax scrolling
│   │       ├── login.js         # Login functionality
│   │       └── dashboard.js     # Dashboard interactions
│   └── logs/                    # Log files directory
├── access_control_system.py     # Standalone demo script
├── run_server.py                # Flask server entry point
├── run.bat                      # Windows batch runner
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Step 1: Install Python
If Python is not installed:
1. Visit https://www.python.org/downloads/
2. Download Python 3.10 or higher
3. **IMPORTANT**: Check "Add Python to PATH" during installation
4. Complete the installation

### Step 2: Install Dependencies
Open Command Prompt or PowerShell in the project directory:

```bash
pip install -r requirements.txt
```

This will install:
- Flask 3.0.0
- Werkzeug 3.0.1
- Jinja2 3.1.2

### Step 3: Run the Application

#### Option 1: Using Batch File (Windows)
Double-click `run.bat` to start the server automatically.

#### Option 2: Using Command Line
```bash
python run_server.py
```

The application will:
- Start on `http://localhost:5000`
- Automatically open in your default browser
- Display demo credentials in the console

## Demo Credentials

| Username | Password | Role | Details |
|----------|----------|------|---------|
| alice | securePass123 | Creator | Can create and publish content |
| bob | adminPass456 | Admin | Full system access and monitoring |
| diana | pr_manager123 | PR Manager | Can approve and monitor content |
| charlie | analyst789 | Analyst | View-only access (device security fails) |

## Usage Guide

### Home Page
- Explore the parallax scrolling homepage
- View system architecture and security features
- Read about Zero Trust Architecture implementation

### Login
1. Enter username and password from demo credentials
2. System validates credentials with SHA-256 hashing
3. Session created with 15-minute timeout
4. Redirected to dashboard on success

### Dashboard
The dashboard has several sections:

#### Overview
- User information and permissions
- Device security status
- Last login timestamp
- Permission count

#### Permissions
- View all access permissions
- View DRM licensing permissions
- Based on user role

#### Access Control Test
- Run predefined test scenarios
- See access decisions in real-time
- Verify Zero Trust validation
- Check DRM watermarking

#### Reports
- View access statistics
- System status monitoring
- Security event summary

## Access Control Test Scenarios

### Scenario 1: Creator Publishing Content
- **User**: alice (Creator)
- **Resource**: CampaignVideo.mp4
- **Action**: PUBLISH
- **Expected**: ✓ GRANTED

### Scenario 2: Admin Monitoring
- **User**: bob (Admin)
- **Resource**: AnalyticsReport.xlsx
- **Action**: MONITOR
- **Expected**: ✓ GRANTED

### Scenario 3: Analyst Attempting Publish (Should Fail)
- **User**: charlie (Analyst)
- **Resource**: SensitiveData.pdf
- **Action**: PUBLISH
- **Expected**: ✗ DENIED (insufficient permissions)

### Scenario 4: Device Security Check
- **User**: charlie (Analyst - device not secure)
- **Resource**: PublicContent.jpg
- **Action**: VIEW
- **Expected**: ✗ DENIED (device security issue)

### Scenario 5: PR Manager Approving
- **User**: diana (PR Manager)
- **Resource**: NewsArticle.html
- **Action**: APPROVE
- **Expected**: ✓ GRANTED

## Log Files

The system creates and maintains log files in `app/logs/`:

- **security_events.log** - Security alerts and violations
- **access_logs.log** - Successful access grants
- **audit_trail.log** - Complete audit trail of all activities
- **admin_alerts.log** - Critical alerts for administrators
- **drm_operations.log** - DRM watermarking operations

## API Endpoints

### Authentication
- `POST /api/login` - User login
- `POST /api/logout` - User logout
- `GET /api/user-info` - Get current user information

### Access Control
- `POST /api/request-access` - Request access to resource
- `GET /api/test-scenarios` - Get test scenarios
- `POST /api/run-test/<id>` - Run specific test
- `GET /api/access-summary` - Get access statistics

### Admin
- `GET /api/users` - List all demo users

## Technology Stack

### Backend
- **Framework**: Flask 3.0.0
- **Language**: Python 3.7+
- **Database**: In-memory (for demo)
- **Security**: SHA-256 password hashing

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Responsive design, parallax effects
- **JavaScript** - Dynamic interactions, API calls
- **Animations** - Smooth transitions and effects

### Deployment
- **Development Server**: Flask built-in server
- **Production**: Can be deployed on Nginx, Apache, or cloud platforms

## Security Considerations

### Implemented
✓ SHA-256 password hashing
✓ Session management with timeouts
✓ CSRF protection via session tokens
✓ Role-based access control
✓ Device verification
✓ Comprehensive audit logging
✓ Alert system for security events

### For Production
- Use HTTPS/TLS encryption
- Implement database for user persistence
- Add rate limiting for login attempts
- Deploy behind reverse proxy
- Use environment variables for secrets
- Implement real MFA (TOTP/SMS)
- Regular security audits
- Database backups and disaster recovery

## Troubleshooting

### Python Not Found
**Solution**: 
- Ensure Python is installed with "Add Python to PATH" enabled
- Restart Command Prompt after installation
- Try using `python3` instead of `python`

### Port 5000 Already in Use
**Solution**:
- Kill the process using port 5000
- Or modify the port in `run_server.py`

### Flask Not Installed
**Solution**:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Blank Page or Styling Issues
**Solution**:
- Clear browser cache (Ctrl+Shift+Delete)
- Hard refresh (Ctrl+Shift+R or Cmd+Shift+R)
- Try a different browser

## Browser Compatibility

- ✓ Chrome 90+
- ✓ Firefox 88+
- ✓ Safari 14+
- ✓ Edge 90+

## Performance Optimization

- Minimized CSS and JavaScript
- Lazy loading of images
- Efficient parallax scrolling
- Session-based caching
- Optimized API responses

## Future Enhancements

- Database integration (PostgreSQL)
- Real multi-factor authentication
- Content management system integration
- Advanced analytics dashboard
- Machine learning for anomaly detection
- Mobile application
- API documentation with Swagger/OpenAPI
- Unit and integration tests
- Continuous integration/deployment

## Report Reference

This implementation is based on the "Field Trip Report to Despite Group of Companies" which details:
- Organization: Despite Group of Companies (Ghana's leading media conglomerate)
- Department: Social Media & Public Relations
- Focus: Cybersecurity implementation for digital asset protection
- Methods: Zero Trust Architecture and Digital Rights Management
- Scope: Access control, content protection, and audit logging

## Authors

**Group E - BSc Cybersecurity**
- Ghana Communication Technology University
- Lecturer: Dr. Martin Mabeifam Ujakpa
- Submission Date: December 25, 2025

## License

Educational project for academic purposes.

## Support

For issues or questions:
1. Check the Troubleshooting section
2. Review log files in `app/logs/`
3. Check browser console (F12) for errors
4. Verify all files are in correct locations

---

**Last Updated**: January 9, 2026
**Version**: 1.0.0
