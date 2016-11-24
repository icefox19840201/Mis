from __future__ import unicode_literals

from django.db import models
import uuid
# Create your models here.
import datetime
class News(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    source=models.CharField(max_length=20)
    author=models.CharField(max_length=10)
    createTime=models.DateTimeField(auto_now_add=True,default=datetime.datetime.now())
    updateTime=models.DateTimeField(auto_now=True,default=datetime.datetime.now())
    class Meta:
        app_label=""

