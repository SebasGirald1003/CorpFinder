# Generated by Django 5.0.2 on 2024-03-19 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corp', '0008_empresa_vacantes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='vacantes',
        ),
    ]
