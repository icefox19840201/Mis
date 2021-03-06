from __future__ import unicode_literals
#encoding:utf-8
from django.db import models


# Create your models here.
class AssetList(models.Model):
    assetName=models.CharField('资产名称',max_length=20)
    assetType=models.ForeignKey('AssetType')
    local=models.CharField(max_length=50)
    Factory=models.CharField('厂商',max_length=20)
    UserOrDep=models.CharField('使用人或部门',max_length=20)
    createDate=models.DateField(auto_now_add=True)
    updateDate=models.DateField(auto_now=True)

class AssetType(models.Model):
    name=models.CharField('资产类别名称',max_length=20)

class AssetDetails(models.Model):
    UsedFor=models.CharField("用途",max_length=20)
    startDate=models.DateField()
    status=models.IntegerField()   #0停用，1启用，
    asset=models.ForeignKey('AssetList')





