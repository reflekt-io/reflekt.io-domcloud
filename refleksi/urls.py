from django.urls import path
from .views import index, add_kegiatan, add_deskripsi

app_name = "refleksi"

urlpatterns = [
    path('', index, name='index'),
    path('add-kegiatan', add_kegiatan, name='add_kegiatan'),
    path('add-deskripsi', add_deskripsi, name='add_deskripsi'),
]