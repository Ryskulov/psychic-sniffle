"""urlconf for the base application"""

from django.conf.urls import url
from place import views


urlpatterns = [
    url(r'^$', views.show_list, name='show_list'),
    url(r'^s/$', views.search, name='search'),
]
