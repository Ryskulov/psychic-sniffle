# -*- coding: utf-8 -*- 
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class PlaceTag(models.Model):
    name = models.CharField(u'Название', max_length=255)

    def __unicode__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(u'Название ', max_length=30)
    slug = models.SlugField(u'Slug')
    created = models.DateTimeField(u'Дата регистрации: ', auto_now_add=True)
    modified = models.DateTimeField(u'Дата изменения: ', auto_now=True)
    main_foto = models.ImageField(u'Фотография заведения', upload_to='media/')
    tags = models.ManyToManyField(PlaceTag, related_name="place" )
    work_time = models.CharField(u'График работы', max_length=100)
    adress = models.CharField(u'Адрес', max_length=100)
    short_description = models.TextField(u'Краткое описание')
    description = models.TextField(u'Полное описание')

    class Meta:
        verbose_name = u'заведение'
        verbose_name_plural = u'заведения'
    
    def __unicode__(self):
        return self.name


class Feedback(models.Model):
    comment = models.TextField(u'Коментарий')
    author = models.ForeignKey(User)
    created = models.DateTimeField(u'Дата публикации', auto_now_add=True)
    published = models.BooleanField(default=False)

    def __unicode__(self):
        return self.author.get_full_name()
        
# Название
# Slug
# created
# modified
# главная фотка
# Теги
# График работы
# Адрес
# краткое описание
# полное описание
# комменты