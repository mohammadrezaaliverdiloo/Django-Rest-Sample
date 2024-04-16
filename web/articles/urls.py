from django.urls import path
from .views import hello,hello2
# app_name= "frist"

urlpatterns = [
    path('f/',hello,name="hello"),
    path('f/uuid:pk>',hello,name="hello-detail"),
    path('p/',hello2,name="helloo"),
    path('p/<uuid:pk>',hello2,name="helloo-datail")
]
