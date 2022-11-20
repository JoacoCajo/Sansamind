from django import forms
from .models import Formul

class AutoForm(forms.ModelForm):
    class Meta: 
        model= Formul
        exclude=["fecha"]
