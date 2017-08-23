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

    def __str__(self):
        return str(self.host + 'vs' +self.opponent )

    def get_abolute_url(self):
        return reverse('saksham17:teams_details',kwargs={'pk':self.pk})

