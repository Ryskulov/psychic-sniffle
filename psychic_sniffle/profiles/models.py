# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django_comments.models import Comment
from place.models import Place # Внимание !!!





class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=u'Пользователь')
    avatar = models.ImageField(u'Фотография пользователя', upload_to='upload/avatar_pic/', blank=True, null=True)
    first_name = models.CharField(u'Имя', max_length=255)
    last_name = models.CharField(u'Фамилия', max_length=255)
    birthday = models.DateField(u'День рождения', blank=True, null=True)
    status = models.CharField(u'Статус', max_length=255, blank=True, null=True)
    phone = models.CharField(u'Мобильный телефон', max_length=30, blank=True, null=True)
    slug = models.SlugField(unique=True)
    create_add = models.DateTimeField(u'Профиль был создан: ', auto_now_add=True)
    favorites = models.ManyToManyField(Place) # Внимание !!!


    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()


    def __unicode__(self):
        return self.user.username


@receiver(post_save, sender=User, dispatch_uid="create_profile")
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)


@receiver(post_save, sender=Comment, dispatch_uid="comment_mail_send")
def comment_mail_send(sender, instance, created, **kwargs):
    sg = sendgrid.SendGridClient('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')

    message = sendgrid.Mail(to='perfect_nur@mail.ru', subject='Example', html='<img src="https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=imgres&cd=&cad=rja&uact=8&ved=0ahUKEwjEqczl59bKAhWB33IKHWWuAFQQjRwICTAA&url=http%3A%2F%2Fgoodnewsanimal.ru%2Fnews%2Fdom_bez_koshki_dom_bez_schastja%2F2013-11-04-3799&psig=AFQjCNF2_Rej-DvtOQHl75I49lDZPmQixA&ust=1454424548242839">', text='Body', from_email='mi@besmart.kz')
    status, msg = sg.send(message)
