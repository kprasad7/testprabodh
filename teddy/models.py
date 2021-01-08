from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField

class Question(models.Model):
    qimage = models.ImageField(null=True,blank=True)
    op1 = models.CharField(max_length=100)
    op2 = models.CharField(max_length=100)
    op3 = models.CharField(max_length=100)
    op4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
class Drive(models.Model):
    field_name = models.URLField(max_length=200)  
    field_link = models.CharField(max_length=200)  

class Item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()

class student(models.Model):
    user = models.OneToOneField(User , null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateField(auto_now_add=True, null=True)
    simage = models.ImageField(null=True,blank=True)

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class extra(models.Model):
    ename = models.CharField(max_length=200, null=True)

class twoextra(models.Model):
    tname = models.CharField(max_length=200, null=True)    

class Video(models.Model):
    caption =models.CharField(max_length=100)
    video=models.FileField(upload_to="video/%y")

    def __str__(self):
        return self.caption