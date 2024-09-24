from django.contrib import admin
from .models import StaticAssets, OpenSource, Competitive, Education, Experience, Skill, Extra, ContactUs
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


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('name', 'year')


admin.site.register(Experience, ExperienceAdmin)


class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Skill, SkillAdmin)


class ExtraInfoAdmin(admin.ModelAdmin):
    list_display = ('reference',)


admin.site.register(Extra, ExtraInfoAdmin)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


admin.site.register(ContactUs, ContactUsAdmin)