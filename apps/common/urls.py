from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from apps.common.views  import  (
    panel_common_document_viewset,
    PersonaClientViewSet,
    EmpresaViewSet,
    ProyectoViewSet,
    UnidadViewSet,
    FichaDatosClienteViewSet,
    CronogramaPagosViewSet,
    CuotaViewSet,
    ObservacionesViewSet,
    GrupoViewSet,
    PersonaStaffViewSet,
    DetallePersonaViewSet
)

urlpatterns  = [
    path('document/', panel_common_document_viewset.as_view()),
    path('personaclient/', PersonaClientViewSet.as_view(), name='persona_client_list'),
    path('empresas/', EmpresaViewSet.as_view(), name='empresas'),
    path('proyectos/', ProyectoViewSet.as_view(), name='proyectos'),
    path('unidades/', UnidadViewSet.as_view(), name='unidades'),
    path('fichas/', FichaDatosClienteViewSet.as_view(), name='fichas_datos_cliente'),
    path('cronogramas/', CronogramaPagosViewSet.as_view(), name='cronogramas_pagos'),
    path('cuotas/', CuotaViewSet.as_view(), name='cuotas'),
    path('observaciones/', ObservacionesViewSet.as_view(), name='observaciones'),
    path('grupos/', GrupoViewSet.as_view(), name='grupos'),
    path('personastaff/', PersonaStaffViewSet.as_view(), name='persona_staff_list'),
    path('detallepersona/', DetallePersonaViewSet.as_view(), name='detalle_persona_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)