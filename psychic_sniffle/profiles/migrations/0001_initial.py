# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-23 14:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='upload/avatar_pic/', verbose_name='\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='\u0414\u0435\u043d\u044c \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f')),
                ('status', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441')),
                ('phone', models.CharField(blank=True, max_length=30, null=True, verbose_name='\u041c\u043e\u0431\u0438\u043b\u044c\u043d\u044b\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('create_add', models.DateTimeField(auto_now_add=True, verbose_name='\u041f\u0440\u043e\u0444\u0438\u043b\u044c \u0431\u044b\u043b \u0441\u043e\u0437\u0434\u0430\u043d: ')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c')),
            ],
        ),
    ]
