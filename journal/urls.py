from django.urls import path
from journal.views import index, add_journal, get_journal_json, add_journal_flutter

app_name = "journal"

urlpatterns = [
    path('', index, name='index'),
    path('add-journal', add_journal, name='add_journal'),
    path('json', get_journal_json, name='get_json'),
    path('add-journal-flutter', add_journal_flutter, name='add_journal_flutter'),
]