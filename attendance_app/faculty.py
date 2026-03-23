from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from datetime import date
from .models import Student, Attendance as AttendanceRecord, AttendanceSummary
from .extensions import db

faculty_bp = Blueprint('faculty', __name__, url_prefix='/faculty')

@faculty_bp.route('/dashboard')
@login_required
def dashboard():
    if current_user.role != 'faculty':
        return 'Access Denied', 403
    return render_template('faculty_dashboard.html')

@faculty_bp.route('/update_profile', methods=['POST'])
@login_required
def update_profile():
    if current_user.role != 'faculty':
        return 'Access Denied', 403

    current_user.subject = request.form.get('subject')
    current_user.department = request.form.get('department')
    current_user.branch = request.form.get('branch')

    db.session.commit()
    flash('Profile updated successfully!', 'success')
    return redirect(url_for('faculty.dashboard'))

@faculty_bp.route('/mark', methods=['GET', 'POST'])
@login_required
def mark():
    from datetime import datetime
    
    department = request.args.get('department') or request.form.get('department', '')
    branch = request.args.get('branch') or request.form.get('branch', '')
    year = request.args.get('year') or request.form.get('year', '')
    section = request.args.get('section') or request.form.get('section', '')
    
    # Set default academic year if not provided
    current_date = datetime.now()
    current_year = current_date.year
    current_month = current_date.month
    
    # Academic year typically runs from August to July
    if current_month >= 6:
        default_academic_year = f"{current_year}-{current_year + 1}"
    else:
        default_academic_year = f"{current_year - 1}-{current_year}"
    
    academic_year = request.args.get('academic_year') or request.form.get('academic_year', default_academic_year)
    
    # Set default semester based on current month
    if 7 <= current_month <= 12:
        default_semester = "1 Semester"
    else:
        default_semester = "2 Semester"
    
    semester = request.args.get('semester') or request.form.get('semester', default_semester)
    subject = request.args.get('subject') or request.form.get('subject', current_user.subject or '')
    
    if request.method == 'POST':
        absent = request.form.getlist('absent')

        students = Student.query.filter_by(
            department=department,
            branch=branch,
            year=int(year),
            section=section,
            academic_year=academic_year,
            semester=semester
        ).all()

        present_count = 0
        absent_count = 0

        for s in students:
            status = 'absent' if s.roll_no in absent else 'present'
            db.session.add(AttendanceRecord(date=date.today(), roll_no=s.roll_no, status=status))
            if status == 'present':
                present_count += 1
            else:
                absent_count += 1

        db.session.add(
            AttendanceSummary(
                date=date.today(),
                department=department,
                branch=branch,
                year=int(year),
                section=section,
                academic_year=academic_year,
                semester=semester,
                subject=subject,
                present=present_count,
                absent=absent_count,
                status='submitted'
            )
        )
        db.session.commit()
        flash('Attendance submitted successfully', 'success')
        return redirect(url_for('faculty.dashboard'))

    # GET request - fetch and display students
    students = []
    if department and branch and year and section and academic_year and semester:
        students = Student.query.filter_by(
            department=department,
            branch=branch,
            year=int(year),
            section=section,
            academic_year=academic_year,
            semester=semester
        ).all()
    
    return render_template('mark_attendance.html',
                           department=department,
                           branch=branch,
                           year=year,
                           section=section,
                           academic_year=academic_year,
                           semester=semester,
                           subject=subject,
                           students=students,
                           today=date.today())
