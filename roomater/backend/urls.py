from django.views.generic.simple import direct_to_template
from django.conf.urls.defaults import patterns, include, url
from backend.views import AddResponseView
from django.contrib import admin
from django.conf.urls.static import static
import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'dash/', 'backend.views.dash'),
    url(r'^index/(?P<entry_id>\d+)/$', 'backend.views.index'),
    url(r'^create_survey', 'backend.views.create_survey'),
    url(r'^submit_create_survey', 'backend.views.submit_create_survey'),
    url(r'^real_survey/(?P<entry_id>\d+)/$', 'backend.views.display_survey'),
    url(r'^submit/(?P<entry_id>\d+)/', 'backend.views.submit_survey'),
)

urlpatterns += patterns('django.contrib.staticfiles.views',
    url(r'^static/(?P<path>.*)$', 'serve', kwargs={"insecure": True}),
)
