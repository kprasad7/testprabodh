from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.
class Itemm(models.Model):
    videoo = EmbedVideoField()  # same like models.URLField()
    cap = models.CharField(max_length=100)