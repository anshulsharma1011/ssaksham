# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-26 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saksham17', '0006_pointstablecricket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointstablecricket',
            name='team',
            field=models.CharField(choices=[('CSE', 'Computer Science and Engineering'), ('IT', 'Information Technology'), ('ECE', 'Electronics and Communication Engineering'), ('ME', 'Mechanical Engineering'), ('CE', 'Civil Engineering'), ('EN', 'Electricals Engineering'), ('EI', 'Electronics and Instrumentation'), ('MBA', 'MBA'), ('MCA', 'MCA')], default='', max_length=100),
        ),
    ]