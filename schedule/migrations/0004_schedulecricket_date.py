# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-23 17:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_auto_20170811_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedulecricket',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]