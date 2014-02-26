from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *


urlpatterns = patterns('',
  url(r'^contacts/', 'contact-form.views.contactview'),
)
