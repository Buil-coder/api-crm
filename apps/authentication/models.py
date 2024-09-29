from django.db import models

class Persona(models.Model):
    nombres_apellidos = models.CharField(max_length=255)
    celular = models.CharField(max_length=15)
    dni = models.CharField(max_length=8)
    correo = models.EmailField(max_length=255)
    conyuge = models.CharField(max_length=255, blank=True, null=True)
    direccion = models.CharField(max_length=255)
    profesion = models.CharField(max_length=255)
    ocupacion = models.CharField(max_length=255)
    centro_trabajo = models.CharField(max_length=255)
    direccion_laboral = models.CharField(max_length=255)
    antiguedad_laboral = models.CharField(max_length=255)
    separacion = models.CharField(max_length=255, blank=True, null=True)
    nombre_rol = models.IntegerField()
    nombre_area = models.IntegerField()
    nombre_origen = models.CharField(max_length=255)
    nombre_canal = models.CharField(max_length=255)
    nombre_medio = models.CharField(max_length=255)
    nombre_usuario = models.IntegerField()

    def __str__(self):
        return self.nombres_apellidos

class Observacion(models.Model):
    descripcion_observaciones = models.CharField(max_length=255)
    adjuntar_informacion = models.CharField(max_length=255, blank=True, null=True)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion_observaciones

class CronogramaPago(models.Model):
    descripcion_cpagos = models.CharField(max_length=255)
    cuota_inicial = models.FloatField()
    cuota_mensual = models.FloatField()
    fecha_inicio_pago = models.DateField()
    plazo_meses = models.IntegerField()
    plazo_años = models.IntegerField()
    TEA = models.FloatField()
    descuento = models.FloatField()
    dias_pago = models.CharField(max_length=255)
    cuota_Balloon = models.FloatField(blank=True, null=True)
    cuota_Balloon_meses = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.descripcion_cpagos

class Cuota(models.Model):
    numero_cuotas = models.CharField(max_length=255)
    fecha_vencimiento = models.DateField()
    deuda_total = models.FloatField()
    amortizacion = models.FloatField()
    cronograma_pago = models.ForeignKey(CronogramaPago, on_delete=models.CASCADE)

    def __str__(self):
        return self.numero_cuotas

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
    proyecto = models.ForeignKey('Proyecto', on_delete=models.CASCADE)

    def __str__(self):
        return f"Unidad {self.manzana_lote}"

class Proyecto(models.Model):
    nombre_proyecto = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_creacion = models.DateField(auto_now_add=True)
    tipo_proyecto = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_proyecto

class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    representante = models.CharField(max_length=255)
    contrato = models.BinaryField()
    razon_social = models.CharField(max_length=255)
    tipo_empresa = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    ruc = models.CharField(max_length=11)
    pais = models.CharField(max_length=255)
    provincia = models.CharField(max_length=255)
    departamento = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    descripcion_empresa = models.ForeignKey('ConfiguracionEmpresa', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class ConfiguracionEmpresa(models.Model):
    color = models.CharField(max_length=255)
    logo = models.BinaryField()

    def __str__(self):
        return self.color
