from django.urls import path
from .views import phq9, get_phq9_json

app_name = "deteksi_depresi"

urlpatterns = [
    path('', phq9, name='phq9'),
    path('phq9-json', get_phq9_json, name='phq9-json'),
]