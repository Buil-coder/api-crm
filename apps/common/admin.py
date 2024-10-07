from django.contrib import admin
from .models import (
    Observaciones,
    PersonaClient,
    CronogramaPagos,
    Cuota,
    FichaDatosCliente,
    Empresa,
    Grupo,
    Proyecto,
    Unidad,
    Document,
    PersonaStaff,
    DetallePersona
)

admin.site.register(Observaciones)
admin.site.register(PersonaClient)
admin.site.register(CronogramaPagos)
admin.site.register(Cuota)
admin.site.register(FichaDatosCliente)
admin.site.register(Empresa)
admin.site.register(Grupo)
admin.site.register(Proyecto)
admin.site.register(Unidad)
admin.site.register(Document)
admin.site.register(PersonaStaff)
admin.site.register(DetallePersona)
