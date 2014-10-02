#!/usr/bin/env python
from django.conf.urls import patterns, url
from payroll import views

urlpatterns = patterns('',
    url(r'^$', views.mainSite, name='index'),                       
)
