from django import forms
from .models import ScheduleCricket,PointsTableCricket, MatchDetails

class ScheduleCricketForm(forms.ModelForm):
    class Meta:
        model = ScheduleCricket
        fields = ['starting_date']

class CreateCricketTableForm(forms.ModelForm):
    class Meta:
        model = PointsTableCricket
        fields = ['team']

class MatchDetailsForm(forms.ModelForm):
    class Meta:
        model = MatchDetails
        fields = ['player_name','match_no']
