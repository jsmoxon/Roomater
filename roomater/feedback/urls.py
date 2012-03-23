from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('feedback.views',
    url(r'^$', 'index'),
    url(r'^(?P<poll_id>\d+)/$', 'detail'),
    url(r'^(?P<poll_id>\d+)/results/$', 'results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),

    url(r'feedback/$', 'feedback_index'), 
    url(r'feedback/(?P<survey_id>\d+)/$', 'feedback_detail'),
    url(r'feedback/(?P<survey_id>\d+)/responses/$', 'feedback_responses'),
    url(r'feedback/(?P<survey_id>\d+)/vote/$', 'feedback_vote'),
)

