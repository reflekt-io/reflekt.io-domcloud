from django.db.models import fields
from kutipan_penyemangat.models import Quotes
from django.forms import ModelForm

class QuotesForm(ModelForm):
    class Meta:
        model = Quotes
        fields = ('name', 'quotes_form')

