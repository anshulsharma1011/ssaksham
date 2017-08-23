from django import forms
from .models import ScheduleCricket

class ScheduleCricketForm(forms.ModelForm):
    class Meta:
        model = ScheduleCricket
        fields = ['starting_date']
