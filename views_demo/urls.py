

from django.urls import path, re_path
from . import views
urlpatterns = [
    # path('helloword/', views.helloworld),
    # path('h/', views.test_redirect),
    # path("projects/<int:pk>/",views.Projects.as_view(),{"pk":"123"})
    # re_path(r"^projects/(?P<pk>[\d]+).?$",views.Projects.as_view())
    path('login/', views.login),
    path('loginfor/', views.loginfor),

]
