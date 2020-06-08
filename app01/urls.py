from django.contrib import admin
from django.urls import path, include
from . import views

app_name="app01"
urlpatterns = [
    path('hello/', views.hello, name="hello"),
]
