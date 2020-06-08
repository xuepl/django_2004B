from django.contrib import admin
from django.urls import path, include
from . import views

app_name="app02"
urlpatterns = [
    path('bye/', views.bye, name="bye"),
    path('login/', views.Login.as_view()),
    path('signup/', views.Signup.as_view()),
]
