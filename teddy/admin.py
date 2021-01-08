from django.contrib import admin
from teddy.models import Question,Drive,Item,student,Document,extra,twoextra,Video
from embed_video.admin import AdminVideoMixin
admin.site.register(Question)
admin.site.register(Drive)
admin.site.register(student)
admin.site.register(Document)
admin.site.register(extra)
admin.site.register(twoextra)
admin.site.register(Video)

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Item, MyModelAdmin)