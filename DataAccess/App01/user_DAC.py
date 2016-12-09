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
def delUserByUid(uid):
    try:
        user=models.user.objects.get(id=uid)
        if not user.loginName=='admin':
            raise ValueError("不能删除系统管理员")
        else:
            user.delete()
            return True
    except:
        return False