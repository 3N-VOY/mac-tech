from django.urls import path
from base import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path("", views.homepage),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)