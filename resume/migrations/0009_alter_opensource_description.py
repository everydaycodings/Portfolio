# Generated by Django 5.1.1 on 2024-09-22 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0008_alter_opensource_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opensource',
            name='description',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
