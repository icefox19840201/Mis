#encoding:utf-8
from Supplier.models import Supplier, SupplierBusinessInfo, Supplier_Support_Record, SupportType
from django.db import connection
from . import sqlhelper
from ViewModel.Supplier.supplierViewModel import supplierViewMode
from ViewModel.Supplier.recordViewModel import Record


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
        obj=Supplier.objects.get(id=id)
        if obj:
              obj.delete()
        else:
           raise ValueError("删除失败")
    except Exception as e:
        raise ValueError("删除失败,原因%s"%e)

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
    return sqlhelper.execquerySql(sql)

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
    return  sqlhelper.getSingleResultByQuerySql(sql)

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

def getSupportRecord():
    sql="""
                    SELECT
                    record.rec_info,
                    record.rec_support_user,
                supporttype.supportDesc,
                    record.rec_date
            from supplier_supplier_support_record record
            LEFT JOIN supplier_supporttype supporttype
            on
            record.Support_Type_id=supportType.id
       """
    return  sqlhelper.execquerySql(sql)


def getRecordViewModel():

      sqlresult=getSupportRecord()
      result=[]
      for item in sqlresult:
            viewModel=Record()
            viewModel.SupportContent=item[0]
            viewModel.SupportUser=item[1]
            viewModel.SuportType=item[2]
            viewModel.SuportTime=str(item[3])
            result.append(viewModel)
      return result

def GetSupportType():
    return SupportType.objects.all().values("id","supportDesc")

def createSupportRecord(viewModel):
    model=Supplier_Support_Record()
    model.Support_Type=viewModel.SuportType
    model.rec_info=viewModel.SupportContent
    try:

        model.save()
    except Exception as e:
        raise e



