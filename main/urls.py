from django.urls import path
from main.views import home, loginUser, logoutUser, registerUser

app_name = 'main'

urlpatterns = [
    path('', home, name='home'),
    path('login', loginUser, name='login'),
    path('register', registerUser, name='register'),
    path('logout', logoutUser, name='logout'),
]
