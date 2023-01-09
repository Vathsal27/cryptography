from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home ,name = "home"),
    path('register/', views.userRegister ,name = "register"),
    path('login/', views.userLogin ,name = "login"),
    path('logout/', views.userLogout ,name = "logout"),
    path('NA/', views.NA ,name = "NA"),
]