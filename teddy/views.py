from django.shortcuts import render
from .models import Item

def homely(request):
    return render(request , "myhome.html")

def video(request):
    obj=Item.objects.all()
    return render(request, 'video.html',{'obj':obj})