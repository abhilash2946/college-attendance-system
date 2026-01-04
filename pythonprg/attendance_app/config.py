import os

class Config:
    SECRET_KEY = "attendance-secret-key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///attendance.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
