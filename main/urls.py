from django.urls import path
from main.views import home, loginUser, logoutUser, project, registerUser, terms, privacy

app_name = 'main'

urlpatterns = [
    path('', home, name='home'),
    path('project', project, name='project'),
    path('terms', terms, name='terms'),
    path('privacy', privacy, name='privacy'),
    path('login/', loginUser, name='login'),
    path('register/', registerUser, name='register'),
    path('logout/', logoutUser, name='logout'),
]
