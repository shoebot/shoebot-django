import shoebot_demos

from django.conf.urls import patterns, include, url

from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'shoebot_demos.views.bot', name='home'),
)
