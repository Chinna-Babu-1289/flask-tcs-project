from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    date_added = db.Column(db.Date(), default=datetime.now(), nullable=False)

    def __repr__(self) -> str:
        return f"user: {self.username}, email:{self.email}, empid:{self.empid}, date_added:{self.date_added},password:{self.password}"


def formatUser(user):
    return {
        "username": user.username,
        "email": user.email,
        "password": user.password,
        
    }
