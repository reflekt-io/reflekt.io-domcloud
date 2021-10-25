from django.urls import path
from journal.views import index, add_journal

app_name = "journal"

urlpatterns = [
    path('', index, name='index'),
    path('add-journal', add_journal, name='add_journal'),
]