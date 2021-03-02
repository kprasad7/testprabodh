from django.db import models

from django.contrib.contenttype.models import ContentType
from django.contrib.contenttype.fields import GenericForeignKey
from django.conf import  settings

User = settings.AUTH_USER_MODEL


class Historyy(models.Model):
    user  = models.ForeignKey(User , on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey


    def __str__(self):
        return 

    class Meta:
        verbose_name_plural = "Histories"