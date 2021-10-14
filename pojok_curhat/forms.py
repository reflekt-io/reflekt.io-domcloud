# import form class from django
from django.utils.translation import gettext_lazy as _
from django import forms
from django.forms import widgets
from .models import Curhatan



# CurhatForm class for views
class CurhatForm(forms.ModelForm):
    class Meta:
        model = Curhatan
        fields=['to','fromNote','title', 'message']

        fromCurhat = forms.CharField(max_length=50)
        title = forms.CharField(max_length=100)
        message = forms.CharField(max_length=300)

        labels = {

            'fromCurhat': _('From'),
            'title': _('Message Title'),
            'message': _('Message'),
        }
        widgets = {
            'msg_message': forms.Textarea(),
        }

        error_messages = {
		    'required' : 'Input cannot be empty',
	    }
