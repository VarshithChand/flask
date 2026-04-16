import os

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:150711@localhost:5432/mydb"
    SQLALCHEMY_TRACK_MODIFICATIONS = False