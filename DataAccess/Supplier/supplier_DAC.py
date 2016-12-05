#encoding:utf-8
from Supplier.models import Supplier, SupplierBusinessInfo


def getAllSupplierInfo():
    alldata= list(Supplier.objects.all().order_by("-id"))
    for item in alldata:
        item.SysDesc=item.systemType.sysDesc
        item.TypeId=item.systemType.id
        item.name=item.Supplier_name.name

    return alldata


def getSupplierInfoById(id):

    pass

def deleteSupplierById(id):
    try:
        obj=Supplier.objects.get(Supplier_name__id=id)
        if not obj:
              obj.delete()
    except:
        return ValueError("")

