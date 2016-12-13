#encoding:utf-8
from Supplier.models import Supplier, SupplierBusinessInfo
from django.db import connection

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

def expSupplierInfo():
    sql="""
                SELECT supplier.sales as '销售',
                     supplier.sales_phone as '销售电话',
                     supplier.engineer as '工程师',
                     supplier.engineer_phone as '工程师电话',
                     business.`name` as '公司'
        FROM supplier_supplier as supplier
        LEFT JOIN
         supplier_supplierbusinessinfo as business
        on
        supplier.Supplier_name_id=business.id
       """
    return execquerySql(sql)

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


