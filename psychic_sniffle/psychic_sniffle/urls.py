""" Default urlconf for psychicSniffle """

from django.conf.urls import include, url
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf.urls.static import static

admin.autodiscover()


def bad(request):
    """ Simulates a server error """
    1 / 0


urlpatterns = [
    url(r'', include('base.urls')),
    url(r'^place/', include('place.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^profiles/', include('profiles.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bad/$', bad),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +\
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
