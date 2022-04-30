from dataclasses import fields
from django import forms
from .models import Adresses, Contacts


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['nome', 'email', 'idade', 'número',]


class AdressesForm(forms.ModelForm):
    class Meta:
        model = Adresses
        fields = ['state', 'city', 'street', 'number',]