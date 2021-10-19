from django.urls import path
from .views import index, add_curhat

urlpatterns = [
    path('', index),
    path('add-curhat', add_curhat),
]