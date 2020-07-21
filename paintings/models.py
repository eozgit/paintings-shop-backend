from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Painting(models.Model):
    title = models.CharField(max_length=100, default='Untitled')
    date = models.DateField()
    media = models.CharField(max_length=100, default='Unknown media')
    height = models.FloatField(validators=[
        MinValueValidator(0, 'Height cannot be less than zero.'),
        MaxValueValidator(100, 'Height cannot be more than 100.')
    ])
    width = models.FloatField(validators=[
        MinValueValidator(0, 'Width cannot be less than zero.'),
        MaxValueValidator(100, 'Width cannot be more than 100.')
    ])
    imageUrl = models.CharField(max_length=100)
    price = models.FloatField()
