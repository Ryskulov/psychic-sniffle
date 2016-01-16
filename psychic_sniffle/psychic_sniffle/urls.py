""" Default urlconf for psychicSniffle """

from django.conf.urls import include, url
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib import admin

admin.autodiscover()


def bad(request):
    """ Simulates a server error """
    1 / 0


urlpatterns = [
    url(r'', include('base.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bad/$', bad),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
