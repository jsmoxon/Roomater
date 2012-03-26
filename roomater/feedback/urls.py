from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('feedback.views',
    url(r'^$', 'feedback_index'), 
    url(r'^(?P<survey_id>\d+)/$', 'feedback_detail'),
    url(r'^(?P<survey_id>\d+)/responses/$', 'feedback_responses'),
    url(r'^(?P<survey_id>\d+)/vote/$', 'feedback_vote'),

    url(r'feedback/$', 'index'),
    url(r'feedback/(?P<poll_id>\d+)/$', 'detail'),
    url(r'feedback/(?P<poll_id>\d+)/results/$', 'results'),
    url(r'feedback/(?P<poll_id>\d+)/vote/$', 'vote'),


)