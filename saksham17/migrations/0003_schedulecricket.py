# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-23 17:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saksham17', '0002_remove_teams_sport'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleCricket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(default='', max_length=100)),
                ('opponent', models.CharField(default='', max_length=100)),
                ('match_no', models.IntegerField(default=0)),
                ('date', models.DateField(default=datetime.date.today)),
                ('starting_date', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]