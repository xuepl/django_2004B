import json

from django.db import transaction
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from model_demo.models import Student


# @transaction.atomic
def test_transaction(request):
    transaction.set_autocommit(False)
    try:
        student = Student.objects.get(id=13)
        student.s_sex = 0
        student.save()
        student = Student.objects.get(id=13)
        student.s_sex=0
        student.save()
        transaction.commit()
    except:
        transaction.rollback()
    return HttpResponse("ok")



'''
写一个视图类，
get 查询所有
post 批量新增
update 修改全部
delete 删除所有
'''


class Students(View):

    def get(self,request):
        students = Student.objects.all()
        student_list = []
        for s in students:
            d = {"id":s.id,
                 "name":s.s_name,
                 "sex":s.s_sex,
                 "phone":s.s_phone,
                 "create_time":s.create_time,
                 "update_time":s.update_time
                 }
            student_list.append(d)

        return JsonResponse(student_list,safe=False)


    def post(self,request):
        students = json.loads(request.body)
        # student_list = []
        # for s in students:
        #     student_list.append(Student(s_name=s["name"], s_sex=s["sex"], s_phone=s["phone"]))
        #
        student_list = [Student(s_name=s["name"],s_sex=s["sex"],s_phone=s["phone"]) for s in students]
        Student.objects.bulk_create(student_list)
        return HttpResponse("创建成功")


    def put(self,request):
        students = Student.objects.all()
        data = json.loads(request.body)
        students.update(**data)
        return HttpResponse("修改成功")


    def delete(self,request):
        Student.objects.all().delete()
        return HttpResponse("删除成功")


