from django.urls import path
from main.views import home

app_name = "about_us"

urlpatterns = [
    path('', home),
]