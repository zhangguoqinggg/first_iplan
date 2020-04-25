
import os

DEBUG = True

SECRET_KEY = os.urandom(24)

HOST_NAME ='39.100.237.11'
PORT = '3306'
DATABASE = 'flask_python'
USERNAME = 'root'
PASSWORD = 'root'
DB_URL = 'mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOST_NAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URL

