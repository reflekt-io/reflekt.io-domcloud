from django.urls import path
from .views import index, add_Curhat, navbar, Curhat_list

app_name = "pojok_curhat"

urlpatterns = [
    path('', index, name='index'),
    path('navbar.html', navbar, name='navbar'),
    path('add-curhat', add_Curhat, name='add_curhat'),
    path('curhat-list', Curhat_list, name='curhat_list'),
]