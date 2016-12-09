#encoding:utf-8
import StringIO
import uuid

from django.contrib.messages.storage import session
from django.core.serializers import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,render_to_response,HttpResponseRedirect
from DataAccess.Supplier import supplier_DAC
from common import utils
from common.Supplier import urlconfig,actionConfig
from Supplier.supperForm import SupplierForm
from common.Supplier import supplier_utils
# Create your views here.
import xlwt
from django.core import serializers

def index(request):

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
    id =utils.GetData(request,"id")
    if utils.Is_GET(request) and utils.GetData(request,"action")=="viewDatails":
        supplierobj= json.dumps(supplier_DAC.getSupplierInfoById(id))
        return JsonResponse(supplierobj)
    elif utils.Is_GET(request) and utils.GetData(request,"action")=="delete":
        pass











