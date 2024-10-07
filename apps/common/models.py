from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Document(models.Model):

    symbol=models.CharField(
        max_length=10,
        blank=True,
        null=True
    )

    name=models.CharField(
        max_length=250,
        blank=True,
        null=True
    )

    is_principal=models.BooleanField(
        default=False,
        null=True
    )

    max_length=models.IntegerField(
        default=1,
        null=True,
    )

    deleted=models.BooleanField(
        default=False,
        null=True
    )

    created_date = models.DateTimeField(auto_now_add = True)

    created_by=models.CharField(
        default='',
        max_length=250,
        null=True
    )


class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    representante = models.CharField(max_length=255)
    contrato = models.BinaryField(blank=True, null=True)
    razon_social = models.CharField(max_length=255)
    tipo_empresa = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    ruc = models.CharField(max_length=11)
    pais = models.CharField(max_length=255)
    provincia = models.CharField(max_length=255)
    departamento = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    id_descri_empresa = models.IntegerField()

    def __str__(self):
        return self.nombre


class Proyecto(models.Model):
    nombre_proyecto = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_creacion = models.DateField()
    tipo_proyecto = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    id_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_proyecto


class Unidad(models.Model):
    manzana_lote = models.IntegerField()
    area = models.CharField(max_length=255)
    perimetro = models.CharField(max_length=255)
    colindancia_frente = models.CharField(max_length=255)
    colindancia_derecha = models.CharField(max_length=255)
    colindancia_izquierda = models.CharField(max_length=255)
    colindancia_fondo = models.CharField(max_length=255)
    distancia_frente = models.FloatField()
    distancia_derecha = models.FloatField()
    distancia_izquierda = models.FloatField()
    distancia_fondo = models.FloatField()
    precio_m2 = models.FloatField()
    estado = models.CharField(max_length=255)
    id_proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

    def __str__(self):
        return f'Unidad {self.manzana_lote}'


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
    cuota_Balloon = models.FloatField()
    cuota_Balloon_meses = models.CharField(max_length=255)

    def __str__(self):
        return self.descripcion_cpagos


class FichaDatosCliente(models.Model):
    estado_legal = models.CharField(max_length=255)
    fecha_cierre = models.DateField(max_length=255)
    fecha_separacion = models.DateField()
    cod_boleta = models.CharField(max_length=100)
    asesor = models.CharField(max_length=255)

    id_cpagos = models.ForeignKey(CronogramaPagos, on_delete=models.CASCADE)
    id_lote = models.ForeignKey(Unidad, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cronograma {self.id_cpagos} - Lote {self.id_lote}"


class Cuota(models.Model):
    numero_cuotas = models.CharField(max_length=255)
    fecha_vencimiento = models.DateField()
    deuda_total = models.FloatField()
    amortizacion = models.FloatField()
    id_cpagos = models.ForeignKey(CronogramaPagos, on_delete=models.CASCADE)

    def __str__(self):
        return f'Cuota {self.numero_cuotas}'


class PersonaClient(models.Model):
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    genero = models.CharField(max_length=255)
    celular = models.CharField(max_length=15)
    correo = models.EmailField(max_length=255)
    pais = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    distrito = models.CharField(max_length=100)
    fecha_creacion = models.DateField()
    ocupacion = models.CharField(max_length=255)
    centro_trabajo = models.CharField(max_length=255)
    tipo_documento = models.CharField(max_length=255)
    num_documento = models.CharField(max_length=255)
    conyuge = models.BooleanField()
    telefono_fijo = models.CharField(max_length=10)

    def __str__(self):
        return self.nombres


class Observaciones(models.Model):
    descripcion_observaciones = models.CharField(max_length=255)
    adjuntar_informacion = models.CharField(max_length=255)
    id_persona_client = models.ForeignKey(PersonaClient, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion_observaciones


class Grupo(models.Model):
    nombre = models.CharField(max_length=255)
    representante = models.CharField(max_length=255)
    contrato = models.BinaryField(blank=True, null=True)
    field_1 = models.CharField(max_length=255)
    field_2 = models.CharField(max_length=255)
    field_3 = models.CharField(max_length=255)
    id_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    

# 06-10-24 | nuevos modelos


class DetallePersona(models.Model):
    tipo_cliente = models.CharField(max_length=255)
    usuario = models.BooleanField(default=False) 
    canal = models.CharField(max_length=255)
    medio = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    origen = models.CharField(max_length=255)
    id_persona_client = models.ForeignKey(
        PersonaClient, on_delete=models.CASCADE)
    id_fichadc = models.ForeignKey(
        FichaDatosCliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"Persona cliente {self.id_persona_client} - Ficha de datos {self.id_fichadc}"


class PersonaStaff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    dni = models.CharField(max_length=8)
    conyuge = models.BooleanField(default=False)
    correo = models.EmailField(max_length=100)
    celular = models.CharField(max_length=9)
    fecha_inicio = models.DateField(default=timezone.now)  # Fecha por defecto: hoy
    fecha_fin = models.DateField()
    rol = models.CharField()

    id_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return f"Persona staff {self.nombres}" 