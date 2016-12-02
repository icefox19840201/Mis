#encoding:utf-8
import StringIO
import uuid
from django.http import HttpResponse
from django.shortcuts import render,render_to_response
from django.utils.safestring import mark_safe
from DataAccess.Supplier import supplier_DAC
from common import utils
from common.Supplier import urlconfig
from Supplier.supperForm import SupplierForm
# Create your views here.
import xlwt

def index(request):
    page_id=''
    if utils.Is_GET(request):
       page_id=str(uuid.uuid4())
       request.session["pageid"]=page_id

       currentPage=int(utils.GetData(request,"page")) if utils.GetData(request,"page") else 1
       pageSize=1
       start=(currentPage-1)*pageSize if currentPage>=1 else 0
       totalCount=supplier_DAC.getAllSupplierInfo().__len__()
       pagecount=divmod(totalCount,pageSize)[0] if divmod(totalCount,pageSize)[1]==0 else divmod(totalCount,pageSize)[0]+1
       end=currentPage*pageSize if currentPage<=pagecount else pagecount
       tempstr="""<div class="pagination">
                            <ul>
                            <li class="disabled">
                                    <a href="#">«</a>
                                </li>"""
       for item in range(0,pagecount):
           tempstr+="""
                         <li class="active">
                                    <a href="/supplier/index/?page={0}">{1}</a>
                         </li>
                 """.format(item+1,item+1)
       tempstr+=" <li class='disabled'><a href='#'>»</a> </li></ul></div>"
       stringLink=mark_safe(tempstr)
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
                form_p.save()
                page_id=str(uuid.uuid4())
                request.session["pageid"]=page_id
                return render_to_response(urlconfig.index,{'form':SupplierForm(),'data':supplier_DAC.getAllSupplierInfo(),'pageId':page_id})
        else:
                 page_id=str(uuid.uuid4())
                 request.session["pageid"]=page_id
                 return render_to_response(urlconfig.index,{'form':SupplierForm(),'data':supplier_DAC.getAllSupplierInfo(),'pageId':page_id})
        return render_to_response(urlconfig.index,{'form':SupplierForm(),'data':supplier_DAC.getAllSupplierInfo(),'pageId':page_id})










