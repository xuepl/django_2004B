import json

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from utils.token import create_token

# Create your views here.
from django.urls import reverse
from django.views import View


def bye(request):
    return HttpResponse("ok")


class Login(View):

    def post(self,request):
        data = json.loads(request.body)
        username = data.get("username",None)
        password = data.get("password",None)
        user = authenticate(username=username,password=password) # 校验用户名和密码，成功返回user对象，失败返回None
        if user:
            token = create_token(user.username)
            return JsonResponse({"code": "0000", "message": "登录成功", "data": token})
        else:
            return JsonResponse({"code": "9999", "message": "用户名或者密码不正确", "data": None})


class Signup(View):

    def post(self,request):
        data = json.loads(request.body)
        username = data.get("username",None)
        password = data.get("password",None)
        email = data.get("email",None)
        try:
            user = User.objects.create_user(username=username,password=password,email=email)
            token = create_token(user.username)
            return JsonResponse({"code":"0000","message":"注册成功","data":token})
        except:
            return JsonResponse({"code": "9999", "message": "用户已存在或者注册信息缺失", "data": None})

