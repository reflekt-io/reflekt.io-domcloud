from django.urls import path
from .views import index

app_name = "about_us"

urlpatterns = [
    path('', index, name='index'),
]