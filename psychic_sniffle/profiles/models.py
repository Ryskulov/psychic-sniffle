# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=u'Пользователь')
    avatar = models.ImageField(u'Фотография пользователя', upload_to='upload/avatar_pic/', blank=True, null=True)
    birthday = models.DateField(u'День рождения', blank=True, null=True)
    status = models.CharField(u'Статус', max_length=255, blank=True, null=True)
    phone = models.CharField(u'Мобильный телефон', max_length=30, blank=True, null=True)

    create_add = models.DateTimeField(u'Профиль был создан: ', auto_now_add=True)

    def __unicode__(self):
        return self.user.username
