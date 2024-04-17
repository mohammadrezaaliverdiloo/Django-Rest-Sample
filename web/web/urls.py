from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("articles.urls")),
    # path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("allauth.urls")),
    # path("accounts/", include("acc.urls")),
    path('p/',include("pages.urls"))
    
]+ static(
settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

if settings.DEBUG: # new
    import debug_toolbar
    urlpatterns = [
    path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns