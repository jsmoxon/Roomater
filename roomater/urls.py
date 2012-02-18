from django.views.generic.simple import direct_to_template

from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'frontend.views.home'),                       
    url(r'^survey', direct_to_template, {'template': 'survey.html'}),
    url(r'^location', direct_to_template, {'template': 'location.html'}),
    # Examples:
    # url(r'^$', 'roomater.views.home', name='home'),
    # url(r'^roomater/', include('roomater.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.contrib.staticfiles.views',
    url(r'^static/(?P<path>.*)$', 'serve', kwargs={"insecure": True}),
)
