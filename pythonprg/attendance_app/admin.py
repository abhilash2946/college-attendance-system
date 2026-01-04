from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required
from .models import AttendanceSummary
from .extensions import db

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/dashboard")
@login_required
def dashboard():
    data = AttendanceSummary.query.all()
    return render_template("admin_dashboard.html", data=data)

@admin_bp.route("/approve/<int:id>")
@login_required
def approve(id):
    rec = AttendanceSummary.query.get(id)
    if rec:
        rec.status = "approved"
        db.session.commit()
    return redirect(url_for('admin.dashboard'))
