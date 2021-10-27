from django import forms
from django.forms import widgets
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            'full_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nama lengkap Anda', 'required': 'true'}),
            'query_topic': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Topik pesan Anda', 'required': 'true'}),
            'phone_number': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nomor telepon Anda', 'required': 'true'}),
            'email': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Alamat surel Anda', 'required': 'true'}),
            'message': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Tuliskan pesan Anda', 'required': 'true'}),
        }