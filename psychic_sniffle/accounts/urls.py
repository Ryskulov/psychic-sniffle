"""urlconf for the base application"""

from django.conf.urls import url
from accounts import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^new_acc/$', views.signup, name='accounts'),
    url(r'^signin/$', views.signin, name='signin'),
]
