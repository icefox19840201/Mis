#encoding:utf-8
from django.utils.safestring import mark_safe

from DataAccess.Supplier import supplier_DAC


def getDropdownList():
    html="""
                 <div class="btn-group" style="float: right;">
                <button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown">功能项
                    <span class="caret"></span>
                </button>
                <ul class="dropdown-menu" role="menu">
                    <li>
                        <a href="/supplier/ex/">导出供应商列表</a>
                    </li>
                    <li>
                        <a href="/supplier/record/" id="record">维护记录</a>
                    </li>
                    <li>
                        <a href="#">维保查询</a>
                    </li>
                       <li>
                        <a href="#">杋房出入登记</a>
                    </li>
                     <li>
                        <a href="#">快速检索</a>
                    </li>
                     <li>
                        <a href="#">维保合同管理</a>
                    </li>
                      <li>
                        <a href="#">添加供应商</a>
                    </li>
                      <li>
                        <a href="#">添加系统类型</a>
                    </li>
                </ul>
            </div>
    """
    return mark_safe(html)

def getSupportTypeDropDownList():
    html="""
      <div class="control-group">
								<label class="control-label" for="input01">维护类型:</label>
								<div class="dropdown">
  <button class="btn btn-default dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropdown" selectvalue="">
    请选择---
    <span class="caret"></span>
  </button>
  <ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu1">


    """
    dropdownListData=supplier_DAC.GetSupportType()

    for item in dropdownListData:
         html+= """<li role="presentation">
                    <a role="menuitem"
                        href="#" onclick="selectSelectedvalue(this)">
                        {0}
                        </a>
                    </li>
             """.format(item.supportDesc)
    html+="""
                <input type="hidden" id="roleid" name="roleid" value="-1"/>
                </ul>
            </div>
        """
    return mark_safe(html)