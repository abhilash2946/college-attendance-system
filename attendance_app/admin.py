from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required
from .models import AttendanceSummary
from .extensions import db
from datetime import datetime

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/dashboard')
@login_required
def dashboard():
    from .models import Student
    
    data = AttendanceSummary.query.order_by(AttendanceSummary.date.desc()).all()
    
    # Get all departments for the template
    all_students = Student.query.all()
    all_departments = {}
    for student in all_students:
        if student.department not in all_departments:
            all_departments[student.department] = []
        if student.branch not in all_departments[student.department]:
            all_departments[student.department].append(student.branch)
    
    departments = list(all_departments.keys())
    
    # Default filters for fresh load
    filters = {
        'department': '', 'branch': '', 'year': '', 'section': '',
        'academic_year': '', 'semester': '', 'date': datetime.now().strftime('%Y-%m-%d')
    }

    return render_template('admin_dashboard.html', data=data, departments=departments, all_departments=all_departments, filters=filters)

@admin_bp.route('/filter_records', methods=['POST'])
@login_required
def filter_records():
    from .models import Student
    
    # Get filter parameters
    filters = {
        'department': request.form.get('department', ''),
        'branch': request.form.get('branch', ''),
        'year': request.form.get('year', ''),
        'section': request.form.get('section', ''),
        'academic_year': request.form.get('academic_year', ''),
        'semester': request.form.get('semester', ''),
        'date': request.form.get('date', '')
    }

    # Build query based on filters
    query = AttendanceSummary.query
    
    if filters['department']:
        query = query.filter(AttendanceSummary.department == filters['department'])
    if filters['branch']:
        query = query.filter(AttendanceSummary.branch == filters['branch'])
    if filters['year']:
        query = query.filter(AttendanceSummary.year == int(filters['year']))
    if filters['section']:
        query = query.filter(AttendanceSummary.section == filters['section'])
    if filters['academic_year']:
        query = query.filter(AttendanceSummary.academic_year == filters['academic_year'])
    if filters['semester']:
        query = query.filter(AttendanceSummary.semester == filters['semester'])
    if filters['date']:
        try:
            filter_date = datetime.strptime(filters['date'], '%Y-%m-%d').date()
            query = query.filter(AttendanceSummary.date == filter_date)
        except ValueError:
            pass

    data = query.order_by(AttendanceSummary.date.desc()).all()
    
    # Get all departments for the template
    all_students = Student.query.all()
    all_departments = {}
    for student in all_students:
        if student.department not in all_departments:
            all_departments[student.department] = []
        if student.branch not in all_departments[student.department]:
            all_departments[student.department].append(student.branch)
    
    departments = list(all_departments.keys())
    
    return render_template('admin_dashboard.html', data=data, departments=departments, all_departments=all_departments, filters=filters)


@admin_bp.route('/view_department/<department>')
@login_required
def view_department(department):
    from .models import Student
    
    # Get branches for the selected department
    students = Student.query.filter_by(department=department).all()
    branches = list(set([s.branch for s in students]))
    
    # Get attendance data for this department
    data = AttendanceSummary.query.filter_by(department=department).order_by(AttendanceSummary.date.desc()).all()
    
    # Get all departments for the template
    all_students = Student.query.all()
    all_departments = {}
    for student in all_students:
        if student.department not in all_departments:
            all_departments[student.department] = []
        if student.branch not in all_departments[student.department]:
            all_departments[student.department].append(student.branch)
    
    departments = list(all_departments.keys())
    
    # Initialize empty filters when viewing via department card
    filters = {
        'department': department, 'branch': '', 'year': '', 'section': '',
        'academic_year': '', 'semester': '', 'date': datetime.now().strftime('%Y-%m-%d')
    }

    return render_template('admin_dashboard.html', data=data, departments=departments, all_departments=all_departments, filters=filters)


@admin_bp.route('/approve/<int:id>')
@login_required
def approve(id):
    rec = AttendanceSummary.query.get(id)
    if rec:
        rec.status = 'approved'
        db.session.commit()
    return redirect(url_for('admin.dashboard'))