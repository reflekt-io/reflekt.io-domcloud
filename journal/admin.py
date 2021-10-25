from django.contrib import admin

# Register your models here.
from journal.models import Journal

admin.site.register(Journal)