# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-26 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saksham17', '0003_schedulecricket'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedulecricket',
            name='runner_up',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='schedulecricket',
            name='winner',
            field=models.CharField(default='', max_length=100),
        ),
    ]
