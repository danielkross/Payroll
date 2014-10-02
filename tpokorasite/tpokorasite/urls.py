from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tpokorasite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('payroll.urls', namespace='payroll')),
    url(r'^admin/', include(admin.site.urls)),
)
