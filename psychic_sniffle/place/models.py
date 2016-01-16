# -*- coding: utf-8 -*- 
from __future__ import unicode_literals

from django.db import models


class PlaceTag(models.Model):
    name = models.CharField(u'Название', max_length=255)

class Place(models.Model):
    name = models.CharField(u'Название ', max_length=30)
    slug = models.SlugField(u'ССЫЛКА???')
    created = models.DateTimeField(u'Дата регистрации: ', auto_now_add=True)
    modified = models.DateTimeField(u'Дата изменения: ', auto_now=True)
    main_foto = models.ImageField(u'Фотография заведения', upload_to='media/')
    tags = models.ManyToManyField(PlaceTag, related_name="place" )
    work_time = models.CharField(u'График работы', max_length=100)
    adress = models.CharField(u'Адрес', max_length=100)
    short_description = models.TextField(u'Краткое описание')
    description = models.TextField(u'Полное описание')
    


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