from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from .models import ScheduleCricket

class ScheduleCricketForm(forms.ModelForm):
    class Meta:
        model = ScheduleCricket
        fields = ['starting_date','closing_date']
