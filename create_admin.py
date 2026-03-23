"""
Helper to create an admin / faculty user.
Usage:
    python create_admin.py
"""
import os
from attendance_app import create_app
from attendance_app.extensions import db
from attendance_app.models import User

app = create_app()
app.app_context().push()

def create_user():
    username = input("Username: ").strip()
    name = input("Full Name: ").strip()
    role = input("Role (admin/faculty): ").strip()
    password = input("Password: ").strip()

    if User.query.filter_by(username=username).first():
        print("User already exists")
        return

    u = User(username=username, name=name, role=role)
    u.set_password(password)
    db.session.add(u)
    db.session.commit()
    print(f"User '{username}' (Name: {name}) created successfully.")

if __name__ == "__main__":
    create_user()