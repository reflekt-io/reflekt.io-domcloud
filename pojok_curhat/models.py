from django.db import models

# Create your models here.
class Curhatan(models.Model):
    fromCurhat = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    message = models.TextField()
