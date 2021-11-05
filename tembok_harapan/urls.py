from django.urls import path
from tembok_harapan.views import index, add_harapan

app_name = 'tembok_harapan'

urlpatterns = [
    path('', index, name='index'),
    path('add-harapan', add_harapan, name='add_harapan'),
]