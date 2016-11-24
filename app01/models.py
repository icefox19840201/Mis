from __future__ import unicode_literals

import uuid
from django.db import models

# Create your models here.
import datetime

class Right(models.Model):
    id=models.UUIDField(default=uuid.uuid4,primary_key=True)
    url=models.URLField()
    queryRight=models.IntegerField(default=1)
    editRight=models.IntegerField(default=1)
    updateRight=models.IntegerField(default=1)
    deleteRight=models.IntegerField(default=1)
    createDate=models.DateField(auto_now_add=True,default=datetime.datetime.now())
    updateDate=models.DateField(auto_now=True,default=datetime.datetime.now())


class user(models.Model):
    id=models.UUIDField(default=uuid.uuid4,primary_key=True)
    loginName=models.CharField(max_length=20)
    usercode=models.CharField(max_length=5)
    pwd=models.CharField(max_length=50)
    username=models.CharField(max_length=20)
    usrRole=models.ForeignKey("userRole")
    createDate=models.DateField(auto_now_add=True,default=datetime.datetime.now())
    updateDate=models.DateField(auto_now=True,default=datetime.datetime.now())

class userRole(models.Model):
    id=models.UUIDField(default=uuid.uuid4,primary_key=True)
    role_desc=models.CharField(max_length=20)
    role_code=models.CharField(max_length=5)
    role_right=models.ManyToManyField("Right")
    createDate=models.DateTimeField(auto_now_add=True,default=datetime.datetime.now())
    updateDate=models.DateField(auto_now=True,default=datetime.datetime.now())
# class Meta:
#     app_label=