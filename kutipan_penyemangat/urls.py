from django.urls import path
from main.views import home

app_name = "kutipan_penyemangat"

urlpatterns = [
    path('', home),
]