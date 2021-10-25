from django import forms
from django.forms import widgets
from journal.models import Journal

# Define widgets
class InputMessage(widgets.Textarea):
    input_type = 'text'

class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ['feeling', 'anxiety_rate', 'summary', 'factor']
        widgets = {'summary': InputMessage()}