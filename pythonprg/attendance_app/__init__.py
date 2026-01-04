from flask import Flask
from .config import Config
from .extensions import db, login_manager
from .auth import auth_bp
from .faculty import faculty_bp
from .admin import admin_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    app.register_blueprint(auth_bp)
    app.register_blueprint(faculty_bp, url_prefix="/faculty")
    app.register_blueprint(admin_bp, url_prefix="/admin")

    return app
