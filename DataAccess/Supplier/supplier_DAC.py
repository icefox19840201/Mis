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
    try:
       return Supplier.objects.get(id=id)
    except Exception as e:
        raise ValueError(e)


def deleteSupplierById(id):
    try:
        obj=Supplier.objects.get(Supplier_name__id=id)
        if not obj:
              obj.delete()
        else:
            raise ValueError('')
    except Exception as e:
        return ValueError(e)

def SearchSupplierInfo(keywords):
    return Supplier.objects.filter(Supplier_name__name__contains=keywords)


