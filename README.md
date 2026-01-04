# college-attendance-system
# Attendance Management System

A Flask-based web application for managing first-period attendance in educational institutions.

## Features

✅ **Faculty Dashboard** - Mark attendance for students by class (branch, year, section)
✅ **Admin Dashboard** - Review and approve submitted attendance records
✅ **Role-Based Access** - Faculty and Admin users with different permissions
✅ **Database** - SQLite for persistent data storage
✅ **Responsive UI** - Bootstrap 5 with clean, modern interface

## Project Structure

```
attendance_app/
├── __init__.py          # Flask app factory
├── config.py            # Configuration (SQLite database)
├── extensions.py        # Flask extensions (SQLAlchemy, LoginManager)
├── models.py            # Database models (User, Student, Attendance, AttendanceSummary)
├── auth.py              # Authentication routes (login/logout)
├── faculty.py           # Faculty routes (dashboard, mark attendance)
├── admin.py             # Admin routes (dashboard, approve attendance)
├── static/
│   └── css/
│       └── styles.css   # Custom styling
└── templates/
    ├── base.html            # Base template with header/nav
    ├── login.html           # Login page
    ├── faculty_dashboard.html   # Faculty home
    ├── mark_attendance.html     # Attendance marking form
    └── admin_dashboard.html     # Admin review panel

run.py                  # Application entry point
requirements.txt        # Python dependencies
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/attendance-system.git
cd attendance-system
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python run.py
```

5. Open browser: **http://127.0.0.1:5000**

## Default Test Credentials

| Role | Username | Password |
|------|----------|----------|
| Faculty | `faculty` | `password` |
| Admin | `admin` | `password` |

## Usage

### Faculty Flow
1. Login with faculty credentials
2. Enter branch, year, and section (e.g., CSE, 1, A)
3. Click "Fetch Students" to see all students in that class
4. Check boxes for absent students (all are marked present by default)
5. Click "Submit Attendance" to save

### Admin Flow
1. Login with admin credentials
2. View all submitted attendance records
3. Check present/absent counts
4. Click "Approve" to mark attendance as approved

## Database Models

- **User** - Faculty and Admin users with role-based access
- **Student** - Student records (roll_no, name, branch, year, section)
- **Attendance** - Individual student attendance records (date, status)
- **AttendanceSummary** - Summary of attendance by class (present count, absent count, status)

## Technologies Used

- **Backend**: Flask 3.1.2, SQLAlchemy 2.0
- **Database**: SQLite
- **Frontend**: Bootstrap 5.3.0, HTML/CSS
- **Authentication**: Flask-Login

## License

MIT License
