from django.urls import path
from main.views import home

app_name = "tembok_harapan"

urlpatterns = [
    path('', home),
]