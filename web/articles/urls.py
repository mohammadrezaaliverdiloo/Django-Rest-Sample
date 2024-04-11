from django.urls import path
from .views import hello,hello2
# app_name= "frist"

urlpatterns = [
    path('f/',hello,name="hello"),
    path('p/',hello2,name="hello"),
]
