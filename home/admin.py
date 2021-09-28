from django.contrib import admin
from .models import Video, Elsaf, Category
# Register your models here.
from embed_video.admin import AdminVideoMixin

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Video, MyModelAdmin)

admin.site.register(Elsaf)
admin.site.register(Category)
