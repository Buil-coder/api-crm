from django.db import models

from django.contrib.auth.models import User
from apps.common.models import Document

from tools.file import FILE


class StaffRole(models.Model):
    name=models.CharField(max_length=250)

    permissions=models.CharField(
        max_length=500,
        null=True,
        default='none',
    )

    is_default=models.BooleanField(
        null=True,
        default=False
    )

    deleted=models.BooleanField(
        null=True,
        default=True
    )

    created_date=models.DateTimeField(auto_now_add=True)

    created_by=models.CharField(
        default='',
        max_length=250,
        null=True
    )


class Staff(models.Model):

    names=models.CharField(
        max_length=250,
        null=True,
    )

    lastnames=models.CharField(
        max_length=250,
        null=True,
    )

    user=models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    role=models.ForeignKey(
        StaffRole,
        default=1,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    document_type=models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    document_number=models.CharField(
        max_length=50,
        null=True,
    )

    created_date=models.DateTimeField(auto_now_add=True)

    created_by=models.CharField(
        default='',
        max_length=250,
        null=True
    )

    deleted=models.BooleanField(
        null=True,
        default=False
    )

    # image=models.ImageField(
    #     upload_to=FILE.image_path,
    #     null=True,
    #     blank=True,
    #     editable=True,
    # )

    # video=models.FileField(
    #     upload_to=FILE.video_path,
    #     null=True,
    #     blank=True,
    #     editable=True,
    # )

    # file=models.FileField(
    #     upload_to=FILE.file_path,
    #     null=True,
    #     blank=True,
    #     editable=True,
    # )

class Persona(models.Model):
    nombres_apellidos = models.CharField(max_length=255)
    celular = models.CharField(max_length=15)
    dni = models.CharField(max_length=8)
    correo = models.CharField(max_length=255)
    conyuge = models.CharField(max_length=255, null=True, blank=True)
    direccion = models.CharField(max_length=255)
    profesion = models.CharField(max_length=255, null=True, blank=True)
    ocupacion = models.CharField(max_length=255, null=True, blank=True)
    centro_trabajo = models.CharField(max_length=255, null=True, blank=True)
    direccion_laboral = models.CharField(max_length=255, null=True, blank=True)
    antiguedad_laboral = models.CharField(max_length=255, null=True, blank=True)
    separacion = models.CharField(max_length=255, null=True, blank=True)
    nombre_rol = models.IntegerField(null=True, blank=True)
    nombre_area = models.IntegerField(null=True, blank=True)
    nombre_origen = models.CharField(max_length=255, null=True, blank=True)
    nombre_canal = models.CharField(max_length=255, null=True, blank=True)
    nombre_medio = models.CharField(max_length=255, null=True, blank=True)
    nombre_usuario = models.IntegerField(null=True, blank=True)


class Observaciones(models.Model):
    descripcion_observaciones = models.CharField(max_length=255)
    adjuntar_informacion = models.CharField(max_length=255, null=True, blank=True)
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE)


class CronogramaPagos(models.Model):
    descripcion_cpagos = models.CharField(max_length=255)
    cuota_inicial = models.FloatField()
    cuota_mensual = models.FloatField()
    fecha_inicio_pago = models.DateField()
    plazo_meses = models.IntegerField()
    plazo_años = models.IntegerField()
    TEA = models.FloatField()
    descuento = models.FloatField()
    dias_pago = models.CharField(max_length=255)
    cuota_balloon = models.FloatField(null=True, blank=True)
    cuota_balloon_meses = models.CharField(max_length=255, null=True, blank=True)


class Cuota(models.Model):
    numero_cuotas = models.CharField(max_length=255)
    fecha_vencimiento = models.DateField()
    deuda_total = models.FloatField()
    amortizacion = models.FloatField()
    id_cpagos = models.ForeignKey(CronogramaPagos, on_delete=models.CASCADE)


class Proyecto(models.Model):
    nombre_proyecto = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_creacion = models.DateField()
    tipo_proyecto = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    id_empresa = models.IntegerField()


class Unidad(models.Model):
    manzana_lote = models.IntegerField()
    area = models.CharField(max_length=255)
    perimetro = models.CharField(max_length=255)
    colindancia_frente = models.CharField(max_length=255, null=True, blank=True)
    colindancia_derecha = models.CharField(max_length=255, null=True, blank=True)
    colindancia_izquierda = models.CharField(max_length=255, null=True, blank=True)
    colindancia_fondo = models.CharField(max_length=255, null=True, blank=True)
    distancia_frente = models.FloatField()
    distancia_derecha = models.FloatField()
    distancia_izquierda = models.FloatField()
    distancia_fondo = models.FloatField()
    precio_m2 = models.FloatField()
    estado = models.CharField(max_length=255)
    id_proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)


class FichaDatosCliente(models.Model):
    id_cpagos = models.ForeignKey(CronogramaPagos, on_delete=models.CASCADE)
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    id_unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)