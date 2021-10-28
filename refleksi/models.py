from django.db import models

class Kegiatan(models.Model):
    nama = models.CharField(max_length=40)
    deskripsi = models.CharField(max_length=60)