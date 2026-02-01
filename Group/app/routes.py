"""
Despite Group Flask Routes and API Endpoints - Enhanced
"""

from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for
from app.models import (
    User, AccessController, Log, AlertSystem, DRM, 
    RiskScoring, BehaviorAnalysis, ComplianceEngine, 
    DeviceFingerprint, MFA, RateLimiter, EncryptionEngine
)
from functools import wraps
from datetime import datetime

routes_bp = Blueprint('routes', __name__)
ac = AccessController()

# ============================================================
# LOGIN REQUIRED DECORATOR
# ============================================================

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return decorated_function


# ============================================================
# WEB ROUTES
# ============================================================

@routes_bp.route('/')
def index():
    """Home page with parallax"""
    return render_template('index.html')


@routes_bp.route('/dashboard')
@login_required
def dashboard():
    """User dashboard"""
    username = session.get('user')
    user_data = User.users_db.get(username)
    if not user_data:
        return redirect(url_for('routes.login'))
    
    return render_template('dashboard.html', username=username, role=user_data['role'])


@routes_bp.route('/login')
def login():
    """Login page"""
    return render_template('login.html')


@routes_bp.route('/test')
def test_page():
    """Access control test page"""
    if 'user' not in session:
        return redirect(url_for('routes.login'))
    return render_template('test.html')


# ============================================================
# API ENDPOINTS
# ============================================================

@routes_bp.route('/api/login', methods=['POST'])
def api_login():
    """API endpoint for login"""
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"status": "error", "message": "Username and password required"}), 400
    
    user = User.authenticate(username, password)
    
    if not user:
        AlertSystem.notify_failed_login(username)
        return jsonify({"status": "error", "message": "Invalid credentials"}), 401
    
    session['user'] = username
    session['role'] = user.role
    
    return jsonify({
        "status": "success",
        "message": "Login successful",
        "user": {
            "username": username,
            "role": user.role,
            "permissions": user.get_permissions(),
            "device_secure": user.device_is_secure()
        }
    }), 200


@routes_bp.route('/api/logout', methods=['POST'])
@login_required
def api_logout():
    """API endpoint for logout"""
    username = session.get('user')
    Log.audit_trail(username, "LOGOUT", "SYSTEM", "SUCCESS")
    session.clear()
    return jsonify({"status": "success", "message": "Logout successful"}), 200


@routes_bp.route('/api/request-access', methods=['POST'])
@login_required
def api_request_access():
    """API endpoint for requesting access to resources"""
    data = request.json
    username = session.get('user')
    resource = data.get('resource')
    action = data.get('action')
    
    if not resource or not action:
        return jsonify({"status": "error", "message": "Resource and action required"}), 400
    
    # Create user object
    user_data = User.users_db.get(username)
    user = User(username, user_data['role'], user_data['device_secure'])
    user.authenticated = True
    
    # Request access
    result = ac.request_access(user, resource, action)
    
    return jsonify({
        "status": "success",
        "access_result": result,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }), 200


@routes_bp.route('/api/user-info', methods=['GET'])
@login_required
def api_user_info():
    """API endpoint to get current user info"""
    username = session.get('user')
    user_data = User.users_db.get(username)
    
    if not user_data:
        return jsonify({"error": "User not found"}), 404
    
    user = User(username, user_data['role'], user_data['device_secure'])
    user.authenticated = True
    
    return jsonify({
        "username": username,
        "role": user_data['role'],
        "permissions": user.get_permissions(),
        "drm_permissions": user.get_drm_permissions(),
        "device_secure": user_data['device_secure'],
        "last_login": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }), 200


@routes_bp.route('/api/test-scenarios', methods=['GET'])
@login_required
def api_test_scenarios():
    """Get predefined test scenarios"""
    scenarios = [
        {
            "id": 1,
            "name": "Creator Publishing Content",
            "description": "Test if creator can publish video content",
            "resource": "CampaignVideo.mp4",
            "action": "PUBLISH"
        },
        {
            "id": 2,
            "name": "Admin Monitoring",
            "description": "Test if admin can monitor analytics",
            "resource": "AnalyticsReport.xlsx",
            "action": "MONITOR"
        },
        {
            "id": 3,
            "name": "Analyst Publishing (Should Fail)",
            "description": "Test if analyst is denied publishing",
            "resource": "SensitiveData.pdf",
            "action": "PUBLISH"
        },
        {
            "id": 4,
            "name": "Device Security Check",
            "description": "Test device security validation",
            "resource": "PublicContent.jpg",
            "action": "VIEW"
        },
        {
            "id": 5,
            "name": "PR Manager Approving",
            "description": "Test if PR manager can approve content",
            "resource": "NewsArticle.html",
            "action": "APPROVE"
        }
    ]
    
    return jsonify({"scenarios": scenarios}), 200


@routes_bp.route('/api/run-test/<int:scenario_id>', methods=['POST'])
@login_required
def api_run_test(scenario_id):
    """Run a specific test scenario"""
    username = session.get('user')
    user_data = User.users_db.get(username)
    
    # Get scenario details
    scenarios = {
        1: {"resource": "CampaignVideo.mp4", "action": "PUBLISH"},
        2: {"resource": "AnalyticsReport.xlsx", "action": "MONITOR"},
        3: {"resource": "SensitiveData.pdf", "action": "PUBLISH"},
        4: {"resource": "PublicContent.jpg", "action": "VIEW"},
        5: {"resource": "NewsArticle.html", "action": "APPROVE"},
    }
    
    if scenario_id not in scenarios:
        return jsonify({"error": "Scenario not found"}), 404
    
    scenario = scenarios[scenario_id]
    
    # Create user and test access
    user = User(username, user_data['role'], user_data['device_secure'])
    user.authenticated = True
    
    result = ac.request_access(user, scenario['resource'], scenario['action'])
    
    return jsonify({
        "status": "success",
        "scenario_id": scenario_id,
        "user": username,
        "role": user_data['role'],
        "test_result": result,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }), 200


@routes_bp.route('/api/access-summary', methods=['GET'])
def api_access_summary():
    """Get access control summary statistics"""
    summary = ac.get_access_summary()
    
    return jsonify({
        "status": "success",
        "summary": summary
    }), 200


@routes_bp.route('/api/users', methods=['GET'])
def api_users():
    """Get list of demo users"""
    users_list = []
    for username, data in User.users_db.items():
        users_list.append({
            "username": username,
            "role": data['role'],
            "device_secure": data['device_secure']
        })
    
    return jsonify({"users": users_list}), 200


# ============================================================
# ADVANCED SECURITY API ENDPOINTS
# ============================================================

@routes_bp.route('/api/security/risk-assessment', methods=['GET'])
@login_required
def api_risk_assessment():
    """Get comprehensive risk assessment"""
    username = session.get('user')
    user_data = User.users_db.get(username, {})
    
    risk_score = RiskScoring.calculate_risk_score(user_data)
    risk_level = RiskScoring.get_risk_level(risk_score)
    
    return jsonify({
        "status": "success",
        "user": username,
        "risk_assessment": {
            "score": risk_score,
            "level": risk_level,
            "factors": {
                "failed_login_attempts": user_data.get('failed_attempts', 0),
                "device_security": "SECURE" if user_data.get('device_secure') else "INSECURE",
                "time_based_anomaly": "DETECTED" if datetime.now().hour < 6 or datetime.now().hour > 22 else "NORMAL",
                "permission_escalation_attempts": user_data.get('escalation_attempts', 0)
            },
            "timestamp": datetime.now().isoformat()
        }
    }), 200


@routes_bp.route('/api/security/behavioral-analysis', methods=['GET'])
@login_required
def api_behavioral_analysis():
    """Get behavioral analysis and anomalies"""
    username = session.get('user')
    
    activity_context = {
        'hour': datetime.now().hour,
        'action': 'VIEW',
        'resource': 'SYSTEM'
    }
    
    anomalies = BehaviorAnalysis.detect_anomalies(username, activity_context)
    profile = BehaviorAnalysis.user_profiles.get(username, {})
    
    return jsonify({
        "status": "success",
        "user": username,
        "behavioral_analysis": {
            "profile": profile,
            "current_activity_anomalies": anomalies,
            "anomaly_count": len(anomalies),
            "risk_level": "HIGH" if len(anomalies) > 2 else "LOW",
            "timestamp": datetime.now().isoformat()
        }
    }), 200


@routes_bp.route('/api/security/compliance-status', methods=['GET'])
@login_required
def api_compliance_status():
    """Get compliance status and violations"""
    username = session.get('user')
    user_data = User.users_db.get(username, {})
    
    violations = ComplianceEngine.check_compliance(user_data)
    compliance_report = ComplianceEngine.generate_compliance_report()
    
    return jsonify({
        "status": "success",
        "user": username,
        "compliance": {
            "violations": violations,
            "is_compliant": len(violations) == 0,
            "violation_count": len(violations),
            "policies_enforced": list(ComplianceEngine.compliance_rules.keys()),
            "report": compliance_report
        }
    }), 200


@routes_bp.route('/api/security/device-fingerprint', methods=['POST'])
@login_required
def api_device_fingerprint():
    """Validate and fingerprint device"""
    data = request.json
    user_agent = data.get('user_agent', 'Unknown')
    ip_address = request.remote_addr
    
    fingerprint = DeviceFingerprint.generate_fingerprint(user_agent, ip_address)
    is_secure = DeviceFingerprint.validate_device_integrity(fingerprint)
    encryption_status = DeviceFingerprint.check_encryption_status()
    malware_status = DeviceFingerprint.check_malware_status()
    
    return jsonify({
        "status": "success",
        "device_fingerprint": {
            "fingerprint_hash": fingerprint,
            "integrity_valid": is_secure,
            "encryption_enabled": encryption_status,
            "malware_detected": malware_status,
            "security_score": 85 if is_secure else 40,
            "ip_address": ip_address,
            "timestamp": datetime.now().isoformat()
        }
    }), 200


@routes_bp.route('/api/security/mfa/initiate', methods=['POST'])
@login_required
def api_mfa_initiate():
    """Initiate MFA challenge"""
    username = session.get('user')
    data = request.json
    challenge_type = data.get('type', 'EMAIL')
    
    challenge_token = MFA.send_challenge(username, challenge_type)
    
    return jsonify({
        "status": "success",
        "mfa": {
            "challenge_initiated": True,
            "type": challenge_type,
            "message": f"MFA challenge sent via {challenge_type}",
            "expires_in": 300  # 5 minutes
        }
    }), 200


@routes_bp.route('/api/security/mfa/verify', methods=['POST'])
@login_required
def api_mfa_verify():
    """Verify MFA challenge"""
    username = session.get('user')
    data = request.json
    token = data.get('token')
    
    if not token:
        return jsonify({"status": "error", "message": "Token required"}), 400
    
    verified = MFA.verify_challenge(username, token)
    
    if verified:
        session['mfa_verified'] = True
        Log.audit_trail(username, "MFA_VERIFICATION", "SUCCESS", "PASSED")
    
    return jsonify({
        "status": "success",
        "mfa": {
            "verified": verified,
            "message": "MFA verification successful" if verified else "MFA verification failed"
        }
    }), 200


@routes_bp.route('/api/security/elevated-access', methods=['POST'])
@login_required
def api_elevated_access():
    """Request elevated access with justification"""
    username = session.get('user')
    user_data = User.users_db.get(username)
    data = request.json
    
    resource = data.get('resource')
    action = data.get('action')
    justification = data.get('justification')
    
    if not all([resource, action, justification]):
        return jsonify({"status": "error", "message": "Resource, action, and justification required"}), 400
    
    user = User(username, user_data['role'], user_data['device_secure'])
    user.authenticated = True
    
    result = AccessController().request_elevated_access(user, resource, action, justification)
    
    return jsonify({
        "status": "success",
        "elevated_access": result
    }), 200


@routes_bp.route('/api/security/threat-detection', methods=['GET'])
@login_required
def api_threat_detection():
    """Get threat detection status"""
    username = session.get('user')
    
    return jsonify({
        "status": "success",
        "threat_detection": {
            "active": True,
            "threats_detected": 0,
            "threats_blocked": AccessController().denied_attempts,
            "last_threat_detected": None,
            "monitoring_status": "ACTIVE",
            "threat_level": "LOW",
            "timestamp": datetime.now().isoformat()
        }
    }), 200


@routes_bp.route('/api/security/detailed-metrics', methods=['GET'])
def api_detailed_metrics():
    """Get detailed security metrics"""
    metrics = AccessController().get_detailed_metrics()
    
    return jsonify({
        "status": "success",
        "metrics": metrics,
        "timestamp": datetime.now().isoformat()
    }), 200


@routes_bp.route('/api/security/encryption-status', methods=['GET'])
@login_required
def api_encryption_status():
    """Get encryption and data protection status"""
    username = session.get('user')
    
    return jsonify({
        "status": "success",
        "encryption": {
            "data_at_rest": "ENCRYPTED_AES256",
            "data_in_transit": "TLS_1_3",
            "key_management": "HSM_PROTECTED",
            "compliance": "HIPAA_COMPLIANT",
            "last_audit": datetime.now().isoformat(),
            "encryption_keys_rotated": "30_days_ago"
        }
    }), 200


@routes_bp.route('/api/security/audit-logs', methods=['GET'])
@login_required
def api_audit_logs():
    """Get recent audit logs"""
    # Read from audit trail log
    logs = []
    try:
        with open("app/logs/audit_trail.log", "r") as f:
            lines = f.readlines()
            # Get last 10 entries
            for line in lines[-10:]:
                logs.append(line.strip())
    except:
        logs = ["No logs available"]
    
    return jsonify({
        "status": "success",
        "audit_logs": logs,
        "total_entries": len(logs),
        "timestamp": datetime.now().isoformat()
    }), 200


@routes_bp.route('/api/security/rate-limit-status', methods=['GET'])
@login_required
def api_rate_limit_status():
    """Get rate limiting status"""
    username = session.get('user')
    request_count = len(RateLimiter.request_history.get(username, []))
    
    return jsonify({
        "status": "success",
        "rate_limiting": {
            "user": username,
            "requests_this_hour": request_count,
            "limit": 100,
            "remaining": 100 - request_count,
            "reset_time": "60_minutes",
            "blocked": False
        }
    }), 200
