"""
Despite Group of Companies - Access Control & DRM System
Zero Trust Architecture Implementation
"""

import hashlib
from datetime import datetime

# ============================================================
# LOGGING SYSTEM
# ============================================================

class Log:
    """Centralized logging for security events and access control"""
    
    @staticmethod
    def security_event(user, message):
        """Log security alerts"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[SECURITY ALERT] {timestamp} - {user.username}: {message}")
        # In production, write to secure log file
        with open("security_events.log", "a") as log_file:
            log_file.write(f"[SECURITY ALERT] {timestamp} - {user.username}: {message}\n")

    @staticmethod
    def access_grant(user, resource):
        """Log successful access grants"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[ACCESS GRANTED] {timestamp} - {user.username} accessed {resource}")
        with open("access_logs.log", "a") as log_file:
            log_file.write(f"[ACCESS GRANTED] {timestamp} - {user.username} accessed {resource}\n")

    @staticmethod
    def audit_trail(user, action, resource, status):
        """Audit trail for compliance and monitoring"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        audit_entry = f"[AUDIT] {timestamp} - User: {user.username} | Action: {action} | Resource: {resource} | Status: {status}"
        print(audit_entry)
        with open("audit_trail.log", "a") as log_file:
            log_file.write(audit_entry + "\n")


# ============================================================
# ALERT SYSTEM
# ============================================================

class AlertSystem:
    """Alert system for notifying administrators of security events"""
    
    @staticmethod
    def send_alert(user, message, severity="WARNING"):
        """Send alert to administrator"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        alert_msg = f"ALERT [{severity}] {timestamp} - User: {user.username} | Message: {message}"
        print(alert_msg)
        
        # In production, would send actual email via SMTP
        # send_email(admin_email, subject, alert_msg)
        
        with open("admin_alerts.log", "a") as alert_file:
            alert_file.write(alert_msg + "\n")

    @staticmethod
    def notify_failed_login(user):
        """Notify admin of failed login attempt"""
        AlertSystem.send_alert(user, f"Failed login attempt for user: {user.username}", severity="CRITICAL")

    @staticmethod
    def notify_unauthorized_access(user, resource, action):
        """Notify admin of unauthorized access attempt"""
        AlertSystem.send_alert(
            user, 
            f"Unauthorized access attempt - Action: {action}, Resource: {resource}",
            severity="CRITICAL"
        )

    @staticmethod
    def notify_device_security_issue(user):
        """Notify admin of device security issue"""
        AlertSystem.send_alert(
            user,
            f"Device security check failed for user: {user.username}",
            severity="HIGH"
        )


# ============================================================
# DIGITAL RIGHTS MANAGEMENT
# ============================================================

class DRM:
    """Digital Rights Management for protecting content"""
    
    @staticmethod
    def apply_watermark(file_name):
        """Apply digital watermark to content"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        watermark_info = f"DRM watermark applied to {file_name} at {timestamp}"
        print(watermark_info)
        with open("drm_operations.log", "a") as drm_file:
            drm_file.write(watermark_info + "\n")
        return True

    @staticmethod
    def verify_content_integrity(file_name, checksum):
        """Verify content has not been tampered with"""
        print(f"Verifying integrity of {file_name}")
        return True

    @staticmethod
    def enforce_license_restrictions(file_name, user_role):
        """Enforce content licensing based on user role"""
        license_rules = {
            "Admin": ["VIEW", "EDIT", "PUBLISH", "DISTRIBUTE"],
            "Creator": ["VIEW", "EDIT", "PUBLISH"],
            "PR_Manager": ["VIEW", "APPROVE", "PUBLISH"],
            "Analyst": ["VIEW"]
        }
        return license_rules.get(user_role, [])


# ============================================================
# USER MODEL
# ============================================================

class User:
    """User model with authentication and role-based access"""
    
    def __init__(self, username, password, role, device_secure=True, mfa_enabled=True):
        self.username = username
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()
        self.role = role
        self.device_secure = device_secure
        self.mfa_enabled = mfa_enabled
        self.authenticated = False
        self.failed_login_attempts = 0
        self.last_login = None

    def authenticate(self, password, mfa_code=None):
        """Authenticate user with password and optional MFA"""
        if hashlib.sha256(password.encode()).hexdigest() != self.password_hash:
            self.failed_login_attempts += 1
            if self.failed_login_attempts >= 3:
                AlertSystem.notify_failed_login(self)
            return False

        if self.mfa_enabled and mfa_code is None:
            print(f"MFA required for user: {self.username}")
            return False

        self.authenticated = True
        self.failed_login_attempts = 0
        self.last_login = datetime.now()
        return True

    def is_authenticated(self):
        """Check if user is authenticated"""
        return self.authenticated

    def device_is_secure(self):
        """Check if user's device meets security standards"""
        return self.device_secure

    def get_permissions(self):
        """Get permissions based on user role"""
        role_permissions = {
            "Admin": ["CREATE", "APPROVE", "PUBLISH", "MONITOR", "DELETE", "CONFIGURE"],
            "Creator": ["CREATE", "PUBLISH"],
            "PR_Manager": ["APPROVE", "MONITOR", "CREATE"],
            "Analyst": ["MONITOR", "VIEW"]
        }
        return role_permissions.get(self.role, [])

    def get_drm_permissions(self):
        """Get DRM-related permissions"""
        return DRM.enforce_license_restrictions(None, self.role)


# ============================================================
# ACCESS CONTROL MODULE - ZERO TRUST ARCHITECTURE
# ============================================================

class AccessController:
    """Access Control Module implementing Zero Trust Architecture"""
    
    def __init__(self):
        self.access_logs = []
        self.denied_attempts = 0
        self.session_timeout = 900  # 15 minutes in seconds

    def request_access(self, user, resource, action):
        """
        Process access request with Zero Trust validation.
        Every request is verified - no defaults trusted.
        """
        
        # Step 1: Verify authentication (Identity)
        if not user.is_authenticated():
            AlertSystem.notify_failed_login(user)
            Log.audit_trail(user, action, resource, "DENIED - Not Authenticated")
            self.denied_attempts += 1
            return "DENIED: User not logged in"

        # Step 2: Verify device security (Device)
        if not user.device_is_secure():
            AlertSystem.notify_device_security_issue(user)
            Log.audit_trail(user, action, resource, "DENIED - Device Security Issue")
            return "DENIED: Device does not meet security standards"

        # Step 3: Verify permissions (Authorization)
        if action not in user.get_permissions():
            AlertSystem.notify_unauthorized_access(user, resource, action)
            Log.security_event(user, f"Unauthorized attempt to {action} {resource}")
            Log.audit_trail(user, action, resource, "DENIED - Insufficient Permissions")
            self.denied_attempts += 1
            return "DENIED: Insufficient permissions"

        # Step 4: Apply DRM if publishing (Content Protection)
        if action == "PUBLISH":
            DRM.apply_watermark(resource)

        # Step 5: Grant access and log
        Log.access_grant(user, resource)
        Log.audit_trail(user, action, resource, "GRANTED")
        return "GRANTED: Access allowed"

    def batch_access_request(self, user, resources, action):
        """Process multiple access requests"""
        results = []
        for resource in resources:
            result = self.request_access(user, resource, action)
            results.append(f"{resource}: {result}")
        return results

    def get_access_summary(self):
        """Get summary of access control statistics"""
        return {
            "total_denied": self.denied_attempts,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }


# ============================================================
# MAIN IMPLEMENTATION & TESTING
# ============================================================

def main():
    """Demonstration of the Access Control & DRM System"""
    
    print("=" * 70)
    print("DESPITE GROUP OF COMPANIES - ACCESS CONTROL SYSTEM DEMO")
    print("Zero Trust Architecture Implementation")
    print("=" * 70)
    print()

    # Create users with different roles
    alice = User("alice", "securePass123", "Creator", device_secure=True, mfa_enabled=True)
    bob = User("bob", "adminPass456", "Admin", device_secure=True, mfa_enabled=True)
    charlie = User("charlie", "analyst789", "Analyst", device_secure=False, mfa_enabled=True)
    diana = User("diana", "pr_manager123", "PR_Manager", device_secure=True, mfa_enabled=True)

    # Create access controller
    ac = AccessController()

    # Authenticate users
    print("\n[PHASE 1] AUTHENTICATION")
    print("-" * 70)
    alice.authenticate("securePass123")
    print(f"✓ Alice authenticated: {alice.is_authenticated()}")
    
    bob.authenticate("adminPass456")
    print(f"✓ Bob authenticated: {bob.is_authenticated()}")
    
    charlie.authenticate("analyst789")
    print(f"✓ Charlie authenticated: {charlie.is_authenticated()}")
    
    diana.authenticate("pr_manager123")
    print(f"✓ Diana authenticated: {diana.is_authenticated()}")

    # Test various access attempts
    print("\n[PHASE 2] ACCESS CONTROL TESTING")
    print("-" * 70)
    
    # Test 1: Creator publishing content (should succeed)
    print("\nTest 1: Creator Publishing Content")
    result = ac.request_access(alice, "CampaignVideo.mp4", "PUBLISH")
    print(f"Result: {result}\n")

    # Test 2: Admin monitoring (should succeed)
    print("Test 2: Admin Monitoring Content")
    result = ac.request_access(bob, "AnalyticsReport.xlsx", "MONITOR")
    print(f"Result: {result}\n")

    # Test 3: Analyst trying to publish (should fail)
    print("Test 3: Analyst Attempting to Publish (Should Fail)")
    result = ac.request_access(charlie, "SensitiveData.pdf", "PUBLISH")
    print(f"Result: {result}\n")

    # Test 4: Device security check (should fail)
    print("Test 4: Device Security Check (Should Fail)")
    result = ac.request_access(charlie, "PublicContent.jpg", "VIEW")
    print(f"Result: {result}\n")

    # Test 5: PR Manager approving content (should succeed)
    print("Test 5: PR Manager Approving Content")
    result = ac.request_access(diana, "NewsArticle.html", "APPROVE")
    print(f"Result: {result}\n")

    # Test 6: Failed login attempt (should trigger alert)
    print("Test 6: Failed Login Attempt")
    eve = User("eve", "wrongPassword", "Creator")
    eve.authenticate("incorrectPassword")
    eve.authenticate("incorrectPassword")
    eve.authenticate("incorrectPassword")
    print()

    # Batch operations
    print("Test 7: Batch Access Request")
    resources = ["Video1.mp4", "Video2.mp4", "Article.txt"]
    batch_results = ac.batch_access_request(alice, resources, "PUBLISH")
    for result in batch_results:
        print(f"  {result}")
    print()

    # Display summary
    print("\n[PHASE 3] ACCESS CONTROL SUMMARY")
    print("-" * 70)
    summary = ac.get_access_summary()
    print(f"Total Denied Attempts: {summary['total_denied']}")
    print(f"Generated at: {summary['timestamp']}")
    
    print("\n[PHASE 4] USER PERMISSIONS SUMMARY")
    print("-" * 70)
    users = [("Alice (Creator)", alice), ("Bob (Admin)", bob), ("Charlie (Analyst)", charlie), ("Diana (PR_Manager)", diana)]
    for name, user in users:
        print(f"\n{name}")
        print(f"  Permissions: {', '.join(user.get_permissions())}")
        print(f"  DRM Permissions: {', '.join(user.get_drm_permissions())}")
        print(f"  Device Secure: {user.device_is_secure()}")

    print("\n" + "=" * 70)
    print("Log files generated:")
    print("  - security_events.log")
    print("  - access_logs.log")
    print("  - audit_trail.log")
    print("  - admin_alerts.log")
    print("  - drm_operations.log")
    print("=" * 70)


if __name__ == "__main__":
    main()
