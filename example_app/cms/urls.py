from __future__ import absolute_import

from django.conf.urls import patterns, url

from .views import *

urlpatterns = patterns(
    "",
    url(r'^$', home),
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    )
