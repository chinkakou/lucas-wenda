import os
import pymysql

pymysql.install_as_MySQLdb()
SECRET_KEY = os.urandom(24)

#dialect+driver://username:password@host:post/database

USERNAME = 'root'
PASSWORD = 'chinkakou'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'demo'
DB_URI = "mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8".format(USERNAME,PASSWORD,HOST,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = False