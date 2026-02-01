"""
Despite Group of Companies - Access Control System
Flask Application Factory
"""

from flask import Flask
import os

def create_app():
    """Create and configure Flask application"""
    
    # Get the absolute path to the app directory
    app_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Create Flask app with correct paths
    app = Flask(
        __name__,
        template_folder=os.path.join(app_dir, 'templates'),
        static_folder=os.path.join(app_dir, 'static')
    )
    
    # Configuration
    app.secret_key = 'despite-group-secure-key-2025'
    app.config['SESSION_TIMEOUT'] = 900  # 15 minutes
    app.config['JSON_SORT_KEYS'] = False
    
    return app
