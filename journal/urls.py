from django.urls import path
from journal.views import index, add_journal, get_journal_json

app_name = "journal"

urlpatterns = [
    path('', index, name='index'),
    path('add-journal', add_journal, name='add_journal'),
    path('json', get_journal_json, name='get_json'),
]