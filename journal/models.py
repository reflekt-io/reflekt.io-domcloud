from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Reference: https://docs.djangoproject.com/en/3.2/ref/models/fields/

class Journal(models.Model):
    date = models.DateTimeField(auto_now=True)
    feeling = models.IntegerField(default=3,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    anxiety_rate = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(0),
            MinValueValidator(10)
        ])
    summary = models.TextField()
