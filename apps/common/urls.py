from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from apps.common.views  import panel_common_document_viewset

urlpatterns  = [
    path('document/', panel_common_document_viewset.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    