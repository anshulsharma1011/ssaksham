from django.db import models
from django.core.urlresolvers import reverse
import datetime
# Create your models here.

TYPE_CHOICES = (
    ('s','Solo'),
    ('t','Team'),
    ('b','Both'),
)

class Sports(models.Model):
    name = models.CharField(max_length=20,default='')
    type = models.CharField(max_length=5,default='s',choices=TYPE_CHOICES)

    def get_absolute_url(self):
        return reverse('saksham17:sports_details', kwargs={'pk':self.pk})

    def __str__(self):
        return self.name

class Teams(models.Model):
    branch_initials = models.CharField(max_length=20,default='')
    branch_name = models.CharField(max_length=100,default='')

    def __str__(self):
        return self.branch_initials

    def get_abolute_url(self):
        return reverse('saksham17:teams_details',kwargs={'pk':self.pk})

class ScheduleCricket(models.Model):
    host = models.CharField(max_length=100,default='')
    opponent = models.CharField(max_length=100,default='')
    match_no = models.IntegerField(default=0)
    date = models.DateField(auto_now=False,auto_now_add=False,default=datetime.date.today)
    starting_date = models.DateField(auto_now=False,auto_now_add=False,default=datetime.date.today)
    winner = models.CharField(max_length=100,default='')
    runner_up = models.CharField(max_length=100,default='')
    type = models.CharField(max_length=20,default='League')
    played = models.BooleanField(default=False)

    def __str__(self):
        return str(self.host + 'vs' +self.opponent )

    def get_abolute_url(self):
        return reverse('saksham17:teams_details',kwargs={'pk':self.pk})


TeamChoices = (
    ('CSE','CSE'),
    ('IT','IT'),
    ('ECE','ECE'),
    ('ME','ME'),
    ('CE + EI','CE + EI'),
    ('EN','EN'),
    ('MBA + MCA','MBA + MCA'),
)

class PointsTableCricket(models.Model):
    team = models.CharField(max_length=100,default='',choices=TeamChoices)
    matches_played = models.IntegerField(default=0)
    won = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)
    tie = models.IntegerField(default=0)
    no_result = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.team
