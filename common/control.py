#encoding:utf-8
from django.utils.safestring import mark_safe


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
