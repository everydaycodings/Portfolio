from django.db import models


def opensourse_img_destination(instance, filename):
    return f'assets/opensource/img/{filename}'


def opensourse_video_destination(instance, filename):
    return f'assets/opensource/videos/{filename}'

def extra_file_destination(instance, filename):
    return f'assets/extra/{filename}'



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


class Competitive(models.Model):
    name = models.CharField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Competitive Programming"  # Singular form
        verbose_name_plural = "Competitive Programming"  # Plural form


class Education(models.Model):
    year = models.CharField(null=True, blank=True)
    name = models.CharField(null=True, blank=True)
    url = models.CharField(null=True, blank=True)
    description = models.TextField(null=True, blank=True, max_length=150)
    grade = models.CharField(null=True, blank=True)
    online = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Education"


class Experience(models.Model):
    year = models.CharField(null=True, blank=True)
    name = models.CharField(null=True, blank=True)
    url = models.CharField(null=True, blank=True)
    description = models.TextField(null=True, blank=True, max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"


class Skill(models.Model):
    name = models.CharField(null=True, blank=True)
    description = models.CharField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"


class Extra(models.Model):
    reference = models.CharField(null=True, blank=True)
    tag1 = models.CharField(null=True, blank=True)
    tag2 = models.TextField(null=True, blank=True)
    tag3 = models.CharField(null=True, blank=True)
    tag4 = models.IntegerField(null=True, blank=True)
    tag5 = models.BooleanField(null=True, blank=True)
    file = models.FileField(upload_to=extra_file_destination, null=True, blank=True)
    tag6 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.reference

    class Meta:
        verbose_name = "Extra"
        verbose_name_plural = "Extra"
