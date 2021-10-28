from django.urls import path
from pojok_curhat.views import index, add_curhat, navbar, curhat_list, json_pojok_curhat

app_name = "pojok_curhat"

urlpatterns = [
    path('', index, name='index'),
    path('json', json_pojok_curhat, name = 'json_pojok_curhat'),
    path('navbar', navbar, name='navbar'),
    path('add-curhat', add_curhat, name='add_curhat'),
    path('curhat-list', curhat_list, name='curhat_list'),
]