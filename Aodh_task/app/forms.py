from django import forms
from .models import helth
class healthform(forms.ModelForm):
    class Meta:
        model=helth
        fields='__all__'