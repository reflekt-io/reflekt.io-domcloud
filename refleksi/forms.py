from django import forms
from .models import Kegiatan

class KegiatanForm(forms.ModelForm):
    class Meta: 
        model = Kegiatan
        exclude = ['user']