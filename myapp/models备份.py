from django.db import models

# Create your models here.


class Course(models.Model):
    '''普通课程'''
    title = models.CharField(max_length=32)

class DegreeCourse(models.Model):
    """
    学位课程
    """
    title = models.CharField(max_length=32)

class PricePolicy(models.Model):
    '''价格策略'''
    price = models.IntegerField()
    period = models.IntegerField()

    table_name = models.CharField(verbose_name='关联的表名称')
    object_id = models.CharField(verbose_name='关联的表中数据行的id')













