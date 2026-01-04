"""
Helper to create an admin / faculty user.
Usage:
    set DATABASE_URL=mysql+pymysql://user:pass@host/db  (Windows)
    python create_admin.py
"""
import os
from attendance_app import create_app
from attendance_app.extensions import db
from attendance_app.models import User

app = create_app()
app.app_context().push()

def create_user():
    username = input("username: ").strip()
    name = input("full name: ").strip()
    role = input("role (admin/faculty/hod/dean/chairman): ").strip()
    password = input("password: ").strip()

    if User.query.filter_by(username=username).first():
        print("User exists")
        return

    u = User(username=username, name=name, role=role)
    u.set_password(password)
    db.session.add(u)
    db.session.commit()
    print("User created:", username)

if __name__ == "__main__":
    create_user()
