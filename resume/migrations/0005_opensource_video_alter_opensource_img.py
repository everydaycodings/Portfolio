# Generated by Django 5.1.1 on 2024-09-22 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_opensource_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='opensource',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='assets/opensource/video/'),
        ),
        migrations.AlterField(
            model_name='opensource',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='assets/opensource/img/'),
        ),
    ]
