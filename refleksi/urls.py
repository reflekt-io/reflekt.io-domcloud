from django.urls import path
from .views import index, form_kegiatan

app_name = "refleksi"

urlpatterns = [
    path('', index, name='index'),
    path('add-kegiatan', form_kegiatan, name='add_kegiatan'),
]