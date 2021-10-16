from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import pymysql
pymysql.install_as_MySQLdb()


class Database: 

    def __init__(self) -> None:
        self.__app = Flask(__name__)
        self.__app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:admin@ctn-mysql-db/school'
        self.__db = SQLAlchemy(self.__app)

    
    def  get_db(self) -> SQLAlchemy:
        return self.__db