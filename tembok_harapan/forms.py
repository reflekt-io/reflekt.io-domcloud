from django import forms
from .models import harapan
# Reordering Form and View

class harapanForm(forms.ModelForm):
    class Meta:
        model = harapan
        fields=['title', 'harapan']


