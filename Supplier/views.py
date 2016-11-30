import uuid

from django.http import HttpResponse
from django.shortcuts import render,render_to_response

from DataAccess.Supplier import supplier_DAC
from common import utils
from common.Supplier import urlconfig
from Supplier.supperForm import SupplierForm
# Create your views here.
def index(request):
    supplier_table_data=supplier_DAC.getAllSupplierInfo()
    page_id=''
    if utils.Is_GET(request):
       page_id=str(uuid.uuid4())
       request.session["pageid"]=page_id
       return render_to_response(urlconfig.index,{'form':SupplierForm(),'data':supplier_table_data,'pageId':page_id})
    elif utils.Is_POST(request):
        if utils.GetData(request,'hid')==request.session["pageid"]:
            form_p=SupplierForm(request.POST)
            if SupplierForm.is_valid:
                form_p.save()
                page_id=str(uuid.uuid4())
                request.session["pageid"]=page_id
                return render_to_response(urlconfig.index,{'form':SupplierForm(),'data':supplier_table_data,'pageId':page_id})
        else:
                 page_id=str(uuid.uuid4())
                 request.session["pageid"]=page_id
                 return render_to_response(urlconfig.index,{'form':SupplierForm(),'data':supplier_table_data,'pageId':page_id})
        return render_to_response(urlconfig.index,{'form':SupplierForm(),'data':supplier_table_data,'pageId':page_id})





