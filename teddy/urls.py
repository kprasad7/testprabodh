from django.contrib import admin
from django.urls import path
from teddy import views


urlpatterns = [
    path('', views.homely,name=""),
    path('vid/', views.video, name="video"),
]