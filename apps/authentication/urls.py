from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (

    
    

    auth_login_viewset,
    RegisterUserView,
    
)

urlpatterns  = [
    path('login/',auth_login_viewset.as_view()),
    path('register/', RegisterUserView.as_view(), name='register'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)