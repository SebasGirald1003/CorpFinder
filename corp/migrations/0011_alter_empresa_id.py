# Generated by Django 5.0.2 on 2024-03-19 19:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corp', '0010_alter_empresa_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(999999999)]),
        ),
    ]
