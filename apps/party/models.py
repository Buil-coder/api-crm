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