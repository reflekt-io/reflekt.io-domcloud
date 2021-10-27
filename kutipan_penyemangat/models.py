from django.db import models
from django.forms import widgets

class Quotes(models.Model):
    name = models.CharField(max_length=70)
    quotes_form = models.CharField(max_length=2000)
