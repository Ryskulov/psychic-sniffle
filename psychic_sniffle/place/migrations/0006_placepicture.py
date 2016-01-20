# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 13:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0005_auto_20160118_0603'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlacePicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='/uploads/places/', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.Place')),
            ],
        ),
    ]
