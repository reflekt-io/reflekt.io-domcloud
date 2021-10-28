from django.db import models

class Activity(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=60)