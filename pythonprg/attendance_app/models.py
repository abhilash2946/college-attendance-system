from .extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    role = db.Column(db.String(20))  # faculty / admin / hod
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(200))

    def set_password(self, pwd):
        self.password = generate_password_hash(pwd)

    def check_password(self, pwd):
        return check_password_hash(self.password, pwd)

class Student(db.Model):
    roll_no = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(100))
    branch = db.Column(db.String(20))
    year = db.Column(db.Integer)
    section = db.Column(db.String(5))

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    roll_no = db.Column(db.String(20))
    status = db.Column(db.String(10))

class AttendanceSummary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    branch = db.Column(db.String(20))
    year = db.Column(db.Integer)
    section = db.Column(db.String(5))
    present = db.Column(db.Integer)
    absent = db.Column(db.Integer)
    status = db.Column(db.String(20))  # submitted / approved
