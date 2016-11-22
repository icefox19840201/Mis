#encoding:utf-8
from  app01 import models
import uuid
def getUserinfoById(userId):
    try:
        userinfo=models.user.objects.get(id=userId)
    except:
        raise ValueError("未查找到相关值")
    return userinfo
def getuserifno(*args,**kwargs):
    pass
def getAllUserInfo():
     userinfo=models.user.objects.all()
     return userinfo