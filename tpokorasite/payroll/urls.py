#!/usr/bin/env python
from django.conf.urls import patterns, url
from payroll import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^(?P<param>\D*)/$', views.mainSite, name='mainSite'),
    url(r'^customers/batch$', views.customerBatch, name='customerBatch'),
    url(r'^suppliers/batch$', views.supplierBatch, name='suppliersBatch'),
)
