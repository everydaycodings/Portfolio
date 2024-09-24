from django import forms
from .models import ContactUs
from django.contrib.auth.models import User


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'phone', 'message']