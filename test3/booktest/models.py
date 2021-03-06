#coding=utf-8
from django.db import models


# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()  # 发布日期
    bread = models.IntegerField(default=0)  # 阅读量
    bcommet = models.BooleanField(default=0)  #评论量
    isDelete = models.BooleanField(default=False)#逻辑删除
    class Meta:
        db_table = 'bookinfo'  # 指定表的名称


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)  # 英雄姓名
    hgender = models.BooleanField(default=True)  # 英雄性别
    isDelete = models.BooleanField(default=False)  # 逻辑删除
    hcontent = models.CharField(max_length=100)  # 英雄描述信息
    hbook = models.ForeignKey('BookInfo')  # 设置hbook的外键是BookInfo的id