from rest_framework import serializers
from apps.common.models import Document

from apps.common.models import (
    PersonaClient,
    Empresa,
    Proyecto,
    Unidad,
    FichaDatosCliente,
    CronogramaPagos,
    Cuota,
    Observaciones,
    Grupo,
    PersonaStaff,
    DetallePersona
)

class PersonaClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaClient
        fields = '__all__'  # Puedes especificar los campos específicos si lo deseas
    
    def create(self, validated_data):
        persona = PersonaClient(**validated_data)
        persona.save(using=self.context.get("tenant"))
        return persona

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save(using=self.context.get("tenant"))
        return instance

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

    def create(self, validated_data):
        empresa = Empresa(**validated_data)
        empresa.save(using=self.context.get("tenant"))
        return empresa

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save(using=self.context.get("tenant"))
        return instance


class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = '__all__'

    def create(self, validated_data):
        proyecto = Proyecto(**validated_data)
        proyecto.save(using=self.context.get("tenant"))
        return proyecto

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save(using=self.context.get("tenant"))
        return instance


class UnidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidad
        fields = '__all__'

    def create(self, validated_data):
        unidad = Unidad(**validated_data)
        unidad.save(using=self.context.get("tenant"))
        return unidad

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save(using=self.context.get("tenant"))
        return instance


class FichaDatosClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FichaDatosCliente
        fields = '__all__'

    def create(self, validated_data):
        ficha = FichaDatosCliente(**validated_data)
        ficha.save(using=self.context.get("tenant"))
        return ficha

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save(using=self.context.get("tenant"))
        return instance


class CronogramaPagosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CronogramaPagos
        fields = '__all__'

    def create(self, validated_data):
        cronograma = CronogramaPagos(**validated_data)
        cronograma.save(using=self.context.get("tenant"))
        return cronograma

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save(using=self.context.get("tenant"))
        return instance


class CuotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuota
        fields = '__all__'

    def create(self, validated_data):
        cuota = Cuota(**validated_data)
        cuota.save(using=self.context.get("tenant"))
        return cuota

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save(using=self.context.get("tenant"))
        return instance


class ObservacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observaciones
        fields = '__all__'

    def create(self, validated_data):
        observacion = Observaciones(**validated_data)
        observacion.save(using=self.context.get("tenant"))
        return observacion

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save(using=self.context.get("tenant"))
        return instance


class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = '__all__'

    def create(self, validated_data):
        grupo = Grupo(**validated_data)
        grupo.save(using=self.context.get("tenant"))
        return grupo

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save(using=self.context.get("tenant"))
        return instance




class document_serializer(serializers.ModelSerializer):
    class Meta:
        model   = Document
        fields  = '__all__'

    def create(self, validated_data):
        document = Document(**validated_data)
        document.save(using=self.context.get("tenant"))
        return document

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            getattr(instance, key)
            setattr(instance, key, value)
        instance.save(update_fields=validated_data.keys(), using=self.context.get("tenant"))
        return instance
    

# 06-10-24 | nuevos serializers

class PersonaStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaStaff
        fields = '__all__'  # Puedes especificar los campos específicos si lo deseas
    
    def create(self, validated_data):
        persona = PersonaStaff(**validated_data)
        persona.save(using=self.context.get("tenant"))
        return persona

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save(using=self.context.get("tenant"))
        return instance
  
    
class DetallePersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePersona
        fields = '__all__'  # Puedes especificar los campos específicos si lo deseas
    
    def create(self, validated_data):
        persona = DetallePersona(**validated_data)
        persona.save(using=self.context.get("tenant"))
        return persona

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save(using=self.context.get("tenant"))
        return instance