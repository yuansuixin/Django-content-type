from django.db import models

# Create your models here.
from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation

from django.contrib.contenttypes.models import ContentType



class Course(models.Model):
    '''普通课程'''
    title = models.CharField(max_length=32)
    # 仅用于反向查找，查找某个课程，可以查出来所有的价格策略
    price_policy_list = GenericRelation('PricePolicy')

class DegreeCourse(models.Model):
    """
    学位课程
    """
    title = models.CharField(max_length=32)

class PricePolicy(models.Model):
    '''价格策略'''
    price = models.IntegerField()
    # 多少天
    period = models.IntegerField()
    # Django的content-type组件自动创建了一个表，存储关联的表名
    content_type = models.ForeignKey(ContentType,verbose_name='关联的表名称')  # 表名称
    object_id = models.IntegerField(verbose_name='关联的表中的数据行的ID')
    # 帮助我们快速实现content-type操作,快速插入数据
    content_object = GenericForeignKey('content_type','object_id')


# 为学位课添加一个价格策略，一个月 9.9
# obj = DegreeCourse.objects.filter(title='python全栈').first()
# # obj.id
# cobj = ContentType.objects.filter(model='course').first()
# PricePolicy.objects.create(price='9.9',period='30',content_type_id=cobj.id,object_id=obj.id)











