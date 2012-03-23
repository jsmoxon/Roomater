from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, Context, loader
from django.core.urlresolvers import reverse
from feedback.models import *

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render_to_response('djangopoll.html', {'latest_poll_list': latest_poll_list})

def detail(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('djangodetail.html', {'poll': p},
                               context_instance=RequestContext(request))

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
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


def results(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('djangoresults.html', {'poll': p})

# Following the index example
def feedback_index(request):
    survey_list = Survey.objects.all().order_by('-pub_date')[:5]
    return render_to_response('feedback_index.html', {'survey_list': survey_list})

# Following the detail example
def feedback_detail(request, survey_id):
    s = get_object_or_404(Survey, pk=survey_id)
    return render_to_response('feedback_detail.html', {'survey': s}, 
                                context_instance=RequestContext(request))

# Following the vote example
def feedback_vote(request, survey_id):
    s = get_object_or_404(Survey, pk=survey_id)
    try: 
        selected_option = s.option_set.get(pk=request.POST['option'])
    except (KeyError, Option.DoesNotExist):
        return render_to_response('feedback_detail.html', {
            'survey': s,
            'error_message': "You didn't opt for any option, you little ruffian! Try again:",
        }, context_instance=RequestContext(request))
    else:
        selected_option.votes += 1
        selected_option.save()
        return HttpResponseRedirect(reverse('feedback.views.feedback_responses', args=(s.id,)))

# following the results example
def feedback_responses(request, survey_id):
    s = get_object_or_404(Survey, pk=survey_id)
    return render_to_response('feedback_responses.html', {'survey': s})



#REVIEW:
# RequestContext, Context, reverse
