from django.db import models


def opensourse_img_destination(instance, filename):
    return f'assets/opensource/img/{filename}'


def opensourse_video_destination(instance, filename):
    return f'assets/opensource/videos/{filename}'



# Create your models here.

class StaticAssets(models.Model):
    reference_name = models.CharField(null=True, blank=True)
    name = models.CharField(null=True, blank=True)
    value = models.CharField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Static Asset"  # Singular form
        verbose_name_plural = "Static Assets"  # Plural form


class OpenSource(models.Model):
    number = models.CharField(null=True, blank=True)
    name = models.CharField(null=True, blank=True)
    description = models.TextField(null=True, blank=True, max_length=200)
    img = models.ImageField(upload_to=opensourse_img_destination, null=True, blank=True)
    video = models.FileField(upload_to=opensourse_video_destination, null=True, blank=True)
    tags = models.CharField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    preview = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Open Source"  # Singular form
        verbose_name_plural = "Open Source"  # Plural form