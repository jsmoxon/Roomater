from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('feedback.views',
    url(r'^$', 'index'),
    #url(r'^$', 'feedback_survey'),
    url(r'^(?P<survey_id>\d+)/$', 'detail'),
    #url(r'^(?P<poll_id>\d+)/results/$', 'results'),
    url(r'^(?P<survey_id>\d+)/results/$', 'feedback_results'),
    url(r'^(?P<survey_id>\d+)/vote/$', 'vote'),
)

