import mysql.connector
import os


def getConn(host,user,password,db):
    cnx = mysql.connector.connect(
        host=os.environ.get('MYSQL_HOST'),
        user=os.environ.get('MYSQL_USER'),
        password=os.environ.get('MYSQL_ROOT_PASSWORD'),
        db=os.environ.get('MYSQL_DATABASE')
    )
    return cnx