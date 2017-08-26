from django import forms
from .models import ScheduleCricket,PointsTableCricket

class ScheduleCricketForm(forms.ModelForm):
    class Meta:
        model = ScheduleCricket
        fields = ['starting_date']

class CreateCricketTableForm(forms.ModelForm):
    class Meta:
        model = PointsTableCricket
        fields = ['team']
