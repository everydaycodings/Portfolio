from django.contrib import admin
from .models import StaticAssets, OpenSource, Competitive, Education
# Register your models here.

admin.site.register(StaticAssets)


class OpenSourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'number')


admin.site.register(OpenSource, OpenSourceAdmin)


class CompetitiveAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Competitive, CompetitiveAdmin)


class EducationAdmin(admin.ModelAdmin):
    list_display = ('name', 'year')


admin.site.register(Education, EducationAdmin)