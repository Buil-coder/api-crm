from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views  import (
    staff_viewset,
    staff_role_viewset
)

urlpatterns  = [
    path('staff/',      staff_viewset.as_view()),
    path('staff/role/', staff_role_viewset.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)