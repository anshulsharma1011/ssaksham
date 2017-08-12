from django.db import models
from accounts.models import Profile
from django.contrib.auth.models import User

# Create your models here.

STATUS_CHOICES = (
    ('s', 'Selected'),
    ('r', 'Rejected'),
    ('w', 'Waiting'),
)

class Apply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,default='')
    cricket = models.BooleanField(default=False)
    badminton = models.BooleanField(default=False)
    football = models.BooleanField(default=False)
    basketball = models.BooleanField(default=False)
    volleyball = models.BooleanField(default=False)
    chess = models.BooleanField(default=False)
    carrom = models.BooleanField(default=False)
    table_tennis = models.BooleanField(default=False)
    tug_of_war = models.BooleanField(default=False)
    athletics = models.BooleanField(default=False)
    status = models.CharField(max_length=1,default='w',choices=STATUS_CHOICES)

    def __str__(self):
        return self.user.username

CRICKET_CHOICES=(
    ('Opening-Batsman','Opening-Batsman'),
    ('Middle-Order-Batsman','Middle-Order-Batsman'),
    ('Wicket-Keeper-Batsman','Wicket-Keeper-Batsman'),
    ('All-rounder','All-rounder'),
    ('Spinner','Spinner'),
    ('Fast-Bowler','Fast-Bowler'),
)

HAND_CHOICES=(
    ('Right','Right'),
    ('Left','Left'),
)
class ApplyCricket(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    fullname = models.CharField(max_length=30,default='')
    player_type = models.CharField(max_length=30,choices=CRICKET_CHOICES,default='')
    cricket = models.BooleanField(default=False)
    preferred_hand = models.CharField(max_length=6,choices=HAND_CHOICES,default='')

    def __str__(self):
        return self.user.username

BADMINTON_CHOICES=(
    ('District Level','District Level'),
    ('Zonals','Zonals'),
    ('State Level','State Level'),
    ('National Level','National Level'),
    ('Never Played in Tournament','Never Played in Tournament')
)
class ApplyBadminton(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    badminton = models.BooleanField(default=False)
    fullname = models.CharField(max_length=30,default='')
    preferred_hand = models.CharField(max_length=6,choices=HAND_CHOICES,default='')
    past = models.CharField(default='Never Played in Tournament',choices=BADMINTON_CHOICES,max_length=50)

    def __str__(self):
        return self.user.username

FOOTBALL_CHOICES=(
    ('Forward','Forward'),
    ('Mid-fielder','Mid-fielder'),
    ('Defence','Defence'),
)
class ApplyFootball(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    football = models.BooleanField(default=False)
    fullname = models.CharField(max_length=30,default='')
    left_or_right = models.CharField(max_length=6,choices=HAND_CHOICES,default='')
    position = models.CharField(default='Never Played in Tournament',choices=FOOTBALL_CHOICES,max_length=50)

    def __str__(self):
        return self.user.username

class ApplyBasketBall(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    basketball = models.BooleanField(default=False)
    fullname = models.CharField(max_length=30,default='')
    past = models.CharField(default='Never Played in Tournament',choices=BADMINTON_CHOICES,max_length=50)

    def __str__(self):
        return self.user.username

class ApplyVolleyBall(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    volleyball = models.BooleanField(default=False)
    fullname = models.CharField(max_length=30,default='')
    past = models.CharField(default='Never Played in Tournament',choices=BADMINTON_CHOICES,max_length=50)
    def __str__(self):
        return self.user.username

class ApplyChess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chess = models.BooleanField(default=False)
    fullname = models.CharField(max_length=30,default='')
    past = models.CharField(default='Never Played in Tournament',choices=BADMINTON_CHOICES,max_length=50)

    def __str__(self):
        return self.user.username

class ApplyCarrom(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    carrom = models.BooleanField(default=False)
    fullname = models.CharField(max_length=30,default='')
    past = models.CharField(default='Never Played in Tournament',choices=BADMINTON_CHOICES,max_length=50)

    def __str__(self):
        return self.user.username

class ApplyTableTennis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table_tennis = models.BooleanField(default=False)
    fullname = models.CharField(max_length=30,default='')
    past = models.CharField(default='Never Played in Tournament',choices=BADMINTON_CHOICES,max_length=50)

    def __str__(self):
        return self.user.username
