from django.contrib import admin
from .models import MakerSpace


class MakerSpaceAdmin(admin.ModelAdmin):
    list_display = ('prompt',)
# Register your models here.
admin.site.register(MakerSpace,MakerSpaceAdmin)  #註冊至Administration(管理員後台)
