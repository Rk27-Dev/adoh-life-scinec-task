from django import forms
from .models import val,Cron
class valform(forms.ModelForm):
    class Meta:
        model=val
        fields=['v1','v2']
class CronForm(forms.ModelForm):
    days = forms.ChoiceField(choices=[(x, x) for x in range(1, 32)])
    class Meta:
        model=Cron
        fields=['name','days']