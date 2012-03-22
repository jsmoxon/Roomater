from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, Context, loader
from django.core.urlresolvers import reverse
from feedback.models import *

def index(request):
    survey_list = Survey.objects.all().order_by('-pub_date')[:5]
    for survey in survey_list:
        return choice_list = survey.choice_set.get(pk=survey.id)
    return render_to_response('feedback_survey.html', {'survey_list': survey_list}, {'choice_list': choice_list},)



def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)
"""
# vote takes 2 arguments: the http request and the id associated with the radio button
def vote(request, poll_id):
# set p as the Poll object whose primary key is that poll_id
    p = get_object_or_404(Poll, pk=poll_id)
# request.POST is a dictionary-like object that lets me access data by key name
# returns the ID of the selected choice as a string
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('djangodetail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('feedback.views.results', args=(p.id,)))
"""

def vote(request, survey_id):
    s = get_object_or_404(Survey, pk=survey_id)
    try:
        selected_option = s.option_set.get(pk=request.POST['option'])
    except (KeyError, Option.DoesNotExist):
        return render_to_response('feedback_survey.html', {
            'survey': s,
            'error_message': "You didn't opt for any of the options!",
            }, context_instance=RequestContext(request))
    else:
        selected_option.votes += 1
        selected_option.save()
        return HttpResponseRedirect(reverse('feedback.views.feedback_results', args=(s.id,)))


def feedback_results(request, survey_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)
