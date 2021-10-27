from django.db import models

# Create your models here.
class Quotes(models.Model):
    name = models.CharField(max_length=40)
    quotes_form = models.TextField()
