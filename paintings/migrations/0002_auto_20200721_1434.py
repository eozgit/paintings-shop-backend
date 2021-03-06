# Generated by Django 3.0.8 on 2020-07-21 14:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paintings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='height',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0, 'Height cannot be less than zero.'), django.core.validators.MaxValueValidator(100, 'Height cannot be more than 100.')]),
        ),
        migrations.AlterField(
            model_name='painting',
            name='width',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0, 'Width cannot be less than zero.'), django.core.validators.MaxValueValidator(100, 'Width cannot be more than 100.')]),
        ),
    ]
