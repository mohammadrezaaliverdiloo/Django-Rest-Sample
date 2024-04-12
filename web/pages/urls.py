from django.urls import path

from .views import PagesView

app_name="pages"
urlpatterns = [
    path("pages/" ,PagesView.as_view(), name= "pagesView")

]
