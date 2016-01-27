# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from place.models import Place # Внимание !!!

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=u'Пользователь')
    avatar = models.ImageField(u'Фотография пользователя', upload_to='upload/avatar_pic/', blank=True, null=True)
    first_name = models.CharField(u'Имя', max_length=255)
    last_name = models.CharField(u'Фамилия', max_length=255)
    birthday = models.DateField(u'День рождения', blank=True, null=True)
    status = models.CharField(u'Статус', max_length=255, blank=True, null=True)
    phone = models.CharField(u'Мобильный телефон', max_length=30, blank=True, null=True)
    create_add = models.DateTimeField(u'Профиль был создан: ', auto_now_add=True)
    favorites = models.ManyToManyField(Place) # Внимание !!!
    def __unicode__(self):
        return self.user.username


@receiver(post_save, sender=User, dispatch_uid="create_profile")
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
