from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("articles.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("acc.urls")),
    path('p/',include("pages.urls"))
    
]
