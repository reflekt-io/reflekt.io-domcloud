from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class HasilDeteksiDepresi(models.Model):
    date = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    result = models.CharField(max_length=30)
