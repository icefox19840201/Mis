#encoding:utf-8
from __future__ import unicode_literals

from datetime import datetime, date
from django.db import models

# Create your models here.
from django.utils import timezone


class Supplier(models.Model):
    name=models.CharField("供应商名称",max_length=100,null=False)
    sales=models.CharField("销售人员",max_length=10,null=False)
    sales_phone=models.CharField("销售电话号码",max_length=20,null=True)
    engineer=models.CharField("技术人员",max_length=10,null=True)
    engineer_phone=models.CharField("技术人员电话号码",max_length=20,null=True)
    systemType=models.ForeignKey('sysType',verbose_name='系统类型')
    createDate=models.DateTimeField("创建日期",auto_now_add=True)
    updateDate=models.DateTimeField("更新日期",auto_now=True)
    def getSupplierDropDownList(self):
        return tuple( list(Supplier.objects.values_list('id','name')))

class sysType(models.Model):
    sys_type=models.IntegerField("系统类型",null=False)
    sysDesc=models.CharField("系统类型描述",max_length=200,null=False)
    createDate=models.DateTimeField("创建日期",auto_now_add=True)
    updateDate=models.DateTimeField("创建日期",auto_now=True)

class Supplier_Support_Record(models.Model):
    rec_info=models.CharField("维护记录",max_length=500,null=False)
    rec_support_user=models.CharField("维护人员",max_length=10,null=False)
    Support_Type=models.ForeignKey('SupportType')
    rec_date=models.DateField("维护时间",null=False)
    createDate=models.DateTimeField("创建日期",auto_now_add=True)
    updateDate=models.DateTimeField("创建日期",auto_now=True)

class SupportType(models.Model):
    supportType=models.IntegerField("支持类型",null=False)
    supportDesc=models.CharField("支持类型描述",max_length=100,null=False)
    createDate=models.DateTimeField("创建日期",auto_now_add=True)
    updateDate=models.DateTimeField("创建日期",auto_now=True)

class SupplierInfo(models.Model):
      Supplier_phone=models.CharField("供应商公司电话号码",max_length=20,null=True)
      Manager=models.CharField("供应商经理",max_length=10,null=True)
      Address=models.CharField("供应商地址",max_length=200,null=True)
      Zip_code=models.CharField("邮政编码",max_length=6,null=True)
      Supplier_BizInfo=models.ForeignKey('BusinessInfo')
      createDate=models.DateTimeField("创建日期",auto_now_add=True)
      updateDate=models.DateTimeField("更新日期",auto_now=True)

class BusinessInfo(models.Model):
    bus_info=models.IntegerField("供应商业务类型")
    bus_info_desc=models.CharField("供应商业务描述",max_length=50)
    bus_info_isCore=models.BooleanField("是否为核心业务")
    createDate=models.DateTimeField("创建日期",auto_now_add=True)
    updateDate=models.DateTimeField("更新日期",auto_now=True)




