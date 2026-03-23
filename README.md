# Attendance Management System (NNRG Edition)

A Flask-based web application for managing college attendance in educational institutions, specifically configured for **Engineering**, **Pharmacy**, and **MBA** departments.

## Latest Updates & Features

✅ **Department-Specific Logic**: 
- **Engineering**: CSE, ECE, AIML, DS, IT (4 Years)
- **Pharmacy**: B.Pharm (4 Years)
- **MBA**: MBA (2 Years)
✅ **Faculty Profiles**: Faculty can set their default Department, Branch, and Subject in their profile for auto-loading.
✅ **Dynamic Filtering**: Admin dashboard with persistent filters for Department, Branch, Year, Section, Academic Year, and Date.
✅ **Auto-Loading Dates**: Current Academic Year, Semester, and Today's Date are automatically selected across all pages.
✅ **Role-Based Access**: Secure login for Faculty and Admin users.
✅ **Dummy Data Generator**: Script to populate the system with 5 students per class (e.g., `AIML-3-A-1`).

## Project Structure

```
attendance_app/
├── models.py            # Database models (User, Student, Attendance Summary)
├── auth.py              # Login/Logout functionality
├── faculty.py           # Faculty operations (Marking attendance, Profile)
├── admin.py             # Admin operations (Filtering, Approving)
├── templates/
│   ├── faculty_dashboard.html   # Faculty entry point with profile
│   ├── mark_attendance.html     # Real-time attendance marking
│   └── admin_dashboard.html     # Advanced filtering & approvals
├── populate_students.py  # Script to generate dummy students
└── reset_db.py          # Script to clear and rebuild database
```

## Installation & Setup

1. **Install Dependencies**:
```bash
pip install -r requirements.txt
```

2. **Reset & Initialize Database** (Required if models change):
```bash
python reset_db.py
```

3. **Generate Dummy Students**:
Adds 5 students for every Branch/Year/Section/Semester combination.
```bash
python populate_students.py
```

4. **Create Users**:
Create your Admin and Faculty login credentials.
```bash
python create_admin.py
```

5. **Run the Application**:
```bash
python run.py
```
Open browser: **http://127.0.0.1:5000**

## Usage Instructions

### For Faculty
1. Login and click **Update Profile** to set your teaching Subject and Department.
2. The Dashboard will now automatically pre-fill your details.
3. Click **Fetch Students**, mark the **Absent** students, and **Submit**.

### For Admin
1. Login to see the global overview.
2. Use the **Filter Row** to find specific records. The system will "remember" your selections after you click Filter.
3. Use the **Specific Date** picker (defaults to today) to see daily reports.
4. Click **Approve** on pending submissions.

## Data Format
- **Student Roll Numbers**: Generated with unique prefixes to allow "Student 1" to exist across different semesters/years.
- **Display Names**: Formatted as `{Branch}-{Year}-{Section}-{Number}` (e.g., `AIML-3-A-1`).

## Technologies Used
- **Backend**: Flask, SQLAlchemy (SQLite)
- **Frontend**: Bootstrap 5, JavaScript (Dynamic UI logic)
- **Security**: Werkzeug (Password Hashing), Flask-Login
