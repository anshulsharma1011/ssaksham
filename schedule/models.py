from django.db import models
import datetime

# Create your models here.

class ScheduleCricket(models.Model):
    host = models.CharField(max_length=50,default='')
    opponent = models.CharField(max_length=50,default='')
    day = models.DateField(auto_now=False,auto_now_add=False,default=datetime.date.today)
    starting_date = models.DateField(auto_now=False,auto_now_add=False,default=datetime.date.today)
    closing_date = models.DateField(auto_now=False,auto_now_add=False,default=datetime.date.today)

    def __str__(self):
        return self.host
