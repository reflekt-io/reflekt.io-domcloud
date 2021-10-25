# import form class from django
from django.utils.translation import gettext_lazy as _
from django import forms
from django.forms import widgets
from .models import Curhatan

# https://stackoverflow.com/questions/3367091/whats-the-cleanest-simplest-to-get-running-datepicker-in-django


# CurhatForm class for views
class CurhatForm(forms.ModelForm):
    class Meta:
        model = Curhatan
        fields=['fromCurhat','title', 'message']

        fromCurhat = forms.CharField(max_length=50, required=True)
        title = forms.CharField(max_length=100, required=True)
        message = forms.Textarea()

        labels = {
            'fromCurhat': _('From'),
            'title': _('Message Title'),
            'message': _('Message'),
        }
        widgets = {
            'message': forms.Textarea(),
        }

        error_messages = {
		    'required' : 'Input cannot be empty',
	    }


