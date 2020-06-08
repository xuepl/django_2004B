from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello(request):
    print("我是app01")
    return HttpResponse("app01")