from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# from app import app
import mysql.connector
from configparser import ConfigParser

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    confirmpassword = db.Column(db.String(255), nullable=False)
    date_added = db.Column(db.Date(), default=datetime.now(), nullable=False)

    def __repr__(self) -> str:
        return f"user: {self.username} created successfully"


config_path = 'config.ini'
config = ConfigParser()
config.read(config_path)

conn = mysql.connector.connect(
    host=config['database']['dbhost'],
    user=config['database']['dbuser'],
    passwd=config['database']['dbpass'],
)


# def create_db(conn, dbName):
#     cursor = conn.cursor()
#     try:
#         cursor.execute("SHOW DATABASES")
#         for db in cursor:
#             if db != dbName:
#                 cursor.execute(f"CREATE DATABASE {dbName}")
#     except Exception as e:
#         raise e
#     finally:
#         cursor.close()


# def create_table(conn, tableName):
#     cursor = conn.cursor()
#     try:
#         cursor.execute("SHOW tables")
#         for table in cursor:
#             if table == tableName:
#                 pass
#             else:
#                 db.create_all()
#     except Exception as e:
#         raise e
#     finally:
#         cursor.close()


# create_table(conn, User)
