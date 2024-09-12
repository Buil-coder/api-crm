from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.conf import settings
from django.urls import path, include, re_path
from rest_framework import permissions
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

schema_view=get_schema_view(
    openapi.Info(
        title="backend.com API",
        default_version='v2',
        description="backend.com v1",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="neil.cuadros.miraval@gmail.com"),
        license=openapi.License(name="backend.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path( route='auth/',        view=include('apps.authentication.urls') ),
    path( route='common/',      view=include('apps.common.urls')         ),
    path( route='party/',       view=include('apps.party.urls')          ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns+=[re_path(r'^media/(?P<path>.*)$',serve,{'document_root': settings.MEDIA_ROOT})]