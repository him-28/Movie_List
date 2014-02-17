import settings

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponseRedirect
from movies.views import load

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', lambda r : HttpResponseRedirect('movie_list/')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<addr>.*)$', load, {}),
)
