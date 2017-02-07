#encoding:utf-8
from django.utils.safestring import mark_safe

from Asset.models import AssetList

from common import utils

def assetPagging(request):
       pagesize=10
       currentPage=int(utils.GetData(request,"page")) if utils.GetData(request,"page")  else 1
       totalCount=AssetList.objects.all().count()
       pagecount=divmod(totalCount,pagesize)[0] if divmod(totalCount,pagesize)[1]==0 else divmod(totalCount,pagesize)[0]+1
       startPage=(currentPage-1)*pagesize if currentPage>=1 else 0
       endpage=pagesize*currentPage if currentPage<=pagecount else pagecount
       tempstr="""
                <div class="pagination"  style="float:right">
                            <ul>
                                 <li class="disabled">
                                      <a href="/supplier/record/?page={0}">«</a>
                                  </li>
            """.format(startPage)

       for item in range(0,pagecount):
           tempstr+="""
                         <li class="active">
                                    <a href="/supplier/record/?page={0}">{1}</a>
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
       return startPage,endpage,stringLink,totalCount