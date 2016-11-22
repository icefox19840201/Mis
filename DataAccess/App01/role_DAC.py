from  app01 import models
def getRoleInfoByRoleId(roleId):
    try:
        return models.userRole.objects.get(id=roleId)
    except:
        raise ValueError("未查找到角色信息")
    return None

