from django import forms
from django.forms import widgets
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            'full_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Full Name', 'required': 'true'}),
            'query_topic': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Query Topic', 'required': 'true'}),
            'phone_number': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Phone Number', 'required': 'true'}),
            'email': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Email Address', 'required': 'true'}),
            'message': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Your Message', 'required': 'true'}),
        }