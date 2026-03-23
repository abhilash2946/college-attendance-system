from attendance_app import create_app
from attendance_app.extensions import db
from attendance_app.models import User, Student, Attendance, AttendanceSummary

app = create_app()

with app.app_context():
    print("Dropping all tables...")
    db.drop_all()
    print("Creating all tables...")
    db.create_all()
    print("Database reset successfully!")
