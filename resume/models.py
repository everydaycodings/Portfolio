from django.db import models

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