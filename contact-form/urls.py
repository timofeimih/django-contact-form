from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
import contactForm.views

urlpatterns = patterns('',
  url(r'^contacts/', 'contactForm.views.contactview'),
)
