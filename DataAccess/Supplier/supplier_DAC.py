#encoding:utf-8
from Supplier.models import Supplier
def getAllSupplierInfo():
    alldata= list(Supplier.objects.all())
    for item in alldata:
        item.SysDesc=item.systemType.sysDesc
        item.TypeId=item.systemType.id
    return alldata

def getSupplierInfoById(id):
    pass
