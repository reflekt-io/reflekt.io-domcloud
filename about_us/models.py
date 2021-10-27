from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(verbose_name="Full Name", max_length=100, null=True, blank=True)
    query_topic = models.CharField(verbose_name="Query Topic",max_length=100, null=True, blank=True)
    phone_number = models.CharField(verbose_name="Phone Number", max_length=15, null=True, blank=True)
    email = models.CharField(verbose_name="Email",max_length=100, null=True, blank=True)
    message = models.CharField(verbose_name="Message",max_length=200, null=True, blank=True)