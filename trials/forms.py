from django.contrib.auth.models import User
from django import forms
from .models import Apply,ApplyCricket,ApplyBadminton,ApplyFootball,ApplyBasketBall,ApplyVolleyBall,ApplyChess,ApplyCarrom,ApplyTableTennis
from django.core.exceptions import ObjectDoesNotExist

class ApplyCricketForm(forms.ModelForm):
    class Meta:
        model = ApplyCricket
        fields = ['player_type','preferred_hand']

class ApplyBadmintonForm(forms.ModelForm):
    class Meta:
        model = ApplyBadminton
        fields = ['preferred_hand','past']

class ApplyFootballForm(forms.ModelForm):
    class Meta:
        model = ApplyFootball
        fields = ['left_or_right','position']

class ApplyBasketballForm(forms.ModelForm):
    class Meta:
        model = ApplyBasketBall
        fields = ['past']

class ApplyVolleyballForm(forms.ModelForm):
    class Meta:
        model = ApplyVolleyBall
        fields = ['past']

class ApplyChessForm(forms.ModelForm):
    class Meta:
        model = ApplyChess
        fields = ['past']

class ApplyCarromForm(forms.ModelForm):
    class Meta:
        model = ApplyCarrom
        fields = ['past']

class ApplyTableTennisForm(forms.ModelForm):
    class Meta:
        model = ApplyTableTennis
        fields = ['past']
