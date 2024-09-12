from django.db import models

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