from django.db import models
from django.contrib.auth.models import User

class Kegiatan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    nama = models.CharField(max_length=40)
    deskripsi = models.CharField(max_length=60)