from django.urls import path
from .views import add_quotes, index

urlpatterns = [
    path('', index, name='index-kutipanpenyemangat'),
    path('add-quotes', add_quotes, name='add-quotes')
]