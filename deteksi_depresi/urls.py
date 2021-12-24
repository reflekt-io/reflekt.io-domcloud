from django.urls import path
from .views import phq9, get_phq9_json, fetch_result_flutter, add_result_flutter

app_name = "deteksi_depresi"

urlpatterns = [
    path('', phq9, name='phq9'),
    path('phq9-json', get_phq9_json, name='phq9-json'),
    path('fetch-result-flutter', fetch_result_flutter, name='fetch-result-flutter'),
    path('add-result-flutter', add_result_flutter, name='add-result-flutter'),
]