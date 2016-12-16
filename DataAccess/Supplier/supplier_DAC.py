#encoding:utf-8
from Supplier.models import Supplier, SupplierBusinessInfo
from django.db import connection

from ViewModel.Supplier.supplierViewModel import supplierViewMode


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
           raise ValueError("删除失败")
    except Exception as e:
        raise ValueError(e)

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

def getDetails(id):
    if not id:
        raise ValueError(u"传入参数不能为空")
    if not isinstance(id,int):
        raise TypeError(u"传入参数类型非法")
    sql="""
                 SELECT * FROM(
                SELECT  supplier.id,
                                supplier.sales,
                                supplier.sales_phone,
                                supplier.engineer,
                                supplier.engineer_phone,
                                bussiness.`name`,
                                sysType.sysDesc,
                        supInfo.Address,
                        supInfo.Manager,
                                supInfo.Supplier_phone,
                                supInfo.Zip_code
                                FROM supplier_supplier supplier
                LEFT JOIN
                    supplier_supplierbusinessinfo bussiness
                on
                    Supplier_name_id=bussiness.id
                LEFT JOIN
                    supplier_systype sysType
                on
                    supplier.systemType_id=sysType.id
                LEFT JOIN
                    supplier_supplierinfo supInfo
                ON
                    bussiness.id=supInfo.Supplier_BizInfo_id
                ) as details
                where id={0}


       """.format(id)
    return  getSingleResultByQuerySql(sql)

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

def getDetailsObjectById(id):
      supplierDetails=getDetails(int(id))
      viewmodel=supplierViewMode()
      viewmodel.Id=supplierDetails[0]
      viewmodel.Sales=supplierDetails[1]
      viewmodel.SalesPhone=supplierDetails[2]
      viewmodel.Enginner=supplierDetails[3]
      viewmodel.EnginnerPhone=supplierDetails[4]
      viewmodel.SupplierName=supplierDetails[5]
      viewmodel.SysType=supplierDetails[6]
      viewmodel.Address=supplierDetails[7]
      viewmodel.SupplierManager=supplierDetails[8]
      viewmodel.Supplier_phone=supplierDetails[9]
      viewmodel.ZipCode=supplierDetails[10]
      return viewmodel



