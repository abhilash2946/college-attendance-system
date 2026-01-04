from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from datetime import date
from .models import Student, Attendance, AttendanceSummary
from .extensions import db

faculty_bp = Blueprint("faculty", __name__)

@faculty_bp.route("/dashboard")
@login_required
def dashboard():
    return render_template("faculty_dashboard.html")

@faculty_bp.route("/mark", methods=["GET", "POST"])
@login_required
def mark():
    branch = request.args.get("branch") or request.form.get("branch", "")
    year = request.args.get("year") or request.form.get("year", "")
    section = request.args.get("section") or request.form.get("section", "")
    
    if request.method == "POST":
        absent = request.form.getlist("absent")

        students = Student.query.filter_by(branch=branch, year=int(year), section=section).all()

        present_count = 0
        absent_count = 0

        for s in students:
            status = "absent" if s.roll_no in absent else "present"
            db.session.add(Attendance(date=date.today(), roll_no=s.roll_no, status=status))
            if status == "present":
                present_count += 1
            else:
                absent_count += 1

        db.session.add(
            AttendanceSummary(
                date=date.today(),
                branch=branch,
                year=int(year),
                section=section,
                present=present_count,
                absent=absent_count,
                status="submitted"
            )
        )
        db.session.commit()
        flash("Attendance submitted successfully", "success")
        return redirect(url_for("faculty.dashboard"))

    # GET request - fetch and display students
    students = []
    if branch and year and section:
        students = Student.query.filter_by(branch=branch, year=int(year), section=section).all()
    
    return render_template("mark_attendance.html", branch=branch, year=year, section=section, students=students, today=date.today())
