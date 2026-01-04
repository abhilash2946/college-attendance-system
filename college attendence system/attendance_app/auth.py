from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user
from .models import User
from .extensions import login_manager

auth_bp = Blueprint("auth", __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@auth_bp.route("/", methods=["GET", "POST"])
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(username=request.form.get("username", "")).first()
        if user and user.check_password(request.form.get("password", "")):
            login_user(user)
            if user.role == "faculty":
                return redirect(url_for('faculty.dashboard'))
            else:
                return redirect(url_for('admin.dashboard'))
        flash("Invalid login")
    return render_template("login.html")

@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
