# Generated by Django 5.0.2 on 2024-03-13 19:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(999999999)])),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=250)),
                ('calificacion', models.IntegerField()),
            ],
        ),
    ]
