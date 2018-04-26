from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from myapp.models import DegreeCourse, PricePolicy, Course


def test(request):
    # 1,为学位课添加一个价格策略
    # obj1 = DegreeCourse.objects.filter(title='python全栈').first()
    # PricePolicy.objects.create(price=9.9, period=30, content_object=obj1)
    # obj2 = DegreeCourse.objects.filter(title='python全栈').first()
    # PricePolicy.objects.create(price=19.9, period=60, content_object=obj2)
    # obj3 = DegreeCourse.objects.filter(title='python全栈').first()
    # PricePolicy.objects.create(price=69.9, period=80, content_object=obj3)

    # 2， 为普通课程添加一个价格策略  一个月  9.9
    obj1 = Course.objects.filter(title='restful').first()
    PricePolicy.objects.create(price=9.9, period=30, content_object=obj1)
    obj2 = Course.objects.filter(title='restful').first()
    PricePolicy.objects.create(price=19.9, period=60, content_object=obj2)
    obj3 = Course.objects.filter(title='restful').first()
    PricePolicy.objects.create(price=69.9, period=80, content_object=obj3)

   # 3. 根据课程id获取课程，获取课程所有的价格策略
    course = Course.objects.filter(id=1).first()
    price_policys = course.price_policy_list.all()

    print(price_policys)

    return HttpResponse('ff')