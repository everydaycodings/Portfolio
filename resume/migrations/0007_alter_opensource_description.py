# Generated by Django 5.1.1 on 2024-09-22 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_alter_opensource_img_alter_opensource_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opensource',
            name='description',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
