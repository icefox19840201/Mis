#encoding:utf-8
from django.db import connection

def execquerySql(sql):
    cursor=connection.cursor()
    cursor.execute(sql)
    result=cursor.fetchall()
    return result

def getSingleResultByQuerySql(sql):
    cursor=connection.cursor()
    cursor.execute(sql)
    result=cursor.fetchone()
    return result
