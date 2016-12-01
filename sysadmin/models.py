#encoding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class System(models.Model):
    SystemName=models.CharField(verbose_name='系统名称',max_length=20,null=False)
    sysType=models.ForeignKey('SystemType',verbose_name='系统类型')
    HostName=models.CharField(verbose_name='主机名',max_length=20,null=True)
    IpAddress=models.GenericIPAddressField(verbose_name='IP地址')
    ServerAdminUser=models.CharField(verbose_name='系统管理员用户名',max_length=20,null=False)
    ServerAdminPassword=models.CharField(verbose_name='系统管理员密码',max_length=50,null=False)
    BuyFrom=models.ForeignKey('Factory',verbose_name='购买厂商',null=True)
    onLineDate=models.DateField(verbose_name='上线日期')
    belongTo=models.CharField(verbose_name='负责人',max_length=10,null=False)
    createDate=models.DateField(verbose_name='创建日期',auto_now_add=True)
    updateDate=models.DateField(verbose_name='更新日期',auto_now=True)

class SystemType(models.Model):
    typeId=models.IntegerField(verbose_name='系统类型')
    typeDesc=models.CharField(max_length=20,null=False,verbose_name='系统描述')
    createDate=models.DateField(auto_now_add=True,verbose_name='创建日期')
    updateDate=models.DateField(auto_now=True,verbose_name='更新日期')

class Factory(models.Model):
    Fac_Desc=models.CharField(max_length=20)
