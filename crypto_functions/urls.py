from django.urls import path
from . import views

urlpatterns = [
    path('cryptography/', views.cryptography ,name = "cryptography"),
]