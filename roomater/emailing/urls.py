from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^remove/(?P<survey_id>\d+)/(?P<user_id>\d+)/', 'emailing.views.remove_and_email_applicant'),
)

urlpatterns += patterns('django.contrib.staticfiles.views',
    url(r'^static/(?P<path>.*)$', 'serve', kwargs={"insecure": True}),
)
