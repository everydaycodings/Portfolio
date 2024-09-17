# Generated by Django 5.1.1 on 2024-09-17 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staticassets',
            options={'verbose_name': 'Static Asset', 'verbose_name_plural': 'Static Assets'},
        ),
        migrations.AlterField(
            model_name='staticassets',
            name='name',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='staticassets',
            name='reference_name',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='staticassets',
            name='value',
            field=models.CharField(blank=True, null=True),
        ),
    ]
