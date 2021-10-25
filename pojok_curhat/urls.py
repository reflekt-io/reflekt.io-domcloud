from django.urls import path
from .views import curhat_list, index, add_curhat

app_name = "pojok_curhat"

urlpatterns = [
    path('', index),
    path('add-curhat', add_curhat),
    path('curhat-list', curhat_list)
]