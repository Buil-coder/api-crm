from rest_framework import serializers
from apps.common.models import Document

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