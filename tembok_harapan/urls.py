from django.urls import path
from tembok_harapan.views import *

app_name = 'tembok_harapan'

urlpatterns = [
    path('', index, name='index'),
    path('add-harapan', add_harapan, name='add_harapan'),
    path('json-tembok-harapan', json_tembok_harapan, name='json-tembok-harapan'),
    path('add-harapan-flutter',add_harapan_flutter, name='add-harapan-flutter'),
]