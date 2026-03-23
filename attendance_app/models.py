from flask_login import UserMixin
from .extensions import db
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100))
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    # New fields for faculty profile
    department = db.Column(db.String(100))
    branch = db.Column(db.String(100))
    subject = db.Column(db.String(100))

    def set_password(self, pwd):
        self.password = generate_password_hash(pwd)
    
    def check_password(self, pwd):
        return check_password_hash(self.password, pwd)

class Student(db.Model):
    roll_no = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(100))
    department = db.Column(db.String(100))
    branch = db.Column(db.String(20))
    year = db.Column(db.Integer)
    section = db.Column(db.String(5))
    academic_year = db.Column(db.String(20))
    semester = db.Column(db.String(20))

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    roll_no = db.Column(db.String(50))
    status = db.Column(db.String(10))

class AttendanceSummary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    department = db.Column(db.String(100))
    branch = db.Column(db.String(20))
    year = db.Column(db.Integer)
    section = db.Column(db.String(5))
    academic_year = db.Column(db.String(20))
    semester = db.Column(db.String(20))
    subject = db.Column(db.String(100))
    present = db.Column(db.Integer)
    absent = db.Column(db.Integer)
    status = db.Column(db.String(20)) # submitted / approved
