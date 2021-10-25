from django.urls import path
<<<<<<< HEAD
from .views import index, add_Curhat, navbar, Curhat_list


urlpatterns = [
    path('', index, name='index'),
    path('navbar.html', navbar, name='navbar'),
    path('add-curhat', add_Curhat, name='add_curhat'),
    path('curhat-list', Curhat_list, name='note_list'),

=======
from .views import index, add_curhat

urlpatterns = [
    path('', index),
    path('add-curhat', add_curhat),
>>>>>>> cfee33232115e578018de7a5a6b4f4b0898ee223
]