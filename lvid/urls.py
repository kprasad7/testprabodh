from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path("s" , views.syllabus , name="s" ),
    path("s1" , views.syllabus1 , name="s1" ),
    path("s2" , views.syllabus2 , name="s2" ),
    path("s3" , views.syllabus3 , name="s3" ),
    path("s4" , views.syllabus4 , name="s4" ),
    path("s5" , views.syllabus5 , name="s5" ),
]
    
    