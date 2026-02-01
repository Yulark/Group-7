"""
Despite Group Access Control System
Main Flask Application Entry Point
"""

from app import create_app
from app.routes import routes_bp
import os
import webbrowser
from threading import Timer

# Create Flask app
app = create_app()

# Register blueprints
app.register_blueprint(routes_bp)

# Create logs directory if it doesn't exist
os.makedirs('app/logs', exist_ok=True)

# Initialize log files
log_files = [
    'app/logs/security_events.log',
    'app/logs/access_logs.log',
    'app/logs/audit_trail.log',
    'app/logs/admin_alerts.log',
    'app/logs/drm_operations.log'
]

for log_file in log_files:
    if not os.path.exists(log_file):
        open(log_file, 'w').close()


def open_browser():
    """Open the application in default browser"""
    webbrowser.open('http://localhost:5000')


if __name__ == '__main__':
    print("=" * 70)
    print("DESPITE GROUP ACCESS CONTROL SYSTEM")
    print("Zero Trust Architecture & Digital Rights Management")
    print("=" * 70)
    print("\n✓ Starting Flask server...")
    print("✓ Access the application at: http://localhost:5000")
    print("\nDemo Credentials:")
    print("  - alice (Creator): securePass123")
    print("  - bob (Admin): adminPass456")
    print("  - diana (PR Manager): pr_manager123")
    print("  - charlie (Analyst): analyst789")
    print("\n" + "=" * 70)
    print("Press CTRL+C to stop the server")
    print("=" * 70 + "\n")

    # Open browser after a short delay
    timer = Timer(2, open_browser)
    timer.daemon = True
    timer.start()

    # Run Flask app
    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000,
        use_reloader=False  # Disable reloader to prevent opening browser multiple times
    )
