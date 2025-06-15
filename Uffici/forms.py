from django import forms
from .models import Reparto

class RepartoForm(forms.ModelForm):
    class Meta:
        model = Reparto
        fields = ['managers']
        widgets = {
            'managers': forms.CheckboxSelectMultiple
        }
