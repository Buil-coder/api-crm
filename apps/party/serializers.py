from rest_framework import serializers

from django.contrib.auth.models import User
from apps.common.models import Document
from apps.common.serializers import document_serializer

from apps.party.models import Staff, StaffRole

class onget_staff_role_serializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField()
    class Meta:
        model=StaffRole
        fields=[
            "id",
            "name",
            "permissions",
            "books",
            "is_default",
            "deleted",
            "created_date",
            "created_by",
            "users",
        ]

    def get_users(self, instance):
        return( Staff.objects.using( self.context.get("tenant") ).filter( role = instance.id ).count() )


class staff_role_serializer(serializers.ModelSerializer):
    class Meta:
        model=StaffRole
        fields="__all__"

    def create(self, validated_data):
        role=StaffRole(**validated_data)
        role.save(using=self.context.get("tenant"))
        return role

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save(update_fields=validated_data.keys(), using=self.context.get("tenant"))
        return instance


class  onget_staff_serializer(serializers.ModelSerializer):
    role=staff_role_serializer("role")

    class Meta:
        model = Staff
        fields = '__all__'

    def get_role(self, instance):
        return staff_role_serializer(StaffRole.objects.using(self.context.get("tenant")).get(id=instance.role_id)).data

    def get_document_type(self, instance):
        return document_serializer(Document.objects.using(self.context.get("tenant")).get(id=instance.document_type_id)).data


class staff_serializer(serializers.ModelSerializer):
    class Meta:
        model=Staff
        fields='__all__'

    def create(self, validated_data):
        tenant = self.context.get("tenant")

        validated_data['user']=self.context.get("user")
        validated_data['role']=StaffRole.objects.using(tenant).get(id=self.context.get("role"))
        validated_data['document_type']=Document.objects.using(tenant).get(id=self.context.get("document_type"))

        staff=Staff(**validated_data)
        staff.save(using=self.context.get("tenant"))

        return staff

    def update(self, instance, validated_data):
        for key,value in validated_data.items():
            setattr(instance,key,value)

        instance.save(update_fields=validated_data.keys(),using=self.context.get("tenant"))
        return instance