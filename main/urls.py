from django.urls import path

from main.views import home, project, terms, privacy

app_name = 'main'

urlpatterns = [
    path('', home, name='home'),
    path('project', project, name='project'),
    path('terms', terms, name='terms'),
    path('privacy', privacy, name='privacy'),
]
