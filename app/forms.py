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

class NewService(forms.ModelForm):
    class Meta:
        model = Service
        exclude = ['area']

class NewEvent(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['area']

class NewHoodForm(forms.ModelForm):
    class Meta:
        model = Hood
        exclude = ['occupants']
