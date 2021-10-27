from django.urls import path
from .views import index

app_name = "deteksi_depresi"

urlpatterns = [
    path('', index, name='index'),
]