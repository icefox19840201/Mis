#encoding:utf-8
import StringIO
import uuid
import json
from django.contrib.messages.storage import session
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,render_to_response,HttpResponseRedirect
from DataAccess.Supplier import supplier_DAC
from ViewModel.Supplier.supplierViewModel import supplierViewMode
from common import utils
from common.Supplier import urlconfig,actionConfig
from Supplier.supperForm import SupplierForm
from common.Supplier import supplier_utils
# Create your views here.
from xlwt import *
from django.core import serializers
import os

def index(request):
    """
    供应商首页及分页以及防止重复数据提交
    :return:
    """
    page_id=''
    stringLink=''
    if utils.Is_GET(request):
       page_id=str(uuid.uuid4())
       request.session["pageid"]=page_id
       stringLink,start,end=supplier_utils.pagging(request)

       return render_to_response(urlconfig.index,
                                 {
                                     'form':SupplierForm(),
                                     'data':supplier_DAC.getAllSupplierInfo()[start:end],
                                     'pageId':page_id,
                                     'paging_link':stringLink
                                 }
                                 )

    elif utils.Is_POST(request):
        if utils.GetData(request,'hid')==request.session["pageid"]:
            form_p=SupplierForm(request.POST)
            if SupplierForm.is_valid:
                stringLink,start,end=supplier_utils.pagging(request)
                page_id=str(uuid.uuid4())
                request.session["pageid"]=page_id
                form_p.save()
                return render_to_response(urlconfig.index,
                                          {
                                           'form':SupplierForm(),
                                           'data':supplier_DAC.getAllSupplierInfo()[start:end],
                                           'pageId':page_id,
                                            'paging_link':stringLink
                                          }

                                          )
        else:
                 page_id=str(uuid.uuid4())
                 request.session["pageid"]=page_id
                 stringLink,start,end=supplier_utils.pagging(request)
                 return render_to_response(
                         urlconfig.index,
                                           {
                                               'form':SupplierForm(),
                                               'data':supplier_DAC.getAllSupplierInfo()[start:end],
                                               'pageId':page_id,
                                               'paging_link':stringLink
                                           }
                 )

        return render_to_response(urlconfig.index,{'form':SupplierForm(),'data':supplier_DAC.getAllSupplierInfo(),'pageId':page_id})


def search(request):
    keywords=str(utils.GetData(request,"keyword")).strip()
    if keywords:
        result=supplier_DAC.SearchSupplierInfo(keywords)

def supplierManage(request):
    '''
    供应商列表管理
    :param request:
    :return:
    '''
    id =utils.GetData(request,"id")
    if utils.Is_GET(request) and utils.GetData(request,"action")=="viewDatails":
        viewmodel=supplier_DAC.getDetailsObjectById(int(id))
        jsonResult=dict(
            Id=viewmodel.Id,
            Sales=viewmodel.Sales,
            SalesPhone=viewmodel.salesPhone,
            Enginner=viewmodel.Enginner,
            EnginnerPhone=viewmodel.EnginnerPhone,
            SupplierName=viewmodel.SupplierName,
            SysType=viewmodel.SysType,
            Address=viewmodel.Address,

        )
        return JsonResponse(jsonResult)
    elif utils.Is_GET(request) and utils.GetData(request,"action")=="delete":
        try:
             supplier_DAC.deleteSupplierById(int(id))
             return JsonResponse({"Msg":"删除成功"})
        except Exception as err:
            msg={"Msg":"删除失败","reson":err.message}
            return JsonResponse(msg)


def Export(request):
    '''
    导出供应商Excel信息
    :param request:
    :return:
    '''
    result=supplier_DAC.expSupplierInfo()
    ws = Workbook(encoding='utf-8')
    w = ws.add_sheet(u"数据报表第一页")
    w.write(0, 0, "销售")
    w.write(0, 1, u"销售电话")
    w.write(0, 2, u"工程师")
    w.write(0, 3, u"工程师电话")
    w.write(0, 4, u"公司")
    excel_row = 1
    for obj in result:
            supplier_sales = obj[0]
            sales_phone = obj[1]
            #data_time = obj.time.strftime("%Y-%m-%d")[:10]
            supplier_engineer = obj[2]
            engineer_phone = obj[3]
            supplier_company=obj[4]
            w.write(excel_row, 0, supplier_sales)
            w.write(excel_row, 1, sales_phone)
            w.write(excel_row, 2, supplier_engineer)
            w.write(excel_row, 3, engineer_phone)
            w.write(excel_row, 4, supplier_company)
            excel_row += 1
    if os.path.exists(u"supplier.xls"):
        os.remove("supplier.xls")
    ws.save("supplier.xls")
    sio = StringIO.StringIO()
    ws.save(sio)
    sio.seek(0)
    response = HttpResponse(sio.getvalue(), content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=supplier.xls'
    response.write(sio.getvalue())
    return response

def supportRecord(request):

    pass












