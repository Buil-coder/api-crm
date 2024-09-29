from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (

    
    

    auth_login_viewset,
    RegisterUserView,
    
)

urlpatterns = [
    path('login/', auth_login_viewset.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),  # Asegúrate de que esta línea esté presente
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)