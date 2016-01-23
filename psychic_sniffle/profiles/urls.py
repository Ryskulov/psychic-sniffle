"""urlconf for the base application"""

from django.conf.urls import url
from profiles import views

urlpatterns = [
    url(r'^$', views.profile),
    url(r'^profile_edit/$', views.profile_edit),
]
