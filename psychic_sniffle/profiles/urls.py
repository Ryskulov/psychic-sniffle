"""urlconf for the base application"""

from django.conf.urls import url
from profiles import views

urlpatterns = [
    url(r'^profile_detail_public/(?P<username>\S+)/$', views.profile_detail_public, name='profile_detail_public'),
    url(r'^profile_detail_private/$', views.profile_detail_private, name='profile_detail_private'),
    url(r'^profile_edit/$', views.profile_edit),
]
