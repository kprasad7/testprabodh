from django.contrib import admin
from .models import Itemm
# Register your models here.
from embed_video.admin import AdminVideoMixin

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Itemm, MyModelAdmin)