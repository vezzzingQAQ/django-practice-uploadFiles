from django.db import models
from datetime import datetime
# Create your models here.
class Users(models.Model):
    #主键id可以省略不写
    name=models.CharField(max_length=5)
    age=models.IntegerField(default=20)#默认值
    idNumber=models.CharField(max_length=8)
    phoneNumber=models.CharField(max_length=16)

    class Meta:
        db_table="person"
