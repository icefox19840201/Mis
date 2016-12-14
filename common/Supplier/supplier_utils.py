#encoding:utf-8
from django.utils.safestring import mark_safe
from DataAccess.Supplier import supplier_DAC
from common import utils


def pagging(request,data=None):

       currentPage=int(utils.GetData(request,"page")) if utils.GetData(request,"page")  else 1
       if currentPage==0:currentPage=1
       pageSize=15
       start=(currentPage-1)*pageSize if currentPage>=1 else 0
       totalCount=supplier_DAC.getAllSupplierInfo().__len__() if not data else data.__len__()
       pagecount=divmod(totalCount,pageSize)[0] if divmod(totalCount,pageSize)[1]==0 else divmod(totalCount,pageSize)[0]+1
       end=currentPage*pageSize if currentPage<=pagecount else pagecount

       tempstr="""
                <div class="pagination">
                            <ul>
                                 <li class="disabled">
                                      <a href="/supplier/index/?page={0}">«</a>
                                  </li>
            """.format(start)

       for item in range(0,pagecount):
           tempstr+="""
                         <li class="active">
                                    <a href="/supplier/index/?page={0}">{1}</a>
                         </li>
                 """.format(item+1,item+1)

       tempstr+="""
                    <li class='disabled'>
                        <a href='#'>»</a>
                    </li>
                </ul>
            </div>
            """
       stringLink=mark_safe(tempstr)
       return stringLink,start,end