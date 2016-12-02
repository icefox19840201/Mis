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
       pageSize=3
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



    # response = HttpResponse(content_type='application/vnd.ms-excel')
    # response[
    #     'Content-Disposition'] = 'attachment;filename={0}-{1}.xls'.format("", "")
    # wb = xlwt.Workbook(encoding='utf-8')
    # sheet_prd = wb.add_sheet('PRD')
    # sheet_uat = wb.add_sheet('UAT')
    # sheet_fat = wb.add_sheet('FAT')
    #
    # style_heading = xlwt.easyxf("""
    #     font:
    #         name Arial,
    #         colour_index white,
    #         bold on,
    #         height 0xA0;
    #     align:
    #         wrap off,
    #         vert center,
    #         horiz center;
    #     pattern:
    #         pattern solid,
    #         fore-colour 0x19;
    #     borders:
    #         left THIN,
    #         right THIN,
    #         top THIN,
    #         bottom THIN;
    #     """
    #                             )
    # style_body = xlwt.easyxf("""
    #     font:
    #         name Arial,
    #         bold off,
    #         height 0XA0;
    #     align:
    #         wrap on,
    #         vert center,
    #         horiz left;
    #     borders:
    #         left THIN,
    #         right THIN,
    #         top THIN,
    #         bottom THIN;
    #     """
    #                          )
    # style_green = xlwt.easyxf(" pattern: pattern solid,fore-colour 0x11;")
    # style_red = xlwt.easyxf(" pattern: pattern solid,fore-colour 0x0A;")
    # fmts = [
    #     'M/D/YY',
    #     'D-MMM-YY',
    #     'D-MMM',
    #     'MMM-YY',
    #     'h:mm AM/PM',
    #     'h:mm:ss AM/PM',
    #     'h:mm',
    #     'h:mm:ss',
    #     'M/D/YY h:mm',
    #     'mm:ss',
    #     '[h]:mm:ss',
    #     'mm:ss.0',
    # ]
    # style_body.num_format_str = fmts[0]
    # # 1st line
    # sheet_prd.write(0, 0, '供应商', style_heading)
    # sheet_prd.write(0, 1, '销售人员', style_heading)
    # sheet_prd.write(0, 2, '销售电话', style_heading)
    # sheet_prd.write(0, 3, '技术人员', style_heading)
    # sheet_prd.write(0, 4, '技术电话', style_heading)
    # row = 1
    # contents = supplier_DAC.getAllSupplierInfo()
    # for content in contents:
    #     sheet_prd.write(row, 0, content.name, style_body)
    #     sheet_prd.write(row, 1, content.sales, style_body)
    #     sheet_prd.write(row, 2, content.sales_phone, style_body)
    #     sheet_prd.write(row, 3, content.engineer, style_body)
    #     sheet_prd.write(row, 4, content.engineer_phone, style_body)
    #     # if content.deploy_progress == u'已发布':
    #     #     sheet_prd.write(row, 3, content.deploy_progress, style_green)
    #     # else:
    #     #     sheet_prd.write(row, 3, content.deploy_progress, style_red)
    #     # sheet_prd.write(row, 4, content.jira_issue_no, style_body)
    #     # sheet_prd.write(row, 5, str(content.create_user), style_body)
    #
    #     # 第一行加宽
    #     sheet_prd.col(0).width = 100 * 50
    #     sheet_prd.col(1).width = 200 * 50
    #     sheet_prd.col(2).width = 50 * 50
    #     sheet_prd.col(3).width = 50 * 50
    #     sheet_prd.col(4).width = 200 * 50
    #     sheet_prd.col(5).width = 50 * 50
    #     sheet_prd.col(6).width = 200 * 50
    #     row += 1
    # output = StringIO.StringIO()
    # wb.save(output)
    # output.seek(0)
    # response.write(output.getvalue())
    # return response







