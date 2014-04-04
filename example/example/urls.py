import shoebot_demos

from django.conf.urls import patterns, include, url
from django.http import HttpResponse

from django.contrib import admin

urlpatterns = patterns('',    
    url(r'^$', 'shoebot_demos.views.index', name='home'),
    url(r'^bots/(?P<filename>[\w.]{0,256})$', 'shoebot_demos.views.bot', name='bot'),
)
