from django.views.generic.simple import direct_to_template
from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf.urls.static import static
import settings
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'frontend.views.home'),                       
    url(r'^survey', direct_to_template, {'template': 'survey.html'}),
    url(r'^location', direct_to_template, {'template': 'location.html'}),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^feedback/', include('feedback.urls')),
    url(r'^backend/', include('backend.urls')),                      
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^login/$', 'backend.views.create_search_profile'),                       
    url(r'^accounts/', include('registration.urls')),                       
)

urlpatterns += patterns('django.contrib.staticfiles.views',
    url(r'^static/(?P<path>.*)$', 'serve', kwargs={"insecure": True}),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


