#encoding:utf-8
from  app01 import models
def getRoleInfoByRoleId(roleId):
    try:
        return models.userRole.objects.get(id=roleId)
    except:
        raise ValueError("未查找到角色信息")
    return None
def getRole():
    return  models.userRole.objects.all().values("id","role_desc","role_code")

