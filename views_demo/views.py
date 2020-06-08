from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect


# Create your views here.

# def helloworld(request):
#     print(request.POST)
#
#     return render(request,"test.html",{"name":"测开大佬们！！"})
#
# def test_redirect(request):
#     return JsonResponse([{"code":0000,"msg":'成功'}],safe=False) # 数据类型为列表，必须指定safe=False
#     # return JsonResponse({"code":0000,"msg":'成功'},safe=False) # 数据类型为字典，不必指定safe
from django.views import View


class Projects(View):

    def get(self,request,pk):
        print(pk)
        return HttpResponse("查询了一个项目")

    def post(self,request,pk):
        return HttpResponse("新增了一个项目")

    def put(self,request,pk):
        return HttpResponse("修改了一个项目")

    def delete(self,request,pk):
        return HttpResponse("删除了一个项目")


from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,HttpRequest
from django.views import View
import json

def login(request):
    content={}
    return render(request,"login.html",context=content)

def loginfor(request):
    print(request.body)
    with open('./static/user.json','r') as f:
        userdata = json.load(f)

    code = {"code":2000,"message":"账号密码错误!"}
    return JsonResponse(dict(code),safe=False)