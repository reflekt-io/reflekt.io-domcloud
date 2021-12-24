from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', home, name='home'),
    path('login', loginUser, name='login'),
    path('register', registerUser, name='register'),
    path('logout', logoutUser, name='logout'),
    path('loginflutter', loginFlutter, name='loginFlutter'),
    path('registerflutter',registerFlutter,name='registerFlutter'),
    path('logoutflutter',logoutFlutter,name='logoutFlutter'),
]
