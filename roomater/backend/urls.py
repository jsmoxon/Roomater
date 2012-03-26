from django.views.generic.simple import direct_to_template
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', direct_to_template, {'template':'home_screen.html'}),                       
    url(r'^dash/', 'backend.views.dash'),
    url(r'^rooms', 'backend.views.list_of_surveys'),
    url(r'^list_room', 'backend.views.create_survey', name='create_survey'),
    url(r'^profile', 'backend.views.create_search_profile', name='profile'),
    url(r'^submit_create_survey', 'backend.views.submit_create_survey'),
    url(r'^room/(?P<entry_id>\d+)/$', 'backend.views.display_survey'),
    url(r'^submit/(?P<entry_id>\d+)/', 'backend.views.submit_survey'),
)

urlpatterns += patterns('django.contrib.staticfiles.views',
    url(r'^static/(?P<path>.*)$', 'serve', kwargs={"insecure": True}),
)
