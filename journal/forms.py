from django import forms
from django.forms import widgets
from journal.models import Journal

# Set choices for radio button parts
FEELINGS = [('1', 'Sangat Buruk'),
            ('2', 'Buruk'),
            ('3', 'Biasa Saja'),
            ('4', 'Baik'),
            ('5', 'Sangat Baik')]

ANXIETY_RATE = [('0', '0'),
                ('1', '1'),
                ('2', '2'),
                ('3', '3'),
                ('4', '4'),
                ('5', '5'),
                ('6', '6'),
                ('7', '7'),
                ('8', '8'),
                ('9', '9'),
                ('10', '10')]

# Define widgets
class InputMessage(widgets.Textarea):
    input_type = 'text'

class JournalForm(forms.ModelForm):
    feeling = forms.ChoiceField(choices=FEELINGS, widget=forms.RadioSelect())
    anxiety_rate = forms.ChoiceField(choices=ANXIETY_RATE, widget=forms.RadioSelect())

    class Meta:
        model = Journal
        fields = ['feeling', 'anxiety_rate', 'summary']
        widgets = {'summary': InputMessage()}