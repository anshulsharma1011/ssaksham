# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-20 16:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('type', models.CharField(choices=[('s', 'Solo'), ('t', 'Team'), ('b', 'Both')], default='s', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_initials', models.CharField(default='', max_length=20)),
                ('branch_name', models.CharField(default='', max_length=100)),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saksham17.Sports')),
            ],
        ),
    ]
