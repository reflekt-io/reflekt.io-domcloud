from django.urls import path
from main.views import home

app_name = "deteksi_depresi"

urlpatterns = [
    path('', home),
]