# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-27 05:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0010_auto_20160125_2006'),
        ('profiles', '0004_auto_20160125_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='favorites',
            field=models.ManyToManyField(to='place.Place'),
        ),
    ]
