from django.contrib import admin
from .models import StaticAssets, OpenSource
# Register your models here.

admin.site.register(StaticAssets)


class OpenSourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'number')


admin.site.register(OpenSource, OpenSourceAdmin)