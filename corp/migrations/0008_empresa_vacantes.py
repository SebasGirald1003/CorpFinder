# Generated by Django 5.0.2 on 2024-03-19 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corp', '0007_remove_empresa_vacantes'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='vacantes',
            field=models.IntegerField(default=0),
        ),
    ]