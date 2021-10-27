from django.urls import path
from main.views import home
from kutipan_penyemangat.views import add_quotes, index, json_kutipan_penyemangat

app_name = "kutipan_penyemangat"

urlpatterns = [
    path('', home),
    path('', index, name='index-kutipan-penyemangat'),
    path('add-quotes', add_quotes, name='add-quotes'),
    path('json', json_kutipan_penyemangat, name='json-kutipan-penyemangat'),
]