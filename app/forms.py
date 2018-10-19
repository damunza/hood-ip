from django import forms
from .models import *

class NewResidentForm(forms.ModelForm):
    class Meta:
        model = Resident
        exclude = ['name', 'home']

class NewBusiness(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['owner', 'neighbourhood']