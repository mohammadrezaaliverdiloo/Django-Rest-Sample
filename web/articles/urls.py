from django.urls import path
from .views import hello
# app_name= "frist"

urlpatterns = [
    path('f/',hello,name="hello"),
]
